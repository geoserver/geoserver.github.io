---
author: geoserver
comments: true
date: 2013-02-26 15:27:22+00:00
layout: post
link: http://blog.geoserver.org/2013/02/26/geoserver-2-3-rc1-released/
slug: geoserver-2-3-rc1-released
title: GeoServer 2.3-RC1 Released
wordpress_id: 1341
categories:
- Announcements
- Features
---

The GeoServer team is happy to announce the release of GeoServer 2.3-RC1, available for [download](http://geoserver.org/display/GEOS/GeoServer+2.3-RC1). This release contains a number of bug fixes and small improvements since [2.3-beta](http://blog.geoserver.org/2013/01/29/geoserver-2-3-beta-released/). Here is a quick summary:



	
  * faster computation of layer bounding box for Oracle data sources when the table is not in the user's schema ([[GEOS-5535](https://jira.codehaus.org/browse/GEOS-5535)])

	
  * a few improvements to SLD 1.1 compatibility, fixing a few bits that are available in SLD 1.0 but not quite working when read from SLD 1.1 ([[GEOS-4718](https://jira.codehaus.org/browse/GEOS-4718)], [[GEOS-5544](https://jira.codehaus.org/browse/GEOS-5544)])

	
  * fix for HTML templates not being used when the SLD has a large number or rules ([[GEOS-5534](https://jira.codehaus.org/browse/GEOS-5534)])

	
  * improvements in the integration of the new GeoWebCache disk quota subsystem ([[GEOS-5633](https://jira.codehaus.org/browse/GEOS-5633)], [[GEOS-5597](https://jira.codehaus.org/browse/GEOS-5597)], [[GEOS-5634](https://jira.codehaus.org/browse/GEOS-5634)])

	
  * handling the same parameter used multiple times in the same request ([[GEOS-5645](https://jira.codehaus.org/browse/GEOS-5645)])

	
  * ability to recover the master password in case it's lost ([[GEOS-5606](https://jira.codehaus.org/browse/GEOS-5606)])

	
  * fixed a number of extensions that were not properly working in 2.3-beta, app-schema and excel, ([[GEOS-5496](https://jira.codehaus.org/browse/GEOS-5496)], [[GEOS-5629](https://jira.codehaus.org/browse/GEOS-5629)])

	
  * GetLegendGraphics won't cut out large point symbols anymore, it will rescale them instead ([[GEOS-5592](https://jira.codehaus.org/browse/GEOS-5592)), and made GetLegendGraphics work against layers whose geometry type is unkonwn ([[GEOS-5587](https://jira.codehaus.org/browse/GEOS-5587)])


See the [change log](https://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=19071) for all the details. Special thanks to everyone who contributed for this release.

Try out the release candidate today and help us by reporting any issues found on the [GeoServer mailing list](http://geoserver.org/display/GEOS/Mailing+Lists) and in the [bug tracker](https://jira.codehaus.org/browse/GEOS).
