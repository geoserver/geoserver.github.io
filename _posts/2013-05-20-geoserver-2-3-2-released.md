---
author: geoserver
comments: true
date: 2013-05-20 03:33:28+00:00
layout: post
link: http://blog.geoserver.org/2013/05/19/geoserver-2-3-2-released/
slug: geoserver-2-3-2-released
title: GeoServer 2.3.2 released
wordpress_id: 1421
---

The GeoServer team is pleased to announce the release of GeoServer 2.3.2 for download.



	
  * This release includes and is made in conjunction with GeoTools 9.2.

	
  * [The INSPIRE plugin](http://docs.geoserver.org/stable/en/user/extensions/inspire/index.html) has now graduated to extension and is included in this release. This plugin adds WMS and WFS capabilities support for metadata required for compliance with the European INSPIRE directive.

	
  * The application schema support (app-schema) support plugin now enables joining by default for data sources that support it.

	
  * Fixed transformation problems with projections based on Hotine Oblique Mercator (variant B) (for example Swiss CH1903 / LV03)

	
  * Fixed WFS lockups when a WFS 1.1 GetFeature is providing a schema referring back to the same server DescribeFeatureType

	
  * A new option to limit the file browser to the data directory, geared towards high security/multi-tenant environments


More details can be found in the [GeoServer 2.3.2 Release Notes](#release-notes).

----

## GeoServer 2.3.2

Released on 17 May 2013

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/geoserver-2.3.2-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/geoserver-2.3.2-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/geoserver-2.3.2.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/geoserver-2.3.2.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/geoserver-2.3.2-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/geoserver-2.3.2-htmldoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/geoserver-2.3.2-javadoc.zip/download)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-ogr-plugin.zip/download)
- [XSLT output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-xslt-plugin.zip/download)
- [INSPIRE support](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-inspire-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-wps-plugin.zip/download)
- [CAS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-cas-plugin.geos-5810.zip/download)
- Monitor ([Core](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-monitor-plugin.zip/download), [Hibernate](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.2/extensions/geoserver-2.3.2-monitor-hibernate-plugin.zip/download))

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19195

## Release notes

Improvement:

* [GEOS-5693](https://osgeo-org.atlassian.net/browse/GEOS-5693) Make app-schema joining the default behaviour
* [GEOS-5791](https://osgeo-org.atlassian.net/browse/GEOS-5791) Graduate the INSIPIRE module to extension status
* [GEOS-5801](https://osgeo-org.atlassian.net/browse/GEOS-5801) Add option for wicket file browser not to expose other locations on the file system

Bug:

* [GEOS-4014](https://osgeo-org.atlassian.net/browse/GEOS-4014) `<snip>` /servlet-api-2.4.jar) - jar not loaded. See Servlet Spec 2.3, section 9.7.2. `<snip>`
* [GEOS-5210](https://osgeo-org.atlassian.net/browse/GEOS-5210) EPSG:21781 (CH1903) converts wrong to EPSG:4326 (WGS84)
* [GEOS-5636](https://osgeo-org.atlassian.net/browse/GEOS-5636) Adding a WMS cascaded layer from a GeoServer using Inspire extensions is very slow and leads to an Exception
* [GEOS-5784](https://osgeo-org.atlassian.net/browse/GEOS-5784) Missing release/ext-xslt.xml causes assembly:attached to fail
* [GEOS-5790](https://osgeo-org.atlassian.net/browse/GEOS-5790) Bad WFS request causes GeoServer to stop responding to certain requests types
* [GEOS-5803](https://osgeo-org.atlassian.net/browse/GEOS-5803) "mode" not "storage" used in default monitor.properties
* [GEOS-5804](https://osgeo-org.atlassian.net/browse/GEOS-5804) Adding XSLT module without proper configuration results in exceptions for normal GML requests
* [GEOS-5811](https://osgeo-org.atlassian.net/browse/GEOS-5811) Changing the SSL Port has no effect for filter chains already restricted to SSL requests
