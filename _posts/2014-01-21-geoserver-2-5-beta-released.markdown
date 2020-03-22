---
author: geoserver
comments: true
date: 2014-01-21 08:59:15+00:00
layout: post
link: http://blog.geoserver.org/2014/01/21/geoserver-2-5-beta-released/
slug: geoserver-2-5-beta-released
title: GeoServer 2.5-beta released
wordpress_id: 1753
---

GeoServer team is pleased to announce the release of [GeoServer 2.5-beta](http://geoserver.org/display/GEOS/GeoServer+2.5-beta).

This release is packed with new features and interesting new extensions. Here is some reason why you should try 2.5.-beta.

**WCS 2.0 and WCS 2.0 EO**

GeoServer 2.5 is now shipping with WCS 2.0 as  a core module, a major improvement in terms of usability compared to both WCS 1.0 and WCS 1.1. For example, getting back the full raster is now as easy as:




http://localhost:8080/geoserver/wcs?request=GetCoverage&service=WCS&version=2.0.1&coverageId=nurc__Img_Sample

while getting the same, but with half the size, can be achieved using:

    
    http://localhost:8080/geoserver/wcs?request=GetCoverage&service=WCS&version=2.0.1&coverageId=nurc__Img_Sample&scaleFactor=0.5


Paired with the WCS 2.0 module we have the WCS 2.0 Earth Observation (EO) extension, which adds the ability to expose the time dimension using standard extensions to the base WCS 2.0 protocol.
We'd like to thank DLR and EUMESAT for sponsoring this work, and GeoSolutions for carrying it out on their behalf.

**Batch layer importer extension**

A new extension that allows for batch import of data, dubbed "the importer", is now also available. It supplements the existing GeoServer ui by adding a much more convenient workflow for layer configuration. For example previously configuring multiple Shapefiles (or multiple PostGIS tables) required users to tediously configure one by one. With the importer it can achieved with a few easy to follow steps. The importer is accessible from both the web ui and a REST api, making it easy to use in a variety of environments.


[![](http://geoserver.wpengine.com/wp-content/uploads/2014/01/Selezione_0561.png)](http://blog.geoserver.org/2014/01/21/geoserver-2-5-beta-released/selezione_056/)


The importer also allows for consumption of formats that GeoServer does not support natively. Formats such as KML and CSV can be conveniently ingested into an existing data formats such as PostGIS and be efficiently served.

The importer was developed and contributed by Boundless. A special thanks to them and the [MapStory](http://mapstory.org/) project for providing most of the funding and requirements for the extension.

**WMS performance and quality improvements**




Going back to pre-existing protocols, let's have a look at WMS.

A new higher performance PNG encoder has been included in GeoServer. Based on the open source [PNGJ library](https://code.google.com/p/pngj/), and with special local optimizations to extract pixels for encoding with minimal overhead, the encoder provides a significant speedup over the encoder included in the JDK (that is, the one you get by default) and also over the ImageIO native extensions one (which is available on selected platforms, and requires you a separate installation). Here are some results comparing map thoughput using the FOSS4G WMS shootout test harness, using Oracle JDK, and then OpenJDK:





### [![](http://geoserver.wpengine.com/wp-content/uploads/2014/01/png_oracleJdk71.png)](http://blog.geoserver.org/2014/01/21/geoserver-2-5-beta-released/png_oraclejdk7/)




_GetMap thoughput over Oracle JDK 7_


[![](http://geoserver.wpengine.com/wp-content/uploads/2014/01/png_jdk71.png)](http://blog.geoserver.org/2014/01/21/geoserver-2-5-beta-released/png_jdk7/)


_GetMap thoughput over OpenJDK7_


Before you get overly excited, remember that this speedups were achieved because the PNG encoding had a major effect on this benchmark, which was drawing maps with rather light contents, if you have maps that take more than 200ms to be rendered the improvement will be difficult to notice by the naked eye (these chart show throughput, to have a reference, the slowest single threaded result in terms of response time was 120ms, for the JDK encoder based results).
The work on this topic was done by Andrea Aime in his spare time, but let's not forget to thank Hernan J. Gonzalez for the all work put in the PNGJ library.

Speaking of performance, if you are building maps with complex geometries on top of a PostGIS database you'll be happy to hear that we're now calling [ST_Simplify](http://www.postgis.org/docs/ST_Simplify.html) to get the geometries be simplified directly in the database, significantly reducing the time spent to transfer them. A benchmark drawing a large number (a few tens of thousands) of complex polygons in a small scale map went up from 7 r/s (requests per second) to 11 r/s (and yes, we made tests showing we are not slowing down when working on simpler geometries). Thanks to Andrea Aime for working on this, and Jonathan Moules for providing the data, styles and benchmark setup that led to this improvement.

And if you're interested in JPEG performance instead, just go and install the newly released JPEG Turbo extension, which allows GeoServer to leverage the excellent work done by the [libjpegturbo](http://libjpeg-turbo.virtualgl.org/) team to speed up JPEG encoding. Here is a benchmark Simone performed on a Windows 64 laptop using a well optimized image mosaic as the source (which notably cannot use the ImageIO native extensions to speed up image encoding):

[![](http://geoserver.wpengine.com/wp-content/uploads/2014/01/jpegturbo11.png)](http://blog.geoserver.org/2014/01/21/geoserver-2-5-beta-released/jpegturbo-2/)

Changing gear, you'll also be pleased to hear that point symbols are now rendered with higher quality and all at the same size/appearance, thanks to pixel precise casting of their position, and that we're suffering from reduced issues at tile borders, even if you don't manually specify a "border"/"gutter" parameter thanks to a much improved estimation of the symbols size (which is performed using static analyisis of the SLD).

**Improved GetFeatureInfo precision**

Most WMS servers available today, including GeoServer 2.4 and earlier, have a pretty simple mechanism to find out what you have clicked on a map:



	
  * decide on a search area, based either on a static configuration, or the size of the biggest symbol in the map being clicked

	
  * do a BBOX search on the data


This is fine and works well if your maps is made of regular symbols, that is, square enough, and more or less having a similar size. But what happens if your map looks like this, what will you get when you click outside of the small circle, or inside the large one? The two "clicks" onthe map below are at the same distance from the center point of the circles, but  one of the two will not work as it should, either you get a positive response from both of them, or no response, whilst you should get a response only with the large circle click.

[![](http://geoserver.wpengine.com/wp-content/uploads/2014/01/Selezione_0531.png)](http://blog.geoserver.org/2014/01/21/geoserver-2-5-beta-released/selezione_053/)

The same goes if you are using irregular point symbols, or if you are using geometry transformations to offset them from the central point location, GetFeautureInfo might not respond as you like when clicking inside the symbol, because it's too far away from the actual geometry.[
](http://blog.geoserver.org/2014/01/21/geoserver-2-5-beta-released/selezione_053/)[![](http://geoserver.wpengine.com/wp-content/uploads/2014/01/Selezione_0551.png)](http://blog.geoserver.org/2014/01/21/geoserver-2-5-beta-released/selezione_055/)

The problem in the end is pretty simple, the commonly used algorithm does not paint the map, so it cannot know how big the symbols will be in the particular area you clicked, nor be informed about their shape. That's what GeoServer 2.5 does instead, it figures out how much of the map it has to paint investigating the largest symbol in the map, and then actually paints it, quickly, to figure out what was actually available in the point you clicked: this way, you'll get only what you actually clicked (well, almost, there is still a small 3px tolerance, so if you click just outside of a circle, you'll get back the info about that circle anyways).

We're pretty excited about this new functionality, and believe you should be too. Let us know how it works on your maps.

Big thanks to the Eskilstuna municipality for funding the improvement, and GeoSolutions for carrying out the work.

**DXF extension**

Have a user base that loves CAD tools? This output format is for you then, it adds DXF output for WFS requests, and also for WPS ones, allowing vector data downloads in this common format. Special thanks to Mauro Bartolomeoli for the initial implementation, and for pushing the module up in supported land.


### **And more**




### The release packs also a hefty number of fixes and improvements that were not backported to the stable series yet, check out the [full release logs](The same goes if you are using irregular point symbols, or if you are using geometry transformations to offset them from the central point location.) for details.


**Let us know how it goes**

This is the beta release for the 2.5 series, and this is where the user community has the best occasion of influencing the 2.5 release by reporting all issues you find in the release. So please, go [download the release](http://geoserver.org/display/GEOS/GeoServer+2.5-beta), try it out, report issues, and help us create, next month, a very good release candidate


