---
author: geoserver
comments: true
date: 2010-12-07 00:01:27+00:00
layout: post
link: http://blog.geoserver.org/2010/12/06/geoserver-2-1-beta2-now-available/
slug: geoserver-2-1-beta2-now-available
title: GeoServer 2.1-beta2 now available
wordpress_id: 789
categories:
- Announcements
tags:
- beta
- release
- security
- ui
- wps
---

We are pleased to announce the [second beta release of GeoServer 2.1](https://web.archive.org/web/20101207/http://geoserver.org/display/GEOS/2.1-beta2).  Big thanks goes out to [GeoSolutions](http://www.geo-solutions.it/) for stepping up to the unglamorous and thankless process of creating a release, not to mention adding lots of great new features.

GeoServer 2.1.0 is shaping up to be quite an incredible step forward.  In addition to all the great features of [the first 2.1 beta]({% post_url 2010-09-04-geoserver-21-beta-released %}), this release brings a few more.


### Graphical File/Directory Chooser


Ever found it difficult to remember the full path when loading a shapefile or GeoTIFF?  A new improvement brings an easy graphical file and directory selection tool to browse the file system that GeoServer is on.  This is definitely a great enhancement to make GeoServer even easier to configure.

Read more about the [new file chooser](http://geo-solutions.blogspot.com/2010/11/new-file-chooser-for-geoserver.html).


### Core improvements to support database-backed catalog


GeoServer's core catalog interfaces received some tweaks to be able to more easily support different backend storage formats. The current in-memory implementation has a number of drawbacks, the most notable being that it is memory bound which means it can not scale up to large amounts of layers.  The support for specific new storage formats is still only available a community module, but these core improvements make it possible to more easily swap in and out different backends.

Read more about the improvements for [database-backed catalog](https://web.archive.org/web/20101207/http://geoserver.org/display/GEOS/GSIP+52+-+Refactor+out+DAO+for+Catalog+and+Configuration).


### Font Improvements


Adding new fonts for your maps should now be much easier, as you can just drop font files directly in to your GeoServer data directory and they will be picked up by GeoServer.  The admin interface also will list the fonts currently available, including the ones picked up directly from the Java Virtual Machine.


### Upgrade to Spring Security 2.0.6


GeoServer has always had [Acegi Security](https://web.archive.org/web/20101207/http://www.acegisecurity.org/) as its core, but that library got absorbed by the Spring community, and improved and upgraded to become [Spring Security](http://static.springsource.org/spring-security/site/index.html), the official security module of the [Spring portfolio](http://www.springsource.org/projects/).  This brings a number of new security protocols to GeoServer, including [OpenID](http://openid.net/) and [Windows NTLM](http://msdn.microsoft.com/en-us/library/aa378749%28VS.85%29.aspx).  It also should be easier to customize security setup, with even more powerful options.

Read more about the [upgrade to Spring Security](https://web.archive.org/web/20101207/http://geoserver.org/display/GEOS/GSIP+54+Upgrade+Geoserver+security+to+Spring+Security+2.0).


### WCS limits


WFS and WMS both have had the ability to limit what a user can request.  Now, similar controls are in place for WCS calls as well.  Thanks to [MassGIS](http://www.mass.gov/mgis/) for funding this improvement.


### Web Processing Service (WPS) in extensions


The one thing to note from last beta release is that the WPS is [maturing](http://geo-solutions.blogspot.com/2010/11/geosolutions-helps-geoserver-wps-going.html), It has been split up in to three modules, "core", "web", and "sextante".  The latter has all the algorithms of the [Sextante](http://www.sextantegis.com/) project, but is not yet mature, so it lives in a community module.  Web and core live in a new WPS extension, meaning that **the core of WPS is now officially supported by GeoServer**.  You can find the WPS extension on the [download page](https://web.archive.org/web/20101207/http://geoserver.org/display/GEOS/2.1-beta2), and add it to GeoServer just like any other extension.

[Read more](https://web.archive.org/web/20101207/http://geoserver.org/display/GEOS/GSIP+55+-+Promote+WPS+to+extension) about WPS in extensions.


### And more


This release also included a number of other bug fixes and improvements.  Check out the entire [changelog](#release-notes). Help us get to a stable 2.1.0 by downloading the beta and trying it out. Be sure to report any issues on the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users) or in the [bug tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS).  We appreciate any and all feedback.  We're hoping to move soon to Release Candidates, after getting one last major improvement in — **WMS 1.3**.

**[Download GeoServer 2.1-beta2](https://web.archive.org/web/20101207/http://geoserver.org/display/GEOS/2.1-beta2)**

----

## GeoServer 2.1-beta2

Released on 06-dec-2010

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/geoserver-2.1-beta2-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/geoserver-2.1-beta2-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/geoserver-2.1-beta2.exe/download)
- [Mac OS X Installer](http://downloads.sourceforge.net/geoserver/geoserver-2.1-beta2.dmg)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/geoserver-2.1-beta2-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/geoserver-2.1-beta2-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/geoserver-2.1-beta2-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/geoserver-2.1-beta2-javadoc.zip/download)
- [Release Notes](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/geoserver-2.1-beta2-notes.txt/view)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-imagemosaic-jdbc-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-control-flow-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-ogr-plugin.zip/download)
- [RESTConfig](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-restconfig-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-wfsv-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/extensions/geoserver-2.1-beta2-wps-plugin.zip/download)

#### [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta2/)

SourceForge Release 2.1-beta2.

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 16728

## Release notes

New Feature:

* [GEOS-2378](https://osgeo-org.atlassian.net/browse/GEOS-2378) GML 3.2 bindings

Improvement:

* [GEOS-3794](https://osgeo-org.atlassian.net/browse/GEOS-3794) Show a list of fonts available to the java runtime in a GUI page
* [GEOS-3824](https://osgeo-org.atlassian.net/browse/GEOS-3824) Improve the GDAL-ImageIO-Ext section User Documentation
* [GEOS-3856](https://osgeo-org.atlassian.net/browse/GEOS-3856) Add WCS limits (similar to those in WMS or WFS)
* [GEOS-3958](https://osgeo-org.atlassian.net/browse/GEOS-3958) Automatically register all fonts that are dropped in the styles directory
* [GEOS-3999](https://osgeo-org.atlassian.net/browse/GEOS-3999) external.type and url.type support for datastores
* [GEOS-4047](https://osgeo-org.atlassian.net/browse/GEOS-4047) Allow users to create new layers by specifying native, eventually pametrized sql queries
* [GEOS-4114](https://osgeo-org.atlassian.net/browse/GEOS-4114) allow servlet filters to be plugged in via spring
* [GEOS-4133](https://osgeo-org.atlassian.net/browse/GEOS-4133) have wfs capabilities use FunctionFactory interface for loading filter functions
* [GEOS-4150](https://osgeo-org.atlassian.net/browse/GEOS-4150) rename Demos to Tools and make tools securable
* [GEOS-4151](https://osgeo-org.atlassian.net/browse/GEOS-4151) Move GEOSERVER_DATA_DIR lookup logic to GeoServerResourceLoader
* [GEOS-4152](https://osgeo-org.atlassian.net/browse/GEOS-4152) Modify service code to prevent singletons from holding direct references to ServiceInfo objects
* [GEOS-4174](https://osgeo-org.atlassian.net/browse/GEOS-4174) REST config reload resource is not documented
* [GEOS-4198](https://osgeo-org.atlassian.net/browse/GEOS-4198) WMS GetFeatureInfo cascading should be as lenient as the other code paths vs the srs params
* [GEOS-4208](https://osgeo-org.atlassian.net/browse/GEOS-4208) Use an interactive server side file chooser to pick shapefiles, directories, geotiffs and the like
* [GEOS-4215](https://osgeo-org.atlassian.net/browse/GEOS-4215) Migrating to spring security 2.0.6
* [GEOS-4218](https://osgeo-org.atlassian.net/browse/GEOS-4218) Split the WPS module in three parts, core, gui and Sextante integration
* [GEOS-4227](https://osgeo-org.atlassian.net/browse/GEOS-4227) Add version/build info to geoserver ui and to built artifacts.
* [GEOS-4237](https://osgeo-org.atlassian.net/browse/GEOS-4237) monitoring: wfs transaction requests don't include any information about what type of transaction
* [GEOS-4240](https://osgeo-org.atlassian.net/browse/GEOS-4240) monitoring: use consistent names and case for all ows operation and service names
* [GEOS-4241](https://osgeo-org.atlassian.net/browse/GEOS-4241) monitoring: normalize layer names before committing to database

Bug:

* [GEOS-3755](https://osgeo-org.atlassian.net/browse/GEOS-3755) REST Api fails on layernames containing space
* [GEOS-3843](https://osgeo-org.atlassian.net/browse/GEOS-3843) KML encode loads all the features regardless of what rules are active at a given scale
* [GEOS-3939](https://osgeo-org.atlassian.net/browse/GEOS-3939) com.microsoft.sqlserver.jdbc.SQLServerException wrong query string on wms GetMap request
* [GEOS-4092](https://osgeo-org.atlassian.net/browse/GEOS-4092) Label Graphics don't line up with the corresponding labels.
* [GEOS-4131](https://osgeo-org.atlassian.net/browse/GEOS-4131) Geoserver Can't parse SQL 2008 Table structure
* [GEOS-4135](https://osgeo-org.atlassian.net/browse/GEOS-4135) GWC TMS TileMapService document (capabilities like) URL doesn't work
* [GEOS-4140](https://osgeo-org.atlassian.net/browse/GEOS-4140) REST Config Plugin does not unescape URL
* [GEOS-4153](https://osgeo-org.atlassian.net/browse/GEOS-4153) Regression: Non-DataStore DataAccesses no longer recognised by GUI
* [GEOS-4168](https://osgeo-org.atlassian.net/browse/GEOS-4168) Polygon clipping/rendering issue
* [GEOS-4171](https://osgeo-org.atlassian.net/browse/GEOS-4171) App-schema: test mappingName with special characters enclosed in quotes
* [GEOS-4172](https://osgeo-org.atlassian.net/browse/GEOS-4172) Cache-control headers are not set on WMS responses
* [GEOS-4177](https://osgeo-org.atlassian.net/browse/GEOS-4177) CQL filter could not parce - Cyrillic data from attribute  table of SHP file
* [GEOS-4182](https://osgeo-org.atlassian.net/browse/GEOS-4182) GetLegendGraphic not working as expected
* [GEOS-4205](https://osgeo-org.atlassian.net/browse/GEOS-4205) Error when querying data from SQL (com.vividsolutions.jts.io.ParseException: Expected number but found '(' )
* [GEOS-4206](https://osgeo-org.atlassian.net/browse/GEOS-4206) Mis-configured ogr2ogr output format breaks all GetFeature calls
* [GEOS-4225](https://osgeo-org.atlassian.net/browse/GEOS-4225) NullPointerException when pressing "reload" in the server status panel
* [GEOS-4236](https://osgeo-org.atlassian.net/browse/GEOS-4236) monitoring: layer names not picked up when the request is a WFS transaction insert

Task:

* [GEOS-2658](https://osgeo-org.atlassian.net/browse/GEOS-2658) Port WMS module to the new Dispatching system, currently it's being adapted

Sub-task:

* [GEOS-2659](https://osgeo-org.atlassian.net/browse/GEOS-2659) port WmsExceptionHandler as a subclass of DefaultServiceExceptionHandler, not legacy
