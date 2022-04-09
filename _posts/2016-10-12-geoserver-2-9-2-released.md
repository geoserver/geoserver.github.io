---
author: jgarnett
comments: true
date: 2016-10-12 19:51:41+00:00
layout: post
link: http://blog.geoserver.org/2016/10/12/geoserver-2-9-2-released/
slug: geoserver-2-9-2-released
title: GeoServer 2.9.2 Released
wordpress_id: 2709
categories:
- Announcements
- Vulnerability
---

The GeoServer team is pleased to announce the release of [GeoServer 2.9.2](http://geoserver.org/release/2.9.2/). Download bundles are provided ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.2/geoserver-2.9.2-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.2/geoserver-2.9.2-war.zip/download), [dmg](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.2/geoserver-2.9.2.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.2/geoserver-2.9.2.exe/download)) along with documentation and extensions.

This is a stable release of GeoServer suitable for production systems. This release is made in conjunction with GeoTools 15.2 and GeoWebCache 1.9.2. We extend our thanks to all contributors for making this release possible.

Highlights of this release include:



 	
  * The macOS DMG is now signed by the Open Source Geospatial Foundation. This work done by Larry Shaffer and the system admin committee improves the Mac install experience.
For macOS 10.12 Apple has asked that all applications to be from the App Store (sigh) or signed by identified developers. Using the OSGeo certificate to sign our application [![geoserver-macos-10-12](/img/uploads/geoserver-macos-10.12.png)](/img/uploads/geoserver-macos-10.12.png)

 	
  * Style icons can now be referenced by URL in both the global styles folder and workspace styles folders.

 	
  * WMTS improved with both a web admin page and "virtual service" support providing a WMTS for each workspace.

 	
  * The INSPIRE extension now supports WMTS capabilities document. Upon installation of the INSPIRE extension the INSPIRE WMTS grid is now available.

 	
  * Embedded GeoWebCache now supports mbtiles based tile storage.

 	
  * Improvements to image mosaic [documentation](http://docs.geoserver.org/stable/en/user/data/raster/imagemosaic/) with more examples.

 	
  * Support for ["JPEG or PNG "output format](http://www.geo-solutions.it/blog/geoserver-smart-transparency/), dynamically choosing the best format based on image transparency

 	
  * Lots of bug fixes (check the release notes for details)


For more information about GeoServer 2.9.2 refer to release notes ([2.9.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=13500) | [2.9.1](https://osgeo-org.atlassian.net/secure/ConfigureReleaseNote.jspa?projectId=10000&version=14202) | [2.9.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=13003&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) | [RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=12502&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) | [beta2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=12700&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) | [beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=12100&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) | [M0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=11401&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) ).


## Security Considerations


This release addresses two security vulnerabilities:



 	
  * The default data directory now includes security restrictions on WFS-T functionality (restricting editing of data to the administrator account). This has the effect of making the service read-only by default, while still advertising we are a compliant WFS-T implementation. _If you have an existing GeoServer deployment which you wish to be read-only your can configure security settings as described, or set the [WFS service level to "basic"](http://docs.geoserver.org/latest/en/user/services/wfs/webadmin.html#service-levels)._
[![geoserver-read-only](/img/uploads/geoserver-read-only.png)](/img/uploads/geoserver-read-only.png)

 	
  * Aaron Waddell reported an XXE vulnerability in the GeoTools library which has been resolved (and is used by GeoServer). _We encourage all users to upgrade to GeoServer 2.9.2 at this time. Please note that there are **no additional releases of GeoServer 2.8 scheduled** - now is the time to upgrade._


If you wish to report a security vulnerability, please visit our website for [instructions on responsible reporting](http://geoserver.org/issues/).


## About GeoServer 2.9


Articles, docs, blog posts and presentations:



 	
  * Lots of goodies in the original [2.9.0 announcement](http://blog.geoserver.org/2016/05/30/geoserver-2-9-0-released/) (GeoServer Blog)

 	
  * Results of our [Bug Stomp Mini Code Sprint](http://blog.geoserver.org/2016/07/26/online-geoserver-bug-stomp-july-2016-results/) in July (GeoServer blog)

 	
  * Internals [upgrade to spring-4](https://github.com/geoserver/geoserver/wiki/Spring-4-Upgrade) for Java 8 compatibility (User Guide)

 	
  * [GeoServer code sprint success](http://blog.geoserver.org/2016/01/25/geoserver-code-sprint-success/) and [wicket migration code sprint](https://github.com/geoserver/geoserver/wiki/Wicket-migration-code-sprint) (GeoServer Blog)

 	
  * [GeoServer Plugin for QGIS](http://blog.geoserver.org/2015/12/23/geoserver-explorer-plugin-for-qgis/) (Boundless)

 	
  * [QGIS SLD export improvements](http://www.geo-solutions.it/blog/qgis-sld-export/) (GeoSolutions)

 	
  * [Smart transparency in GeoServer with image/vnd.jpeg-png format](http://www.geo-solutions.it/blog/geoserver-smart-transparency/) (GeoSolutions)

 	
  * [Simplify complex feature mappings setup with HALE](http://www.geo-solutions.it/blog/inspire-support-in-geoserver-made-easy-with-hale/) (GeoSolutions)

 	
  * [REST management of Resources](http://docs.geoserver.org/stable/en/user/rest/api/resources.html) (User Guide)


