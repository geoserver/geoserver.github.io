---
author: bencaradocdavies
comments: true
date: 2016-08-12 02:21:49+00:00
layout: post
link: http://blog.geoserver.org/2016/08/12/geoserver-2-8-5-released/
slug: geoserver-2-8-5-released
title: GeoServer 2.8.5 Released
wordpress_id: 2695
categories:
- Announcements
- Vulnerability
---



The GeoServer team is pleased to announce the release of [GeoServer 2.8.5](http://geoserver.org/release/2.8.5/). Download bundles are provided ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.8.5/geoserver-2.8.5-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.8.5/geoserver-2.8.5-war.zip/download), [dmg](https://sourceforge.net/projects/geoserver/files/GeoServer/2.8.5/geoserver-2.8.5.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.8.5/geoserver-2.8.5.exe/download)) along with documentation and extensions.

GeoServer 2.8.5 is the final maintenance release of the 2.8.x series. This release is made by Ben Caradoc-Davies ([Transient](http://transient.nz/)) in conjunction with [GeoTools 14.5](http://geotoolsnews.blogspot.com/2016/08/geotools-145-released.html) and GeoWebCache 1.8.3. We thank the many contributors who have made this release possible.

The [GeoServer 2.8.5 release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=13200) detail the changes in this release. These include:



 	
  * Fixes for WFS editing failing for geometries in full 3D CRS

 	
  * ColorMap variable substitution now working correctly for multiple layers in a GetMap request

 	
  * Fixed a missing JNA jar in the netcdf-out plugin

 	
  * KML placemarks now being set correctly when KMSCORE=0

 	
  * Support for multivalued xlink:href ClientProperty in app-schema mappings, even without feature chaining

 	
  * Support requiring files to exist for GeoServer startup, to protect against insecure fallback when a data directory on a network share is unavailable










### Security Considerations


This release includes several security enhancements and is a recommended upgrade for production systems:



 	
  * Although we have not been able to reproduce from GeoServer, a remote execution vulnerability has been reported against both the Restlet  and the Apache Commons BeanUtils libraries we use. We have patched our use of these libraries as a preventative measure. We would like to thank Kevin Smith for doing the bulk of the work, and Andrea Aime for providing a patched BeanUtils library addressing these vulnerabilities.

 	
  * Layer security restrictions in CHALLENGE mode were not being correctly applied by embedded GeoWebCache. Thanks to Nick Muerdter for his responsible report of this vulnerability and for submitting a fix (that included a unit test!)

 	
  * Carl Schroedl reported a vulnerability at application startup when working with a data directory on a network file system, a new [configuration option](http://docs.geoserver.org/stable/en/user/datadirectory/setting.html#require-files-to-exist) has been provided to check that the directory exists.  Thanks to Carl for following our responsible disclosure procedure, and to Ben Caradoc-Davies for implementing the new parameter.


If you wish to report a security vulnerability, please visit our website for [instructions on responsible reporting](http://geoserver.org/issues/).


## About GeoServer 2.8





 	
  * [State of GeoServer 2015](http://www.slideshare.net/jgarnett/state-of-geoserver-2015) (FOSS4G)

 	
  * [XEE Vunerability](http://blog.geoserver.org/2015/06/27/geoserver-xee-vulnerability/) (GeoServer)

 	
  * [Remote Execution Vulnerability](http://blog.geoserver.org/2015/10/20/remote-execution-vulnerability/) (GeoServer)

 	
  * [Z ordering features within and across feature types and layers](http://docs.geoserver.org/latest/en/user/styling/sld-extensions/z-order/index.html#z-ordering-features-within-and-across-feature-types-and-layers) (User Manual)

 	
  * [JAI-Ext, the Open Source replacement for Oracle JAI](http://www.geo-solutions.it/blog/developers-corner-jai-ext-the-open-source-replacement-for-oracle-jai/) (GeoSolutions)

 	
  * [Customizable arrow in GeoServer](http://www.geo-solutions.it/blog/customizable-arrow-geoserver/) (GeoSolutions)

 	
  * [PostGIS Curve Support](http://www.geo-solutions.it/blog/postgis-curves-in-geoserver/) (GeoSolutions)

 	
  * [Improved NetCDF/GRIB support in GeoServer](http://www.geo-solutions.it/blog/netcdf-grib-support-geoserver/) (GeoSolutions)

 	
  * Initial [GeoServer 2.8.0 release](http://blog.geoserver.org/2015/09/30/geoserver-2-8-0-released/) announcement  (GeoServer)



