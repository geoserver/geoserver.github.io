---
author: aaime
comments: true
date: 2009-06-11 15:03:12+00:00
layout: post
link: http://blog.geoserver.org/2009/06/11/geoserver-175-released/
slug: geoserver-175-released
title: GeoServer 1.7.5 Released
wordpress_id: 222
categories:
- Announcements
tags:
- charts
- jndi
- production
- release
---

The GeoServer Team is happy to announce the the release of GeoServer 1.7.5, the sixth stable version in the 1.7 series.

This release contains some new features that are designed to improve the use of GeoServer in a production environment. Some [new WMS settings](http://docs.geoserver.org/1.7.5/user/services/wms/configuration.html) have been added that allow the administrator to limit the amount of resources consumed by each WMS request, specifically in terms of memory and time used.  It is also now possible to use [JNDI connection pools](http://docs.geoserver.org/1.7.5/user/data/jndi-connection-pools.html) for the DB2 and Oracle (NG) databases, providing better integration with enterprise environments.

The [features pregeneralized](http://docs.geoserver.org/1.7.5/user/tutorials/feature-pregeneralized/feature-pregeneralized_tutorial.html) datastore extension now allows an administrator to set up a vector data pyramid, and therefore significantly speed up WMS data serving over large data sets, especially those having geometries with a large number of coordinates.

The chart extension ([previously mentioned on this blog]({% post_url 2009-06-01-geoserver-chart-extension %})) is contained in the release, allowing the overlay of typical business charts on top of WMS maps.

For Windows users, this version introduces a new [service-based installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/geoserver-1.7.5-ng.exe/download), making GeoServer run like any other standard Windows service, and allowing for easier administration.

And, as usual, a host of [bug fixes](#release-notes) (over 40!) have been incorporated into this release.  Give it a try!

----

## GeoServer 1.7.5

Released on June 9, 2009

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/geoserver-1.7.5-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/geoserver-1.7.5-war.zip/download)

(NEW!) [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/geoserver-1.7.5-ng.exe/download)

- [Legacy Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/geoserver-1.7.5.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/geoserver-1.7.5.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/geoserver-1.7.5-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/geoserver-1.7.5-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/geoserver-1.7.5-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/geoserver-1.7.5-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Datastore**

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-db2-plugin.zip/download)
- [DB2 (Next Generation)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-db2ng-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-mysql-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-feature-pregeneralized-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-oracle-plugin.zip/download)
- [Oracle (Next Generation)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-oracleng-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-vpf-plugin.zip/download)

**Coveragestore**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-pyramid-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-charts-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-geosearch-plugin.zip/download)
- [Image Map](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-imagemap-plugin.zip/download)
- [OGR Output Format](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-ogr-plugin.zip/download)
- [REST](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-restconfig-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/extensions/geoserver-1.7.5-wfsv-plugin.zip/download)

#### [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.5/)

SourceForge Release 688538.

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 14788

## Release notes

New Feature:

* [GEOS-2517](https://osgeo-org.atlassian.net/browse/GEOS-2517) Service based Windows installer
* [GEOS-3031](https://osgeo-org.atlassian.net/browse/GEOS-3031) Include chart renderer as part of the release
* [GEOS-3085](https://osgeo-org.atlassian.net/browse/GEOS-3085) Add a memory allocation limit to WMS requests
* [GEOS-3086](https://osgeo-org.atlassian.net/browse/GEOS-3086) Add a response time limit to WMS requests
* [GEOS-3087](https://osgeo-org.atlassian.net/browse/GEOS-3087) Add an error count limit for WMS rendering requests

Improvement:

* [GEOS-2395](https://osgeo-org.atlassian.net/browse/GEOS-2395) Have MrSid layers configure with tiling and multithreading by default
* [GEOS-2500](https://osgeo-org.atlassian.net/browse/GEOS-2500) Performance degradation when there are a lot of ArcSDE layers
* [GEOS-2529](https://osgeo-org.atlassian.net/browse/GEOS-2529) REST CoverageListResource improvement
* [GEOS-2531](https://osgeo-org.atlassian.net/browse/GEOS-2531) REST CoverageResource improvement
* [GEOS-2614](https://osgeo-org.atlassian.net/browse/GEOS-2614) cql filter and wms group layers
* [GEOS-2851](https://osgeo-org.atlassian.net/browse/GEOS-2851) Support FeatureLayerConstraints in external SLD for WMS requests
* [GEOS-2868](https://osgeo-org.atlassian.net/browse/GEOS-2868) WFS 1.1.0 fails with filter having surface that is a plain polygon
* [GEOS-2869](https://osgeo-org.atlassian.net/browse/GEOS-2869) Geometry type cannot be set for WFS 1.0 with schema.xml file
* [GEOS-3074](https://osgeo-org.atlassian.net/browse/GEOS-3074) FilePublisher should return binary type for all not known mime types
* [GEOS-3109](https://osgeo-org.atlassian.net/browse/GEOS-3109) Have ResourcePool set the namespace when connecting to a datastore
* [GEOS-3131](https://osgeo-org.atlassian.net/browse/GEOS-3131) Expand the set of connection unwrappers for Oracle JNDI usage

Bug:

* [GEOS-2126](https://osgeo-org.atlassian.net/browse/GEOS-2126) GML featureTypeCache does not qualify entries by namespace
* [GEOS-2190](https://osgeo-org.atlassian.net/browse/GEOS-2190) WFS GetFeature outputformat=json returns error when you try to explicity or implicity have propertytype include geometry.
* [GEOS-2703](https://osgeo-org.atlassian.net/browse/GEOS-2703) Completely wipe out the "schema base" drop down from the feature type editor
* [GEOS-2743](https://osgeo-org.atlassian.net/browse/GEOS-2743) Oracle NG won't work properly when loose bbox is set
* [GEOS-2748](https://osgeo-org.atlassian.net/browse/GEOS-2748) SDE Raster issue - image shifted
* [GEOS-2754](https://osgeo-org.atlassian.net/browse/GEOS-2754) KML output for Oracle DataStore, worked in 1.7.0 not working in 1.7.2 without mode=refresh
* [GEOS-2771](https://osgeo-org.atlassian.net/browse/GEOS-2771) Some shp-files don't get rendered in Geoserver WMS.
* [GEOS-2782](https://osgeo-org.atlassian.net/browse/GEOS-2782) MaxFeatures equal to Integer.MAX_VALUE not disgarded when requesting multiple layers
* [GEOS-2790](https://osgeo-org.atlassian.net/browse/GEOS-2790) Cannot download WCS outputs coverages generated with store=true
* [GEOS-2842](https://osgeo-org.atlassian.net/browse/GEOS-2842) WFS-T feature insert Failure
* [GEOS-2926](https://osgeo-org.atlassian.net/browse/GEOS-2926) Unable to POST Coverages to CoverageStore
* [GEOS-2928](https://osgeo-org.atlassian.net/browse/GEOS-2928) ERDAS image rotating 45 degrees.
* [GEOS-2956](https://osgeo-org.atlassian.net/browse/GEOS-2956) Mosaic of ecw/mrsid files extremely slow
* [GEOS-2980](https://osgeo-org.atlassian.net/browse/GEOS-2980) SRS List link on WMS Layer Group page yields 404
* [GEOS-3055](https://osgeo-org.atlassian.net/browse/GEOS-3055) Freemarker template - *.ftl file is destroyed when applying/saving configuration
* [GEOS-3056](https://osgeo-org.atlassian.net/browse/GEOS-3056) ResourceInfoImpl equality fails to compare CRS
* [GEOS-3061](https://osgeo-org.atlassian.net/browse/GEOS-3061) external bitmap is not resizable for polygon fills
* [GEOS-3067](https://osgeo-org.atlassian.net/browse/GEOS-3067) Dispatcher use of ThreadLocal might induce (small) memory leaks
* [GEOS-3089](https://osgeo-org.atlassian.net/browse/GEOS-3089) PDF output format should directly stream to output instead of storing the PDF in memory before sending int
* [GEOS-3103](https://osgeo-org.atlassian.net/browse/GEOS-3103) Adding a feature type via restconfig does not reload the internal wfs schemas
* [GEOS-3112](https://osgeo-org.atlassian.net/browse/GEOS-3112) UI is not reloaded when rest calls are made
* [GEOS-3113](https://osgeo-org.atlassian.net/browse/GEOS-3113) schema encoder should respect prefix in the schema.xsd and schema.xml files
* [GEOS-3123](https://osgeo-org.atlassian.net/browse/GEOS-3123) Following the logout link when GeoServer is using a proxy leads to an NPE
* [GEOS-3125](https://osgeo-org.atlassian.net/browse/GEOS-3125) Schema created from ArcSDE feature class does not correspond to the definition in the database
* [GEOS-3130](https://osgeo-org.atlassian.net/browse/GEOS-3130) Failure reprojecting bbox in a WFS 1.1 request

Task:

* [GEOS-2988](https://osgeo-org.atlassian.net/browse/GEOS-2988) Remove Mortbay package from geoserver main module
* [GEOS-3059](https://osgeo-org.atlassian.net/browse/GEOS-3059) restconfig java sources miss copyright headers
* [GEOS-3080](https://osgeo-org.atlassian.net/browse/GEOS-3080) Update release guide: documentation
* [GEOS-3083](https://osgeo-org.atlassian.net/browse/GEOS-3083) Document usage of JNDI Connection pools in GeoServer
* [GEOS-3104](https://osgeo-org.atlassian.net/browse/GEOS-3104) Document rencently added WMS resource consumption limit
