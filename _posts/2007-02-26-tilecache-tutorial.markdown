---
author: Chris Holmes
comments: true
date: 2007-02-26 20:57:04+00:00
layout: post
link: http://blog.geoserver.org/2007/02/26/tilecache-tutorial/
slug: tilecache-tutorial
title: TileCache Tutorial
wordpress_id: 25
categories:
- Tutorials
---

One of the nicest little pieces of software we've come across in the last few months has been [MetaCarta's](http://www.metacarta.com/) [TileCache](http://monitor.metacarta.com/wms-c/), which performs a very specific job - caching WMS requests for use in clients that understand tiles - and does it very well.  We are making good use of it on our [demo site](http://sigma.openplans.org), to give an even better user experience in terms of the speed the map shows up.

[Chris](http://crschmidt.net/blog/) and [Schuyler](http://iconocla.st/) gave lots of advice on how to use it in conjunction with [OpenLayers](http://openlayers.org), so we thought it'd be worthwhile to write up a [new tutorial](http://docs.codehaus.org/display/GEOSDOC/TileCache+Tutorial) for GeoServer users looking to make use of it.  And there are a few [tips and tricks](http://docs.codehaus.org/display/GEOSDOC/TileCache+Tutorial#TileCacheTutorial-TipsandTricks) that will likely be useful to others, especially some of the nice things you can do in OpenLayers that make it work better with TileCache, like setting multiple host names to cheat the browsers connection limit and setting OL to try to reload when it gets pink tiles.

We hope to eventually be able to ship a nice integrated GeoServer plug-in that will run a TileCache with a nice GUI and enable easy integration with nice [distributed](http://www.jboss.org/products/jbosscache) [java](http://www.opensymphony.com/oscache/wiki/Clustering.html) [caches](http://jakarta.apache.org/jcs/).  The ideal would be to share code with TileCache and run in [jython](http://jython.org), but if that's not possible we will likely do a hand port and leverage [JAI](http://java.sun.com/javase/technologies/desktop/media/jai/).  A big kudos to the MetaCarta programmers, it's a very nice piece of code.
