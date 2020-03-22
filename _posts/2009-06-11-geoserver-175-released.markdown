---
author: aaime
comments: true
date: 2009-06-11 15:03:12+00:00
layout: post
link: http://blog.geoserver.org/2009/06/11/geoserver-175-released/
slug: geoserver-175-released
title: GeoServer 1.7.5 Released
wordpress_id: 222
categories:
- Announcements
tags:
- charts
- jndi
- production
- release
---

The GeoServer Team is happy to announce the the release of [GeoServer 1.7.5](http://geoserver.org/display/GEOS/GeoServer+1.7.5), the sixth stable version in the 1.7 series.

This release contains some new features that are designed to improve the use of GeoServer in a production environment. Some [new WMS settings](http://docs.geoserver.org/1.7.5/user/services/wms/configuration.html) have been added that allow the administrator to limit the amount of resources consumed by each WMS request, specifically in terms of memory and time used.  It is also now possible to use [JNDI connection pools](http://docs.geoserver.org/1.7.5/user/data/jndi-connection-pools.html) for the DB2 and Oracle (NG) databases, providing better integration with enterprise environments.

The [features pregeneralized](http://docs.geoserver.org/1.7.5/user/tutorials/feature-pregeneralized/feature-pregeneralized_tutorial.html) datastore extension now allows an administrator to set up a vector data pyramid, and therefore significantly speed up WMS data serving over large data sets, especially those having geometries with a large number of coordinates.

The chart extension ([previously mentioned on this blog](http://blog.geoserver.org/2009/06/01/geoserver-chart-extension/)) is contained in the release, allowing the overlay of typical business charts on top of WMS maps.

For Windows users, this version introduces a new [service-based installer](http://downloads.sourceforge.net/geoserver/geoserver-1.7.5-ng.exe), making GeoServer run like any other standard Windows service, and allowing for easier administration.

And, as usual, a host of [bug fixes](http://jira.codehaus.org/browse/GEOS/fixforversion/14787) (over 40!) have been incorporated into this release.  [Give it a try!](http://geoserver.org/display/GEOS/GeoServer+1.7.5)
