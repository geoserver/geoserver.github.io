---
author: Ian Turton
comments: false
date: 2020-12-22
layout: post
title: GeoServer 2.17.4 Released
categories:
- Announcements
tags:
- Release
---


We are pleased to announce the release of GeoServer [2.17.4](http://geoserver.org/release/2.17.4/) with downloads (
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.4/geoserver-2.17.4-war.zip/download) |
[bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.4/geoserver-2.17.4-bin.zip/download) ),
[documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.4/geoserver-2.17.4-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.4/extensions/).

This release is made in conjunction with GeoTools 23.4 and GeoWebCache 1.17.4. This is a maintenance release recommended for production systems. You are reminded that this is most likely to be the last release made on the 2.17 branch and you should consider moving to the stable 2.18 branch as soon as possible.


Thanks to everyone who contributed, and Ian Turton (Astun Technology) & Jody Garnett (GeoCat) for making this release.



### Improvements and Fixes

This release includes a number of improvements. Notable improvements:

+ [GEOS-9753] - Features-templating plug-in allows `env` parametrization on `vendorOptions`
+ [GEOS-9765] - Add IP Address range to GeoFence UI
+ [GEOS-9780] - status page shows (read-only) loopback partitions

Fixes included in this release:

+ [GEOS-9689] - WFS-NG Other SRS in URN OGC format are not matched by WMS Request SRS
+ [GEOS-9750] - WPS processes fail with missing CSV dependencies
+ [GEOS-9754] - Not consistent array element enumeration in flat GeoJson output format
+ [GEOS-9758] - CRS Panel overrides URN SRS format with EPSG:XXXX format
+ [GEOS-9791] - GeoJSON bounding box axis order wrongly encoded when CRS axis order is NORTH-EAST
+ [GEOS-9816] - Download links from the result of an asynchronous process will not honor the proxy base URL, if it uses HTTP header variables


For more information check the [2.17.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16801) release notes.


## About GeoServer 2.17


Features, presentations and reference material on the 2.17 series:


  * New security tab on each [layer](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#edit-layer-security), [layer group](https://docs.geoserver.org/latest/en/user/data/webadmin/layergroups.html#edit-a-layer-group) and [workspace](https://docs.geoserver.org/latest/en/user/data/webadmin/workspaces.html#edit-a-workspace) page
  * Option to use [date created and date modified](https://github.com/geoserver/geoserver/wiki/GSIP-179) to sort UI lists
  * New [resource browser extension](https://docs.geoserver.org/latest/en/user/configuration/tools/resource/index.html)
  * New [Mapbox style extension](https://docs.geoserver.org/latest/en/user/styling/mbstyle/index.html)
  * FOSDEM GeoServer Orientation presentation ([slides](https://www.slideshare.net/jgarnett/geoserver-orientation)|[video](https://ftp.fau.de/fosdem/2020/AW1.126/geoserver.mp4))
  * [Full OSM data directory](https://www.geosolutionsgroup.com/blog/geoserver-osm-styles-full-data-directory-available/) for GeoServer available on GitHub
  * [Code of Conduct](https://github.com/geoserver/geoserver/blob/master/CODE_OF_CONDUCT.md)
  * Release Notes ([2.17.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16801)|
  [2.17.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16789)|
  [2.17.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16785)|
  [2.17.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16782)|
  [2.17-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16766))








