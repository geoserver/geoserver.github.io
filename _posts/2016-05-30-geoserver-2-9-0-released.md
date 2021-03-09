---
author: jgarnett
comments: true
date: 2016-05-30 21:20:39+00:00
layout: post
link: http://blog.geoserver.org/2016/05/30/geoserver-2-9-0-released/
slug: geoserver-2-9-0-released
title: GeoServer 2.9.0 Released
wordpress_id: 2637
categories:
- Announcements
tags:
- release
- stable
---

The GeoServer team is overjoyed to announce the GeoServer 2.9.0 release. Downloads are available ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.0/geoserver-2.9.0-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.0/geoserver-2.9.0-war.zip/download), [dmg](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.0/geoserver-2.9.0.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.0/geoserver-2.9.0.exe/download)) along with docs and extensions. We will be working with OSGeo to provide a signed DMG download shortly.

This release is made by Jody Garnett (Boundless) and Devon Tucker (Boundless) with help from Andrea Aime and Alessandro Parma (GeoSolutions) in conjunction with the GeoWebCache 1.9.0 and GeoTools 15.0 releases.

For more information on this release check the release notes ([2.9.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=13003)|[RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=12502)|[beta2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=12700)|[beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=12100), [M0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=11401)).

[![GeoServer 2.9.0](/img/uploads/2.9.0-about-e1464386798600.png)](/img/uploads/2.9.0-about-e1464386798600.png)


## Highlights


As this is a major release GeoServer 2.9.0 includes a number of important changes, including both new features and compatibility requirements.


### Java 8 Required


This release requires the use of Java 8, and is compatible with both Oracle JDK and Open JDK.

[![Java 8 Required](/img/uploads/2.9.0-java8.png)](/img/uploads/2.9.0-java8.png)


### Servlet 3 Required


