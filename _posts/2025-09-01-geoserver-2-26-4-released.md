---
author: Peter Smythe
date: 2025-09-01
layout: post
title: GeoServer 2.26.4 Release
categories:
- Announcements
tags:
- Release
release: release_226
version: 2.26.4
jira_version: 17210
--- 

GeoServer [2.26.4](/release/2.26.4/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.4/geoserver-2.26.4-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.4/geoserver-2.26.4-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.4/GeoServer-2.26.4-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.4/geoserver-2.26.4-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.4/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.
GeoServer 2.26.4 is made in conjunction with GeoTools 32.4, and GeoWebCache 1.26.4. 

Thanks to Peter Smythe (AfriGIS) for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is considered an important update for existing installations.

* CVE-2025-52465 High <!-- https://github.com/geoserver/geoserver/security/advisories/GHSA-7qmg-grcp-qf25 -->

<!-- update cve list details when disclosed --> 

The use of the CVE system allows the GeoServer team to reach a wider audience than blog posts. See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Upgrade instructions

Please take note of the [Upgrade Instructions](https://docs.geoserver.org/main/en/user/installation/upgrade.html), specifically:

The global setting Unrestricted XML External Entity Resolution has been replaced with the `ENTITY_RESOLUTION_UNRESTRICTED` application property.

* https://docs.geoserver.org/main/en/user/installation/upgrade.html#entity-resolution-unrestricted-application-property-geoserver-2-26-4-and-newer

## Release notes

New Feature:

* [GEOS-11805](https://osgeo-org.atlassian.net/browse/GEOS-11805) Option to disable the management of stored queries
* [GEOS-11911](https://osgeo-org.atlassian.net/browse/GEOS-11911) Application property ROOT_LOGIN_ENABLED

Improvement:

* [GEOS-11867](https://osgeo-org.atlassian.net/browse/GEOS-11867) Improve entity resolution
* [GEOS-11877](https://osgeo-org.atlassian.net/browse/GEOS-11877) Improve CoverageView composition to support noData fill on missing bands/coverages
* [GEOS-11892](https://osgeo-org.atlassian.net/browse/GEOS-11892) Column mentioning user that performed last modification for layers and stores list UI

Bug:

* [GEOS-10728](https://osgeo-org.atlassian.net/browse/GEOS-10728) Cannot download GeoPackage if the source data contains UUID types
* [GEOS-11820](https://osgeo-org.atlassian.net/browse/GEOS-11820) WCS spatial sub-setting does not work when native CRS != declared CRS
* [GEOS-11832](https://osgeo-org.atlassian.net/browse/GEOS-11832) count=0 service exception for some formats
* [GEOS-11866](https://osgeo-org.atlassian.net/browse/GEOS-11866) Prevent requests setting variables that should only be set by GeoServer
* [GEOS-11896](https://osgeo-org.atlassian.net/browse/GEOS-11896) WPS map download flips east/west coordinates
* [GEOS-11900](https://osgeo-org.atlassian.net/browse/GEOS-11900) CRS:XY syntax builds isolated CRSs that do not leverage the EPSG database transformation library

Task:

* [GEOS-11831](https://osgeo-org.atlassian.net/browse/GEOS-11831) OseoDispatcherCallback improvements
* [GEOS-11852](https://osgeo-org.atlassian.net/browse/GEOS-11852) Remove master password info page
* [GEOS-11853](https://osgeo-org.atlassian.net/browse/GEOS-11853) Clarify keystore vs master vs root password
* [GEOS-11854](https://osgeo-org.atlassian.net/browse/GEOS-11854) Generation of security/masterpw.info no longer required
* [GEOS-11869](https://osgeo-org.atlassian.net/browse/GEOS-11869) Replace entity resolution setting with application property

For the complete list see [2.26.4](https://github.com/geoserver/geoserver/releases/tag/2.26.4) release notes. 

## Community Updates

Community module development:

* [GEOS-11829](https://osgeo-org.atlassian.net/browse/GEOS-11829) Features templating ability to override schema
* [GEOS-11830](https://osgeo-org.atlassian.net/browse/GEOS-11830) Smart data loader create store page fails when environment variables are in use
* [GEOS-11839](https://osgeo-org.atlassian.net/browse/GEOS-11839) New Community Module for WPS Download in NetCDF output format for spatiotemporal coverages
* [GEOS-11847](https://osgeo-org.atlassian.net/browse/GEOS-11847) Next link is missing in "Search" OGC API - Features proposal implementation when startIndex is not set
* [GEOS-11871](https://osgeo-org.atlassian.net/browse/GEOS-11871) Allow native execution of group by in DGGS store, when grouping on geometries
* [GEOS-11876](https://osgeo-org.atlassian.net/browse/GEOS-11876) WPS Vertical Longitudinal Profile: Support automatic distance computation
* [GEOS-11878](https://osgeo-org.atlassian.net/browse/GEOS-11878) WFS HITS request returns the whole data records on a GML feature templated layer
* [GEOS-11880](https://osgeo-org.atlassian.net/browse/GEOS-11880) OGC API Maps is not showing up in GeoServer home page

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.26 Series

Additional information on GeoServer 2.26 series:

* [GeoServer 2.26 User Manual](https://docs.geoserver.org/2.26.x/en/user/)
* [GeoServer 2024 Q3 Developer Update]({% post_url 2024-07-22-developer-update %}) 
* [Raster Attribute Table extension](https://github.com/geoserver/geoserver/wiki/GSIP-222)
* [Community module graduation, amending generality rule](https://github.com/geoserver/geoserver/wiki/GSIP-223)
* [Individual contributor clarification](https://github.com/geoserver/geoserver/wiki/GSIP-224)
* [Migrate geoserver-users from SourceForge to discourse](https://github.com/geoserver/geoserver/wiki/GSIP-225)

Release notes:
( [2.26.4](https://github.com/geoserver/geoserver/releases/tag/2.26.4)
| [2.26.3](https://github.com/geoserver/geoserver/releases/tag/2.26.3)
| [2.26.2](https://github.com/geoserver/geoserver/releases/tag/2.26.2)
| [2.26.1](https://github.com/geoserver/geoserver/releases/tag/2.26.1)
| [2.26.0](https://github.com/geoserver/geoserver/releases/tag/2.26.0)
| [2.26-M0](https://github.com/geoserver/geoserver/releases/tag/2.26-M0)
) 

