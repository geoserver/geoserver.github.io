---
author: geoserver
comments: true
date: 2015-01-20 10:48:15+00:00
layout: post
link: http://blog.geoserver.org/2015/01/20/geoserver-2-6-2-released/
slug: geoserver-2-6-2-released
title: GeoServer 2.6.2 released
wordpress_id: 2066
---

The GeoServer team is happy to announce the release of [GeoServer 2.6.2](http://geoserver.org/release/2.6.2/). Download bundles are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.2/geoserver-2.6.2-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.2/geoserver-2.6.2-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.2/geoserver-2.6.2.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.2/geoserver-2.6.2.exe/download))  along with documentation and extensions.

GeoServer 2.6.2 is the next the stable release of GeoServer and is recommended for production deployment. Thanks to everyone taking part, submitting fixes and new functionality:



	
  * The issue with GZIP encoding breaking CSS download in some browsers has been fixed

	
  * Have the pre-generalized store use again the simplified geometries against the PostGIS store (regressed in 2.6.0)

	
  * Relative paths in SLD using a "file://image.png" syntax are supported again (regressed in 2.6.0)

	
  * Removing also layer groups and styles contained in the workspace when the workspace is deleted

	
  * Make WCS 2.0 / WCS EO more lenient when the workspace is not specified in requests, or when a single mosaic granule is requested in EO requests

	
  * Allow disabling "advanced projection handling" for raster data via a system variable (for the few cases in which it misbehaves, fixes are underway, please do report if you see issues)

	
  * A number of minor fixes to WCS capabilities and GetCoverage handling

	
  * Added icelandic language support in the INSPIRE plugin

	
  * Check the [release notes](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20760) for more details

	
  * This release is made in conjunction with GeoTools 12.2


Thanks to Andrea (GeoSolutions), Jody and Kevin (Boundless) for this release


# About GeoServer 2.6


Articles and resources for GeoServer 2.6 series:



	
  * [GeoServer at FOSS4G](http://blog.geoserver.org/2014/10/01/geoserver-at-foss4g/)

	
    * [State of GeoServer and GeoTools 2014](http://vimeo.com/106835755) ([slides](http://www.slideshare.net/jgarnett/state-of-geoserver-geotools-and-friends-2014))




	
  * [Raster Views in GeoServer via the CoverageView concept](http://www.geo-solutions.it/blog/overageview-concept-for-geoserver/) (GeoSolutions)

	
  * [Advanced Raster Projection in GeoServer](http://www.geo-solutions.it/blog/developers-corner-advanced-raster-projection-geoserver/) (GeoSolutions)

	
  * [Supporting Wind Barbs In GeoServer and GeoTools](http://www.geo-solutions.it/blog/developers-corner-supporting-wind-barbs-geoserver-geotools/) (GeoSolutions)

	
  * [GeoServer now supports Vector Footprints for ImageMosaic](http://www.geo-solutions.it/blog/geoserver-supports-footprints-imagemosaic/) (GeoSolutions)

	
  * [2.6.0 announcement](http://blog.geoserver.org/2014/10/03/geoserver-2-6-0-released/) and [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20399)

	
  * [2.6-RC1 announcement](http://blog.geoserver.org/2014/08/18/geoserver-2-6-rc1-released/) and [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?version=20536&styleName=&projectId=10311)

	
  * [2.6-beta announcement](http://blog.geoserver.org/2014/07/24/geoserver-2-6-beta-released/) and [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20172)





