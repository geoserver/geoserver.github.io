---
author: David Blasby
date: 2005-04-22
layout: post
link: http://docs.codehaus.org/display/GEOS/GeoServer+1.3.0-beta3
wayback: https://web.archive.org/web/20060624095120/http://docs.codehaus.org:80/display/GEOS/GeoServer+1.3.0-beta3
title: "GeoServer 1.3.0-beta3 Released"
categories:
- Announcements
---

GeoServer 1.3.0-beta3 has been released, check it out below.

----

Servlet Container Compatabilty:

- [x] Jetty
- Others - currently untested

More GeoServer 1.3.0-beta3 links:

- [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-beta3/)
- [Release Notes](#release-notes)

Please add comments to this page for installation tips and tricks. You can edit this page to report back on additional servelt containers that work...

## Release notes

Improvement:

* [GEOS-142](https://osgeo-org.atlassian.net/browse/GEOS-142) Store services.xml and catalog.xml in a .geoserver directory?
* [GEOS-187](https://osgeo-org.atlassian.net/browse/GEOS-187) Update the document target.
* [GEOS-286](https://osgeo-org.atlassian.net/browse/GEOS-286) Add reprojection support and expose different bboxes
* [GEOS-329](https://osgeo-org.atlassian.net/browse/GEOS-329) Get rid of all the FINE level logging in LiteRenderer2

Bug:

* [GEOS-271](https://osgeo-org.atlassian.net/browse/GEOS-271) ACE_GIS Test 9 -  some map formats are not being returned properly
* [GEOS-297](https://osgeo-org.atlassian.net/browse/GEOS-297) Fail to render label

Task:

* [GEOS-233](https://osgeo-org.atlassian.net/browse/GEOS-233) Pass all CITE WMS tests
* [GEOS-234](https://osgeo-org.atlassian.net/browse/GEOS-234) Pass all ACE-GIS WMS tests

Sub-task:

* [GEOS-302](https://osgeo-org.atlassian.net/browse/GEOS-302) Reprojection in the WMS
* [GEOS-307](https://osgeo-org.atlassian.net/browse/GEOS-307) Make new demo calls for new shapefiles
