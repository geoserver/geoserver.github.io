---
author: tbarsballe
comments: true
date: 2016-05-03 20:48:03+00:00
layout: post
link: http://blog.geoserver.org/2016/05/03/geoserver-2-9-rc1-released/
slug: geoserver-2-9-rc1-released
title: GeoServer 2.9-RC1 Released!
wordpress_id: 2633
categories:
- Announcements
tags:
- release
---

The GeoServer team is pleased to announce GeoServer 2.9-RC1. Downloads are available ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9-RC1/geoserver-2.9-RC1-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9-RC1/geoserver-2.9-RC1-war.zip/download), [dmg](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9-RC1/geoserver-2.9-RC1.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9-RC1/geoserver-2.9-RC1.exe/download)) along with docs and extensions.

This release is made by Torben Barsballe (Boundless) in conjunction with GeoWebCache 1.9-RC1 and GeoTools 15-RC1.

This is a release candidate for final testing before we release 2.9.0.

Highlights:



 	
  * This release requires Java 8 and is compatible with Oracle JDK and OpenJDK

 	
  * GeoServer now requires Servlet 3 (so Tomcat 7 or newer if you are doing a WAR install)

 	
  * Update to Spring 4 and JAI-EXT to 1.0.9

 	
  * For more information, check the [2.9-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=12100), [2.9-beta2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=12700), and [2.9-M0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=11401) release notes.


Fixes since beta:

 	
  * [Naming geoserver layer differently from underlying postgis table causes aggregates to be omitted in SQL queries supporting time dimension in GetCapabilities and related operations.](https://osgeo-org.atlassian.net/browse/GEOS-5977)

 	
  * [Web interface does not reflect workspace specific WPS enabled/disabled properly](https://osgeo-org.atlassian.net/browse/GEOS-7159)

 	
  * [Enabling WPS for a workspace doesn't appear on the GUI after reload](https://osgeo-org.atlassian.net/browse/GEOS-7253)

 	
  * [WPS workspace specific configurations fails to load](https://osgeo-org.atlassian.net/browse/GEOS-7449)

 	
  * [Drag and drop rules in GeoFence not working](https://osgeo-org.atlassian.net/browse/GEOS-7487)

 	
  * [Restricting security on layers breaks aggregate visitor optimizations in JDBC stores](https://osgeo-org.atlassian.net/browse/GEOS-7497)

 	
  * [Stacktrace when modifying the configuration of a WMS Cascade layer](https://osgeo-org.atlassian.net/browse/GEOS-7499)

 	
  * [Update jetty version used by windows installer service wrapper](https://osgeo-org.atlassian.net/browse/GEOS-7507)

 	
  * [Stacktrace with unsupported option in GWC Memory Blobstore](https://osgeo-org.atlassian.net/browse/GEOS-7523)

 	
  * [PDF generation can contain invalid polygons whose fill bleeds out in the whole map](https://osgeo-org.atlassian.net/browse/GEOS-7525)


For more information see 2.9-RC1 [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=12502).

We would like to thank the sponsors of the [Wicket 7 upgrade](https://wiki.osgeo.org/wiki/GeoServer_Code_Sprint_2016) sprint: [OSGeo](http://www.osgeo.org/), [Boundless](http://boundlessgeo.com/), [Vivid Solutions](http://www.vividsolutions.com/), [How 2 Map](http://www.how2map.com/), [San Jose Water Company](https://www.sjwater.com/), [Transient](http://transient.nz/) and [Geobeyond](http://www.geobeyond.it/) (with in-kind sponsors GeoSolutions, CCRi, Astun Technology and Voyager).


## About GeoServer 2.9


Articles, docs, blog posts and presentations:



 	
  * Internals [upgrade to spring-4](https://github.com/geoserver/geoserver/wiki/Spring-4-Upgrade) for Java 8 compatibility

 	
  * [GeoServer code sprint success](http://blog.geoserver.org/2016/01/25/geoserver-code-sprint-success/) and [wicket migration code sprint](https://github.com/geoserver/geoserver/wiki/Wicket-migration-code-sprint)

 	
  * [GeoServer Plugin for QGIS](http://blog.geoserver.org/2015/12/23/geoserver-explorer-plugin-for-qgis/)

 	
  * [REST configuration Resources](http://docs.geoserver.org/latest/en/user/rest/api/resources.html) (docs)




## GeoServer Community


GeoServer Community modules provide an area for ideas and experimentation. Community highlights for this release:



 	
  * [Community YSLD](https://github.com/geoserver/geoserver/tree/master/src/community/ysld): The YSLD [styling language](https://github.com/geotools/geotools/tree/master/modules/unsupported/ysld) provides a more concise alternative to SLD, while still sharing the same structure.


Community modules should be considered a work-in-progress and are subject to quality assurance, documentation IP checks and a maintainer before being considered ready for release.
