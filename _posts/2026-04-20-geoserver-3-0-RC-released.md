---
author: Jody Garnett
date: 2026-04-20
layout: post
title: GeoServer 3.0-RC Release
categories:
- Announcements
tags:
- Release
- Release Candidate
release: release_30-
version: 3.0-RC
jira_version: 17934
--- 

GeoServer [3.0-RC](/release/3.0-RC/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0-RC/geoserver-3.0-RC-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0-RC/geoserver-3.0-RC-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0-RC/GeoServer-3.0-RC-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0-RC/geoserver-3.0-RC-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0-RC/extensions/).

This is a release candidate intended for public review and feedback.
GeoServer 3.0-RC is made in conjunction with GeoTools 35-RC, and GeoWebCache 2.0-RC. 

Thanks to Jody Garnett (GeoCat) and Andrea Aime (GeoSOlutions) for making this release. 

## Welcome to GeoServer 3

We are overjoyed to share this update with our community, this is the final stretch of a long road, a year of development, and a lot of planning and support to make it all happen.

There will be more technical details in the final release announcement - but for now we wish to say thank you.

### Straight forward upgrade

We have taken great pains to make the upgrade process seemless from GeoServer 2.28.x.

1. We have made no changes to the GeoServer Data Directory.

2. A few modules have migrated from core to extensions:

   * [WCS 1.0](https://docs.geoserver.org/latest/en/user/services/wcs/install/) and [WCS 1.1](https://docs.geoserver.org/latest/en/user/services/wcs/install/)
   * [World Image](https://docs.geoserver.org/latest/en/user/data/raster/arcgrid/#arcgrid_install) and [ArcGRID](https://docs.geoserver.org/latest/en/user/data/raster/arcgrid/#arcgrid_install) raster data sources.
   
   And the pure java `h2` database is no longer provided.
   
3. The [log file location](https://docs.geoserver.org/latest/en/user/configuration/logging/#logging_location) setting
   is now managed using ``GEOSERVER_LOG_LOCATION`` application property  
   
   
4. The [NetCDF] index support has been simplified and is now self contained. With this improvement NetCDF
   no longer needs an database or local `.idx` files to operate.
   
   Instructions are provided for how to clean up these now unused files.

Please see the [upgrade instructions](https://docs.geoserver.org/latest/en/user/installation/upgrade3/) for details.

### New User Experience and User Interface Theme

GeoServer 3 features a new "context-driven" user experience, and a fresh theme, which we really hope you enjoy.

* Search: Using the left hand side search field to find information. Autocomplete results are shown as you type, and results are shown in a tree which can be navigated below.

  <img src="/img/posts/3.0/welcome-global.png" alt="User Interface Search"
   style="display:block; margin-left:auto; margin-right:auto; max-width: 500px; height:auto;"/>
  
* Context: Clicking on a search item establishes the context which is shown as breadcrumbs along the top of the page.
  A drop-down context menu provides quick access to actions that can be performed.

  <img src="/img/posts/3.0/context-menu.png" alt="User Interface Context Menu"
   style="display:block; margin-left:auto; margin-right:auto; max-width: 500px; height:auto;"/>
  
* Page: Page content adjusts to the current context. The welcome page adjusts to showing the layer tile and description, along with preview links, sample data downloads, and metdata and data links configured.

  <img src="/img/posts/3.0/welcome-layer.png" alt="User Interface Welcome Layer Page"
   style="display:block; margin-left:auto; margin-right:auto; max-width: 500px; height:auto;"/>
  
* Menu: The menu bar at the top of the page provides login on the right hand side, and access to the familiar GeoSever to-level menus. Many of these pages now adjust their content to reflect the current context.

  <img src="/img/posts/3.0/menus.png" alt="User Interface Top Level Menus"
   style="display:block; margin-left:auto; margin-right:auto; max-width: 500px; height:auto;"/>

For more information see the [user guide](https://docs.geoserver.org/main/en/user/webadmin/).


### New Layer Preview

A new full-screen layer preview is provided using the latest OpenLayers library.


### New Environment

GeoServer 3 is pleased to support the latest Tomcat 11.0.x and Jetty 12.0 application servers after completing our transition to Spring Framework 7 and JakartaEE Servlet API 6.1.

| JavaEE          | JakartaEE       | Tomcat        | Jetty      | GeoServer      | Java     |
| --------------- | --------------- | --------------| ---------- | -------------- | -------- |
|                 | Servlet API 6.1 | Tomcat 11.0.x | Jetty 12.1 | GeoServer 3.0  | 21,17    |
|                 | Servlet API 6.0 | Tomcat 10.1.x | Jetty 12.0 | not supported  |          |
|                 | Servlet API 5.0 | Tomcat 10.0.x | Jetty 11.0 | not supported  |          |
| Servlet API 4   |                 | Tomcat 9.x    |            | GeoServer 2.28 | 21,17    |
| Servlet API 3.1 |                 |               | Jetty 9.4  | GeoServer 2.28 | 21,17    |

We have been extensively testing GeoSever 3 with Java 17 and Java 21, maintaining the same Java environment as the previous GeoServer 2.28 release.  Java 25 is subject to automated testing, but we are going to hold off recommending this environment until our user forum has had an opportunity to try it out and report back.

For more information see [container considerations](https://docs.geoserver.org/latest/en/user/production/container/).

### New documentation

The long wished for transition to "markdown" documentation has finally arrived.

* [User Manual](https://docs.geoserver.org/main/en/user/)

Thanks to Peter (AfriGIS) and Jody (GeoCat) for working on this activity which ended up being an incredible amount of work.


## Release notes

New Feature:

* [GEOS-12063](https://osgeo-org.atlassian.net/browse/GEOS-12063) [GSIP-238] GeoServer 3 UI / UX Refresh

Improvement:

* [GEOS-11886](https://osgeo-org.atlassian.net/browse/GEOS-11886) Sort entries in all .properties files alphabetically
* [GEOS-12015](https://osgeo-org.atlassian.net/browse/GEOS-12015) Switch tests using H2 to GeoPackage
* [GEOS-12023](https://osgeo-org.atlassian.net/browse/GEOS-12023) Improve developer logging during catalog resources loading and WMS capabilities requests
* [GEOS-12024](https://osgeo-org.atlassian.net/browse/GEOS-12024) Add Git branch name in GEOSERVER_NODE_OPTS
* [GEOS-12072](https://osgeo-org.atlassian.net/browse/GEOS-12072) Remove deprecated REST endpoint on the DataStoreFileController
* [GEOS-12077](https://osgeo-org.atlassian.net/browse/GEOS-12077) Remove H2/DB based index and binary index from CoverageMultidim/NetCDF stores
* [GEOS-12081](https://osgeo-org.atlassian.net/browse/GEOS-12081) Update MapML.js (<mapml-viewer> custom element suite) to v0.17.0
* [GEOS-12082](https://osgeo-org.atlassian.net/browse/GEOS-12082) CoverageStore - quick fail for incorrect files
* [GEOS-12083](https://osgeo-org.atlassian.net/browse/GEOS-12083) Skip brute force login delays when checking for default administrator password

Bug:

* [GEOS-10509](https://osgeo-org.atlassian.net/browse/GEOS-10509) WFS Request fails when XML POST body is larger than 8kB
* [GEOS-11903](https://osgeo-org.atlassian.net/browse/GEOS-11903) WPS does not respect raw response output selection when there are multiple outputs
* [GEOS-11916](https://osgeo-org.atlassian.net/browse/GEOS-11916) Data directory migration performed on built-in default security configuration
* [GEOS-11926](https://osgeo-org.atlassian.net/browse/GEOS-11926) ogcapi plugin makes WFS advertising an outputFormat which is actually unavailable
* [GEOS-11930](https://osgeo-org.atlassian.net/browse/GEOS-11930) OGC-API extension breaks security REST API 
* [GEOS-11942](https://osgeo-org.atlassian.net/browse/GEOS-11942) ImagePPIO does not run any longer
* [GEOS-11964](https://osgeo-org.atlassian.net/browse/GEOS-11964) Metadata Bulk Operations: wicket error
* [GEOS-11965](https://osgeo-org.atlassian.net/browse/GEOS-11965) KMZ export incorrectly references remote icon URLs instead of embedding them in the KMZ archive
* [GEOS-11981](https://osgeo-org.atlassian.net/browse/GEOS-11981) POST /security/authproviders | 400: Unsupported className
* [GEOS-11988](https://osgeo-org.atlassian.net/browse/GEOS-11988) Fix bug: preserve metaTilingThreads=0 in saneConfig()
* [GEOS-11999](https://osgeo-org.atlassian.net/browse/GEOS-11999) The version of Jetty (12) no longer supports web.xml CORS configuration
* [GEOS-12065](https://osgeo-org.atlassian.net/browse/GEOS-12065) WMS Layer REST PUT always returns 500 due to Collections.emptySet() in getRemoteStyleInfos()
* [GEOS-12073](https://osgeo-org.atlassian.net/browse/GEOS-12073) Remove log location configuration from Admin Console and REST API
* [GEOS-12084](https://osgeo-org.atlassian.net/browse/GEOS-12084) TemplateController REST endpoints accept non-existent workspace, store, and resource names
* [GEOS-12085](https://osgeo-org.atlassian.net/browse/GEOS-12085) LocalSettingsController does not validate workspace existence

Task:

* [GEOS-11987](https://osgeo-org.atlassian.net/browse/GEOS-11987) ImageN 0.9.1 migration requires renaming of registryFile.jai to registryFile.imagen
* [GEOS-12004](https://osgeo-org.atlassian.net/browse/GEOS-12004) Make WMS indepependent of WFS
* [GEOS-12005](https://osgeo-org.atlassian.net/browse/GEOS-12005) Remove GeoServer H2 extension
* [GEOS-12006](https://osgeo-org.atlassian.net/browse/GEOS-12006) GWC, removal of leftover H2 references
* [GEOS-12011](https://osgeo-org.atlassian.net/browse/GEOS-12011) Move KML module to extension
* [GEOS-12016](https://osgeo-org.atlassian.net/browse/GEOS-12016) Move WCS 1.1 module to extension
* [GEOS-12017](https://osgeo-org.atlassian.net/browse/GEOS-12017) Move WCS 1.0 to extension
* [GEOS-12018](https://osgeo-org.atlassian.net/browse/GEOS-12018) Switch GeoServer tests away from H2
* [GEOS-12019](https://osgeo-org.atlassian.net/browse/GEOS-12019) Turn arcgrid and worldimage formats into plugins
* [GEOS-12025](https://osgeo-org.atlassian.net/browse/GEOS-12025) Split WMS 1.1 and 1.3
* [GEOS-12040](https://osgeo-org.atlassian.net/browse/GEOS-12040) Updating BouncyCatle libraries to LTS 2.73.10
* [GEOS-12041](https://osgeo-org.atlassian.net/browse/GEOS-12041) Update Spring LDAP to 4.0.1
* [GEOS-12071](https://osgeo-org.atlassian.net/browse/GEOS-12071) Remove the WPS remote module
* [GEOS-12064](https://osgeo-org.atlassian.net/browse/GEOS-12064) CSS: add documentation for localized @title and @abstract metadata

Sub-task:

* [GEOS-12066](https://osgeo-org.atlassian.net/browse/GEOS-12066) Present keywords as a table
* [GEOS-12067](https://osgeo-org.atlassian.net/browse/GEOS-12067) Add Full Screen OpenLayers 10.8.0 layer preview
* [GEOS-12086](https://osgeo-org.atlassian.net/browse/GEOS-12086) Keyboard navigation for file browser

For the complete list see [3.0-RC](https://github.com/geoserver/geoserver/releases/tag/3.0-RC) release notes. 

## Community Updates

Community module development:

* [GEOS-11904](https://osgeo-org.atlassian.net/browse/GEOS-11904) OGC API Processes: add support for envelope input/output
* [GEOS-11905](https://osgeo-org.atlassian.net/browse/GEOS-11905) OGC API processes status response lacks jobid and links to self
* [GEOS-11906](https://osgeo-org.atlassian.net/browse/GEOS-11906) OGC API Processes: use correct error code for access to results when execution is not complete
* [GEOS-11907](https://osgeo-org.atlassian.net/browse/GEOS-11907) OGC API Processes: support multiple raw responses
* [GEOS-11908](https://osgeo-org.atlassian.net/browse/GEOS-11908) OGC API Processes page should be pageable
* [GEOS-11909](https://osgeo-org.atlassian.net/browse/GEOS-11909) Add support for OGC API Echo process
* [GEOS-11915](https://osgeo-org.atlassian.net/browse/GEOS-11915) OGC API Processes: improve support for binary input and output
* [GEOS-11972](https://osgeo-org.atlassian.net/browse/GEOS-11972) GSIP 233 - Community Pending Release Profile
* [GEOS-11980](https://osgeo-org.atlassian.net/browse/GEOS-11980) Add support for uploading a single parquet file to GeoServer via REST
* [GEOS-11983](https://osgeo-org.atlassian.net/browse/GEOS-11983) GSR /query fails with HTTP 500 when where parameter is empty
* [GEOS-12000](https://osgeo-org.atlassian.net/browse/GEOS-12000) Ignore DescribeFeatureType requests without typeName in Features Templating schemas override
* [GEOS-12002](https://osgeo-org.atlassian.net/browse/GEOS-12002) hz-cluster: homepage pop-up fails
* [GEOS-12007](https://osgeo-org.atlassian.net/browse/GEOS-12007) Add AWS credential chain authentication UI and documentation for GeoParquet
* [GEOS-12013](https://osgeo-org.atlassian.net/browse/GEOS-12013) Support vector datasets ingestion in VectorMosaic via REST
* [GEOS-12044](https://osgeo-org.atlassian.net/browse/GEOS-12044) STAC search endpoint should report invalid collection names as invalid parameters instead of internal errors
* [GEOS-12061](https://osgeo-org.atlassian.net/browse/GEOS-12061) New Community Module for PNG-WIND output format for wind datasets
* [GEOS-12062](https://osgeo-org.atlassian.net/browse/GEOS-12062) Add DuckDB datastore community extension (gs-duckdb)
* [GEOS-12069](https://osgeo-org.atlassian.net/browse/GEOS-12069) Align the hazelcast version in hz-cluster to the rest of GeoServer
* [GEOS-12074](https://osgeo-org.atlassian.net/browse/GEOS-12074) Remove activeMQ-broker community module
* [GEOS-12089](https://osgeo-org.atlassian.net/browse/GEOS-12089) GWC sqlite community module breaks legend preview in style page

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 3.0- Series

Additional information on GeoServer 3.0- series:

* [GeoServer 3.0- User Manual](https://docs.geoserver.org/3.0-.x/en/user/)

Release notes:
( [3.0-RC](https://github.com/geoserver/geoserver/releases/tag/3.0-RC)
) 

