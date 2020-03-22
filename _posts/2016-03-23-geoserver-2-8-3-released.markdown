---
author: aaime
comments: true
date: 2016-03-23 10:16:20+00:00
layout: post
link: http://blog.geoserver.org/2016/03/23/geoserver-2-8-3-released/
slug: geoserver-2-8-3-released
title: GeoServer 2.8.3 released
wordpress_id: 2629
categories:
- Announcements
tags:
- release
- stable
---

The GeoServer team is pleased to announce the release of [GeoServer 2.8.3](http://geoserver.org/release/2.8.3/). Download bundles are provided ([bin](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8.3/geoserver-2.8.3-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8.3/geoserver-2.8.3-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8.3/geoserver-2.8.3.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8.3/geoserver-2.8.3.exe/download)) along with documentation and extensions.

GeoServer 2.8.3 is the latest stable release of GeoServer and is recommended for production deployment. This release is made in conjunction with [GeoTools 14.3](http://geotoolsnews.blogspot.ca/2016/03/geotools-143-released.html). Thanks to all contributors. Fixes and new functionality include:



 	
  * A few security subsystem related fixed, DescribeFeatureType and layer preview now works with mixed security mode, new layer groups can be edited when using GeoFence, mixing layer groups and layers with other styles in a GetMap request now works with GeoFence too, it's possible to access workspace specific services when security only allows access to some layers of it (but not the full workspace), embedded GWC can now serve layer groups when "data security" is enabled

 	
  * WFS cascading related fixes, the WFS store does not get disabled on restart anymore, and can handle straight line elements embedded in a curve container,

 	
  * WFS server received GML3 encoding fixes for geometries with 3D coordinates and pure geometry collections

 	
  * Fixed regression with configuration of SQL Views having multiple geometry fields

 	
  * WPS can now be enabled/disabled per workspace properly

 	
  * And much more, see all the 34 tickets resolved in the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=12401)


Thanks to Andrea Aime ([GeoSolutions](http://www.geo-solutions.it/)) for this release.


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


