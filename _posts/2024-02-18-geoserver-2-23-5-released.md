---
author: Andrea Aime
date: 2024-02-18
layout: post
title: GeoServer 2.23.5 Release
categories:
- Announcements
tags:
- Release
release: release_223
version: 2.23.5
jira_version: 16910
--- 

GeoServer [2.23.5](/release/2.23.5/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.5/geoserver-2.23.5-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.5/geoserver-2.23.5-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.5/GeoServer-2.23.5-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.5/geoserver-2.23.5-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.5/extensions/).

This is the last planned maintenance release of GeoServer 2.23.x, providing existing installations with minor updates and bug fixes.
Sites using the 2.23.x series are encouraged to upgrade to GeoServer 2.24.x, or eventually wait next month, for the 2.25.0 release, and upgrade their installation, with the help of the [upgrade guide](https://docs.geoserver.org/main/en/user/installation/upgrade.html#notes-on-upgrading-specific-versions).

GeoServer 2.23.5 is made in conjunction with GeoTools 29.5, and GeoWebCache 1.23.4. 

Thanks to Andrea Aime (GeoSolutions) for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is considered an essential upgrade for production systems.

- [CVE-2024-23634](https://github.com/geoserver/geoserver/security/advisories/GHSA-75m5-hh4r-q9gx) Arbitrary file renaming vulnerability in REST Coverage/Data Store API (Moderate).

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Release notes

New Feature:

* [GEOS-11225](https://osgeo-org.atlassian.net/browse/GEOS-11225) AuthKey synchronize the user/group automatically
* [GEOS-11279](https://osgeo-org.atlassian.net/browse/GEOS-11279) metadata: allow same field on multiple tabs

Improvement:

* [GEOS-11213](https://osgeo-org.atlassian.net/browse/GEOS-11213) Improve REST external upload method unzipping
* [GEOS-11246](https://osgeo-org.atlassian.net/browse/GEOS-11246) Schemaless plugin performance for WFS
* [GEOS-11260](https://osgeo-org.atlassian.net/browse/GEOS-11260) JNDI tutorial uses outdated syntax
* [GEOS-11276](https://osgeo-org.atlassian.net/browse/GEOS-11276) Use style_body to define CSS style for a layer
* [GEOS-11288](https://osgeo-org.atlassian.net/browse/GEOS-11288) Improve input validation in ClasspathPublisher

Bug:

* [GEOS-11174](https://osgeo-org.atlassian.net/browse/GEOS-11174) GWC rest api returns erroneous truncated response when gzip http encoding is enabled 
* [GEOS-11205](https://osgeo-org.atlassian.net/browse/GEOS-11205) Layer page: style image fails if it is in isolated workspace
* [GEOS-11250](https://osgeo-org.atlassian.net/browse/GEOS-11250) WFS GeoJSON encoder fails with an exception if an infinity number is used in the geometry
* [GEOS-11255](https://osgeo-org.atlassian.net/browse/GEOS-11255) Multiple inserts in WPS with different idGen strategies does not work
* [GEOS-11256](https://osgeo-org.atlassian.net/browse/GEOS-11256) Cannot retrieve LegendGraphic from a PostGIS datastore with 'hideEmptyRules' and 'Support on the fly geometry simplification' enabled
* [GEOS-11278](https://osgeo-org.atlassian.net/browse/GEOS-11278) metadata: only selected tab is submitted
* [GEOS-11285](https://osgeo-org.atlassian.net/browse/GEOS-11285) GWC REST Content-Encoding gzip returns broken response
* [GEOS-11291](https://osgeo-org.atlassian.net/browse/GEOS-11291) GeoFence: Cleanup stale log4j references

For the complete list see [2.23.5](https://github.com/geoserver/geoserver/releases/tag/2.23.5) release notes. 

## Community Updates

Community module development:

* [GEOS-10933](https://osgeo-org.atlassian.net/browse/GEOS-10933) keycloak logout NPE
* [GEOS-11290](https://osgeo-org.atlassian.net/browse/GEOS-11290) With Oauth enabled, anon users get random auth requests

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
( [2.23.5](https://github.com/geoserver/geoserver/releases/tag/2.23.5)
| [2.23.4](https://github.com/geoserver/geoserver/releases/tag/2.23.4)
| [2.23.3](https://github.com/geoserver/geoserver/releases/tag/2.23.3)
| [2.23.2](https://github.com/geoserver/geoserver/releases/tag/2.23.2)
| [2.23.1](https://github.com/geoserver/geoserver/releases/tag/2.23.1)
| [2.23.0](https://github.com/geoserver/geoserver/releases/tag/2.23.0)
| [2.23-RC1](https://github.com/geoserver/geoserver/releases/tag/2.23-RC1)
) 

