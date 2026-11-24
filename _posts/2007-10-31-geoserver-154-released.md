---
author: Gabriel Roldan
comments: true
date: 2007-10-31 04:53:41+00:00
layout: post
link: http://blog.geoserver.org/2007/10/30/geoserver-154-released/
slug: geoserver-154-released
title: GeoServer 1.5.4 Released
wordpress_id: 73
categories:
- Announcements
---

The GeoServer team is pleased to announce the availability of the latest stable release, 1.5.4.

This release mostly cleans up stuff for Google Earth and Maps.  Generated maps now line up perfectly on Google Maps, with a fix to the projection code.  This allows us to replace the Google Maps overlay demo with OpenLayers, so it works with GMaps, Yahoo! Maps and Virtual Earth.  Google Earth will now zoom to the exact location of the dataset, and has further support for 'time' elements.

There are additionally a few improvements for Oracle users, including proper Shapefile output, and the ability to run in an Oracle Application Server.  Also new is Arabic rendering support and fixes for serving additional content through GeoServer.

Full changelog is located [here](#release-notes).

This release is based off the brand new GeoTools 2.3.5 stable release.

Thanks to all the users and contributors who helped out with testing and feature suggestions, this project would not be possible without all of you.

----

GeoServer 1.5.4 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/).[Announcement](http://blog.geoserver.org/2007/10/30/geoserver-154-released/) on the [GeoServer Blog](http://blog.geoserver.org).

SourceForge Release 550759

- [Release Notes](#release-notes)
- [geoserver-1.5.4a.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/geoserver-1.5.4a.exe/download)
- [geoserver-1.5.4a.bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/geoserver-1.5.4a.bin.zip/download)
- [geoserver-1.5.4a.src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/geoserver-1.5.4a.src.zip/download)
- [geoserver-1.5.4a.war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/geoserver-1.5.4a.war.zip/download)
- [geoserver-1.5.4-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/geoserver-1.5.4-doc.zip/download)
- [geoserver-1.5.4-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/geoserver-1.5.4-javadoc.zip/download)

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/extensions/)

#### DataStore Extensions

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/extensions/geoserver-1.5.4-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/extensions/geoserver-1.5.4-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/extensions/geoserver-1.5.4-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/extensions/geoserver-1.5.4-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/extensions/geoserver-1.5.4-vpf-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/extensions/geoserver-1.5.4-wfs-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/extensions/geoserver-1.5.4-oracle-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.4/extensions/geoserver-1.5.4-wfs-plugin.zip/download)

Tested with: Jetty, Tomcat, OC4J

## Release notes

Improvement:

* [GEOS-1063](https://osgeo-org.atlassian.net/browse/GEOS-1063) KML with Time
* [GEOS-1240](https://osgeo-org.atlassian.net/browse/GEOS-1240) Make a good LookAt for KML layers
* [GEOS-1313](https://osgeo-org.atlassian.net/browse/GEOS-1313) Use the DB for filtering object for GetFeatureInfo
* [GEOS-1323](https://osgeo-org.atlassian.net/browse/GEOS-1323) Make sure the admin link in the installer points to localhost not 127.0.0.1, improve the description of the demo
* [GEOS-1354](https://osgeo-org.atlassian.net/browse/GEOS-1354) Investigate png encoding performance dropdown at gs 1.5
* [GEOS-1357](https://osgeo-org.atlassian.net/browse/GEOS-1357) Find out a better mime type matcher
* [GEOS-1377](https://osgeo-org.atlassian.net/browse/GEOS-1377) Meta-buffer interferes with coverage rendering
* [GEOS-1397](https://osgeo-org.atlassian.net/browse/GEOS-1397) Replace google maps example with OpenLayers
* [GEOS-9398](https://osgeo-org.atlassian.net/browse/GEOS-9398) [Community][wps-remote] Async Request Management Proposal

Bug:

* [GEOS-1033](https://osgeo-org.atlassian.net/browse/GEOS-1033) delete sld in web admin should actually delete the sld file
* [GEOS-1109](https://osgeo-org.atlassian.net/browse/GEOS-1109) InCorrect Colors produced from Imagemosaic Maps
* [GEOS-1289](https://osgeo-org.atlassian.net/browse/GEOS-1289) FeatureType CRS does not get properly adjusted in case of CRS forcing
* [GEOS-1291](https://osgeo-org.atlassian.net/browse/GEOS-1291) Google projection is using the wrong axis
* [GEOS-1308](https://osgeo-org.atlassian.net/browse/GEOS-1308) Utilize newly-released GML 2.1.2.1 schemas in geoserver
* [GEOS-1334](https://osgeo-org.atlassian.net/browse/GEOS-1334) Make GeoServer run in Oracle Application Server
* [GEOS-1358](https://osgeo-org.atlassian.net/browse/GEOS-1358) FilePublisher mime type guessing is not working properly for html and xml files. Use ServletContext.getMimeType instead
* [GEOS-1359](https://osgeo-org.atlassian.net/browse/GEOS-1359) KML request + legend generation may trigger an exception
* [GEOS-1369](https://osgeo-org.atlassian.net/browse/GEOS-1369) Make arabic labels display fine
* [GEOS-1396](https://osgeo-org.atlassian.net/browse/GEOS-1396) Missing batik jars prevent svg icon usage
* [GEOS-1402](https://osgeo-org.atlassian.net/browse/GEOS-1402) GeoServer returns 415 UNSUPPORTED_MEDIA_TYPE when asking for "http://localhost:8080/geoserver/styles/default_polygon.sld"
* [GEOS-1405](https://osgeo-org.atlassian.net/browse/GEOS-1405) Oracle datastore fails to detect the geometry type if the native srs is not recognized
* [GEOS-1409](https://osgeo-org.atlassian.net/browse/GEOS-1409) KML thorws NPE and enters big strange loop when Mark has no Fill element
* [GEOS-1412](https://osgeo-org.atlassian.net/browse/GEOS-1412) Oracle should try to handle more SRS codes
* [GEOS-1413](https://osgeo-org.atlassian.net/browse/GEOS-1413) ShapeZip output format should force the declared crs, and also handle the eventual lack of a prj file in the generated shapefile
* [GEOS-1428](https://osgeo-org.atlassian.net/browse/GEOS-1428) Problem with SLD - External Graphics
* [GEOS-1453](https://osgeo-org.atlassian.net/browse/GEOS-1453) External image and font loading is not thread safe

Task:

* [GEOS-1432](https://osgeo-org.atlassian.net/browse/GEOS-1432) backport KML LookAt improvements to 1.5.x
