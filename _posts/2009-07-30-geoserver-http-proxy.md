---
author: geoserver
comments: true
date: 2009-07-30 20:35:38+00:00
layout: post
link: http://blog.geoserver.org/2009/07/30/geoserver-http-proxy/
slug: geoserver-http-proxy
title: GeoServer HTTP Proxy
wordpress_id: 233
categories:
- Announcements
- Developer notes
tags:
- developer
- prototype
- proxy
---

Are you developing JavaScript applications that interact with GeoServer, but having trouble with the [Same Origin Policy](http://en.wikipedia.org/wiki/Same_origin_policy)?  A prototype for a proxy built into GeoServer is coming to help you out with that.  This proxy makes it possible to send HTTP requests to an arbitrary domain through GeoServer's own domain.

[More information and instructions are available on the wiki](http://geoserver.org/display/GEOS/GeoServer+Proxy+Extension).  You'll need either a [Nightly](http://geoserver.org/display/GEOS/Nightly) build, or the [latest GeoServer beta](http://geoserver.org/display/GEOS/Latest) in order to use this proxy.  This proxy is newly in development, so be sure to provide feedback to the GeoServer mailing list with your experiences.
