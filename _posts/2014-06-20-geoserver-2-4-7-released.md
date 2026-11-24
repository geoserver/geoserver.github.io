---
author: geoserver
comments: true
date: 2014-06-20 01:18:05+00:00
layout: post
link: http://blog.geoserver.org/2014/06/19/geoserver-2-4-7-released/
slug: geoserver-2-4-7-released
title: GeoServer 2.4.7 Released
wordpress_id: 1890
categories:
- Announcements
---

The GeoServer team is pleased to announce the maintenance release of GeoServer 2.4.7: 



	
  * [GeoServer 2.4.7 download page](http://geoserver.org/release/2.4.7/)


This release is made in conjunction with [GeoTools 10.7](http://geotoolsnews.blogspot.com.au/2014/04/geotools-107-released.html).

The [GeoServer 2.4.7 Release Notes](#release-notes) detail changes in this maintenance release, which include:



	
  * Rendering and referencing improvements for both polar projections and whole earth projections.

	
  * Rendering fixes for multi-line labels

	
  * UI fix for keeping SLD files separated during editing

	
  * Security fixes for those using CAS security

	
  * Using WPS and workspaces? This release has a few fixes for you.

	
  * See also [GeoTools 10.7 Release Notes](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOT%20AND%20fixVersion%3D10.7).



Now is a great time to upgrade to GeoServer 2.5. If you need more time there is a final 2.4 maintenance release scheduled for August (as part of our [extended release schedule]({% post_url 2014-02-27-extended-release-schedule %}).)

## Release notes

Improvement:

* [GEOS-6465](https://osgeo-org.atlassian.net/browse/GEOS-6465) autoWrap should count "(" as being within the same string

Bug:

* [GEOS-4943](https://osgeo-org.atlassian.net/browse/GEOS-4943) /geoserver/accessDenied.jsp not found
* [GEOS-5545](https://osgeo-org.atlassian.net/browse/GEOS-5545) Two different SLD's that seem to be connected
* [GEOS-6109](https://osgeo-org.atlassian.net/browse/GEOS-6109) CAS login request exposes internal server URL
* [GEOS-6110](https://osgeo-org.atlassian.net/browse/GEOS-6110) CAS logout request is incorrect
* [GEOS-6414](https://osgeo-org.atlassian.net/browse/GEOS-6414) WMS-T time range query incorrect
* [GEOS-6440](https://osgeo-org.atlassian.net/browse/GEOS-6440) Advanced projection handling is not enabled in WMS 1.3
* [GEOS-6471](https://osgeo-org.atlassian.net/browse/GEOS-6471) GetFeatureWithLock expiry is not parsed when using WFS 1.1 POST requests
* [GEOS-6493](https://osgeo-org.atlassian.net/browse/GEOS-6493) WFS GetFeature with feature bounds enabled can leak connections
* [GEOS-6501](https://osgeo-org.atlassian.net/browse/GEOS-6501) Links in workspace specific WPS GetCapabilities are incorrect
* [GEOS-6503](https://osgeo-org.atlassian.net/browse/GEOS-6503) WPS won't work with  workspace specific urls, a 404 is returned
* [GEOS-6504](https://osgeo-org.atlassian.net/browse/GEOS-6504) If one of the top level service configuration files fails to load, the whole startup fails

Task:

* [GEOS-6537](https://osgeo-org.atlassian.net/browse/GEOS-6537) Improve documentation about JNDI connection pool configuration
