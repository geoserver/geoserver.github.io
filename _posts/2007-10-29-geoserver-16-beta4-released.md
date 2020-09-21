---
author: Chris Holmes
comments: true
date: 2007-10-29 15:33:36+00:00
layout: post
link: http://blog.geoserver.org/2007/10/29/geoserver-16-beta4-released/
slug: geoserver-16-beta4-released
title: GeoServer 1.6-beta4 released
wordpress_id: 72
categories:
- Announcements
---

The GeoServer team is pleased to announce what should be the last beta release in the 1.6 series.  So please [download](http://docs.codehaus.org/display/GEOS/1.6.0-beta4), help us test, test, test, and RC1 should come out soon.

Beta4 has a number of great improvements, all across the board.  The [versioning support](http://docs.codehaus.org/display/GEOS/Versioning+WFS) has had a number of improvements and bug fixes, soon we should have some easy to use tutorials and stable examples, but for the impatient you can try to figure things out from an [early example](http://geo.openplans.org/tschaub/wfsv/feature-editor.html) and the [foss4g tutorial](http://docs.codehaus.org/display/GEOSDOC/6+Versioning).  Google Earth support has some nice improvements, with better sizes for icons and the addition of the KML 'LookAt' tag, which zooms you straight to where your data is, plus a number of bug fixes.

GeoJSON support has been updated to the latest spec, and the 'www' portion of the data directory is now working properly, allowing anyone to ship demos to be served by GeoServer.  For the next release we will show some examples of how to do this.  Also new is support for 'component WMS', which allows GeoServer to do on the fly rendering of layers that reside on other servers.  In the WMS request you just specify the SLD and the location of the WFS and GeoServer gives you the rest.  There is also support for Arabic labels.  GeoServer is also now working properly in Oracle Application server.
