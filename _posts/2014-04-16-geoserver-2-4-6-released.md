---
author: geoserver
comments: true
date: 2014-04-16 06:45:53+00:00
layout: post
link: http://blog.geoserver.org/2014/04/16/geoserver-2-4-6-released/
slug: geoserver-2-4-6-released
title: GeoServer 2.4.6 Released
wordpress_id: 1853
categories:
- Announcements
---

The GeoServer team is pleased to announce the release of GeoServer 2.4.6: 



	
  * [GeoServer 2.4.6 download page](/release/2.4.6/)


This release is made in conjunction with [GeoTools 10.6](http://geotoolsnews.blogspot.com.au/2014/04/geotools-106-released.html).

The [GeoServer 2.4.6 Release Notes](#release-notes) detail changes in this maintenance release, which include:



	
  * Improved importer support for Oracle

	
  * Better labelling of top and bottom layers in groups

	
  * Demos now honour proxy base URL

	
  * Fixes for KML LookAt, time and elevation support, and a resource leak

	
  * Logging and documentation improvements


See also changes in the [GeoTools 10.6 Release Notes](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOT%20AND%20fixVersion%3D10.6).

Now is a good time to plan your upgrade to the 2.5 series. Our [extended release schedule]({% post_url 2014-02-27-extended-release-schedule %}) provides six month maintenance window allowing you to upgrade when ready.

## Release notes

Improvement:

* [GEOS-5550](https://osgeo-org.atlassian.net/browse/GEOS-5550) Top/Bottom statement on Layers Group
* [GEOS-6408](https://osgeo-org.atlassian.net/browse/GEOS-6408) Provide better logging when required to fall back on embedded data directory

Bug:

* [GEOS-5511](https://osgeo-org.atlassian.net/browse/GEOS-5511) Help icons on various GWC pages do nothing
* [GEOS-5532](https://osgeo-org.atlassian.net/browse/GEOS-5532) Renaming workspaces doesn't translate over to Tile Caches
* [GEOS-6114](https://osgeo-org.atlassian.net/browse/GEOS-6114) Request URL in Demo Requests exposes internal server URL
* [GEOS-6320](https://osgeo-org.atlassian.net/browse/GEOS-6320) When migrating layergroups from 2.3.x Web Admin UI can fail
* [GEOS-6373](https://osgeo-org.atlassian.net/browse/GEOS-6373) Persisters fails writing temporary file
* [GEOS-6381](https://osgeo-org.atlassian.net/browse/GEOS-6381) Missing user roles if using Authkey Authentication Filter
* [GEOS-6391](https://osgeo-org.atlassian.net/browse/GEOS-6391) Unable to get 5x5 test coverage when configuring a layer with footprint in some cases.
* [GEOS-6410](https://osgeo-org.atlassian.net/browse/GEOS-6410) LookAt value in SimpleNetworkLinkBuilder not set correctly
* [GEOS-6411](https://osgeo-org.atlassian.net/browse/GEOS-6411) Time and elevation parameter is not passed in KML export
* [GEOS-6413](https://osgeo-org.atlassian.net/browse/GEOS-6413) The new KML encoder can leak unclosed feature iterators
* [GEOS-6424](https://osgeo-org.atlassian.net/browse/GEOS-6424) Importer fails to import into Oracle data in geographic coordinates
* [GEOS-6448](https://osgeo-org.atlassian.net/browse/GEOS-6448) WPS RangeLookupTest Java 7 Failure
* [GEOS-6453](https://osgeo-org.atlassian.net/browse/GEOS-6453) ImageMosaic regression - WMS requests take forever to serve

Task:

* [GEOS-3662](https://osgeo-org.atlassian.net/browse/GEOS-3662) Documentation for jp2kak extension
* [GEOS-6393](https://osgeo-org.atlassian.net/browse/GEOS-6393) Addition of documentation about Footprint management
