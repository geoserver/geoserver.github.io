---
author: geoserver
comments: true
date: 2015-10-20 16:43:47+00:00
layout: post
link: http://blog.geoserver.org/2015/10/20/geoserver-2-7-3-released/
slug: geoserver-2-7-3-released
title: GeoServer 2.7.3 released
wordpress_id: 2394
categories:
- Announcements
tags:
- release
---

The GeoServer team is happy to announce the release of [GeoServer 2.7.3](http://geoserver.org/release/2.7.3/). Download bundles are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.3/geoserver-2.7.3-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.3/geoserver-2.7.3-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.3/geoserver-2.7.3.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.3/geoserver-2.7.3.exe/download))  along with documentation and extensions.

GeoServer 2.7.3 is a maintenance release of GeoServer recommended for production deployment. Thanks to everyone taking part, submitting fixes and new functionality including:



	
  * Further fixes for the XXE vulnerability, along with a fix for a remote code execution vulnerability in the REST API (requires admin credentials to trigger it)

	
  * Some WCS 1.1 and 2.0 fixes

	
  * Some improvements in the management of style specific workspaces when modifying layer groups with the REST API

	
  * Optimized the size of DBF in the SHAPE-ZIP output format

	
  * A few improvements in the importer, including speeding up import setup by delaying layer bounds computation, and allowing to harvest granules in an empty mosaic previously setup via the REST API

	
  * For a full list, see the [release notes](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=11101).


Also, as a heads up for Oracle users, the Oracle store does not ship anymore with the JDBC driver (due to redistribution limitations imposed by Oracle). For details see the updated the oracle installation instructions [here](http://docs.geoserver.org/stable/en/user/data/database/oracle.html#oracle-install).

Thanks to Andrea (GeoSolutions) and Kevin (Boundless) for this release.


