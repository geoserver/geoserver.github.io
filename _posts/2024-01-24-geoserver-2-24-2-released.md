---
author: Jody Garnett
date: 2024-01-24
layout: post
title: GeoServer 2.24.2 Release
categories:
- Announcements
tags:
- Release
- Vulnerability
release: release_224
version: 2.24.2
jira_version: 16908
--- 

GeoServer [2.24.2](/release/2.24.2/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.2/geoserver-2.24.2-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.2/geoserver-2.24.2-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.2/GeoServer-2.24.2-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.2/geoserver-2.24.2-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.2/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 2.24.2 is made in conjunction with GeoTools 30.2, and GeoWebCache 1.24.2.

Thanks to Jody Garnett (GeoCat) for making this release, everyone who contributed, and to Georg Weickelt and Peter Smythe for preflight testing.

## Security Considerations

This release addresses security vulnerabilities and is considered an essential upgrade for production systems.

- [CVE-2024-23634](https://github.com/geoserver/geoserver/security/advisories/GHSA-75m5-hh4r-q9gx) Arbitrary file renaming vulnerability in REST Coverage/Data Store API (Moderate).

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.


## Release notes

Improvement:

* [GEOS-11213](https://osgeo-org.atlassian.net/browse/GEOS-11213) Improve REST external upload method unzipping
* [GEOS-11246](https://osgeo-org.atlassian.net/browse/GEOS-11246) Schemaless plugin performance for WFS
* [GEOS-11219](/browse/GEOS-11219) Upgraded mail and activation libraries for SMTP compatibility

Bug:

* [GEOS-9757](https://osgeo-org.atlassian.net/browse/GEOS-9757) Return a service exception when client provided WMS dimensions are not a match
* [GEOS-11051](https://osgeo-org.atlassian.net/browse/GEOS-11051) Env parametrization does not save correctly in AuthKey extension
* [GEOS-11223](https://osgeo-org.atlassian.net/browse/GEOS-11223) Layer not visible in preview/capabilities if security closes the workspace, but allows access to the layer
* [GEOS-11224](https://osgeo-org.atlassian.net/browse/GEOS-11224) Platform independent binary doesn't start properly with default data directory
* [GEOS-11235](https://osgeo-org.atlassian.net/browse/GEOS-11235) preauthentication filters - session reuse even after having logout
* [GEOS-11241](https://osgeo-org.atlassian.net/browse/GEOS-11241) ModificationProxy breaks information hidding on CatalogInfo.accept(CatalogVisitor) exposing the proxied object
* [GEOS-11250](https://osgeo-org.atlassian.net/browse/GEOS-11250) WFS GeoJSON encoder fails with an exception if an infinity number is used in the geometry
* [GEOS-11255](https://osgeo-org.atlassian.net/browse/GEOS-11255) Multiple inserts in WPS with different idGen strategies does not work

Task:

* [GEOS-11220](https://osgeo-org.atlassian.net/browse/GEOS-11220) Upgrade Hazelcast from 5.3.1 to 5.3.6
* [GEOS-11245](https://osgeo-org.atlassian.net/browse/GEOS-11245) Update OSHI from 6.2.2 to 6.4.10

For the complete list see [2.24.2](https://github.com/geoserver/geoserver/releases/tag/2.24.2) release notes. 

## Community Updates

Community module development:

* [GEOS-10933](/browse/GEOS-10933) keycloak logout NPE

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.24 Series

Additional information on GeoServer 2.24 series:

* [GeoServer 2.24 User Manual](https://docs.geoserver.org/2.24.x/en/user/)
* [Control remote HTTP requests sent by GeoTools/GeoServer](https://github.com/geoserver/geoserver/wiki/GSIP-218)
* [State of GeoServer 2.24.1](https://docs.google.com/presentation/d/1X7iU1fd47frfh1EsN_CdUll0qtMMgPXkkMjaTbejj3g/edit?usp=sharing) (foss4g-asia presentation)
* [Multiple CRS authority support, planetary CRS](https://github.com/geoserver/geoserver/wiki/GSIP-219)
* [Extensive GeoServer Printing improvements](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html)
* [Upgraded security policy](https://github.com/geoserver/geoserver/wiki/GSIP-220)

Release notes:
( [2.24.2](https://github.com/geoserver/geoserver/releases/tag/2.24.2)
| [2.24.1](https://github.com/geoserver/geoserver/releases/tag/2.24.1)
| [2.24.0](https://github.com/geoserver/geoserver/releases/tag/2.24.0)
| [2.24-RC](https://github.com/geoserver/geoserver/releases/tag/2.24-RC)
) 

