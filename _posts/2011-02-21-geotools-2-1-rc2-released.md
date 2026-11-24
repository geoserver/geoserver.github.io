---
author: geoserver
comments: true
date: 2011-02-21 23:14:43+00:00
layout: post
link: http://blog.geoserver.org/2011/02/21/geotools-2-1-rc2-released/
slug: geotools-2-1-rc2-released
title: GeoServer 2.1-RC2 Released
wordpress_id: 885
categories:
- Announcements
---

The GeoServer community is happy to announce that the second release candidate of GeoServer 2.1 is now available for download. There is not much in the way of new features for this release, but the team has been busy fixing bugs. Checkout the [change log](#release-notes) for the list of fixes.

Download and try 2.1-RC2 now. You can help us reach the final 2.1 release by reporting any bugs in the [issue tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS) and sending feedback to the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users). Thanks for supporting GeoServer.

----

## GeoServer 2.1-RC2

Released on Feb 18, 2011

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/geoserver-2.1-RC2-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/geoserver-2.1-RC2-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/geoserver-2.1-RC2.exe/download)
- [Mac OS X Installer](http://downloads.sourceforge.net/geoserver/geoserver-2.1-RC2.dmg)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/geoserver-2.1-RC2-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/geoserver-2.1-RC2-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/geoserver-2.1-RC2-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/geoserver-2.1-RC2-javadoc.zip/download)
- [Release Notes](http://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/geoserver-2.1-RC2-release-notes.txt)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-control-flow-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-ogr-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-wfsv-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC2/extensions/geoserver-2.1-RC2-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 17077

## Release notes

New Feature:

* [GEOS-4274](https://osgeo-org.atlassian.net/browse/GEOS-4274) Catalan translation
* [GEOS-4309](https://osgeo-org.atlassian.net/browse/GEOS-4309) Add support for DirectConnect + MultipleGeodatabase in ArcSDE extension

Improvement:

* [GEOS-4180](https://osgeo-org.atlassian.net/browse/GEOS-4180) Enhance FormatOptionsKvpParser to support back slash escaping
* [GEOS-4201](https://osgeo-org.atlassian.net/browse/GEOS-4201) Allow to create global freemarker templates
* [GEOS-4216](https://osgeo-org.atlassian.net/browse/GEOS-4216) Small Typo on "Catalog Mode Configuration" page
* [GEOS-4321](https://osgeo-org.atlassian.net/browse/GEOS-4321) Hide the demo/tool page in case there is no links inside it
* [GEOS-4324](https://osgeo-org.atlassian.net/browse/GEOS-4324) Have CollectGeometries use type specific collections if possible
* [GEOS-4335](https://osgeo-org.atlassian.net/browse/GEOS-4335) Oracle Documentation - additional note on schema setting
* [GEOS-4362](https://osgeo-org.atlassian.net/browse/GEOS-4362) Add a community module providing  filter functions supporting cross layer filtering
* [GEOS-4366](https://osgeo-org.atlassian.net/browse/GEOS-4366) Integrated GWC is not caching layer groups
* [GEOS-4376](https://osgeo-org.atlassian.net/browse/GEOS-4376) Pass down background color to readers in direct rendering path
* [GEOS-4381](https://osgeo-org.atlassian.net/browse/GEOS-4381) reorganize web ui sidebar

Bug:

* [GEOS-4129](https://osgeo-org.atlassian.net/browse/GEOS-4129) Wrong display of Arabic labels
* [GEOS-4306](https://osgeo-org.atlassian.net/browse/GEOS-4306) Image Pyramid dies in fast path with npe
* [GEOS-4307](https://osgeo-org.atlassian.net/browse/GEOS-4307) STYLES parameter is not set on GetFeatureInfo request for cascading layers
* [GEOS-4311](https://osgeo-org.atlassian.net/browse/GEOS-4311) RenderedImageMapOutputFormat.readBestCoverage is improperly setting readParams
* [GEOS-4317](https://osgeo-org.atlassian.net/browse/GEOS-4317) INSPIRE WMS extension: the inspire_vs.xsd is missing locally
* [GEOS-4318](https://osgeo-org.atlassian.net/browse/GEOS-4318) INSPIRE WMS extension: strange artifact appended to metadata URL
* [GEOS-4325](https://osgeo-org.atlassian.net/browse/GEOS-4325) Allow setting of proxy base url via web.xml
* [GEOS-4326](https://osgeo-org.atlassian.net/browse/GEOS-4326) ResourcePoolInitializer sets the feature type cache size to 0 regardless of the actual configuration
* [GEOS-4328](https://osgeo-org.atlassian.net/browse/GEOS-4328) Demo SRS list area of validity preview is broken
* [GEOS-4329](https://osgeo-org.atlassian.net/browse/GEOS-4329) ConcurrentModificationException in GetFeature under heavy load
* [GEOS-4331](https://osgeo-org.atlassian.net/browse/GEOS-4331) Significant slow down in GetFeature execution times
* [GEOS-4334](https://osgeo-org.atlassian.net/browse/GEOS-4334) Allow log file location to be overridden by enviroment variable
* [GEOS-4337](https://osgeo-org.atlassian.net/browse/GEOS-4337) RGBA raster + direct raster path + JPEG output -> inverted colors
* [GEOS-4341](https://osgeo-org.atlassian.net/browse/GEOS-4341) The rest dispatcher fails to set the content type to "text/plain" when reporting back an error message
* [GEOS-4345](https://osgeo-org.atlassian.net/browse/GEOS-4345) Wrong URL's generated for KML overlays
* [GEOS-4360](https://osgeo-org.atlassian.net/browse/GEOS-4360) Translucent colors in input + solid background not properly handled by the direct render path
* [GEOS-4363](https://osgeo-org.atlassian.net/browse/GEOS-4363) The direct raster path ignores map decorations
* [GEOS-4367](https://osgeo-org.atlassian.net/browse/GEOS-4367) Style modifications through restconfig do not cause a catalog event to be thrown, preventing GWC to clear the cache
* [GEOS-4370](https://osgeo-org.atlassian.net/browse/GEOS-4370) Restore ThreadPoolExecutor support for multithreaded imageMosaic/imagePyramid granules loading
* [GEOS-4371](https://osgeo-org.atlassian.net/browse/GEOS-4371) GeoServer hangs because multi-threaded loader is null
* [GEOS-4374](https://osgeo-org.atlassian.net/browse/GEOS-4374) ogr2ogr module can generate corrupt zip files
* [GEOS-4377](https://osgeo-org.atlassian.net/browse/GEOS-4377) Changing settings in WCS dialog results in type conversion error
* [GEOS-4385](https://osgeo-org.atlassian.net/browse/GEOS-4385) Using a global thread pool for rendering might break stores that make heavy usage of thread locals
* [GEOS-4391](https://osgeo-org.atlassian.net/browse/GEOS-4391) WCS configuration submit throws java.lang.ClassCastException error.

Task:

* [GEOS-4160](https://osgeo-org.atlassian.net/browse/GEOS-4160) Better GWC integation - short term goals
* [GEOS-4310](https://osgeo-org.atlassian.net/browse/GEOS-4310) Add Proxy Server instuctions to WFS Data Store Doco

Sub-task:

* [GEOS-4162](https://osgeo-org.atlassian.net/browse/GEOS-4162) Front page capabilities link integration
* [GEOS-4322](https://osgeo-org.atlassian.net/browse/GEOS-4322) List only available languages in WMS configuration UI for INSPIRE language selection
