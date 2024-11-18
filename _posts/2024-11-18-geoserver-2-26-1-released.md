---
author: Peter Smythe
date: 2024-11-18
layout: post
title: GeoServer 2.26.1 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_226
version: 2.26.1
jira_version: 16935
--- 

GeoServer [2.26.1](/release/2.26.1/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.1/geoserver-2.26.1-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.1/geoserver-2.26.1-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.1/GeoServer-2.26.1-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.1/geoserver-2.26.1-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.1/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 2.26.1 is made in conjunction with GeoTools 32.1, and GeoWebCache 1.26.1. 

Thanks to Peter Smythe for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is considered an essential upgrade for production systems.

<!-- update cve list details when disclosed -->
* [GEOS-11557](https://osgeo-org.atlassian.net/browse/GEOS-11557) CVE-2024-45748 High

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

## Release notes

Improvement:

* [GEOS-11557](https://osgeo-org.atlassian.net/browse/GEOS-11557) CVE-2024-45748 High
* [GEOS-11561](https://osgeo-org.atlassian.net/browse/GEOS-11561) Client-Delegating MapML Proxy
* [GEOS-11588](https://osgeo-org.atlassian.net/browse/GEOS-11588) GWC disk quota, check JDBC connection pool validation query

Bug:

* [GEOS-11107](https://osgeo-org.atlassian.net/browse/GEOS-11107) Open search for EO community module: packaging missing gt-cql-json-xx.x.jar
* [GEOS-11524](https://osgeo-org.atlassian.net/browse/GEOS-11524) csw: default queryables mapping not generated
* [GEOS-11543](https://osgeo-org.atlassian.net/browse/GEOS-11543) Unable to use propertyName to filter properties in a GetFeature request when service is not set
* [GEOS-11553](https://osgeo-org.atlassian.net/browse/GEOS-11553) SLD Style: Empty SE Rotationelement throws RuntimeException (QGIS generated SLD)
* [GEOS-11556](https://osgeo-org.atlassian.net/browse/GEOS-11556) NullPointerException when GWC disk quota monitoring is disabled
* [GEOS-11559](https://osgeo-org.atlassian.net/browse/GEOS-11559) The customized attributes editor is prone to setting the wrong attribute source 
* [GEOS-11573](https://osgeo-org.atlassian.net/browse/GEOS-11573) TileLayer preview doesn't work anymore

Task:

* [GEOS-11574](https://osgeo-org.atlassian.net/browse/GEOS-11574) Bump org.eclipse.jetty:jetty-server from 9.4.52.v20230823 to 9.4.55.v20240627 in /src
* [GEOS-11587](https://osgeo-org.atlassian.net/browse/GEOS-11587) Update map fish-print-v2 2.3.2
* [GEOS-11609](https://osgeo-org.atlassian.net/browse/GEOS-11609) Bump XStream from 1.4.20 to 1.4.21
* [GEOS-11610](https://osgeo-org.atlassian.net/browse/GEOS-11610) Update Jetty from 9.4.55.v20240627 to 9.4.56.v20240826

For the complete list see [2.26.1](https://github.com/geoserver/geoserver/releases/tag/2.26.1) release notes. 

## Community Updates

Community module development:

* [GEOS-11517](https://osgeo-org.atlassian.net/browse/GEOS-11517) Using various OGC APIs results in service enabled check related WARN logs
* [GEOS-11560](https://osgeo-org.atlassian.net/browse/GEOS-11560) OGC API modules lack cql2-json in assembly
* [GEOS-11563](https://osgeo-org.atlassian.net/browse/GEOS-11563) Allow configuring a DGGS resolution offset on a layer basis
* [GEOS-11565](https://osgeo-org.atlassian.net/browse/GEOS-11565) Allow configuring the minimum and maximum DGGS resolution for a layer
* [GEOS-11579](https://osgeo-org.atlassian.net/browse/GEOS-11579) DGGS modules prevent GeoServer startup if JEP is not installed

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.26 Series

Additional information on GeoServer 2.26 series:

* [GeoServer 2.26 User Manual](https://docs.geoserver.org/2.26.x/en/user/)
* [GeoServer 2024 Q3 Developer Update]({% post_url 2024-07-22-developer-update.md %}) 
* [Raster Attribute Table extension](https://github.com/geoserver/geoserver/wiki/GSIP-222)
* [Community module graduation, amending generality rule](https://github.com/geoserver/geoserver/wiki/GSIP-223)
* [Individual contributor clarification](https://github.com/geoserver/geoserver/wiki/GSIP-224)
* [Migrate geoserver-users from SourceForge to discourse](https://github.com/geoserver/geoserver/wiki/GSIP-225)

Release notes:
( [2.26.1](https://github.com/geoserver/geoserver/releases/tag/2.26.1)
| [2.26.0](https://github.com/geoserver/geoserver/releases/tag/2.26.0)
| [2.26-M0](https://github.com/geoserver/geoserver/releases/tag/2.26-M0)
) 

