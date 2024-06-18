---
author: Jody Garnett
date: 2024-06-13
layout: post
title: GeoServer 2.23.6 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_223
version: 2.23.6
jira_version: 16917
--- 

GeoServer [2.23.6](/release/2.23.6/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.6/geoserver-2.23.6-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.6/geoserver-2.23.6-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.6/GeoServer-2.23.6-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.6/geoserver-2.23.6-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.6/extensions/).

This series has previously reached end-of-life, with this release issued to address an urgent bug or security vulnerability  (see CVE-2024-36401 below).

This GeoServer 2.23.6 update is provided as a temporary measure. Rather plan to upgrade to a stable GeoServer 2.23.6 or maintenance GeoServer 2.24.4. 

GeoServer 2.23.6 is made in conjunction with GeoTools 29.6, and GeoWebCache 1.23.5.

Thanks to Jody Garnett (GeoCat) for making this release on behalf of GeoCat customers.

## Security Considerations

This release addresses security vulnerabilities and is considered an essential update for production systems.

* CVE-2024-36401 Critical
* CVE-2024-24749 Moderate

The details of this vulnerability will be made available at the end of the month providing an opportunity to update.

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Release notes

Improvement:

* [GEOS-11327](https://osgeo-org.atlassian.net/browse/GEOS-11327) Add warning about using embedded data directories
* [GEOS-11347](https://osgeo-org.atlassian.net/browse/GEOS-11347) STAC Landing Page links should include root link

Bug:

* [GEOS-11331](https://osgeo-org.atlassian.net/browse/GEOS-11331) OAuth2 can throw a "java.lang.RuntimeException: Never should reach this point"

Task:

* [GEOS-11316](https://osgeo-org.atlassian.net/browse/GEOS-11316) Update Spring version to 5.3.32
* [GEOS-11318](https://osgeo-org.atlassian.net/browse/GEOS-11318) Upgrade postgresql from 42.6.0 to 42.7.2

For the complete list see [2.23.6](https://github.com/geoserver/geoserver/releases/tag/2.23.6) release notes.

## Community Updates

Community module development:

* [GEOS-11348](https://osgeo-org.atlassian.net/browse/GEOS-11348) JMS cluster does not allow to publish style via REST "2 step" approach
* [GEOS-11358](https://osgeo-org.atlassian.net/browse/GEOS-11358) Feature-Autopopulate Update operation does not apply the Update Element filter
* [GEOS-11381](https://osgeo-org.atlassian.net/browse/GEOS-11381) Error in OIDC plugin in combination with RoleService
* [GEOS-11412](https://osgeo-org.atlassian.net/browse/GEOS-11412) Remove reference to JDOM from JMS Cluster (as JDOM is no longer in use)

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.23 Series

Additional information on GeoServer 2.23 series:

* [GeoServer 2.23 User Manual](https://docs.geoserver.org/2.23.x/en/user/)
* [Drop Java 8](https://github.com/geoserver/geoserver/wiki/GSIP-215)
* [GUI CSS Cleanup](https://github.com/geoserver/geoserver/wiki/GSIP-213)
* [Add the possibility to use fixed values in Capabilities for Dimension metadata](https://github.com/geoserver/geoserver/wiki/GSIP-208)
* [State of GeoServer 2.23](https://docs.google.com/presentation/d/1nRKIILXWGLMGXZ6thfJgPR9kZ6Wh8Hp1dwZdQGw2YRc/edit?usp=share_link)
* [GeoServer Feature Frenzy 2023](https://docs.google.com/presentation/d/1vE8eCrOyewoH54g8CjuoiO3pxVLToEpuvpoZWmy0wTg/edit?usp=share_link)
* [GeoServer used in fun and interesting ways](https://docs.google.com/presentation/d/1PP2qk7eH8TzAf1tvEWH7Geattd0YFh7ZEDx1_tlrRWY/edit?usp=share_link)
* [GeoServer Orientation](https://docs.google.com/presentation/d/1sh9C4dIkDRnk3quCD1PRYoiJhjI9dqnAdOScJCgQWU8/edit?usp=share_link)

Release notes:
( [2.23.6](https://github.com/geoserver/geoserver/releases/tag/2.23.6)
| [2.23.5](https://github.com/geoserver/geoserver/releases/tag/2.23.5)
| [2.23.4](https://github.com/geoserver/geoserver/releases/tag/2.23.4)
| [2.23.3](https://github.com/geoserver/geoserver/releases/tag/2.23.3)
| [2.23.2](https://github.com/geoserver/geoserver/releases/tag/2.23.2)
| [2.23.1](https://github.com/geoserver/geoserver/releases/tag/2.23.1)
| [2.23.0](https://github.com/geoserver/geoserver/releases/tag/2.23.0)
| [2.23-RC1](https://github.com/geoserver/geoserver/releases/tag/2.23-RC1)
) 

