---
author: jgarnett
comments: false
date: 2019-04-30 13:59:23+00:00
layout: post
link: http://blog.geoserver.org/2019/04/30/geoserver-2-15-1-released/
slug: geoserver-2-15-1-released
title: GeoServer 2.15.1 Released
wordpress_id: 3019
categories:
- Announcements
tags:
- Release
release: release_215_war
version: 2.15.1
jira_version: 16753
---




We are pleased to announce the release of [GeoServer 2.15.1](http://geoserver.org/release/2.15.1/) with downloads ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.1/geoserver-2.15.1-bin.zip/download)|[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.1/geoserver-2.15.1-war.zip/download)|[exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.1/geoserver-2.15.1.exe/download)), documentation ([html](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.1/geoserver-2.15.1-htmldoc.zip/download)|[pdf](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.1/geoserver-2.15.1-user-manual.pdf/download)) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.1/extensions/).







This is a stable release recommended for production. This release is made in conjunction with GeoTools 21.1 and GeoWebCache 1.15.1. Thanks to everyone who contributed to this release.







For more information see the [GeoServer 2.15.1 release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16753).







#### Improvements and Fixes







This release includes a number of fixes and improvements, including:







  * Addressed "potentially malicious String" error encountered when first establishing a session with the web administration application. 
  * Importer fixed to connect to and create PostGIS datastore
  * Fix REST API user creation problem
  * Map preview fix to display projected maps with WMS 1.3.0
  * WCS 2.0.1 metadata fix for GetCapabilities and DescribeCoverage
  * WCS 1.0.0 and WCS 2.0 fixes for elevation and custom dimension use
  * GetFeatureInfo template can now access metadata for raster layers
  * Styling improvements respecting followLine and maxAngleDelta 






### About GeoServer 2.15 Series







Additional information on the 2.15 series:







  * [Layer service settings](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#services-settings) allow WFS, WMS, WPS to be enabled on a layer by layer basis.
  * [GeoFence internal server extension](https://docs.geoserver.org/latest/en/user/extensions/geofence-server/index.html) a new approach to access control
  * Style Editor supports auto-complete using **control-space** shortcut.
  * [SLD REST Service extension](https://docs.geoserver.org/latest/en/user/extensions/sldservice/index.html) supports generation of thematic styles for vector and raster content.
  * WPS vendor operation GetExecutation Status and Dismiss all [management of running processes](https://docs.geoserver.org/latest/en/user/services/wps/operations.html).  
  * Java 11 can now be used, see [Running on Java 11](https://docs.geoserver.org/latest/en/user/production/java.html#running-on-java-11). 
  * JAI-EXT [operations](https://docs.geoserver.org/latest/en/user/configuration/image_processing/index.html#jai-ext) are now enabled by default.
  * Release notes ([2.15.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16753)|[2.15.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16736)|[2.15-RC](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16740)|[2.15-M0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16746))






Java 11 comparability is the result of a successful code-sprint. Thanks to participating organizations ([Boundless](http://boundlessgeo.com/), [GeoSolutions](https://www.geo-solutions.it/), [GeoCat](https://www.geocat.net/), [Astun Technology](https://astuntechnology.com/), [CCRi](https://www.ccri.com/)) and sprint sponsors ([Gaia3D](http://www.gaia3d.com/), [atol](https://www.atolcd.com/), [osgeo:uk](https://uk.osgeo.org/), [Astun Technology](https://astuntechnology.com/)).



