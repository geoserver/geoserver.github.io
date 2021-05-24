---
author: aaime
comments: false
date: 2017-10-23 17:35:07+00:00
layout: post
link: http://blog.geoserver.org/2017/10/23/geoserver-2-11-3-released/
slug: geoserver-2-11-3-released
title: GeoServer 2.11.3 released
wordpress_id: 2918
categories:
- Announcements
tags:
- Release
release: release_211
version: 2.11.3
jira_version: 16300
---

We are happy to announce the release of [GeoServer 2.11.3](http://geoserver.org/release/2.11.3/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.3/geoserver-2.11.3-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.3/geoserver-2.11.3-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.3/geoserver-2.11.3.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.11.3/geoserver-2.11.3.exe/download)) along with documentation and extensions.

GeoServer 2.11.3 is the first maintenance release of the GeoServer 2.11.x series recommended for production system. This release is made in conjunction with GeoTools 17.3.

Highlights of this release are featured below, for more information please see the release notes ([2.11.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16300) |  [2.11.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16001) | [2.11.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15800) | [2.11.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=15501&styleName=Html&projectId=10000) | [2.11-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=15301&projectId=10000) | [2.11-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=14404&projectId=10000&) ).


## New Features and Improvements





 	
  * KML has two new options to control polygon placemark placement, to force it within the current view, and to make sure it's inside polygons regardless of the polygon shape

 	
  * The layer preview allows filtering on raster layers such as mosaics and image pyramids (which can apply the filter on the underlying mosaic index)




## Bug Fixes





 	
  * Improvements on pre-build legend treatment in GetLegendGraphic, now works against a layer default style too, and for workspace specific styles

 	
  * GDAL bindings jars restored in the build, making it easier to use the pre-built native support (as opposed to custom built ones, for those remember to remove them)

 	
  * Raster rendering fixes: no more empty output when asking for highly oversampled rasters in WMS, make sure new image mosaic tiles are rendered even if outside the original bounds in image mosaic

 	
  * GWC related improvemenets, seed links now working when running behind a proxy, and more strict checks for non cacheable requests over the WMS service endpoint (especially useful when using direct integration)

 	
  * GeoServer now changes the SLD version number when uploading a SLD 1.1 overwriting a SLD 1.0 file using the REST API (especially useful for QGIS and GeoNode integrations). The UI was not affected by this issue.

 	
  * And several more, check the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16300) for full details




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


