---
author: Jody Garnett
date: 2025-05-13
layout: post
title: GeoServer 2.25.7 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_225
version: 2.25.7
jira_version: 17074
--- 

GeoServer [2.25.7](/release/2.25.7/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.7/geoserver-2.25.7-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.7/geoserver-2.25.7-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.7/GeoServer-2.25.7-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.7/geoserver-2.25.7-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.7/extensions/).

This series has previously reached end-of-life, with this release issued to address an urgent bug or security vulnerability. Please apply this update as a mitigation measure only, and plan to upgrade to a stable or maintenance release of GeoServer.
GeoServer 2.25.7 is made in conjunction with GeoTools 31.7. 

Thanks to Jody Garnett for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is considered an critical upgrade for production systems.

<!-- update cve list details when disclosed -->

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

## Release notes

Improvement:


Bug:

* [GEOS-11774](https://osgeo-org.atlassian.net/browse/GEOS-11774) Logout with OAuth plugin will give error if logged in locally

Task:

* [GEOS-11770](https://osgeo-org.atlassian.net/browse/GEOS-11770) Update to jai-ext 1.1.31

For the complete list see [2.25.7](https://github.com/geoserver/geoserver/releases/tag/2.25.7) release notes. 

## Community Updates

Community module development:

* [GEOS-11762](https://osgeo-org.atlassian.net/browse/GEOS-11762) Feature Templates by feature type can not be listed via GeoServer Rest API
* [GEOS-11783](https://osgeo-org.atlassian.net/browse/GEOS-11783) Longitudinal profile process should allow for input chaining
* [GEOS-11784](https://osgeo-org.atlassian.net/browse/GEOS-11784) The longitudinal profile process should limit the number of points it can extract
* [GEOS-11785](https://osgeo-org.atlassian.net/browse/GEOS-11785) The longitudinal profile process should respect cancellation
* [GEOS-11786](https://osgeo-org.atlassian.net/browse/GEOS-11786) Longitudinal profile process: general performance improvements
* [GEOS-11811](https://osgeo-org.atlassian.net/browse/GEOS-11811) Features templating editor is unable to update and save the template body

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.25 Series

Additional information on GeoServer 2.25 series:

* [GeoServer 2.25 User Manual](https://docs.geoserver.org/2.25.x/en/user/)
* [GeoServer 2024 Roadmap Plannings]({% post_url 2024-01-03-roadmap %}) 
* [Raster Attribute Table extension](https://github.com/geoserver/geoserver/wiki/GSIP-222)
* [Individual contributor clarification](https://github.com/geoserver/geoserver/wiki/GSIP-224)

Release notes:
( [2.25.7](https://github.com/geoserver/geoserver/releases/tag/2.25.7)
| [2.25.6](https://github.com/geoserver/geoserver/releases/tag/2.25.6)
| [2.25.5](https://github.com/geoserver/geoserver/releases/tag/2.25.5)
| [2.25.4](https://github.com/geoserver/geoserver/releases/tag/2.25.4)
| [2.25.3](https://github.com/geoserver/geoserver/releases/tag/2.25.3)
| [2.25.2](https://github.com/geoserver/geoserver/releases/tag/2.25.2)
| [2.25.1](https://github.com/geoserver/geoserver/releases/tag/2.25.1)
| [2.25.0](https://github.com/geoserver/geoserver/releases/tag/2.25.0)
| [2.25-RC](https://github.com/geoserver/geoserver/releases/tag/2.25-RC)
) 

