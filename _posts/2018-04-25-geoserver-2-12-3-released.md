---
author: jgarnett
comments: false
date: 2018-04-25 21:01:11+00:00
layout: post
link: http://blog.geoserver.org/2018/04/25/geoserver-2-12-3-released/
slug: geoserver-2-12-3-released
title: GeoServer 2.12.3 Released
wordpress_id: 2947
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_212
version: 2.12.3
jira_version: 16715
---

We are happy to announce the release of [GeoServer 2.12.3](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.3/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.3/geoserver-2.12.3-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.3/geoserver-2.12.3-war.zip/download), and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.3/geoserver-2.12.3.exe/download)) along with docs and extensions.







This is a maintenance release and a recommend update production systems. This release is made in conjunction with GeoTools 18.3.




Highlights of this release are featured below, for more information please see the release notes ([2.12.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16715),[2.12.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16709), [2.12.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16705) | [2.12.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16703) | [2.12-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16600) | [2.12-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15700)).


## Improvements





 	
  * Improved bounding box reporting in WMS GetCapabilities allowing more entries to be supported when _Output bounding box for every support CRS_ is selected. Bounding boxes are now returned for layer groups as well.

 	
  * NetCDF/GRIB has been improved with a [new setting](http://docs.geoserver.org/latest/en/user/extensions/netcdf-out/index.html#settings) to copy over global attributes when generating NetCDF output




## Bug Fixes





 	
  * WFS 2.0 fix for interaction with startIndex and the total features count

 	
  * CQL filters can now be used with the WMS vector tile output format

 	
  * GeoPackage WPS output corrected to generate y coordinates from bottom left

 	
  * User interface for editing workspace details checks for conflicts with name or namespace URI.

 	
  * GML 3.2 output can now limit the number of decimals used for coordinate output

 	
  * REST management of styles now supports defining a style using POST for CSS, YSLD and MapBox styles (previously this only worked for SLD)

 	
  * WPS output error handling does a better job reporting when Async output format parameters are incorrect.

 	
  * WPS improvements have also been made for the cleanup of temporary folders and output "raw data encoder" (which is often used for image generation).

 	
  * Demo request page does a better job of of reporting authorization failures, and correctly sending credentials for testing service security.

 	
  * GetLegendGraphic fixes to correct line thickness and ensure polygons and points are not cut off.




## Community Updates


For developers building from source our community modules remain a great place to collaborate on new functionality and improvements. This month Nuno Oliveira has added a new community module for the GeoTools MongoDB datastore.


## Security Updates


Please update your production instances of GeoServer to receive the latest security updates and fixes.

If you encounter a security vulnerability in GeoServer, or any other open source software, please take care to report the issue in a [responsible fashion](http://docs.geoserver.org/stable/en/user/introduction/gettinginvolved.html#bug-tracking).









# About GeoServer 2.12 Series


Additional information on the 2.12 series:



 	
  * [State of GeoServer 2.12 ](https://www.slideshare.net/geosolutions/state-of-geoserver-21geoservernodeopts2)(SlideShare)

 	
  * [GeoServer Feature Frenzy](https://www.slideshare.net/jgarnett/geoserver-feature-frenzy-80906586/jgarnett/geoserver-feature-frenzy-80906586) (SlideShare)

 	
  * New [REST API documentation](http://docs.geoserver.org/latest/en/user/rest/index.html#rest)

 	
  * [REST API Code Sprint Results](http://blog.geoserver.org/2017/04/11/rest-api-code-sprint-results/)



