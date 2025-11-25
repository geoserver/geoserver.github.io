---
author: Andrea Aime
date: 2025-11-25
layout: post
title: GeoServer 2.28.1 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_228
version: 2.28.1
jira_version: 17537
--- 

GeoServer [2.28.1](/release/2.28.1/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.1/geoserver-2.28.1-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.1/geoserver-2.28.1-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.1/GeoServer-2.28.1-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.1/geoserver-2.28.1-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.1/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 2.28.1 is made in conjunction with GeoTools 34.1, and GeoWebCache 1.28.1. 

Thanks to Andrea Aime for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is considered an important upgrade for production systems.

* [GEOS-11921](https://osgeo-org.atlassian.net/browse/GEOS-11921) - [CVE-2025-21621](https://github.com/geoserver/geoserver/security/advisories/GHSA-w66h-j855-qr72) - Reflected Cross-Site Scripting (XSS) vulnerability in WMS GetFeatureInfo HTML format (Moderate)
* [GEOS-11922](https://osgeo-org.atlassian.net/browse/GEOS-11922) - [CVE-2025-58360](https://github.com/geoserver/geoserver/security/advisories/GHSA-fjf5-xgmq-5525) - Unauthenticated XXE via WMS GetMap (High)

The use of the CVE system allows the GeoServer team to reach a wider audience than blog posts.

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.
 

## Release notes

Improvement:

* [GEOS-11950](https://osgeo-org.atlassian.net/browse/GEOS-11950) WMS cascade: fully respect ‘restrict to layer bounds’ flag on GetMap requests

Bug:

* [GEOS-4159](https://osgeo-org.atlassian.net/browse/GEOS-4159) Layer from SQL view feature type details not refreshing after editing sql query (and refreshing attributes there)
* [GEOS-11930](https://osgeo-org.atlassian.net/browse/GEOS-11930) OGC-API extension breaks security REST API 
* [GEOS-11963](https://osgeo-org.atlassian.net/browse/GEOS-11963) BlobStorePage breaks when failing to save a blob store configuration
* [GEOS-11965](https://osgeo-org.atlassian.net/browse/GEOS-11965) KMZ export incorrectly references remote icon URLs instead of embedding them in the KMZ archive
* [GEOS-11981](https://osgeo-org.atlassian.net/browse/GEOS-11981) POST /security/authproviders | 400: Unsupported className
* [GEOS-11988](https://osgeo-org.atlassian.net/browse/GEOS-11988) Fix bug: preserve metaTilingThreads=0 in saneConfig()

Task:

* [GEOS-11898](https://osgeo-org.atlassian.net/browse/GEOS-11898) GeoFence: issues in evaluation of virtual layer services access
* [GEOS-11962](https://osgeo-org.atlassian.net/browse/GEOS-11962) Run CITE tests against Java 17, 21 and 25
* [GEOS-11987](https://osgeo-org.atlassian.net/browse/GEOS-11987) ImageN 0.9.1 migration requires renaming of registryFile.jai to registryFile.imagen

For the complete list see [2.28.1](https://github.com/geoserver/geoserver/releases/tag/2.28.1) release notes. 

## Community Updates

Community module development:

* [GEOS-11959](https://osgeo-org.atlassian.net/browse/GEOS-11959) New community module GeoWebCache Google Cloud Storage 
* [GEOS-11961](https://osgeo-org.atlassian.net/browse/GEOS-11961) OSEO layer management: Support creation of image mosaics in CRS other than 4326
* [GEOS-11980](https://osgeo-org.atlassian.net/browse/GEOS-11980) Add support for uploading a single parquet file to GeoServer via REST
* [GEOS-11983](https://osgeo-org.atlassian.net/browse/GEOS-11983) GSR /query fails with HTTP 500 when where parameter is empty

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.28 Series

Additional information on GeoServer 2.28 series:

* [GeoServer 2.28 User Manual](https://docs.geoserver.org/2.28.x/en/user/)
* [GeoServer 2025 Q4 Developer Update]({% post_url 2025-10-14-developer-update %})* [Advertise and Enforce Attribute Restrictions](https://github.com/geoserver/geoserver/wiki/GSIP-234)

Release notes:
( [2.28.1](https://github.com/geoserver/geoserver/releases/tag/2.28.1)
| [2.28.0](https://github.com/geoserver/geoserver/releases/tag/2.28.0)
| [2.28-M0](https://github.com/geoserver/geoserver/releases/tag/2.28-M0)
) 

