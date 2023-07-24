---
author: Ian Turton
date: 2023-07-21
layout: post
title: GeoServer 2.23.2 Release
categories:
- Announcements
tags:
- Release
- Vulnerability
release: release_223
version: 2.23.2
jira_version: 16893
--- 

GeoServer [2.23.2](/release/2.23.2/) release is now available
with downloads (
[bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.2/geoserver-2.23.2-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.2/geoserver-2.23.2-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.2/GeoServer-2.23.2-winsetup.exe/download))
, along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.2/geoserver-2.23.2-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.2/extensions/).

This is a stable release of GeoServer recommended production use.
GeoServer  is made in conjunction with GeoTools 29.2, and GeoWebCache 1.23.1. 

Thanks to Ian Turton for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is considered an essential upgrade for production systems.

* [GEOS-10949](https://osgeo-org.atlassian.net/browse/GEOS-10949) Control remote resources accessed by 
  GeoServer
* [GEOS-11008](https://osgeo-org.atlassian.net/browse/GEOS-11008) Update sqlite-jdbc from 3.34.0 to 3.41.2.2

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

## Release notes

New Feature:

* [GEOS-10949](https://osgeo-org.atlassian.net//browse/GEOS-10949) Control remote resources accessed by GeoServer
* [GEOS-10992](https://osgeo-org.atlassian.net//browse/GEOS-10992) Make GWC UI for disk quota expose HSQLDB, remove H2, automatically update existing installations 

Improvement:

* [GEOS-10973](https://osgeo-org.atlassian.net//browse/GEOS-10973) DWITHIN delegation to mongoDB
* [GEOS-11048](https://osgeo-org.atlassian.net//browse/GEOS-11048) Improve URL checking

Bug:

* [GEOS-10874](https://osgeo-org.atlassian.net//browse/GEOS-10874) Log4J: Windows binary zip release file with log4j-1.2.14.jar
* [GEOS-10875](https://osgeo-org.atlassian.net//browse/GEOS-10875) Disk Quota JDBC password shown in plaintext 
* [GEOS-10901](https://osgeo-org.atlassian.net//browse/GEOS-10901) GetCapabilities lists the same style multiple times when used as both a default and alternate style
* [GEOS-10903](https://osgeo-org.atlassian.net//browse/GEOS-10903) WMS filtering with Filter 2.0 fails
* [GEOS-10906](https://osgeo-org.atlassian.net//browse/GEOS-10906) Authentication not sent if connection pooling activated 
* [GEOS-10932](https://osgeo-org.atlassian.net//browse/GEOS-10932) csw-iso: should only add 'xsi:nil = false' attribute
* [GEOS-10936](https://osgeo-org.atlassian.net//browse/GEOS-10936) YSLD and OGC API modules are incompatible
* [GEOS-10964](https://osgeo-org.atlassian.net//browse/GEOS-10964) Support virtual services for OSEO/STAC
* [GEOS-10980](https://osgeo-org.atlassian.net//browse/GEOS-10980) CSS extension lacks ASM JARs as of 2.23.0, stops rendering layer when style references a file
* [GEOS-10981](https://osgeo-org.atlassian.net//browse/GEOS-10981) Slow CSW GetRecords requests with JDBC Configuration
* [GEOS-10982](https://osgeo-org.atlassian.net//browse/GEOS-10982) Wicket bug when trying to add new Vector Attribute (build 2.23 on Tomcat/Windows)
* [GEOS-10993](https://osgeo-org.atlassian.net//browse/GEOS-10993) Disabled resources can cause incorrect CSW GetRecords response
* [GEOS-10994](https://osgeo-org.atlassian.net//browse/GEOS-10994) OOM due to too many dimensions when range requested
* [GEOS-10997](https://osgeo-org.atlassian.net//browse/GEOS-10997) GetCapabilities broken when using Data Security Layer groups
* [GEOS-10998](https://osgeo-org.atlassian.net//browse/GEOS-10998) LayerGroupContainmentCache is being rebuilt on each ApplicationEvent
* [GEOS-11015](https://osgeo-org.atlassian.net//browse/GEOS-11015) geopackage wfs output builds up tmp files over time
* [GEOS-11024](https://osgeo-org.atlassian.net//browse/GEOS-11024) metadata: add datetime field type to feature catalog
* [GEOS-11025](https://osgeo-org.atlassian.net//browse/GEOS-11025) projection parameter takes no effect on MongoDB Schemaless features WFS requests
* [GEOS-11026](https://osgeo-org.atlassian.net//browse/GEOS-11026) ClassNotFoundException: org.h2.driver on shutdown
* [GEOS-11033](https://osgeo-org.atlassian.net//browse/GEOS-11033) WCS DescribeCoverage ReferencedEnvelope with null crs
* [GEOS-11035](https://osgeo-org.atlassian.net//browse/GEOS-11035) Enabling OSEO from Workspace Edit Page Results in an NPE
* [GEOS-11036](https://osgeo-org.atlassian.net//browse/GEOS-11036) The OAuth2/OIDC security filters do not 
  work as expected anymore after the spring-security-core depencency update to 5.7.8
* [GEOS-11046](https://osgeo-org.atlassian.net//browse/GEOS-11046) Styles using the custom mark `shape://dot` don't draw any fill
* [GEOS-11054](https://osgeo-org.atlassian.net//browse/GEOS-11054) NullPointerException creating layer with REST, along with attribute list
* [GEOS-11055](https://osgeo-org.atlassian.net//browse/GEOS-11055) Multiple layers against the same ES document type conflict with each other
* [GEOS-11060](https://osgeo-org.atlassian.net//browse/GEOS-11060) charts and mssql extension zips are missing the extension
* [GEOS-11069](https://osgeo-org.atlassian.net//browse/GEOS-11069) Layer configuration page doesn't work for broken SQL views

Task:

* [GEOS-10987](https://osgeo-org.atlassian.net//browse/GEOS-10987) Bump xalan:xalan and xalan:serializer from 2.7.2 to 2.7.3
* [GEOS-10988](https://osgeo-org.atlassian.net//browse/GEOS-10988) Update spring.version from 5.3.26 to 5.3.27 and spring-integration.version from 5.5.17 to 5.5.18
* [GEOS-11008](https://osgeo-org.atlassian.net//browse/GEOS-11008) Update sqlite-jdbc from 3.34.0 to 3.41.2.2
* [GEOS-11010](https://osgeo-org.atlassian.net//browse/GEOS-11010) Upgrade guava from 30.1 to 32.0.0
* [GEOS-11011](https://osgeo-org.atlassian.net//browse/GEOS-11011) Upgrade postgresql from 42.4.3 to 42.6.0
* [GEOS-11012](https://osgeo-org.atlassian.net//browse/GEOS-11012) Upgrade commons-collections4 from 4.2 to 4.4
* [GEOS-11018](https://osgeo-org.atlassian.net//browse/GEOS-11018) Upgrade commons-lang3 from 3.8.1 to 3.12.0
* [GEOS-11020](https://osgeo-org.atlassian.net//browse/GEOS-11020) Add test scope to mockito-core dependency
* [GEOS-11062](https://osgeo-org.atlassian.net//browse/GEOS-11062)  Upgrade httpclient from 4.5.13 to 4.5.14
* [GEOS-11063](https://osgeo-org.atlassian.net//browse/GEOS-11063) Upgrade httpcore from 4.4.10 to 4.4.16
* [GEOS-11067](https://osgeo-org.atlassian.net//browse/GEOS-11067) Upgrade wiremock to 2.35.0

For the complete list see [2.23.2](https://github.com/geoserver/geoserver/releases/tag/2.23.2) release notes. 

# About GeoServer 2.23 Series

Additional information on GeoServer 2.23 series:

* [Running with Java 17 
  Notes](https://docs.geoserver.org/2.23.x/en/user/production/java.html#running-on-java-17)
* [GeoServer 2.23 User Manual](https://docs.geoserver.org/2.23.x/en/user/)
* [Drop Java 8](https://github.com/geoserver/geoserver/wiki/GSIP-215)
* [GUI CSS Cleanup](https://github.com/geoserver/geoserver/wiki/GSIP-213)
* [Add the possibility to use fixed values in Capabilities for Dimension metadata](https://github.com/geoserver/geoserver/wiki/GSIP-208)
* [State of GeoServer 2.23](https://docs.google.com/presentation/d/1nRKIILXWGLMGXZ6thfJgPR9kZ6Wh8Hp1dwZdQGw2YRc/edit?usp=share_link)
* [GeoServer Feature Frenzy 2023](https://docs.google.com/presentation/d/1vE8eCrOyewoH54g8CjuoiO3pxVLToEpuvpoZWmy0wTg/edit?usp=share_link)
* [GeoServer used in fun and interesting ways](https://docs.google.com/presentation/d/1PP2qk7eH8TzAf1tvEWH7Geattd0YFh7ZEDx1_tlrRWY/edit?usp=share_link)
* [GeoServer Orientation](https://docs.google.com/presentation/d/1sh9C4dIkDRnk3quCD1PRYoiJhjI9dqnAdOScJCgQWU8/edit?usp=share_link)

Release notes:
( [2.23.2](https://github.com/geoserver/geoserver/releases/tag/2.23.2)
| [2.23.1](https://github.com/geoserver/geoserver/releases/tag/2.23.1)
| [2.23.0](https://github.com/geoserver/geoserver/releases/tag/2.23.0)
| [2.23-RC1](https://github.com/geoserver/geoserver/releases/tag/2.23-RC1)
) 

