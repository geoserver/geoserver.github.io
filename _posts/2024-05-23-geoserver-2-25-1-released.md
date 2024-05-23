---
author: Jody Garnett
date: 2024-05-23
layout: post
title: GeoServer 2.25.1 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
- Vulnerability
release: release_225
version: 2.25.1
jira_version: 16919
--- 

GeoServer [2.25.1](/release/2.25.1/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.1/geoserver-2.25.1-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.1/geoserver-2.25.1-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.1/GeoServer-2.25.1-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.1/geoserver-2.25.1-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.1/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 2.25.1 is made in conjunction with GeoTools 31.1, and GeoWebCache 1.25.1. 

Thanks to Jody Garnett (GeoCat) for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is considered an essential upgrade for production systems.

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

## Raster Attribute Table Extension

A new extension is available that takes advantage of the GDAL Raster Attribute Table (RAT). This data structure provides a way to associate attribute information for individual pixel values within the raster. This provides a table that links each cell value in the raster to one or more attributes on the fly.

![](/img/posts/2.25/rat-ui.png)

![](/img/posts/2.25/rat-map.png)

Thanks to Andrea Aime (GeoSolutions) for the development and NOAA for sponsoring this new capability. Please see the user guide [Raster Attribute Table support](https://docs.geoserver.org/latest/en/user/extensions/rat/index.html) for more information.

* [GEOS-11376](https://osgeo-org.atlassian.net/browse/GEOS-11376) Graduate Raster Attribute Table to extension

## Release notes

New Feature:

* [GEOS-11267](https://osgeo-org.atlassian.net/browse/GEOS-11267) CSW ISO extension multiple mappings should also have multiple queryable mappings
* [GEOS-11376](https://osgeo-org.atlassian.net/browse/GEOS-11376) Graduate Raster Attribute Table to extension

Improvement:

* [GEOS-11306](https://osgeo-org.atlassian.net/browse/GEOS-11306) Java 17 does not support GetFeature lazy JDBC count(*)
* [GEOS-11311](https://osgeo-org.atlassian.net/browse/GEOS-11311) Show a full stack trace in the JVM stack dump panel
* [GEOS-11342](https://osgeo-org.atlassian.net/browse/GEOS-11342) STAC should exclude items when the collection in path is wrong
* [GEOS-11359](https://osgeo-org.atlassian.net/browse/GEOS-11359) Update MapML viewer to release 0.13.2
* [GEOS-11369](https://osgeo-org.atlassian.net/browse/GEOS-11369) Additional authentication options for cascaded WMS|WMTS data stores
* [GEOS-11377](https://osgeo-org.atlassian.net/browse/GEOS-11377) RAT module: allow to reload/recompute the RAT
* [GEOS-11400](https://osgeo-org.atlassian.net/browse/GEOS-11400) About Page Layout and display of build information
* [GEOS-11401](https://osgeo-org.atlassian.net/browse/GEOS-11401) Introduce environmental variables for Module Status page

Bug:

* [GEOS-11202](https://osgeo-org.atlassian.net/browse/GEOS-11202) CAS extension doesn't use global "proxy base URL" setting for service ticket
* [GEOS-11236](https://osgeo-org.atlassian.net/browse/GEOS-11236) WFS 2.0.0/GetFeature - Shapefile - "We have had issues trying to flip axis"
* [GEOS-11331](https://osgeo-org.atlassian.net/browse/GEOS-11331) OAuth2 can throw a " java.lang.RuntimeException: Never should reach this point"
* [GEOS-11332](https://osgeo-org.atlassian.net/browse/GEOS-11332) Renaming style with uppercase/downcase empty the sld file
* [GEOS-11382](https://osgeo-org.atlassian.net/browse/GEOS-11382) The interceptor "CiteComplianceHack" never gets invoked by the Dispatcher Servlet
* [GEOS-11385](https://osgeo-org.atlassian.net/browse/GEOS-11385) Demo Requests functionality does not honour ENV variable PROXY_BASE_URL
* [GEOS-11392](https://osgeo-org.atlassian.net/browse/GEOS-11392) ConcurrentModificationException while using proxy-base-ext

Task:

* [GEOS-11360](https://osgeo-org.atlassian.net/browse/GEOS-11360) Upgrade Apache POI from 4.1.1 to 5.2.5
* [GEOS-11362](https://osgeo-org.atlassian.net/browse/GEOS-11362) Upgrade Spring libs from 5.3.32 to 5.3.33
* [GEOS-11374](https://osgeo-org.atlassian.net/browse/GEOS-11374) Upgrade Spring version from 5.3.33 to 5.3.34
* [GEOS-11375](https://osgeo-org.atlassian.net/browse/GEOS-11375) GSIP 224 - Individual contributor clarification
* [GEOS-11388](https://osgeo-org.atlassian.net/browse/GEOS-11388) Update ImageIO-EXT to 1.4.10
* [GEOS-11393](https://osgeo-org.atlassian.net/browse/GEOS-11393) Upgrade commons-io from 2.12.0 to 2.16.1
* [GEOS-11395](https://osgeo-org.atlassian.net/browse/GEOS-11395) Upgrade guava from 32.0.0 to 33.2.0
* [GEOS-11397](https://osgeo-org.atlassian.net/browse/GEOS-11397) App-Schema Includes fix Integration Tests
* [GEOS-11402](https://osgeo-org.atlassian.net/browse/GEOS-11402) Upgrade PostgreSQL driver from 42.7.2 to 42.7.3
* [GEOS-11403](https://osgeo-org.atlassian.net/browse/GEOS-11403) Upgrade commons-text from 1.10.0 to 1.12.0
* [GEOS-11404](https://osgeo-org.atlassian.net/browse/GEOS-11404) Upgrade commons-codec from 1.15 to 1.17.0

For the complete list see [2.25.1](https://github.com/geoserver/geoserver/releases/tag/2.25.1) release notes. 

## Community Updates

Community module development:

* [GEOS-11040](https://osgeo-org.atlassian.net/browse/GEOS-11040) Could not get a ServiceInfo for service Features thus could not check if the service is enabled
* [GEOS-11330](https://osgeo-org.atlassian.net/browse/GEOS-11330) OAuth2 kid verification should be optional
* [GEOS-11339](https://osgeo-org.atlassian.net/browse/GEOS-11339) Introducing the Features Autopopulate Community Plugin
* [GEOS-11340](https://osgeo-org.atlassian.net/browse/GEOS-11340)  WFS Freemarker HTML Outputformat
* [GEOS-11345](https://osgeo-org.atlassian.net/browse/GEOS-11345) STAC Conformance URIs need to be updated to v1.0.0
* [GEOS-11348](https://osgeo-org.atlassian.net/browse/GEOS-11348) JMS cluster does not allow to publish style via REST "2 step" approach
* [GEOS-11358](https://osgeo-org.atlassian.net/browse/GEOS-11358) Feature-Autopopulate Update operation does not apply the Update Element filter
* [GEOS-11381](https://osgeo-org.atlassian.net/browse/GEOS-11381) Error in OIDC plugin in combination with RoleService
* [GEOS-11394](https://osgeo-org.atlassian.net/browse/GEOS-11394) OGC APIs cannot handle time extent when the source data type is java.sql.Date

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.25 Series

Additional information on GeoServer 2.25 series:

* [GeoServer 2.25 User Manual](https://docs.geoserver.org/2.25.x/en/user/)
* [GeoServer 2024 Roadmap Plannings]({% post_url 2024-01-03-roadmap %}) 
* [Raster Attribute Table extension](https://github.com/geoserver/geoserver/wiki/GSIP-222)
* [Individual contributor clarification](https://github.com/geoserver/geoserver/wiki/GSIP-224)

Release notes:
( [2.25.1](https://github.com/geoserver/geoserver/releases/tag/2.25.1)
| [2.25.0](https://github.com/geoserver/geoserver/releases/tag/2.25.0)
| [2.25-RC](https://github.com/geoserver/geoserver/releases/tag/2.25-RC)
) 

