---
author: geoserver
comments: true
date: 2013-05-20 03:33:28+00:00
layout: post
link: http://blog.geoserver.org/2013/05/19/geoserver-2-3-2-released/
slug: geoserver-2-3-2-released
title: GeoServer 2.3.2 released
wordpress_id: 1421
---

The GeoServer team is pleased to announce the release of GeoServer 2.3.2 for [download](http://geoserver.org/display/GEOS/GeoServer+2.3.2).



	
  * This release includes and is made in conjunction with GeoTools 9.2.

	
  * [The INSPIRE plugin](http://docs.geoserver.org/stable/en/user/extensions/inspire/index.html) has now graduated to extension and is included in this release. This plugin adds WMS and WFS capabilities support for metadata required for compliance with the European INSPIRE directive.

	
  * The application schema support (app-schema) support plugin now enables joining by default for data sources that support it.

	
  * Fixed transformation problems with projections based on Hotine Oblique Mercator (variant B) (for example Swiss CH1903 / LV03)

	
  * Fixed WFS lockups when a WFS 1.1 GetFeature is providing a schema referring back to the same server DescribeFeatureType

	
  * A new option to limit the file browser to the data directory, geared towards high security/multi-tenant environments


More details can be found in the [GeoServer 2.3.2 Release Notes](https://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=19195).
