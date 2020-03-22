---
author: dtucker
comments: true
date: 2016-08-05 00:33:20+00:00
layout: post
link: http://blog.geoserver.org/2016/08/05/geoserver-2-9-1-released/
slug: geoserver-2-9-1-released
title: GeoServer 2.9.1 Released
wordpress_id: 2689
---

The GeoServer team is pleased to announce the release of GeoServer 2.9.1. Download bundles are provided ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.1/geoserver-2.9.1-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.1/geoserver-2.9.1-war.zip/download), [dmg](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.1/geoserver-2.9.1.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9.1/geoserver-2.9.1.exe/download)) along with documentation and extensions.

GeoServer 2.9.1 is the latest stable release of GeoServer and is recommended for production deployment. This release is made in conjunction with GeoTools 15.1 and GeoWebCache 1.9.1. Thanks to all contributors. Fixes and new functionality include:



 	
  * Fixes for WFS editing failing for geometries in full 3D CRS

 	
  * ColorMap variable substitution now working correctly for multiple layers in a GetMap request

 	
  * PDF printing fixed to properly render SLD “shape://horline” symbol, prevent invalid polygon generation, out of memory errors, and large file generation.

 	
  * Integrated GeoFence DB path is now set correctly in Windows.

 	
  * KML placemarks now being set correctly when KMSCORE=0

 	
  * Support for rotated pole projection NetCDF and GRIB2 files, including the native GRIB2 file format used by the [NOAA Rapid Refresh (RAPv3) weather forecast model](http://rapidrefresh.noaa.gov/)

 	
  * Support for multivalued xlink:href ClientProperty in app-schema mappings

 	
  * Support requiring files to exist for GeoServer startup, to protect against insecure fallback when a data directory on a network share is unavailable

 	
  * And much more, see all the tickets resolved in the [release notes](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=13001)


This release has been made by Devon Tucker (Boundless) with help and encouragement from the GeoServer community.


## Security Considerations


This release includes several security enhancements and is a recommended upgrade for production systems:



 	
  * Although we have not been able to reproduce from GeoServer, a remote execution vulnerability has been reported against both the Restlet  and the Apache Commons BeanUtils libraries we use. We have patched our use of these libraries as a preventative measure. We would like to thank Kevin Smith for doing the bulk of the work, and Andrea Aime for providing a patched BeanUtils library addressing these vulnerabilities.

 	
  * Layer security restrictions in CHALLENGE mode were not being correctly applied by embedded GeoWebCache. Thanks to Nick Muerdter for his responsible report of this vulnerability and for submitting a fix (that included a unit test!)

 	
  * Carl Schroedl reported a vulnerability at application startup when working with a data directory on a network file system, a new [configuration option](http://docs.geoserver.org/stable/en/user/datadirectory/setting.html#require-files-to-exist) has been provided to check that the directory exists.  Thanks to Carl for following our responsible disclosure procedure, and to Ben Caradoc-Davies for implementing the new parameter.


If you wish to report a security vulnerability, please visit our website for [instructions on responsible reporting](http://geoserver.org/issues/).


## About GeoServer 2.9


Articles, docs, blog posts and presentations:



 	
  * Lots of goodies in the original [2.9.0 announcement](http://blog.geoserver.org/2016/05/30/geoserver-2-9-0-released/) (GeoServer Blog)

 	
  * Results of our [Bug Stomp Mini Code Sprint](http://blog.geoserver.org/2016/07/26/online-geoserver-bug-stomp-july-2016-results/) in July (GeoServer blog)

 	
  * Internals [upgrade to spring-4](https://github.com/geoserver/geoserver/wiki/Spring-4-Upgrade) for Java 8 compatibility (User Guide)

 	
  * [GeoServer code sprint success](http://blog.geoserver.org/2016/01/25/geoserver-code-sprint-success/) and [wicket migration code sprint](https://github.com/geoserver/geoserver/wiki/Wicket-migration-code-sprint) (GeoServer Blog)

 	
  * [GeoServer Plugin for QGIS](http://blog.geoserver.org/2015/12/23/geoserver-explorer-plugin-for-qgis/) (Boundless)

 	
  * [Simplify complex feature mappings setup with HALE](http://www.geo-solutions.it/blog/inspire-support-in-geoserver-made-easy-with-hale/) (GeoSolutions)

 	
  * [REST management of Resources](http://docs.geoserver.org/stable/en/user/rest/api/resources.html) (User Guide)


