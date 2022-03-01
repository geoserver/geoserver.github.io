---
author: tbarsballe
comments: false
date: 2017-05-19 17:26:43+00:00
layout: post
link: http://blog.geoserver.org/2017/05/19/geoserver-2-11-1-released/
slug: geoserver-2-11-1-released
title: GeoServer 2.11.1 Released
wordpress_id: 2867
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_211
version: 2.11.1
jira_version: 15800
---

We are happy to announce the release of [GeoServer 2.11.1](http://geoserver.org/release/2.11.1/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.1/geoserver-2.11.1-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.1/geoserver-2.11.1-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.1/geoserver-2.11.1.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.11.1/geoserver-2.11.1.exe/download)) along with documentation and extensions.

GeoServer 2.11.1 is the latest stable release of GeoSever recommended for production system. This release is made in conjunction with GeoTools 17.1.

Highlights of this release are featured below, for more information please see the release notes ([2.11.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15800) | [2.11.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=15501&styleName=Html&projectId=10000) | [2.11-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=15301&projectId=10000) | [2.11-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=14404&projectId=10000&) ).


## Security Considerations


This release addresses three security vulnerabilities:



 	
  * Added a [configurable delay](http://docs.geoserver.org/latest/en/user/security/webadmin/auth.html#brute-force-attack-prevention) during login, to mitigate a brute force attack.

 	
  * Added a [configurable parameter](http://docs.geoserver.org/latest/en/user/production/config.html#x-frame-options-policy) to control clickjacking attacks against the GeoServer UI.

 	
  * Added an additional parameter for locking down password autocomplete in the GeoServer UI


Thanks to Andrea Aime and Devon Tucker for providing fixes to these issues.

These fixes are also included in the 2.10.3 release.

If you wish to report a security vulnerability, please visit our website for [instructions on responsible reporting](http://geoserver.org/issues/).


## New Features and Improvements





 	
  * There is a new Mapbox Style community module available, which adds support for an interoperable json styling language. For more details, refer to the [documentation](http://docs.geoserver.org/latest/en/user/styling/mbstyle/index.html).

 	
  * GSIP 158 - NetCDF output support for variable attributes and extra variables. This improvement adds the ability to set attributes on output NetCDF variables, copy attributes from source NetCDF/GRIB variables, and copy scalar variables from NetCDF/GRIB sources including ImageMosaics. See [the documentation](http://docs.geoserver.org/stable/en/user/extensions/netcdf-out/index.html) for details.

 	
  * Allow disabling usage of SLD and SLD_BODY in WMS requests (also for virtual services).




## Bug Fixes





 	
  * Various improvements to virtual services, including lookup and GML 3 encoding handling

 	
  * Namespace filtering on capabilities returns all layer groups (including the ones in other workspaces)

 	
  * Not possible to PUT workspace using REST

 	
  * GeoServer Home Page missing information messages

 	
  * Style Editor Preview Legend Fails on non-SLD Styles

 	
  * Integrated GWC does not work with layer and layer group specific services

 	
  * Generating a raster SLD style from template produces a functionally invalid style

 	
  * GeoServer generates invalid GeoPackage raster mosaics

 	
  * Metatiling may throw a ClassCastException: Raster cannot be cast to WritableRaster




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


