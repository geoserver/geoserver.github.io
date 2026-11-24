---
author: geoserver
comments: true
date: 2013-03-18 19:42:49+00:00
layout: post
link: http://blog.geoserver.org/2013/03/18/geoserver-2-3-0-released-first-official-osgeo-release/
slug: geoserver-2-3-0-released-first-official-osgeo-release
title: GeoServer 2.3.0 released, first official OSGeo release!
wordpress_id: 1363
---

The GeoServer team is happy to announce the release of GeoServer 2.3.0, available for download.

This release contains six months worth of improvements and fixes to the GeoServer code base. Including several important new features and improvements such as:



	
  * A pluggable configuration subsystem (for the catalog and service configuration)

	
  * GeoWebCache clustering and disk quota improvements

	
  * More powerful layer groups and better control of the WMS capabilities layer tree

	
  * Several security subsystem improvements

	
  * WPS process whitelist (control which processes your WPS is exposing)

	
  * WMS dimensions support improvements (units, custom dimensions)

	
  * JSON and JSONP output format support in many OGC operations

	
  * The monitoring module finally graduating to official extension

	
  * Raster re-projection quality improvements and speedups

	
  * INSPIRE module improvements for the WFS protocol

	
  * A newfound ability to catalogue all components of GeoServer via a REST API


For those daring enough to try out nightly builds the 2.3.x series also offers a new scripting extension allowing you to write WPS processes and small applications in your preferred scripting language. Also included as a nightly community module available is a complete WCS 2.0 service implementation.

More information about the new features of the 2.3.x stream can be found in the  [GeoServer 2.3-beta release announcement]({% post_url 2013-01-29-geoserver-2-3-beta-released %}).

[![OSGeo Project](/img/uploads/OSGeo_project1.png)](/img/uploads/OSGeo_project1.png)

The good news do not stop there. GeoServer has finally completed the OSGeo incubation and it's now an official OSGeo project. Many thanks to all that participated, in particular Jody Garnett for constantly pushing forward, Landon Blake for mentoring us, and all the people that participated to the FOSS4G-AU code sprint in which all of the grunt work of provenance review was done. We want to thank in particular Jody Garnett, Adam Brown, Karin Stronkhorst, Luca Morandini and Joshua Vote for the hard work.

And last but not least there have been some bug fixes since the RC1 release, you can find a full list in the GeoServer 2.3.0 [changelog](#release-notes). Included in this list, for those willing to try out [nightly builds](http://gridlock.opengeo.org/geoserver/2.3.x/community-latest/), is a new[ fast WMS JPEG](http://geo-solutions.blogspot.it/2013/03/libjpeg-turbo.html) encoder based on [libjpeg-turbo](http://libjpeg-turbo.virtualgl.org/) which should give a nice boost to your raster data serving.

Download GeoServer 2.3, try it out, and provide feedback on the [GeoServer mailing list](https://web.archive.org/web/20130318/http://geoserver.org/display/GEOS/Mailing+Lists).  As with any new version, _be sure to backup your data directory before upgrading_.

**Thanks again for using GeoServer!**

**Download GeoServer 2.3**

----

## GeoServer 2.3.0

Released on March 18th 2013

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/geoserver-2.3.0-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/geoserver-2.3.0-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/geoserver-2.3.0.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/geoserver-2.3.0.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/geoserver-2.3.0-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/geoserver-2.3.0-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/geoserver-2.3.0-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/geoserver-2.3.0-javadoc.zip/download)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-ogr-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-wps-plugin.zip/download)
- [CAS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-cas-plugin.zip/download)
- Monitor ([Core](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-monitor-plugin.zip/download), [Hibernate](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.0/extensions/geoserver-2.3.0-monitor-hibernate-plugin.zip/download))

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19111

## Release notes

New Feature:

* [GEOS-5700](https://osgeo-org.atlassian.net/browse/GEOS-5700) libjpeg-turbo WMS Encoder as Community Module

Improvement:

* [GEOS-5666](https://osgeo-org.atlassian.net/browse/GEOS-5666) Various fixes for trimming
* [GEOS-5678](https://osgeo-org.atlassian.net/browse/GEOS-5678) Improve logging in geoserver.security
* [GEOS-5682](https://osgeo-org.atlassian.net/browse/GEOS-5682) Fix WCS20 ScaleToExtent and ScaleToSize operations

Bug:

* [GEOS-4761](https://osgeo-org.atlassian.net/browse/GEOS-4761) AdvancedDispatchFilter throws NPE for additional non directory servlet mappings
* [GEOS-5019](https://osgeo-org.atlassian.net/browse/GEOS-5019) Map wrapping can cause out of memory errors due to excessive geometry cloning
* [GEOS-5163](https://osgeo-org.atlassian.net/browse/GEOS-5163) Reordering layers in layer group pages results in broken table
* [GEOS-5319](https://osgeo-org.atlassian.net/browse/GEOS-5319) WFS-T insert of MultiPolygon exception with logging at VERBOSE
* [GEOS-5482](https://osgeo-org.atlassian.net/browse/GEOS-5482) GetLegendGraphic does not work for styles with rendering Transformation
* [GEOS-5514](https://osgeo-org.atlassian.net/browse/GEOS-5514) Oracle table list has too many "tables".
* [GEOS-5530](https://osgeo-org.atlassian.net/browse/GEOS-5530) GML2-GZIP - Wrong MIME type - Drop the format
* [GEOS-5625](https://osgeo-org.atlassian.net/browse/GEOS-5625) WMTS capabilities exception when a layer uses a grid subset with a positive (non zero) starting zoom level
* [GEOS-5656](https://osgeo-org.atlassian.net/browse/GEOS-5656) NPE when showing WPS info from workspace page
* [GEOS-5664](https://osgeo-org.atlassian.net/browse/GEOS-5664) Improve Coverage of KVP and XML Tests for WCS 2.0
* [GEOS-5672](https://osgeo-org.atlassian.net/browse/GEOS-5672) self-referential layer group
* [GEOS-5690](https://osgeo-org.atlassian.net/browse/GEOS-5690) WCS 2.0 GET DescribeCoverage fails against a list of coverageIds
* [GEOS-5691](https://osgeo-org.atlassian.net/browse/GEOS-5691) WCS 2.0 DescribeCoverage fails against image mosaic layers
* [GEOS-5692](https://osgeo-org.atlassian.net/browse/GEOS-5692) WCS 2.0 describe coverage can reports bands with all the same names when no color interpretation is available in the source data
* [GEOS-5696](https://osgeo-org.atlassian.net/browse/GEOS-5696) WCS services need to declare their namespace
* [GEOS-5705](https://osgeo-org.atlassian.net/browse/GEOS-5705) Enabled and advertised flags in the resource will get out of synch with the LayerInfo ones right after GUI editing
* [GEOS-5711](https://osgeo-org.atlassian.net/browse/GEOS-5711) org.geoserver.security.decorators.DecoratingWMSLayerInfo prefixName method calls itself indefinitely

Task:

* [GEOS-5702](https://osgeo-org.atlassian.net/browse/GEOS-5702) Add libjpeg-turbo community module to nightly deploy
