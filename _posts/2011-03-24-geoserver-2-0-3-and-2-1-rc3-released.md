---
author: geoserver
comments: true
date: 2011-03-24 21:22:15+00:00
layout: post
link: http://blog.geoserver.org/2011/03/24/geoserver-2-0-3-and-2-1-rc3-released/
slug: geoserver-2-0-3-and-2-1-rc3-released
title: GeoServer 2.0.3 and 2.1-RC3 Released
wordpress_id: 897
categories:
- Announcements
- Features
---

This week has been a busy one for the GeoServer team with two releases coming out. The community is happy to announce the release of both 2.0.3 and 2.1-RC3.

GeoServer 2.0.3 is a maintenance release for the 2.0.x branch and contains [over 60 fixes and a few small new features](#release-notes). For those who have already upgraded to 2.1 there is nothing new but those still on 2.0.2 will find:



	
  * Ability to limit the amount of raster data read and delivered in each WCS request

	
  * A host of stabilization improvements in the WFS department, allowing GeoServer to widthstand higher WFS workloads

	
  * The new [control flow](http://docs.geoserver.org/stable/en/user/extensions/querylayer/index.html) extension allowing administrators to exert finer control over the number of parallel requests a GeoServer will handle, to ensure the server cannot be overloaded by malicious users or by a spike in traffic

	
  * Ability to read the GeoServer log file directly from the user interface, without the need to hunt it down in the data directory

	
  * Improvements to the [ogr2ogr](http://docs.geoserver.org/2.0.x/en/user/extensions/ogr.html) extension, allowing for the use of the famous ogr2ogr utility to extend the number of GeoServer WFS output formats

	
  * Finer control over shapefiles returned by the [SHAPE-ZIP output format](http://docs.geoserver.org/latest/en/user/services/wfs/outputformats.html#zipped-shapefile-customisation)


This release is likely the last of the 2.0.x series as the 2.1.0 release nears completion.

The third release candidate of GeoServer 2.1 also brings a number of [bug fixes and improvements](#release-notes) including:



	
  * The [querylayer](http://docs.geoserver.org/stable/en/user/community/querylayer/index.html) module which is a powerful extension that allows for cross layer filtering

	
  * Support for GML3 encoding in Atom/RSS output formats

	
  * Raster to vector conversion processes for WPS

	
  * Inclusion of WMS decorations in PDF output


And more. Check out the entire [change log](#release-notes) for more information.

Thanks to everyone who have worked hard over the past few months adding features and fixing bugs, in order to make this release happen. As usual, we encourage you to download, try it out, and provide feedback on the [users mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users).

----

## GeoServer 2.0.3

Released on March 11th, 2011

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/geoserver-2.0.3-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/geoserver-2.0.3-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/geoserver-2.0.3.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/geoserver-2.0.3.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/geoserver-2.0.3-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/geoserver-2.0.3-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/geoserver-2.1-RC3-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/geoserver-2.0.3-javadoc.zip/download)
- [Release Notes](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/release-notes-2.0.3.txt/download)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-imagemosaic-jdbc-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-charts-plugin.zip/download)
- [Control flow](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.0.3/geoserver-2.0.3-control-flow-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-ogr-plugin.zip/download)
- [RESTConfig](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-restconfig-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.3/extensions/geoserver-2.0.3-wfsv-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 16507


----

## GeoServer 2.1-RC3

Released on March 23, 2011

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/geoserver-2.1-RC3-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/geoserver-2.1-RC3-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/geoserver-2.1-RC3.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/geoserver-2.1-RC3.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/geoserver-2.1-RC3-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/geoserver-2.1-RC3-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/geoserver-2.1-RC3-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/geoserver-2.1-RC3-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-control-flow-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-ogr-plugin.zip/download)
- [RESTConfig](http://downloads.sourceforge.net/geoserver/geoserver-2.1-RC3-restconfig-plugin.zip)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-wfsv-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-RC3/extensions/geoserver-2.1-RC3-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 17257

## Release notes

### 2.0.3

Improvement:

* [GEOS-3824](https://osgeo-org.atlassian.net/browse/GEOS-3824) Improve the GDAL-ImageIO-Ext section User Documentation
* [GEOS-3856](https://osgeo-org.atlassian.net/browse/GEOS-3856) Add WCS limits (similar to those in WMS or WFS)
* [GEOS-3905](https://osgeo-org.atlassian.net/browse/GEOS-3905) Control CSS -> FeatureTypeStyle conversion with z-index parameter
* [GEOS-3920](https://osgeo-org.atlassian.net/browse/GEOS-3920) Add Labeling VendorOption SLD extensions to CSS module syntax
* [GEOS-3962](https://osgeo-org.atlassian.net/browse/GEOS-3962) Centralize reset/reload utilities, reset image and font caches
* [GEOS-3974](https://osgeo-org.atlassian.net/browse/GEOS-3974) Hide the REST API from bots by default
* [GEOS-3981](https://osgeo-org.atlassian.net/browse/GEOS-3981) Add USE_JAI_IMAGEREAD read parameter configuration to CoverageStore
* [GEOS-3994](https://osgeo-org.atlassian.net/browse/GEOS-3994) Allow KML icons to be placed in $DATA_DIR/styles subdirectories
* [GEOS-3999](https://osgeo-org.atlassian.net/browse/GEOS-3999) external.type and url.type support for datastores
* [GEOS-4000](https://osgeo-org.atlassian.net/browse/GEOS-4000) provide a note of where the data dir is in the UI
* [GEOS-4017](https://osgeo-org.atlassian.net/browse/GEOS-4017) Simple patch for ColorMapLegendCreator.java
* [GEOS-4031](https://osgeo-org.atlassian.net/browse/GEOS-4031) Show log file contents in the web GUI
* [GEOS-4052](https://osgeo-org.atlassian.net/browse/GEOS-4052) Allow integration tests to involve servlet filters as well
* [GEOS-4087](https://osgeo-org.atlassian.net/browse/GEOS-4087) Allow admin to specify a rendering buffer per layer
* [GEOS-4088](https://osgeo-org.atlassian.net/browse/GEOS-4088) Allow geoserver to start from an empty data directory
* [GEOS-4106](https://osgeo-org.atlassian.net/browse/GEOS-4106) Extend PropertyFileWatcher to other file types
* [GEOS-4121](https://osgeo-org.atlassian.net/browse/GEOS-4121) datastore connection paramters contain spaces and can't be updated via REST configuration
* [GEOS-4174](https://osgeo-org.atlassian.net/browse/GEOS-4174) REST config reload resource is not documented
* [GEOS-4188](https://osgeo-org.atlassian.net/browse/GEOS-4188) Allow GeoServer WFS to use the AUTO crs family
* [GEOS-4196](https://osgeo-org.atlassian.net/browse/GEOS-4196) Add support for single file outputs to ogr2ogr
* [GEOS-4199](https://osgeo-org.atlassian.net/browse/GEOS-4199) Improve shapefile output traceability and flexibility
* [GEOS-4200](https://osgeo-org.atlassian.net/browse/GEOS-4200) Allow WFS BBOX kvp parser to handle AUTO projections
* [GEOS-4203](https://osgeo-org.atlassian.net/browse/GEOS-4203) DescribeFeatureType should be working even when the namespace is not specified

Bug:

* [GEOS-3534](https://osgeo-org.atlassian.net/browse/GEOS-3534) DescribeFeatureType leaks memory
* [GEOS-3701](https://osgeo-org.atlassian.net/browse/GEOS-3701) java.lang.ClassCastException throwed by org.geoserver.config.util.XStreamPersister while saving a layer with "java.lang.Short" bondary values
* [GEOS-3755](https://osgeo-org.atlassian.net/browse/GEOS-3755) REST Api fails on layernames containing space
* [GEOS-3793](https://osgeo-org.atlassian.net/browse/GEOS-3793) Company's address is not shown in the GetCapabilities statement
* [GEOS-3873](https://osgeo-org.atlassian.net/browse/GEOS-3873) GeoServer binary distribution might use 100% constantly due to a bug in the JVM
* [GEOS-3899](https://osgeo-org.atlassian.net/browse/GEOS-3899) Various issues converting a CSS style with scale dependencies
* [GEOS-3939](https://osgeo-org.atlassian.net/browse/GEOS-3939) com.microsoft.sqlserver.jdbc.SQLServerException wrong query string on wms GetMap request
* [GEOS-3963](https://osgeo-org.atlassian.net/browse/GEOS-3963) Layer deleted through REST Interface is not completely removed
* [GEOS-3982](https://osgeo-org.atlassian.net/browse/GEOS-3982) Intermittent build failure in NewUserPageTest
* [GEOS-3985](https://osgeo-org.atlassian.net/browse/GEOS-3985) RetypeDataStore does not properly handle the case of a feature type renamed to a target name that is also available the native name of another feature type
* [GEOS-3987](https://osgeo-org.atlassian.net/browse/GEOS-3987) Clearing resource cache after adding a new store results in a NPE
* [GEOS-3988](https://osgeo-org.atlassian.net/browse/GEOS-3988) Feature type reload warning dialog fails to display properly
* [GEOS-3993](https://osgeo-org.atlassian.net/browse/GEOS-3993) Integrated GWC does not recognize newly added layer groups
* [GEOS-3995](https://osgeo-org.atlassian.net/browse/GEOS-3995) Build failure caused by unsafe URL-File conversion in KMLMapTransformer
* [GEOS-3996](https://osgeo-org.atlassian.net/browse/GEOS-3996) GetFeatureInfo in GML format against a raster layer will trigger an NPE
* [GEOS-3998](https://osgeo-org.atlassian.net/browse/GEOS-3998) GeoserverInfoImpl.setClientProperties has no effect:
* [GEOS-4002](https://osgeo-org.atlassian.net/browse/GEOS-4002) Error occurs when click on the Map CSS Demo link
* [GEOS-4004](https://osgeo-org.atlassian.net/browse/GEOS-4004) Build failure on Windows caused by unsafe File path manipulation in KMLMapTransformer
* [GEOS-4039](https://osgeo-org.atlassian.net/browse/GEOS-4039) Rendering Process fails when outside scale denominator of GraphicStroke
* [GEOS-4041](https://osgeo-org.atlassian.net/browse/GEOS-4041) Unsafe File to URL conversion causes failure when deployed in path with spaces
* [GEOS-4042](https://osgeo-org.atlassian.net/browse/GEOS-4042) ModificationProxy fails to notice changes in Map properties and improperly reports them for live collections
* [GEOS-4057](https://osgeo-org.atlassian.net/browse/GEOS-4057) Consider anonymous auth token as lack of authentication in the GUI
* [GEOS-4073](https://osgeo-org.atlassian.net/browse/GEOS-4073) Improved word wrap on in-image error reports
* [GEOS-4079](https://osgeo-org.atlassian.net/browse/GEOS-4079) GWC integration fails when control-flow code tries to access cookies
* [GEOS-4083](https://osgeo-org.atlassian.net/browse/GEOS-4083) Retyping datastore causes issue surrounding projections
* [GEOS-4084](https://osgeo-org.atlassian.net/browse/GEOS-4084) Layer Preview uses invalid layer params
* [GEOS-4085](https://osgeo-org.atlassian.net/browse/GEOS-4085) Transaction update fails when retyping in effect
* [GEOS-4108](https://osgeo-org.atlassian.net/browse/GEOS-4108) Layer group editor does not include the workspace prefix in layer names
* [GEOS-4140](https://osgeo-org.atlassian.net/browse/GEOS-4140) REST Config Plugin does not unescape URL
* [GEOS-4153](https://osgeo-org.atlassian.net/browse/GEOS-4153) Regression: Non-DataStore DataAccesses no longer recognised by GUI
* [GEOS-4165](https://osgeo-org.atlassian.net/browse/GEOS-4165) Error creating bounding box on SQL Server 2008 table with null geometry values
* [GEOS-4170](https://osgeo-org.atlassian.net/browse/GEOS-4170) Cache-control configuration ignored on raster Layer
* [GEOS-4171](https://osgeo-org.atlassian.net/browse/GEOS-4171) App-schema: test mappingName with special characters enclosed in quotes
* [GEOS-4195](https://osgeo-org.atlassian.net/browse/GEOS-4195) ogr2ogr output format should always use the GML intermediate representation
* [GEOS-4204](https://osgeo-org.atlassian.net/browse/GEOS-4204) ogr2ogr won't work on windows due to command line parsing issues with the WKT
* [GEOS-4206](https://osgeo-org.atlassian.net/browse/GEOS-4206) Mis-configured ogr2ogr output format breaks all GetFeature calls
* [GEOS-4270](https://osgeo-org.atlassian.net/browse/GEOS-4270) overlapping images extracted from the same ArcSDE raster don't quite match
* [GEOS-4325](https://osgeo-org.atlassian.net/browse/GEOS-4325) Allow setting of proxy base url via web.xml
* [GEOS-4329](https://osgeo-org.atlassian.net/browse/GEOS-4329) ConcurrentModificationException in GetFeature under heavy load
* [GEOS-4419](https://osgeo-org.atlassian.net/browse/GEOS-4419) attributes from AbstractFeatureType not filtered from application schema

Task:

* [GEOS-4013](https://osgeo-org.atlassian.net/browse/GEOS-4013) Move control-flow to extensions
* [GEOS-4310](https://osgeo-org.atlassian.net/browse/GEOS-4310) Add Proxy Server instuctions to WFS Data Store Doco

Sub-task:

* [GEOS-4008](https://osgeo-org.atlassian.net/browse/GEOS-4008) Missing SLD in release configuration

### 2.1-RC3

New Feature:

* [GEOS-2324](https://osgeo-org.atlassian.net/browse/GEOS-2324) See revision # in the UI on non-tagged builds
* [GEOS-4123](https://osgeo-org.atlassian.net/browse/GEOS-4123) gml 3.2 output format
* [GEOS-4437](https://osgeo-org.atlassian.net/browse/GEOS-4437) Promote querylayer module to extension

Improvement:

* [GEOS-3641](https://osgeo-org.atlassian.net/browse/GEOS-3641) WMS decorations are not included in PDF
* [GEOS-4299](https://osgeo-org.atlassian.net/browse/GEOS-4299) Shave off the boundedBy attribute when reading a feature collection for wps usage
* [GEOS-4357](https://osgeo-org.atlassian.net/browse/GEOS-4357) Add raster to vector conversion processes
* [GEOS-4401](https://osgeo-org.atlassian.net/browse/GEOS-4401) Add support for GML encoding in RSS/Atom output formats
* [GEOS-4405](https://osgeo-org.atlassian.net/browse/GEOS-4405) The direct rendering path expands grayscale images to RGB even when not necessary
* [GEOS-4420](https://osgeo-org.atlassian.net/browse/GEOS-4420) Docs about disabling the GS security subsystem need to be updated after the switch to Spring security

Bug:

* [GEOS-2034](https://osgeo-org.atlassian.net/browse/GEOS-2034) GeoRSS does not support GML encoding
* [GEOS-3018](https://osgeo-org.atlassian.net/browse/GEOS-3018) Content-type for se_inimage exceptions is the format
* [GEOS-3944](https://osgeo-org.atlassian.net/browse/GEOS-3944) Cannot access FID in SLD for Labels
* [GEOS-4105](https://osgeo-org.atlassian.net/browse/GEOS-4105) Most filter functions are not null safe
* [GEOS-4332](https://osgeo-org.atlassian.net/browse/GEOS-4332) New layer page has a double title
* [GEOS-4338](https://osgeo-org.atlassian.net/browse/GEOS-4338) WFS transactions against PostGIS will fail if index statistics are not up to date
* [GEOS-4369](https://osgeo-org.atlassian.net/browse/GEOS-4369) Double event notification in Catalog.save
* [GEOS-4389](https://osgeo-org.atlassian.net/browse/GEOS-4389) WMS 1.3 capabilities might throw an exception if a layer has any metadata name but a null ELEVATION_DOMAIN entry
* [GEOS-4403](https://osgeo-org.atlassian.net/browse/GEOS-4403) WMS GetMap requires SLD,SLD_BODY,etc... content to have a version
* [GEOS-4404](https://osgeo-org.atlassian.net/browse/GEOS-4404) ConcurrentModificationException in DefaultCatalogFacade.getLayerByName
* [GEOS-4406](https://osgeo-org.atlassian.net/browse/GEOS-4406) When sld schema not specified for validation purposes the internal lookup for a fallback fails
* [GEOS-4408](https://osgeo-org.atlassian.net/browse/GEOS-4408) OpenLayers output format fails if transparent=true is added to the request
* [GEOS-4410](https://osgeo-org.atlassian.net/browse/GEOS-4410) jaitools based processes won't work in Tomcat due to jai registration issues
* [GEOS-4411](https://osgeo-org.atlassian.net/browse/GEOS-4411) When rendering a gray image on openLayer, asking for png8/GIF results in ArrayIndexOutOfBoundsException
* [GEOS-4414](https://osgeo-org.atlassian.net/browse/GEOS-4414) geoserver-2.1-RC2-src release does not contain restconfig
* [GEOS-4415](https://osgeo-org.atlassian.net/browse/GEOS-4415) Map rendering may fail to pain certain symbolizers
* [GEOS-4431](https://osgeo-org.atlassian.net/browse/GEOS-4431) GWCTransactionListener breaks transaction processing for deletes over non qualified feature types
* [GEOS-4433](https://osgeo-org.atlassian.net/browse/GEOS-4433) GWCTransactionListener does not work for requests with no layer namespace declared
* [GEOS-4434](https://osgeo-org.atlassian.net/browse/GEOS-4434) ThreadPool for coverage access shutting down on catalog reload
* [GEOS-4438](https://osgeo-org.atlassian.net/browse/GEOS-4438) KML may return no data if the style has rules with scale dependencies
* [GEOS-4440](https://osgeo-org.atlassian.net/browse/GEOS-4440) GeoServer fails to load raster for one layer from file system but works with mounted volume
