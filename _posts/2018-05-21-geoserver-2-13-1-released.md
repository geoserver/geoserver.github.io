---
author: tbarsballe
comments: false
date: 2018-05-21 20:07:10+00:00
layout: post
link: http://blog.geoserver.org/2018/05/21/geoserver-2-13-1-released/
slug: geoserver-2-13-1-released
title: GeoServer 2.13.1 Released
wordpress_id: 2949
categories:
- Announcements
tags:
- Release
release: release_213
version: 2.13.1
jira_version: 16724
---



We are happy to announce the release of [GeoServer 2.13.1](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.1/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.1/geoserver-2.13.1-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.1/geoserver-2.13.1-war.zip/download), and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13.1/geoserver-2.13.1.exe/download)) along with docs and extensions.

This is a stable release recommended for production use. This release is made in conjunction with GeoTools 19.1 and GeoWebCache 1.13.1.




Highlights of this release are featured below, for more information please see the release notes ([2.13.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16724) | [2.13.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16722) | [2.13-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16717) | [2.13-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16702)):


## New Features and Improvements





 	
  * MongoDB community module moved to extension

 	
  * Support PNG/JPEG WPS Downloads

 	
  * Allow self joining GetFeature without aliases

 	
  * Add support for priority in control-flow bounded queues

 	
  * Hibernate Monitoring extension moved to a community module




## Bug Fixes





 	
  * WCS 1.0.0 generates wrong links in GetCapabilities

 	
  * WFS 2.0 capabilities report transaction support even if the service level is not configured as such

 	
  * WPSResourceManager cleanup is not deleting temporary subfolders (only files)

 	
  * GeoServer in CITE compliance mode fails to validate an empty LockFeature request

 	
  * WMS 1.3 GetMap request significantly slower than WMS 1.1.0 since GeoServer 2.11.4

 	
  * Import objects cannot be deleted when in COMPLETE state

 	
  * Style with Interpolate function causes NullPointerException on GetLegendGraphic

 	
  * Windows Installation issue - upgrading GeoServer results in corrupt data_dir

 	
  * Windows Installer: Remove 'work' folder when uninstalling



