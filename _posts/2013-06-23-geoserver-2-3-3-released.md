---
author: geoserver
comments: true
date: 2013-06-23 10:35:59+00:00
layout: post
link: http://blog.geoserver.org/2013/06/23/geoserver-2-3-3-released/
slug: geoserver-2-3-3-released
title: GeoServer 2.3.3 Released
wordpress_id: 1450
categories:
- Announcements
---

The GeoServer team is pleased to announce the release of GeoServer 2.3.3:



	
  * Downloads ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/geoserver-2.3.3-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/geoserver-2.3.3-war.zip/download), [dmg](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/geoserver-2.3.3.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/geoserver-2.3.3.exe/download)) are listed on the GeoServer 2.3.3 page along with documentation and extensions.

	
    * This release includes and is made in conjunction with [GeoTools 9.3](http://geotoolsnews.blogspot.com.au/2013/06/geotools-93-released.html).




	
  * Thanks to [Warwickshire County Council ](http://www.warwickshire.gov.uk/)for some great GeoWebCache integration work:

	
    * GeoWebCache tile layer HTTP cache headers are now taken from GeoServer layer configration

	
    * GeoWebCache settings are now correctly saved on Windows




	
  * A wide range of improvements provided by the community

	
    * Scale hints now exposed in WMS GetCapabilities document

	
    * Fixed Symbology Encoding 1.1 encoding of relative external graphics

	
    * Addressed axis order issues cascading WMS 1.3.0 services through GeoServer





More details can be found in the [GeoServer 2.3.3 Release Notes](#release-notes).

----

## GeoServer 2.3.3

Released on 23 June 2013

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/geoserver-2.3.3-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/geoserver-2.3.3-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/geoserver-2.3.3.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/geoserver-2.3.3.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/geoserver-2.3.3-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/geoserver-2.3.3-htmldoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/geoserver-2.3.3-javadoc.zip/download)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-vpf-plugin.zip/download)
- [INSPIRE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-inspire-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-ogr-plugin.zip/download)
- [XSLT output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-xslt-plugin.zip/download)

- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-wps-plugin.zip/download)
- [CAS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-cas-plugin.zip/download)
- Monitor ([Core](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-monitor-plugin.zip/download), [Hibernate](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.3/extensions/geoserver-2.3.3-monitor-hibernate-plugin.zip/download))

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19231

## Release notes

Improvement:

* [GEOS-572](https://osgeo-org.atlassian.net/browse/GEOS-572) Expose scale hints in WMS capabilities documents
* [GEOS-4760](https://osgeo-org.atlassian.net/browse/GEOS-4760) Make GWC tile layers use the GeoServer layer's http caching settings

Bug:

* [GEOS-3387](https://osgeo-org.atlassian.net/browse/GEOS-3387) Metadata links should be included in the WFS capabilites document as well
* [GEOS-5536](https://osgeo-org.atlassian.net/browse/GEOS-5536) GeoWebCache settings won't be persisted on Windows
* [GEOS-5618](https://osgeo-org.atlassian.net/browse/GEOS-5618) By enabling applicaiton schema joining support, WFS getfeature request on parent table returns all child records only for first parent record!- Incorrect response
* [GEOS-5754](https://osgeo-org.atlassian.net/browse/GEOS-5754) Some "Save" buttons do not work with Google Chrome
* [GEOS-5760](https://osgeo-org.atlassian.net/browse/GEOS-5760) Documentation not referrencing Xms correctly.
* [GEOS-5785](https://osgeo-org.atlassian.net/browse/GEOS-5785) Authentication GUI does not persist the changes
* [GEOS-5786](https://osgeo-org.atlassian.net/browse/GEOS-5786) GWC - Tile gutter is not cropped when metatile contains only one tile
* [GEOS-5800](https://osgeo-org.atlassian.net/browse/GEOS-5800) GeoServer won't parse relative external graphic locations in SE 1.1 styles
* [GEOS-5810](https://osgeo-org.atlassian.net/browse/GEOS-5810) Packaging error for the CAS extension
* [GEOS-5816](https://osgeo-org.atlassian.net/browse/GEOS-5816) Error with WCS 1.0 and GetCoverage with bilinear interpolation
* [GEOS-5818](https://osgeo-org.atlassian.net/browse/GEOS-5818) WMS 1.3 cascading broken after GEOT-4283 changes
* [GEOS-5840](https://osgeo-org.atlassian.net/browse/GEOS-5840) Changing the default style of a layer won't cause truncation of the tile caches for layer groups containing the layer
* [GEOS-5844](https://osgeo-org.atlassian.net/browse/GEOS-5844) WMS virtual service will throw NPE on GetCapabilities w/ more than one layer in workspace
* [GEOS-7783](https://osgeo-org.atlassian.net/browse/GEOS-7783) CLONE - GeoWebCache settings won't be persisted on Windows
