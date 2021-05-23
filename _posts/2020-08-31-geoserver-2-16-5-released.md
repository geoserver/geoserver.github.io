---
author: iant
comments: false
date: 2020-08-31 10:13:57+00:00
layout: post
link: http://blog.geoserver.org/2020/08/31/geoserver-2-16-5-released/
slug: geoserver-2-16-5-released
title: GeoServer 2.16.5 Released
wordpress_id: 3141
categories:
- Announcements
tags:
- Release
release: release_216
version: 2.16.5
jira_version: 16791
---

We are pleased to announce the release of GeoServer [2.16.5](http://geoserver.org/release/2.16.5/) with downloads ([war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.5/geoserver-2.16.5-war.zip/download)\|[zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.5/geoserver-2.16.5-war.zip/download)), [documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.5/geoserver-2.16.5-war.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.5/extensions/).

This release is made in conjunction with GeoTools 22.5. This is the final planned maintenance  release and we highly recommend users to switch to the 2.17 branch for production systems.

Thanks to everyone who contributed, and Ian Turton (Astun Technology) for making this release. 


### Improvements and Fixes

[GEOS-6467] - UI bug in disabling tile caching for layers  
[GEOS-8569] - JSON encoding on NaN values fails  
[GEOS-9266] - Geopackage raster table with dots in the name cannot be added  
[GEOS-9482] - Nearest Match NPE if source database table is empty  
[GEOS-9539] - URLKvpParser encodes urls also when not needed  
[GEOS-9622] - NullPointerException when using WMS vendor parameter "CLIP" on an ImageMosaic based layer  
[GEOS-9629] - Legend Graphic fails on first visit to publish tab on a new layer publish  
[GEOS-9638] - Duplicate SRS in Native SRS List selection on WFS 2.0.0 layer  
[GEOS-9639] - Add OGC URN syntax support for Native SRS selection  
[GEOS-9649] - NullPointerException for geoJSON output format with ComplexFeatures if some feature misses geometry value  
[GEOS-9654] - Layer preview layer count and paging off base when secured layers are not visible  
[GEOS-9655] - WMTS layer configuration page doesn't show all the native srs in getCapabilties document  
[GEOS-9668] - UniqueProcess call against a JDBC store does not result in a "select distinct" anymore  
[GEOS-9678] - SldService numberFormatException if percentages true with customClasses  
[GEOS-9680] - WMTS othersSrs always add EPSG:4326 and shows wrong CRS code  
[GEOS-9682] - GetFeatureInfo on raster layers ignores rendering transformations

## About GeoServer 2.16

Features, presentations and reference material on the 2.16 series:

* State of GeoServer 2.16 ([video](https://media.ccc.de/v/bucharest-169-state-of-geoserver-2019)\|[slides](https://docs.google.com/presentation/d/1eVD8H023fp-mbiP8vNX2GFDXTDnciRUW7MJ57hJpzoY/edit?usp=sharing))
* GeoServer Feature Frenzy 2019 ([video](https://media.ccc.de/v/bucharest-170-geoserver-feature-frenzy)\|[slides](https://docs.google.com/presentation/d/1AfQyNenkpq-bT-EN1ef_y_50CyIKwZKnzleTQUcBu_M/edit?usp=sharing))
* New [SLDService extension](https://docs.geoserver.org/stable/en/user/extensions/sldservice/index.html) using data classification for style generation
* New [authentication key extension](https://docs.geoserver.org/stable/en/user/extensions/authkey/index.html) available
* Server [status page](https://docs.geoserver.org/stable/en/user/configuration/status.html#system-status) now includes system status details
* GDAL 2.x binaries are now used for GDAL [image formats](https://docs.geoserver.org/stable/en/user/data/raster/gdal.html) along with OGR [WFS output](https://docs.geoserver.org/stable/en/user/extensions/ogr.html) and [WPS output](https://docs.geoserver.org/stable/en/user/extensions/ogr.html#ogr-based-wps-output-format) formats
* Release Notes ( [2.16.5](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16791) \| [2.16.4](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16786)  \| [2.16.3](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16777)  \| [2.16.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16773) \| [2.16.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16769) \| [2.16.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16765) \| [2.16-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16750) )








