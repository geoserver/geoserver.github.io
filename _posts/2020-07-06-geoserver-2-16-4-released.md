---
author: aaime
comments: false
date: 2020-07-06 10:15:16+00:00
layout: post
link: http://blog.geoserver.org/2020/07/06/geoserver-2-16-4-released/
slug: geoserver-2-16-4-released
title: GeoServer 2.16.4 released
wordpress_id: 3134
categories:
- Announcements
tags:
- Release
release: release_216
version: 2.16.4
jira_version: 16786
---




We are pleased to announce the release of GeoServer [2.16.4](http://geoserver.org/release/2.16.4/) with downloads ([war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.4/geoserver-2.16.4-war.zip/download)|[zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.3/geoserver-2.16.4-bin.zip/download)), [HTML documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.4/geoserver-2.16.4-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.4/extensions/).







This is a stable release recommended for production systems.







### Improvements and Fixes







This release includes a number of improvements, including:







  * The GetFeatureInfo GeoJSON output can now be [controlled with freemarker templates](https://docs.geoserver.org/maintain/en/user/tutorials/GetFeatureInfo/geojson.html#tutorials-getfeatureinfo-geojson).
  * Image mosaic REST API now allows updating the native BBOX of the mosaic during update and delete operations. It's also now possible to store the mosaic index in SQL Server.
  * Documentation on[ how to integrate the app-schema plugin with MongoDB](https://docs.geoserver.org/maintain/en/user/data/app-schema/mongo-tutorial.html) has been improved.
  * The JSON-LD community module has a new option to [filter output contents](https://docs.geoserver.org/maintain/en/user/community/json-ld/configuration.html#filtering-support).
  * The WPS download community module [can reproject the eventual pixel value as well, in case it is an elevation](https://docs.geoserver.org/maintain/en/user/community/wps-download/rawDownload.html#wps-download-vertical-resampling), using a grid shift file.






For more information and the small assorted bug fixes, check the [2.16.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16786) release notes.







## About GeoServer 2.16

Features, presentations and reference material on the 2.16 series:

* State of GeoServer 2.16 ([video](https://media.ccc.de/v/bucharest-169-state-of-geoserver-2019)\|[slides](https://docs.google.com/presentation/d/1eVD8H023fp-mbiP8vNX2GFDXTDnciRUW7MJ57hJpzoY/edit?usp=sharing))
* GeoServer Feature Frenzy 2019 ([video](https://media.ccc.de/v/bucharest-170-geoserver-feature-frenzy)\|[slides](https://docs.google.com/presentation/d/1AfQyNenkpq-bT-EN1ef_y_50CyIKwZKnzleTQUcBu_M/edit?usp=sharing))
* New [SLDService extension](https://docs.geoserver.org/stable/en/user/extensions/sldservice/index.html) using data classification for style generation
* New [authentication key extension](https://docs.geoserver.org/stable/en/user/extensions/authkey/index.html) available
* Server [status page](https://docs.geoserver.org/stable/en/user/configuration/status.html#system-status) now includes system status details
* GDAL 2.x binaries are now used for GDAL [image formats](https://docs.geoserver.org/stable/en/user/data/raster/gdal.html) along with OGR [WFS output](https://docs.geoserver.org/stable/en/user/extensions/ogr.html) and [WPS output](https://docs.geoserver.org/stable/en/user/extensions/ogr.html#ogr-based-wps-output-format) formats
* Release Notes ( [2.16.4](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16786)  \| [2.16.3](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16777)  \| [2.16.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16773) \| [2.16.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16769) \| [2.16.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16765) \| [2.16-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16750) )







