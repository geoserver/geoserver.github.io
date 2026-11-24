---
author: geoserver
comments: true
date: 2013-08-18 13:53:10+00:00
layout: post
link: http://blog.geoserver.org/2013/08/18/geoserver-2-3-5-released/
slug: geoserver-2-3-5-released
title: GeoServer 2.3.5 Released
wordpress_id: 1519
categories:
- Announcements
tags:
- release
- stable
---

The GeoServer team is pleased to announce the release of GeoServer 2.3.5:



	
  * Downloads ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.5/geoserver-2.3.5-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.5/geoserver-2.3.5-war.zip/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.5/geoserver-2.3.5.exe/download)) are listed on the GeoServer 2.3.5 page along with documentation and extensions.


This is a stable release containing several important fixes:

	
  * A couple new [authentication options for LDAP](https://osgeo-org.atlassian.net/browse/GEOS-5805), thanks to Mauro Bartolomeoli for this work.

	
  * The file browser used when defining a new data source once again lets windows users [explore the available drives](https://osgeo-org.atlassian.net/browse/GEOS-5842)

	
  * Alessio has [back ported](https://osgeo-org.atlassian.net/browse/GEOS-2527) a fix for creating a [data sources referencing a shared file system](https://osgeo-org.atlassian.net/browse/GEOS-2508).

	
  * GeoWebCache has fixes for [WMS 1.3.0](https://osgeo-org.atlassian.net/browse/GEOS-5685) and [database security](https://osgeo-org.atlassian.net/browse/GEOS-5828) (thanks to Jonathan Moules for reporting this one).

	
  * More details can be found in the [GeoServer 2.3.5 Release Notes](#release-notes).


This release is made in conjunction with [GeoTools 9.5](http://geotoolsnews.blogspot.com.au/2013/08/geotools-95-released.html) and is the last [scheduled release](https://web.archive.org/web/20130818/http://geoserver.org/display/GEOS/GeoTools+and+GeoServer+release+schedule) for the GeoServer 2.3.x series.

----

## GeoServer 2.3.5

Released on August 18, 2013

#### Download format

- [Binary (OS independent)](http://sourceforge.net/projects/geoserver/files/GeoServer/2.3.5/geoserver-2.3.5-bin.zip/download)
- [Web Archive](http://sourceforge.net/projects/geoserver/files/GeoServer/2.3.5/geoserver-2.3.5-war.zip)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.5/geoserver-2.3.5.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.5/geoserver-2.3.5.dmg/download)
- [Source Code](http://sourceforge.net/projects/geoserver/files/GeoServer/2.3.5/geoserver-2.3.5-src.zip)

#### Documentation

- [HTML Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.3.5/geoserver-2.3.5-htmldoc.zip)
- [API Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.3.5/geoserver-2.3.5-javadoc.zip)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-app-schema-plugin.zip)
- [ArcSDE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-arcsde-plugin.zip)
- [DB2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-db2-plugin.zip)
- [H2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-h2-plugin.zip)
- [MySQL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-mysql-plugin.zip)
- [Oracle](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-oracle-plugin.zip)
- [Pregeneralized features](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-feature-pregeneralized-plugin.zip)
- [SQL Server](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-sqlserver-plugin.zip)
- [Teradata](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-teradata-plugin.zip)
- [VPF](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-vpf-plugin.zip)
- [INSPIRE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-inspire-plugin.zip)

**Coverage store**

- [GDAL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-gdal-plugin.zip)
- [Image Pyramid](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-pyramid-plugin.zip)
- [JPEG2000](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-jp2k-plugin.zip)
- [JDBC Image Mosaic](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-imagemosaic-jdbc-plugin.zip)

**Other**

- [Chart dynamic symbolizer](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-charts-plugin.zip)
- [Control flow](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-control-flow-plugin.zip)
- [Cross layer filtering](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-querylayer-plugin.zip)
- [CSS styling](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-css-plugin.zip)
- [Excel output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-excel-plugin.zip)
- [GeoSearch](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-geosearch-plugin.zip)
- [Image Map output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-imagemap-plugin.zip)
- [OGR output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-ogr-plugin.zip)
- [XSLT output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-xslt-plugin.zip)
- [WPS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-wps-plugin.zip)
- [CAS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-cas-plugin.zip)
- Monitor ([Core](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-monitor-plugin.zip), [Hibernate](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.3.5/geoserver-2.3.5-monitor-hibernate-plugin.zip))

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19445

## Release notes

Improvement:

* [GEOS-1849](https://osgeo-org.atlassian.net/browse/GEOS-1849) Remove old SPI for GetMap and GetLegendGraphics
* [GEOS-2362](https://osgeo-org.atlassian.net/browse/GEOS-2362) Remove NURC namespace
* [GEOS-2527](https://osgeo-org.atlassian.net/browse/GEOS-2527) Port GEOS-2508 to trunk
* [GEOS-2530](https://osgeo-org.atlassian.net/browse/GEOS-2530) Port GEOS-2529 to trunk
* [GEOS-5805](https://osgeo-org.atlassian.net/browse/GEOS-5805) Add new options to LDAP authentication provider

Bug:

* [GEOS-1414](https://osgeo-org.atlassian.net/browse/GEOS-1414) Geoserver can't find logging config when it's installed (or it's data dir is located in) a path with a space in it
* [GEOS-3329](https://osgeo-org.atlassian.net/browse/GEOS-3329) Exception to add this geotif
* [GEOS-3550](https://osgeo-org.atlassian.net/browse/GEOS-3550) Geoserver fails to create mrSID data on MassGIS data
* [GEOS-3883](https://osgeo-org.atlassian.net/browse/GEOS-3883) reprojection error being applied to each processing tile with in a requested image subset.
* [GEOS-3923](https://osgeo-org.atlassian.net/browse/GEOS-3923) Pyramide
* [GEOS-4063](https://osgeo-org.atlassian.net/browse/GEOS-4063) ImageMosaic plugin can't read dataset
* [GEOS-4077](https://osgeo-org.atlassian.net/browse/GEOS-4077) Error reading metadata on GeoTIFF store load
* [GEOS-4393](https://osgeo-org.atlassian.net/browse/GEOS-4393) WMS-request on ECW-datastores seems to consume all available memory
* [GEOS-5685](https://osgeo-org.atlassian.net/browse/GEOS-5685) GeoWebCache not WMS 1.3.0 compliant
* [GEOS-5703](https://osgeo-org.atlassian.net/browse/GEOS-5703) TurboJPEG issue: BandSelect on images with alpha
* [GEOS-5704](https://osgeo-org.atlassian.net/browse/GEOS-5704) TurboJPEG issue: ImageMosaic TurboJpeg encoding may throw IllegalArgumentException
* [GEOS-5828](https://osgeo-org.atlassian.net/browse/GEOS-5828) GWC - External Database issues (including security one)
* [GEOS-5842](https://osgeo-org.atlassian.net/browse/GEOS-5842) List of drives is invisible for Adding store
* [GEOS-5881](https://osgeo-org.atlassian.net/browse/GEOS-5881) LayerGroup page does not mandate the specification of the CRS
* [GEOS-5921](https://osgeo-org.atlassian.net/browse/GEOS-5921) Disabling anonymous authentication for the GUI results in an HTTP redirect loop

Task:

* [GEOS-3549](https://osgeo-org.atlassian.net/browse/GEOS-3549) wcs 1.0 module with multi dimensional coverage support
* [GEOS-5896](https://osgeo-org.atlassian.net/browse/GEOS-5896) Document uconfiguration of GDAL_DRIVER_PATH on Windows
