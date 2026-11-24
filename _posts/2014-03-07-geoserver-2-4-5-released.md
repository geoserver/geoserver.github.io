---
author: geoserver
comments: true
date: 2014-03-07 11:38:35+00:00
layout: post
link: http://blog.geoserver.org/2014/03/07/geoserver-2-4-5-released/
slug: geoserver-2-4-5-released
title: GeoServer 2.4.5 Released
wordpress_id: 1834
categories:
- Announcements
---

The GeoServer team is pleased to announce the release of GeoServer 2.4.5:



	
  * GeoServer 2.4.5 download page


This is the final stable release of the 2.4 series:

	
  * Oracle JNDI configuration now allows a fetch size parameter, limiting the number of rows that are retrieved in one gulp.

	
  * Fix for Polar stereographic projections

	
  * Fix for CSW namespace handling

	
  * Review the [change log](#release-notes) for the full list


Now is a good time to plan your upgrade to the 2.5 series. Our [extended release schedule]({% post_url 2014-02-27-extended-release-schedule %}) provides six month maintenance window allowing you to upgrade when ready.

This release is made in conjunction with [GeoTools 10.5](http://geotoolsnews.blogspot.com.au/2014/02/geotools-105-released.html).

----

## GeoServer 2.4.5

Released on

#### Download format

- [Binary (OS independent)](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.5/geoserver-2.4.5-bin.zip/download)
- [Web Archive](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.5/geoserver-2.4.5-war.zip)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4.5/geoserver-2.4.5.exe/download)

![](https://web.archive.org/web/20140307im_/http://geoserver.org/download/attachments/819222/download-sm-mac.png) Mac OS X Installer

- [Source Code](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.5/geoserver-2.4.5-src.zip)

#### Documentation

- [HTML Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.5/geoserver-2.4.5-htmldoc.zip)
- [API Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.5/geoserver-2.4.5-javadoc.zip)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-app-schema-plugin.zip)
- [ArcSDE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-arcsde-plugin.zip)
- [DB2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-db2-plugin.zip)
- [H2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-h2-plugin.zip)
- [MySQL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-mysql-plugin.zip)
- [Oracle](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-oracle-plugin.zip)
- [Pregeneralized features](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-feature-pregeneralized-plugin.zip)
- [SQL Server](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-sqlserver-plugin.zip)
- [Teradata](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-teradata-plugin.zip)
- [VPF](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-vpf-plugin.zip)
- [INSPIRE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-inspire-plugin.zip)

**Coverage store**

- [GDAL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-gdal-plugin.zip)
- [Image Pyramid](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-pyramid-plugin.zip)
- [JPEG2000](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-jp2k-plugin.zip)
- [JDBC Image Mosaic](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-imagemosaic-jdbc-plugin.zip)

**Other**

- [Chart dynamic symbolizer](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-charts-plugin.zip)
- [Control flow](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-control-flow-plugin.zip)
- [Cross layer filtering](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-querylayer-plugin.zip)
- [CSS styling](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-css-plugin.zip)
- [Excel output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-excel-plugin.zip)
- [GeoSearch](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-geosearch-plugin.zip)
- [Image Map output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-imagemap-plugin.zip)
- [OGR output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-ogr-plugin.zip)
- [XSLT output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-xslt-plugin.zip)
- [WPS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-wps-plugin.zip)
- [CAS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-cas-plugin.zip)
- Monitor ([Core](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-monitor-plugin.zip), [Hibernate](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-monitor-hibernate-plugin.zip))
- [CSW](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-csw-plugin.zip)
- Importer ([Core](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-importer-plugin.zip), [BerkeleyDB Backend](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-importer-bdb-plugin.zip))
- [WCS 2.0 EO](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-wcs2_0-eo-plugin.zip)
- [DXF output format for WFS/WPS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-dxf-plugin.zip)
- [WMS libJpegTurbo output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.5/geoserver-2.4.5-libjpeg-turbo-plugin.zip)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 20122

## Release notes

Improvement:

* [GEOS-5276](https://osgeo-org.atlassian.net/browse/GEOS-5276) Oracle JNDI store configuration should expose fetch size parameter
* [GEOS-6290](https://osgeo-org.atlassian.net/browse/GEOS-6290) Graduate dxf to extention on 2.4.x branch
* [GEOS-6328](https://osgeo-org.atlassian.net/browse/GEOS-6328) Use direct read when CoverageBuilder creates a sample 5x5 coverage
* [GEOS-6330](https://osgeo-org.atlassian.net/browse/GEOS-6330) REST HTML interface links to coverages contain coveragestores against instead of coverages
* [GEOS-6335](https://osgeo-org.atlassian.net/browse/GEOS-6335) Backport DynamicColorMap on 2.4.x
* [GEOS-6341](https://osgeo-org.atlassian.net/browse/GEOS-6341) Associate css style as default for a layer from the css demo page

Bug:

* [GEOS-5970](https://osgeo-org.atlassian.net/browse/GEOS-5970) POST-ing wps requests fails at the dispatcher level when using curl
* [GEOS-6046](https://osgeo-org.atlassian.net/browse/GEOS-6046) Geometry transformation validation fails in SE 1.1
* [GEOS-6052](https://osgeo-org.atlassian.net/browse/GEOS-6052) Geoserver does not start when a virtualtable misses the geometry section with oracle JNDI datastore
* [GEOS-6187](https://osgeo-org.atlassian.net/browse/GEOS-6187) wfs2 + resultType=hits + maxFeatures returns bad numberMatched
* [GEOS-6210](https://osgeo-org.atlassian.net/browse/GEOS-6210) CSS Extension does not allow whitespace in compound labels
* [GEOS-6216](https://osgeo-org.atlassian.net/browse/GEOS-6216) app-schema WFS 2.0.0 lat-lon axis ordering wrong and inconsistent with core GeoServer WFS behaviour
* [GEOS-6262](https://osgeo-org.atlassian.net/browse/GEOS-6262) GeoWebCache REST api /masstruncate is not working
* [GEOS-6292](https://osgeo-org.atlassian.net/browse/GEOS-6292) Cascading WMS: "java.lang.NullPointerException: Unable to transform referenced envelope, crs has not yet been provided"
* [GEOS-6298](https://osgeo-org.atlassian.net/browse/GEOS-6298) Build failure in gs-importer CSVDataStoreTest caused by bad URL`<->`File conversion
* [GEOS-6299](https://osgeo-org.atlassian.net/browse/GEOS-6299) 1bit Raster Transparency with transparent color, rendering failure
* [GEOS-6304](https://osgeo-org.atlassian.net/browse/GEOS-6304) Remove stax-api-1.0.1.jar from excel extension
* [GEOS-6314](https://osgeo-org.atlassian.net/browse/GEOS-6314) Allow JSON id generation to be optional
* [GEOS-6317](https://osgeo-org.atlassian.net/browse/GEOS-6317) GetRecordById is not accepted in POST requests
* [GEOS-6324](https://osgeo-org.atlassian.net/browse/GEOS-6324) Unable to configure WPS per workspace
* [GEOS-6331](https://osgeo-org.atlassian.net/browse/GEOS-6331) JDBCConfig only shows first page when paging a list of entries
* [GEOS-6336](https://osgeo-org.atlassian.net/browse/GEOS-6336) NetCDF output format: coordinates represent cell's center
* [GEOS-6344](https://osgeo-org.atlassian.net/browse/GEOS-6344) PNGJWriter logs exceptions at warning level even if the client closed the connection
* [GEOS-6347](https://osgeo-org.atlassian.net/browse/GEOS-6347) csw release packages misses the web-csw jar
* [GEOS-6351](https://osgeo-org.atlassian.net/browse/GEOS-6351) Printing plugin and CSS plugin are incompatible
* [GEOS-6354](https://osgeo-org.atlassian.net/browse/GEOS-6354) Polar stereographic projections broken
* [GEOS-6368](https://osgeo-org.atlassian.net/browse/GEOS-6368) CSW regression: record type handling is not namespace aware anymore
* [GEOS-6378](https://osgeo-org.atlassian.net/browse/GEOS-6378) CAS extension throws exception in case of empty URL params
* [GEOS-6412](https://osgeo-org.atlassian.net/browse/GEOS-6412) ECW Format no more present

Task:

* [GEOS-6302](https://osgeo-org.atlassian.net/browse/GEOS-6302) Create PNGJ Encoder Extension
* [GEOS-6305](https://osgeo-org.atlassian.net/browse/GEOS-6305) Remove unnecessary jar from WPS module archive
