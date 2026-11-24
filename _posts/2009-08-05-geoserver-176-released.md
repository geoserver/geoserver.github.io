---
author: geoserver
comments: true
date: 2009-08-05 00:23:50+00:00
layout: post
link: http://blog.geoserver.org/2009/08/04/geoserver-176-released/
slug: geoserver-176-released
title: GeoServer 1.7.6 Released
wordpress_id: 235
categories:
- Announcements
- Features
tags:
- lisasoft
- release
- stable
---

GeoServer 1.7.6 marks the seventh stable release of the 1.7 series.

As the development focus of the GeoServer team moves more towards the eventual [release of 2.0](http://docs.geoserver.org/1.7.6/developer/policies/community-process.html#road-map), the 1.7 series is winding down.  This release focused mostly on [bug squashing](#release-notes) and general stability, with improvements implemented for the [shapefile output](http://docs.geoserver.org/1.7.6/user/services/wfs/outputformats.html) format and Next Generation [Oracle datastore](http://docs.geoserver.org/1.7.6/user/data/oracleng.html).

In addition, a few highly coveted features were added for this release.  The [ArcSDE datastore](http://docs.geoserver.org/1.7.6/user/data/arcsde.html) now supports connectivity to non-spatial tables as well as connection to a specified database version.  [KML support](http://docs.geoserver.org/1.7.6/user/google-earth/features/kmlheighttime.html) has also been extended to include output of 3d lines.

The WMS rendering issue discussed in a [previous post]({% post_url 2009-07-03-geoserver-175-critical-wms-patch %}) is also included in this release.

We encourage you to try it out a try and [let us know](mailto:geoserver-users@lists.sourceforge.net) how you like the latest and greatest.

----

## GeoServer 1.7.6

Released on August 4, 2009

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/geoserver-1.7.6-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/geoserver-1.7.6-war.zip/download)
- [Windows Service Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/geoserver-1.7.6-ng.exe/download)
- [Windows Console Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/geoserver-1.7.6.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/geoserver-1.7.6.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/geoserver-1.7.6-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/geoserver-1.7.6-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/geoserver-1.7.6-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/geoserver-1.7.6-javadoc.zip/download)
- [Release Notes](http://downloads.sourceforge.net/project/geoserver/GeoServer/1.7.6/geoserver-1.7.6-ReleaseNotes)
- [Change Log](#release-notes)

#### Extensions

**Datastore**

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-db2-plugin.zip/download)
- [DB2 (Next Generation)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-db2ng-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-mysql-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-feature-pregeneralized-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-oracle-plugin.zip/download)
- [Oracle (Next Generation)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-oracleng-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-vpf-plugin.zip/download)

**Coveragestore**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-pyramid-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-charts-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-geosearch-plugin.zip/download)
- [Image Map](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-imagemap-plugin.zip/download)
- [OGR Output Format](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-ogr-plugin.zip/download)
- [REST](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-restconfig-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/extensions/geoserver-1.7.6-wfsv-plugin.zip/download)

#### [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.6/)

SourceForge Release n/a.

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 15369

## Release notes

New Feature:

* [GEOS-2605](https://osgeo-org.atlassian.net/browse/GEOS-2605) GetCapabilities response for gwc
* [GEOS-3152](https://osgeo-org.atlassian.net/browse/GEOS-3152) ArcSDE DataStore level versioning support
* [GEOS-3153](https://osgeo-org.atlassian.net/browse/GEOS-3153) Allow serving non-spatial ArcSDE registered tables

Improvement:

* [GEOS-2645](https://osgeo-org.atlassian.net/browse/GEOS-2645) support 3D lines for output to kml in google earth
* [GEOS-2741](https://osgeo-org.atlassian.net/browse/GEOS-2741) Tilesorigin is confusing, make it work better and document it better
* [GEOS-3145](https://osgeo-org.atlassian.net/browse/GEOS-3145) Direct users to a JDK download from the Windows Installer
* [GEOS-3185](https://osgeo-org.atlassian.net/browse/GEOS-3185) Switch default KML generation mode to refresh
* [GEOS-3235](https://osgeo-org.atlassian.net/browse/GEOS-3235) ShapeZipOutputFormat cannot handle long shapefile incompatible schemas
* [GEOS-3278](https://osgeo-org.atlassian.net/browse/GEOS-3278) Make sure shapefiles generated by SHAPE-ZIP wfs output format do not contain dots in the name

Bug:

* [GEOS-2572](https://osgeo-org.atlassian.net/browse/GEOS-2572) Switching topp:states to new pophatch.sld style yields NPE
* [GEOS-2735](https://osgeo-org.atlassian.net/browse/GEOS-2735) Excel extension does not contain a README (or LICENSE) file
* [GEOS-2783](https://osgeo-org.atlassian.net/browse/GEOS-2783) getfeatureinfo requests return no features for some shapefiles
* [GEOS-2822](https://osgeo-org.atlassian.net/browse/GEOS-2822) Geoserver fails reprojecting 2238 and 900913 in BBOX spatial queries
* [GEOS-2931](https://osgeo-org.atlassian.net/browse/GEOS-2931) TimeKvpParser.getDate() is not thread safe -- WMS request causes NumberFormatException
* [GEOS-3049](https://osgeo-org.atlassian.net/browse/GEOS-3049) Failure to connect to a data store prevents WFS GetFeature to work on any other layer
* [GEOS-3137](https://osgeo-org.atlassian.net/browse/GEOS-3137) GeoServer assembly generates and empty geoserver-`<version>`-doc.zip file
* [GEOS-3138](https://osgeo-org.atlassian.net/browse/GEOS-3138) Add instructions for building the new Windows installer  to the Release Guide
* [GEOS-3139](https://osgeo-org.atlassian.net/browse/GEOS-3139) Add instructions on building PDF docs to the Release Guide
* [GEOS-3140](https://osgeo-org.atlassian.net/browse/GEOS-3140) The feature-pregeneralized plugin does not follow other plugins naming convention
* [GEOS-3156](https://osgeo-org.atlassian.net/browse/GEOS-3156) Render Bug 1.7.5
* [GEOS-3160](https://osgeo-org.atlassian.net/browse/GEOS-3160) Non Transparent PNG8
* [GEOS-3178](https://osgeo-org.atlassian.net/browse/GEOS-3178) startup.bat doesn't like pathnames with spaces
* [GEOS-3179](https://osgeo-org.atlassian.net/browse/GEOS-3179) BBOX request against big Shapefile ( FeatureInfo, WFS)  take a very long time
* [GEOS-3180](https://osgeo-org.atlassian.net/browse/GEOS-3180) Shapefile download - problem if null geometries
* [GEOS-3182](https://osgeo-org.atlassian.net/browse/GEOS-3182) GML2 output returns invalid feature bounds when geometry is null
* [GEOS-3184](https://osgeo-org.atlassian.net/browse/GEOS-3184) SHAPE-ZIP output fails for data in NAD83 (EPSG:4269)
* [GEOS-3201](https://osgeo-org.atlassian.net/browse/GEOS-3201) Raster legends don't show rules when labels are all empty
* [GEOS-3205](https://osgeo-org.atlassian.net/browse/GEOS-3205) Download doesn't contain plugin
* [GEOS-3208](https://osgeo-org.atlassian.net/browse/GEOS-3208) SDE instruction tell to grab jars from service pack, but it does not contain the requested jars
* [GEOS-3210](https://osgeo-org.atlassian.net/browse/GEOS-3210) filtering property names does not work properly with aliased feature type with json output
* [GEOS-3265](https://osgeo-org.atlassian.net/browse/GEOS-3265) Oracle (Next Generation): GetCapabilities fails if the table has a BLOB column
* [GEOS-3272](https://osgeo-org.atlassian.net/browse/GEOS-3272) Oracle NG cannot deal with views anymore
* [GEOS-3282](https://osgeo-org.atlassian.net/browse/GEOS-3282) Map shifted when using metatling and the current tile is very far away from the tile origin
* [GEOS-3287](https://osgeo-org.atlassian.net/browse/GEOS-3287) org.opengis.coverage.CannotEvaluateException when trying to execute GetFeatureInfo outside the bounds a DEM coverage

Task:

* [GEOS-2490](https://osgeo-org.atlassian.net/browse/GEOS-2490) update source release to include gwc and to reflect recent source tree chagnes
* [GEOS-2491](https://osgeo-org.atlassian.net/browse/GEOS-2491) update oracleng artifact to include the orgacleng jar
* [GEOS-2696](https://osgeo-org.atlassian.net/browse/GEOS-2696) Document new work with raster legends
* [GEOS-3211](https://osgeo-org.atlassian.net/browse/GEOS-3211) Port CatalogRepsitory from feature-pregeneralized extension to main
* [GEOS-3281](https://osgeo-org.atlassian.net/browse/GEOS-3281) Alter documentation to reflect change in default KML output