Due to internal upgrades GeoServer now requires a Servlet 3 compatible application server.



 	
  * The standalone downloads for Mac, Windows and Linux has been update to [Jetty 9.2.13](http://download.eclipse.org/jetty/updates/jetty-bundles-9.x/9.2.13.v20150730/)

 	
  * Tomcat users will be required to upgrade to Tomcat 7 or newer (for those doing a WAR install)




### Web Administration


A number of improvements and clarifications have been made to the web administration application:



 	
  * The [Layers](http://docs.geoserver.org/stable/en/user/data/webadmin/layers.html#data-webadmin-layers) and [Layer Preview](http://docs.geoserver.org/stable/en/user/data/webadmin/layerpreview.html) has been restructured to lead with layer title in the first column, layer workspace and name combined into the second column. By popular request these pages now use layer (rather than resource) actions with "Add a new layer", and "Remove selected layers".
[![Layers Page](/img/uploads/2.9.0-layers.png)](/img/uploads/2.9.0-layers.png)

 	
  * You can now [generate layer bounds](http://docs.geoserver.org/stable/en/user/data/webadmin/layers.html#bounding-boxes) from either the data bounds or from the spatial reference system bounds. This is handy for dynamic layers that will have content added to them over time.
[![2.9.0-srs-bounds](/img/uploads/2.9.0-srs-bounds.png)](/img/uploads/2.9.0-srs-bounds.png)

 	
  * Styles can now include an [optional legend graphic](http://docs.geoserver.org/stable/en/user/data/webadmin/styles.html#add-a-legend) for use in WMS GetCapabilities.
[![2.9.0-legend](/img/uploads/2.9.0-legend.png)](/img/uploads/2.9.0-legend.png)

 	
  * [Global Settings](http://docs.geoserver.org/stable/en/user/configuration/globalsettings.html#config-globalsettings) have been grouped into a section for configuration of web services and a section for internal settings (affecting the GeoServer application as a whole).

 	
  * [Image Processing](http://docs.geoserver.org/stable/en/user/configuration/image_processing/index.html#jai) and [Raster Access](http://docs.geoserver.org/stable/en/user/configuration/raster_access.html#config-converageaccess) are clearly presented with controls for memory and CPU use. Previously these screens were expressed in terms of the internal components used.
[![image_processing.png](/img/uploads/image_processing.png)](/img/uploads/image_processing.png)




### User Guide


The user guide has been restructured:



 	
  * The [document layout](http://docs.geoserver.org/stable/en/user/index.html) has been reduced to a smaller number of sections

 	
    * [Data management](http://docs.geoserver.org/latest/en/user/data/index.html) covers vector, raster, database and web services along with common settings

 	
    * [Services](http://docs.geoserver.org/stable/en/user/services/index.html#services) (WMS, WFS, WCS, WPS, CSW) have been gathered into a single section for consistency, even though WPS is an optional install.




 	
  * The duplication between service description and application configuration has been resolved:

 	
    * Each Service is described, both in terms of functionality, alongside details on how the service is configured

 	
    * The [Web administration interface](http://docs.geoserver.org/stable/en/user/webadmin/index.html) section remains focused on on application configuration, linking to to service configuration above (to prevent duplication).




 	
  * [Tutorials](http://docs.geoserver.org/latest/en/user/tutorials/index.html) have been gathered into a single location.




### Resource REST API


A new feature for GeoServer 2.9 is the ability to [manage resources](http://docs.geoserver.org/stable/en/user/rest/api/resources.html) (icons, fonts, configuration files) via the REST API.  This approach works with both the default file based GeoServer configuration and JDBCConfig community module.



 	
  * **GET: rest/resource/styles/grass_fill.png?
![](https://raw.githubusercontent.com/geoserver/geoserver/master/data/release/styles/grass_fill.png)
**

 	
  * **GET: rest/resource/styles/grass_fill.png?operation=metadata&format=json**

    
    {  "ResourceMetadata":  {
         "name": "grass_fill.png",
         "parent": {
           "path": "/styles",
           "link": {
              "href": "http://localhost:8080/geoserver/rest/resource/styles",
              "rel": "alternate",
              "type": "application/json"
           }
         },
         "lastModified": "2016-05-27 19:31:30.0 UTC",
         "type": "resource"
       }
    }








### About/Status REST API


The about REST API already reports on the jars installed and the version of high-level components. GeoServer 2.9 includes the addition of [about/status](http://docs.geoserver.org/stable/en/user/rest/api/manifests.html#about-status-format) which reports not only what components are installed, but if they are correctly functioning. We will be working with this endpoint in subsequent releases to better reporting on GeoServer installation status.



 	
  * **GET rest/about/status**


[![2.9.0-status](/img/uploads/2.9.0-status.png)](/img/uploads/2.9.0-status.png)


### Offset line support


[Symbology Encoding 1.0 offset line is now supported](http://docs.geoserver.org/latest/en/user/styling/sld-reference/linesymbolizer.html#offsetting-lines), along with a vendor extension to use the same in SLD 1.0, and CSS support via the ["stroke-offset" property](http://docs.geoserver.org/stable/en/user/extensions/css/properties.html#line-symbology). Here are a couple of screenshots of the effects that can be achieved by using offset line.

[![line_offset1](/img/uploads/line_offset1-300x225.png)](/img/uploads/line_offset1.png)

[![polygon_offset1](/img/uploads/polygon_offset1-300x225.png)](/img/uploads/polygon_offset1.png)


### UTFGrid support in WMS and WMTS


GeoServer [WMS and WMTS](http://docs.geoserver.org/latest/en/user/services/wms/outputformats.html) now support [UTFGrid](https://github.com/mapbox/utfgrid-spec/blob/master/1.3/utfgrid.md) as an output format, to get fast and rich feature info on the client side. The WMS output has been tested with OpenLayers 2 by applying [this patch](https://github.com/openlayers/ol2/pull/1486), while not officially tested it should also work with OpenLayers 3 and Leaflet using the appropriate URL templates against the WMTS output.

[![Selezione_208](/img/uploads/Selezione_208-300x269.png)](/img/uploads/Selezione_208.png)




### Improved WPS aggregation process with group by


The Aggregate process has been improved to support group-by against any data source, with the ability to turn the execution in an efficient SQL with group by query, if the underlying data source is a database. In case of group-by a rich JSON output is generated, than can then be used to drive client side libraries such as D3 to generate nice charts for your users:

    
    {
      "GroupByAttributes": [ "groupingAttribute" ],
      "AggregationResults": [
        [ "Class1", 18 ],
        [ "Class2", 1 ],
        [ "Class3", 3 ],
        [ "Class4", 3 ]
      ],
      "AggregationFunctions": [ "Count" ],
      "AggregationAttribute": "countingAttribute"
    }


[![Selezione_210](/img/uploads/Selezione_210-300x157.png)](/img/uploads/Selezione_210.png)




### Vector masking support for GDAL based formats


All GDAL based formats now support vector masks to cut NODATA areas away from rendering, similar to what image mosaic already supported. Here is a sample, cutting away some areas from a JPEG 2000 image (the format adds compression artifacts at the border, thus the input transparent color cannot be used to achieve a similar effect).

[![masking](/img/uploads/masking-300x276.png)](/img/uploads/masking.png)

[![gdalmasks](/img/uploads/gdalmasks.png)](/img/uploads/gdalmasks.png)




### Internal Upgrades


Internally GeoServer has received a number of important upgrades:



 	
  * **Update to Spring 4:** The upgrade to Spring 4 is responsible for the delay of the GeoServer 2.9 and was required for Java 8 compatibility. This upgrade was far reaching with both  the REST-API and Security integration requiring a concerted quality assurance effort on geoserver-devel.
This upgrade was technically challenging resulting in a delay to the 2.9 release schedule. Thanks to everyone who helped out, beta testers, and Justin, Andrea and Niels for tackling the harder issues.

 	
  * **Upgrade to JAI-EXT to 1.0.9:** To enable JAI-EXT use startup parameter org.geotools.coverage.jaiext.enabled=true (for more information see [Image Processing](http://docs.geoserver.org/stable/en/user/configuration/image_processing/index.html#jai-ext) in the user guide).
[![](/img/uploads/JAIEXTops.png)](http://docs.geoserver.org/stable/en/user/configuration/image_processing/index.html#jai-ext)

 	
  * **Upgrade to Wicket 7: **The web administration application has been updated to use the latest Wicket library, thanks to a larger team effort. We would like to thank the sponsors of the [Wicket 7 upgrade](https://wiki.osgeo.org/wiki/GeoServer_Code_Sprint_2016) sprint: [OSGeo](http://www.osgeo.org/), [Boundless](http://boundlessgeo.com/), [Vivid Solutions](http://www.vividsolutions.com/), [How 2 Map](http://www.how2map.com/), [San Jose Water Company](https://www.sjwater.com/), [Transient](http://transient.nz/), [Geobeyond](http://www.geobeyond.it/) (with in-kind sponsors GeoSolutions, CCRi, Astun Technology and Voyager).
[![Can you see the difference? Neither can we.](/img/uploads/Wicket-upgrade.png)](/img/uploads/Wicket-upgrade.png)

 	
  * The GeoServer **default data directory has been updated** with titles and descriptions for many layers (to better take advantage of the user interface improvements). The previously disabled **Pk50095** layer (shown below) is now enabled by default.
[![Pk50095](/img/uploads/2.9.0-Pk50095.png)](/img/uploads/2.9.0-Pk50095.png)




## About GeoServer 2.9


Articles, docs, blog posts and presentations:



 	
  * Internals [upgrade to spring-4](https://github.com/geoserver/geoserver/wiki/Spring-4-Upgrade) for Java 8 compatibility (User Guide)

 	
  * [GeoServer code sprint success](http://blog.geoserver.org/2016/01/25/geoserver-code-sprint-success/) and [wicket migration code sprint](https://github.com/geoserver/geoserver/wiki/Wicket-migration-code-sprint) (GeoServer Blog)

 	
  * [GeoServer Plugin for QGIS](http://blog.geoserver.org/2015/12/23/geoserver-explorer-plugin-for-qgis/) (Boundless)

 	
  * [Simplify complex feature mappings setup with HALE](http://www.geo-solutions.it/blog/inspire-support-in-geoserver-made-easy-with-hale/) (GeoSolutions)

 	
  * [REST management of Resources](http://docs.geoserver.org/stable/en/user/rest/api/resources.html) (User Guide)




## 
