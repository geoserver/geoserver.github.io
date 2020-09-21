---
author: Chris Holmes
comments: true
date: 2008-01-07 20:30:56+00:00
layout: post
link: http://blog.geoserver.org/2008/01/07/warviews-powered-by-geoserver-openlayers-and-google-earth/
slug: warviews-powered-by-geoserver-openlayers-and-google-earth
title: 'WarViews: Powered by GeoServer, OpenLayers and Google Earth'
wordpress_id: 82
categories:
- User perspectives
---

Though I admit the name made me a bit scared, Andrea Aime [pointed out](http://www.nabble.com/Very-interesting-GeoServer-OL-GE-based-application-to14612498.html) a really nice use of some of our favorite platforms in the '[WarViews'](http://www.icr.ethz.ch/research/warviews) project.  No, it's not some geolocated remote missile camera, it's a project by the [International Conflict Research](http://www.icr.ethz.ch/) (IRC) group at a Swiss university that attempts to show more clearly the link between geography and conflict.

It complies several GIS datasets of conflict, and shows them on a static map built with OpenLayers, as well as a really nice use of GeoServer's Google Earth [time support](http://docs.codehaus.org/display/GEOSDOC/02-Time+Templates) to demonstrate the events over time.   I just wanted to point out their great work to everyone, go and have a play with what they've built.  It does a great job of showing how you get multiple output options with GeoServer, and can point users to appropriate clients that take advantage of different features.  If another researcher wanted the actual GIS data they could easily point at the WFS and get the raw GML or Shapefiles of the data.
