---
author: Chris Holmes
comments: true
date: 2007-08-14 16:12:21+00:00
layout: post
link: http://blog.geoserver.org/2007/08/14/geoserver-embraces-the-geoweb/
slug: geoserver-embraces-the-geoweb
title: GeoServer embraces the GeoWeb
wordpress_id: 66
categories:
- Announcements
---

We are pleased to announce the release of [GeoServer 1.5.3](http://docs.codehaus.org/display/GEOS/GeoServer+1.5.3).  This version represents the culmination of a ton of hard work to make GeoServer more compatible with the new formats gaining great popularity in the rapidly expanding geo world.  Foremost among the improvements is a number of advances in our [support for Google Earth](http://docs.codehaus.org/display/GEOSDOC/Google+Earth).  KML, the format understood by Google Earth, has been available from GeoServer for awhile.  But our implementation wasn't flexible enough to make good looking maps and to take advantage of the advanced features of the format.  That has all changed, with better default styling, [custom placemarks from templates](http://docs.codehaus.org/display/GEOSDOC/01-Placemark+Templates), support for '[Super-Overlays'](http://docs.codehaus.org/display/GEOSDOC/05-KML+Super+Overlays) and [Time](http://docs.codehaus.org/display/GEOSDOC/02-Time+Templates), and automatic [generation of legend](http://docs.codehaus.org/display/GEOSDOC/04-Legend+Overlays) information.  There is also experimental support for [referencing an existing cache](http://docs.codehaus.org/display/GEOSDOC/03-Super+Overlays+and+TileCache) of tiles to use in a Super-Overlay.  The ability to style one's 2d map and get the same output in Google Earth has also improved dramatically, as it now picks up proper scale elements.

The other big announcement is support for [GeoRSS](http://docs.codehaus.org/display/GEOSDOC/GeoRSS), which allows GeoServer data to also be served on Virtual Earth and Yahoo! Maps.  The GeoRSS output can pick up the same pop-up templates as KML, so again you just have to configure your data once and it's available on a number of different formats.   With a bit of coding from Andrea we're also now shipping with support for the map projection used by Virtual Earth and Google Maps, thanks to [SharpGIS](http://www.sharpgis.net/2007/07/27/TheMicrosoftLiveMapsAndGoogleMapsProjection.aspx) and [Chris Schmidt](http://crschmidt.net/blog/archives/238/understanding-googles-projection-slightly-anyway/).   So now if you use [900913](http://crschmidt.net/blog/archives/243/google-projection-900913/) as the EPSG code for your WMS requests our output will be perfectly overlaid on those maps.  The final new web-friendly format is [GeoJSON](http://geojson.org).  This is not part of the main distribution yet, but you can [download the plug-in](http://downloads.sourceforge.net/geoserver/geojson-1.0-RC1.zip), which is easy to add to a GeoServer instance.  JSON is a smaller format than GML, and [early reports](http://ctuot.twoday.net/stories/4132499/) have it coming down faster with less overall size for the same dataset.

The other efficiency improvement is support for [paletted images](http://docs.codehaus.org/display/GEOSDOC/Paletted+images+tutorial), which allows very quick generation of images like png8 and gif that are much smaller in size than our normal output.  This is very useful in situations with low bandwidth, and indeed with tile caching the size of the tiles becomes one of the biggest speed bottlenecks.

The final piece worth mentioning is advances in our Oracle support.  Thanks goes to [JDi Solutions](http://jdi-solutions.co.uk/) for funding [The Open Planning Project](http://topp.openplans.org) to perform the work.  Oracle in GeoServer can now handle full WFS-T transactions against all coordinate reference systems.  There have also been a few nice speed improvements with Oracle as well.  Thanks to all the users and contributors who helped out with testing and feature suggestions, this project would not be possible without all of you.
