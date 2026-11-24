---
author: bmmpxf
comments: true
date: 2009-03-11 14:49:30+00:00
layout: post
link: http://blog.geoserver.org/2009/03/11/geoserver-173-released/
slug: geoserver-173-released
title: GeoServer 1.7.3 Released
wordpress_id: 186
categories:
- Announcements
- Features
---

The GeoServer team is proud to announce the release of GeoServer 1.7.3.  The team has been busy in the six weeks since the previous release, with a code sprint in New York last month and a whopping [63 bugs and new features](#release-notes) fixed and implemented (respectively, of course).

This release brings improved support for **ArcSDE rasters**. Previously GeoServer only supported a limited number of SDE rasters, namely 3 and 4 band UCHAR with no color map support. GeoServer now supports all sample types up to an arbitrary number of bands, with color map support. Special thanks goes out to [MassGIS](http://www.mass.gov/mgis/) who provided the funding for this work, and Gabriel for his hard work implementing this feature.

In a first step towards a “multiple configurations” feature, GeoServer now allows you to [filter any capabilities request based on namespace](https://web.archive.org/web/20090311/http://geoserver.org/display/GEOSDOC/WCS+vendor+parameters).  A client can now ask for a particular subset of layers instead of having to receive all of them, which can greatly increase client performance if serving lots of layers.  (This works the same way for all services, although the above link is for WCS.)

There are quite a few new extensions for GeoServer, including:


<blockquote>**REST** - GeoServer now allows for [configuration via REST](https://web.archive.org/web/20090311/http://geoserver.org/display/GEOSDOC/RESTful+Configuration+API) ([REpresentational State Transfer](http://en.wikipedia.org/wiki/Representational_State_Transfer)).  This opens up a whole new world for interfacing with GeoServer, whether it's [a simple metadata update, a batch configuring of layers, or a one step shapefile upload](https://web.archive.org/web/20090311/http://geoserver.org/display/GEOSDOC/RESTFul+Configuration+API+Use+Cases).</blockquote>




<blockquote>**JDBC Image Mosaic** - This extension allows a coverage to be stored along with its pyramids in a [JDBC database](https://web.archive.org/web/20090311/http://geoserver.org/display/GEOSDOC/Using+the+ImageMosaic+JDBC+Plugin).  Special thanks to Christian Müller, who contributed this work!</blockquote>




<blockquote>**Excel** - Adding to the list of [WFS output formats](https://web.archive.org/web/20090311/http://geoserver.org/display/GEOSDOC/WFS+output+formats), feature data can now be output in Microsoft Excel (.XLS) format.  If you want tabular output, but don't need the full power of Excel, you can output comma-separated values (.CSV).  CSV output is available as part of the GeoServer's core, with no extension needed.</blockquote>




<blockquote>**Directory datastore** - In addition to the REST interface, there is now an even easier way to add lots of shapefiles to your catalog.  With the [directory datastore](https://web.archive.org/web/20090311/http://geoserver.org/display/GEOSDOC/Directory+datastore), you can point GeoServer to a directory full of shapefiles and just hit go (well, Submit, Apply, and Save) and all of the shapefiles will be loaded in as datastores.</blockquote>


Also, don't forget that [GeoWebCache](https://web.archive.org/web/20090311/http://geoserver.org/display/GEOSDOC/5.+GWC+-+GeoWebCache) is now built in to GeoServer (it was previously an extension), so GeoServer can immediately cache WMS tiles, which can vastly improve the speed of rendering.

As usual, we invite everyone to press that download button, try out those new extensions, [find (and report!) bugs](https://web.archive.org/web/20090311/http://geoserver.org/display/GEOSDOC/2+Issue+Tracker), and [give some feedback](https://web.archive.org/web/20090311/http://geoserver.org/display/GEOSDOC/1+Mailing+lists).  Thanks for using GeoServer!

----

## GeoServer 1.7.3

Released on March 9, 2009 ([Updated on March 17, 2009]({% post_url 2009-03-16-geoserver-173-updated %}))

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/geoserver-1.7.3a-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/geoserver-1.7.3a-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/geoserver-1.7.3a.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/geoserver-1.7.3a.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/geoserver-1.7.3-src.zip/download)

#### Documentation

- [Documentation (Site Export)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/geoserver-1.7.3-doc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/geoserver-1.7.3-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Datastore**

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-db2-plugin.zip/download)
- [DB2 (Next Generation)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-db2ng-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-oracle-plugin.zip/download)
- [Oracle (Next Generation)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-oracleng-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-vpf-plugin.zip/download)

**Coveragestore**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-pyramid-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [OGR Output Format](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-ogr-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-wfsv-plugin.zip/download)
- [REST](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-restconfig-plugin.zip/download)
- [Excel](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-excel-plugin.zip/download)
- [GeoExt Styler](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/styler-1.7.3.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-geosearch-plugin.zip/download)
- [Image Map](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/extensions/geoserver-1.7.3-imagemap-plugin.zip/download)

#### [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.3/)

SourceForge Release 666349.

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 14786

## Release notes

New Feature:

* [GEOS-1411](https://osgeo-org.atlassian.net/browse/GEOS-1411) Allow for optional callback parameter in GET requests that return json formatted structures
* [GEOS-2228](https://osgeo-org.atlassian.net/browse/GEOS-2228) Stroke width control impossible below 1.5 pixels
* [GEOS-2288](https://osgeo-org.atlassian.net/browse/GEOS-2288) Add directory data store to the list of standard GeoServer data stores
* [GEOS-2296](https://osgeo-org.atlassian.net/browse/GEOS-2296) Add ECW support in the GeoServer downloads
* [GEOS-2471](https://osgeo-org.atlassian.net/browse/GEOS-2471) Support namespace filter for WMS/WFS/WCS getCapabilities
* [GEOS-2496](https://osgeo-org.atlassian.net/browse/GEOS-2496) Move geosearch module to core distribution
* [GEOS-2497](https://osgeo-org.atlassian.net/browse/GEOS-2497) move restconfig to core module
* [GEOS-2502](https://osgeo-org.atlassian.net/browse/GEOS-2502) Labelling improvements
* [GEOS-2513](https://osgeo-org.atlassian.net/browse/GEOS-2513) Add gwc links to the main welcome page
* [GEOS-2520](https://osgeo-org.atlassian.net/browse/GEOS-2520) Bring Imageio-ext extension to supported status
* [GEOS-2550](https://osgeo-org.atlassian.net/browse/GEOS-2550) Have the OL map preview list a layer styles
* [GEOS-2567](https://osgeo-org.atlassian.net/browse/GEOS-2567) Support new ArcSDE raster formats
* [GEOS-2601](https://osgeo-org.atlassian.net/browse/GEOS-2601) Ability to turn on/off TextSymbolizer "left-to-right" aligning feature
* [GEOS-2615](https://osgeo-org.atlassian.net/browse/GEOS-2615) Bring CSV/Excel output formats to extension status

Improvement:

* [GEOS-1638](https://osgeo-org.atlassian.net/browse/GEOS-1638) If the native bbox is not known, use the 4326 one and reproject back (computing the native one might be way too expensive)
* [GEOS-2300](https://osgeo-org.atlassian.net/browse/GEOS-2300) Provide Expires header with Cache-Control: max-age
* [GEOS-2314](https://osgeo-org.atlassian.net/browse/GEOS-2314) Dispatcher.findXmlReader does not use "service" to find the proper output format
* [GEOS-2474](https://osgeo-org.atlassian.net/browse/GEOS-2474) Merge KMATTR and KMPLACEMARK
* [GEOS-2529](https://osgeo-org.atlassian.net/browse/GEOS-2529) REST CoverageListResource improvement
* [GEOS-2531](https://osgeo-org.atlassian.net/browse/GEOS-2531) REST CoverageResource improvement
* [GEOS-2580](https://osgeo-org.atlassian.net/browse/GEOS-2580) SVG output does not work when multiple fts are used
* [GEOS-2583](https://osgeo-org.atlassian.net/browse/GEOS-2583) Generate feature collection bounds in wfs 1.1 output when feature bounding is enabled
* [GEOS-2585](https://osgeo-org.atlassian.net/browse/GEOS-2585) OGROutputFormat: use shapefile as the intermediate data format when possible
* [GEOS-2586](https://osgeo-org.atlassian.net/browse/GEOS-2586) OGRoutputFormat: set content disposition
* [GEOS-2588](https://osgeo-org.atlassian.net/browse/GEOS-2588) Configuration reader triggers bounds computation for that whose native bbox is not known
* [GEOS-2589](https://osgeo-org.atlassian.net/browse/GEOS-2589) Use AbstractGridCoverage2DReader.getInfo():ServiceInfo to give implementations a chance to provide meaningful default metadata
* [GEOS-2591](https://osgeo-org.atlassian.net/browse/GEOS-2591) startup.bat in -bin distribution won't work if JAVA_HOME is not specified
* [GEOS-2644](https://osgeo-org.atlassian.net/browse/GEOS-2644) Do not print NULL and blank values from default KML template, rename attribute to field

Bug:

* [GEOS-479](https://osgeo-org.atlassian.net/browse/GEOS-479) TextSymbolizer with no Font --> no rendering
* [GEOS-1620](https://osgeo-org.atlassian.net/browse/GEOS-1620) SLD parser trims whitespaces from literals
* [GEOS-1661](https://osgeo-org.atlassian.net/browse/GEOS-1661) Label mixed syntax loses newlines
* [GEOS-1844](https://osgeo-org.atlassian.net/browse/GEOS-1844) Build failure in community/csv (invalid POM)
* [GEOS-2006](https://osgeo-org.atlassian.net/browse/GEOS-2006) Data stored in Oracle with a projection already assigned can not be shown properly
* [GEOS-2204](https://osgeo-org.atlassian.net/browse/GEOS-2204) Bbox filters + reprojection do fail again Oracle datastore
* [GEOS-2308](https://osgeo-org.atlassian.net/browse/GEOS-2308) GeoRSS polygon overlay in Google Maps Virtual Earth omits some polygons
* [GEOS-2429](https://osgeo-org.atlassian.net/browse/GEOS-2429) Grey Map because DataAccessException
* [GEOS-2452](https://osgeo-org.atlassian.net/browse/GEOS-2452) Coverage Configuration edit/apply/save may lead to problems
* [GEOS-2476](https://osgeo-org.atlassian.net/browse/GEOS-2476) Filters are not added to the GetFeatureInfo request in the standard GeoServer map preview
* [GEOS-2477](https://osgeo-org.atlassian.net/browse/GEOS-2477) Invalid namespace URI cause an  java.net.URISyntaxException from uDig
* [GEOS-2486](https://osgeo-org.atlassian.net/browse/GEOS-2486) GraphicStroke rendering poor due to missing antialiasing and interpolation
* [GEOS-2487](https://osgeo-org.atlassian.net/browse/GEOS-2487) Workaround misleading characted codes as reported by Windows charmap for TTF marks
* [GEOS-2488](https://osgeo-org.atlassian.net/browse/GEOS-2488) GraphicFill+Mark is not working
* [GEOS-2494](https://osgeo-org.atlassian.net/browse/GEOS-2494) "My GeoServer" link in the UI assumes that the instance is named .../geoserver
* [GEOS-2524](https://osgeo-org.atlassian.net/browse/GEOS-2524) WMS request does not work with coverage plugin producing a multiband image
* [GEOS-2536](https://osgeo-org.atlassian.net/browse/GEOS-2536) "My GeoServer" link on top is hardcoded to /geoserver
* [GEOS-2551](https://osgeo-org.atlassian.net/browse/GEOS-2551) Document the hatched fill related mark factory
* [GEOS-2590](https://osgeo-org.atlassian.net/browse/GEOS-2590) Remove "Properties" datastore option on "Create New Feature Data Set " page
* [GEOS-2593](https://osgeo-org.atlassian.net/browse/GEOS-2593) RequestCRSs and ResponseCRSs should be automagically set when forcing to a native crs
* [GEOS-2602](https://osgeo-org.atlassian.net/browse/GEOS-2602) Error thrown when tring to get back a non spatial property and the feature bounds from a wfs collection
* [GEOS-2603](https://osgeo-org.atlassian.net/browse/GEOS-2603) GetFeatureInfo returns html tables without css style if more than one layer is selected
* [GEOS-2606](https://osgeo-org.atlassian.net/browse/GEOS-2606) xmlns:xml attribute in GetFeature responses
* [GEOS-2608](https://osgeo-org.atlassian.net/browse/GEOS-2608) External sort / regionating appears to fill H2 database with empty tiles
* [GEOS-2610](https://osgeo-org.atlassian.net/browse/GEOS-2610) A True Type Font Symbol is flipped horizontally when using with a PolygonSymbolizer
* [GEOS-2619](https://osgeo-org.atlassian.net/browse/GEOS-2619) schema.xml no longer works
* [GEOS-2620](https://osgeo-org.atlassian.net/browse/GEOS-2620) LegacyCoverageInfoReader may throw NullPointerException when calling requestCRSs and responseCRSs on old info.xml which doesn't have these childs.
* [GEOS-2621](https://osgeo-org.atlassian.net/browse/GEOS-2621) MapPreview NPE when there is a projected layer with no native bbox configured
* [GEOS-2622](https://osgeo-org.atlassian.net/browse/GEOS-2622) Per feature type MaxFeature configuration not stored in info.xml, nor it's read back from info.xml
* [GEOS-2623](https://osgeo-org.atlassian.net/browse/GEOS-2623) adding a metdata link in feature type editor causes an exception on save
* [GEOS-2626](https://osgeo-org.atlassian.net/browse/GEOS-2626) Gzip filter is memory bound, kills streaming
* [GEOS-2627](https://osgeo-org.atlassian.net/browse/GEOS-2627) Alternate style information is not read anymore
* [GEOS-2632](https://osgeo-org.atlassian.net/browse/GEOS-2632) disabling acegi and applying causes exception
* [GEOS-2640](https://osgeo-org.atlassian.net/browse/GEOS-2640) Missing maxFeatures causes null pointer exception
* [GEOS-2643](https://osgeo-org.atlassian.net/browse/GEOS-2643) Trouble with multiple deletes in a single transaction against shapefiles
* [GEOS-2751](https://osgeo-org.atlassian.net/browse/GEOS-2751) After adding a new feature, the feature type edit page is inaccessible

Task:

* [GEOS-2691](https://osgeo-org.atlassian.net/browse/GEOS-2691) Document namespace filter functionality
* [GEOS-2693](https://osgeo-org.atlassian.net/browse/GEOS-2693) Document new directory datastore
* [GEOS-2694](https://osgeo-org.atlassian.net/browse/GEOS-2694) Document new stroke width control
