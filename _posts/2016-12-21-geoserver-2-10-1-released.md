---
author: tbarsballe
comments: true
date: 2016-12-21 06:35:37+00:00
layout: post
link: http://blog.geoserver.org/2016/12/21/geoserver-2-10-1-released/
slug: geoserver-2-10-1-released
title: GeoServer 2.10.1 Released
wordpress_id: 2777
categories:
- Announcements
tags:
- Release
release: release_210
version: 2.10.1
jira_version: 14500
---

The GeoServer team is pleased to announce the release of [GeoServer 2.10.1](http://geoserver.org/release/2.10.1/). Download bundles are provided ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.10.1/geoserver-2.10.1-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.10.1/geoserver-2.10.1-war.zip/download), [dmg](https://sourceforge.net/projects/geoserver/files/GeoServer/2.10.1/geoserver-2.10.1.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.10.1/geoserver-2.10.1.exe/download)) along with documentation and extensions.

GeoServer 2.10.1 is the latest stable release of GeoServer and is recommended for production deployment. This release is made in conjunction with GeoTools 16.1 and GeoWebCache 1.10.1. Thanks to all contributors.

New Features and Improvements:



 	
  * Allow windows installer to use port 80

 	
  * Allow underlined labels in SLD

 	
  * Add documentation for the WMTS multidimensional module

 	
  * Add an example of GS Download process with request of output reference


Bug Fixes:

 	
  * Slow startup of GeoServer with many layers

 	
  * Cannot upload style files in the style editor

 	
  * Generating a raster SLD style from template produces a formally invalid style

 	
  * WPS fails if geometry column is named "location"

 	
  * REST API services settings.html throws errors for null values

 	
  * REST PUT property update on ServiceInfo does not work properly for primitive properties

 	
  * ClassCastException when posting WFS Transaction request on a URL containing a valid GetFeature request

 	
  * High oversampling on raster cells with reproject can put a significant amount of load on GeoServer

 	
  * JMS Clustering does not propagate virtual services configurations


And more! For more information on this release check the release notes ([2.10.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=14500) | [2.10.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=14401&styleName=&projectId=10000) | [2.10-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=14202) | [2.10-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=13902&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) | [2.10-M0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=13102&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) )


## Security Considerations


This release addresses three security vulnerabilities:



 	
  * Additional restrictions have been placed on the demo request page

 	
  * Addressed an XML injection vulnerability identified in an automatic scan.

 	
  * GeoServer now changes sessions during login, this addresses a class of vulnerablities known as “session fixation”.


Thanks again to Nick Muerdter for reporting these in a responsible manner (and Andrea and Jody for addressing these during the November [bug stomp](http://blog.geoserver.org/2016/11/09/bug-stomp/).)

If you wish to report a security vulnerability, please visit our website for [instructions on responsible reporting](http://geoserver.org/issues/).


## About GeoServer 2.10


Articles, docs, blog posts and presentations:



 	
  * [State of GeoServer 2016](http://www.slideshare.net/jgarnett/state-of-geoserver) (slideshare)

 	
  * The [style editor](http://docs.geoserver.org/latest/en/user/styling/webadmin/index.html#style-editor) has been refreshed with the best ideas from the css extension

 	
  * The [styling workshop](http://docs.geoserver.org/latest/en/user/styling/workshop/index.html) has been updated for foss4g 2016 and now includes both CSS and YSLD examples.

 	
  * [Smart transparency in GeoServer with image/vnd.jpeg-png format](http://www.geo-solutions.it/blog/geoserver-smart-transparency/) (GeoSolutions)

 	
  * [QGIS SLD export improvements](http://www.geo-solutions.it/blog/qgis-sld-export/) (GeoSolutions)


Community modules

 	
  * A new community module to [backup/restore](http://docs.geoserver.org/latest/en/user/community/backuprestore/index.html) and restore GeoServer configuration

 	
  * A resource browser is available allowing remote management of styles, icons and fonts (needs building from sources).

 	
  * A new [WMTS multidimensional domain discovery](http://demo.geo-solutions.it/share/wmts-multidim/wmts_multidim_geosolutions.html) community module for discovering patches of data in scattered data sets

 	
  * The YSLD community module has been updated with extensive [documentation](http://docs.geoserver.org/latest/en/user/styling/ysld/index.html)


