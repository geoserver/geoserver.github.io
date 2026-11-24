---
author: geoserver
comments: true
date: 2014-08-18 21:07:09+00:00
layout: post
link: http://blog.geoserver.org/2014/08/18/geoserver-2-4-8-released/
slug: geoserver-2-4-8-released
title: GeoServer 2.4.8 Released
wordpress_id: 1989
categories:
- Announcements
---

The GeoServer team is pleased to announce the final maintenance release of the GeoServer 2.4 serieis.

You can download GeoServer 2.4.8 from our new website:



	
  * [GeoServer 2.4.8 download page](http://geoserver.org/release/2.4.8/)


The [GeoServer 2.4.8 Release Notes](#release-notes) detail a small number of changes in this final maintenance release:



	
  * Performance: Avoid full namespace scan for GetFeature requests

	
  * WPS fixes including a new PagedUnique process

	
  * Fix for REST management of SLD files

	
  * Fix for working with JBoss and Oracle via JNDI

	
  * This release is made in conjunction with [GeoTools 10.8](http://geotoolsnews.blogspot.ca/2014/08/geotools-108-released.html) (see also [GeoTools 10.8 Release Notes](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOT%20AND%20fixVersion%3D10.8))


We trust you have enjoyed GeoServer 2.4. All users are encouraged to take opportunity to migrate to GeoServer 2.5.

## Release notes

New Feature:

* [GEOS-6530](https://osgeo-org.atlassian.net/browse/GEOS-6530) WPS PagedUnique Process

Improvement:

* [GEOS-6597](https://osgeo-org.atlassian.net/browse/GEOS-6597) Avoid full namespace scan for GetFeature requests

Bug:

* [GEOS-6489](https://osgeo-org.atlassian.net/browse/GEOS-6489) Reading SLD by REST changes attribute value breaks geoserver on update
* [GEOS-6510](https://osgeo-org.atlassian.net/browse/GEOS-6510) Error in enabling WPS service in workspace
* [GEOS-6529](https://osgeo-org.atlassian.net/browse/GEOS-6529) NullPointerException in AdvancedDispatchFilter, seen when geoserver-monitoring included
* [GEOS-6575](https://osgeo-org.atlassian.net/browse/GEOS-6575) Rapid Concurrent REST usage can invalidate DataStore still being used
* [GEOS-6578](https://osgeo-org.atlassian.net/browse/GEOS-6578) Unable to unwrap OracleConnection from JBoss WrappedConnectionJDK6
* [GEOS-6616](https://osgeo-org.atlassian.net/browse/GEOS-6616) Clear cached attribute information during FeatureType DELETE
* [GEOS-6617](https://osgeo-org.atlassian.net/browse/GEOS-6617) Scale computation is wrong when the map is expressed in a unit other than meters
