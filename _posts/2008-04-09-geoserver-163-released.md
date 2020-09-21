---
author: bmmpxf
comments: true
date: 2008-04-09 15:25:46+00:00
layout: post
link: http://blog.geoserver.org/2008/04/09/geoserver-163-released/
slug: geoserver-163-released
title: GeoServer 1.6.3 Released
wordpress_id: 99
categories:
- Announcements
---

The GeoServer team would like to announce the release of 1.6.3.  This is a stable release containing over 30 patches and improvements since 1.6.2.

One of the more visible additions is support for [watermarking](http://geoserver.org/display/GEOSDOC/Watermarking).  People have been asking for this for some time, so thanks to [GeoSolutions](http://www.geo-solutions.it) for implementing it.  Also, coverage reprojection now works much better.  Thanks to Martin Desruisseaux of [Geomatys](http://www.geomatys.fr) for the continued support on the GeoServer CRS subsystem.  KML generation has been optimized (faster, less memory consumption) especially when dealing with large geometries.  GeoServer supports so many projections natively, but that can have its downsides, namely when certain clients aren't prepared for the size of the capabilities document!  Now the [SRS list can be limited](http://geoserver.org/display/GEOSDOC/Common+OWS+Configuration) in the WMS capabilities.  Special thanks to Gabriel Roldán for the above two features.

You can view the 1.6.3 [changelog](http://jira.codehaus.org/secure/IssueNavigator.jspa?reset=true&pid=10311&fixfor=14102) for details, and download from [geoserver.org](http://geoserver.org/display/GEOS/GeoServer+1.6.3). Thanks to the community for continually improving GeoServer.  Please continue to submit those [bug reports](http://jira.codehaus.org/browse/GEOS) and feature requests.
