---
author: Ian Turton
date: 2024-07-18
layout: post
title: GeoServer 2.25.3 Release
categories:
- Announcements
tags:
- Release
release: release_225
version: 2.25.3
jira_version: 16927
--- 

GeoServer [2.25.3](/release/2.25.3/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.3/geoserver-2.25.3-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.3/geoserver-2.25.3-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.3/GeoServer-2.25.3-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.3/geoserver-2.25.3-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.3/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 2.25.3 is made in conjunction with GeoTools 31.3. This release is smaller than usual due to the 
earlier 2.25.2 security update that was released earlier this month. 

Thanks to Ian Turton for making this release. 

## Release notes

Improvement:

* [GEOS-11336](https://osgeo-org.atlassian.net/browse/GEOS-11336) security-keycloak: upgrade keycloak version
* [GEOS-11424](https://osgeo-org.atlassian.net/browse/GEOS-11424) Speed up web-ui WorkspaceAdminComponentAuthorizer
* [GEOS-11441](https://osgeo-org.atlassian.net/browse/GEOS-11441) DisabledServiceResourceFilter spams debugging logs with property accesses
* [GEOS-11442](https://osgeo-org.atlassian.net/browse/GEOS-11442) Cache availability of gdal_translate in gdal_translate based WCS output formats
* [GEOS-11443](https://osgeo-org.atlassian.net/browse/GEOS-11443) REST API does not take effect immediately due to 10 minute authentication cache

Bug:

* [GEOS-11446](https://osgeo-org.atlassian.net/browse/GEOS-11446) [INSPIRE] Incorrect behavior for unsupported languages
* [GEOS-11462](https://osgeo-org.atlassian.net/browse/GEOS-11462) 500 error thrown when double adding a user to a group via REST with JDBC user/group services

Task:

* [GEOS-11464](https://osgeo-org.atlassian.net/browse/GEOS-11464) Update Jackson 2 libs from 2.17.1 to 2.17.2

For the complete list see [2.25.3](https://github.com/geoserver/geoserver/releases/tag/2.25.3) release notes. 

## Community Updates

Community module development:

* [GEOS-10690](https://osgeo-org.atlassian.net/browse/GEOS-10690) Task manager plugin is missing dependencies
* [GEOS-11111](https://osgeo-org.atlassian.net/browse/GEOS-11111) Open search for EO community module: STAC search page has wrong self link
* [GEOS-11438](https://osgeo-org.atlassian.net/browse/GEOS-11438) OpenSearch for EO/STAC lack the service configuration panel
* [GEOS-11439](https://osgeo-org.atlassian.net/browse/GEOS-11439) JDBCOpenSearch access should cache the list of type names in request scope
* [GEOS-11445](https://osgeo-org.atlassian.net/browse/GEOS-11445) OGCAPI ServiceDescriptors
* [GEOS-11469](https://osgeo-org.atlassian.net/browse/GEOS-11469) Datadir catalog loader does not decrypt HTTPStoreInfo passwords

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.25 Series

Additional information on GeoServer 2.25 series:

* [GeoServer 2.25 User Manual](https://docs.geoserver.org/2.25.x/en/user/)
* [GeoServer 2024 Roadmap Plannings]({% post_url 2024-01-03-roadmap %})
* [GeoServer 2024 Q3 Developer Update]({% post_url 2024-07-22-developer-update %})
* [Raster Attribute Table extension](https://github.com/geoserver/geoserver/wiki/GSIP-222)
* [Individual contributor clarification](https://github.com/geoserver/geoserver/wiki/GSIP-224)

Release notes:
( [2.25.3](https://github.com/geoserver/geoserver/releases/tag/2.25.3)
| [2.25.2](https://github.com/geoserver/geoserver/releases/tag/2.25.2)
| [2.25.1](https://github.com/geoserver/geoserver/releases/tag/2.25.1)
| [2.25.0](https://github.com/geoserver/geoserver/releases/tag/2.25.0)
| [2.25-RC](https://github.com/geoserver/geoserver/releases/tag/2.25-RC)
) 

