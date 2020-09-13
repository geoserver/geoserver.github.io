---
author: bmmpxf
comments: true
date: 2009-04-08 21:58:53+00:00
layout: post
link: http://blog.geoserver.org/2009/04/08/marine-conservation-with-geoserver/
slug: marine-conservation-with-geoserver
title: Marine conservation with GeoServer
wordpress_id: 190
categories:
- User perspectives
tags:
- ext geoext marine
---

I received a note recently from a GeoServer blog reader who wanted to show off another project using GeoServer, which I am happy to present here.

The [Marine Science Institute at UC Santa Barbara](http://www.msi.ucsb.edu/) and [Farallon Geographics](http://www.fargeo.com/) have built a public, online mapping application enabling scientists and community members to help select marine environments that they feel should be designated for conservation, recreational, and/or commercial uses.  It's called the [MarineMap Decision Support Tool](http://www.marinemap.org/marinemap/).

[![](http://geoserver.wpengine.com/wp-content/uploads/2009/04/marinemap1-300x1771.png)](http://geoserver.wpengine.com/wp-content/uploads/2009/04/marinemap11.png)

You need to have a login to make edits, but anyone can view the layers that are already there.  And there's a good amount of info too, from water quality to estuaries to locations of popular surfing sites.  These layers can be exported to Google Earth as well.  The designers have also helpfully created a [screencast](http://marinemap.org/demos/mmintro/mmintro.htm) showing how to use their application.

The site is based on GeoServer and [OpenLayers](http://openlayers.org).  But what intrigued me was the pleasing desktop-styled application.  It reminded me of [GeoExt](http://geoext.org), and for good reason, since GeoExt is a framework for constructing web mapping applications combining the user interface components of [Ext](http://extjs.com/) with OpenLayers.  And sure enough, it turns out that Ext was used in this application.

I don't know about you, but I think the folks at the MSI should join up with the GeoExt project; I'm sure everyone could learn a lot.
