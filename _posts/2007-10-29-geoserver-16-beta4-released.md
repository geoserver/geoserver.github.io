---
author: Chris Holmes
comments: true
date: 2007-10-29 15:33:36+00:00
layout: post
link: http://blog.geoserver.org/2007/10/29/geoserver-16-beta4-released/
slug: geoserver-16-beta4-released
title: GeoServer 1.6-beta4 released
wordpress_id: 72
categories:
- Announcements
---

The GeoServer team is pleased to announce what should be the last beta release in the 1.6 series.  So please download, help us test, test, test, and RC1 should come out soon.

Beta4 has a number of great improvements, all across the board.  The [versioning support](https://web.archive.org/web/20071029/http://docs.codehaus.org/display/GEOS/Versioning+WFS) has had a number of improvements and bug fixes, soon we should have some easy to use tutorials and stable examples, but for the impatient you can try to figure things out from an [early example](http://geo.openplans.org/tschaub/wfsv/feature-editor.html) and the [foss4g tutorial](https://web.archive.org/web/20071029/http://docs.codehaus.org/display/GEOSDOC/6+Versioning).  Google Earth support has some nice improvements, with better sizes for icons and the addition of the KML 'LookAt' tag, which zooms you straight to where your data is, plus a number of bug fixes.

GeoJSON support has been updated to the latest spec, and the 'www' portion of the data directory is now working properly, allowing anyone to ship demos to be served by GeoServer.  For the next release we will show some examples of how to do this.  Also new is support for 'component WMS', which allows GeoServer to do on the fly rendering of layers that reside on other servers.  In the WMS request you just specify the SLD and the location of the WFS and GeoServer gives you the rest.  There is also support for Arabic labels.  GeoServer is also now working properly in Oracle Application server.

----

GeoServer 1.6.0-beta4 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta4/). SourceForge Release 549768

