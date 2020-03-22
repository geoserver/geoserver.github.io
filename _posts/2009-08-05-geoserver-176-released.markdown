---
author: geoserver
comments: true
date: 2009-08-05 00:23:50+00:00
layout: post
link: http://blog.geoserver.org/2009/08/04/geoserver-176-released/
slug: geoserver-176-released
title: GeoServer 1.7.6 Released
wordpress_id: 235
categories:
- Announcements
- Features
tags:
- lisasoft
- release
- stable
---

[GeoServer 1.7.6](http://geoserver.org/display/GEOS/GeoServer+1.7.6) marks the seventh stable release of the 1.7 series.

As the development focus of the GeoServer team moves more towards the eventual [release of 2.0](http://docs.geoserver.org/1.7.6/developer/policies/community-process.html#road-map), the 1.7 series is winding down.  This release focused mostly on [bug squashing](http://jira.codehaus.org/browse/GEOS/fixforversion/15369) and general stability, with improvements implemented for the [shapefile output](http://docs.geoserver.org/1.7.6/user/services/wfs/outputformats.html) format and Next Generation [Oracle datastore](http://docs.geoserver.org/1.7.6/user/data/oracleng.html).

In addition, a few highly coveted features were added for this release.  The [ArcSDE datastore](http://docs.geoserver.org/1.7.6/user/data/arcsde.html) now supports connectivity to non-spatial tables as well as connection to a specified database version.  [KML support](http://docs.geoserver.org/1.7.6/user/google-earth/features/kmlheighttime.html) has also been extended to include output of 3d lines.

The WMS rendering issue discussed in a [previous post](http://blog.geoserver.org/2009/07/03/geoserver-175-critical-wms-patch/) is also included in this release.

We encourage you to [try it out](http://geoserver.org/display/GEOS/GeoServer+1.7.6) a try and [let us know](mailto:geoserver-users@lists.sourceforge.net) how you like the latest and greatest.
