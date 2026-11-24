---
author: geoserver
comments: true
date: 2012-05-22 15:32:40+00:00
layout: post
link: http://blog.geoserver.org/2012/05/22/geoserver-2-2-beta2-released/
slug: geoserver-2-2-beta2-released
title: GeoServer 2.2-beta2 Released
wordpress_id: 1055
categories:
- Announcements
- Features
---

The GeoServer team is happy to announce the second beta release of GeoServer 2.2, now available for download.

The 2.2-beta2 release includes a number of great improvements and bug fixes. Some of the highlights include:



	
  * Support for **8-bit PNG output with transparency** resulting in a nice tradeoff of performance and appealing visualization. Special thanks to Andrea for this new feature.

	
  * Continued work for supporting **high accuracy datum transformations** that now allows for user defined transformations supplied via WKT. Thanks to the [Catalan Cartographic Institute](http://www.icc.cat) for funding the work and to Oscar Fonts and Andrea for doing the development.

	
  * A new **lenient capabilities mode** that allows the GeoServer capabilities documents to remain functioning despite the presence of misconfigured layers. Thanks to David Winslow for this work.


And much more. See the complete [changelog](#release-notes) of this release for the entire list.

Download and try out 2.2-beta2 today. You can help us get closer to the official 2.2 release by reporting issues in the [bug tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS) and on the [mailing list](mailto:geoserver-users@lists.sourceforge.net).

Thanks for supporting GeoServer!

----

## GeoServer 2.2-beta2

Released on May 21, 2012

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/geoserver-2.2-beta2-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/geoserver-2.2-beta2-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/geoserver-2.2-beta2.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/geoserver-2.2-beta2.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/geoserver-2.2-beta2-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/geoserver-2.2-beta2-htmldoc.zip/download)
- [PDF Documentation](http://downloads.sourceforge.net/geoserver/geoserver-2.2-beta2-pdfdoc.zip)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/geoserver-2.2-beta2-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-ogr-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/extensions/geoserver-2.2-beta2-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 18437

## Release notes

New Feature:

* [GEOS-5006](https://osgeo-org.atlassian.net/browse/GEOS-5006) GeoserverGridShiftLocator

Improvement:

* [GEOS-4702](https://osgeo-org.atlassian.net/browse/GEOS-4702) Passwords stored in plain text
* [GEOS-4919](https://osgeo-org.atlassian.net/browse/GEOS-4919) Support alpha transparency in png8 output
* [GEOS-5050](https://osgeo-org.atlassian.net/browse/GEOS-5050) Start jetty in the IDE with an open SSL port optionally
* [GEOS-5064](https://osgeo-org.atlassian.net/browse/GEOS-5064) Central Authentication Service (CAS) Support
* [GEOS-5071](https://osgeo-org.atlassian.net/browse/GEOS-5071) ability to upload multiple shapefiles in zip files via rest api
* [GEOS-5081](https://osgeo-org.atlassian.net/browse/GEOS-5081) Make the contract of the recently added Catalog.getLayerGroupByName(workspace, name) method more consistent
* [GEOS-5091](https://osgeo-org.atlassian.net/browse/GEOS-5091) WMS - GetCapabilities - INSPIRE

Bug:

* [GEOS-4336](https://osgeo-org.atlassian.net/browse/GEOS-4336) PNG encoder does not support indexed images with alpha in the pallete entries
* [GEOS-4432](https://osgeo-org.atlassian.net/browse/GEOS-4432) CLONE -GeoServer trunk does not correctly match a shapefile's projection to the correct epsg
* [GEOS-5003](https://osgeo-org.atlassian.net/browse/GEOS-5003) NullPointer in GWC when caching enabled for TIME or ELEVATION parameters
* [GEOS-5041](https://osgeo-org.atlassian.net/browse/GEOS-5041) Broken File/URL conversions in security
* [GEOS-5043](https://osgeo-org.atlassian.net/browse/GEOS-5043) Build failure in sec-jdbc
* [GEOS-5047](https://osgeo-org.atlassian.net/browse/GEOS-5047) LockFile implementation doesn't close IO streams.
* [GEOS-5053](https://osgeo-org.atlassian.net/browse/GEOS-5053) Denial of service opportunity in REST API using new security system
* [GEOS-5060](https://osgeo-org.atlassian.net/browse/GEOS-5060) Changing password encryption for user group service prevents future logins
* [GEOS-5067](https://osgeo-org.atlassian.net/browse/GEOS-5067) Random build failure in wms DimensionHelperTest
* [GEOS-5073](https://osgeo-org.atlassian.net/browse/GEOS-5073) org.geoserver.catalog.impl.ProxyList is said to be immutable, but it's not
* [GEOS-5074](https://osgeo-org.atlassian.net/browse/GEOS-5074) DefaultCatalogFacade's encapsulation of styles broken, and risks concurrent modification exceptions on styles and layergroups
* [GEOS-5078](https://osgeo-org.atlassian.net/browse/GEOS-5078) Saved GeoServer tile layer gridsubset extents can overlap the gridset's area of validity instead of being contained
* [GEOS-5079](https://osgeo-org.atlassian.net/browse/GEOS-5079) JDBC User Group Service uses DDL statement property file for DML as default
* [GEOS-5082](https://osgeo-org.atlassian.net/browse/GEOS-5082) Intermittent build failure caused by race condition in LRUAuthenticationCacheTest.testAuthenticationEntry
* [GEOS-5087](https://osgeo-org.atlassian.net/browse/GEOS-5087) Access mode admin not available on data access rule page
* [GEOS-5092](https://osgeo-org.atlassian.net/browse/GEOS-5092) Out of sync GWC layers prevent server startup
* [GEOS-5093](https://osgeo-org.atlassian.net/browse/GEOS-5093) If a GridSet was somehow removed externally and a tilelayer had a gridsubset for it, then the tile layer edit page breaks
* [GEOS-5096](https://osgeo-org.atlassian.net/browse/GEOS-5096) Build hang in wps-core ExecuteTest.testConcurrentRequests on one CPU
* [GEOS-5099](https://osgeo-org.atlassian.net/browse/GEOS-5099) Layer Preview does not show prefixed names for standard layers
* [GEOS-5100](https://osgeo-org.atlassian.net/browse/GEOS-5100) Typo in GeoServerSecurityProvider API
* [GEOS-5107](https://osgeo-org.atlassian.net/browse/GEOS-5107) Build failure in app-schema-test WmsGetMapTest in a path with spaces
* [GEOS-5109](https://osgeo-org.atlassian.net/browse/GEOS-5109) Do "already configured?" check based on native name, not published one
* [GEOS-5120](https://osgeo-org.atlassian.net/browse/GEOS-5120) KML output document does not correctly handle standalone documents

Task:

* [GEOS-4983](https://osgeo-org.atlassian.net/browse/GEOS-4983) Make sure embedded GWC config gets reloaded when the GeoServer config is called for a reload
* [GEOS-5065](https://osgeo-org.atlassian.net/browse/GEOS-5065) Move cas out to separate security module
* [GEOS-5089](https://osgeo-org.atlassian.net/browse/GEOS-5089) Document admin access mode
