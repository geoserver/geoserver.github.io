---
author: geoserver
comments: true
date: 2009-12-12 01:50:23+00:00
layout: post
link: http://blog.geoserver.org/2009/12/11/time-support-for-geoserver/
slug: time-support-for-geoserver
title: Adding Time support to GeoServer via the ImageMosaic plugin
wordpress_id: 392
categories:
- Behind The Scenes
- Developer notes
- Features
tags:
- GeoServer
- GeoTools
- Giannecchini
- GIS
- Mosaic
- Temporal
- TIME
- wms
---

Lately, I have been working on adding support for the **TIME **attribute for GeoServer in WMS GetMap requests via an improvement of the ImageMosaic raster store:


<blockquote>`http://yourserver/geoserver/wms?REQUEST=GetMap&...&TIME=2009-12-12,2009-12-13&...`</blockquote>


You can get some more details on the [GeoSolutions blog](http://geo-solutions.blogspot.com/2009/12/adding-time-support-to-geoserver-and.html).
