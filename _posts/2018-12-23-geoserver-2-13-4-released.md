---
author: aaime
comments: false
date: 2018-12-23 09:42:56+00:00
layout: post
link: http://blog.geoserver.org/2018/12/23/geoserver-2-13-4-released/
slug: geoserver-2-13-4-released
title: GeoServer 2.13.4 released
wordpress_id: 2986
categories:
- Announcements
tags:
- Release
release: release_213
version: 2.13.4
jira_version: 16741
---



We are happy to announce the release of [GeoServer 2.13.4](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.4/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.4/geoserver-2.13.4-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.4/geoserver-2.13.4-war.zip/download), and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.4/geoserver-2.13.4.exe/download)) along with docs and extensions.

This is a maintenance release recommended for production use (for newer projects please use the 2.14.x series, as this is last community sponsored 2.13.x release).
This release is made in conjunction with GeoTools 19.4 and GeoWebCache 1.13.4.




Highlights of this release are featured below, for more information please see the release notes ([2.13.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16741) | [2.13.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16733) | [2.13.2 ](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16728)| [2.13.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16724) | [2.13.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16722) | [2.13-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16717) | [2.13-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16702)).


### Improvements and Fixes





 	
  * Significant speedup in WMTS capabilities document generation when source data is not in WGS84

 	
  * GeoPackage improvements, speed up raster reading and reprojection, make sure global coverage GeoPackage can be displayed

 	
  * Removed gml:id attribute from GML 3.1 encoding (was added in previous releases by mistake)

 	
  * NetCDF output format improvement, fixing projection coefficients in some cases, make sure data packing takes into account all data slices when calculating linear transformation coefficients

 	
  * WCS 2.0 compliance improvements, DescribeCoverage output schema compliance fixes when using GeoServer extensions, returning correct exception type when subsetting request is out of range on time/elevation/custom dimension axis

 	
  * KML request handling fixes, support for sortBy and CQL filtering on layer groups

 	
  * GWC related fixes, could not modify blobstore configuration without changing its name too, wrong axis order in configuration when saving EPSG:4326 gridset configurations

 	
  * Styling related improvements, cannot read dynamic SLD served by an apache server, SLD 1.1 posted to the REST API resulted in garbled content

 	
  * And various others, please see the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16741) for details




## About GeoServer 2.13 Series


Additional information on the 2.13 series:



 	
  * [Isolated workspaces](http://docs.geoserver.org/latest/en/user/data/webadmin/workspaces.html#isolated-workspaces) (User Guide)

 	
  * [Coverage views from heterogeneous bands](http://docs.geoserver.org/latest/en/user/data/raster/coverageview.html#heterogeneous-coverage-views) (User Guide)

 	
  * [State of GeoServer 2.13](https://www.slideshare.net/jgarnett/state-of-geoserver-213) (slideshare)

 	
  * See the [GeoServer 2.13.0 released](http://blog.geoserver.org/2018/03/20/geoserver-2-13-0-released/) announcement for visual guide to new features



