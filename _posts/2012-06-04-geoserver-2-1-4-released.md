---
author: geoserver
comments: true
date: 2012-06-04 10:59:02+00:00
layout: post
link: http://blog.geoserver.org/2012/06/04/geoserver-2-1-4-released/
slug: geoserver-2-1-4-released
title: GeoServer 2.1.4 released
wordpress_id: 1072
---

The GeoServer team is happy to announce the release of GeoServer 2.1.4, now available for [download](http://geoserver.org/display/GEOS/GeoServer+2.1.4).

For the most part this is a maintainance release consisting of bug fixes, but as usual a few new features and improvements have managed to creep in. The release contains a total of [ 46 between bug fixes and improvements](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=18238). Some of the new and noteworthy include:



	
  * various improvements to the SQL server data store extension

	
  * snappier GUI when working with data whose coordinate system cannot be direclty matched to a native EPSG code

	
  * more accurate GetFeatureInfo

	
  * support for geography columns in SQL views against PostGIS

	
  * GetLegendGraphics now takes into account UOM and DPI parameters

	
  * ip based control and blacklisting in the control-flow extension

	
  * before/after custom sql statements when hitting DBSMs (session oriented sql, can be used to switch authentication in the database


And more. Check out the [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=17865) for the entire list. A big thank you to all core developers, and a particular mention to users that contributed patches for this release. This includes:



	
  * Lars Lingner for addding the "forceLabel" parameter to GetLegendGraphic

	
  * Rudi Hochmeister for speeding up the JSON output format on large layers

	
  * Robert Coup for making SQL views parameters easier to pass in

	
  * Tony Young for making WCS 1.0 DescribeCoverage support the "all coverages" description mode

	
  * Hajo Kliemeck for making GetFeatureInfo work properly with user defined SLDs, and for improving legend decoration code

	
  * Tim Shaub for making the OpenLayers preview work with Firefox 10+


And of course, thanks to all those who helped out by filing bug reports.

[Download 2.1.4](http://geoserver.org/display/GEOS/GeoServer+2.1.4), try it out and help us to continue to improve GeoServer by providing feedback on the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users) and reporting bugs in the [issue tracker](https://jira.codehaus.org/browse/GEOS).


