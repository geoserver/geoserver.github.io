---
author: Justin Deoliveira
comments: true
date: 2007-02-02 02:24:52+00:00
layout: post
link: http://blog.geoserver.org/2007/02/01/open-web-services-4-and-wfs-11/
slug: open-web-services-4-and-wfs-11
title: Open Web Services 4 and WFS 1.1
wordpress_id: 20
categories:
- Announcements
---

GeoServer took part in this years [Open Web Services Initiative](http://www.opengeospatial.org/projects/initiatives/ows-4) as the reference implementation of the next version of the Web Feature Specification. WFS 1.1 brings a few new nice features to GeoServer WFS, such as sorting, GML 3, and coordinate reference system support.

Along with WFS 1.1 support comes a few nice improvements to the GeoServer core itself. The most notable being an improved dispatching system which allows developers to develop services as plain old java objects (pojos), not having to implement complex interfaces of any sort. This brings us a good step closer to having GeoServer be a true framework for people wishing to develop new services.

A preliminary version is available as a [Web Archive](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6-alpha/geoserver-1.6-alpha-war.zip/download) and as [Source](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6-alpha/geoserver-1.6-alpha-src.zip/download).
