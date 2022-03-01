---
author: jgarnett
comments: true
date: 2016-11-25 00:45:44+00:00
layout: post
link: http://blog.geoserver.org/2016/11/25/geoserver-2-9-3-released/
slug: geoserver-2-9-3-released
title: GeoServer 2.9.3 Released
wordpress_id: 2775
categories:
- Announcements
- Vulnerability
tags:
- maintenance
- release
---

The GeoServer team is pleased to announce the release of [GeoServer 2.9.3](http://geoserver.org/release/2.9.3/). Download bundles are provided ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.3/geoserver-2.9.3-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.3/geoserver-2.9.3-war.zip/download), [dmg](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.3/geoserver-2.9.3.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.3/geoserver-2.9.3.exe/download)) along with documentation and extensions.

This is a maintenance release of GeoServer suitable for production systems. Maintenance releases are focused on bug fixes and stability, rather than new features.

The team has been working hard, resulting in a wide range of bug fixes:



 	
  * Windows installer fixed allowing port to set for standalone or service use

 	
  * KML Output managed a date-month swap when used in a non-POSIX locale.

 	
  * Improved documentation for the [demo pages](http://docs.geoserver.org/maintain/en/user/configuration/demos/index.html#demos-wcsrequestbuilder), including the [WCS Request builder](http://docs.geoserver.org/maintain/en/user/services/wcs/requestbuilder.html#wcs-request-builder).

 	
  * CSS stroke-offset now supports expressions

 	
  * WMS GetCapabilities fix for inadvertently show layer group contents multiple times.

 	
  * Style generation fix for raster data layers

 	
  * Coverage view improvements include preservation of origional band names, and alpha band if available.

 	
  * WFS correctly handles disabled stores

 	
  * REST API

 	
    * Correctly represent empty true/false values for html output

 	
    * Representation of an empty styles list in JSON fixed

 	
    * Cascade delete fixed to correctly handle nested layer groups




 	
  * JMS Clustering has received a number of fixes: correctly handles virtual service configuration, propagation of workspace and service settings.

 	
  * Lots of bug fixes (check the release notes for details)


For more information about GeoServer 2.9.3 refer to release notes ([2.9.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=14402)|[2.9.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=13500) | [2.9.1](https://osgeo-org.atlassian.net/secure/ConfigureReleaseNote.jspa?projectId=10000&version=14202) | [2.9.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=13003&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) | [RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=12502&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) | [beta2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=12700&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) | [beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=12100&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) | [M0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=11401&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) ).


## Community Modules


Community module updates:



 	
  * A community module is now available allowing GeoServer to authenticate against the OAuth2 protocol (including Google OAuth2).




## Security Considerations


This release addresses three security vulnerabilities:



 	
  * Additional restrictions have been placed on the demo request page

 	
  * Addressed an XML injection vulnerability identified in an automatic scan.

 	
  * GeoServer now changes sessions during login, this addresses a class of vulnerablities known as "session fixation".


Thanks again to Nick Muerdter for reporting these in a responsible manner (and Andrea and Jody for addressing these during the November [bug stomp](http://blog.geoserver.org/2016/11/09/bug-stomp/).)

If you wish to report a security vulnerability, please visit our website for [instructions on responsible reporting](http://geoserver.org/issues/).


## About GeoServer 2.9


Articles, docs, blog posts and presentations:



 	
  * Lots of goodies in the original [2.9.0 announcement](http://blog.geoserver.org/2016/05/30/geoserver-2-9-0-released/) (GeoServer Blog)

 	
  * Results of our [Bug Stomp Mini Code Sprint](http://blog.geoserver.org/2016/07/26/online-geoserver-bug-stomp-july-2016-results/) in July (GeoServer blog)

 	
  * Internals [upgrade to spring-4](https://github.com/geoserver/geoserver/wiki/Spring-4-Upgrade) for Java 8 compatibility (User Guide)

 	
  * [GeoServer code sprint success](http://blog.geoserver.org/2016/01/25/geoserver-code-sprint-success/) and [wicket migration code sprint](https://github.com/geoserver/geoserver/wiki/Wicket-migration-code-sprint) (GeoServer Blog)

 	
  * [GeoServer Plugin for QGIS](http://blog.geoserver.org/2015/12/23/geoserver-explorer-plugin-for-qgis/) (Boundless)

 	
  * [QGIS SLD export improvements](http://www.geo-solutions.it/blog/qgis-sld-export/) (GeoSolutions)

 	
  * [Smart transparency in GeoServer with image/vnd.jpeg-png format](http://www.geo-solutions.it/blog/geoserver-smart-transparency/) (GeoSolutions)

 	
  * [Simplify complex feature mappings setup with HALE](http://www.geo-solutions.it/blog/inspire-support-in-geoserver-made-easy-with-hale/) (GeoSolutions)

 	
  * [REST management of Resources](http://docs.geoserver.org/stable/en/user/rest/api/resources.html) (User Guide)




## 
