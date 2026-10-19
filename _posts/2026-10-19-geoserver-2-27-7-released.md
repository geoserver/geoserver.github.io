---
author: Jody Garnett
date: 2026-10-19
layout: post
title: GeoServer 2.27.7 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_227
version: 2.27.7
jira_version: 18140
--- 

GeoServer [2.27.7](/release/2.27.7/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.7/geoserver-2.27.7-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.7/geoserver-2.27.7-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.7/GeoServer-2.27.7-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.7/geoserver-2.27.7-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.7/extensions/).

This series has previously reached end-of-life, with this release issued to address an urgent bug or security vulnerability. Please apply this update as a mitigation measure only, and plan to upgrade to a stable or maintenance release of GeoServer.

GeoServer 2.27.7 is made in conjunction with GeoTools 33.7. 

Thanks to Peter Smythe (AfriGIS) for making this release, and Andrea Aime (GeoSolutions) for testing.

## Security Considerations

This release addresses security vulnerabilities and is an important upgrade for production systems, details about the fixes will be provided at the start of November.

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Release notes

Improvement:

* [GEOS-12099](https://osgeo-org.atlassian.net/browse/GEOS-12099) GWC backup deadlock caused by DefaultTileLayerCatalog FileSystem
* [GEOS-12127](https://osgeo-org.atlassian.net/browse/GEOS-12127) Fix flaky tests causing non-deterministic CI failures
* [GEOS-12154](https://osgeo-org.atlassian.net/browse/GEOS-12154) Improve URL validation in SLD processing
* [GEOS-12195](https://osgeo-org.atlassian.net/browse/GEOS-12195) Refactoring of service resolution in Dispatcher
* [GEOS-12199](https://osgeo-org.atlassian.net/browse/GEOS-12199) Apply the catalog's entity resolver consistently to stored query parsing
* [GEOS-12211](https://osgeo-org.atlassian.net/browse/GEOS-12211) WPS: clean up GDAL configuration parsing
* [GEOS-12234](https://osgeo-org.atlassian.net/browse/GEOS-12234) Report invalid connection settings when saving JDBC user/group, role and authentication services
* [GEOS-12235](https://osgeo-org.atlassian.net/browse/GEOS-12235) Centralize remote IP resolution into a servlet filter
* [GEOS-12237](https://osgeo-org.atlassian.net/browse/GEOS-12237) The style editor layer preview breaks with invalid chars in style names
* [GEOS-12238](https://osgeo-org.atlassian.net/browse/GEOS-12238) CSW: Clearer exception in DirectDownload invalid requests
* [GEOS-12239](https://osgeo-org.atlassian.net/browse/GEOS-12239) Read JDBC user and role property values as text.
* [GEOS-12240](https://osgeo-org.atlassian.net/browse/GEOS-12240) Clearer stored query error messages when query id is too long

Bug:

* [GEOS-12100](https://osgeo-org.atlassian.net/browse/GEOS-12100) Use SyncTaskExecutor to prevent deadlock in backup/restore tasklets

Task:

* [GEOS-12136](https://osgeo-org.atlassian.net/browse/GEOS-12136) IOTestUtils.createRandomDirectory() replacing mkdir call to more recent java.nio.files API
* [GEOS-12160](https://osgeo-org.atlassian.net/browse/GEOS-12160) Add URL checks to wps-download-plugin

For the complete list see [2.27.7](https://github.com/geoserver/geoserver/releases/tag/2.27.7) release notes. 

## Community Updates

Community module development:

* [GEOS-12219](https://osgeo-org.atlassian.net/browse/GEOS-12219) Remove the gwc-sqlite community module
* [GEOS-12222](https://osgeo-org.atlassian.net/browse/GEOS-12222) JWT-Header: Improvements and documentation clarifications

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
( [2.27.7](https://github.com/geoserver/geoserver/releases/tag/2.27.7)
| [2.27.6](https://github.com/geoserver/geoserver/releases/tag/2.27.6)
| [2.27.5](https://github.com/geoserver/geoserver/releases/tag/2.27.5)
| [2.27.4](https://github.com/geoserver/geoserver/releases/tag/2.27.4)
| [2.27.3](https://github.com/geoserver/geoserver/releases/tag/2.27.3)
| [2.27.2](https://github.com/geoserver/geoserver/releases/tag/2.27.2)
| [2.27.1](https://github.com/geoserver/geoserver/releases/tag/2.27.1)
| [2.27.0](https://github.com/geoserver/geoserver/releases/tag/2.27.0)
) 

