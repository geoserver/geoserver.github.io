---
author: tbarsballe
comments: false
date: 2017-11-21 23:43:37+00:00
layout: post
link: http://blog.geoserver.org/2017/11/21/geoserver-2-12-1-released/
slug: geoserver-2-12-1-released
title: GeoServer 2.12.1 Released
wordpress_id: 2920
categories:
- Announcements
tags:
- Release
release: release_212
version: 2.12.1
jira_version: 16705
---

We are happy to announce the release of [GeoServer 2.12.1](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.1/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.1/geoserver-2.12.1-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.1/geoserver-2.12.1-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.1/geoserver-2.12.1.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.1/geoserver-2.12.1.exe/download)) along with docs and extensions.










This is a stable release recommended for production use. This release is made in conjunction with GeoTools 18.1.




Highlights of this release are featured below, for more information please see the release notes ([2.12.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16705) | [2.12.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=16703&styleName=Html&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7Cf148b3772c10d37fb2a345c4d35ca4b24e27e75d%7Clin) | [2.12-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16600) | [2.12-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15700)).


## New Features and Improvements





 	
  * Moved Users/Groups/Roles REST from geofence-server (extension) to restconfig (core)




## Bug Fixes





 	
  * Copy style needs to copy content and format

 	
  * REST API CORS support

 	
  * YSLD ColorMap incorrectly recording a String (as shown in SLD conversion)

 	
  * MapPreviewPage search displays wrong results on first try

 	
  * GWC Seed Form returns blank page when seeding a layer.

 	
  * Monitor REST API won't return xml/json representation for request

 	
  * Failed to resolve workspace for style messages during startup













## About GeoServer 2.12 Series


Additional information on the 2.12 series:



 	
  * [State of GeoServer 2.12 ](https://www.slideshare.net/geosolutions/state-of-geoserver-21geoservernodeopts2)(SlideShare)

 	
  * [GeoServer Feature Frenzy](https://www.slideshare.net/jgarnett/geoserver-feature-frenzy-80906586/jgarnett/geoserver-feature-frenzy-80906586) (SlideShare)

 	
  * New [REST API documentation](http://docs.geoserver.org/latest/en/user/rest/index.html#rest)

 	
  * [REST API Code Sprint Results](http://blog.geoserver.org/2017/04/11/rest-api-code-sprint-results/)






