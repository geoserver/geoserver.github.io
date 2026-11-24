---
author: geoserver
comments: true
date: 2012-09-03 09:33:27+00:00
layout: post
link: http://blog.geoserver.org/2012/09/03/geoserver-2-2-rc3-released/
slug: geoserver-2-2-rc3-released
title: GeoServer 2.2-RC3 Released
wordpress_id: 1134
---

The GeoServer team is happy to announce the release of GeoServer 2.2-RC3.The release is available for download from:
https://web.archive.org/web/20120903/http://geoserver.org/display/GEOS/GeoServer+2.2-RC3

This release comes with assorted bug fixes and small improvements, and aims to be the latest RC before the final release. Notable changes:



	
  * improvements in the security subsystem upgrade from the 2.1.x series

	
  * bug fixes and improvements in the control-flow module (you won't be wondering anymore if it's properly installed, or not)

	
  * avoid deadlocks on some WFS transactions


The entire change logfor the 2.2-RC3 release is available in the issue tracker:
[Release notes](#release-notes)
A very special thanks to all those who contributed bug fixes and improvements to this release.
--The GeoServer Team

----

## GeoServer 2.2-RC3

Released on September 3rd, 2012

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/geoserver-2.2-RC3-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/geoserver-2.2-RC3-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/geoserver-2.2-RC3.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/geoserver-2.2-RC3.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/geoserver-2.2-RC3-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/geoserver-2.2-RC3-htmldoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/geoserver-2.2-RC3-javadoc.zip/download)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-ogr-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC3/extensions/geoserver-2.2-RC3-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 18700

## Release notes

Improvement:

* [GEOS-5241](https://osgeo-org.atlassian.net/browse/GEOS-5241) Tighten type constraints in AuthenticationFilterPanel
* [GEOS-5242](https://osgeo-org.atlassian.net/browse/GEOS-5242) Improve logging for control-flow
* [GEOS-5256](https://osgeo-org.atlassian.net/browse/GEOS-5256) Use admin password as master password during migration
* [GEOS-5261](https://osgeo-org.atlassian.net/browse/GEOS-5261) CLONE - WMS GetLegendGraphic should output labels if no Rule is specified

Bug:

* [GEOS-5209](https://osgeo-org.atlassian.net/browse/GEOS-5209) Avoid altering attribute name case in GetFeatureInfo HTML template
* [GEOS-5226](https://osgeo-org.atlassian.net/browse/GEOS-5226) The coverage settings are getting re-initialized at each and every catalog modification
* [GEOS-5243](https://osgeo-org.atlassian.net/browse/GEOS-5243) Using both user and ip flow controllers leads to ip users being locked out
* [GEOS-5259](https://osgeo-org.atlassian.net/browse/GEOS-5259) GeoServer security subsytem fails to migrate previously valid user names
* [GEOS-5266](https://osgeo-org.atlassian.net/browse/GEOS-5266) Coverage parameters may fail to be properly converted
* [GEOS-5275](https://osgeo-org.atlassian.net/browse/GEOS-5275) Edit user page uses XML store regardless of
* [GEOS-5281](https://osgeo-org.atlassian.net/browse/GEOS-5281) Documentation on "Security » Role system » Role services" has incorrect tablename for the role sevice schema
* [GEOS-5283](https://osgeo-org.atlassian.net/browse/GEOS-5283) Bin package will OOM after a few demo requests
* [GEOS-5285](https://osgeo-org.atlassian.net/browse/GEOS-5285) WMS + SLD demo request waits indefinitely
* [GEOS-5286](https://osgeo-org.atlassian.net/browse/GEOS-5286) Tasmania cities preview fails due to empty bbox
* [GEOS-5287](https://osgeo-org.atlassian.net/browse/GEOS-5287) KML with superoverlays generates empty documents
* [GEOS-5292](https://osgeo-org.atlassian.net/browse/GEOS-5292) Update community sldService to work with the latest security structure
* [GEOS-5295](https://osgeo-org.atlassian.net/browse/GEOS-5295) org.geowebcache.grid.BoundingBox -> DecimalFormat uses localized pattern characters
* [GEOS-5344](https://osgeo-org.atlassian.net/browse/GEOS-5344) I cannot see Layer Preview
