---
author: geoserver
comments: true
date: 2011-04-05 22:13:31+00:00
layout: post
link: http://blog.geoserver.org/2011/04/05/geoserver-2-1-rc4-released/
slug: geoserver-2-1-rc4-released
title: GeoServer 2.1-RC4 Released
wordpress_id: 917
categories:
- Announcements
---

The GeoServer team is happy to announce the fourth release candidate for 2.1, now available for download.

This release brings some important bug fixes and addresses a few regressions discovered in RC3. This includes a [new parameter](https://osgeo-org.atlassian.net/browse/GEOS-4454) that will once again allow multiple GeoServer instances to run from a single data directory. This parameter, named "GWC_DISKQUOTA_DISABLED", will disable the GeoWebCache disk quota module preventing it from maintaining a lock in the data directory.

Other key fixes include an issue with the alternate and more performant method of [raster reprojection](https://osgeo-org.atlassian.net/browse/GEOS-4443) that comes with the GeoServer 2.1 series, as well as some fixes for WMS 1.3 support surrounding axis ordering issues. Check out the [change log](#release-notes) for the full list.

Thanks to everyone who tested RC3 and helped us flush out these last few issues. You can continue to help us get to the official 2.1 release by downloading and trying out RC4. Be sure to report any issues in the [bug tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS) or on the [mailing list](mailto:geoserver-users@lists.sourceforge.net).

Thanks for using GeoServer!

----

## GeoServer 2.1-RC4

Released on April 06, 2011

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/geoserver-2.1-RC4-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/geoserver-2.1-RC4a-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/geoserver-2.1-RC4.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/geoserver-2.1-RC4.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/geoserver-2.1-RC4-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/geoserver-2.1-RC4-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/geoserver-2.1-RC4-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/geoserver-2.1-RC4-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-control-flow-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-ogr-plugin.zip/download)
- [RESTConfig](http://downloads.sourceforge.net/geoserver/geoserver-2.1-RC4-restconfig-plugin.zip)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-wfsv-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC4/extensions/geoserver-2.1-RC4-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 17294

## Release notes

Bug:

* [GEOS-4283](https://osgeo-org.atlassian.net/browse/GEOS-4283) wms 1.3 getCapabilities layer BoundingBox with swapped axis
* [GEOS-4344](https://osgeo-org.atlassian.net/browse/GEOS-4344) exeption in PostgreSQL Create new feature type...
* [GEOS-4441](https://osgeo-org.atlassian.net/browse/GEOS-4441) Per row security filters are not applied on all code paths
* [GEOS-4443](https://osgeo-org.atlassian.net/browse/GEOS-4443) Raster reprojection fails against areas where the projection is fully symmetrical
* [GEOS-4446](https://osgeo-org.atlassian.net/browse/GEOS-4446) WMS 1.3 GetFeatureInfo uses incorrect screen coordinates
* [GEOS-4454](https://osgeo-org.atlassian.net/browse/GEOS-4454) GWC quota support prevents multiple GS to start against the same data directory
* [GEOS-4456](https://osgeo-org.atlassian.net/browse/GEOS-4456) Spurious extra points might appear in the map with an Oracle data source
* [GEOS-4457](https://osgeo-org.atlassian.net/browse/GEOS-4457) Chosen Bursa wolf parameters for NAD83 -> WGS84 are valid only over Hawaii
* [GEOS-4467](https://osgeo-org.atlassian.net/browse/GEOS-4467) advanced dispatch filter causes failure on tomcat 7
