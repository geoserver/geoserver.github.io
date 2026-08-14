---
author: Jody Garnett
date: 2026-08-14
layout: post
title: GeoServer 2.27.6 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_227
version: 2.27.6
jira_version: 17835
--- 

GeoServer [2.27.6](/release/2.27.6/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.6/geoserver-2.27.6-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.6/geoserver-2.27.6-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.6/GeoServer-2.27.6-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.6/geoserver-2.27.6-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.6/extensions/).

This series has previously reached end-of-life, with this release issued to address an urgent bug or security vulnerability. Please apply this update as a mitigation measure only, and plan to upgrade to a stable or maintenance release of GeoServer.

GeoServer 2.27.6 is made in conjunction with GeoTools 33.6. 

Thanks to Andrea Aime (GeoSolutions) and Jody Garnett (GeoCat) for making this release.

## Security Considerations

This release addresses security vulnerabilities and is an urgent update for production systems.

* [GHSA-mqjf-5f49-2fjh](https://github.com/geotools/geotools/security/advisories/GHSA-mqjf-5f49-2fjh) Unauthenticated SQL injection in the jsonArrayContains filter function against PostGIS layers (High)
  
  This releases includes the GeoTools 33.5 resolution of the above SQL Injection
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

Task:


For the complete list see [2.27.6](https://github.com/geoserver/geoserver/releases/tag/2.27.6) release notes. 

## Community Updates

Community module development:

* [GEOS-12098](https://osgeo-org.atlassian.net/browse/GEOS-12098) Rename JWT Header assembly so it is collected for nightly downloads
* [GEOS-12101](https://osgeo-org.atlassian.net/browse/GEOS-12101) Workspace styles not persisted to disk after restore
* [GEOS-12129](https://osgeo-org.atlassian.net/browse/GEOS-12129) Longitudinal profile positive altitude includes first elevation as ascent from zero

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.27 Series

Additional information on GeoServer 2.27 series:

* [GeoServer 2.27 User Manual](https://docs.geoserver.org/2.27.x/en/user/)
* [CITE Certification achieved]({% post_url 2025-07-16-cite-certification %}) 
* [GeoServer 2025 Q2 Developer Update]({% post_url 2025-05-13-developer-update %}) 
* [GeoServer 2025 Roadmap]({% post_url 2025-01-13-roadmap %}) 
* [Content-Security-Policy Headers](https://github.com/geoserver/geoserver/wiki/GSIP-227)
* [OGCAPI Features Extension](https://github.com/geoserver/geoserver/wiki/GSIP-230)
* [File system access isolation](https://github.com/geoserver/geoserver/wiki/GSIP-229)
* [Promote data dir catalog loader to core](https://github.com/geoserver/geoserver/wiki/GSIP-231)

Release notes:
( [2.27.6](https://github.com/geoserver/geoserver/releases/tag/2.27.6)
| [2.27.5](https://github.com/geoserver/geoserver/releases/tag/2.27.5)
| [2.27.4](https://github.com/geoserver/geoserver/releases/tag/2.27.4)
| [2.27.3](https://github.com/geoserver/geoserver/releases/tag/2.27.3)
| [2.27.2](https://github.com/geoserver/geoserver/releases/tag/2.27.2)
| [2.27.1](https://github.com/geoserver/geoserver/releases/tag/2.27.1)
| [2.27.0](https://github.com/geoserver/geoserver/releases/tag/2.27.0)
) 

