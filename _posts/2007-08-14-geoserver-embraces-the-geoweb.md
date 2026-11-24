---
author: Chris Holmes
comments: true
date: 2007-08-14 16:12:21+00:00
layout: post
link: http://blog.geoserver.org/2007/08/14/geoserver-embraces-the-geoweb/
slug: geoserver-embraces-the-geoweb
title: GeoServer embraces the GeoWeb
wordpress_id: 66
categories:
- Announcements
---

We are pleased to announce the release of GeoServer 1.5.3.  This version represents the culmination of a ton of hard work to make GeoServer more compatible with the new formats gaining great popularity in the rapidly expanding geo world.  Foremost among the improvements is a number of advances in our [support for Google Earth](https://web.archive.org/web/20070814/http://docs.codehaus.org/display/GEOSDOC/Google+Earth).  KML, the format understood by Google Earth, has been available from GeoServer for awhile.  But our implementation wasn't flexible enough to make good looking maps and to take advantage of the advanced features of the format.  That has all changed, with better default styling, [custom placemarks from templates](https://web.archive.org/web/20070814/http://docs.codehaus.org/display/GEOSDOC/01-Placemark+Templates), support for '[Super-Overlays'](https://web.archive.org/web/20070814/http://docs.codehaus.org/display/GEOSDOC/05-KML+Super+Overlays) and [Time](https://web.archive.org/web/20070814/http://docs.codehaus.org/display/GEOSDOC/02-Time+Templates), and automatic [generation of legend](https://web.archive.org/web/20070814/http://docs.codehaus.org/display/GEOSDOC/04-Legend+Overlays) information.  There is also experimental support for [referencing an existing cache](https://web.archive.org/web/20070814/http://docs.codehaus.org/display/GEOSDOC/03-Super+Overlays+and+TileCache) of tiles to use in a Super-Overlay.  The ability to style one's 2d map and get the same output in Google Earth has also improved dramatically, as it now picks up proper scale elements.

The other big announcement is support for [GeoRSS](https://web.archive.org/web/20070814/http://docs.codehaus.org/display/GEOSDOC/GeoRSS), which allows GeoServer data to also be served on Virtual Earth and Yahoo! Maps.  The GeoRSS output can pick up the same pop-up templates as KML, so again you just have to configure your data once and it's available on a number of different formats.   With a bit of coding from Andrea we're also now shipping with support for the map projection used by Virtual Earth and Google Maps, thanks to [SharpGIS](http://www.sharpgis.net/2007/07/27/TheMicrosoftLiveMapsAndGoogleMapsProjection.aspx) and [Chris Schmidt](http://crschmidt.net/blog/archives/238/understanding-googles-projection-slightly-anyway/).   So now if you use [900913](http://crschmidt.net/blog/archives/243/google-projection-900913/) as the EPSG code for your WMS requests our output will be perfectly overlaid on those maps.  The final new web-friendly format is [GeoJSON](http://geojson.org).  This is not part of the main distribution yet, but you can [download the plug-in](http://downloads.sourceforge.net/geoserver/geojson-1.0-RC1.zip), which is easy to add to a GeoServer instance.  JSON is a smaller format than GML, and [early reports](http://ctuot.twoday.net/stories/4132499/) have it coming down faster with less overall size for the same dataset.

The other efficiency improvement is support for [paletted images](https://web.archive.org/web/20070814/http://docs.codehaus.org/display/GEOSDOC/Paletted+images+tutorial), which allows very quick generation of images like png8 and gif that are much smaller in size than our normal output.  This is very useful in situations with low bandwidth, and indeed with tile caching the size of the tiles becomes one of the biggest speed bottlenecks.

The final piece worth mentioning is advances in our Oracle support.  Thanks goes to [JDi Solutions](http://jdi-solutions.co.uk/) for funding [The Open Planning Project](http://topp.openplans.org) to perform the work.  Oracle in GeoServer can now handle full WFS-T transactions against all coordinate reference systems.  There have also been a few nice speed improvements with Oracle as well.  Thanks to all the users and contributors who helped out with testing and feature suggestions, this project would not be possible without all of you.

----

GeoServer 1.5.3 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/). [Announcement](http://blog.geoserver.org/2007/08/14/geoserver-embraces-the-geoweb/) on the [GeoServer Blog](http://blog.geoserver.org). SourceForge Release 532090

- [Release Notes](#release-notes)
- [geoserver-1.5.3.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/geoserver-1.5.3.exe/download)
- [geoserver-1.5.3-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/geoserver-1.5.3-bin.zip/download)
- [geoserver-1.5.3-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/geoserver-1.5.3-src.zip/download)
- [geoserver-1.5.3-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/geoserver-1.5.3-war.zip/download)
- [geoserver-1.5.3-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/geoserver-1.5.3-doc.zip/download)
- [geoserver-1.5.3-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/geoserver-1.5.3-javadoc.zip/download)
- [Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/extensions/)

#### DataStore Extensions

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/extensions/geoserver-1.5.3-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/extensions/geoserver-1.5.3-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/extensions/geoserver-1.5.3-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/extensions/geoserver-1.5.3-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/extensions/geoserver-1.5.3-vpf-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/extensions/geoserver-1.5.3-wfs-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/extensions/geoserver-1.5.3-oracle-plugin.zip/download)

#### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.3/extensions/geoserver-1.5.3-pyramid-plugin.zip/download)

#### Output Format Extensions

- [GeoJSON](http://downloads.sourceforge.net/geoserver/geojson-1.0-RC1.zip) (RC1)

Tested with: Jetty, Tomcat

## Release notes

Improvement:

* [GEOS-1118](https://osgeo-org.atlassian.net/browse/GEOS-1118) The wms-gs-1_0_1.js library doesn't take SLD parameter into account
* [GEOS-1274](https://osgeo-org.atlassian.net/browse/GEOS-1274) KML polygons should have borders by default (like before)
* [GEOS-1275](https://osgeo-org.atlassian.net/browse/GEOS-1275) Default text color for KML should be white
* [GEOS-1277](https://osgeo-org.atlassian.net/browse/GEOS-1277) Use 900913 for gs-wms.js, to help promote that value

Bug:

* [GEOS-1271](https://osgeo-org.atlassian.net/browse/GEOS-1271) georss output does not work with shorthand, or without being url encoded
* [GEOS-1272](https://osgeo-org.atlassian.net/browse/GEOS-1272) georss output ignores bounding box
* [GEOS-1273](https://osgeo-org.atlassian.net/browse/GEOS-1273) atom rss producer should declare georss namespace mapping
* [GEOS-1278](https://osgeo-org.atlassian.net/browse/GEOS-1278) wfs:Delete does not work anymore with Oracle Datastore since 1.5.2
* [GEOS-1286](https://osgeo-org.atlassian.net/browse/GEOS-1286) Coverage configuration form allows pure SRS number to be inputed, but all of the code expects EPSG:XXXX instead
