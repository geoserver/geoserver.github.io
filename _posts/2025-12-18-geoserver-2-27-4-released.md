---
author: Peter Smythe
date: 2025-12-18
layout: post
title: GeoServer 2.27.4 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_227
version: 2.27.4
jira_version: 17570
--- 

GeoServer [2.27.4](/release/2.27.4/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.4/geoserver-2.27.4-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.4/geoserver-2.27.4-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.4/GeoServer-2.27.4-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.4/geoserver-2.27.4-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.4/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.
GeoServer 2.27.4 is made in conjunction with GeoTools 33.4, and GeoWebCache 1.27.4. 

Thanks to Peter Smythe (AfriGIS) for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is an important upgrade for production systems.

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Release notes

Improvement:

* [GEOS-12012](https://osgeo-org.atlassian.net/browse/GEOS-12012) Switching CSVPPIO Strategy from ATTRIBUTES_ONLY_STRATEGY to WKT_STRATEGY

Bug:

* [GEOS-10509](https://osgeo-org.atlassian.net/browse/GEOS-10509) WFS Request fails when XML POST body is larger than 8kB
* [GEOS-11926](https://osgeo-org.atlassian.net/browse/GEOS-11926) ogcapi plugin makes WFS advertising an outputFormat which is actually unavailable
* [GEOS-11930](https://osgeo-org.atlassian.net/browse/GEOS-11930) OGC-API extension breaks security REST API 
* [GEOS-11965](https://osgeo-org.atlassian.net/browse/GEOS-11965) KMZ export incorrectly references remote icon URLs instead of embedding them in the KMZ archive
* [GEOS-11981](https://osgeo-org.atlassian.net/browse/GEOS-11981) POST /security/authproviders | 400: Unsupported className
* [GEOS-11988](https://osgeo-org.atlassian.net/browse/GEOS-11988) Fix bug: preserve metaTilingThreads=0 in saneConfig()

For the complete list see [2.27.4](https://github.com/geoserver/geoserver/releases/tag/2.27.4) release notes. 

## Community Updates

Community module development:

* [GEOS-11947](https://osgeo-org.atlassian.net/browse/GEOS-11947) Add the ability to skip numberMatched in STAC/OpenSearch for EO responses
* [GEOS-11983](https://osgeo-org.atlassian.net/browse/GEOS-11983) GSR /query fails with HTTP 500 when where parameter is empty
* [GEOS-12000](https://osgeo-org.atlassian.net/browse/GEOS-12000) Ignore DescribeFeatureType requests without typeName in Features Templating schemas override

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
( [2.27.4](https://github.com/geoserver/geoserver/releases/tag/2.27.4)
| [2.27.3](https://github.com/geoserver/geoserver/releases/tag/2.27.3)
| [2.27.2](https://github.com/geoserver/geoserver/releases/tag/2.27.2)
| [2.27.1](https://github.com/geoserver/geoserver/releases/tag/2.27.1)
| [2.27.0](https://github.com/geoserver/geoserver/releases/tag/2.27.0)
) 

