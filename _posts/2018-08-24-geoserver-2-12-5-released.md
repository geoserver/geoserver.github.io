---
author: tbarsballe
comments: false
date: 2018-08-24 19:52:22+00:00
layout: post
link: http://blog.geoserver.org/2018/08/24/geoserver-2-12-5-released/
slug: geoserver-2-12-5-released
title: GeoServer 2.12.5 released
wordpress_id: 2963
---

We are happy to announce the release of [GeoServer 2.12.5](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.4/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.5/geoserver-2.12.5-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.5/geoserver-2.12.5-war.zip/download), and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.5/geoserver-2.12.5.exe/download)) along with docs and extensions.







This is the last maintenance release for the 2.12.x series, so we recommend users to plan an upgrade to 2.13.x or to the upcoming 2.14.x series. This release is made in conjunction with GeoTools 18.5.




Highlights of this release are featured below, for more information please see the release notes ([2.12.5](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16731), [2.12.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16726), [2.12.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16715),[2.12.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16709), [2.12.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16705)| [2.12.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16703) | [2.12-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16600) | [2.12-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15700)).


## Improvements





 	
  * ImageMosaic should work when the images have no CRS information

 	
  * Upgrade Apache POI dependencies

 	
  * Upgrade jasypt dependency

 	
  * Upgrade json-lib dependency to 2.4

 	
  * Upgrade bouncycastle provider to 1.60




## Bug Fixes





 	
  *  NullPointerException during WMS request of layer group when caching is enabled

 	
  * GeorectifyCoverage fails to handle paths with spaces

 	
  *  CSS translator does not support mark offset/anchors based on expressions (but SLD does)

 	
  * GeoServerSecuredPage might not redirect to login page in some obscure cases after Wicket upgrade




### Security updates


Please update your production instances of GeoServer to receive the latest security updates and fixes.




This release addresses several security vulnerabilities:



 	
  * Prevent arbitrary code execution via Freemarker Template injection

 	
  * XXE vulnerability in GeoTools XML Parser

 	
  * XXE vulnerability in WPS Request builder

 	
  * Various library upgrades (see above) from versions with known CVEs


Thanks to Steve Ikeoka, Kevin Smith, Brad Hards and Nuno Oliveira for providing fixes to these issues.

These fixes are also included in the 2.13.2 release.




If you encounter a security vulnerability in GeoServer, or any other open source software, please take care to report the issue in a [responsible fashion](http://docs.geoserver.org/stable/en/user/introduction/gettinginvolved.html#bug-tracking).









# About GeoServer 2.12 Series


Additional information on the 2.12 series:



 	
  * [State of GeoServer 2.12 ](https://www.slideshare.net/geosolutions/state-of-geoserver-21geoservernodeopts2)(SlideShare)

 	
  * [GeoServer Feature Frenzy](https://www.slideshare.net/jgarnett/geoserver-feature-frenzy-80906586/jgarnett/geoserver-feature-frenzy-80906586) (SlideShare)

 	
  * New [REST API documentation](http://docs.geoserver.org/latest/en/user/rest/index.html#rest)

 	
  * [REST API Code Sprint Results](http://blog.geoserver.org/2017/04/11/rest-api-code-sprint-results/)



