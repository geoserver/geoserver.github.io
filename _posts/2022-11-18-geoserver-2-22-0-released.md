---
author: Martha Nagginda
date: 2022-11-18
layout: post
title: GeoServer 2.22.0 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_222
version: 2.22.0
jira_version: 16867
---

GeoServer [2.22.0](/release/2.22.0/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.0/geoserver-2.22.0-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.0/geoserver-2.22.0-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.0/GeoServer-2.22.0-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.0/geoserver-2.22.0-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.0/extensions/).

This is a stable release of the GeoServer 2.22.x series, made in conjunction with GeoTools 28.0 
and GeoWebCache 1.22.0.

All major new features have been described in the [Release Candidate (RC) Blog post](https://geoserver.org/announcements/2022/10/19/geoserver-2-22-RC-released.html).

Thanks to Martha Nagginda (GeoSolutions) and Andrea Aime (GeoSolutions) for making this release.

### Improvements and Fixes


## Improvement

[GEOS-10717](https://osgeo-org.atlassian.net/browse/GEOS-10717) XStreamServiceLoader performance improvement with XstreamPersister caching

[GEOS-10718](https://osgeo-org.atlassian.net/browse/GEOS-10718) \[OIDC\] the OIDC plugin does not currently take into account the id\_token\_hint parameter

[GEOS-10735](https://osgeo-org.atlassian.net/browse/GEOS-10735) Obfuscate secret key in S3 Blob Store, avoiding requiring reentry when editing and HTML source visibility

[GEOS-10739](https://osgeo-org.atlassian.net/browse/GEOS-10739) Contact information user interface feedback for welcome message

[GEOS-10740](https://osgeo-org.atlassian.net/browse/GEOS-10740) Service enabled does not respect minimal/custom service names

[GEOS-10750](https://osgeo-org.atlassian.net/browse/GEOS-10750) German Translation Overhaul Part 1

## New Feature

[GEOS-10734](https://osgeo-org.atlassian.net/browse/GEOS-10734) SpatialJSON WFS output format community module

## Task

[GEOS-10721](https://osgeo-org.atlassian.net/browse/GEOS-10721) Bump jettison from 1.4.1 to 1.5.1

## Bug

[GEOS-4727](https://osgeo-org.atlassian.net/browse/GEOS-4727) Editing SQL views seems to be leaking connections

[GEOS-10667](https://osgeo-org.atlassian.net/browse/GEOS-10667) WFS: inconsistent srsDimension=4 with topp:tasmania\_roads layer

[GEOS-10707](https://osgeo-org.atlassian.net/browse/GEOS-10707) GeoFence internal LayerGroup Limit merge inconsistency

[GEOS-10709](https://osgeo-org.atlassian.net/browse/GEOS-10709) Schemaless Features - Simplified property access might return values for wrong property names

[GEOS-10710](https://osgeo-org.atlassian.net/browse/GEOS-10710) Features Templating backward mapping with back xpath \('../my/property/name'\) doesn't work

[GEOS-10714](https://osgeo-org.atlassian.net/browse/GEOS-10714) DefaultGeoServerFacade throws ConcurrentModificationException for workspace settings and services

[GEOS-10729](https://osgeo-org.atlassian.net/browse/GEOS-10729) Concurrent access on data access rules \(authorization\) can lead to loss of configured catalog mode, and lost rules

[GEOS-10731](https://osgeo-org.atlassian.net/browse/GEOS-10731) GWC variable Parameterization does not work with geoserver-environment.properties due to the bean initialization order

[GEOS-10736](https://osgeo-org.atlassian.net/browse/GEOS-10736) OSEO product creation via REST API fails if the product id starts with a valid ISO date

[GEOS-10737](https://osgeo-org.atlassian.net/browse/GEOS-10737) GeoCSS misses support for labelInFeatureInfo and labelAttributeName vendor options

[GEOS-10741](https://osgeo-org.atlassian.net/browse/GEOS-10741) Remove deprecated YUI usage

For complete information see [2.22.0 release notes](https://github.com/geoserver/geoserver/releases/tag/2.22.0).

## About GeoServer 2.22

Additional information on GeoServer 2.22 series:

* [Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/metadata/index.html)
* [CSW ISO Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/csw-iso/index.html)
* [State of GeoServer](https://docs.google.com/presentation/d/1mnOFSvYb8npVudvUR5MSjSTFHc6ZQ_bStafZrBV7LZ8/edit?usp=sharing) (FOSS4G Presentation)
* [GeoServer Beginner Workshop](https://docs.google.com/presentation/d/1fbPLN-1Cs95WK-IxDG1PxCEKyHwFbNBGNkkomxmLr0Y/edit?usp=sharing) (FOSS4G Workshop)
* [Welcome page](https://docs.geoserver.org/latest/en/user/webadmin/welcome.html) (User Guide)

Release notes:
( 
  [2.22.0](https://github.com/geoserver/geoserver/releases/tag/2.22.0) |
  [2.22-RC](https://github.com/geoserver/geoserver/releases/tag/2.22-RC)
| [2.22-M0](https://github.com/geoserver/geoserver/releases/tag/2.22-M0)
)
