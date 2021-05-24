---
author: jgarnett
comments: false
date: 2019-12-20 14:47:23+00:00
layout: post
link: http://blog.geoserver.org/2019/12/20/geoserver-2-15-4-released/
slug: geoserver-2-15-4-released
title: GeoServer 2.15.4 Released
wordpress_id: 3083
categories:
- Announcements
tags:
- Release
release: release_215_war
version: 2.15.4
jira_version: 16771
---




We are pleased to announce the release of [GeoServer 2.15.4](http://geoserver.org/release/2.15.4/) with downloads ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.4/geoserver-2.15.4-bin.zip/download)|[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.4/geoserver-2.15.4-war.zip/download)), documentation ([html](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.4/geoserver-2.15.4-htmldoc.zip/download)) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.4/extensions/).







This is a maintenance release and is a recommended update for existing installations. This is the last scheduled 2.15 maintenance release and we recommend planning your upgrade to 2.16.







This release is made in conjunction with GeoTools 21.3 and GeoWebCache 1.15.3. Thanks to everyone who contributed to this release.







For more information see the [GeoServer 2.15.4 release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16771).







#### Improvements and Fixes







This release includes a number of improvements, including:







  * Improve ncWMS extension to support time list and time range.
  * Truncate of tiles fixed use of parameters.
  * Upgrade of XStream and Jackson libraries.






A number of fixes are also present:







  * Fix cascading WMTS use of credentials
  * ncWMS extension now respects no-data values.
  * Importer fixed to respect shapefile charset encoding.






### About GeoServer 2.15 Series







Additional information on the 2.15 series:







  * [Layer service settings](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#services-settings) allow WFS, WMS, WPS to be enabled on a layer by layer basis.
  * [GeoFence internal server extension](https://docs.geoserver.org/latest/en/user/extensions/geofence-server/index.html) a new approach to access control
  * Style Editor supports auto-complete using **control-space** shortcut.
  * [SLD REST Service extension](https://docs.geoserver.org/latest/en/user/extensions/sldservice/index.html) supports generation of thematic styles for vector and raster content.
  * WPS vendor operation GetExecution Status and Dismiss, [management of running processes](https://docs.geoserver.org/latest/en/user/services/wps/operations.html).
  * Java 11 can now be used, see [Running on Java 11](https://docs.geoserver.org/latest/en/user/production/java.html#running-on-java-11).
  * JAI-EXT [operations](https://docs.geoserver.org/latest/en/user/configuration/image_processing/index.html#jai-ext) are now enabled by default.
  * Release notes ([2.15.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16771)|[2.15.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16761)|[2.15.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16757)|[2.15.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16753)|[2.15.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16736)|[2.15-RC](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16740)|[2.15-M0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16746))


