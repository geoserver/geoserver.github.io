---
author: geoserver
comments: true
date: 2012-07-10 02:59:50+00:00
layout: post
link: http://blog.geoserver.org/2012/07/09/geoserver-2-2-rc1-released/
slug: geoserver-2-2-rc1-released
title: GeoServer 2.2-RC1 released
wordpress_id: 1109
categories:
- Announcements
---

The GeoServer team is happy to announce the release of  GeoServer 2.2-RC1, now available for download. We would like to encourage you to download and try out some of our new features and let us know if there are any bugs to be fixed.

This release includes plenty of bug fixes and new improvements such as:



	
  * Allow security provider plugins to hook into initialization process

	
  * REST security configuration improvement

	
  * Allow KML Document Title to be set by format_options parameters

	
  * Increased performance when saving a layer whose native SRS has no native EPSG code

	
  * Added functionality for setting return page to GeoServerBasePage


For more information, please refer to the [changelog](#release-notes) for this release.

The GeoServer team have also migrated from the SVN repository to [GitHub](http://github.com) and would like to give a special thanks to Justin Deoliveira from [OpenGeo ](https://web.archive.org/web/20120710/http://opengeo.org/)for all his hard work into making the migration possible.

A big thank you to all the users, contributors, and sponsors that have helped to make this release possible by providing feedback and support to the GeoServer community.

----

## GeoServer 2.2-RC1

Released on July 9, 2012

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/geoserver-2.2-RC1-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/geoserver-2.2-RC1-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/geoserver-2.2-RC1.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/geoserver-2.2-RC1.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/geoserver-2.2-RC1-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/geoserver-2.2-RC1-htmldoc.zip/download)
- [PDF Documentation](http://downloads.sourceforge.net/geoserver/geoserver-2.2-RC1-pdfdoc.zip)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/geoserver-2.2-RC1-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-ogr-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-RC1/extensions/geoserver-2.2-RC1-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 18610

## Release notes

New Feature:

* [GEOS-4545](https://osgeo-org.atlassian.net/browse/GEOS-4545) Add option to encode srsName as urn:ogc in WFS responses

Improvement:

* [GEOS-5110](https://osgeo-org.atlassian.net/browse/GEOS-5110) Allow KML Document Title to be set by format_options parameters
* [GEOS-5119](https://osgeo-org.atlassian.net/browse/GEOS-5119) (Backport to 2.1.x) Allow KML Document Title to be set by format_options parameters
* [GEOS-5126](https://osgeo-org.atlassian.net/browse/GEOS-5126) Saving a layer whose native SRS has no native EPSG code takes several seconds
* [GEOS-5129](https://osgeo-org.atlassian.net/browse/GEOS-5129) Support idgen=UseExisting via WFS transaction
* [GEOS-5132](https://osgeo-org.atlassian.net/browse/GEOS-5132) Dispatch based on namespace in xml post requests
* [GEOS-5134](https://osgeo-org.atlassian.net/browse/GEOS-5134) added functionality for setting return page to GeoServerBasePage
* [GEOS-5139](https://osgeo-org.atlassian.net/browse/GEOS-5139) REST security configuration improvement
* [GEOS-5142](https://osgeo-org.atlassian.net/browse/GEOS-5142) Have the wms scale denominator among the wms default environment variables
* [GEOS-5158](https://osgeo-org.atlassian.net/browse/GEOS-5158) Allow securityprovider plugins to hook into initialization process
* [GEOS-5171](https://osgeo-org.atlassian.net/browse/GEOS-5171) rest api does not fall back on custom file data stores

Bug:

* [GEOS-4608](https://osgeo-org.atlassian.net/browse/GEOS-4608) GTOPO30 from UGS appear scrambled
* [GEOS-5085](https://osgeo-org.atlassian.net/browse/GEOS-5085) WFS 2.0 paging returns wrong features for startindex=0
* [GEOS-5101](https://osgeo-org.atlassian.net/browse/GEOS-5101) Assure unique role names
* [GEOS-5103](https://osgeo-org.atlassian.net/browse/GEOS-5103) Workspace-specific styles are not represented correctly in REST API representations for layers
* [GEOS-5125](https://osgeo-org.atlassian.net/browse/GEOS-5125) Spatial filters in WMS (SLD or CQL) won't work if the geometries are expressed in a SRS other than the data native one
* [GEOS-5128](https://osgeo-org.atlassian.net/browse/GEOS-5128) wfs 2.0 request with accept versions or accept formats results in classcastexception
* [GEOS-5130](https://osgeo-org.atlassian.net/browse/GEOS-5130) acceptversions not respected if version parameter is specified
* [GEOS-5147](https://osgeo-org.atlassian.net/browse/GEOS-5147) Typo in WMS Interpolation Settings
* [GEOS-5152](https://osgeo-org.atlassian.net/browse/GEOS-5152) LDAPAuthenticationProvider gets stuck in endless doAuthenticate loop with DelegatingAuthenticationProvider
* [GEOS-5161](https://osgeo-org.atlassian.net/browse/GEOS-5161) Even/odd rows display oddly on Server Status page
* [GEOS-5169](https://osgeo-org.atlassian.net/browse/GEOS-5169) Shapefile memory mapping options uneditable under recent Firefox versions
* [GEOS-5173](https://osgeo-org.atlassian.net/browse/GEOS-5173) SLDs with Rendering Transformations do not validate in Style Editor
* [GEOS-5227](https://osgeo-org.atlassian.net/browse/GEOS-5227) The coverage settings page does not validate the thread pool min and max size

Task:

* [GEOS-5131](https://osgeo-org.atlassian.net/browse/GEOS-5131) turn off srsDimension encoding during wfs 1.1 cite tests
* [GEOS-5200](https://osgeo-org.atlassian.net/browse/GEOS-5200) Transition version control to Git
