---
author: aaime
comments: false
date: 2018-02-20 17:02:02+00:00
layout: post
link: http://blog.geoserver.org/2018/02/20/geoserver-2-11-5-released/
slug: geoserver-2-11-5-released
title: GeoServer 2.11.5 released
wordpress_id: 2928
categories:
- Announcements
tags:
- Release
release: release_211_no_osx
version: 2.11.5
jira_version: 16712
---

We are happy to announce the release of [GeoServer 2.11.5](http://geoserver.org/release/2.11.5/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.5/geoserver-2.11.5-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.5/geoserver-2.11.5-war.zip/download), and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.11.5/geoserver-2.11.5.exe/download)) along with documentation and extensions (OSX installer is currently missing as we're unable to generate a signed installed version due to security/infrastructure issues being discussed on geoserver-devel).

GeoServer 2.11.5 is the last maintenance release of the GeoServer 2.11.x series, so we recommend users to plan an upgrade to 2.12.x or to the upcoming 2.13.x series. This release is made in conjunction with GeoTools 17.5.

Highlights of this release are featured below, for more information please see the release notes ([2.11.5](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16712) | [2.11.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16707) | [2.11.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16300) |  [2.11.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16001) | [2.11.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15800) | [2.11.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=15501&styleName=Html&projectId=10000) | [2.11-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=15301&projectId=10000) | [2.11-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=14404&projectId=10000&) ).


## Bug Fixes





 	
  * Fixed GetFeatureInfo on rasters setup with "reproject to declared" SRS policy

 	
  * Assorted fixes on demo request page (password was not being sent

 	
  * Allow importer to handle multi-coverage files on import (NetCDF)

 	
  * GetLegendGraphic fixes for cut symbols on rescale (happened with large symbols and odd sized legends)

 	
  * WMS fixes on rendering rasters whose native CRS is a polar stereographic

 	
  * And several more, check the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16712) for full details




## About GeoServer 2.11


Articles, docs, blog posts and presentations:



 	
  * [OAuth2 for GeoServer](http://www.geo-solutions.it/blog/oauth2-geoserver/) (GeoSolutions)

 	
  * [YSLD](http://docs.geoserver.org/stable/en/user/styling/ysld/index.html) has graduated and is now available for download as a supported extension

 	
  * [Vector tiles](http://docs.geoserver.org/latest/en/user/extensions/vectortiles/index.html) has graduate and is now available for download as an extension

 	
  * The rendering engine continues to improve with underlying labels now available as a vendor option

 	
  * A new “[opaque container](http://docs.geoserver.org/latest/en/user/data/webadmin/layergroups.html#layer-group-modes)” layer group mode can be used to publish a basemap while completely restricting access to the individual layers.

 	
  * Layer group security restrictions are now available

 	
  * [Latest in performance optimizations in GeoServer](http://www.geo-solutions.it/blog/performance-geoserver/) (GeoSolutions)

 	
  * Improved lookup of EPSG codes allows GeoServer to automatically match EPSG codes making shapefiles easier to import into a database (or publish individually).


