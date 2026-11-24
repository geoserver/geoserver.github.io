---
author: geoserver
comments: true
date: 2012-06-04 10:59:02+00:00
layout: post
link: http://blog.geoserver.org/2012/06/04/geoserver-2-1-4-released/
slug: geoserver-2-1-4-released
title: GeoServer 2.1.4 released
wordpress_id: 1072
---

The GeoServer team is happy to announce the release of GeoServer 2.1.4, now available for download.

For the most part this is a maintainance release consisting of bug fixes, but as usual a few new features and improvements have managed to creep in. The release contains a total of [ 46 between bug fixes and improvements](#release-notes). Some of the new and noteworthy include:



	
  * various improvements to the SQL server data store extension

	
  * snappier GUI when working with data whose coordinate system cannot be direclty matched to a native EPSG code

	
  * more accurate GetFeatureInfo

	
  * support for geography columns in SQL views against PostGIS

	
  * GetLegendGraphics now takes into account UOM and DPI parameters

	
  * ip based control and blacklisting in the control-flow extension

	
  * before/after custom sql statements when hitting DBSMs (session oriented sql, can be used to switch authentication in the database


And more. Check out the [change log](#release-notes) for the entire list. A big thank you to all core developers, and a particular mention to users that contributed patches for this release. This includes:



	
  * Lars Lingner for addding the "forceLabel" parameter to GetLegendGraphic

	
  * Rudi Hochmeister for speeding up the JSON output format on large layers

	
  * Robert Coup for making SQL views parameters easier to pass in

	
  * Tony Young for making WCS 1.0 DescribeCoverage support the "all coverages" description mode

	
  * Hajo Kliemeck for making GetFeatureInfo work properly with user defined SLDs, and for improving legend decoration code

	
  * Tim Shaub for making the OpenLayers preview work with Firefox 10+


And of course, thanks to all those who helped out by filing bug reports.

Download 2.1.4, try it out and help us to continue to improve GeoServer by providing feedback on the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users) and reporting bugs in the [issue tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS).

----

## GeoServer 2.1.4

Released on June 04 2012

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/geoserver-2.1.4-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/geoserver-2.1.4-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/geoserver-2.1.4.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/geoserver-2.1.4.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/geoserver-2.1.4-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/geoserver-2.1.4-htmldoc.zip/download)
- [PDF Documentation](http://downloads.sourceforge.net/geoserver/geoserver-2.1.4-pdfdoc.zip)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/geoserver-2.1.4-javadoc.zip/download)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-ogr-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.4/extensions/geoserver-2.1.4-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 18238

## Release notes

New Feature:

* [GEOS-4693](https://osgeo-org.atlassian.net/browse/GEOS-4693) Some tiles are not being drawn when source is ArcSDE but it works okay with Geoserver 2.0.2. OR if source is PostGIS
* [GEOS-4922](https://osgeo-org.atlassian.net/browse/GEOS-4922) Authentication by unique key community module

Improvement:

* [GEOS-2630](https://osgeo-org.atlassian.net/browse/GEOS-2630) Allow user to choose which properties will be included in the GetFeatureInfo output
* [GEOS-3527](https://osgeo-org.atlassian.net/browse/GEOS-3527) Add an option to delete data when deleting configuration
* [GEOS-4918](https://osgeo-org.atlassian.net/browse/GEOS-4918) Support JDBC stores parametric session startup/teardown sql commands
* [GEOS-4927](https://osgeo-org.atlassian.net/browse/GEOS-4927) Refactoring of legend decoration to use getLegendGraphic
* [GEOS-4933](https://osgeo-org.atlassian.net/browse/GEOS-4933) New Layer page: avoid gathering the list of tables multiple times during a single page render
* [GEOS-4940](https://osgeo-org.atlassian.net/browse/GEOS-4940) Update Excel WFS reponse plugin to use streaming api for Excel 2007 documents
* [GEOS-4961](https://osgeo-org.atlassian.net/browse/GEOS-4961) Control flow module enhancements as described in GSIP - 72
* [GEOS-4988](https://osgeo-org.atlassian.net/browse/GEOS-4988) Layer retyping/renaming results in underlying DataStore.getTypeNames() being called continuously
* [GEOS-4994](https://osgeo-org.atlassian.net/browse/GEOS-4994) Add call to ImageIO.scanForPlugins() on startup to work around tomcat IIORegistry issues
* [GEOS-5004](https://osgeo-org.atlassian.net/browse/GEOS-5004) Allow ":" in SQL view parameter values without escaping
* [GEOS-5062](https://osgeo-org.atlassian.net/browse/GEOS-5062) Regenerate native and latlon bounding boxes through REST API
* [GEOS-5112](https://osgeo-org.atlassian.net/browse/GEOS-5112) GetFeatureInfo does not always take into account the external graphic size

Bug:

* [GEOS-1191](https://osgeo-org.atlassian.net/browse/GEOS-1191) Pattern fills do not align properly in tiled maps
* [GEOS-1739](https://osgeo-org.atlassian.net/browse/GEOS-1739) Filtering by multiple bounding box on SDE sources
* [GEOS-4069](https://osgeo-org.atlassian.net/browse/GEOS-4069) SLD examples for lines in the SLD-cookbook don't validate
* [GEOS-4384](https://osgeo-org.atlassian.net/browse/GEOS-4384) DWITHIN filter query fails when a request is made against a feature from an Oracle datastore
* [GEOS-4636](https://osgeo-org.atlassian.net/browse/GEOS-4636) LegendDecoration won't paint raster legends
* [GEOS-4675](https://osgeo-org.atlassian.net/browse/GEOS-4675) WMS 1.3.0 may to handle CRS whose native order is NORTH/EAST (for raster formats that use RasterLayerRequest class)
* [GEOS-4801](https://osgeo-org.atlassian.net/browse/GEOS-4801) Shapefile timezone parameter corrupted on catalog save
* [GEOS-4850](https://osgeo-org.atlassian.net/browse/GEOS-4850) Reprojecting UTM GeoTiff through WMS failed with MismatchedReferenceSystemException
* [GEOS-4860](https://osgeo-org.atlassian.net/browse/GEOS-4860) WCS 1.0's DescribeCoverage in GeoServer r16592 does not work with ArcMap 10.0
* [GEOS-4876](https://osgeo-org.atlassian.net/browse/GEOS-4876) wfsrequest.txt must not encode real server host name
* [GEOS-4888](https://osgeo-org.atlassian.net/browse/GEOS-4888) REST AbstractResource handling of MediaType.ALL causing NPE on GET requests
* [GEOS-4912](https://osgeo-org.atlassian.net/browse/GEOS-4912) NullPointerException if WPSResoruceManager.addResource is called without a set execution id
* [GEOS-4913](https://osgeo-org.atlassian.net/browse/GEOS-4913) A disappearing scaleline
* [GEOS-4930](https://osgeo-org.atlassian.net/browse/GEOS-4930) OpenLayers Map Preview always points to localhost
* [GEOS-4931](https://osgeo-org.atlassian.net/browse/GEOS-4931) Build failure in 2.1.x printing caused by Java 6 mapfish dependency
* [GEOS-4932](https://osgeo-org.atlassian.net/browse/GEOS-4932) JSON outputFormat extremely slow for GetFeature + BBOX with big WFS-layer
* [GEOS-4937](https://osgeo-org.atlassian.net/browse/GEOS-4937) Error "Operation on two geometries with different SRIDs" appears for views with null geometries in first row
* [GEOS-4945](https://osgeo-org.atlassian.net/browse/GEOS-4945) Blank Capabilities Responses when ProxyBaseURL is wrong and TILED=true
* [GEOS-4953](https://osgeo-org.atlassian.net/browse/GEOS-4953) Click on OpenLayers map fails to identify elements on small windows with Firefox 10
* [GEOS-4955](https://osgeo-org.atlassian.net/browse/GEOS-4955) Mismatch between WMS GetMap image and GetFeatureInfo output
* [GEOS-4958](https://osgeo-org.atlassian.net/browse/GEOS-4958) GetFeatureInfo and Getfeature will fail for shapefiles and directory of shapefiles configured in a workspace other than the default one
* [GEOS-4967](https://osgeo-org.atlassian.net/browse/GEOS-4967) geowebcache xml file provided in gwc-2.1.3.jar is invalid in case of uncommenting
* [GEOS-4995](https://osgeo-org.atlassian.net/browse/GEOS-4995) GetLegendGraphics dpi rescaling would not work if a specific rule is requested
* [GEOS-5005](https://osgeo-org.atlassian.net/browse/GEOS-5005) SQL Views don't include Geography Type Fields (from PostGIS)
* [GEOS-5008](https://osgeo-org.atlassian.net/browse/GEOS-5008) SLD with broken/invalid external graphics link causes large unrecoverable jump in CPU usage on GetLegendGraphic request
* [GEOS-5015](https://osgeo-org.atlassian.net/browse/GEOS-5015) Layers backed by a WMSLayer resource do not link back to it in the REST config xml representation
* [GEOS-5037](https://osgeo-org.atlassian.net/browse/GEOS-5037) Unable to set GEOSERVER_LOG_LOCATION with web.xml context parameter
* [GEOS-5045](https://osgeo-org.atlassian.net/browse/GEOS-5045) Shp publish into postgis datastore with MULTIPOLYGON EMPTY value violates check constraint.
* [GEOS-5088](https://osgeo-org.atlassian.net/browse/GEOS-5088) GeoServer WPS would execute at most one asynch request at a time
* [GEOS-5096](https://osgeo-org.atlassian.net/browse/GEOS-5096) Build hang in wps-core ExecuteTest.testConcurrentRequests on one CPU
* [GEOS-5109](https://osgeo-org.atlassian.net/browse/GEOS-5109) Do "already configured?" check based on native name, not published one
* [GEOS-5117](https://osgeo-org.atlassian.net/browse/GEOS-5117) OpenLayers preview won't switch to an alternate style anymore
* [GEOS-5225](https://osgeo-org.atlassian.net/browse/GEOS-5225) Teradata plugin needs 64 bit version of GeoServer/geojni.dll
* [GEOS-5282](https://osgeo-org.atlassian.net/browse/GEOS-5282) GetFeatureInfo is 10 to 20x slower on large layers in 2.1.4 compared to 2.1.3
