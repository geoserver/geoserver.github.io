---
author: geoserver
comments: true
date: 2015-04-20 16:37:46+00:00
layout: post
link: http://blog.geoserver.org/2015/04/20/geoserver-2-6-3-released/
slug: geoserver-2-6-3-released
title: GeoServer 2.6.3 released
wordpress_id: 2199
categories:
- Announcements
---

The GeoServer team is happy to announce the release of [GeoServer 2.6.3](http://geoserver.org/release/2.6.3/). Download bundles are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.3/geoserver-2.6.3-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.3/geoserver-2.6.3-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.3/geoserver-2.6.3.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.3/geoserver-2.6.3.exe/download))  along with documentation and extensions.

GeoServer 2.6.3 is a maintenance release of GeoServer recommended for production deployment. Thanks to everyone taking part, submitting fixes and new functionality:



	
  * The WPS download community module is now available on the 2.6.x branch too

	
  * Some WPS fixes related to requests not including the response form

	
  * Fixed layer naming regression that prevented non XML valid names to be used for coverages (care on naming is still advised, different protocols have different requirements, check the ones you are using)

	
  * Some WFS 2.0 join related fixes

	
  * Speed up generation of JSON files when the native CRS is EPSG:900913

	
  * Avoid leaks of commons-httpclient pools (which in turn can lead to a native thread leak)

	
  * Check the [release notes](https://github.com/geoserver/geoserver/wiki/GeoServer-2.6.3-changelog) for more details

	
  * This release is made in conjunction with GeoTools 12.3


Thanks to Andrea (GeoSolutions), Jody (Boundless) for this release


# About GeoServer 2.6


Articles and resources for GeoServer 2.6 series:



	
  * [GeoServer at FOSS4G](http://blog.geoserver.org/2014/10/01/geoserver-at-foss4g/)

	
    * [State of GeoServer and GeoTools 2014](http://vimeo.com/106835755) ([slides](http://www.slideshare.net/jgarnett/state-of-geoserver-geotools-and-friends-2014))




	
  * [Raster Views in GeoServer via the CoverageView concept](http://www.geo-solutions.it/blog/overageview-concept-for-geoserver/) (GeoSolutions)

	
  * [Advanced Raster Projection in GeoServer](http://www.geo-solutions.it/blog/developers-corner-advanced-raster-projection-geoserver/) (GeoSolutions)

	
  * [Supporting Wind Barbs In GeoServer and GeoTools](http://www.geo-solutions.it/blog/developers-corner-supporting-wind-barbs-geoserver-geotools/) (GeoSolutions)

	
  * [GeoServer now supports Vector Footprints for ImageMosaic](http://www.geo-solutions.it/blog/geoserver-supports-footprints-imagemosaic/) (GeoSolutions)

	
  * [2.6.2 announcement](http://blog.geoserver.org/2015/01/20/geoserver-2-6-2-released/) and [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20760)

	
  * [2.6.1 announcement](http://blog.geoserver.org/2014/11/18/geoserver-2-6-1-released/) and [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20651)

	
  * [2.6.0 announcement](http://blog.geoserver.org/2014/10/03/geoserver-2-6-0-released/) and [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20399)

	
  * [2.6-RC1 announcement](http://blog.geoserver.org/2014/08/18/geoserver-2-6-rc1-released/) and [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?version=20536&styleName=&projectId=10311)

	
  * [2.6-beta announcement](http://blog.geoserver.org/2014/07/24/geoserver-2-6-beta-released/) and [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20172)





