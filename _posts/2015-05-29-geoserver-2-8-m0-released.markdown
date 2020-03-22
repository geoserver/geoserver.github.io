---
author: geoserver
comments: true
date: 2015-05-29 06:16:35+00:00
layout: post
link: http://blog.geoserver.org/2015/05/29/geoserver-2-8-m0-released/
slug: geoserver-2-8-m0-released
title: GeoServer 2.8-M0 Released
wordpress_id: 2214
categories:
- Announcements
---

We are happy to announce the release of [GeoServer 2.8-M0](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8-M0/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8-M0/geoserver-2.8-M0-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8-M0/geoserver-2.8-M0-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8-M0/geoserver-2.8-M0.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8-M0/geoserver-2.8-M0.exe/download)) along with docs and extensions.

This is milestone release of GeoServer made in conjunction with GeoTools 14-M0.

We have both new features and a number of key "under the hood" changes to GeoServer. This technology preview is made available for your evaluation and feedback and is not intended for production.

Highlights from the [release notes](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=10163):



	
  * JAI-Ext integration for geospatial specific image processing operations  ([github](https://github.com/geosolutions-it/jai-ext)), adding direct support for NODATA in raster sources

	
  * Replacement of vecmath with EJML matrix library

	
  * Importer improvements, dalwarp/gdal_translate/gdaladdo transformations and ability to add a granule to a mosaic

	
  * Read/write PostGIS curve support

	
  * GetMap support for by layer interpolation methods

	
  * Stop shipping old Oracle JDBC driver

	
  * Pretty print option for style REST API

	
  * Allow environment variables to be used in freemarker template files


Also, looking at the GeoTools 14-M0 release notes, we have:

	
  * Significant increase in GML 3.X encoding speed

	
  * New projections supported: sinusoidal, gnomonic

	
  * New extshape://arrow with parameters controlling its proportions


Thanks to Jody (Boundless) for pulling this release together.


## About GeoServer 2.8


GeoServer 2.8 is [scheduled](http://geoserver.org/roadmap/) for September release. For more information:



	
  * [JAI-Ext, the Open Source replacement for Oracle JAI](http://www.geo-solutions.it/blog/developers-corner-jai-ext-the-open-source-replacement-for-oracle-jai/) (GeoSolutions)


We will add additional blog posts to this section as news is made available.
