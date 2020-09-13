---
author: tbarsballe
comments: true
date: 2016-08-15 18:35:53+00:00
layout: post
link: http://blog.geoserver.org/2016/08/15/geoserver-2-10-m0-released/
slug: geoserver-2-10-m0-released
title: GeoServer 2.10-M0 Released
wordpress_id: 2698
---



We are happy to announce the release of [GeoServer 2.10-M0](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-M0/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-M0/geoserver-2.10-M0-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-M0/geoserver-2.10-M0-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-M0/geoserver-2.10-M0.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-M0/geoserver-2.10-M0.exe/download)) along with docs and extensions.

This is a milestone release of GeoServer made in conjunction with GeoTools 16-M0.

We have both new features and a number of key “under the hood” changes to GeoServer. This technology preview is made available for your evaluation and feedback and is not intended for production.

Highlights from the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=13102):



 	
  * Resource Browser (ResourceStore GUI)

 	
  * LDAP UserGroupService

 	
  * Add WMTS web admin page

 	
  * Allow WMTS service requests per workspace (virtual service)

 	
  * Allow the Wicket UI to show a Server Busy page when updating the configuration instead of locking the server

 	
  * Control over execution time separate to total queuing and execution time

 	
  * Fix Windows exe installer failure to start GeoServer

 	
  * Can't delete Default Cached Gridsets

 	
  * Add support for dynamically choosing jpeg or png compression based on output contents


Also, looking at the GeoTools 16-M0 release notes, we have:

 	
  * Upgrade to NetCDF-Java 4.6.6, including support for NetCDF rotated pole projection

 	
  * Allows ImagePyramid supporting multiple Coverages

 	
  * The old wfs module has now been replaced with the wfs-ng module




## Security Considerations


This release includes several security enhancements (which are also included in the recent GeoServer [2.8.5](http://blog.geoserver.org/2016/08/12/geoserver-2-8-5-released/) and [2.9.1](http://blog.geoserver.org/2016/08/05/geoserver-2-9-1-released/) releases



 	
  * Although we have not been able to reproduce from GeoServer, a remote execution vulnerability has been reported against both the Restlet  and the Apache Commons BeanUtils libraries we use. We have patched our use of these libraries as a preventative measure. We would like to thank Kevin Smith for doing the bulk of the work, and Andrea Aime for providing a patched BeanUtils library addressing these vulnerabilities.

 	
  * Layer security restrictions in CHALLENGE mode were not being correctly applied by embedded GeoWebCache. Thanks to Nick Muerdter for his responsible report of this vulnerability and for submitting a fix (that included a unit test!)

 	
  * Carl Schroedl reported a vulnerability at application startup when working with a data directory on a network file system, a new [configuration option](http://docs.geoserver.org/stable/en/user/datadirectory/setting.html#require-files-to-exist) has been provided to check that the directory exists.  Thanks to Carl for following our responsible disclosure procedure, and to Ben Caradoc-Davies for implementing the new parameter.


If you wish to report a security vulnerability, please visit our website for [instructions on responsible reporting](http://geoserver.org/issues/).






## Style Page


The GeoServer Style page has been upgraded to include several features from the CSS Styles page (part of the CSS extension). The new GeoServer style page includes:



 	
  * Updated Style Page layout

 	
  * Style - Layer Association editor

 	
  * Layer Preview

 	
  * Layer Attribute Preview







## About GeoServer 2.10


GeoServer 2.10 is scheduled for October release.


