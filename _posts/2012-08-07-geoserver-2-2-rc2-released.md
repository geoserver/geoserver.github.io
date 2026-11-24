---
author: geoserver
comments: true
date: 2012-08-07 06:54:19+00:00
layout: post
link: http://blog.geoserver.org/2012/08/07/geoserver-2-2-rc2-released/
slug: geoserver-2-2-rc2-released
title: GeoServer 2.2-RC2 released
wordpress_id: 1130
categories:
- Announcements
---

The GeoServer team is happy to announce the release of  GeoServer 2.2-RC2, now available for [download here](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/). We would like to encourage you to download and try out some of our new features and let us know if there are any bugs to be fixed.

This release includes plenty of bug fixes and new improvements such as:



	
  * Have rest endpoint display a note when no rest extensions are installed

	
  * Rearrange GWC UI components for higher consistency

	
  * Support EPSG:102113 as an alias for web mercator

	
  * Write GWC specific HTTP response headers when using direct WMS integration

	
  * Control the meta tile output format cache so that external apps can drop it on demand

	
  * Made it possible to configure embedded gwc tile layers through the REST API

	
  * Made GWC "direct WMS integration" work with virtual services


For more information, please refer to the [changelog ](#release-notes)for this release.

A big thank you to all the users, contributors, and sponsors that have helped to make this release possible by providing feedback and support to the GeoServer community.

----

## GeoServer 2.2-RC2

Released on August 07, 2012

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/geoserver-2.2-RC2-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/geoserver-2.2-RC2-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/geoserver-2.2-RC2.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/geoserver-2.2-RC2.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/geoserver-2.2-RC2-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/geoserver-2.2-RC2-htmldoc.zip/download)
- [PDF Documentation](http://downloads.sourceforge.net/geoserver/geoserver-2.2-RC2-pdfdoc.zip)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/geoserver-2.2-RC2-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-ogr-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC2/extensions/geoserver-2.2-RC2-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 18611

## Release notes

New Feature:

* [GEOS-4209](https://osgeo-org.atlassian.net/browse/GEOS-4209) Add a way to control the meta tile output format cache so that external apps can drop it on demand
* [GEOS-4980](https://osgeo-org.atlassian.net/browse/GEOS-4980) Make it possible to configure embedded gwc tile layers through the REST API
* [GEOS-4993](https://osgeo-org.atlassian.net/browse/GEOS-4993) Make GWC "direct WMS integration" work with virtual services

Improvement:

* [GEOS-3901](https://osgeo-org.atlassian.net/browse/GEOS-3901) Have rest endpoint display a note when no rest extensions are installed
* [GEOS-5039](https://osgeo-org.atlassian.net/browse/GEOS-5039) Rearrange GWC UI components for higher consistency
* [GEOS-5212](https://osgeo-org.atlassian.net/browse/GEOS-5212) Support EPSG:102113 as an alias for web mercator
* [GEOS-5235](https://osgeo-org.atlassian.net/browse/GEOS-5235) write GWC specific HTTP response headers when using direct WMS integration

Bug:

* [GEOS-5135](https://osgeo-org.atlassian.net/browse/GEOS-5135) Incorrect canonical schema location in WFS 2.0.0 GetCapabilities response
* [GEOS-5162](https://osgeo-org.atlassian.net/browse/GEOS-5162) "Actions" column in Cached Layers page provides inconsistent UI
* [GEOS-5167](https://osgeo-org.atlassian.net/browse/GEOS-5167) Metadata URL in WMS 1.3.0 capabilities is wrong host is localhost
* [GEOS-5168](https://osgeo-org.atlassian.net/browse/GEOS-5168) Metadata Links should be in WCS capabilities
* [GEOS-5172](https://osgeo-org.atlassian.net/browse/GEOS-5172) table filtering in dialog doesn't work on webkit/ie browsers
* [GEOS-5198](https://osgeo-org.atlassian.net/browse/GEOS-5198) Broken link in user documentation
* [GEOS-5201](https://osgeo-org.atlassian.net/browse/GEOS-5201) layer name collisions
* [GEOS-5204](https://osgeo-org.atlassian.net/browse/GEOS-5204) publish tiff in EPSG:3575 fails
* [GEOS-5207](https://osgeo-org.atlassian.net/browse/GEOS-5207) DescribeFeatureType contains all attributes despite attribute limitations setup by the security subsytem
* [GEOS-5208](https://osgeo-org.atlassian.net/browse/GEOS-5208) WPS chaining may result in a NPE if the inner process attempts to report progress
* [GEOS-5211](https://osgeo-org.atlassian.net/browse/GEOS-5211) Duplicate processes are defined in WPS
* [GEOS-5219](https://osgeo-org.atlassian.net/browse/GEOS-5219) WMS 1.3 cite tests fail on metadata mime type

Task:

* [GEOS-5217](https://osgeo-org.atlassian.net/browse/GEOS-5217) update geoserver release documentation
