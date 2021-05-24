---
author: aaime
comments: false
date: 2019-03-22 11:03:16+00:00
layout: post
link: http://blog.geoserver.org/2019/03/22/geoserver-2-14-3-released/
slug: geoserver-2-14-3-released
title: GeoServer 2.14.3 Released
wordpress_id: 3017
categories:
- Announcements
tags:
- Release
release: release_214
version: 2.14.3
jira_version: 16748
---

We are happy to announce the release of [GeoServer 2.14.3](http://geoserver.org/release/2.14.3/). Downloads are provided ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.3/geoserver-2.14.3-bin.zip/download)|[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.3/geoserver-2.14.3-war.zip/download)|[exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.3/geoserver-2.14.3.exe/download)) along with docs ([html](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.3/geoserver-2.14.3-htmldoc.zip/download)|[pdf](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.3/geoserver-2.14.3-user-manual.pdf/download)) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.3/extensions/).

This is a maintenance release of the GeoServer 2.14 series and is recommended for all production systems. Users of prior releases of GeoServer are encouraged to upgrade.

This release is made in conjunction with GeoTools 20.3 and GeoWebCache 1.14.3. Thanks to all who contributed to this release.

For more information please see our release notes ([2.14.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16748) | [2.14.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16744) | [2.14.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16739)|[2.14.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16734)|[2.14-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16718)).


## Improvements and Fixes


This release includes a number of new features and improvements, including:



 	
  * Fix user creation failing on REST API

 	
  * OpenLayers 3 preview did not work on projected data when using version 1.3 of the WMS protocol

 	
  * Fixed style editor HTML issues when going back from full screen editor mode, and fixed moving styles referring to local icons from global to workspace

 	
  * NetCDF extension packaging fix, allows it to run without also having the NetCDF out plugin installed

 	
  * Assorted fixes in WMTS workspace specific capabilities document generation




## About GeoServer 2.14 Series


Additional information on the GeoServer 2.14 series:



 	
  * New [MongoDB extension](https://docs.geoserver.org/latest/en/user/extensions/mongodb/index.html) added

 	
  * Style editor improvements including [side by side editing](https://docs.geoserver.org/latest/en/user/styling/webadmin/index.html#style-editor-full-screen-side-by-side-mode)

 	
  * Nearest match support for [WMS dimension handling](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#edit-layer-dimensions)

 	
  * Upgrade notes documenting [REST API feature type definition change](https://docs.geoserver.org/stable/en/user/installation/upgrade.html#jts-type-bindings-geoserver-2-14-and-newer)

 	
  * [State of GeoServer 2.14](https://www.slideshare.net/jgarnett/state-of-geoserver-214) (SlideShare)

 	
  * [GeoServer Ecosystem](https://www.slideshare.net/jgarnett/geoserver-ecosystem-2018) (SlideShare)

 	
  * [GeoServer Developers Workshop](https://www.slideshare.net/jgarnett/geoserver-developers-workshop) (SlideShare)


