---
author: Justin Deoliveira
comments: true
date: 2007-12-19 15:02:24+00:00
layout: post
link: http://blog.geoserver.org/2007/12/19/geoserver-160-rc2-released/
slug: geoserver-160-rc2-released
title: GeoServer 1.6.0-RC2 Released!
wordpress_id: 81
categories:
- Announcements
- Features
---

We are happy to announce the second release candidate of GeoServer 1.6.0. You can download the release from [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/).

As usual this release candidate brings a heap of bug fixes, with a few minor improvements. Output formats such as [KML](http://docs.codehaus.org/display/GEOSDOC/Google+Earth), SVG, and [GeoRSS](http://docs.codehaus.org/display/GEOSDOC/GeoRSS) have been tightened up fixing a few minor bugs. Backend issues such as PostGIS bounds reprojection and Oracle permissions have also been addressed.  For a complete list check out the [change log](#release-notes).

There are also a few notable improvements to mention. The first being a "strict" request parameter which allows clients to turn on [WFS XML validation](http://docs.codehaus.org/display/GEOSDOC/WFS+vendor+parameters#WFSvendorparameters-validation) on a request by request basis. This provides a nice debugging tool for clients to use for validating WFS requests. Also worth mention is the ongoing work and improvements to the experimental [Versioning WFS protocol](https://web.archive.org/web/20071219/http://docs.codehaus.org/display/GEOS/Versioning+WFS).

With any luck this will be the last release candidate before the official 1.6.0 release. You can help us out by downloading it and trying out. Please report any issues encountered in the [bug tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS).

----

GeoServer 1.6.0-RC2 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/). SourceForge Release 562389

- [geoserver-1.6.0-RC2.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/geoserver-1.6.0-RC2.exe/download)
- [geoserver-1.6.0-RC2-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/geoserver-1.6.0-RC2-bin.zip/download)
- [geoserver-1.6.0-RC2-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/geoserver-1.6.0-RC2-src.zip/download)
- [geoserver-1.6.0-RC2-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/geoserver-1.6.0-RC2-war.zip/download)
- [geoserver-1.6.0-RC2-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/geoserver-1.6.0-RC2-doc.zip/download)
- [geoserver-1.6.0-RC2-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/geoserver-1.6.0-RC2-javadoc.zip/download)

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/extensions/)