- [Release Notes](#release-notes)
- [geoserver-1.6-beta4.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta4/geoserver-1.6-beta4.exe/download)
- [geoserver-1.6-beta4-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta4/geoserver-1.6-beta4-bin.zip/download)
- [geoserver-1.6-beta4-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta4/geoserver-1.6-beta4-src.zip/download)
- [geoserver-1.6-beta4-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta4/geoserver-1.6-beta4-war.zip/download)
- [geoserver-1.6.0-beta4-doc.zip](http://downloads.sourceforge.net/geoserver/geoserver-1.6-beta4-doc.zip)
- [geoserver-1.6-beta4-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta4/geoserver-1.6-beta4-javadoc.zip/download)

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta4/extensions/)

#### DataStore Extensions

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta4/extensions/geoserver-1.6-beta4-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta4/extensions/geoserver-1.6-beta4-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta4/extensions/geoserver-1.6-beta4-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta4/extensions/geoserver-1.6-beta4-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta4/extensions/geoserver-1.6-beta4-vpf-plugin.zip/download)
- [WFS](http://downloads.sourceforge.net/geoserver/geoserver-1.6-beta4-wfs-plugin.zip)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta4/extensions/geoserver-1.6-beta4-oracle-plugin.zip/download)

#### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta4/extensions/geoserver-1.6-beta4-pyramid-plugin.zip/download)

Tested with: Jetty, Tomcat, OC4J, JBoss

## Release notes

Improvement:

* [GEOS-750](https://osgeo-org.atlassian.net/browse/GEOS-750) KVP readers should be version aware
* [GEOS-807](https://osgeo-org.atlassian.net/browse/GEOS-807) Layer group finctionality
* [GEOS-908](https://osgeo-org.atlassian.net/browse/GEOS-908) add optional ogc:Filter to kml_reflect-or
* [GEOS-1006](https://osgeo-org.atlassian.net/browse/GEOS-1006) Add png8 image output format
* [GEOS-1055](https://osgeo-org.atlassian.net/browse/GEOS-1055) Base map seems to use layer's default style instead of using the ones defined along it
* [GEOS-1105](https://osgeo-org.atlassian.net/browse/GEOS-1105) Sorts featureTypes Collection before the Capabilities is generated.
* [GEOS-1151](https://osgeo-org.atlassian.net/browse/GEOS-1151) Better name than GeoServer for root KML Document (and maybe kml reflect)
* [GEOS-1184](https://osgeo-org.atlassian.net/browse/GEOS-1184) Cannot have two feature types with different namespaces anymore
* [GEOS-1225](https://osgeo-org.atlassian.net/browse/GEOS-1225) Change KML reflectors defaults
* [GEOS-1245](https://osgeo-org.atlassian.net/browse/GEOS-1245) Put asKML link on the OpenLayers Preview Pages
* [GEOS-1246](https://osgeo-org.atlassian.net/browse/GEOS-1246) Set `<scale>` param for KML icons to 0.20
* [GEOS-1251](https://osgeo-org.atlassian.net/browse/GEOS-1251) Templates for Time in KML
* [GEOS-1266](https://osgeo-org.atlassian.net/browse/GEOS-1266) Make it so the preview page shows formats other than openlayers
* [GEOS-1267](https://osgeo-org.atlassian.net/browse/GEOS-1267) Investigate better mercator projection for google maps
* [GEOS-1351](https://osgeo-org.atlassian.net/browse/GEOS-1351) Properly parse TIME parameter
* [GEOS-1353](https://osgeo-org.atlassian.net/browse/GEOS-1353) Use ISO date format for WFS-V HTML logs output
* [GEOS-1354](https://osgeo-org.atlassian.net/browse/GEOS-1354) Investigate png encoding performance dropdown at gs 1.5
* [GEOS-1357](https://osgeo-org.atlassian.net/browse/GEOS-1357) Find out a better mime type matcher
* [GEOS-1374](https://osgeo-org.atlassian.net/browse/GEOS-1374) An exception is throw when generating the kml legend for a layer using a text symbolizer
* [GEOS-1375](https://osgeo-org.atlassian.net/browse/GEOS-1375) KML Polygon placemark is too small, making it hard to click
* [GEOS-1377](https://osgeo-org.atlassian.net/browse/GEOS-1377) Meta-buffer interferes with coverage rendering
* [GEOS-1378](https://osgeo-org.atlassian.net/browse/GEOS-1378) DifferenceQuery parser ignores the eventual filter inside it
* [GEOS-1384](https://osgeo-org.atlassian.net/browse/GEOS-1384) GetLog does not respect maxFeatures
* [GEOS-1385](https://osgeo-org.atlassian.net/browse/GEOS-1385) Have DifferenceQuery fromFeatureVersion default to "FIRST"
* [GEOS-1387](https://osgeo-org.atlassian.net/browse/GEOS-1387) Add GML2 and GeoJSON output to GetLog call
* [GEOS-1391](https://osgeo-org.atlassian.net/browse/GEOS-1391) GetLog fails if no output format is specified, the WFSGetFeatureOutputFormat tries to handle the result instead of GetLogGML3OutputFormat
* [GEOS-1393](https://osgeo-org.atlassian.net/browse/GEOS-1393) Templates do break when an attribute contains a boolean value
* [GEOS-1417](https://osgeo-org.atlassian.net/browse/GEOS-1417) Styles with many feature type style are working for with attribute filtering disabled

Bug:

* [GEOS-920](https://osgeo-org.atlassian.net/browse/GEOS-920) test kml stuff with new dispatcher
* [GEOS-945](https://osgeo-org.atlassian.net/browse/GEOS-945) underscore in typeName of a Query element causes validation error
* [GEOS-946](https://osgeo-org.atlassian.net/browse/GEOS-946) WFS 1.1 sample requests not working
* [GEOS-959](https://osgeo-org.atlassian.net/browse/GEOS-959) PropertyIsNull will grab nulls WMS SLD, but nulls also seem to be considered greater value than numbers
* [GEOS-965](https://osgeo-org.atlassian.net/browse/GEOS-965) capabilities does not report available output formats
* [GEOS-1011](https://osgeo-org.atlassian.net/browse/GEOS-1011) There's code leaving Transactions open in Geoserver
* [GEOS-1081](https://osgeo-org.atlassian.net/browse/GEOS-1081) kmattr and kmscore do not make it past the kml reflector
* [GEOS-1087](https://osgeo-org.atlassian.net/browse/GEOS-1087) Make it so that the source release is buildable
* [GEOS-1129](https://osgeo-org.atlassian.net/browse/GEOS-1129) shutdown.sh does not work, still referneces stop.jar
* [GEOS-1131](https://osgeo-org.atlassian.net/browse/GEOS-1131) On the fly meta tiler breaks GIF output format
* [GEOS-1137](https://osgeo-org.atlassian.net/browse/GEOS-1137) WFS and WMS FeatureId filter parsing broken
* [GEOS-1143](https://osgeo-org.atlassian.net/browse/GEOS-1143) Previously working (but invalid) WFS requests no longer work with 1.6.x
* [GEOS-1152](https://osgeo-org.atlassian.net/browse/GEOS-1152) kml ignores scale when rendering rules
* [GEOS-1164](https://osgeo-org.atlassian.net/browse/GEOS-1164) Make sure it's possible to try out the WFS datastore
* [GEOS-1197](https://osgeo-org.atlassian.net/browse/GEOS-1197) wfs insert with boolean value fails in postgis
* [GEOS-1198](https://osgeo-org.atlassian.net/browse/GEOS-1198) property filters in sld with boolean property do not match properly
* [GEOS-1211](https://osgeo-org.atlassian.net/browse/GEOS-1211) Wrong scale computation in previewing projected layers
* [GEOS-1215](https://osgeo-org.atlassian.net/browse/GEOS-1215) Returned coverage dimensions do not always match those requested
* [GEOS-1218](https://osgeo-org.atlassian.net/browse/GEOS-1218) Shapefile with thousands of points not entirely served by GeoServer
* [GEOS-1219](https://osgeo-org.atlassian.net/browse/GEOS-1219) WMS test failure, WMTVER not recognized
* [GEOS-1220](https://osgeo-org.atlassian.net/browse/GEOS-1220) GetFeatureInfo GML output cite test failure
* [GEOS-1221](https://osgeo-org.atlassian.net/browse/GEOS-1221) sld point styling with external graphic does not pick up external urls
* [GEOS-1223](https://osgeo-org.atlassian.net/browse/GEOS-1223) Do not force reprojection if no geometry properties are around
* [GEOS-1227](https://osgeo-org.atlassian.net/browse/GEOS-1227) ArcSDE raster support broken on trunk (perhaps by latest WMS-CRS handling changes?)
* [GEOS-1229](https://osgeo-org.atlassian.net/browse/GEOS-1229) Insert fails because of GML formatting
* [GEOS-1233](https://osgeo-org.atlassian.net/browse/GEOS-1233) Legend graphics are not antialiased
* [GEOS-1241](https://osgeo-org.atlassian.net/browse/GEOS-1241) Points aren't picking up KML name from SLD label
* [GEOS-1247](https://osgeo-org.atlassian.net/browse/GEOS-1247) superoverlays break at high zoom levels
* [GEOS-1250](https://osgeo-org.atlassian.net/browse/GEOS-1250) Remote external graphics fail for KML points
* [GEOS-1255](https://osgeo-org.atlassian.net/browse/GEOS-1255) Make sure not even developer logging level make shapefile renderer dump down that gazillion of log statements
* [GEOS-1256](https://osgeo-org.atlassian.net/browse/GEOS-1256) Stroke linejoin and linewith seem to have no effect on 1.6.x
* [GEOS-1258](https://osgeo-org.atlassian.net/browse/GEOS-1258) Fast bbox computation missing for Oracle
* [GEOS-1259](https://osgeo-org.atlassian.net/browse/GEOS-1259) Port palette work from 1.5.x to trunk
* [GEOS-1260](https://osgeo-org.atlassian.net/browse/GEOS-1260) GetLegendGraphics sample request fails
* [GEOS-1261](https://osgeo-org.atlassian.net/browse/GEOS-1261) Multiple feature types with the same name and different namespace make insert code fail
* [GEOS-1264](https://osgeo-org.atlassian.net/browse/GEOS-1264) SVG point wont' display and validate
* [GEOS-1279](https://osgeo-org.atlassian.net/browse/GEOS-1279) XML config writer does not escape xml entities, generating a catalog.xml that cannot be parsed
* [GEOS-1280](https://osgeo-org.atlassian.net/browse/GEOS-1280) MySql datastore does not honor the specified namespace
* [GEOS-1286](https://osgeo-org.atlassian.net/browse/GEOS-1286) Coverage configuration form allows pure SRS number to be inputed, but all of the code expects EPSG:XXXX instead
* [GEOS-1288](https://osgeo-org.atlassian.net/browse/GEOS-1288) Support use of proxyRedirectURL parameter in AceGI security and other spots
* [GEOS-1289](https://osgeo-org.atlassian.net/browse/GEOS-1289) FeatureType CRS does not get properly adjusted in case of CRS forcing
* [GEOS-1291](https://osgeo-org.atlassian.net/browse/GEOS-1291) Google projection is using the wrong axis
* [GEOS-1292](https://osgeo-org.atlassian.net/browse/GEOS-1292) ShapefileRenderer does not behave properly if a shapefile layer has been forced to another projection, or if it has none
* [GEOS-1308](https://osgeo-org.atlassian.net/browse/GEOS-1308) Utilize newly-released GML 2.1.2.1 schemas in geoserver
* [GEOS-1318](https://osgeo-org.atlassian.net/browse/GEOS-1318) Freemarker templates are using the "default encoding" instead of UTF-8
* [GEOS-1319](https://osgeo-org.atlassian.net/browse/GEOS-1319) Halos don't seem to be properly centered on the primary label.
* [GEOS-1320](https://osgeo-org.atlassian.net/browse/GEOS-1320) gml encoding does not work if geometry column is named 'location'
* [GEOS-1331](https://osgeo-org.atlassian.net/browse/GEOS-1331) wfs insert fails when you have a dataset which has names that clash with the gml abstract feature type
* [GEOS-1334](https://osgeo-org.atlassian.net/browse/GEOS-1334) Make GeoServer run in Oracle Application Server
* [GEOS-1340](https://osgeo-org.atlassian.net/browse/GEOS-1340) Applied style to polygons not visible in KML
* [GEOS-1346](https://osgeo-org.atlassian.net/browse/GEOS-1346) insert with srsName on geometry fails in wfs 1.0
* [GEOS-1355](https://osgeo-org.atlassian.net/browse/GEOS-1355) The GML2-GZIP in version 1.6.0-beta3 is broken.
* [GEOS-1358](https://osgeo-org.atlassian.net/browse/GEOS-1358) FilePublisher mime type guessing is not working properly for html and xml files. Use ServletContext.getMimeType instead
* [GEOS-1359](https://osgeo-org.atlassian.net/browse/GEOS-1359) KML request + legend generation may trigger an exception
* [GEOS-1360](https://osgeo-org.atlassian.net/browse/GEOS-1360) nullpointer exception in kmlreflector
* [GEOS-1362](https://osgeo-org.atlassian.net/browse/GEOS-1362) Data from postgis not rendered correctly
* [GEOS-1365](https://osgeo-org.atlassian.net/browse/GEOS-1365) GeoJSON Output format  - null pointer error when the geometry property is not required
* [GEOS-1367](https://osgeo-org.atlassian.net/browse/GEOS-1367) Links on online Documentation page don't work
* [GEOS-1369](https://osgeo-org.atlassian.net/browse/GEOS-1369) Make arabic labels display fine
* [GEOS-1376](https://osgeo-org.atlassian.net/browse/GEOS-1376) GeoJSON extension should support most recent draft from geojson.org
* [GEOS-1394](https://osgeo-org.atlassian.net/browse/GEOS-1394) boundedBy on features in transaction should be ignored, not throw exeption
* [GEOS-1395](https://osgeo-org.atlassian.net/browse/GEOS-1395) gml:coordinates should be accepted as well as gml:posList for gml3 geometries
* [GEOS-1396](https://osgeo-org.atlassian.net/browse/GEOS-1396) Missing batik jars prevent svg icon usage
* [GEOS-1402](https://osgeo-org.atlassian.net/browse/GEOS-1402) GeoServer returns 415 UNSUPPORTED_MEDIA_TYPE when asking for "http://localhost:8080/geoserver/styles/default_polygon.sld"
* [GEOS-1404](https://osgeo-org.atlassian.net/browse/GEOS-1404) QNameKvpParser NPE's when hit with an uknown prefix
* [GEOS-1405](https://osgeo-org.atlassian.net/browse/GEOS-1405) Oracle datastore fails to detect the geometry type if the native srs is not recognized
* [GEOS-1409](https://osgeo-org.atlassian.net/browse/GEOS-1409) KML thorws NPE and enters big strange loop when Mark has no Fill element
* [GEOS-1412](https://osgeo-org.atlassian.net/browse/GEOS-1412) Oracle should try to handle more SRS codes
* [GEOS-1413](https://osgeo-org.atlassian.net/browse/GEOS-1413) ShapeZip output format should force the declared crs, and also handle the eventual lack of a prj file in the generated shapefile
* [GEOS-1423](https://osgeo-org.atlassian.net/browse/GEOS-1423) Add support for component WMS
* [GEOS-1433](https://osgeo-org.atlassian.net/browse/GEOS-1433) Make sure  "http://www.opengis.net/gml/srs/epsg.xml#xxx" is interpreted as lon/lat by default
* [GEOS-1444](https://osgeo-org.atlassian.net/browse/GEOS-1444) GeoServer logging setup fails if there is a space in the geoserver installation path
* [GEOS-1446](https://osgeo-org.atlassian.net/browse/GEOS-1446) More logging configuration problems

Task:

* [GEOS-934](https://osgeo-org.atlassian.net/browse/GEOS-934) ensure dispatcher respects proxy base url
* [GEOS-1237](https://osgeo-org.atlassian.net/browse/GEOS-1237) Remove overview window from default openlayers output
* [GEOS-1379](https://osgeo-org.atlassian.net/browse/GEOS-1379) Time parameter in WMS, and the way to parse ISO date

Sub-task:

* [GEOS-1424](https://osgeo-org.atlassian.net/browse/GEOS-1424) Add support for REMOTE_OWS_TYPE and REMOTE_OWS_URL
* [GEOS-1425](https://osgeo-org.atlassian.net/browse/GEOS-1425) Fix SLD libray mode
* [GEOS-1426](https://osgeo-org.atlassian.net/browse/GEOS-1426) Add support for remote UserLayer in sld=xxx and SLD_BODY=xxx
