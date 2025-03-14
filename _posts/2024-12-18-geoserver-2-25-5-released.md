---
author: Andrea Aime
date: 2024-12-18
layout: post
title: GeoServer 2.25.5 Release
categories:
- Announcements
tags:
- Release
release: release_225
version: 2.25.5
jira_version: 16938
--- 

GeoServer [2.25.5](/release/2.25.5/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.5/geoserver-2.25.5-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.5/geoserver-2.25.5-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.5/GeoServer-2.25.5-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.5/geoserver-2.25.5-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.5/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.
GeoServer 2.25.5 is made in conjunction with GeoTools 31.5, and GeoWebCache 1.25.3. 
The final release of the 2.25 series is planned for February 2025, please start making plans for an upgrade to 2.26.x or newer.

Thanks to Andrea Aime (GeoSolutions) for making this release. 

## Release notes

Improvement:

* [GEOS-11612](https://osgeo-org.atlassian.net/browse/GEOS-11612) Add system property support for Proxy base URL -> use headers activation
* [GEOS-11616](https://osgeo-org.atlassian.net/browse/GEOS-11616) GSIP 229 - File system access isolation
* [GEOS-11644](https://osgeo-org.atlassian.net/browse/GEOS-11644) Introducing the rest/security/acl/catalog/reload rest endpoint

Bug:

* [GEOS-11494](https://osgeo-org.atlassian.net/browse/GEOS-11494) WFS GetFeature request with a propertyname parameter fails when layer attributes are customized (removed or reordered)
* [GEOS-11606](https://osgeo-org.atlassian.net/browse/GEOS-11606) geofence-server imports obsolete asm dep
* [GEOS-11611](https://osgeo-org.atlassian.net/browse/GEOS-11611) When Extracting the WFS Service Name from the HTTP Request A Slash Before the Question Marks Causes Issues
* [GEOS-11643](https://osgeo-org.atlassian.net/browse/GEOS-11643) WCS input read limits can be fooled by geotiff reader

Task:

* [GEOS-11609](https://osgeo-org.atlassian.net/browse/GEOS-11609) Bump XStream from 1.4.20 to 1.4.21
* [GEOS-11610](https://osgeo-org.atlassian.net/browse/GEOS-11610) Update Jetty from 9.4.55.v20240627 to 9.4.56.v20240826
* [GEOS-11631](https://osgeo-org.atlassian.net/browse/GEOS-11631) Update MySQL driver to 9.1.0

For the complete list see [2.25.5](https://github.com/geoserver/geoserver/releases/tag/2.25.5) release notes. 

## Community Updates

Community module development:

* [GEOS-11635](https://osgeo-org.atlassian.net/browse/GEOS-11635) Add support for opaque auth tokens in OpenID connect
* [GEOS-11637](https://osgeo-org.atlassian.net/browse/GEOS-11637) DGGS min/max resolution settings stop working after restart

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.25 Series

Additional information on GeoServer 2.25 series:

* [GeoServer 2.25 User Manual](https://docs.geoserver.org/2.25.x/en/user/)
* [GeoServer 2024 Roadmap Plannings]({% post_url 2024-01-03-roadmap %}) 
* [Raster Attribute Table extension](https://github.com/geoserver/geoserver/wiki/GSIP-222)
* [Individual contributor clarification](https://github.com/geoserver/geoserver/wiki/GSIP-224)

Release notes:
( [2.25.5](https://github.com/geoserver/geoserver/releases/tag/2.25.5)
| [2.25.4](https://github.com/geoserver/geoserver/releases/tag/2.25.4)
| [2.25.3](https://github.com/geoserver/geoserver/releases/tag/2.25.3)
| [2.25.2](https://github.com/geoserver/geoserver/releases/tag/2.25.2)
| [2.25.1](https://github.com/geoserver/geoserver/releases/tag/2.25.1)
| [2.25.0](https://github.com/geoserver/geoserver/releases/tag/2.25.0)
| [2.25-RC](https://github.com/geoserver/geoserver/releases/tag/2.25-RC)
) 

