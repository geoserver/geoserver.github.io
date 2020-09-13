---
author: geoserver
comments: true
date: 2009-07-03 17:22:39+00:00
layout: post
link: http://blog.geoserver.org/2009/07/03/geoserver-175-critical-wms-patch/
slug: geoserver-175-critical-wms-patch
title: GeoServer 1.7.5 critical WMS patch
wordpress_id: 227
---

The latest stable GeoServer version, 1.7.5, was released with a small but critical bug that slows down rendering when a very small polygon or a line is displayed at a high zoom level (so that the displayed area is a very small fraction of the
whole). The slowdown increases as one zooms in, and eventually may lead the Java Virtual Machine to crash.
The bug also makes for non optimal rendering of cased roads (the typical highway display).

The issue is actually due to a [Sun Java bug](http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=6568969), but happily we have a workaround for it. If you find you're affected by this problem, follow these simple instructions:



	
  * stop GeoServer

	
  * download this [patch ja](http://sigma.openplans.org/~aaime/gt-api-2.5.6.jar)r and save it under geoserver/WEB-INF/lib

	
  * restart GeoServer


Voilà, bug gone.

We want to thank Stefan Ziegler for the quick bug report and the other users that reminded us of how important this patch is.
