---
author: Peter Smythe
date: 2026-02-18
layout: post
title: GeoServer 2.27.5 Release
categories:
- Announcements
tags:
- Release
release: release_227
version: 2.27.5
jira_version: 17703
--- 

GeoServer [2.27.5](/release/2.27.5/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.5/geoserver-2.27.5-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.5/geoserver-2.27.5-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.5/GeoServer-2.27.5-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.5/geoserver-2.27.5-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.5/extensions/).

This is the last scheduled maintenance release of GeoServer series 2.27 - providing existing installations with minor updates and bug fixes.
GeoServer 2.27.5 is made in conjunction with GeoTools 33.5, and GeoWebCache 1.27.5. 

Are you aware that the all new [GeoServer 3](https://geoserver.org/behind%20the%20scenes/2026/02/17/gs3-first-public-release-date.html) is just around the corner?

----

And, separately as a special sneak peek, if you're interested in ARM64 docker images (for example, on AWS, Graviton3 offers a 40% better price performance) then check out [this 2.27.5 release](https://hub.docker.com/repository/docker/petersmythe/geoserver-test/tags?name=2.27) as a multi-platform (amd64 & arm4) build, which will very soon be [merged](https://github.com/geoserver/docker/pull/263) into the official [docker.osgeo.org repo](https://docker.osgeo.org/#browse/browse:docker:v2%2Fgeoserver%2Ftags%2F2.27.5) as the new multi-architecture builder going forward.

Thanks to Peter Smythe (AfriGIS) for making this release and driving the ARM64 docker images. 

## Release notes

Improvement:

* [GEOS-12023](https://osgeo-org.atlassian.net/browse/GEOS-12023) Improve developer logging during catalog resources loading and WMS capabilities requests
* [GEOS-12033](https://osgeo-org.atlassian.net/browse/GEOS-12033) Allow to configure custom CRS authorities and transformations
* [GEOS-12037](https://osgeo-org.atlassian.net/browse/GEOS-12037) Support Metatiling on MapBox Vectortiles

Task:


For the complete list see [2.27.5](https://github.com/geoserver/geoserver/releases/tag/2.27.5) release notes. 

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
( [2.27.5](https://github.com/geoserver/geoserver/releases/tag/2.27.5)
| [2.27.4](https://github.com/geoserver/geoserver/releases/tag/2.27.4)
| [2.27.3](https://github.com/geoserver/geoserver/releases/tag/2.27.3)
| [2.27.2](https://github.com/geoserver/geoserver/releases/tag/2.27.2)
| [2.27.1](https://github.com/geoserver/geoserver/releases/tag/2.27.1)
| [2.27.0](https://github.com/geoserver/geoserver/releases/tag/2.27.0)
) 

