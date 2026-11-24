---
author: Chris Holmes
comments: true
date: 2007-11-19 14:43:09+00:00
layout: post
link: http://blog.geoserver.org/2007/11/19/download-the-first-release-candidate-of-160/
slug: download-the-first-release-candidate-of-160
title: Download the first Release Candidate of 1.6.0
wordpress_id: 78
categories:
- Announcements
---

We are pleased to announce GeoServer 1.6.0-RC1 is available for download (try [direct from sourceforge](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/) if that link isn't working).  Since beta4 the team has has closed over 60 issues, tightening up every single detail.  This is easily the most solid first release candidate that we've ever issued, as we are wanting to have as few release candidates as possible.  So if you have not upgraded to the 1.6.x series then now is the time to do so, to ensure that any problems that may arise get fixed as quickly as possible, before 1.6.0.

The 1.6.x series is a major leap forward from 1.5, with major leaps in performance, WFS 1.1 support, and the new ['versioning' WFS](https://web.archive.org/web/20071119/http://docs.codehaus.org/display/GEOS/Versioning+WFS).  There is also much better [support for Google Earth](http://docs.codehaus.org/display/GEOSDOC/Google+Earth) and [Google Maps/Virtual Earth/Yahoo! Maps](http://docs.codehaus.org/display/GEOSDOC/Google+Maps), leveraging better integration with [OpenLayers](http://openlayers.org).  There is also a new integrated [security subsystem](http://docs.codehaus.org/display/GEOSDEV/Geoserver+security+implementation%2C+initial+version), built on [Acegi](http://www.acegisecurity.org/), to provide role-based access control to GeoServer resources.  But the real reason to upgrade to 1.6.0 is a ton of bug fixes, all the rough edges are getting sanded down, so that most all features 'just work', no matter what you throw at them.  So please download and let us know how it goes.

----

GeoServer 1.6.0-RC1 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/). SourceForge Release 554392

- [geoserver-1.6.0-RC1.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/geoserver-1.6.0-RC1.exe/download)
- [geoserver-1.6.0-RC1-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/geoserver-1.6.0-RC1-bin.zip/download)
- [geoserver-1.6.0-RC1-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/geoserver-1.6.0-RC1-src.zip/download)
- [geoserver-1.6.0-RC1-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/geoserver-1.6.0-RC1-war.zip/download)
- [geoserver-1.6.0-RC1-doc.zip](http://downloads.sourceforge.net/geoserver/geoserver-1.6.0-RC1-doc.zip)
- [geoserver-1.6.0-RC1-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/geoserver-1.6.0-RC1-javadoc.zip/download)

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/extensions/)

#### DataStore Extensions

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/extensions/geoserver-1.6.0-RC1-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/extensions/geoserver-1.6.0-RC1-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/extensions/geoserver-1.6.0-RC1-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/extensions/geoserver-1.6.0-RC1-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/extensions/geoserver-1.6.0-RC1-vpf-plugin.zip/download)
- [WFS](http://downloads.sourceforge.net/geoserver/geoserver-1.6.0-RC1-wfs-plugin.zip)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/extensions/geoserver-1.6.0-RC1-oracle-plugin.zip/download)

#### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC1/extensions/geoserver-1.6.0-RC1-pyramid-plugin.zip/download)

Tested with: Jetty, Tomcat

## Release notes

New Feature:

* [GEOS-1464](https://osgeo-org.atlassian.net/browse/GEOS-1464) add bbox to GeoJSON output

Improvement:

* [GEOS-754](https://osgeo-org.atlassian.net/browse/GEOS-754) Check configuration sanity at startup
* [GEOS-850](https://osgeo-org.atlassian.net/browse/GEOS-850) no data should be accessed in GetCapabilities request
* [GEOS-1047](https://osgeo-org.atlassian.net/browse/GEOS-1047) have WMS/KML reflector calculate bounds from cached feature type
* [GEOS-1048](https://osgeo-org.atlassian.net/browse/GEOS-1048) have wms/kml reflector calculate one of width or height based on aspect ratio
* [GEOS-1239](https://osgeo-org.atlassian.net/browse/GEOS-1239) Handle non-4326 srs with KML output better
* [GEOS-1285](https://osgeo-org.atlassian.net/browse/GEOS-1285) Set DB2 property setFetchSize configurable from geoserver webadmin interface
* [GEOS-1305](https://osgeo-org.atlassian.net/browse/GEOS-1305) integrating fid as an id in KML Placemark
* [GEOS-1342](https://osgeo-org.atlassian.net/browse/GEOS-1342) Logging profile deafaults to verbose when not set
* [GEOS-1381](https://osgeo-org.atlassian.net/browse/GEOS-1381) Update the wfs-t demo in geoserver to OpenLayers 2.5 and beef it up a little in the process
* [GEOS-1397](https://osgeo-org.atlassian.net/browse/GEOS-1397) Replace google maps example with OpenLayers
* [GEOS-1415](https://osgeo-org.atlassian.net/browse/GEOS-1415) smaller OL build for previews
* [GEOS-1442](https://osgeo-org.atlassian.net/browse/GEOS-1442) SLDParser: CssParameter parser should support mixed syntax
* [GEOS-1460](https://osgeo-org.atlassian.net/browse/GEOS-1460) Upgrade iText to 2.0.6
* [GEOS-1462](https://osgeo-org.atlassian.net/browse/GEOS-1462) Investigate OGC geometric filteres breakage on postgis
* [GEOS-1466](https://osgeo-org.atlassian.net/browse/GEOS-1466) Transparent graphic from WMS GetLegendGraphic
* [GEOS-1467](https://osgeo-org.atlassian.net/browse/GEOS-1467) SLDWizard does not figure out the geometry if it's the last attribute in the feature type
* [GEOS-1478](https://osgeo-org.atlassian.net/browse/GEOS-1478) Patch GeoTools to do mixed content SLD labels
* [GEOS-1498](https://osgeo-org.atlassian.net/browse/GEOS-1498) allow user to specify less features then declared in layer grouping

Bug:

* [GEOS-915](https://osgeo-org.atlassian.net/browse/GEOS-915) Sample WFS requests making Geoserver throw exceptions of various kind
* [GEOS-1295](https://osgeo-org.atlassian.net/browse/GEOS-1295) NPE when adding a new feature type on a PostGIS table without a geometry field
* [GEOS-1325](https://osgeo-org.atlassian.net/browse/GEOS-1325) Handle axis order issues
* [GEOS-1326](https://osgeo-org.atlassian.net/browse/GEOS-1326) TextSymbolizer Graphic OnlineResource seems to lose accessibility to the graphic file.
* [GEOS-1330](https://osgeo-org.atlassian.net/browse/GEOS-1330) KML not reprojected into target SRS when SRS option 3 (trust data native srs) is selected
* [GEOS-1363](https://osgeo-org.atlassian.net/browse/GEOS-1363) Geometryless data cannot be nor configured nor wfs-inserted
* [GEOS-1420](https://osgeo-org.atlassian.net/browse/GEOS-1420) Current interpretation of SLD library mode does not conform to the spec (afaik)
* [GEOS-1428](https://osgeo-org.atlassian.net/browse/GEOS-1428) Problem with SLD - External Graphics
* [GEOS-1429](https://osgeo-org.atlassian.net/browse/GEOS-1429) Randomly problems with external graphics loading
* [GEOS-1435](https://osgeo-org.atlassian.net/browse/GEOS-1435) WFS GET bbox parsing looses axis orientation
* [GEOS-1437](https://osgeo-org.atlassian.net/browse/GEOS-1437) srsName does not cascade from Query to bounding box (and eventually, to other geometries as well)
* [GEOS-1438](https://osgeo-org.atlassian.net/browse/GEOS-1438) SRS fails to travel from gml:Envelope to Disjoint filter
* [GEOS-1439](https://osgeo-org.atlassian.net/browse/GEOS-1439) BBox filters won't consider their envelope SRS
* [GEOS-1440](https://osgeo-org.atlassian.net/browse/GEOS-1440) GML3 geometry bindings disregard srs information
* [GEOS-1441](https://osgeo-org.atlassian.net/browse/GEOS-1441) GetFeature should reproject to the _declared_ crs
* [GEOS-1445](https://osgeo-org.atlassian.net/browse/GEOS-1445) Feature symbology covering labels.
* [GEOS-1448](https://osgeo-org.atlassian.net/browse/GEOS-1448) GetLog DifferenceQuery throws NullPointerException
* [GEOS-1449](https://osgeo-org.atlassian.net/browse/GEOS-1449) Fix transaction framework limitations
* [GEOS-1450](https://osgeo-org.atlassian.net/browse/GEOS-1450) Null pointer exception on startup in the validation subsystem
* [GEOS-1451](https://osgeo-org.atlassian.net/browse/GEOS-1451) Null pointer when doing a request against a galdos server
* [GEOS-1452](https://osgeo-org.atlassian.net/browse/GEOS-1452) Component WMS with generic SLD not working
* [GEOS-1453](https://osgeo-org.atlassian.net/browse/GEOS-1453) External image and font loading is not thread safe
* [GEOS-1454](https://osgeo-org.atlassian.net/browse/GEOS-1454) Multilayer request with default styles fails
* [GEOS-1455](https://osgeo-org.atlassian.net/browse/GEOS-1455) GetLog with WFS 1.0 defaults to GML3 encoding, shoud default to GML2
* [GEOS-1458](https://osgeo-org.atlassian.net/browse/GEOS-1458) Web configuration UI creates lots of datastores without ever disposing them
* [GEOS-1463](https://osgeo-org.atlassian.net/browse/GEOS-1463) feature type bounds not updated when projection changes
* [GEOS-1465](https://osgeo-org.atlassian.net/browse/GEOS-1465) Adding a new feature type with postgis when the underlying geometry type is XYM fails
* [GEOS-1473](https://osgeo-org.atlassian.net/browse/GEOS-1473) WMSGetLegendGraphic-SLD doesn't work quite right
* [GEOS-1475](https://osgeo-org.atlassian.net/browse/GEOS-1475) Update on boolean properties fails
* [GEOS-1481](https://osgeo-org.atlassian.net/browse/GEOS-1481) NullPointerException for json output on geometryless table
* [GEOS-1484](https://osgeo-org.atlassian.net/browse/GEOS-1484) OGC Filter not working with covrage and featuretypes layer combination
* [GEOS-1487](https://osgeo-org.atlassian.net/browse/GEOS-1487) wms/reflect has issues
* [GEOS-1490](https://osgeo-org.atlassian.net/browse/GEOS-1490) Dispose datastores on geoserver shutdown
* [GEOS-1491](https://osgeo-org.atlassian.net/browse/GEOS-1491) Can't edit/add style when port is not 8080
* [GEOS-1493](https://osgeo-org.atlassian.net/browse/GEOS-1493) startup fails with an old style config if the config directory is not writable
* [GEOS-1500](https://osgeo-org.atlassian.net/browse/GEOS-1500) Migrate admin user name and password onto users.properties and setup a service security file too
* [GEOS-1501](https://osgeo-org.atlassian.net/browse/GEOS-1501) Old data dirs using "shapefile url" parameters aren't opened properly anymore
* [GEOS-1503](https://osgeo-org.atlassian.net/browse/GEOS-1503) support basemap group layers in wms getmap post
* [GEOS-1504](https://osgeo-org.atlassian.net/browse/GEOS-1504) Exception in ReTypingDatastore when trying to cascade MapServer with WFS Datastore
* [GEOS-1505](https://osgeo-org.atlassian.net/browse/GEOS-1505) Switch logging subsystem to the new GeoTools Logging.getLogger(xxx) call
* [GEOS-1510](https://osgeo-org.atlassian.net/browse/GEOS-1510) Filters are not getting encoded in WFS cascading
* [GEOS-1512](https://osgeo-org.atlassian.net/browse/GEOS-1512) Template lookup won't work with remote WFS layers (used in component WMS)
* [GEOS-1516](https://osgeo-org.atlassian.net/browse/GEOS-1516) WMS kvp parser fails to parse &styles="s1,,s2,," properly
* [GEOS-1517](https://osgeo-org.atlassian.net/browse/GEOS-1517) WMS kvp parser fails to parse &styles= properly
* [GEOS-1518](https://osgeo-org.atlassian.net/browse/GEOS-1518) Invalid wfs schema references when using describe feature type against multiple

Task:

* [GEOS-1456](https://osgeo-org.atlassian.net/browse/GEOS-1456) organize cite directories on trunk
* [GEOS-1476](https://osgeo-org.atlassian.net/browse/GEOS-1476) Make the size of the transparent + point KML images smaller

Sub-task:

* [GEOS-1468](https://osgeo-org.atlassian.net/browse/GEOS-1468) Equals/NotEquals filters do not get reprojected (but they may have geometries inside)
* [GEOS-1470](https://osgeo-org.atlassian.net/browse/GEOS-1470) Elements below Not filters do not get reprojected... but some may be geometries or bboxes
* [GEOS-1471](https://osgeo-org.atlassian.net/browse/GEOS-1471) Update/Detele/Lock filters should be reprojected as needed
* [GEOS-1472](https://osgeo-org.atlassian.net/browse/GEOS-1472) New features/update geometries should assume the declared crs if none is specified
