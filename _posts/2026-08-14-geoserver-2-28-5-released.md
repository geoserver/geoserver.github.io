---
author: Jody Garnett
date: 2026-08-14
layout: post
title: GeoServer 2.28.5 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_228
version: 2.28.5
jira_version: 18034
--- 

GeoServer [2.28.5](/release/2.28.5/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.5/geoserver-2.28.5-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.5/geoserver-2.28.5-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.5/GeoServer-2.28.5-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.5/geoserver-2.28.5-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.5/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.
GeoServer 2.28.5 is made in conjunction with GeoTools 34.5, and GeoWebCache 1.28.5. 

Thanks to Andrea Aime (GeoSolutions) and Jody Garnett (GeoCat) for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is an urgent update for production systems.

* [GHSA-mqjf-5f49-2fjh](https://github.com/geotools/geotools/security/advisories/GHSA-mqjf-5f49-2fjh) Unauthenticated SQL injection in the jsonArrayContains filter function against PostGIS layers (High)
  
  This releases includes the GeoTools 34.5 resolution of the above SQL Injection
  vulnerability which affects PostGIS 12 and up.
  Unfortunately our coordinated vulnerability disclosure policy was not followed in this case.
  This post will be updated with an official CVE number when one is available.

The use of the CVE system allows the GeoServer team to reach a wider audience than blog posts. 
See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Release notes

Improvement:

* [GEOS-12080](https://osgeo-org.atlassian.net/browse/GEOS-12080) style edit: check image loads
* [GEOS-12082](https://osgeo-org.atlassian.net/browse/GEOS-12082) CoverageStore - quick fail for incorrect files
* [GEOS-12095](https://osgeo-org.atlassian.net/browse/GEOS-12095) LDAP: conversion from group-member-username to user-search username
* [GEOS-12140](https://osgeo-org.atlassian.net/browse/GEOS-12140) Improve CoverageAccessLimits's RasterFilter masking on SecureGridCoverage2DReader reading
* [GEOS-12141](https://osgeo-org.atlassian.net/browse/GEOS-12141) WMS nearest match machinery can issue queries that are guaranteed to return an empty result
* [GEOS-12151](https://osgeo-org.atlassian.net/browse/GEOS-12151) Allow caching small images used by ImageMosaic in memory

Bug:

* [GEOS-11373](https://osgeo-org.atlassian.net/browse/GEOS-11373) Geometry type mismatch in WFS 1.1.0
* [GEOS-11571](https://osgeo-org.atlassian.net/browse/GEOS-11571) The geoserver-2.26.0-printing-plugin is missing some dependend libraries
* [GEOS-12138](https://osgeo-org.atlassian.net/browse/GEOS-12138) Improve DescribeDomains expandLimit validation
* [GEOS-12145](https://osgeo-org.atlassian.net/browse/GEOS-12145) Missing spatial filter in `GeoFenceAccessManager` SQL query when only CLIP is applied
* [GEOS-12146](https://osgeo-org.atlassian.net/browse/GEOS-12146) Wrong CRS axis order used in `SecuredFeatureSource` when clipping features for WFS 2.0.0 requests
* [GEOS-12149](https://osgeo-org.atlassian.net/browse/GEOS-12149) GeoServer WMTS capabilities put query parameters in the wrong place in generated URLs
* [GEOS-12165](https://osgeo-org.atlassian.net/browse/GEOS-12165) GeoServer does not start when fileLockProvider is set: lock wait times out

Task:

* [GEOS-12137](https://osgeo-org.atlassian.net/browse/GEOS-12137) Update OSHI from 6.8.2 to 7.3.0
* [GEOS-12148](https://osgeo-org.atlassian.net/browse/GEOS-12148) Update GetFeatureInfo to list features (rather than as a table)

Sub-task:

* [GEOS-12153](https://osgeo-org.atlassian.net/browse/GEOS-12153) Include description in AttributeMap

For the complete list see [2.28.5](https://github.com/geoserver/geoserver/releases/tag/2.28.5) release notes. 

## Community Updates

Community module development:

* [GEOS-12129](https://osgeo-org.atlassian.net/browse/GEOS-12129) Longitudinal profile positive altitude includes first elevation as ascent from zero
* [GEOS-12173](https://osgeo-org.atlassian.net/browse/GEOS-12173) Remove the REST module profile from community modules as the module does not exist here

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.28 Series

Additional information on GeoServer 2.28 series:

* [GeoServer 2.28 User Manual](https://docs.geoserver.org/2.28.x/en/user/)
* [GeoServer 2025 Q4 Developer Update]({% post_url 2025-10-14-developer-update %})
* [GSIP-234](https://github.com/geoserver/geoserver/wiki/GSIP-234) Advertise and Enforce Attribute Restrictions

Release notes:
( [2.28.5](https://github.com/geoserver/geoserver/releases/tag/2.28.5)
| [2.28.4](https://github.com/geoserver/geoserver/releases/tag/2.28.4)
| [2.28.3](https://github.com/geoserver/geoserver/releases/tag/2.28.3)
| [2.28.2](https://github.com/geoserver/geoserver/releases/tag/2.28.2)
| [2.28.1](https://github.com/geoserver/geoserver/releases/tag/2.28.1)
| [2.28.0](https://github.com/geoserver/geoserver/releases/tag/2.28.0)
) 

