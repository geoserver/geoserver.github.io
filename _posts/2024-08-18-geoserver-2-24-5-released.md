---
author: Andrea Aime
date: 2024-08-18
layout: post
title: GeoServer 2.24.5 Release
categories:
- Announcements
tags:
- Release
release: release_224
version: 2.24.5
jira_version: 16928
--- 

GeoServer [2.24.5](/release/2.24.5/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.5/geoserver-2.24.5-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.5/geoserver-2.24.5-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.5/GeoServer-2.24.5-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.5/geoserver-2.24.5-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.5/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.
GeoServer 2.24.5 is made in conjunction with GeoTools 30.5, and GeoWebCache 1.24.5. 

Thanks to Andrea Aime for making this release. 

## Release notes

Improvement:

* [GEOS-11336](https://osgeo-org.atlassian.net/browse/GEOS-11336) security-keycloak: upgrade keycloak version
* [GEOS-11443](https://osgeo-org.atlassian.net/browse/GEOS-11443) REST API does not take effect immediately due to 10 minute authentication cache
* [GEOS-11463](https://osgeo-org.atlassian.net/browse/GEOS-11463) WMS vector dimension validation should query only one feature and only for dimension attribute 
* [GEOS-11502](https://osgeo-org.atlassian.net/browse/GEOS-11502) Permit resize on user/group/role palette textbox to allow for extra long role names

Bug:

* [GEOS-11446](https://osgeo-org.atlassian.net/browse/GEOS-11446) [INSPIRE] Incorrect behavior for unsupported languages
* [GEOS-11453](https://osgeo-org.atlassian.net/browse/GEOS-11453) Failure to look-up default value of custom dimensions on vector layers
* [GEOS-11462](https://osgeo-org.atlassian.net/browse/GEOS-11462) 500 error thrown when double adding a user to a group via REST with JDBC user/group services
* [GEOS-11484](https://osgeo-org.atlassian.net/browse/GEOS-11484) DirectRasterRenderer is not respecting advancedProjectionHandling and continuosMapWrapping format_options
* [GEOS-11493](https://osgeo-org.atlassian.net/browse/GEOS-11493) Azure blob store may not get environment parameters from property file

Task:

* [GEOS-11464](https://osgeo-org.atlassian.net/browse/GEOS-11464) Update Jackson 2 libs from 2.17.1 to 2.17.2

For the complete list see [2.24.5](https://github.com/geoserver/geoserver/releases/tag/2.24.5) release notes. 

## Community Updates

Community module development:

* [GEOS-11111](https://osgeo-org.atlassian.net/browse/GEOS-11111) Open search for EO community module: STAC search page has wrong self link

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.24 Series

Additional information on GeoServer 2.24 series:

* [GeoServer 2.24 User Manual](https://docs.geoserver.org/2.24.x/en/user/)
* [Control remote HTTP requests sent by GeoTools/GeoServer](https://github.com/geoserver/geoserver/wiki/GSIP-218)
* [State of GeoServer 2.24.1](https://docs.google.com/presentation/d/1X7iU1fd47frfh1EsN_CdUll0qtMMgPXkkMjaTbejj3g/edit?usp=sharing) (foss4g-asia presentation)
* [Multiple CRS authority support, planetary CRS](https://github.com/geoserver/geoserver/wiki/GSIP-219)
* [Extensive GeoServer Printing improvements](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html)
* [Upgraded security policy](https://github.com/geoserver/geoserver/wiki/GSIP-220)

Release notes:
( [2.24.5](https://github.com/geoserver/geoserver/releases/tag/2.24.5)
| [2.24.4](https://github.com/geoserver/geoserver/releases/tag/2.24.4)
| [2.24.3](https://github.com/geoserver/geoserver/releases/tag/2.24.3)
| [2.24.2](https://github.com/geoserver/geoserver/releases/tag/2.24.2)
| [2.24.1](https://github.com/geoserver/geoserver/releases/tag/2.24.1)
| [2.24.0](https://github.com/geoserver/geoserver/releases/tag/2.24.0)
| [2.24-RC](https://github.com/geoserver/geoserver/releases/tag/2.24-RC)
) 

