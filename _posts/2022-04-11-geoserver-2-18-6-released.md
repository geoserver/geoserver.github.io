---
author: Andrea Aime
date: 2022-04-11
layout: post
title: GeoServer 2.18.6 Released
categories:
- Announcements
tags:
- Release
release: release_218
version: 2.18.6
jira_version: 16846
---

GeoServer [2.18.6](/release/2.18.6/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.6/geoserver-2.18.6-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.6/geoserver-2.18.6-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.6/GeoServer-2.18.6-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.6/geoserver-2.18.6-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.6/extensions/).

This is an extra maintenance release of the 2.18.x series recommended for production systems that have not yet upgraded to 2.19. This release was made in conjunction with GeoTools 24.6.

Thanks to everyone who contributed, and to Andrea Aime (GeoSolutions) and Jody Garnett (GeoCat) for making this release.

### Security Considerations

This release includes security enhancements and is a recommended upgrade for production systems.

This release includes two improvements addressing [Jiffle and GeoTools RCE vulnerabilities]({% post_url 2022-04-11-geoserver-2-jiffle-jndi-rce %}):

* [GEOS-10458](https://osgeo-org.atlassian.net/browse/GEOS-10458) Upgrade to JAI-EXT 1.1.22

* [GEOT-7115](https://osgeo-org.atlassian.net/browse/GEOT-7115) Streamline JNDI lookups
  
This release also includes:

* [GEOS-10445](https://osgeo-org.atlassian.net/browse/GEOS-10445) Upgrade Spring Framework from 5.1.20.RELEASE to 5.2.20.RELEASE
  
  Although GeoServer [assessment]({% post_url 2022-04-01-spring %}) did not identify any issue we have now updated the the spring framework library.

### Improvements and Fixes

* [GEOS-10437](https://osgeo-org.atlassian.net/browse/GEOS-10437) Breaking SLD 1.1 style by REST upload

* [GEOS-10249](https://osgeo-org.atlassian.net/browse/GEOS-10249) GWC produce NPE when it comes to race condition

* [GEOS-10215](https://osgeo-org.atlassian.net/browse/GEOS-10215) Layers nested inside a group maintain their prefix even in workspace specific services

* [GEOS-10213](https://osgeo-org.atlassian.net/browse/GEOS-10213) WMS requests fail on LayerGroup default style names, when used in GetMap/GetFeatureInfo/GetLegendGraphics

* [GEOS-10200](https://osgeo-org.atlassian.net/browse/GEOS-10200) GetLegendGraphic can fail if SCALE removes all rules

* [GEOS-10321](https://osgeo-org.atlassian.net/browse/GEOS-10321) WCS 2.0 might fail to return coverages whose native BBOX goes slighly outside of the dateline

* [GEOS-10194](https://osgeo-org.atlassian.net/browse/GEOS-10194) Improve importer LOGGING

* [GEOS-10335](https://osgeo-org.atlassian.net/browse/GEOS-10335) Update GeoServer to a log4j version that does not support RCEs

For more information see [2.18.6 release notes](https://github.com/geoserver/geoserver/releases/tag/2.18.6).

## About GeoServer 2.18

Additional information on GeoServer 2.18 series:

* [Jiffle and GeoTools RCE vulnerabilities]({% post_url 2022-04-11-geoserver-2-jiffle-jndi-rce %})
* [Log4J2 zero day vulnerability assessment]({% post_url 2021-12-13-logj4-rce-statement %})  
* State of GeoServer 2.18 ([slides](https://docs.google.com/presentation/d/1Q0pHRUcvucAuHDeZPoeDJG4UY5izwbqo8ZawUdk9xYM/edit?usp=sharing))
* GeoServer Orientation ([slides](https://t.co/fvBTLMia6f?amp=1)|[video](https://youtu.be/bdkk5eVR674))

Release Notes ( [2.18.6](https://github.com/geoserver/geoserver/releases/tag/2.18.6)
\| [2.18.5](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16822)
\| [2.18.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16819)
\| [2.18.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16808)
\| [2.18.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16803)
\| [2.18.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16800)
\| [2.18.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16796)
\| [2.18-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16783) )
