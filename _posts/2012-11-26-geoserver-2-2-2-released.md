---
author: geoserver
comments: true
date: 2012-11-26 22:42:28+00:00
layout: post
link: http://blog.geoserver.org/2012/11/26/geoserver-2-2-2-released/
slug: geoserver-2-2-2-released
title: GeoServer 2.2.2 Released
wordpress_id: 1279
categories:
- Announcements
- Features
---

The GeoServer team is happy to announce the release of GeoServer 2.2.2, now available for download.

This is the latest release of the stable 2.2 series and contains a number of good fixes and improvements including:



	
  * [[GEOS-5157](https://osgeo-org.atlassian.net/browse/GEOS-5157)] - Can't configure MediaType in INSPIRE extension

	
  * [[GEOS-5376](https://osgeo-org.atlassian.net/browse/GEOS-5376)] - Line sizes with UOM in legend decoration are doubly scaled when using DPI

	
  * [[GEOS-5377](https://osgeo-org.atlassian.net/browse/GEOS-5377)] - WMS GetFeatureInfo fails when post filter required

	
  * [[GEOS-5388](https://osgeo-org.atlassian.net/browse/GEOS-5388)] - Confusing 'Bad credentials forroot' exception in verbose_logging mode when logged in as admin or root

	
  * [[GEOS-5395](https://osgeo-org.atlassian.net/browse/GEOS-5395)] - Catalog reload breaks GWC integration, update sequence upgrade and namespace/workspace consistency

	
  * [[GEOS-5402](https://osgeo-org.atlassian.net/browse/GEOS-5402)] - Subclasses of GeoServerPreAuthenticationFilter do not map local admin roles to global admin roles

	
  * [[GEOS-5366](https://osgeo-org.atlassian.net/browse/GEOS-5366)] - Better heuristic for OWS Request filenames


A number of great fixes came in via community pull requests:

	
  * [Image mosaic filtering fixes](https://github.com/geoserver/geoserver/pull/45)

	
  * [Removing json-lib conflict with GWC](https://github.com/geoserver/geoserver/pull/55)

	
  * [Property handling of POST/PUT requests for proxy module](https://github.com/geoserver/geoserver/pull/71)


Special thanks to Carlo Cancellieri, Jared Erickson, and Andreas Hocevar for their contributions.

And last but not least we saw two new interesting community modules surface for this release:

	
  * [XSLT output format generator plugin for WFS ](http://docs.geoserver.org/latest/en/user/community/xslt/index.html)

	
  * [JSR-223 based scripting extension](http://docs.geoserver.org/latest/en/user/community/scripting/index.html)


Both are available as community nightly builds.

Download GeoServer 2.2.2, try it out, and provide feedback on the [GeoServer mailing list](https://web.archive.org/web/20121126/http://geoserver.org/display/GEOS/Mailing+Lists).

Thanks again for using GeoServer!

----

## GeoServer 2.2.2

Released on Nov 23, 2012

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/geoserver-2.2.2-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/geoserver-2.2.2-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/geoserver-2.2.2.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/geoserver-2.2.2.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/geoserver-2.2.2-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/geoserver-2.2.2-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/geoserver-2.2.2-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/geoserver-2.2.2-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-ogr-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.2/extensions/geoserver-2.2.2-wps-plugin.zip/download)
- [CAS](http://downloads.sourceforge.net/geoserver/geoserver-2.2.2-cas-plugin.zip)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 18898

## Release notes

Improvement:

* [GEOS-5366](https://osgeo-org.atlassian.net/browse/GEOS-5366) Better heuristic for OWS Request filenames

Bug:

* [GEOS-4970](https://osgeo-org.atlassian.net/browse/GEOS-4970) Changing scale ratio map decorations in accordance to dpi settings and producing dpi independent scale line
* [GEOS-5157](https://osgeo-org.atlassian.net/browse/GEOS-5157) Can't configure MediaType in INSPIRE extension
* [GEOS-5279](https://osgeo-org.atlassian.net/browse/GEOS-5279) ImageMosaic Filter option does not work
* [GEOS-5347](https://osgeo-org.atlassian.net/browse/GEOS-5347) RestConfig leaves files opened when downloading stores as zip
* [GEOS-5376](https://osgeo-org.atlassian.net/browse/GEOS-5376) Line sizes with UOM in legend decoration are doubly scaled when using DPI
* [GEOS-5377](https://osgeo-org.atlassian.net/browse/GEOS-5377) WMS GetFeatureInfo fails when post filter required
* [GEOS-5388](https://osgeo-org.atlassian.net/browse/GEOS-5388) Confusing 'Bad credentials forroot' exception in verbose_logging mode when logged in as admin or root
* [GEOS-5395](https://osgeo-org.atlassian.net/browse/GEOS-5395) Catalog reload breaks GWC integration, update sequence upgrade and namespace/workspace consistency
* [GEOS-5402](https://osgeo-org.atlassian.net/browse/GEOS-5402) Subclasses of GeoServerPreAuthenticationFilter do not map local admin roles to global admin roles
* [GEOS-5507](https://osgeo-org.atlassian.net/browse/GEOS-5507) Can't assign workspace-specific style to a layer in the same workspace via REST
