---
author: jgarnett
comments: false
date: 2018-07-25 13:23:00+00:00
layout: post
link: http://blog.geoserver.org/2018/07/25/geoserver-2-13-2-released/
slug: geoserver-2-13-2-released
title: GeoServer 2.13.2 released
wordpress_id: 2953
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_213
version: 2.13.2
jira_version: 16728
---



We are happy to announce the release of [GeoServer 2.13.2](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.2/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.2/geoserver-2.13.2-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.2/geoserver-2.13.2-war.zip/download), and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.2/geoserver-2.13.2.exe/download)) along with docs and extensions.

This is a stable release recommended for production use. This release is made in conjunction with GeoTools 19.2 and GeoWebCache 1.13.2.




Highlights of this release are featured below, for more information please see the release notes ([2.13.2 ](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16728)| [2.13.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16724) | [2.13.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16722) | [2.13-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16717) | [2.13-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16702)).


### Improvements and Fixes





 	
  * style editor map legend always includes legend

 	
  * performance improvement for multi-band coverage time series

 	
  * WMS 1.3.0 performance improvement for north/east axis order

 	
  * Fix support of external graphics over http




### Security updates


Please update your production instances of GeoServer to receive the latest security updates and fixes.

This release addresses several security vulnerabilities:



 	
  * Prevent arbitrary code execution via Freemarker Template injection

 	
  * XXE vulnerability in GeoTools XML Parser

 	
  * XXE vulnerability in WPS Request builder

 	
  * Various library upgrades (see above) from versions with known CVEs


Thanks to Steve Ikeoka, Kevin Smith, Brad Hards and Nuno Oliveira for providing fixes to these issues.

If you encounter a security vulnerability in GeoServer, or any other open source software, please take care to report the issue in a [responsible fashion](http://docs.geoserver.org/stable/en/user/introduction/gettinginvolved.html#bug-tracking).


## About GeoServer 2.13 Series


Additional information on the 2.13 series:



 	
  * [Isolated workspaces](http://docs.geoserver.org/latest/en/user/data/webadmin/workspaces.html#isolated-workspaces) (User Guide)

 	
  * [Coverage views from heterogeneous bands](http://docs.geoserver.org/latest/en/user/data/raster/coverageview.html#heterogeneous-coverage-views) (User Guide)

 	
  * [State of GeoServer 2.13](https://www.slideshare.net/jgarnett/state-of-geoserver-213) (slideshare)

 	
  * See the [GeoServer 2.13.0 released](http://blog.geoserver.org/2018/03/20/geoserver-2-13-0-released/) announcement for visual guide to new features



