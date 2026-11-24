---
author: geoserver
comments: true
date: 2011-06-25 05:21:27+00:00
layout: post
link: http://blog.geoserver.org/2011/06/25/geoserver-2-1-1-released/
slug: geoserver-2-1-1-released
title: GeoServer 2.1.1 Released
wordpress_id: 994
categories:
- Announcements
tags:
- '2.1'
- GeoServer
- release
---

Close on the heels of the release of our newest stable branch, the GeoServer team is pleased to announce the release of GeoServer 2.1.1.  While primarily a bug-fixing release, a number of enhancements have been made, including support for the upcoming [PostGIS](http://www.postgis.org/) 2.0, the addition of a number of new WPS processes and the addition of the [Teradata](http://docs.geoserver.org/2.1.1/user/data/teradata.html) database extension to the release.  As always, there are a great many people to thank for the successful release.  Our contributors continue their tireless efforts to move GeoServer forward.  Our users and advocates provide invaluable feedback and direction to the project.  [Sponsoring companies](https://web.archive.org/web/20110625/http://geoserver.org/display/GEOS/Commercial+Support) and groups provide much needed funding to drive the addition of new functionality.  This release I would like to draw special attention to a few contributions.



	
  * Rudi Hochmeister has contributed a patches to our logging system to simplify debugging and to fix a number of issues in our developer documentation.

	
  * Gianni Barrotta, Andrea Di Nora, and Pietro Arena have contributed a number of new WPS processes to the project.

	
  * Robert Coup has identified inconsistencies in the handling of URLs in the KML and GeoRSS output formats and has contributed patches to bring those in line with the rest of the code base.

	
  * Matt Bertrand has added support for the definition of character set during shapefile uploads and associated testing.


Contributions like these help keep GeoServer responsive to the needs of our community and allow us to continue providing a stable and useful product.  Thank you!  Thanks also go to [LISAsoft](https://web.archive.org/web/20110625/http://www.lisasoft.com) for sponsoring this release.  Please download GeoServer 2.1.1, try it out, and provide feedback on the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users).  Your feedback helps GeoServer to continue to improve.

----

## GeoServer 2.1.1

Released on June 23, 2011

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/geoserver-2.1.1-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/geoserver-2.1.1-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/geoserver-2.1.1.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/geoserver-2.1.1.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/geoserver-2.1.1-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/geoserver-2.1.1-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/geoserver-2.1.1-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/geoserver-2.1.1-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-control-flow-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-ogr-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-wfsv-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.1/extensions/geoserver-2.1.1-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 17360

## Release notes

New Feature:

* [GEOS-4046](https://osgeo-org.atlassian.net/browse/GEOS-4046) SHAPE-ZIP output format - allow parameter for output file name
* [GEOS-4347](https://osgeo-org.atlassian.net/browse/GEOS-4347) Create a dispatchercallback interface for rest

Improvement:

* [GEOS-1337](https://osgeo-org.atlassian.net/browse/GEOS-1337) Find the best option to handle 2/4 bits png when using the native encoder
* [GEOS-4175](https://osgeo-org.atlassian.net/browse/GEOS-4175) REST service to show a list of fonts available to the java runtime
* [GEOS-4184](https://osgeo-org.atlassian.net/browse/GEOS-4184) Enable SQL View parameters to be specified per layer
* [GEOS-4284](https://osgeo-org.atlassian.net/browse/GEOS-4284) WPS Topological processes
* [GEOS-4291](https://osgeo-org.atlassian.net/browse/GEOS-4291) enable logging about gzip compression
* [GEOS-4343](https://osgeo-org.atlassian.net/browse/GEOS-4343) some improvements to GeoServerTablePanel to better support large collections
* [GEOS-4500](https://osgeo-org.atlassian.net/browse/GEOS-4500) Metadata URL's for LayerGroups
* [GEOS-4503](https://osgeo-org.atlassian.net/browse/GEOS-4503) Make SHAPE-ZIP WFS output format capable of sending .prj files in ESRI WKT format
* [GEOS-4540](https://osgeo-org.atlassian.net/browse/GEOS-4540) logging buffer for XML post requests shouldnt be hardcoded
* [GEOS-4566](https://osgeo-org.atlassian.net/browse/GEOS-4566) Make ogr2ogr output format work with v 1.8 too
* [GEOS-4577](https://osgeo-org.atlassian.net/browse/GEOS-4577) URLMangler support in KML/GeoRSS
* [GEOS-4581](https://osgeo-org.atlassian.net/browse/GEOS-4581) Add PostGIS 2.0 compatibility

Bug:

* [GEOS-1697](https://osgeo-org.atlassian.net/browse/GEOS-1697) Incorrect drawing of multipolygon when using external graphic as graphic stroke
* [GEOS-3745](https://osgeo-org.atlassian.net/browse/GEOS-3745) changing the style in the OpenLayers preview is not reflected in getfeatureinfo requests
* [GEOS-3851](https://osgeo-org.atlassian.net/browse/GEOS-3851) "Compute from native bounds" should implicitly fire "Compute from data"
* [GEOS-3975](https://osgeo-org.atlassian.net/browse/GEOS-3975) Native SRS field should be text instead of an input field
* [GEOS-4242](https://osgeo-org.atlassian.net/browse/GEOS-4242) Failure to cascade WMS 1.3 servers
* [GEOS-4278](https://osgeo-org.atlassian.net/browse/GEOS-4278) A WCS request with image/tiff output format over a large coverage may make the server unresponsive
* [GEOS-4400](https://osgeo-org.atlassian.net/browse/GEOS-4400) PostGIS geography datatype - rendering problems
* [GEOS-4422](https://osgeo-org.atlassian.net/browse/GEOS-4422) Dataset sdhapefile - error when browsing for a file
* [GEOS-4435](https://osgeo-org.atlassian.net/browse/GEOS-4435) geoserver failed to render a shapefile data
* [GEOS-4521](https://osgeo-org.atlassian.net/browse/GEOS-4521) WPS DescribeProcess output is not valid
* [GEOS-4526](https://osgeo-org.atlassian.net/browse/GEOS-4526) Contrast enhancement not applied when falling out of the direct raster path
* [GEOS-4549](https://osgeo-org.atlassian.net/browse/GEOS-4549) Control flow + direct GWC integration = server lockup
* [GEOS-4551](https://osgeo-org.atlassian.net/browse/GEOS-4551) Avoid extra-read operation when read coverage is null. (RenderedImageMapOutputFormat)
* [GEOS-4553](https://osgeo-org.atlassian.net/browse/GEOS-4553) Moving circles on a line with dasharray
* [GEOS-4563](https://osgeo-org.atlassian.net/browse/GEOS-4563) Direct raster path + paletted tiff without transparency + transparency request in the request -> opaque image
* [GEOS-4564](https://osgeo-org.atlassian.net/browse/GEOS-4564) Teradata, SQL views do not work due to issue mapping geometry columns
* [GEOS-4565](https://osgeo-org.atlassian.net/browse/GEOS-4565) Raster rendering migth result in out of place images
* [GEOS-4567](https://osgeo-org.atlassian.net/browse/GEOS-4567) Regression: cannot login or logout anymore
* [GEOS-4580](https://osgeo-org.atlassian.net/browse/GEOS-4580) GeoTiff file handles are not closed immediately, can accumulate and result in OS level errors
* [GEOS-4582](https://osgeo-org.atlassian.net/browse/GEOS-4582) GeoServer can lose the connection to the EPSG database
* [GEOS-4583](https://osgeo-org.atlassian.net/browse/GEOS-4583) "Force declared srs" does not work for rasters
* [GEOS-4586](https://osgeo-org.atlassian.net/browse/GEOS-4586) OL layer preview does not honor the current filter in GetFeatureInfo
* [GEOS-4590](https://osgeo-org.atlassian.net/browse/GEOS-4590) Error trying to delete built-in styles
* [GEOS-4593](https://osgeo-org.atlassian.net/browse/GEOS-4593) "Edit Layer" title shows up three times in the publish layer settings page
* [GEOS-4594](https://osgeo-org.atlassian.net/browse/GEOS-4594) PDF map output of very small size will fail to be generated using the partial buffer strategy
* [GEOS-4600](https://osgeo-org.atlassian.net/browse/GEOS-4600) orphaned link in devel guide
* [GEOS-4614](https://osgeo-org.atlassian.net/browse/GEOS-4614) GWC error after REST shapefile upload
* [GEOS-4627](https://osgeo-org.atlassian.net/browse/GEOS-4627) Cannot set the watermark to a local file anymore
* [GEOS-4628](https://osgeo-org.atlassian.net/browse/GEOS-4628) KML does not use the same FeatureTypeStyle activation rules as StreamingRenderer
* [GEOS-4674](https://osgeo-org.atlassian.net/browse/GEOS-4674) Attribute restriction are not applied when not accompained by a corresponding filter
* [GEOS-4688](https://osgeo-org.atlassian.net/browse/GEOS-4688) Cann't create a new Workspace

Task:

* [GEOS-2854](https://osgeo-org.atlassian.net/browse/GEOS-2854) Document dynamic symbolizers (for real)
* [GEOS-4538](https://osgeo-org.atlassian.net/browse/GEOS-4538) Add extension point to allow contributing content to the Web UI home page body
* [GEOS-4571](https://osgeo-org.atlassian.net/browse/GEOS-4571) Add a WEB-UI extension point to contribute LayerGroup configuration panels
* [GEOS-4575](https://osgeo-org.atlassian.net/browse/GEOS-4575) Upgrade Teradata module to extension

Wish:

* [GEOS-3528](https://osgeo-org.atlassian.net/browse/GEOS-3528) Filtering capabilities for coverage plugins
