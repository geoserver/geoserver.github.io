---
author: jgarnett
comments: true
date: 2017-03-14 07:23:39+00:00
layout: post
link: http://blog.geoserver.org/2017/03/14/geoserver-2-11-rc1-released/
slug: geoserver-2-11-rc1-released
title: GeoServer 2.11-RC1 Released
wordpress_id: 2817
categories:
- Announcements
tags:
- release
- Release Candidate
---

We are happy to announce the release of [GeoServer 2.11-RC1](http://geoserver.org/release/2.11-RC1/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11-RC1/geoserver-2.11-RC1-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11-RC1/geoserver-2.11-RC1-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-RC1/geoserver-2.11-RC1.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11-RC1/geoserver-2.11-RC1.exe/download)) along with docs and extensions.

This is a release candidate of GeoServer not intended for production use. This release is made in conjunction with GeoTools 16-RC1 and GeoWebCache 1.11-RC1.

Thanks to everyone who provided feedback, bug reports and fixes. Here are some of the changes included in 2.11-RC1:



 	
  * Incompatibilities with GeoFence and Control-flow have been resolved

 	
  * Empty WFS Transactions (which perform no changes) no indicating everything has changed

 	
  * Improvements to WFS GetFeature support for 3D BBOX requests

 	
  * We have one known regression with the windows service installer (memory setting is incorrect)

 	
  * Please additional details see the release notes ([2.11-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=15301&projectId=10000) | [2.11-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=14404&projectId=10000&) )




## Release Candidate Testing


The 2.11 release is expected in March, this release candidate is a "dry run" where we confirm new functionality is working as expected and double check the packaging and release process.

Please note that GeoServer 2.9 has reached its end-0f-life. If your organization has not yet upgraded please give us hand by evaluating 2.11-RC1 and providing feedback and your experiences for the development team. This is a win/win situation where your participation can both assist the GeoServer team and reduce your risk when upgrading.


### Corrected default AnchorPoint for LabelPlacement


An [issue with SLD 1.0 rendering](https://osgeo-org.atlassian.net/browse/GEOT-5632) has been fixed - when a LabelPlacement did not include a AnchorPoint we were using the wrong default!



 	
  * BEFORE: default anchor point was X=0.5 and Y=0.5 - which is at the middle height and middle length of the label text.

 	
  * AFTER: default anchor point was X=0.0 and Y=0.5 - which is at the middle height of the lefthand
side of the label text.


This is a long standing issue that was only just noticed in February. If you need to "restore" the incorrect behaviour please startup with -D_org.geotools.renderer.style.legacyAnchorPoint=true _system property.


### Startup Performance


With [extensive improvement](https://github.com/geoserver/geoserver/wiki/GSIP%20155)s to startup performance and OGC requests for large installations we are looking forward to feedback from your experience testing.


## About GeoServer 2.11


GeoServer 2.11 is scheduled for March 2017 release. This puts GeoServer back on our six month "time boxed" release schedule.



 	
  * [OAuth2 for GeoServer](http://www.geo-solutions.it/blog/oauth2-geoserver/) (GeoSolutions)

 	
  * [YSLD](http://docs.geoserver.org/stable/en/user/styling/ysld/index.html) has graduated and is now available for download as a supported extension

 	
  * [Vector tiles](http://docs.geoserver.org/latest/en/user/extensions/vectortiles/index.html) has graduate and is now available for download as an extension

 	
  * The rendering engine continues to improve with underlying labels now available as a vendor option

 	
  * A new "[opaque container](http://docs.geoserver.org/latest/en/user/data/webadmin/layergroups.html#layer-group-modes)" layer group mode can be used to publish a basemap while completely restricting access to the individual layers.

 	
  * Layer group security restrictions are now available

 	
  * [Latest in performance optimizations in GeoServer](http://www.geo-solutions.it/blog/performance-geoserver/) (GeoSolutions)

 	
  * Improved lookup of EPSG codes allows GeoServer to automatically match EPSG codes making shapefiles easier to import into a database (or publish individually).


