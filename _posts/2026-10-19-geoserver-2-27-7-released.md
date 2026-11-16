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

GeoServer 2.27.7 is made in conjunction with [GeoTools 33.7](https://github.com/geotools/geotools/releases/tag/33.7). 

Thanks to Peter Smythe (AfriGIS) for making this release, and Andrea Aime (GeoSolutions) for testing.

## Security Considerations

This release addresses security vulnerabilities and is an important upgrade for production systems.

* [CVE-2026-120705](https://github.com/geoserver/geoserver/security/advisories/GHSA-39mw-5chv-jh47) Unauthenticated WFS GetFeatureById XML injection (High)
* [CVE-2026-120701](https://github.com/geoserver/geoserver/security/advisories/GHSA-3x82-qq72-g4p3) Unauthenticated SSRF via WPS gs:DownloadMap (High, WPS Download extension)
* [CVE-2026-120706](https://github.com/geoserver/geoserver/security/advisories/GHSA-5v3x-f56f-2xm8) Unauthenticated SSRF and file read via WPS inline VRT to native GDAL (High, WPS extension)
* [CVE-2026-129243](https://github.com/geoserver/geoserver/security/advisories/GHSA-rv5g-g2r9-58rj) Service security rules bypassed with a prefixed service name such as x/WFS (High)
* [CVE-2026-129242](https://github.com/geoserver/geoserver/security/advisories/GHSA-9wf2-fcgq-vxhq) Deserialization in JDBC user and role services allows administrator code execution (High)
* [CVE-2026-120704](https://github.com/geoserver/geoserver/security/advisories/GHSA-wc3v-48j7-xf57) Remote code execution via SQLite JDBC extension loading in JDBC security services (High)
* [CVE-2026-120710](https://github.com/GeoWebCache/geowebcache/security/advisories/GHSA-xqwh-vc83-cp7g) Arbitrary file write via GeoWebCache FileRasterFilter ZIP update (High)
* [CVE-2026-129293](https://github.com/geoserver/geoserver/security/advisories/GHSA-3xvw-cfcr-v3h7) Stored XSS via style name in style editor Layer Preview (High)
* [CVE-2026-120707](https://github.com/geoserver/geoserver/security/advisories/GHSA-37mm-jp7f-64jp) GeoFence source IP rules bypass via X-Forwarded-For (High, GeoFence extension)
* [CVE-2026-120708](https://github.com/geoserver/geoserver/security/advisories/GHSA-9j5h-q8xc-hppq) ACL source IP rules bypass via X-Forwarded-For (High, ACL plugin)
* [CVE-2026-129294](https://github.com/geoserver/geoserver/security/advisories/GHSA-65mr-5frw-93xf) Unauthenticated style management in OGC API Styles (High, community module)
* [CVE-2026-120703](https://github.com/geoserver/geoserver/security/advisories/GHSA-vv34-hm2r-7h59) JWT Headers roles header trusted without validation (High, community module)
* [CVE-2026-129240](https://github.com/geoserver/geoserver/security/advisories/GHSA-rg89-jmrw-x26f) Local file probing via file:// schemaLocation during strict schema validation (Medium)
* [CVE-2026-120709](https://github.com/geoserver/geoserver/security/advisories/GHSA-9vfc-p7x6-xxwh) Unauthenticated SSRF and file read via printing legend icon URL (Medium, printing extension)
* [CVE-2026-129244](https://github.com/geoserver/geoserver/security/advisories/GHSA-4v26-c537-jvxc) WFS stored query exception discloses data directory path (Medium)
* [CVE-2026-120702](https://github.com/geoserver/geoserver/security/advisories/GHSA-8w5h-q76f-7mc7) CSW DirectDownload served for layers where it is disabled (Medium)

The use of the CVE system allows the GeoServer team to reach a wider audience than blog posts.

It is worth repeating that the 2.27 series has reached end-of-life. While we understand that this is the last series supporting Java 8 please update to the supported 2.28 or 3.0 releases.

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
* [GEOS-12259](https://osgeo-org.atlassian.net/browse/GEOS-12259) [CVE-2026-120702] CSW DirectDownload served for layers where it is disabled
* [GEOS-12264](https://osgeo-org.atlassian.net/browse/GEOS-12264) [CVE-2026-120708] ACL Source IP rules bypass via X-Forwarded-For
* [GEOS-12268](https://osgeo-org.atlassian.net/browse/GEOS-12268) [CVE-2026-129294] Unauthenticated style management in OGC API Styles
* [GEOS-12269](https://osgeo-org.atlassian.net/browse/GEOS-12269) [CVE-2026-120707] GeoFence source IP rules bypass via X-Forwarded-For
* [GEOS-12270](https://osgeo-org.atlassian.net/browse/GEOS-12270) [CVE-2026-120703] JWT Headers community module roles header trusted without validation
* [GEOS-12271](https://osgeo-org.atlassian.net/browse/GEOS-12271) [CVE-2026-120710] Arbitrary file write via GeoWebCache FileRasterFilter ZIP update
* [GEOS-12272](https://osgeo-org.atlassian.net/browse/GEOS-12272) [CVE-2026-120706] Unauthenticated SSRF and file read via WPS inline VRT to native GDAL
* [GEOS-12274](https://osgeo-org.atlassian.net/browse/GEOS-12274) [CVE-2026-120709] Unauthenticated SSRF and file read via printing legend icon URL
* [GEOS-12281](https://osgeo-org.atlassian.net/browse/GEOS-12281) [CVE-2026-129293] Stored XSS via style name in style editor Layer Preview
* [GEOS-12282](https://osgeo-org.atlassian.net/browse/GEOS-12282) [CVE-2026-129244] WFS stored query exception discloses data directory path
* [GEOS-12283](https://osgeo-org.atlassian.net/browse/GEOS-12283) [CVE-2026-129242] Deserialization in JDBC user and role services allows administrator code execution
* [GEOS-12284](https://osgeo-org.atlassian.net/browse/GEOS-12284) [CVE-2026-129243] Service security rules bypassed with a prefixed service name such as x/WFS
* [GEOS-12291](https://osgeo-org.atlassian.net/browse/GEOS-12291) [CVE-2026-120701] Unauthenticated SSRF via WPS gs:DownloadMap
* [GEOS-12292](https://osgeo-org.atlassian.net/browse/GEOS-12292) [CVE-2026-120704] Remote code execution via SQLite JDBC extension loading in JDBC security services
* [GEOS-12293](https://osgeo-org.atlassian.net/browse/GEOS-12293) [CVE-2026-120705] Unauthenticated WFS GetFeatureById XML injection
* [GEOS-12297](https://osgeo-org.atlassian.net/browse/GEOS-12297) [CVE-2026-129240] Local file probing via file:// schemaLocation during strict schema validation

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

