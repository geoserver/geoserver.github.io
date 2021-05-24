---
author: tbarsballe
comments: false
date: 2019-06-28 21:32:15+00:00
layout: post
link: http://blog.geoserver.org/2019/06/28/geoserver-2-15-1-released-2/
slug: geoserver-2-15-1-released-2
title: GeoServer 2.15.2 Released
wordpress_id: 3027
categories:
- Announcements
tags:
- Release
release: release_215_war
version: 2.15.2
jira_version: 16757
---




We are pleased to announce the release of [GeoServer 2.15.2](http://geoserver.org/release/2.15.2/) with downloads ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.2/geoserver-2.15.2-bin.zip/download)|[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.2/geoserver-2.15.2-war.zip/download)), documentation ([html](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.2/geoserver-2.15.2-htmldoc.zip/download)) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.2/extensions/).







This is a stable release recommended for production. This release is made in conjunction with GeoTools 21.2 and GeoWebCache 1.15.2. Thanks to everyone who contributed to this release.







For more information see the [GeoServer 2.15.2 release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16757).







#### Improvements and Fixes







This release includes a number of fixes and improvements, including:







  * Upgrade jackson to 2.9.9
  * Upgrade spring-security-oauth2 version from 2.0.11 to 2.0.16
  * Parameter Extractor plugin cannot mangle URL correctly if Monitor plugin is installed
  * Fix warning message "Unable to find property 'format.wfs.DXF' for preview component"
  * Integrated GWC fails to seed layers if any data security is configured
  * WCS 2.0 scaling policies do not account for scaling factor already applied during read (due to subsampling and overview)
  * Unresolvable Spring circular reference on Solr module
  * REST exception handler and controllers do not always set the response content type
  * Advanced Projection Handling can generate vertical gaps in output images when reprojecting
  * Parameter Extractor plugin prevents the Monitor plugin to log requests
  * WMTS multidimensional, support bboxes spanning the dateline






### About GeoServer 2.15 Series







Additional information on the 2.15 series:







  * [Layer service settings](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#services-settings) allow WFS, WMS, WPS to be enabled on a layer by layer basis.
  * [GeoFence internal server extension](https://docs.geoserver.org/latest/en/user/extensions/geofence-server/index.html) a new approach to access control
  * Style Editor supports auto-complete using **control-space** shortcut.
  * [SLD REST Service extension](https://docs.geoserver.org/latest/en/user/extensions/sldservice/index.html) supports generation of thematic styles for vector and raster content.
  * WPS vendor operation GetExecutation Status and Dismiss all [management of running processes](https://docs.geoserver.org/latest/en/user/services/wps/operations.html).
  * Java 11 can now be used, see [Running on Java 11](https://docs.geoserver.org/latest/en/user/production/java.html#running-on-java-11).
  * JAI-EXT [operations](https://docs.geoserver.org/latest/en/user/configuration/image_processing/index.html#jai-ext) are now enabled by default.
  * Release notes ( [2.15.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16757)|[2.15.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16753)|[2.15.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16736)|[2.15-RC](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16740)|[2.15-M0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16746))






Java 11 comparability is the result of a successful code-sprint. Thanks to participating organizations ([Boundless](http://boundlessgeo.com/), [GeoSolutions](https://www.geo-solutions.it/), [GeoCat](https://www.geocat.net/), [Astun Technology](https://astuntechnology.com/), [CCRi](https://www.ccri.com/)) and sprint sponsors ([Gaia3D](http://www.gaia3d.com/), [atol](https://www.atolcd.com/), [osgeo:uk](https://uk.osgeo.org/), [Astun Technology](https://astuntechnology.com/)).



