---
author: geoserver
comments: true
date: 2012-10-24 08:33:29+00:00
layout: post
link: http://blog.geoserver.org/2012/10/24/geoserver-2-2-1-released/
slug: geoserver-2-2-1-released
title: GeoServer 2.2.1 Released
wordpress_id: 1259
---

The GeoServer team is happy to announce the release of GeoServer 2.2.1, now available for download.

A lot of fixes, improved security sub-system and new stable version of GeoWebcache included.

Enjoy!

The GeoServer Team.

Changes



	
  1. GEOS-5279 ([detail](http://hudson.opengeo.org/hudson/job/geoserver-release/46/changes#detail0))

	
  2. Improved IM filter junit tests ([detail](http://hudson.opengeo.org/hudson/job/geoserver-release/46/changes#detail1))

	
  3. added check for null readParameters and fix format ([detail](http://hudson.opengeo.org/hudson/job/geoserver-release/46/changes#detail2))

	
  4. Layout fixes for IE ([detail](http://hudson.opengeo.org/hudson/job/geoserver-release/46/changes#detail3))

	
  5. Updating developer guide to require JDK 6 ([detail](http://hudson.opengeo.org/hudson/job/geoserver-release/46/changes#detail4))

----

## GeoServer 2.2.1

Released on 24 Oct 2012

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/geoserver-2.2.1-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/geoserver-2.2.1-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/geoserver-2.2.1.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/geoserver-2.2.1.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/geoserver-2.2.1-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/geoserver-2.2.1-htmldoc.zip/download)
- [PDF Documentation](http://downloads.sourceforge.net/geoserver/geoserver-2.2.1-pdfdoc.zip)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/geoserver-2.2.1-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-ogr-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-wps-plugin.zip/download)
- [CAS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2.1/extensions/geoserver-2.2.1-cas-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 18798

## Release notes

Bug:

* [GEOS-4857](https://osgeo-org.atlassian.net/browse/GEOS-4857) PostGIS Layer Leaking Connection when using WMS getFeatureInfo calls in Layer Preview (Open Layers)
* [GEOS-5293](https://osgeo-org.atlassian.net/browse/GEOS-5293) CAS proxy tickets must not be used as key for the authentication cache
* [GEOS-5294](https://osgeo-org.atlassian.net/browse/GEOS-5294) Valid CAS service tickets must result in an HTTP session creation
* [GEOS-5315](https://osgeo-org.atlassian.net/browse/GEOS-5315) WPS request builder incorrectly formats input
* [GEOS-5324](https://osgeo-org.atlassian.net/browse/GEOS-5324) Unable to configure or read already configured layergroup with name in the form 'test:foo'
* [GEOS-5343](https://osgeo-org.atlassian.net/browse/GEOS-5343) DefaultWebCoverageService100.java does not pass a grid geometry to the reader
* [GEOS-5350](https://osgeo-org.atlassian.net/browse/GEOS-5350) Build failures in wps-core on master and 2.2.x
* [GEOS-5354](https://osgeo-org.atlassian.net/browse/GEOS-5354) wms_scale_denominator env variable might not be set when making GetMap larger than world
* [GEOS-5363](https://osgeo-org.atlassian.net/browse/GEOS-5363) geoserver username/password filter uses invalid login form url
