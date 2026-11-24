---
author: geoserver
comments: true
date: 2012-12-24 14:02:32+00:00
layout: post
link: http://blog.geoserver.org/2012/12/24/geoserver-2-2-3-released/
slug: geoserver-2-2-3-released
title: GeoServer 2.2.3 released
wordpress_id: 1289
---

The GeoServer team is happy to announce the release of GeoServer 2.2.3, now available for download.

This is the latest release of the stable 2.2 series and contains some small new features and interesting fixes:



	
  * [[GEOS-3885](https://osgeo-org.atlassian.net/browse/GEOS-3885)] - Update Freemarker templates through REST API

	
  * [[GEOS-5325](https://osgeo-org.atlassian.net/browse/GEOS-5325)] - Add title and abstract to LayerGroupInfo

	
  * [[GEOS-5462](https://osgeo-org.atlassian.net/browse/GEOS-5462)] - The rendering thread can block forever under request cancellation

	
  * [[GEOS-5479](https://osgeo-org.atlassian.net/browse/GEOS-5479)] - Error in Documentation: </PropertyName> tag used instead of </Literal>

	
  * [[GEOS-5483](https://osgeo-org.atlassian.net/browse/GEOS-5483)] - json output in WPS extension does not work due to missing library

	
  * [[GEOS-5485](https://osgeo-org.atlassian.net/browse/GEOS-5485)] - Border artifacts when reprojecting single banded (scientific) raster data


Also, looking at the corresponding GeoTools release changelog we have the following extra goodies in:

	
  * better support for chaining rendering transformations

	
  * fixes to time/date handling in CQL

	
  * Oracle specific SDO_NN function to find the N nearest objects to a given location


We also welcome our newest committer, Davide Savazzi, and thank him for the work on Freemarker template through the REST API and the title and abstract support in layer groups, as well as the SDO_NN work back in GeoTools.

Download GeoServer 2.2.3, try it out, and provide feedback on the [GeoServer mailing list](https://web.archive.org/web/20121224/http://geoserver.org/display/GEOS/Mailing+Lists).

Thanks again for using GeoServer!

----

## GeoServer 2.2.3

Released on Dec 24, 2012

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/geoserver-2.2.3-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/geoserver-2.2.3-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/geoserver-2.2.3.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/geoserver-2.2.3.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/geoserver-2.2.3-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/geoserver-2.2.3-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/geoserver-2.2.3-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/geoserver-2.2.3-javadoc.zip/download)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-ogr-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.3/extensions/geoserver-2.2.3-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

## Release notes

Improvement:

* [GEOS-3885](https://osgeo-org.atlassian.net/browse/GEOS-3885) Update freemarker templates through REST API
* [GEOS-5325](https://osgeo-org.atlassian.net/browse/GEOS-5325) Add title and abstract to LayerGroupInfo

Bug:

* [GEOS-5462](https://osgeo-org.atlassian.net/browse/GEOS-5462) The rendering thread can block forever under request cancellation
* [GEOS-5479](https://osgeo-org.atlassian.net/browse/GEOS-5479) Error in Documentation: `</PropertyName>` tag used instead of `</Literal>`
* [GEOS-5483](https://osgeo-org.atlassian.net/browse/GEOS-5483) json output in WPS extension does not work due to missing library
* [GEOS-5485](https://osgeo-org.atlassian.net/browse/GEOS-5485) Border artifacts when reprojecting single banded (scientific) raster data
* [GEOS-5586](https://osgeo-org.atlassian.net/browse/GEOS-5586) XSLT WFS output format - new community module
