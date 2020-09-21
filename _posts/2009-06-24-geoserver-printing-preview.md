---
author: geoserver
comments: true
date: 2009-06-24 20:05:54+00:00
layout: post
link: http://blog.geoserver.org/2009/06/24/geoserver-printing-preview/
slug: geoserver-printing-preview
title: GeoServer printing preview release
wordpress_id: 225
categories:
- Announcements
- Developer notes
- Features
tags:
- community
- MapFish
- module
- printing
---

Remember the good ol' days, when the only maps you had were pieces of paper?  The past is now! ![PDF example](http://geoserver.org/download/thumbnails/20938936/Picture%201.png)

Hi, I'm Alan, and I'm interning with [OpenGeo](http://opengeo.org/) this summer.  My first order of business has been plugging [MapFish](http://trac.mapfish.org/trac/mapfish/wiki/PrintModuleDoc)'s printing capability into GeoServer as a community module; right now we're releasing a developer preview. The module exposes an HTTP interface that allows the user to ask the server to compose an attractive map in PDF format.  MapFish also provides a JavaScript library that allows easy printing from a OpenLayers map.

Up for trying it out? You'll need to [download a nightly build of trunk](http://gridlock.openplans.org/geoserver/trunk) and add a few files to it.  I have [written up step-by-step instructions](http://geoserver.org/display/GEOS/Printing+2.0+HOWTO) for anyone interested.  If you have any feedback, please chime in on the [GeoServer developers mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-devel).

**EDIT: **The print module instructions have been updated for GeoServer .2.0.x.  Please refer to [http://docs.geoserver.org/stable/en/user/community/printing/](http://docs.geoserver.org/stable/en/user/community/printing/) instead of the old wiki page.
