---
author: geoserver
comments: true
date: 2014-11-18 09:06:14+00:00
layout: post
link: http://blog.geoserver.org/2014/11/18/geoserver-2-6-1-released/
slug: geoserver-2-6-1-released
title: GeoServer 2.6.1 released
wordpress_id: 2041
---

The GeoServer team is happy to announce the release of [GeoServer 2.6.1](http://geoserver.org/release/2.6.1/). Download bundles are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.1/geoserver-2.6.1-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.1/geoserver-2.6.1-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.1/geoserver-2.6.1.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.1/geoserver-2.6.1.exe/download))  along with documentation and extensions.

GeoServer 2.6.1 is the next the stable release of GeoServer and is recommended for production deployment. Thanks to everyone taking part, submitting fixes and new functionality:



	
  * Fix for slow rendering of maps with lots of layers coming from a spatial database, reported by numerous users

	
  * Improvements in rendering labels over transparent maps

	
  * Fix for rendering tiled raster data, it could occasionally miss portions of the data

	
  * Fixes for WFS 2.0 joins

	
  * Better memory management when HTTP gzip-ping large amounts of GML/CSV/JSON data

	
  * Multidimensional WCS 2.0 outputs (NetCDF downloads) now support subsetting in CRS other than WGS84

	
  * An option to disable JAI native warp, which can cause some instability when reprojecting certain raster data sets

	
  * Some improvements in the GeoPackage outputs (still a community module, available via nightly builds)

	
  * Check the [release notes](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20651) for more details

	
  * This release is made in conjunction with GeoTools 12.1


Thanks to Andrea (GeoSolutions) for this release


# About GeoServer 2.6


Articles and resources for GeoServer 2.6 series:



	
  * [GeoServer at FOSS4G](http://blog.geoserver.org/2014/10/01/geoserver-at-foss4g/)

	
    * [State of GeoServer and GeoTools 2014](http://vimeo.com/106835755) ([slides](http://www.slideshare.net/jgarnett/state-of-geoserver-geotools-and-friends-2014))




	
  * [Raster Views in GeoServer via the CoverageView concept](http://www.geo-solutions.it/blog/overageview-concept-for-geoserver/) (GeoSolutions)

	
  * [Advanced Raster Projection in GeoServer](http://www.geo-solutions.it/blog/developers-corner-advanced-raster-projection-geoserver/) (GeoSolutions)

	
  * [Supporting Wind Barbs In GeoServer and GeoTools](http://www.geo-solutions.it/blog/developers-corner-supporting-wind-barbs-geoserver-geotools/) (GeoSolutions)

	
  * [GeoServer now supports Vector Footprints for ImageMosaic](http://www.geo-solutions.it/blog/geoserver-supports-footprints-imagemosaic/) (GeoSolutions)

	
  * [2.6.0 announcement](http://blog.geoserver.org/2014/10/03/geoserver-2-6-0-released/) and [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20399)

	
  * [2.6-RC1 announcement](http://blog.geoserver.org/2014/08/18/geoserver-2-6-rc1-released/) and [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?version=20536&styleName=&projectId=10311)

	
  * [2.6-beta announcement](http://blog.geoserver.org/2014/07/24/geoserver-2-6-beta-released/) and [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20172)





