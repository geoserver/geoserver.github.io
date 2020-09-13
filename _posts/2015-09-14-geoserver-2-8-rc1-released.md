---
author: geoserver
comments: true
date: 2015-09-14 18:50:49+00:00
layout: post
link: http://blog.geoserver.org/2015/09/14/geoserver-2-8-rc1-released/
slug: geoserver-2-8-rc1-released
title: GeoServer 2.8-RC1 Released
wordpress_id: 2346
categories:
- Announcements
tags:
- GeoServer
- release
- Release Candidate
---

The GeoServer team is pleased to announce GeoServer 2.8-RC1. Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8-RC1/geoserver-2.8-RC1-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8-RC1/geoserver-2.8-RC1-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8-RC1/geoserver-2.8-RC1.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8-RC1/geoserver-2.8-RC1.exe/download)) along with docs and extensions.

This release is made by Kevin Smith (Boundless) in conjunction with GeoWebCache 1.8-RC1 and GeoTools14-RC1.

This is a release candidate for final testing before we release 2.8.0.

Fixes since beta:



	
  * [The WPS Download process cannot use output formats plugged via a factory](https://osgeo-org.atlassian.net/browse/GEOS-7186)

	
  * [Remove remaining codehaus repo references](https://osgeo-org.atlassian.net/browse/GEOS-7191)

	
  * [WFS SHAPE-ZIP output does not always honor field length restrictions](https://osgeo-org.atlassian.net/browse/GEOS-7195)


For more information see 2.8-RC1 [release notes](https://osgeo-org.atlassian.net/projects/GEOS/versions/11302).


## About GeoServer 2.8


GeoServer 2.8 is [scheduled](http://geoserver.org/roadmap/) for September release. For more information:



	
  * [XEE Vunerability](http://blog.geoserver.org/2015/06/27/geoserver-xee-vulnerability/) (GeoServer)

	
  * [Z ordering features within and across feature types and layers](http://docs.geoserver.org/latest/en/user/styling/sld-extensions/z-order/index.html#z-ordering-features-within-and-across-feature-types-and-layers) (User Manual)

	
  * [JAI-Ext, the Open Source replacement for Oracle JAI](http://www.geo-solutions.it/blog/developers-corner-jai-ext-the-open-source-replacement-for-oracle-jai/) (GeoSolutions)

	
  * [Customizable arrow in GeoServer](http://www.geo-solutions.it/blog/customizable-arrow-geoserver/) (GeoSolutions)

	
  * [PostGIS Curve Support](http://www.geo-solutions.it/blog/postgis-curves-in-geoserver/) (GeoSolutions)

	
  * [Improved NetCDF/GRIB support in GeoServer](http://www.geo-solutions.it/blog/netcdf-grib-support-geoserver/) (GeoSolutions)


For additional details see the [2.8-beta](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=10164) and [2.8-M0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=10163) release notes.


## GeoServer Community


GeoServer Community modules provide an area for ideas and experimentation:



	
  * WCS and WPS output formats based on gdal_translate to provide a greater range of output formats

	
  * Embedded GeoFence server, REST API and GUI is the result of a productive collaboration between GeoSolutions and Boundless offering greater rule-based control of GeoServer security

	
  * [MongoDB DataStore](http://boundlessgeo.com/2015/07/mongodb-collaboration/) enabling GeoServer to publish from this popular JSON based document database (no zip packaging, needs volunteer)


Community modules should be considered a work-in-progress and are subject to quality assurance, documentation IP checks and a maintainer before being considered ready for release.


