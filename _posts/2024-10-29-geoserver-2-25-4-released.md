---
author: Jody Garnett
date: 2024-10-29
layout: post
title: GeoServer 2.25.4 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_225
version: 2.25.4
jira_version: 16930
--- 

GeoServer [2.25.4](/release/2.25.4/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.4/geoserver-2.25.4-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.4/geoserver-2.25.4-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.4/GeoServer-2.25.4-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.4/geoserver-2.25.4-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.4/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.
GeoServer 2.25.4 is made in conjunction with GeoTools 31.4, and GeoWebCache 1.25.3.

Thanks to Jody Garnett for making this release. 

**Update 2024-11-08:** Testing from Sören Kalesse noted the downloads included snapshot jars. The binaries have been updated with intended geotools and geowebcache jars.

## Security Considerations

This release addresses security vulnerabilities and is considered an important upgrade for production systems.

<!-- update cve list details when disclosed -->
* [GEOS-11557](https://osgeo-org.atlassian.net/browse/GEOS-11557) CVE-2024-45748 High

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

## Release notes

New Feature:

* [GEOS-11352](https://osgeo-org.atlassian.net/browse/GEOS-11352) REST service for URL checks

Improvement:

* [GEOS-11399](https://osgeo-org.atlassian.net/browse/GEOS-11399) Use Catalog streaming API in LayerGroupPage
* [GEOS-11427](https://osgeo-org.atlassian.net/browse/GEOS-11427) metadata: "fix all" to support changing config repeatable field
* [GEOS-11463](https://osgeo-org.atlassian.net/browse/GEOS-11463) WMS vector dimension validation should query only one feature and only for dimension attribute 
* [GEOS-11502](https://osgeo-org.atlassian.net/browse/GEOS-11502) Permit resize on user/group/role palette textbox to allow for extra long role names
* [GEOS-11503](https://osgeo-org.atlassian.net/browse/GEOS-11503) Update mongo schemaless DWITHIN to support non-point geometry
* [GEOS-11557](https://osgeo-org.atlassian.net/browse/GEOS-11557) CVE-2024-45748 High
* [GEOS-11588](https://osgeo-org.atlassian.net/browse/GEOS-11588) GWC disk quota, check JDBC connection pool validation query

Bug:

* [GEOS-10811](https://osgeo-org.atlassian.net/browse/GEOS-10811) GeoServer 2.22.0 WPS error while clipping raster with GeoJSON input
* [GEOS-11071](https://osgeo-org.atlassian.net/browse/GEOS-11071) GeoJSON PPIO goes NPE while decoding a GeoJSON geometry
* [GEOS-11107](https://osgeo-org.atlassian.net/browse/GEOS-11107) Open search for EO community module: packaging missing gt-cql-json-xx.x.jar
* [GEOS-11453](https://osgeo-org.atlassian.net/browse/GEOS-11453) Failure to look-up default value of custom dimensions on vector layers
* [GEOS-11484](https://osgeo-org.atlassian.net/browse/GEOS-11484) DirectRasterRenderer is not respecting advancedProjectionHandling and continuosMapWrapping format_options
* [GEOS-11493](https://osgeo-org.atlassian.net/browse/GEOS-11493) Azure blob store may not get environment parameters from property file
* [GEOS-11497](https://osgeo-org.atlassian.net/browse/GEOS-11497) WPS execution fails with GeoJSON input
* [GEOS-11504](https://osgeo-org.atlassian.net/browse/GEOS-11504) ResourceAccessManagerWrapper misses some delegating methods
* [GEOS-11505](https://osgeo-org.atlassian.net/browse/GEOS-11505) OWS Monitor only handles WFS 1.0 requests
* [GEOS-11513](https://osgeo-org.atlassian.net/browse/GEOS-11513) WMTS/GetDomainValues - Returned values are not sorted
* [GEOS-11514](https://osgeo-org.atlassian.net/browse/GEOS-11514) Fix parsing WPS geometry geojson inputs
* [GEOS-11524](https://osgeo-org.atlassian.net/browse/GEOS-11524) csw: default queryables mapping not generated
* [GEOS-11543](https://osgeo-org.atlassian.net/browse/GEOS-11543) Unable to use propertyName to filter properties in a GetFeature request when service is not set
* [GEOS-11553](https://osgeo-org.atlassian.net/browse/GEOS-11553) SLD Style: Empty SE Rotationelement throws RuntimeException (QGIS generated SLD)
* [GEOS-11556](https://osgeo-org.atlassian.net/browse/GEOS-11556) NullPointerException when GWC disk quota monitoring is disabled
* [GEOS-11559](https://osgeo-org.atlassian.net/browse/GEOS-11559) The customized attributes editor is prone to setting the wrong attribute source 

Task:

* [GEOS-11470](https://osgeo-org.atlassian.net/browse/GEOS-11470) Upgrade the version of Mongo driver for schemaless plugin from 4.0.6 to 4.11.2
* [GEOS-11506](https://osgeo-org.atlassian.net/browse/GEOS-11506) Upgrade Spring version from 5.3.37 to 5.3.39 and Spring security from 5.8.13 to 5.8.14
* [GEOS-11508](https://osgeo-org.atlassian.net/browse/GEOS-11508) Update OSHI from 6.4.10 to 6.6.3
* [GEOS-11533](https://osgeo-org.atlassian.net/browse/GEOS-11533) Update org.apache.commons.vfs2 to 2.9.0
* [GEOS-11574](https://osgeo-org.atlassian.net/browse/GEOS-11574) Bump org.eclipse.jetty:jetty-server from 9.4.52.v20230823 to 9.4.55.v20240627 in /src
* [GEOS-11587](https://osgeo-org.atlassian.net/browse/GEOS-11587) Update map fish-print-v2 2.3.2

For the complete list see [2.25.4](https://github.com/geoserver/geoserver/releases/tag/2.25.4) release notes. 

## Community Updates

Community module development:

* [GEOS-11517](https://osgeo-org.atlassian.net/browse/GEOS-11517) Using various OGC APIs results in service enabled check related WARN logs
* [GEOS-11518](https://osgeo-org.atlassian.net/browse/GEOS-11518) DGGS JDBC store SQL encoder should not force the timezone to CET
* [GEOS-11519](https://osgeo-org.atlassian.net/browse/GEOS-11519) Make DGGS rHealPix tests run again
* [GEOS-11560](https://osgeo-org.atlassian.net/browse/GEOS-11560) OGC API modules lack cql2-json in assembly
* [GEOS-11563](https://osgeo-org.atlassian.net/browse/GEOS-11563) Allow configuring a DGGS resolution offset on a layer basis
* [GEOS-11565](https://osgeo-org.atlassian.net/browse/GEOS-11565) Allow configuring the minimum and maximum DGGS resolution for a layer
* [GEOS-11579](https://osgeo-org.atlassian.net/browse/GEOS-11579) DGGS modules prevent GeoServer startup if JEP is not installed

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.25 Series

Additional information on GeoServer 2.25 series:

* [GeoServer 2.25 User Manual](https://docs.geoserver.org/2.25.x/en/user/)
* [GeoServer 2024 Roadmap Plannings]({% post_url 2024-01-03-roadmap %}) 
* [Raster Attribute Table extension](https://github.com/geoserver/geoserver/wiki/GSIP-222)
* [Individual contributor clarification](https://github.com/geoserver/geoserver/wiki/GSIP-224)

Release notes:
( [2.25.4](https://github.com/geoserver/geoserver/releases/tag/2.25.4)
| [2.25.3](https://github.com/geoserver/geoserver/releases/tag/2.25.3)
| [2.25.2](https://github.com/geoserver/geoserver/releases/tag/2.25.2)
| [2.25.1](https://github.com/geoserver/geoserver/releases/tag/2.25.1)
| [2.25.0](https://github.com/geoserver/geoserver/releases/tag/2.25.0)
| [2.25-RC](https://github.com/geoserver/geoserver/releases/tag/2.25-RC)
) 

