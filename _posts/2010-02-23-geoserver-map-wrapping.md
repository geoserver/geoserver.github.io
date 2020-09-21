---
author: geoserver
comments: true
date: 2010-02-23 22:31:53+00:00
layout: post
link: http://blog.geoserver.org/2010/02/23/geoserver-map-wrapping/
slug: geoserver-map-wrapping
title: GeoServer continuous map wrapping!
wordpress_id: 482
categories:
- Announcements
tags:
- date line
- dateline
- GeoSolutions
- google
- wraparound
- wrapping
---

GeoServer is now able to output maps that look like continuous wrapped maps from [Google](http://maps.google.com/?ie=UTF8&ll=25.799891,150.117188&spn=155.12213,360&z=2)!

Let's have a look at an example. Below is a map drawn by GeoServer that is reprojected to a projection that happens to sit across the dateline, the usual "edge" of the map.  As you can see the reprojection is not doing a good job where the dateline is crossed:

[caption id="attachment_487" align="aligncenter" width="266" caption="Polygons crossing dateline change before improving the renderer"]![Poor output where polygons cross the dateline](http://geoserver.wpengine.com/wp-content/uploads/2010/02/geoserver-266x3001.png)[/caption]

However, GeoServer now has what is called **advanced projection handling**.  With this enabled, the dateline wrapping is properly handled and, in addition, the map repeats in a continuous fashion:

[caption id="attachment_488" align="aligncenter" width="300" caption="Polygons crossing the dateline with advanced projection handling"]![Polygons crossing dateline change after improving the renderer](http://geoserver.wpengine.com/wp-content/uploads/2010/02/continents_900913-300x1751.png)[/caption]

For more information, including how to turn on this (optional) feature, please see this [post from GeoSolutions](http://geo-solutions.blogspot.com/2010/02/geoserver-continuous-map-wrapping.html).
