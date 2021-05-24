---
author: jgarnett
comments: true
date: 2016-10-12 20:33:49+00:00
layout: post
link: http://blog.geoserver.org/2016/10/12/geoserver-2-10-rc1-released/
slug: geoserver-2-10-rc1-released
title: GeoServer 2.10-RC1 released
wordpress_id: 2708
categories:
- Announcements
tags:
- Release
release: release_210
version: 2.10-rc1
jira_version: 14202
---



The GeoServer team is happy to announce the release of [GeoServer 2.10-RC1](http://geoserver.org/release/2.10-RC1/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-RC1/geoserver-2.10-RC1-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-RC1/geoserver-2.10-RC1-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-RC1/geoserver-2.10-RC1.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-RC1/geoserver-2.10-RC1.exe/download)) along with docs and extensions.

While this release candidate is not intended for production we would like to ask everyone to download, try it out in your environment, try it out with your data, and report back success/glitches/failures to the [email list](http://geoserver.org/comm/).

We would like to thank everyone who This is a release candidate beta release of GeoServer made in conjunction with GeoTools 16-RC1.


## Testing Priorities


Here is our priorities for testing:



 	
  * Updated[ GeoServer Style Editor](http://docs.geoserver.org/latest/en/user/styling/webadmin/index.html#style-editor)

 	
  * CSS Extension - [nested rule](http://docs.geoserver.org/latest/en/user/styling/css/nested.html) and [rendering transform](http://docs.geoserver.org/latest/en/user/styling/css/transformation.html) support

 	
  * WMS Cascade functionality




## New Features and Highlights





 	
  * The macOS DMG is now signed by the Open Source Geospatial Foundation.

 	
  * Aaron Waddell reported an XXE vulnerability in the GeoTools library which has been resolved (and is used by GeoServer).

 	
  * GeoWebCache can now use MBTiles, including vector tiles.

 	
  * The default data directory now includes security restrictions on WFS-T functionality (restricting editing of data to the administrator account).

 	
  * Several fix/improvements in coverage view support for multiband sources and associated SLD band selection optimizations

 	
  * Work continues on the WMTS multidimensional extension (some fixes for GetHistogram and DescribeDomains)


For more information about the what is included in the GeoServer 2.10 refer to release notes ([2.10-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=14202) | [2.10-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=13902&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) | [2.10-M0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=13102&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) ).


## 










## About GeoServer 2.10


Articles, docs, blog posts and presentations:



 	
  * [State of GeoServer 2016](http://www.slideshare.net/jgarnett/state-of-geoserver) (slideshare)

 	
  * The [style editor](http://docs.geoserver.org/latest/en/user/styling/webadmin/index.html#style-editor) has been refreshed with the best ideas from the css extension

 	
  * [Smart transparency in GeoServer with image/vnd.jpeg-png format](http://www.geo-solutions.it/blog/geoserver-smart-transparency/) (GeoSolutions)

 	
  * [QGIS SLD export improvements](http://www.geo-solutions.it/blog/qgis-sld-export/) (GeoSolutions)


Community modules

 	
  * A new community module to [backup/restore](http://docs.geoserver.org/latest/en/user/community/backuprestore/index.html) and restore GeoServer configuration

 	
  * A new [WMTS multidimensional domain discovery](http://demo.geo-solutions.it/share/wmts-multidim/wmts_multidim_geosolutions.html) community module for discovering patches of data in scattered data sets

 	
  * The [styling workshop](http://docs.geoserver.org/latest/en/user/styling/workshop/index.html) has been updated to feature both CSS and YSLD examples.

 	
  * The YSLD community module has been updated with extensive [documentation](http://docs.geoserver.org/latest/en/user/styling/ysld/index.html)



