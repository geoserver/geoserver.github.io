---
author: Gabriel Roldan, Jody Garnett
comments: false
date: 2021-02-22
layout: post
title: GeoServer 2.17.5 Released
categories:
- Announcements
tags:
- Release
release: release_217
version: 2.17.5
jira_version: 16806
---


We are pleased to announce the release of GeoServer [2.17.5](http://geoserver.org/release/2.17.5/) with downloads (
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.5/geoserver-2.17.5-war.zip/download) |
[bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.5/geoserver-2.17.5-bin.zip/download) ), [documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.5/geoserver-2.17.5-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.5/extensions/) .

This release is made in conjunction with GeoTools 23.5. This is a maintenance release recommended for production systems.

The GeoServer 2.17.x has reached end-of-life and this is the last scheduled release fo the 2.17.x branch. Production systems are advised to use 2.17.5 release as a temporary measure, and schedule your upgrade to 2.18.

Thanks to everyone who contributed, and Gabriel Roldan & Jody Garnett (GeoCat) for making this release.

### Improvements and Fixes

Fixes included in this release:

* [GEOS-9879](https://osgeo-org.atlassian.net/browse/GEOS-9879) - app-schema extension fix for feature collection count
+ [GEOS-9897](https://osgeo-org.atlassian.net/browse/GEOS-9897) - JTS upgrade breaks geofence integration
+ [GEOS-9880](https://osgeo-org.atlassian.net/browse/GEOS-9880) - Monitor failure when maxSize is set to unbound 
+ [GEOS-9881](https://osgeo-org.atlassian.net/browse/GEOS-9881) - SldService failure when percentages and continuous parameters both set to true
* [GEOS-9895](https://osgeo-org.atlassian.net/browse/GEOS-9895) - Override transformation operations ignored for bounding box computation
* [GEOS-9911](https://osgeo-org.atlassian.net/browse/GEOS-9911) - Params-extractor plugin, wrong url in getCapabilities when having context with addition "/"

For more information check the [2.17.5](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16806) release notes.

## About GeoServer 2.17

Features, presentations and reference material on the 2.17 series:

  * New security tab on each [layer](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#edit-layer-security), [layer group](https://docs.geoserver.org/latest/en/user/data/webadmin/layergroups.html#edit-a-layer-group) and [workspace](https://docs.geoserver.org/latest/en/user/data/webadmin/workspaces.html#edit-a-workspace) page
  * Option to use [date created and date modified](https://github.com/geoserver/geoserver/wiki/GSIP-179) to sort UI lists
  * New [resource browser extension](https://docs.geoserver.org/latest/en/user/configuration/tools/resource/index.html)
  * New [Mapbox style extension](https://docs.geoserver.org/latest/en/user/styling/mbstyle/index.html)
  * FOSDEM GeoServer Orientation presentation ([slides](https://www.slideshare.net/jgarnett/geoserver-orientation)|[video](https://ftp.fau.de/fosdem/2020/AW1.126/geoserver.mp4))
  * [Full OSM data directory](https://www.geosolutionsgroup.com/blog/geoserver-osm-styles-full-data-directory-available/) for GeoServer available on GitHub
  * [Code of Conduct](https://github.com/geoserver/geoserver/blob/master/CODE_OF_CONDUCT.md)
  * Release Notes ([2.17.5](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16806)
  [2.17.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16801)|
  [2.17.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16789)|
  [2.17.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16785)|
  [2.17.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16782)|
  [2.17-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16766))








