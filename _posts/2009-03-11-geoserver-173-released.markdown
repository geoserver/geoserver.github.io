---
author: bmmpxf
comments: true
date: 2009-03-11 14:49:30+00:00
layout: post
link: http://blog.geoserver.org/2009/03/11/geoserver-173-released/
slug: geoserver-173-released
title: GeoServer 1.7.3 Released
wordpress_id: 186
categories:
- Announcements
- Features
---

The GeoServer team is proud to announce the release of [GeoServer 1.7.3](http://geoserver.org/display/GEOS/GeoServer+1.7.3).  The team has been busy in the six weeks since the previous release, with a code sprint in New York last month and a whopping [63 bugs and new features](http://jira.codehaus.org/browse/GEOS/fixforversion/14786) fixed and implemented (respectively, of course).

This release brings improved support for **ArcSDE rasters**. Previously GeoServer only supported a limited number of SDE rasters, namely 3 and 4 band UCHAR with no color map support. GeoServer now supports all sample types up to an arbitrary number of bands, with color map support. Special thanks goes out to [MassGIS](http://www.mass.gov/mgis/) who provided the funding for this work, and Gabriel for his hard work implementing this feature.

In a first step towards a “multiple configurations” feature, GeoServer now allows you to [filter any capabilities request based on namespace](http://geoserver.org/display/GEOSDOC/WCS+vendor+parameters).  A client can now ask for a particular subset of layers instead of having to receive all of them, which can greatly increase client performance if serving lots of layers.  (This works the same way for all services, although the above link is for WCS.)

There are quite a few new extensions for GeoServer, including:


<blockquote>**REST** - GeoServer now allows for [configuration via REST](http://geoserver.org/display/GEOSDOC/RESTful+Configuration+API) ([REpresentational State Transfer](http://en.wikipedia.org/wiki/Representational_State_Transfer)).  This opens up a whole new world for interfacing with GeoServer, whether it's [a simple metadata update, a batch configuring of layers, or a one step shapefile upload](http://geoserver.org/display/GEOSDOC/RESTFul+Configuration+API+Use+Cases).</blockquote>




<blockquote>**JDBC Image Mosaic** - This extension allows a coverage to be stored along with its pyramids in a [JDBC database](http://geoserver.org/display/GEOSDOC/Using+the+ImageMosaic+JDBC+Plugin).  Special thanks to Christian Müller, who contributed this work!</blockquote>




<blockquote>**Excel** - Adding to the list of [WFS output formats](http://geoserver.org/display/GEOSDOC/WFS+output+formats), feature data can now be output in Microsoft Excel (.XLS) format.  If you want tabular output, but don't need the full power of Excel, you can output comma-separated values (.CSV).  CSV output is available as part of the GeoServer's core, with no extension needed.</blockquote>




<blockquote>**Directory datastore** - In addition to the REST interface, there is now an even easier way to add lots of shapefiles to your catalog.  With the [directory datastore](http://geoserver.org/display/GEOSDOC/Directory+datastore), you can point GeoServer to a directory full of shapefiles and just hit go (well, Submit, Apply, and Save) and all of the shapefiles will be loaded in as datastores.</blockquote>


Also, don't forget that [GeoWebCache](http://geoserver.org/display/GEOSDOC/5.+GWC+-+GeoWebCache) is now built in to GeoServer (it was previously an extension), so GeoServer can immediately cache WMS tiles, which can vastly improve the speed of rendering.

As usual, we invite everyone to [press that download button](http://geoserver.org/display/GEOS/GeoServer+1.7.3), try out those new extensions, [find (and report!) bugs](http://geoserver.org/display/GEOSDOC/2+Issue+Tracker), and [give some feedback](http://geoserver.org/display/GEOSDOC/1+Mailing+lists).  Thanks for using GeoServer!
