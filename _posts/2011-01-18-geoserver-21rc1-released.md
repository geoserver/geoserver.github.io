---
author: geoserver
comments: true
date: 2011-01-18 16:04:15+00:00
layout: post
link: http://blog.geoserver.org/2011/01/18/geoserver-21rc1-released/
slug: geoserver-21rc1-released
title: GeoServer 2.1-RC1 Released
wordpress_id: 837
categories:
- Announcements
- Features
---

The GeoServer community is happy to announce that the first release candidate of GeoServer 2.1 is now available for download. The team has been busy working on some great new improvements and features since 2.1-beta3.

First up is **GeoWebCache integration**, allowing clients to enjoy the benefits of tile caching through the regular GeoServer WMS endpoint. This enables GeoWebCache to transparently proxy for the GeoServer WMS without the need for a separate service endpoint. Taking advantage of the recently added **disk-quota** functionality, GeoWebCache now provides the ability to set limits on the amount of disk space used for storing tiles, allowing users to control and limit the size of the tile cache on disk. Big thanks to Gabriel Roldán for the great GeoWebCache improvements.

This release also brings some improvements to **RESTConfig**, which is now shipped with GeoServer by default so users need no longer install it as a separate plugin. Improvements to the API include the file upload operation that now allows for uploading files into an existing data store. This addition allows users to upload a shapefile and have it converted automatically into a PostGIS database, publishing it as a PostGIS layer rather than as a Shapefile layer. Finally, the API also supports recursive DELETE operations, making it more convenient to remove resources that contain other resources like stores or workspaces. Thanks to David Winslow and Justin Deoliveira of [OpenGeo](http://opengeo.org/) for these improvements.

Thanks to some great work from the folks at [GeoSolutions](http://www.geo-solutions.it/)**, raster reprojection performance** has improved significantly by using linear appoximations of transformation functions. This improvement was initially added in 2.1-beta3 but has continued to be improved for 2.1-RC1. Those interested should checkout this [article](http://geo-solutions.blogspot.com/2011/01/developers-corner-improving.html) that links to a white paper with the full technical details.

Last but certainly not least, thanks to Andrea Aime for the addition of a **Web Coverage Service** [request builder](http://jira.codehaus.org/secure/attachment/52920/requestBuilder10-nq8.png), a handy tool for graphically building WCS requests to test a coverage service. As clients for WCS have always been sparse, this tool goes a long way for making the service more usable.

We are happy to report the contribution of yet another translation of the web admin interface—special thanks to Oscar Fonts for submitting a **Catalan translation** and to [Geodata Sistemas](http://www.geodata.es) for funding the work.

Also worthy of thanks this round is Ivan Grcic who has submitted some excellent patches, including [bug fixes](https://osgeo-org.atlassian.net/browse/GEOS-4286) for WMS layer functionality. Thanks Ivan!

As always, a number of other bug fixes and improvements have made it into this release. Check out the [change log](#release-notes) for all new and noteworthy changes.

Download and try 2.1-RC1 now. You can help us reach the final 2.1 release by reporting any bugs in the [issue tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS) and sending feedback to the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users).

Thanks for supporting GeoServer!

----

## GeoServer 2.1-RC1

Released on Jan 17, 2011

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/geoserver-2.1-RC1-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/geoserver-2.1-RC1-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/geoserver-2.1-RC1.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/geoserver-2.1-RC1.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/geoserver-2.1-RC1-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/geoserver-2.1-RC1-htmldoc.zip/download)
- [PDF Documentation](http://downloads.sourceforge.net/geoserver/geoserver-2.1-RC1-pdfdoc.zip)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/geoserver-2.1-RC1-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-control-flow-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-ogr-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-wfsv-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC1/extensions/geoserver-2.1-RC1-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 16982

## Release notes

New Feature:

* [GEOS-4274](https://osgeo-org.atlassian.net/browse/GEOS-4274) Catalan translation
* [GEOS-4282](https://osgeo-org.atlassian.net/browse/GEOS-4282) WCS request builder

Improvement:

* [GEOS-4183](https://osgeo-org.atlassian.net/browse/GEOS-4183) Develop a RESTConfig analogous to the recursive deletes in Geoserver's UI
* [GEOS-4271](https://osgeo-org.atlassian.net/browse/GEOS-4271) Create Option to bypass Raster Direct Path
* [GEOS-4288](https://osgeo-org.atlassian.net/browse/GEOS-4288) GSIP 57 - authorization framework improvements
* [GEOS-4292](https://osgeo-org.atlassian.net/browse/GEOS-4292) Add ability to upload files into store of different type
* [GEOS-4297](https://osgeo-org.atlassian.net/browse/GEOS-4297) Disable layer when REST upload contains layer that cannot be completely configured

Bug:

* [GEOS-3826](https://osgeo-org.atlassian.net/browse/GEOS-3826) Geoserver GDAL ImageIO-ext extensions don't work on last Tomcat >= 6.0.24 versions
* [GEOS-3915](https://osgeo-org.atlassian.net/browse/GEOS-3915) While uploading a shapefile via REST, GeoServer does not consider workspaces/namespaces.
* [GEOS-4191](https://osgeo-org.atlassian.net/browse/GEOS-4191) traceback when clicking warning next to "reload feature type"
* [GEOS-4232](https://osgeo-org.atlassian.net/browse/GEOS-4232) Cascaded WMS layer cannot be properly managed by SecureCatalogImpl
* [GEOS-4238](https://osgeo-org.atlassian.net/browse/GEOS-4238) Unable to add directory via relative path of rshapefiles from the shapefile datastore configuration page
* [GEOS-4251](https://osgeo-org.atlassian.net/browse/GEOS-4251) WFS GetFeature with "JSON" outputFormat may cause an exception
* [GEOS-4268](https://osgeo-org.atlassian.net/browse/GEOS-4268) GeoServer 2.1.x would fail configuring large shapefiles on Windows
* [GEOS-4269](https://osgeo-org.atlassian.net/browse/GEOS-4269) If layer groups bounds are filled by hand the crs won't be persisted
* [GEOS-4270](https://osgeo-org.atlassian.net/browse/GEOS-4270) overlapping images extracted from the same ArcSDE raster don't quite match
* [GEOS-4273](https://osgeo-org.atlassian.net/browse/GEOS-4273) NullPointerException happens if WMS casade layer is used inside LayerGroup
* [GEOS-4286](https://osgeo-org.atlassian.net/browse/GEOS-4286) LayerPage does not handle new WMSStoreInfo class
* [GEOS-4287](https://osgeo-org.atlassian.net/browse/GEOS-4287) Anonymous types handling are broken in app-schema
* [GEOS-4293](https://osgeo-org.atlassian.net/browse/GEOS-4293) ogr2ogr output format will fail if no features are returned
* [GEOS-4295](https://osgeo-org.atlassian.net/browse/GEOS-4295) CatalogBuilder.buildLayer method does not handle WMSLayerInfo type
* [GEOS-4298](https://osgeo-org.atlassian.net/browse/GEOS-4298) Shape zip output format may fail in WPS
* [GEOS-4301](https://osgeo-org.atlassian.net/browse/GEOS-4301) Enable GetFeatureInfo for wms cascading layer
* [GEOS-4383](https://osgeo-org.atlassian.net/browse/GEOS-4383) WMS cascading URL port problem

Sub-task:

* [GEOS-4161](https://osgeo-org.atlassian.net/browse/GEOS-4161) Minimal GWC UI to configure the basics of integration with GeoServer
* [GEOS-4163](https://osgeo-org.atlassian.net/browse/GEOS-4163) WMS integration: let GWC sit in front of the GeoServer WMS to serve tiled content
* [GEOS-4164](https://osgeo-org.atlassian.net/browse/GEOS-4164) Integrate the GWC disk-quota module

Wish:

* [GEOS-1242](https://osgeo-org.atlassian.net/browse/GEOS-1242) Add text/xml as an output format for WMS exceptions
