---
author: Ian Turton
date: 2023-01-24
layout: post
title: GeoServer 2.22.1 Release
categories:
- Announcements
tags:
- Release
release: release_222
version: 2.22.1
jira_version: 16872
---

GeoServer [2.22.1](/release/2.22.1/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.1/geoserver-2.22.1-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.1/geoserver-2.22.1-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.1/GeoServer-2.22.1-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.1/geoserver-2.22.1-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.1/extensions/).

This is a stable release of the GeoServer 2.22.x series, made in conjunction with GeoTools 28.1 
and GeoWebCache 1.22.0.

Thanks to Ian Turton (Astun Technology) for making this release.

### Bugs

+ [GEOS-10632](https://osgeo-org.atlassian.net/browse/GEOS-10632) Make sure GetLegendGraphics honors the WMS 
  memory service limits
+ [GEOS-10704](https://osgeo-org.atlassian.net/browse/GEOS-10704) Task Manager Metadata wrong gs-metadata 
  dependency
+ [GEOS-10753](https://osgeo-org.atlassian.net/browse/GEOS-10753) GeoServer can create GML output that is not 
  valid XML
+ [GEOS-10757](https://osgeo-org.atlassian.net/browse/GEOS-10757) CITE: WMS <Style> has elements in wrong 
  order \(DTD validation\)
+ [GEOS-10770](https://osgeo-org.atlassian.net/browse/GEOS-10770) Support list of audiences \(aud\) when 
  validating Oauth 2.0 Bearer Tokens
+ [GEOS-10794](https://osgeo-org.atlassian.net/browse/GEOS-10794) Add a new vector data source \(Web Feature 
  Server \(NG\)\) Filter compliance level bug
+ [GEOS-10807](https://osgeo-org.atlassian.net/browse/GEOS-10807) LayerGroup with nested group POST rest op 
  fails with null styles attribute
+ [GEOS-10809](https://osgeo-org.atlassian.net/browse/GEOS-10809) Keycloak : add support for usernames with 
  spaces
+ [GEOS-10813](https://osgeo-org.atlassian.net/browse/GEOS-10813) jdbc config cache bug
+ [GEOS-10817](https://osgeo-org.atlassian.net/browse/GEOS-10817) Features Templating - XML HTML output 
  doesn't escape all html and xml symbols
+ [GEOS-10818](https://osgeo-org.atlassian.net/browse/GEOS-10818) Schemaless Property Accessor returns 
  emptylist instead of null for null/not existing properties
+ [GEOS-10829](https://osgeo-org.atlassian.net/browse/GEOS-10829) JDBC Config missing some nested layer 
  properties

### Improvement

+ [GEOS-10673](https://osgeo-org.atlassian.net/browse/GEOS-10673) Add example of using FlatGeobuf granules to the Vector Mosaic documentation
+ [GEOS-10746](https://osgeo-org.atlassian.net/browse/GEOS-10746) STAC Sortables should be a subset of the 
configured queryables
+ [GEOS-10755](https://osgeo-org.atlassian.net/browse/GEOS-10755) WCS 2.0 module should not use string 
concatenation to build XML
+ [GEOS-10762](https://osgeo-org.atlassian.net/browse/GEOS-10762) Allow enabling auto-escaping for WMS 
GetFeatureInfo HTML templates
+ [GEOS-10773](https://osgeo-org.atlassian.net/browse/GEOS-10773) Enable localized MapML responses that use WMS 
language parameter
+ [GEOS-10777](https://osgeo-org.atlassian.net/browse/GEOS-10777) Update MapML viewer to latest release
+ [GEOS-10790](https://osgeo-org.atlassian.net/browse/GEOS-10790) Allow to control map transparency in 
DownloadMapProcess
+ [GEOS-10810](https://osgeo-org.atlassian.net/browse/GEOS-10810) Enable internationalized layer label / MapML 
document title
+ [GEOS-10814](https://osgeo-org.atlassian.net/browse/GEOS-10814) Update jdbc config to use consistent SQL 
formatting
+ [GEOS-10816](https://osgeo-org.atlassian.net/browse/GEOS-10816) OGC API Features complex features test fails 
since introduction of <meta> tag in HTML templates
+ [GEOS-10827](https://osgeo-org.atlassian.net/browse/GEOS-10827) Document property selection in image mosaic

### New Feature

+ [GEOS-10716](https://osgeo-org.atlassian.net/browse/GEOS-10716) Build schema for simple feature types 
  leveraging column descriptions, when available
+ [GEOS-10758](https://osgeo-org.atlassian.net/browse/GEOS-10758) OGCAPI - Features - Add storageCrs property 
  for Collections

### Task

+ [GEOS-10775](https://osgeo-org.atlassian.net/browse/GEOS-10775) Update xmlunit to 1.6
+ [GEOS-10778](https://osgeo-org.atlassian.net/browse/GEOS-10778) Retire GeoStyler community module
+ [GEOS-10812](https://osgeo-org.atlassian.net/browse/GEOS-10812) Update Jettison to 1.5.3



For complete information see [2.22.1 release 
notes](https://github.com/geoserver/geoserver/releases/tag/2.22.1).

### About GeoServer 2.22

Additional information on GeoServer 2.22 series:

* [Update Instructions](https://docs.geoserver.org/latest/en/user/installation/upgrade.html)
* [Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/metadata/index.html)
* [CSW ISO Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/csw-iso/index.html)
* [State of GeoServer](https://docs.google.com/presentation/d/1mnOFSvYb8npVudvUR5MSjSTFHc6ZQ_bStafZrBV7LZ8/edit?usp=sharing) (FOSS4G Presentation)
* [GeoServer Beginner Workshop](https://docs.google.com/presentation/d/1fbPLN-1Cs95WK-IxDG1PxCEKyHwFbNBGNkkomxmLr0Y/edit?usp=sharing) (FOSS4G Workshop)
* [Welcome page](https://docs.geoserver.org/latest/en/user/webadmin/welcome.html) (User Guide)

Release notes:
( [2.22.1](https://github.com/geoserver/geoserver/releases/tag/2.22.1) |
  [2.22.0](https://github.com/geoserver/geoserver/releases/tag/2.22.0) |
  [2.22-RC](https://github.com/geoserver/geoserver/releases/tag/2.22-RC)
| [2.22-M0](https://github.com/geoserver/geoserver/releases/tag/2.22-M0)
)
