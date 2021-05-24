---
author: aaime
comments: false
date: 2018-10-18 17:31:56+00:00
layout: post
link: http://blog.geoserver.org/2018/10/18/geoserver-2-13-3-released/
slug: geoserver-2-13-3-released
title: GeoServer 2.13.3 released
wordpress_id: 2979
categories:
- Announcements
tags:
- Release
release: release_213
version: 2.13.3
jira_version: 16733
---



We are happy to announce the release of [GeoServer 2.13.3](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.3/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.3/geoserver-2.13.3-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.3/geoserver-2.13.3-war.zip/download), and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.3/geoserver-2.13.3.exe/download)) along with docs and extensions.

This is a maintenance release recommended for production use (for newer projects please use the 2.14.x series, as 2.13.x will cease to be supported in a few months).
This release is made in conjunction with GeoTools 19.3 and GeoWebCache 1.13.3.




Highlights of this release are featured below, for more information please see the release notes ([2.13.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16733) | [2.13.2 ](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16728)| [2.13.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16724) | [2.13.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16722) | [2.13-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16717) | [2.13-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16702)).


### Improvements and Fixes





 	
  * Allow selection of geometry attribute in app-schema, support mapping files over HTTP connection, push spatial filters over nested geometries down into SQL when possible

 	
  * Performance improvement when reporting dimension values in WMS capabilities, for dimensions out of raster data and presented as "interval and resolution"

 	
  * WCS thread safety fixes when using requests with reprojection and rescaling under high load. Also, when requesting an area inside the bounds of a sparse mosaic, the result might have had less pixels than requested.

 	
  * CSS translator fixed to support mark offset/anchors based on expressions

 	
  * File chooser autocomplete had duplicate entries on Linux

 	
  * REST config, it was not possible to set the default style using a layer PUT

 	
  * GetLegendGraphic ignores the OnlineResource configured in the style for raster layers




## About GeoServer 2.13 Series


Additional information on the 2.13 series:



 	
  * [Isolated workspaces](http://docs.geoserver.org/latest/en/user/data/webadmin/workspaces.html#isolated-workspaces) (User Guide)

 	
  * [Coverage views from heterogeneous bands](http://docs.geoserver.org/latest/en/user/data/raster/coverageview.html#heterogeneous-coverage-views) (User Guide)

 	
  * [State of GeoServer 2.13](https://www.slideshare.net/jgarnett/state-of-geoserver-213) (slideshare)

 	
  * See the [GeoServer 2.13.0 released](http://blog.geoserver.org/2018/03/20/geoserver-2-13-0-released/) announcement for visual guide to new features



