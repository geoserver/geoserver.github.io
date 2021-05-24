---
author: bencaradocdavies
comments: false
date: 2017-12-19 21:01:38+00:00
layout: post
link: http://blog.geoserver.org/2017/12/19/geoserver-2-11-4-released/
slug: geoserver-2-11-4-released
title: GeoServer 2.11.4 Released
wordpress_id: 2923
categories:
- Announcements
tags:
- Release
release: release_211
version: 2.11.4
jira_version: 16707
---

The GeoServer team are pleased to announce the release of [GeoServer 2.11.4](http://geoserver.org/release/2.11.4/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.4/geoserver-2.11.4-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.4/geoserver-2.11.4-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.4/geoserver-2.11.4.dmg/download), and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.11.4/geoserver-2.11.4.exe/download)) along with documentation and extensions.

GeoServer 2.11.4 is a maintenance release of the GeoServer 2.11.x series recommended for production system. This release is made in conjunction with GeoTools 17.4 and GeoWebCache 1.11.3.

This release contains bug fixes as well as new features. For more information, please see the release notes ([2.11.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16707) | [2.11.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16300) |  [2.11.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16001) | [2.11.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15800) | [2.11.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=15501&styleName=Html&projectId=10000) | [2.11-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=15301&projectId=10000) | [2.11-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=14404&projectId=10000&)).


## New Features





 	
  * Support for MongoDB as a source data store for app-schema.

 	
  * Support for GeoJSON output for complex features (app-schema).




## About GeoServer 2.11





 	
  * [OAuth2 for GeoServer](http://www.geo-solutions.it/blog/oauth2-geoserver/) (GeoSolutions).

 	
  * [YSLD](http://docs.geoserver.org/maintain/en/user/styling/ysld/index.html) has graduated and is now available for download as a supported extension.

 	
  * [Vector tiles](http://docs.geoserver.org/maintain/en/user/extensions/vectortiles/index.html) has graduated and is now available for download as an extension.

 	
  * The rendering engine continues to improve with underlying labels now available as a vendor option.

 	
  * A new “[opaque container](http://docs.geoserver.org/maintain/en/user/data/webadmin/layergroups.html#layer-group-modes)” layer group mode can be used to publish a basemap while completely restricting access to the individual layers.

 	
  * Layer group security restrictions are now available.

 	
  * [Latest in performance optimizations in GeoServer](http://www.geo-solutions.it/blog/performance-geoserver/) (GeoSolutions).

 	
  * Improved lookup of EPSG codes allows GeoServer to automatically match EPSG codes making shapefiles easier to import into a database (or publish individually).


