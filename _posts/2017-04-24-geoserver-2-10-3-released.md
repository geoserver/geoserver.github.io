---
author: iant
comments: false
date: 2017-04-24 08:37:18+00:00
layout: post
link: http://blog.geoserver.org/2017/04/24/geoserver-2-10-3-released/
slug: geoserver-2-10-3-released
title: GeoServer 2.10.3 Released
wordpress_id: 2859
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_2102
version: 2.10.3
jira_version: 15201
---

We are happy to announce the release of [GeoServer 2.10.3](http://geoserver.org/release/2.10.3/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10.3/geoserver-2.10.3-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10.3/geoserver-2.10.3-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10.3/geoserver-2.10.3/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.10.3/geoserver-2.10.3.exe/download)) along with docs and extensions.

This is the release of GeoServer of the 2.10 branch is now going into maintenance and is no longer recommended for new production system. This release is made in conjunction with GeoTools 16.3.

This release is made by Ian Turton from the Astun Technology team. We would like to thank these volunteers  and everyone who contributed features, fixes and time during the release process.


## Security Considerations


This release addresses three security vulnerabilities:



 	
  * Added a [configurable delay](http://docs.geoserver.org/latest/en/user/security/webadmin/auth.html#brute-force-attack-prevention) during login, to mitigate a brute force attack.

 	
  * Added a [configurable parameter](http://docs.geoserver.org/latest/en/user/production/config.html#x-frame-options-policy) to control clickjacking attacks against the GeoServer UI.

 	
  * Added an additional parameter for locking down password autocomplete in the GeoServer UI


Thanks to Andrea Aime and Devon Tucker for providing fixes to these issues.

These fixes are also included in the 2.11.1 release.

If you wish to report a security vulnerability, please visit our website for [instructions on responsible reporting](http://geoserver.org/issues/).


## New Features and Improvements





 	
  * [[GEOS-7684](https://osgeo-org.atlassian.net/browse/GEOS-7684)] - Add rest endpoint for geofence admin rules

 	
  * [[GEOS-7763](https://osgeo-org.atlassian.net/browse/GEOS-7763)] - Add REST endpoint for a user to change their password

 	
  * [[GEOS-7957](https://osgeo-org.atlassian.net/browse/GEOS-7957)] - GeoFence: REST Rule DTO does not handle addressrange

 	
  * [[GEOS-8022](https://osgeo-org.atlassian.net/browse/GEOS-8022)] - Allow disabling usage of SLD and SLD_BODY in WMS requests (also for virtual services)




## Bug Fixes


A large number of bugs were fixed for this release including several that affected JMS clustering, WFS with 3D data and using the Style Editor with non-SLD styles. See the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15201) for more details of all the fixes.
