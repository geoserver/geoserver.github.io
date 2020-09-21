---
author: tbarsballe
comments: true
date: 2017-02-22 21:08:38+00:00
layout: post
link: http://blog.geoserver.org/2017/02/22/geoserver-2-10-2-released/
slug: geoserver-2-10-2-released
title: GeoServer 2.10.2 released
wordpress_id: 2788
categories:
- Announcements
---

The GeoServer team is pleased to announce the release of [GeoServer 2.10.2](http://geoserver.org/release/2.10.2/). Download bundles are provided ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.10.2/geoserver-2.10.2.bin/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.10.2/geoserver-2.10.2-war.zip/download), [dmg](https://sourceforge.net/projects/geoserver/files/GeoServer/2.10.2/geoserver-2.10.2.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.10.2/geoserver-2.10.2.exe/download)) along with documentation and extensions.

GeoServer 2.10.2 is the latest stable release of GeoServer and is recommended for production deployment. This release is made in conjunction with GeoTools 16.2 and GeoWebCache 1.10.2. Thanks to all contributors.

New Features and Improvements:



 	
  * Promote [YSLD module](http://docs.geoserver.org/stable/en/user/styling/ysld/index.html) to extension

 	
  * Add jetty-servlets.jar file to default jetty [to help users set up CORS](http://docs.geoserver.org/stable/en/user/production/container.html#enable-cors)

 	
  * Handle non error http codes (from HttpCodeException) as normal response

 	
  * Reducing output size of PDF with graphic fills by using tiling patterns


Bug Fixes:

 	
  * Disk quota usage page no longer shows negative bytes free (if you already have negative values in your quota DB, [follow this instructions](https://osgeo-org.atlassian.net/browse/GEOS-5615?focusedCommentId=69500&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-69500))

 	
  * New style editor can now detect and fix old GeoServer CSS styles (which were marked as SLD)

 	
  * Fixes to json output for layergroup

 	
  * Can not display table based pages in Turkish locale

 	
  * WMS 1.3.0 GetCapabilities response doesn't validate against the schema when using LayerGroups

 	
  * Editing style and moving it into workspace loses the edits

 	
  * Style Edit Page: Apply then Submit causes WicketRuntimeException

 	
  * Force transformation of ROI and NoData to transparent/bg color in direct raster rendering path


And more! For more information on this release check the release notes ([2.10.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=14800) | [2.10.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=14500) | [2.10.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=14401&styleName=&projectId=10000) | [2.10-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=14202) | [2.10-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=13902&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) | [2.10-M0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=13102&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) )


## About GeoServer 2.10


Articles, docs, blog posts and presentations:



 	
  * The YSLD extension added, with extensive [documentation](http://docs.geoserver.org/latest/en/user/styling/ysld/index.html)

 	
  * [State of GeoServer 2016](http://www.slideshare.net/jgarnett/state-of-geoserver) (slideshare)

 	
  * The [style editor](http://docs.geoserver.org/latest/en/user/styling/webadmin/index.html#style-editor) has been refreshed with the best ideas from the css extension

 	
  * The [styling workshop](http://docs.geoserver.org/latest/en/user/styling/workshop/index.html) has been updated for foss4g 2016 and now includes both CSS and YSLD examples.

 	
  * [Smart transparency in GeoServer with image/vnd.jpeg-png format](http://www.geo-solutions.it/blog/geoserver-smart-transparency/) (GeoSolutions)

 	
  * [QGIS SLD export improvements](http://www.geo-solutions.it/blog/qgis-sld-export/) (GeoSolutions)


Community modules

 	
  * A new community module to [backup/restore](http://docs.geoserver.org/latest/en/user/community/backuprestore/index.html) and restore GeoServer configuration

 	
  * A resource browser is available allowing remote management of styles, icons and fonts (needs building from sources).

 	
  * A new [WMTS multidimensional domain discovery](http://demo.geo-solutions.it/share/wmts-multidim/wmts_multidim_geosolutions.html) community module for discovering patches of data in scattered data sets


