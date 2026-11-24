---
author: Chris Holmes
comments: true
date: 2007-06-06 17:54:25+00:00
layout: post
link: http://blog.geoserver.org/2007/06/06/geoserver-151-ready-for-download/
slug: geoserver-151-ready-for-download
title: GeoServer 1.5.1 ready for download
wordpress_id: 51
categories:
- Announcements
---

The GeoServer team is pleased to announce the latest release in the stable 1.5.x series.  It's great to see GeoServer settling to be a really mature project, as most of the [changes](#release-notes) done for 1.5.1 were actually improvements instead of bug fixes.  The big change is that we're shipping with [OpenLayers](http://openlayers.org) as our default preview and demo application.  And we took a bit of extra time to get GeoServer producing tiles with nice labels by borrowing 'metaTile' ideas from [TileCache](http://labs.metacarta.com/wms-c), creating them on the fly and in memory.  This summer we've got a Google Summer of Code [project](http://code.google.com/soc/osgeo/appinfo.html?csaid=FED722EC29A37BC5) to work on Tile Caching, so soon those tiles will be cached to disk (and distributed about) as well.

The other fun OpenLayers improvement we've got is making it available as an output format.  So instead of


<blockquote>[http://server.org/geoserver/wms?bbox=-13....&Format=image/png](http://localhost:8080/geoserver/wms?bbox=-130,24,-66,50&styles=&request=GetMap&layers=topp:states&width=550&height=250&srs=EPSG:4326&Format=image/png)</blockquote>


You can do


<blockquote>[http://server.org/geoserver/wms?bbox=-13...&Format=application/openlayers](http://localhost:8080/geoserver/wms?bbox=-130,24,-66,50&styles=&request=GetMap&layers=topp:states&width=550&height=250&srs=EPSG:4326&Format=application/openlayers)</blockquote>


and you'll get an interactive OpenLayers map instead of a mere png image.  Just put _**Format=application/openlayers**_ on any WMS request and we'll make an OpenLayers map with it, changing the default parameters as you pass them in.

And if putting in all those WMS values in is too much for you, we've now got a WMS reflector that makes some guesses as to reasonable defaults.  So you can do:


<blockquote>[http://localhost:8080/geoserver/wms/reflect?layers=topp:states  ](http://localhost:8080/geoserver/wms/reflect?layers=topp:states)</blockquote>


The defaults aren't ideal yet, we're hoping to improve them for the next release to be able to derive more defaults, like take in to account the bbox of the dataset.

Past OpenLayers we've got a lot of nice KML improvements.  First up we've got templates, see the [new tutorial](http://docs.codehaus.org/display/GEOSDOC/KML+Placemark+Templates) on this great feature.  We've leveraged the great [FreeMarker](http://freemarker.sourceforge.net/) templating library to give users incredibly powerful control over the output of KML pop-ups.  Soon we'll also make this available to GetFeatureInfo and GeoRSS as well.  Our old pop-ups would just dump attribute information, now users can make use of KML's html features and link in content using the information stored in their geospatial data.

Other KML improvements include [our first crack](http://docs.codehaus.org/display/GEOSDOC/Google+Earth#GoogleEarth-superoverlay) at [SuperOverlays](http://code.google.com/apis/kml/documentation/kml_21tutorial.html#superoverlays), which are easily one of the most powerful features in Google Earth.  We've taken most all the complexity out of them, allowing users to just configure their layers in GeoServer and we'll automatically do the super overlay.  Right now GeoServer generates all data on the fly, but soon we should have a few caching options.  We also have a few other small improvements for KML, like picking up point icons from SLD, a param to [add a Legend](http://docs.codehaus.org/display/GEOSDOC/Google+Earth#GoogleEarth-legend) to Google Earth, and cleaning our output up so it works with Google Maps better.

We've also had some great contributions this release.  Saul Farber of MassGIS has his ArcSDE raster support in pretty good shape, and is looking for users to test it out and give feedback.  If anyone gets it going with Google Earth Superoverlays do let us know.  More details will be on this blog soon. The other nice contributions were translations of the web admin console to Chinese and Portuguese, adding to Spanish, German, Japanese, and French.

Please give us feedback on this release, especially on documentation and the KML improvements.  We're looking to do a big press release  for the next release to highlight the recent work, and hopefully pick up some new users, so want to be sure everything is really tight.

----

GeoServer 1.5.1 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/). SourceForge Release 513796

- [Release Notes](#release-notes)
- [geoserver-1.5.1.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/geoserver-1.5.1.exe/download)
- [geoserver-1.5.1-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/geoserver-1.5.1-bin.zip/download)
- [geoserver-1.5.1-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/geoserver-1.5.1-src.zip/download)
- [geoserver-1.5.1-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/geoserver-1.5.1-war.zip/download)
- [geoserver-1.5.1-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/geoserver-1.5.1-doc.zip/download)
- [geoserver-1.5.1-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/geoserver-1.5.1-javadoc.zip/download)

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/extensions/)

#### DataStore Extensions

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/extensions/geoserver-1.5.1-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/extensions/geoserver-1.5.1-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/extensions/geoserver-1.5.1-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/extensions/geoserver-1.5.1-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/extensions/geoserver-1.5.1-vpf-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/extensions/geoserver-1.5.1-wfs-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/extensions/geoserver-1.5.1-oracle-plugin.zip/download)

#### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.1/extensions/geoserver-1.5.1-pyramid-plugin.zip/download)

Tested with: Jetty, Tomcat

## Release notes

New Feature:

* [GEOS-996](https://osgeo-org.atlassian.net/browse/GEOS-996) add TIME and ELEVATION parameters in a Getmap request

Improvement:

* [GEOS-993](https://osgeo-org.atlassian.net/browse/GEOS-993) Icons for KML placemarks should pick up point SLD stylings
* [GEOS-998](https://osgeo-org.atlassian.net/browse/GEOS-998) Allow WFS to serve features not having a geometry attribute
* [GEOS-1031](https://osgeo-org.atlassian.net/browse/GEOS-1031) replace mapbuilder demos with openlayers
* [GEOS-1032](https://osgeo-org.atlassian.net/browse/GEOS-1032) Only outlines on KML from an SLD
* [GEOS-1034](https://osgeo-org.atlassian.net/browse/GEOS-1034) Support super overlays in GeoServer
* [GEOS-1040](https://osgeo-org.atlassian.net/browse/GEOS-1040) Allow legend support in KML
* [GEOS-1041](https://osgeo-org.atlassian.net/browse/GEOS-1041) Allow JPEG compression level to be user configurable
* [GEOS-1085](https://osgeo-org.atlassian.net/browse/GEOS-1085) Portuguese Translation of GeoServer web admin

Bug:

* [GEOS-747](https://osgeo-org.atlassian.net/browse/GEOS-747) ArcSde datastore not outputting database queries
* [GEOS-1044](https://osgeo-org.atlassian.net/browse/GEOS-1044) Issues with units in Geoserver 1.5.0
* [GEOS-1057](https://osgeo-org.atlassian.net/browse/GEOS-1057) kml produces error is GMaps due to # on colors and NaN in coordinate values
* [GEOS-1059](https://osgeo-org.atlassian.net/browse/GEOS-1059) Handle XML requests without sufficient service/version paramaters apprpriately

Task:

* [GEOS-1056](https://osgeo-org.atlassian.net/browse/GEOS-1056) Chinese translation

Sub-task:

* [GEOS-1073](https://osgeo-org.atlassian.net/browse/GEOS-1073) Replace mapbuilder tazmania demo with openlayers tazmania demo
* [GEOS-1076](https://osgeo-org.atlassian.net/browse/GEOS-1076) Get labels working better with OpenLayers
* [GEOS-1077](https://osgeo-org.atlassian.net/browse/GEOS-1077) Port changes to 1.5.x branch
* [GEOS-1078](https://osgeo-org.atlassian.net/browse/GEOS-1078) Use single file compressed OpenLayers javascript file

Wish:

* [GEOS-1222](https://osgeo-org.atlassian.net/browse/GEOS-1222) visualize my wms file
