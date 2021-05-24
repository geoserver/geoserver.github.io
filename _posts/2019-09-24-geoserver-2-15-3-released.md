---
author: aaime
comments: false
date: 2019-09-24 08:01:57+00:00
layout: post
link: http://blog.geoserver.org/2019/09/24/geoserver-2-15-3-released/
slug: geoserver-2-15-3-released
title: GeoServer 2.15.3 released
wordpress_id: 3061
categories:
- Announcements
tags:
- Release
release: release_215_war
version: 2.15.3
jira_version: 16761
---




We are pleased to announce the release of [GeoServer 2.15.3](http://geoserver.org/release/2.15.3/) with downloads ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.3/geoserver-2.15.3-bin.zip/download)|[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.3/geoserver-2.15.3-war.zip/download)), documentation ([html](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.3/geoserver-2.15.3-htmldoc.zip/download)) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.3/extensions/).







This is a maintenance release and is a recommended update for existing installations. This release is made in conjunction with GeoTools 21.3 and GeoWebCache 1.15.3. Thanks to everyone who contributed to this release.







For more information see the [GeoServer 2.15.3 release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16761).







#### Improvements and Fixes







This release includes a number of improvements, including:







  * Enhance mongodb schema generation
  * Allow setting Entity Expansion limit on WFS XML Readers
  * Promote authkey to extension (GSIP-174)
  * Make MongoDB App-Schema schema rebuilder endpoints only rebuild schemas present in mappings.
  * Promote status-monitoring module from Community to Extension
  * Upgrade Jetty to 9.4.18.v20190429






A number of fixes are also present:







  * WMS GetFeatureInfo formats text/html, text/plain, text/xml and application/vnd.ogc.gml (GML2) don't handle time correctly
  * Wrong URL scheme in layer preview (when using HTTPS)
  * GetCapabilities on a single layer fails if a style is duplicated
  * Renaming a layer doesn't update Data Security rules
  * SLD file renamed with REST PUT request when not needed
  * GeoTIFF sources configured with GeoServer 2.14.x might not work in 2.15.x
  * Style editor extension point not working
  * NullPointerException on WFS ComplexGeoJsonWriter Link check
  * Switching from System Status to Modules tab gives an error.
  * Nodata is not made transparent after channelSelect+contrastEnhancement on multibands dataset
  * WFS GeoJSONBuilder limits max nested level to 20






### About GeoServer 2.15 Series







Additional information on the 2.15 series:







  * [Layer service settings](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#services-settings) allow WFS, WMS, WPS to be enabled on a layer by layer basis.
  * [GeoFence internal server extension](https://docs.geoserver.org/latest/en/user/extensions/geofence-server/index.html) a new approach to access control
  * Style Editor supports auto-complete using **control-space** shortcut.
  * [SLD REST Service extension](https://docs.geoserver.org/latest/en/user/extensions/sldservice/index.html) supports generation of thematic styles for vector and raster content.
  * WPS vendor operation GetExecution Status and Dismiss, [management of running processes](https://docs.geoserver.org/latest/en/user/services/wps/operations.html).
  * Java 11 can now be used, see [Running on Java 11](https://docs.geoserver.org/latest/en/user/production/java.html#running-on-java-11).
  * JAI-EXT [operations](https://docs.geoserver.org/latest/en/user/configuration/image_processing/index.html#jai-ext) are now enabled by default.
  * Release notes ( [2.15.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16757)|[2.15.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16753)|[2.15.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16736)|[2.15-RC](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16740)|[2.15-M0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16746))






Java 11 comparability is the result of a successful code-sprint. Thanks to participating organizations ([Boundless](http://boundlessgeo.com/), [GeoSolutions](https://www.geo-solutions.it/), [GeoCat](https://www.geocat.net/), [Astun Technology](https://astuntechnology.com/), [CCRi](https://www.ccri.com/)) and sprint sponsors ([Gaia3D](http://www.gaia3d.com/), [atol](https://www.atolcd.com/), [osgeo:uk](https://uk.osgeo.org/), [Astun Technology](https://astuntechnology.com/)).



