---
author: Jody Garnett
date: 2026-10-19
layout: post
title: GeoServer 2.28.6 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_228
version: 2.28.6
jira_version: 18103
--- 

GeoServer [2.28.6](/release/2.28.6/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.6/geoserver-2.28.6-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.6/geoserver-2.28.6-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.6/GeoServer-2.28.6-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.6/geoserver-2.28.6-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.6/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.
GeoServer 2.28.6 is made in conjunction with GeoTools 34.6, and GeoWebCache 1.28.6. 

Thanks to Peter Smythe (AfriGIS) for making this release, and Andrea Aime (GeoSolutions) for testing.

## Security Considerations

This release addresses security vulnerabilities and is an important upgrade for production systems.

This release contains vulnerabilities that have not yet been disclosed; details will be provided at the start of November.

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

See also the [Check for Updates](#check-for-updates) module announced below.

## Check for Updates

The new **Check for Updates** community module helps administrators stay on top of important security releases. It checks a small JSON feed on GitHub against the version you're running — entirely on your own server, with nothing about your installation sent anywhere. It can also expose the result through a REST endpoint for your own monitoring tools.

![Check for Updates status](https://docs.geoserver.org/main/en/user/community/updates-checker/status.png)

See the [Check for Updates documentation](https://docs.geoserver.org/main/en/user/community/updates-checker/) for details and installation instructions.

## Release notes

New Feature:

* [GEOS-12180](https://osgeo-org.atlassian.net/browse/GEOS-12180)  Add support for multi-layer tile caching (coalescing) in GWC

Improvement:

* [GEOS-12099](https://osgeo-org.atlassian.net/browse/GEOS-12099) GWC backup deadlock caused by DefaultTileLayerCatalog FileSystem
* [GEOS-12127](https://osgeo-org.atlassian.net/browse/GEOS-12127) Fix flaky tests causing non-deterministic CI failures
* [GEOS-12139](https://osgeo-org.atlassian.net/browse/GEOS-12139) GSIP 241 - GeoWebCache Security-Aware Tile Caching
* [GEOS-12154](https://osgeo-org.atlassian.net/browse/GEOS-12154) Improve URL validation in SLD processing
* [GEOS-12183](https://osgeo-org.atlassian.net/browse/GEOS-12183) CSS can trigger a bean loading circularity during startup
* [GEOS-12187](https://osgeo-org.atlassian.net/browse/GEOS-12187) GeoJSON vector tiles are empty when the layer is meta-tiled
* [GEOS-12195](https://osgeo-org.atlassian.net/browse/GEOS-12195) Refactoring of service resolution in Dispatcher
* [GEOS-12198](https://osgeo-org.atlassian.net/browse/GEOS-12198) Support single-tenant Microsoft Entra ID authentication
* [GEOS-12199](https://osgeo-org.atlassian.net/browse/GEOS-12199) Apply the catalog's entity resolver consistently to stored query parsing
* [GEOS-12203](https://osgeo-org.atlassian.net/browse/GEOS-12203) OIDC: let the identity provider assert the built-in "admin" account
* [GEOS-12205](https://osgeo-org.atlassian.net/browse/GEOS-12205) Support GDAL 3.12+ new Raster Attribute Table data types
* [GEOS-12209](https://osgeo-org.atlassian.net/browse/GEOS-12209) Allow admins to request all layers from CSW endpoints
* [GEOS-12211](https://osgeo-org.atlassian.net/browse/GEOS-12211) WPS: clean up GDAL configuration parsing
* [GEOS-12218](https://osgeo-org.atlassian.net/browse/GEOS-12218) The print extension ships with a snapshot jar
* [GEOS-12234](https://osgeo-org.atlassian.net/browse/GEOS-12234) Report invalid connection settings when saving JDBC user/group, role and authentication services
* [GEOS-12235](https://osgeo-org.atlassian.net/browse/GEOS-12235) Centralize remote IP resolution into a servlet filter
* [GEOS-12237](https://osgeo-org.atlassian.net/browse/GEOS-12237) The style editor layer preview breaks with invalid chars in style names
* [GEOS-12238](https://osgeo-org.atlassian.net/browse/GEOS-12238) CSW: Clearer exception in DirectDownload invalid requests
* [GEOS-12239](https://osgeo-org.atlassian.net/browse/GEOS-12239) Read JDBC user and role property values as text.
* [GEOS-12240](https://osgeo-org.atlassian.net/browse/GEOS-12240) Clearer stored query error messages when query id is too long

Bug:

* [GEOS-12065](https://osgeo-org.atlassian.net/browse/GEOS-12065) WMS Layer REST PUT always returns 500 due to Collections.emptySet() in getRemoteStyleInfos()
* [GEOS-12100](https://osgeo-org.atlassian.net/browse/GEOS-12100) Use SyncTaskExecutor to prevent deadlock in backup/restore tasklets
* [GEOS-12159](https://osgeo-org.atlassian.net/browse/GEOS-12159) ReprojectingFeatureCollection throws ClassCastException reprojecting per-feature geometry between two Geographic 3D CRSs
* [GEOS-12193](https://osgeo-org.atlassian.net/browse/GEOS-12193) "Encode coordinates measures" gives different geometries per GML version
* [GEOS-12206](https://osgeo-org.atlassian.net/browse/GEOS-12206) WMTS Multidim operations (DescribeDomains/GetHistogram/...) do not honor datasecurity
* [GEOS-12213](https://osgeo-org.atlassian.net/browse/GEOS-12213) Changing the workspace of a WMS/WMTS cascaded store does not update its layers
* [GEOS-12216](https://osgeo-org.atlassian.net/browse/GEOS-12216) Datadir loader fails on cross-workspace resource references

Task:

* [GEOS-12136](https://osgeo-org.atlassian.net/browse/GEOS-12136) IOTestUtils.createRandomDirectory() replacing mkdir call to more recent java.nio.files API
* [GEOS-12160](https://osgeo-org.atlassian.net/browse/GEOS-12160) Add URL checks to wps-download-plugin

For the complete list see [2.28.6](https://github.com/geoserver/geoserver/releases/tag/2.28.6) release notes. 

## Community Updates

Community module development:

* [GEOS-12182](https://osgeo-org.atlassian.net/browse/GEOS-12182) Support Azure SAS token authentication for COG stores
* [GEOS-12219](https://osgeo-org.atlassian.net/browse/GEOS-12219) Remove the gwc-sqlite community module
* [GEOS-12221](https://osgeo-org.atlassian.net/browse/GEOS-12221) WPS Longitudinal Profile: compute distances on the ground
* [GEOS-12222](https://osgeo-org.atlassian.net/browse/GEOS-12222) JWT-Header: Improvements and documentation clarifications

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.28 Series

Additional information on GeoServer 2.28 series:

* [GeoServer 2.28 User Manual](https://docs.geoserver.org/2.28.x/en/user/)
* [GeoServer 2025 Q4 Developer Update]({% post_url 2025-10-14-developer-update %}) 
* [GSIP-234](https://github.com/geoserver/geoserver/wiki/GSIP-234) Advertise and Enforce Attribute Restrictions

Release notes:
( [2.28.6](https://github.com/geoserver/geoserver/releases/tag/2.28.6)
| [2.28.5](https://github.com/geoserver/geoserver/releases/tag/2.28.5)
| [2.28.4](https://github.com/geoserver/geoserver/releases/tag/2.28.4)
| [2.28.3](https://github.com/geoserver/geoserver/releases/tag/2.28.3)
| [2.28.2](https://github.com/geoserver/geoserver/releases/tag/2.28.2)
| [2.28.1](https://github.com/geoserver/geoserver/releases/tag/2.28.1)
| [2.28.0](https://github.com/geoserver/geoserver/releases/tag/2.28.0)
) 

