---
author: jgarnett
comments: true
date: 2016-04-22 00:02:21+00:00
layout: post
link: http://blog.geoserver.org/2016/04/22/geoserver-2-9-beta2-released/
slug: geoserver-2-9-beta2-released
title: GeoServer 2.9-beta2 released
wordpress_id: 2631
categories:
- Announcements
tags:
- beta
- release
---

The GeoServer team is pleased to announce the release of [GeoServer 2.9-beta2](http://geoserver.org/release/2.9-beta2/). The previous 2.9-beta discovered an [incompatibility](https://github.com/geoserver/geoserver/wiki/Spring-4-Upgrade) with Java 8, resulting in a bit of [emergency planning](https://github.com/geoserver/geoserver/wiki/GSIP-142) and a delay to the 2.9.0 [release schedule](https://github.com/geoserver/geoserver/wiki/Release-Schedule).

Download [bundles](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9-beta2/) are available ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9-beta2/geoserver-2.9-beta2-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9-beta2/geoserver-2.9-beta2-war.zip/download), [dmg](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9-beta2/geoserver-2.9-beta2.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9-beta2/geoserver-2.9-beta2.exe/download)). A reminder that beta releases are intended for public feedback and are not recommended for production use.

Highlights:



 	
  * This release requires Java 8 and is compatible with Oracle JDK and OpenJDK

 	
  * GeoServer now requires Servlet 3 (so Tomcat 7 or newer if you are doing a WAR install)

 	
  * Negative-date now supported (for GeoNode compatibility)

 	
  * New REST API for [installation status](http://docs.geoserver.org/latest/en/user/rest/api/manifests.html#about-status-format)

 	
  * For more information check the release notes for [beta2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=12700) (history [beta1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=12100)|[M0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=11401&styleName=&projectId=10000))

 	
  * Update to Spring 4 and JAI-EXT to 1.0.9


This 2.9-beta2 release is released in conjunction with GeoTools 15-beta2 and GeoWebCache 1.9-beta2. Thanks to Jody Garnett (Boundless) and Kevin Smith (Boundless) for this release.


## Beta Testing


The GeoServer Team has been hard at work to bring you this beta release. Thanks to the committers for taking part in the emergency spring-4 upgrade and community members joining for subsequent testing and quality assurance: Justin Deoliveira and Andrea Aimie, Emanuele Tajariol, Damiano Giampaoli, Ben Caradoc-Davies, Niels Charlier, Mauro Bartolomeoli, Jody Garnett, Jukka Rahkonen, Brad Hards, Kevin Smith, Chris Snider, Torben Barsballe, Christian Mueller, Luigi Pirelli  ... and next you!

Here is our priorities for testing:



 	
  * Seeking confirmation on Java 8 compatibility (test Oracle JDK and OpenJDK on a range of platforms)

 	
  * Testing of the user-interface (although the team has performed extensive manual testing we need your help)

 	
  * Release packaging (check for anything out of date, any issues starting up)

 	
  * GeoServer security integration


We have a couple known issues to keep in mind when testing:

 	
  * Windows installer "Install as service" needs a configuration change once installed ([GEOS-7507](https://osgeo-org.atlassian.net/browse/GEOS-7507))
Open wrapper.conf and update contents with: wrapper.app.parameter.1=org.eclipse.jetty.start.Main

 	
  * Windows installer "Run manually" may have an issue with startup.bat ([GEOS-7509](https://osgeo-org.atlassian.net/browse/GEOS-7509))

 	
  * Several issues have been reported with the Demo Page ([GEOS-7513](https://osgeo-org.atlassian.net/browse/GEOS-7513))




## About GeoServer 2.9


Articles, docs, blog posts and presentations:



 	
  * Internals [upgrade to spring-4](https://github.com/geoserver/geoserver/wiki/Spring-4-Upgrade) for Java 8 compatibility

 	
  * [GeoServer code sprint success](http://blog.geoserver.org/2016/01/25/geoserver-code-sprint-success/) and [wicket migration code sprint](https://github.com/geoserver/geoserver/wiki/Wicket-migration-code-sprint)

 	
  * [GeoServer Plugin for QGIS](http://blog.geoserver.org/2015/12/23/geoserver-explorer-plugin-for-qgis/)

 	
  * [REST configuration Resources](http://docs.geoserver.org/latest/en/user/rest/api/resources.html) (docs)


The GeoServer team extends our thanks to wicket upgrade sprint sponsors: [OSGeo](http://www.osgeo.org/), [Boundless](http://boundlessgeo.com/), [Vivid Solutions](http://www.vividsolutions.com/), [How 2 Map](http://www.how2map.com/), [San Jose Water Company](https://www.sjwater.com/), [Transient](http://transient.nz/) and [Geobeyond](http://www.geobeyond.it/).
