---
author: geoserver
comments: true
date: 2013-08-18 13:53:10+00:00
layout: post
link: http://blog.geoserver.org/2013/08/18/geoserver-2-3-5-released/
slug: geoserver-2-3-5-released
title: GeoServer 2.3.5 Released
wordpress_id: 1519
categories:
- Announcements
tags:
- release
- stable
---

The GeoServer team is pleased to announce the release of [GeoServer 2.3.5](http://geoserver.org/display/GEOS/GeoServer+2.3.5):



	
  * Downloads ([zip](http://downloads.sourceforge.net/geoserver/geoserver-2.3.5-bin.zip), [war](http://downloads.sourceforge.net/geoserver/geoserver-2.3.5-war.zip) and [exe](http://downloads.sourceforge.net/geoserver/geoserver-2.3.5.exe)) are listed on the [GeoServer 2.3.5](http://geoserver.org/display/GEOS/GeoServer+2.3.5) page along with documentation and extensions.


This is a stable release containing several important fixes:

	
  * A couple new [authentication options for LDAP](http://jira.codehaus.org/browse/GEOS-5805), thanks to Mauro Bartolomeoli for this work.

	
  * The file browser used when defining a new data source once again lets windows users [explore the available drives](http://jira.codehaus.org/browse/GEOS-5842)

	
  * Alessio has [back ported](http://jira.codehaus.org/browse/GEOS-2527) a fix for creating a [data sources referencing a shared file system](http://jira.codehaus.org/browse/GEOS-2508).

	
  * GeoWebCache has fixes for [WMS 1.3.0](http://jira.codehaus.org/browse/GEOS-5685) and [database security](http://jira.codehaus.org/browse/GEOS-5828) (thanks to Jonathan Moules for reporting this one).

	
  * More details can be found in the [GeoServer 2.3.5 Release Notes](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=19445).


This release is made in conjunction with [GeoTools 9.5](http://geotoolsnews.blogspot.com.au/2013/08/geotools-95-released.html) and is the last [scheduled release](http://geoserver.org/display/GEOS/GeoTools+and+GeoServer+release+schedule) for the GeoServer 2.3.x series.
