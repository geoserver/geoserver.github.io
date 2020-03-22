---
author: iant
comments: false
date: 2020-02-24 10:18:19+00:00
layout: post
link: http://blog.geoserver.org/2020/02/24/geoserver-2-15-5-released/
slug: geoserver-2-15-5-released
title: GeoServer 2.15.5 Released
wordpress_id: 3094
---




We are pleased to announce the release of [GeoServer 2.15.5](http://geoserver.org/release/2.15.5/) with downloads ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.5/geoserver-2.15.5-bin.zip/download)|[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.5/geoserver-2.15.5-war.zip/download)), documentation ([html](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.5/geoserver-2.15.5-htmldoc.zip/download)) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.5/extensions/).







This is a maintenance release and is a recommended update for existing installations. This is the final scheduled 2.15 maintenance release and we recommend planning your upgrade to 2.16.







This release is made in conjunction with GeoTools 21.5 and GeoWebCache 1.15.5. Thanks to everyone who contributed to this release.







For more information see the [GeoServer 2.15.5 release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16775).







#### Improvements and Fixes







This release includes a number of improvements, including:







  * Improve ncWMS extension to support time list and time range.
  * Truncate of tiles fixed use of parameters.
  * Upgrade of XStream and Jackson libraries.






A number of fixes are also present:







  * [[GEOS-8940](https://osgeo-org.atlassian.net/browse/GEOS-8940)] - Tile Layers page layer names bring to the "Publishing" tab by default
  * [[GEOS-9375](https://osgeo-org.atlassian.net/browse/GEOS-9375)] - WCS 2.0 scalefactor=0 can cause excess memory usage
  * [[GEOS-9428](https://osgeo-org.atlassian.net/browse/GEOS-9428)] - Authkey role service filters broken on 2.16+
  * [[GEOS-9431](https://osgeo-org.atlassian.net/browse/GEOS-9431)] - Integrated GWC does not kick in when making request not qualified by workspace
  * [[GEOS-9484](https://osgeo-org.atlassian.net/browse/GEOS-9484)] - ADMIN_ROLE is assigned by default if no role is returned for a user inside Web Service Body Response
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
  * Release notes ( [2.15.5](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16775) | [2.15.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16771)|[2.15.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16761)|[2.15.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16757)|[2.15.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16753)|[2.15.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16736)|[2.15-RC](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16740)|[2.15-M0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16746))


