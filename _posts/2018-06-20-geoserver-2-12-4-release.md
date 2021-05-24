---
author: iant
comments: false
date: 2018-06-20 08:44:07+00:00
layout: post
link: http://blog.geoserver.org/2018/06/20/geoserver-2-12-4-release/
slug: geoserver-2-12-4-release
title: GeoServer 2.12.4 Release
wordpress_id: 2951
categories:
- Announcements
tags:
- Release
release: release_212
version: 2.12.4
jira_version: 16726
---

We are happy to announce the release of [GeoServer 2.12.4](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.4/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.4/geoserver-2.12.4-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.4/geoserver-2.12.4-war.zip/download), and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.4/geoserver-2.12.4.exe/download)) along with docs and extensions.







This is a maintenance release and a recommend update production systems. This release is made in conjunction with GeoTools 18.4.




Highlights of this release are featured below, for more information please see the release notes ([2.12.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16726), [2.12.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16715),[2.12.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16709), [2.12.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16705) | [2.12.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16703) | [2.12-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16600) | [2.12-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15700)).


## Improvements





 	
  * Add forceLabels=on in the style editor map legend to help users,

 	
  * Remove language warnings during Windows setup compilation and remove 'work' folder when uninstalling on Windows

 	
  * Move MongoDB community module to supported status




## Bug Fixes





 	
  * Response time of WMS 1.3.0 significantly higher than vs WMS 1.x.x on systems whose axis in north/east order

 	
  * Exception with NULL values with AggregateProcess

 	
  * Style with Interpolate function causes NullPointerException on GetLegendGraphic

 	
  * WFS with startIndex doesn't return some results

 	
  * Vector identifying feature info uses an undocumented system variable to set the default search area

 	
  * Removing extensions with own configuration bits may cause GeoServer not to start up anymore

 	
  * Windows Installation issue - upgrading GeoServer results in corrupt data_dir

 	
  * Class java.util.Map$Entry is not whitelisted for XML parsing.

 	
  * Add WMS GetMap and GetFeatureInfo tests for App-Schema MongoDB integration

 	
  * CatalogRepository cannot find a store by name, if the store has just been added

 	
  * WCS 1.0.0 generates wrong links in GetCapabilities

 	
  * CatalogRepository should return a null on store not found, instead it throws a RuntimeException

 	
  * Layer page will only show up to 25 bands, regardless of the actual set of bands available

 	
  * Undocumented GDAL 2.3.0 CSV output geometry column name change breaks WPSOgrTest




## Security Updates


Please update your production instances of GeoServer to receive the latest security updates and fixes.

If you encounter a security vulnerability in GeoServer, or any other open source software, please take care to report the issue in a [responsible fashion](http://docs.geoserver.org/stable/en/user/introduction/gettinginvolved.html#bug-tracking).









# About GeoServer 2.12 Series


Additional information on the 2.12 series:



 	
  * [State of GeoServer 2.12 ](https://www.slideshare.net/geosolutions/state-of-geoserver-21geoservernodeopts2)(SlideShare)

 	
  * [GeoServer Feature Frenzy](https://www.slideshare.net/jgarnett/geoserver-feature-frenzy-80906586/jgarnett/geoserver-feature-frenzy-80906586) (SlideShare)

 	
  * New [REST API documentation](http://docs.geoserver.org/latest/en/user/rest/index.html#rest)

 	
  * [REST API Code Sprint Results](http://blog.geoserver.org/2017/04/11/rest-api-code-sprint-results/)



