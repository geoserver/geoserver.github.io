---
author: Jody Garnett
date: 2026-08-14
layout: post
title: GeoServer 3.0.1 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_30.
version: 3.0.1
jira_version: 18069
--- 

GeoServer [3.0.1](/release/3.0.1/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.1/geoserver-3.0.1-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.1/geoserver-3.0.1-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.1/GeoServer-3.0.1-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.1/geoserver-3.0.1-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.1/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 3.0.1 is made in conjunction with GeoTools 35.1, and GeoWebCache 2.0.1. 

Thanks to Andrea Aime (GeoSolutions) and Jody Garnett (GeoCat) for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is an urgent update for production systems.

* [GHSA-mqjf-5f49-2fjh](https://github.com/geotools/geotools/security/advisories/GHSA-mqjf-5f49-2fjh) Unauthenticated SQL injection in the jsonArrayContains filter function against PostGIS layers (High)
  
  This releases includes the GeoTools 35.1 resolution of the above SQL Injection
  vulnerability which affects PostGIS 12 and up.
  Unfortunately our coordinated vulnerability disclosure policy was not followed in this case.
  This post will be updated with an official CVE number when one is available.

The use of the CVE system allows the GeoServer team to reach a wider audience than blog posts. 
See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Release notes

New Feature:

* [GEOS-12158](https://osgeo-org.atlassian.net/browse/GEOS-12158) Keycloak Role Service for use alongside OIDC Extension

Improvement:

* [GEOS-12095](https://osgeo-org.atlassian.net/browse/GEOS-12095) LDAP: conversion from group-member-username to user-search username
* [GEOS-12124](https://osgeo-org.atlassian.net/browse/GEOS-12124) Make GWC seeder thread pool sizes configurable via gwc-gs.xml and environment variables
* [GEOS-12139](https://osgeo-org.atlassian.net/browse/GEOS-12139) GSIP 241 - GeoWebCache Security-Aware Tile Caching
* [GEOS-12140](https://osgeo-org.atlassian.net/browse/GEOS-12140) Improve CoverageAccessLimits's RasterFilter masking on SecureGridCoverage2DReader reading
* [GEOS-12141](https://osgeo-org.atlassian.net/browse/GEOS-12141) WMS nearest match machinery can issue queries that are guaranteed to return an empty result
* [GEOS-12151](https://osgeo-org.atlassian.net/browse/GEOS-12151) Allow caching small images used by ImageMosaic in memory
* [GEOS-12154](https://osgeo-org.atlassian.net/browse/GEOS-12154) Improve URL validation in SLD processing
* [GEOS-12169](https://osgeo-org.atlassian.net/browse/GEOS-12169) Update MapML viewer to v0.18.0

Bug:

* [GEOS-11373](https://osgeo-org.atlassian.net/browse/GEOS-11373) Geometry type mismatch in WFS 1.1.0
* [GEOS-12144](https://osgeo-org.atlassian.net/browse/GEOS-12144) "application/vnd.ogc.fg+json" output format fails when requesting non-geographical datasets
* [GEOS-12145](https://osgeo-org.atlassian.net/browse/GEOS-12145) Missing spatial filter in `GeoFenceAccessManager` SQL query when only CLIP is applied
* [GEOS-12146](https://osgeo-org.atlassian.net/browse/GEOS-12146) Wrong CRS axis order used in `SecuredFeatureSource` when clipping features for WFS 2.0.0 requests
* [GEOS-12149](https://osgeo-org.atlassian.net/browse/GEOS-12149) GeoServer WMTS capabilities put query parameters in the wrong place in generated URLs
* [GEOS-12165](https://osgeo-org.atlassian.net/browse/GEOS-12165) GeoServer does not start when fileLockProvider is set: lock wait times out

Sub-task:


For the complete list see [3.0.1](https://github.com/geoserver/geoserver/releases/tag/3.0.1) release notes. 

## Community Updates

Community module development:

* [GEOS-12173](https://osgeo-org.atlassian.net/browse/GEOS-12173) Remove the REST module profile from community modules as the module does not exist here

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 3.0 Series

Additional information on GeoServer 3.0 series:

* [GeoServer 3.0 User Manual](https://docs.geoserver.org/3.0.x/en/user/)
* [GeoServer 3.0-RC, a crowdfunded success story]({% post_url 2026-04-21-geoserver-3-rc-crowdfunding-success %})
* [GSIP-221](https://github.com/geoserver/geoserver/wiki/GSIP-221) MkDocs Migration
* [GSIP-226](https://github.com/geoserver/geoserver/wiki/GSIP-226) GeoServer 3
* [GSIP-233](https://github.com/geoserver/geoserver/wiki/GSIP-233) Community Pending Profile
* [GSIP-236](https://github.com/geoserver/geoserver/wiki/GSIP-236) Lightening up the Core for GeoServer 3
* [GSIP-238](https://github.com/geoserver/geoserver/wiki/GSIP-238) UI / UX Refresh
* [GSIP 239](https://github.com/geoserver/geoserver/wiki/GSIP-239) Promote OIDC Community Module to Extension

Release notes:
( [3.0.1](https://github.com/geoserver/geoserver/releases/tag/3.0.1)
| [3.0.0](https://github.com/geoserver/geoserver/releases/tag/3.0.0)
) 

