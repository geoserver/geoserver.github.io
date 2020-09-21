---
author: randomorder
comments: true
date: 2016-06-18 13:42:56+00:00
layout: post
link: http://blog.geoserver.org/2016/06/18/geoserver-2-8-4-released/
slug: geoserver-2-8-4-released
title: GeoServer 2.8.4 released
wordpress_id: 2665
categories:
- Announcements
---

The GeoServer team is pleased to announce the release of GeoServer 2.8.4. Download bundles are provided ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.8.4/geoserver-2.8.4-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.8.4/geoserver-2.8.4-war.zip/download), [dmg](https://sourceforge.net/projects/geoserver/files/GeoServer/2.8.4/geoserver-2.8.4.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.8.4/geoserver-2.8.4.exe/download)) along with documentation and extensions.

GeoServer 2.8.4 is the latest stable release of GeoServer and is recommended for production deployment. This release is made in conjunction with [GeoTools 14.4](http://geotoolsnews.blogspot.it/2016/06/geotools-144-released.html). Thanks to all contributors. Fixes and new functionality include:



 	
  * Security fix for a reflected XSS vulnerability

 	
  * Fix for potential out of memory state when rendering lots of very small tiles

 	
  * Fix for an embedded GeoFence issue that caused user settings to be lost after a restart

 	
  * Improved ImageMosaic creation and update speed for databases with many tables

 	
  * Monitoring extension fixes for RemoteUser logging and monitoring hibernate extension causing startup issues to GeoServer

 	
  * CSS styling extension related fix: A bug in CSS to SLD conversion led in some cases to performance issues with the generated SLD

 	
  * PDF printing related fixes to properly render SLD "shape://horline" symbol, prevent invalid polygon generation and avoid potential out of memory state or very large files when handling large outputs with dense hatch fills

 	
  * And much more, see all the 24 tickets resolved in the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=12801)


Thanks to Alessandro Parma ([GeoSolutions](http://www.geo-solutions.it/)) and Andrea Aime ([GeoSolutions](http://www.geo-solutions.it/)) for this release.


# About GeoServer 2.8


Articles, blog posts and presentations:



 	
  * [State of GeoServer 2015](http://www.slideshare.net/jgarnett/state-of-geoserver-2015) (FOSS4G)

 	
  * [XEE Vunerability](http://blog.geoserver.org/2015/06/27/geoserver-xee-vulnerability/) (GeoServer)

 	
  * [Remote Execution Vulnerability](http://blog.geoserver.org/2015/10/20/remote-execution-vulnerability/) (GeoServer)

 	
  * [Z ordering features within and across feature types and layers](http://docs.geoserver.org/latest/en/user/styling/sld-extensions/z-order/index.html#z-ordering-features-within-and-across-feature-types-and-layers) (User Manual)

 	
  * [JAI-Ext, the Open Source replacement for Oracle JAI](http://www.geo-solutions.it/blog/developers-corner-jai-ext-the-open-source-replacement-for-oracle-jai/) (GeoSolutions)

 	
  * [Customizable arrow in GeoServer](http://www.geo-solutions.it/blog/customizable-arrow-geoserver/) (GeoSolutions)

 	
  * [PostGIS Curve Support](http://www.geo-solutions.it/blog/postgis-curves-in-geoserver/) (GeoSolutions)

 	
  * [Improved NetCDF/GRIB support in GeoServer](http://www.geo-solutions.it/blog/netcdf-grib-support-geoserver/) (GeoSolutions)

 	
  * Initial [GeoServer 2.8.0 release](http://blog.geoserver.org/2015/09/30/geoserver-2-8-0-released/) announcement  (GeoServer)


