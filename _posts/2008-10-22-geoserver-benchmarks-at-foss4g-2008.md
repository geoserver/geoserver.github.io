---
author: bmmpxf
comments: true
date: 2008-10-22 15:19:26+00:00
layout: post
link: http://blog.geoserver.org/2008/10/22/geoserver-benchmarks-at-foss4g-2008/
slug: geoserver-benchmarks-at-foss4g-2008
title: GeoServer Benchmarks at FOSS4G 2008
wordpress_id: 139
categories:
- Developer notes
---

There are some questions that are asked quite frequently by people who are using GeoServer, or who are thinking about doing so.  And certain ones can't be so easily answered as those in our [FAQ](http://geoserver.org/display/GEOSDOC/FAQ).  One of the most common I see is this:



_“GeoServer is nifty, but is it fast?”
_





Clearly some benchmarks are needed.  Testing was first done at a presentation at [FOSS4G 2007](http://www.foss4g2007.org/presentations/view.php?abstract_id=120) by Justin Deolivera ([OpenGeo](http://opengeo.org)) and Brock Anderson ([Refractions Research](http://www.refractions.net/)).  They chose to compare performance of GeoServer against [MapServer](http://mapserver.gis.umn.edu/), another popular open-source GIS.  The presentation was well-received and showed off the strengths and weaknesses in both servers.

This year, at [FOSS4G 2008](http://conference.osgeo.org/index.php/foss4g/2008/paper/view/256), Andrea Aime (also OpenGeo) took over the benchmarking process, this time with an updated test suite including thematic mapping, anti-aliasing, raster data, and tile caching.  Since the previous year, MapServer had improved its shapefile rendering to be faster than GeoServer's render time.  But Andrea continues:



_“The hard part started when our results showed GeoServer being in the lead in both PostGIS and raster tests.  I could buy the PostGIS results, but I did not believe the raster results.  MapServer has had long-standing and well-reputed raster support, so how come the newcomer was doing better?”
_





Andrea and Justin worked directly with Steve Lime, Paul Ramsey, and Frank Warmerdam to confirm and discuss the findings.  But the results were clear:  although MapServer was faster at shapefile rendering, GeoServer was faster at raster and PostGIS rendering.

Andrea continues:



_“When you [look at our results](http://presentations.opengeo.org/2008_FOSS4G/WebMapServerPerformance-FOSS4G2008.pdf), remember that the MapServer developers are already working hard to improve MapServer performance, just like they did one year ago with the shapefile results.  GeoServer developers won't be sleeping either, as we're already working on some changes to get PostGIS support both more secure and faster.
_








_For next year, we're looking forward to doing a joint presentation that will allow each group to tune their respective servers to the best of their capabilities, and look into some extra tests. I'm looking forward to it; a bit of friendly competition is benefiting both servers and keeping the audience interested.”
_





Sounds like a friendly throwdown to me.

But don't just [take his word for it](http://presentations.opengeo.org/2008_FOSS4G/WebMapServerPerformance-FOSS4G2008.pdf).  Why don't you [download the test suite](http://presentations.opengeo.org/2008_FOSS4G/foss4g-benchmarks-data-scripts.tar.bz2) and report back your findings?
