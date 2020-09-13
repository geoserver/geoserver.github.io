---
author: aaime
comments: false
date: 2017-07-31 17:56:31+00:00
layout: post
link: http://blog.geoserver.org/2017/07/31/geoserver-2-11-2-released/
slug: geoserver-2-11-2-released
title: GeoServer 2.11.2 released
wordpress_id: 2884
---

We are happy to announce the release of [GeoServer 2.11.2](http://geoserver.org/release/2.11.2/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.2/geoserver-2.11.2-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.2/geoserver-2.11.2-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.2/geoserver-2.11.2.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.11.2/geoserver-2.11.2.exe/download)) along with documentation and extensions.

GeoServer 2.11.1 is the latest stable release of GeoSever recommended for production system. This release is made in conjunction with GeoTools 17.1.

Highlights of this release are featured below, for more information please see the release notes ([2.11.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16001) | [2.11.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15800) | [2.11.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=15501&styleName=Html&projectId=10000) | [2.11-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=15301&projectId=10000) | [2.11-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=14404&projectId=10000&) ).


## New Features and Improvements





 	
  * There is a new GetLegendGraphic option that will [return feature counts](http://docs.geoserver.org/stable/en/user/services/wms/get_legend_graphic/index.html#content-dependent) in the legend label, counting them in the current bounding box

 	
  * Geometries in GetFeatureInfo GML output are now reprojected following the base GetMap output projection

 	
  * The LayerGroup edit page allows configuring keywords and identifiers (as already available for normal layers)

 	
  * 



## Bug Fixes





 	
  * Various raster improvements, including better handling of heterogeneous CRS mosaics, lower pixelation at high latitudes in EPSG:3857,

 	
  * GetLegendGraphic against multiple layers did not work if any layer was out of scale range, fixed

 	
  * GetFeatureInfo now works against a mix of queriable and non queriable layers

 	
  * Cascading WMS now supports very long credentials

 	
  * Several fixes and tweaks in the configuration UI for an improved experience

 	
  * And several more, check the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16001) for full details




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


