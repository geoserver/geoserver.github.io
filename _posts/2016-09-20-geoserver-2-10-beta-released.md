---
author: tbarsballe
comments: true
date: 2016-09-20 23:02:16+00:00
layout: post
link: http://blog.geoserver.org/2016/09/20/geoserver-2-10-beta-released/
slug: geoserver-2-10-beta-released
title: GeoServer 2.10-beta released
wordpress_id: 2702
---






We are happy to announce the release of [GeoServer 2.10-beta](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-beta/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-beta/geoserver-2.10-beta-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-beta/geoserver-2.10-beta-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-beta/geoserver-2.10-beta.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-beta/geoserver-2.10-beta.exe/download)) along with docs and extensions.

This is a beta release of GeoServer made in conjunction with GeoTools 16-beta.


## Beta Testing


The GeoServer Team has been hard at work to bring you this beta release.

Here is our priorities for testing:



 	
  * Updated[ GeoServer Style Editor](http://docs.geoserver.org/latest/en/user/styling/webadmin/index.html#style-editor)

 	
  * [Module Status](http://docs.geoserver.org/latest/en/user/rest/api/manifests.html#about-status-format) REST endpoint

 	
  * CSS Extension - [Nested rule](http://docs.geoserver.org/latest/en/user/styling/css/nested.html) and [rendering transform](http://docs.geoserver.org/latest/en/user/styling/css/transformation.html) support


We one crititcal known issues to keep in mind when testing:

 	
  * [GEOS-7750](https://osgeo-org.atlassian.net/browse/GEOS-7750) - The WMS and LegendSample beans used in GeoServerTileLayer may provoke a cyclic dependency when Spring beans are loaded. As a consequence **tiled layers may not be loaded and are deleted** by GWC integration. Please back up your data and configuration before testing the GeoServer 2.10-beta with data you care about.


Highlights from the release notes:

 	
  * Add CSS nested rule support

 	
  * Add CSS rendering transform support

 	
  * Add WMTS multi dimensional community module

 	
  * Add WCS 2.0 Demo Requests

 	
  * OL3 Preview in tiled mode supports map wrapping

 	
  * Make JDBCStore compatible with HazelCast Clustering

 	
  * Changes to WMS GetFeatureInfo for coverages:

 	
    * Band names now presented in responses as NCNames for all info_formats (spaces and leading digits replaced with underscores)

 	
    * Support for continuous map wrapping for latitude/longitude projections

 	
    * Support for coverages with native latitude/longitude coordinates and longitudes > 180 degrees East





Also, looking at the GeoTools 16-M0 release notes, we have:

 	
  * Support Azimuthal Equidistant projection

 	
  * Implement Vladimir's Polygon label point algorithim

 	
  * GeoPackage can write to boolean fields


For more information about the what is included in the GeoServer 2.10 release, also refer to the GeoServer 2.10-M0 [release anouncement](http://blog.geoserver.org/2016/08/15/geoserver-2-10-m0-released/).


## 










## About GeoServer 2.10


GeoServer 2.10 is scheduled for October release.





