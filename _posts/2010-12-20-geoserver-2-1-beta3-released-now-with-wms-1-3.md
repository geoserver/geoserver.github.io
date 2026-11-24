---
author: geoserver
comments: true
date: 2010-12-20 15:38:13+00:00
layout: post
link: http://blog.geoserver.org/2010/12/20/geoserver-2-1-beta3-released-now-with-wms-1-3/
slug: geoserver-2-1-beta3-released-now-with-wms-1-3
title: GeoServer 2.1-beta3 released (now with WMS 1.3)
wordpress_id: 811
categories:
- Announcements
tags:
- beta
- cql
- se
- SLD
- sql
- wms
- wms 1.3
---

The GeoServer community is proud to announce the release of 2.1-beta3, which is now available for download.

The big feature for this release is support for **WMS 1.3**. Special thanks goes out to [Ordnance Survey](http://www.ordnancesurvey.co.uk/), Great Britain's national mapping agency, for providing [OpenGeo](https://web.archive.org/web/20101220/http://opengeo.org/) with funding to complete the task. With WMS 1.3 mandated by the [INSPIRE Initiative](http://inspire.jrc.ec.europa.eu/), the Ordnance Survey needed to meet the INSPIRE requirements.  Rather than implement a solution on their own, they opted to fund the GeoServer project so that other organizations in the UK and the rest of Europe and the world could all benefit.

This is the value and the beauty of open source.  Government agencies across Europe can now upgrade their servers to the latest GeoServer at no additional cost.  In time, other mapping agencies can and will further benefit one another by funding additional GeoServer improvements, like WFS 2.0 and [Application Schema](http://docs.geoserver.org/latest/en/user/data/app-schema/index.html) configurations for INSPIRE, but the Ordnance Survey deserves special recognition from all GeoServer users for taking the lead.

In addition to WMS 1.3, this release includes some **SLD 1.1 / SE 1.1 enhancements**.  It will be possible to use most SE 1.1 documents, though not every new option is fully supported yet.  User feedback on which new options we should support first is greatly appreciated.  Also funded by Ordnance Survey is a community module to implement the WMS extensions for INSPIRE View Service compliance—namely the language parameter and several extended capabilities fields.

The release also includes a few nice fixes and improvements from beta2, such as [upgrading CQL to ECQL](https://osgeo-org.atlassian.net/browse/GEOS-3928), and [a fix](https://osgeo-org.atlassian.net/browse/GEOS-4254) by Eli Miller, a newcomer to the GeoServer community, to allow the [REST Config API](http://docs.geoserver.org/latest/en/user/extensions/rest/index.html) to properly handle [SQL Views](http://docs.geoserver.org/latest/en/user/data/sqlview.html).

We encourage you to download GeoServer 2.1-beta3, try it out, and let us know if there are any bugs.  This software is still a beta, so we recommend testing extensively before running it in a production environment.  That said, we're hoping to move to 2.1.0 release candidates soon, so any and all testing will this process move along faster.

**Download GeoServer 2.1-beta3**

----

## GeoServer 2.1-beta3

Released on December 20, 2010

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/geoserver-2.1-beta3-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/geoserver-2.1-beta3-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/geoserver-2.1-beta3.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/geoserver-2.1-beta3.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/geoserver-2.1-beta3-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/geoserver-2.1-beta3-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/geoserver-2.1-beta3-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/geoserver-2.1-beta3-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-imagemosaic-jdbc-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-control-flow-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-ogr-plugin.zip/download)
- [RESTConfig](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-restconfig-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-wfsv-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/extensions/geoserver-2.1-beta3-wps-plugin.zip/download)

#### [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta3/)

SourceForge Release .

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 17024

## Release notes

Improvement:

* [GEOS-4261](https://osgeo-org.atlassian.net/browse/GEOS-4261) Create an extension point for plugins to add panels to admin pages

Bug:

* [GEOS-4146](https://osgeo-org.atlassian.net/browse/GEOS-4146) Class cast exception disposing of old feature type info cache entries
* [GEOS-4181](https://osgeo-org.atlassian.net/browse/GEOS-4181) GetFeature without INFO_FORMAT specified only returns features from first layer
* [GEOS-4229](https://osgeo-org.atlassian.net/browse/GEOS-4229) WCS 1.1 capabilities request should ignore the "version" parameter
* [GEOS-4252](https://osgeo-org.atlassian.net/browse/GEOS-4252) OpenLayers preview misses the required parameter srs
* [GEOS-4253](https://osgeo-org.atlassian.net/browse/GEOS-4253) Trying to validate the SLD results in an NPE
* [GEOS-4254](https://osgeo-org.atlassian.net/browse/GEOS-4254) REST API does not handle SQL Views properly
* [GEOS-4259](https://osgeo-org.atlassian.net/browse/GEOS-4259) NPE publishing two layers in a row
* [GEOS-4265](https://osgeo-org.atlassian.net/browse/GEOS-4265) DataStoreFileResource does not use workspace name to look up datastore on file upload
* [GEOS-4267](https://osgeo-org.atlassian.net/browse/GEOS-4267) WMS 1.3 service exception returned when version should match 1.1.1 but is not exact
