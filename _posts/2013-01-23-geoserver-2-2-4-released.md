---
author: geoserver
comments: true
date: 2013-01-23 11:37:27+00:00
layout: post
link: http://blog.geoserver.org/2013/01/23/geoserver-2-2-4-released/
slug: geoserver-2-2-4-released
title: GeoServer 2.2.4 released
wordpress_id: 1302
---

The GeoServer team is happy to announce the release of GeoServer 2.2.4, now available for download.

This is the latest release of the stable 2.2 series. The changes that might interest the most users are:



	
  * the monitoring extension module just got promoted to official extension [[GEOS-5538](https://osgeo-org.atlassian.net/browse/GEOS-5538)]

	
  * the status page does not throw errors after catalog reloads anymore [[GEOS-5371](https://osgeo-org.atlassian.net/browse/GEOS-5371)]

	
  * one critical fix in the REST configuration of freemarker templates [[GEOS-5533](https://osgeo-org.atlassian.net/browse/GEOS-5533)]


The changelog also contains the following minor bug fixes

	
  * [[GEOS-5338](https://osgeo-org.atlassian.net/browse/GEOS-5338)] - Filter function IEEERemainder mishbehaves in SLD

	
  * [[GEOS-5537](https://osgeo-org.atlassian.net/browse/GEOS-5537)] - Tiling artifacts with RasterSymbolizer using bilinear interpolation (when oversampling raster)

	
  * [[GEOS-5551](https://osgeo-org.atlassian.net/browse/GEOS-5551)] - WFS 1.0 capabilities will NPE with misconfigured OGR and XSLT output formats

	
  * [[GEOS-5565](https://osgeo-org.atlassian.net/browse/GEOS-5565)] - workspace admin unable to create sql view

	
  * [[GEOS-5570](https://osgeo-org.atlassian.net/browse/GEOS-5570)] - QueryProcess fails if called with an OGC filter (either 1.0 or 1.1)

	
  * [[GEOS-5197](https://osgeo-org.atlassian.net/browse/GEOS-5197)] - Use the layer abstract as the GeoRSS channel description

	
  * [[GEOS-5561](https://osgeo-org.atlassian.net/browse/GEOS-5561)] - Missing i18n support for ReprojectPage

	
  * [[GEOS-5562](https://osgeo-org.atlassian.net/browse/GEOS-5562)] - Missing i18n support for WorkspaceEditPage

	
  * [[GEOS-5563](https://osgeo-org.atlassian.net/browse/GEOS-5563)] - slight mixed up order of Y-parameters in AffineTransformPanel


Also, looking at the corresponding GeoTools release changelog we have the following extra goodies in:

	
  * improvements in the WFS cascading, we can now better interact with remote WFS servers running on TinyOWS and ArcGIS

	
  * imageio-ext was upgraded to version 1.1.6, which means from now on GeoServer uses GDAL 1.9 to extends the range of raster formats it supports


Download GeoServer 2.2.4, try it out, and provide feedback on the [GeoServer mailing list](https://web.archive.org/web/20130123/http://geoserver.org/display/GEOS/Mailing+Lists).

Thanks again for using GeoServer!

----

## GeoServer 2.2.4

Released on January 22 2013

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/geoserver-2.2.4-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/geoserver-2.2.4-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/geoserver-2.2.4.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/geoserver-2.2.4.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/geoserver-2.2.4-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/geoserver-2.2.4-htmldoc.zip/download)
- [PDF Documentation](http://downloads.sourceforge.net/geoserver/geoserver-2.2.4-pdfdoc.zip)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/geoserver-2.2.4-javadoc.zip/download)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-ogr-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-wps-plugin.zip/download)
- [CAS](http://downloads.sourceforge.net/geoserver/geoserver-2.2.4-cas-plugin.zip)
- Monitor ([Core](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-monitor-plugin.zip/download), [Hibernate](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.4/extensions/geoserver-2.2.4-monitor-hibernate-plugin.zip/download))

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19031

## Release notes

Improvement:

* [GEOS-5197](https://osgeo-org.atlassian.net/browse/GEOS-5197) Use the layer abstract as the GeoRSS channel description
* [GEOS-5538](https://osgeo-org.atlassian.net/browse/GEOS-5538) Promote monitor module to extension
* [GEOS-5561](https://osgeo-org.atlassian.net/browse/GEOS-5561) Missing i18n support for ReprojectPage
* [GEOS-5562](https://osgeo-org.atlassian.net/browse/GEOS-5562) Missing i18n support for WorkspaceEditPage
* [GEOS-5563](https://osgeo-org.atlassian.net/browse/GEOS-5563) slight mixed up order of Y-parameters in AffineTransformPanel

Bug:

* [GEOS-5338](https://osgeo-org.atlassian.net/browse/GEOS-5338) Filter function IEEERemainder
* [GEOS-5371](https://osgeo-org.atlassian.net/browse/GEOS-5371) Reloading config break status config page
* [GEOS-5533](https://osgeo-org.atlassian.net/browse/GEOS-5533) Updating freemarker templates via REST-API deletes whole target folder
* [GEOS-5537](https://osgeo-org.atlassian.net/browse/GEOS-5537) Tiling artifacts with RasterSymbolizer using bilinear interpolation
* [GEOS-5551](https://osgeo-org.atlassian.net/browse/GEOS-5551) WFS 1.0 capabilities will NPE with misconfigured OGR and XSLT output formats
* [GEOS-5565](https://osgeo-org.atlassian.net/browse/GEOS-5565) workspace admin unable to create sql view
* [GEOS-5570](https://osgeo-org.atlassian.net/browse/GEOS-5570) QueryProcess fails if called with an OGC filter (either 1.0 or 1.1)
* [GEOS-5639](https://osgeo-org.atlassian.net/browse/GEOS-5639) Mac OSX installer not working
