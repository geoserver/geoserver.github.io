---
author: geoserver
comments: true
date: 2011-04-26 07:05:36+00:00
layout: post
link: http://blog.geoserver.org/2011/04/26/geoserver-2-1-rc5-released/
slug: geoserver-2-1-rc5-released
title: GeoServer 2.1-RC5 released
wordpress_id: 931
categories:
- Announcements
---



The GeoServer team is happy to announce the fifth release candidate for 2.1, now available for download.

This release brings some bug fixes and addresses a few residual regressions compared to the old 2.0.x series. In no particular order:



	
  * While GeoServer 2.1 uses extended CQL (ECQL) for all the CQL related activities, it now also preserve backwards compatibility with the old CQL language (in particular, new keywords in ECQL might have conflicted with valid CQL statements).

	
  * The compatibility towards Google Earth 6 was improved too, making Google Earth 6 properly display KMZ files with embedded images.

	
  * The [querylayer](http://docs.geoserver.org/2.1.x/en/user/extensions/querylayer/index.html) module, allowing for cross layer filtering, was promoted from community to extension module and is thus available as an official extension in the release.

	
  * Finally, GeoServer 2.1-RC5 avoids HTTP session creation on all OGC service paths, even when using basic authentication, providing better overall scalability.


Check out the [change log](#release-notes) for the full list.

Thanks to everyone who tested RC4 and helped us flush out these last few issues. You can continue to help us get to the official 2.1 release by downloading and trying out RC5. Be sure to report any issues in the [bug tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS) or on the [mailing list](mailto:geoserver-users@lists.sourceforge.net). Unless new regressions or serious bugs are found RC5 will be re-released as 2.1.0 final.

Thanks for using GeoServer!

----

## GeoServer 2.1-RC5

Released on April 20 2011

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/geoserver-2.1-RC5-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/geoserver-2.1-RC5-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/geoserver-2.1-RC5.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/geoserver-2.1-RC5.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/geoserver-2.1-RC5-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/geoserver-2.1-RC5-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/geoserver-2.1-RC5-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/geoserver-2.1-RC5-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-control-flow-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-imagemap-plugin.zip/download)
- [QueryLayer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-querylayer-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-ogr-plugin.zip/download)
- [RESTConfig](http://downloads.sourceforge.net/geoserver/geoserver-2.1-RC5-restconfig-plugin.zip)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-wfsv-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC5/extensions/geoserver-2.1-RC5-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 17324

## Release notes

Improvement:

* [GEOS-4424](https://osgeo-org.atlassian.net/browse/GEOS-4424) Make GML attribute overriding behaviour configurable
* [GEOS-4427](https://osgeo-org.atlassian.net/browse/GEOS-4427) Map preview broken when disabling global services
* [GEOS-4478](https://osgeo-org.atlassian.net/browse/GEOS-4478) Add a filter to help debugging spurious session creation
* [GEOS-4479](https://osgeo-org.atlassian.net/browse/GEOS-4479) create cql utility class that can fall back cql if ecql fails

Bug:

* [GEOS-4342](https://osgeo-org.atlassian.net/browse/GEOS-4342) Cannot update a postgis table using WFS 1.0/1.1
* [GEOS-4378](https://osgeo-org.atlassian.net/browse/GEOS-4378) Wrong URL's generated for raster overlays
* [GEOS-4425](https://osgeo-org.atlassian.net/browse/GEOS-4425) GeoServerLoader reload forgets to load initializers
* [GEOS-4444](https://osgeo-org.atlassian.net/browse/GEOS-4444) bbox computation : Problem with bounding box
* [GEOS-4445](https://osgeo-org.atlassian.net/browse/GEOS-4445) RC3 GetMap Request Renders Differently Depending on Bounding Box
* [GEOS-4472](https://osgeo-org.atlassian.net/browse/GEOS-4472) Unclosed BufferedInputStream in GeoServerLoader.readConfiguration
* [GEOS-4477](https://osgeo-org.atlassian.net/browse/GEOS-4477) Avoid session creation in all paths but the user interface
* [GEOS-4483](https://osgeo-org.atlassian.net/browse/GEOS-4483) Google Earth 6 shows Big Red Cross
* [GEOS-4492](https://osgeo-org.atlassian.net/browse/GEOS-4492) Problem creating jpeg tiles with geowebcache

Task:

* [GEOS-4484](https://osgeo-org.atlassian.net/browse/GEOS-4484) Update WPS to leverage on last jai-tools version (1.1.1)