#### DataStore Extensions

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/extensions/geoserver-1.6.0-RC2-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/extensions/geoserver-1.6.0-RC2-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/extensions/geoserver-1.6.0-RC2-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/extensions/geoserver-1.6.0-RC2-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/extensions/geoserver-1.6.0-RC2-vpf-plugin.zip/download)
- [WFS](http://downloads.sourceforge.net/geoserver/geoserver-1.6.0-RC2-wfs-plugin.zip)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/extensions/geoserver-1.6.0-RC2-oracle-plugin.zip/download)

#### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC2/extensions/geoserver-1.6.0-RC2-pyramid-plugin.zip/download)

Tested with: Jetty, Tomcat

## Release notes

Improvement:

* [GEOS-1469](https://osgeo-org.atlassian.net/browse/GEOS-1469) Revert back reprojection tests to 900913 once related gt2 issue is fixed
* [GEOS-1514](https://osgeo-org.atlassian.net/browse/GEOS-1514) add a lax parameter to wfs service
* [GEOS-1519](https://osgeo-org.atlassian.net/browse/GEOS-1519) If strict sld library mode parsing fails fall back on the previous lax behaviour (find the first style that applies to the layer's feature type)
* [GEOS-1563](https://osgeo-org.atlassian.net/browse/GEOS-1563) unclear problem in getcapabilities response
* [GEOS-1571](https://osgeo-org.atlassian.net/browse/GEOS-1571) Inconsistency between scale computed by GeoServer and OL map preview
* [GEOS-1577](https://osgeo-org.atlassian.net/browse/GEOS-1577) Special characters not encoded on save from the web UI
* [GEOS-1597](https://osgeo-org.atlassian.net/browse/GEOS-1597) If no xml or kvp reader is configured the Dispatcher throws an NPE
* [GEOS-1599](https://osgeo-org.atlassian.net/browse/GEOS-1599) WFS DescribeFeatureType returns incorrect schema locations
* [GEOS-1602](https://osgeo-org.atlassian.net/browse/GEOS-1602) WFS 1.0 describe feature type output mixes single and double quotes
* [GEOS-1603](https://osgeo-org.atlassian.net/browse/GEOS-1603) WMS Reflector should support reprojection
* [GEOS-1605](https://osgeo-org.atlassian.net/browse/GEOS-1605) Add support for versioning feature collection on the wfs-v protocol
* [GEOS-1615](https://osgeo-org.atlassian.net/browse/GEOS-1615) GetFeature fails if user attempts to reproject a geometryless feature type

Bug:

* [GEOS-1183](https://osgeo-org.atlassian.net/browse/GEOS-1183) Admin password with ampersand (or other special XML characters) breaks deploy
* [GEOS-1368](https://osgeo-org.atlassian.net/browse/GEOS-1368) kml processes/returns features that dont match any rules in the sld
* [GEOS-1513](https://osgeo-org.atlassian.net/browse/GEOS-1513) turn xml validation on by default
* [GEOS-1515](https://osgeo-org.atlassian.net/browse/GEOS-1515) Default value for new layer group (<new_layer_group>) makes geoserver to fail to start if was saved unchanged.
* [GEOS-1522](https://osgeo-org.atlassian.net/browse/GEOS-1522) Geoserver log output fails on 1.60b4
* [GEOS-1525](https://osgeo-org.atlassian.net/browse/GEOS-1525) WFS requests with 'propertyname="*"' raise an exception
* [GEOS-1526](https://osgeo-org.atlassian.net/browse/GEOS-1526) wms rendering with scale dependnent styles consumes a lot of resources
* [GEOS-1528](https://osgeo-org.atlassian.net/browse/GEOS-1528) trouble getting capabilities for a custom crs
* [GEOS-1541](https://osgeo-org.atlassian.net/browse/GEOS-1541) Add listener to shapefile renderer so that rendering errors are reported at FINE logging level
* [GEOS-1542](https://osgeo-org.atlassian.net/browse/GEOS-1542) Default attribute points in KML output are too big and rasterized
* [GEOS-1543](https://osgeo-org.atlassian.net/browse/GEOS-1543) kml reflector does not proeprly set layer bounds when superoveray requested
* [GEOS-1549](https://osgeo-org.atlassian.net/browse/GEOS-1549) GML2 encoding performance dropdown in 1.6.0-rc1
* [GEOS-1550](https://osgeo-org.atlassian.net/browse/GEOS-1550) georss output does not work well
* [GEOS-1553](https://osgeo-org.atlassian.net/browse/GEOS-1553) GeoServer source distribution is missing a few modules
* [GEOS-1554](https://osgeo-org.atlassian.net/browse/GEOS-1554) GeoServer security subsystem does not work properly when Tomcat security subsystem is used around it
* [GEOS-1556](https://osgeo-org.atlassian.net/browse/GEOS-1556) WMS Relector zooms out on repeated requests
* [GEOS-1557](https://osgeo-org.atlassian.net/browse/GEOS-1557) KML encoder keeps on encoding even if the connection is closed mid flight by the client
* [GEOS-1558](https://osgeo-org.atlassian.net/browse/GEOS-1558) Update fails with strange error message if typename namespace is not declared
* [GEOS-1559](https://osgeo-org.atlassian.net/browse/GEOS-1559) Geoserver (c) should have date and copyright holder's too
* [GEOS-1566](https://osgeo-org.atlassian.net/browse/GEOS-1566) GetCaps on wfs 1.1 lists all outputformats twice
* [GEOS-1568](https://osgeo-org.atlassian.net/browse/GEOS-1568) Metatile cache expiry should be linked to config reload and transaction plugins
* [GEOS-1578](https://osgeo-org.atlassian.net/browse/GEOS-1578) PROXY_BASE_URL configuration seems to only work part way
* [GEOS-1581](https://osgeo-org.atlassian.net/browse/GEOS-1581) WCS Describe Coverage does not work properly with rotated coverages
* [GEOS-1584](https://osgeo-org.atlassian.net/browse/GEOS-1584) Versioning datastore does not version enable point tables with a single point inside
* [GEOS-1585](https://osgeo-org.atlassian.net/browse/GEOS-1585) Legend production fails if there is a raster symbolizer in the mix
* [GEOS-1589](https://osgeo-org.atlassian.net/browse/GEOS-1589) Batik SVG output format generates no output at all
* [GEOS-1592](https://osgeo-org.atlassian.net/browse/GEOS-1592) Oracle user must be the schema owner
* [GEOS-1593](https://osgeo-org.atlassian.net/browse/GEOS-1593) kml polygon line width
* [GEOS-1594](https://osgeo-org.atlassian.net/browse/GEOS-1594) Reprojected polylines appear in the wrong place
* [GEOS-1595](https://osgeo-org.atlassian.net/browse/GEOS-1595) Legend breaks kml output
* [GEOS-1606](https://osgeo-org.atlassian.net/browse/GEOS-1606) Versioned FeatureCollection bug
* [GEOS-1607](https://osgeo-org.atlassian.net/browse/GEOS-1607) Unidentified EPSG code in shapefile
* [GEOS-1609](https://osgeo-org.atlassian.net/browse/GEOS-1609) reflect malfunction
* [GEOS-1612](https://osgeo-org.atlassian.net/browse/GEOS-1612) Reprojected GetFeature on a feature type with null geometries fails badly
* [GEOS-1613](https://osgeo-org.atlassian.net/browse/GEOS-1613) No kvp request for GetVersionedFeature GET request
* [GEOS-1617](https://osgeo-org.atlassian.net/browse/GEOS-1617) Reprojected FeatureCollection bounds are incorrect when datastore is Postgis
* [GEOS-1619](https://osgeo-org.atlassian.net/browse/GEOS-1619) SLD parser trims whitespaces from literals
* [GEOS-1737](https://osgeo-org.atlassian.net/browse/GEOS-1737) Start Menu Stop GeoServer does not work
