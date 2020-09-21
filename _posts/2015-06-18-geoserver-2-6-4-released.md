---
author: geoserver
comments: true
date: 2015-06-18 20:37:04+00:00
layout: post
link: http://blog.geoserver.org/2015/06/18/geoserver-2-6-4-released/
slug: geoserver-2-6-4-released
title: GeoServer 2.6.4 Released
wordpress_id: 2225
categories:
- Announcements
---

The GeoServer team is pleased to announce the release of [GeoServer 2.6.4](http://geoserver.org/release/2.6.4/). Download bundles are provided ([bin](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.4/geoserver-2.6.4-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.4/geoserver-2.6.4-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.4/geoserver-2.6.4.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.4/geoserver-2.6.4.exe/download)) along with documentation and extensions.

GeoServer 2.6.4 is a maintenance release of GeoServer recommended for  production deployment. This release contains **IMPORTANT SECURITY FIXES** so please upgrade.

Thanks to everyone who took part by contributing fixes, new functionality, and documentation. Notable changes:



	
  * **SECURITY**: [Fixed a serious vulnerability that allowed arbitrary files on the server to be read by crafting a malicious WFS request](https://osgeo-org.atlassian.net/browse/GEOS-7032)

	
  * **SECURITY**: Fixed a defect that permitted WPS service to continue to respond even when disabled

	
  * Oracle JDBC driver (ojdbc14.jar) is no longer included with the Oracle plugin; [ojdbc6.jar or ojdbc7.jar must be obtained from Oracle](http://docs.geoserver.org/2.6.x/en/user/data/database/oracle.html#installing-the-oracle-extension)

	
  * Vendor parameter to specify WMS GetMap interpolation method

	
  * Dynamic raster styling with CQL expression support for color map entries

	
  * User-defined variables in Freemarker templates

	
  * Check the [release notes](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=10159) for more details

	
  * This release is made in conjunction with [GeoTools 12.4](http://geotoolsnews.blogspot.com/2015/06/geotools-124-released.html) and GeoWebCache 1.6.2


Thanks to Ben Caradoc-Davies ([Transient Software Limited](http://transient.nz/)) for this release. Thanks also to Kevin Smith (Boundless) for releasing GeoWebCache 1.6.2 and to Jody Garnett (Boundless) for building the GeoServer 2.6.4 DMG.


## About GeoServer 2.6


Articles and resources for GeoServer 2.6 series:



	
  * [GeoServer at FOSS4G](http://blog.geoserver.org/2014/10/01/geoserver-at-foss4g/)

	
    * [State of GeoServer and GeoTools 2014](http://vimeo.com/106835755) ([slides](http://www.slideshare.net/jgarnett/state-of-geoserver-geotools-and-friends-2014))




	
  * [Raster Views in GeoServer via the CoverageView concept](http://www.geo-solutions.it/blog/overageview-concept-for-geoserver/) (GeoSolutions)

	
  * [Advanced Raster Projection in GeoServer](http://www.geo-solutions.it/blog/developers-corner-advanced-raster-projection-geoserver/) (GeoSolutions)

	
  * [Supporting Wind Barbs In GeoServer and GeoTools](http://www.geo-solutions.it/blog/developers-corner-supporting-wind-barbs-geoserver-geotools/) (GeoSolutions)

	
  * [GeoServer now supports Vector Footprints for ImageMosaic](http://www.geo-solutions.it/blog/geoserver-supports-footprints-imagemosaic/) (GeoSolutions)

	
  * [2.6.3 announcement](http://blog.geoserver.org/2015/04/20/geoserver-2-6-3-released/) and [change log](https://github.com/geoserver/geoserver/wiki/GeoServer-2.6.3-changelog)

	
  * [2.6.2 announcement](http://blog.geoserver.org/2015/01/20/geoserver-2-6-2-released/)

	
  * [2.6.1 announcement](http://blog.geoserver.org/2014/11/18/geoserver-2-6-1-released/)

	
  * [2.6.0 announcement](http://blog.geoserver.org/2014/10/03/geoserver-2-6-0-released/)

	
  * [2.6-RC1 announcement](http://blog.geoserver.org/2014/08/18/geoserver-2-6-rc1-released/)

	
  * [2.6-beta announcement](http://blog.geoserver.org/2014/07/24/geoserver-2-6-beta-released/)


