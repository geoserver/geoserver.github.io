---
author: bmmpxf
comments: true
date: 2008-03-24 15:16:26+00:00
layout: post
link: http://blog.geoserver.org/2008/03/24/book-report-gis-for-web-developers/
slug: book-report-gis-for-web-developers
title: 'Book report: GIS for Web Developers'
wordpress_id: 95
categories:
- User perspectives
---

Greetings all.


I am new to the GIS world.  Well, not entirely.  I've been an avid map fan since I was a wee lad, and to this day I own a small but extensive collection of [Rand McNally](http://www.randmcnally.com/) [Road Atlases](http://store.randmcnally.com/category/road+atlases.do).  Fast forward the tape a bit, and here I am at [The Open Planning Project](http://topp.openplans.org), as an Outreach Engineer for GeoServer.  However, despite some years of working in technical fields and some more years of ogling nice-looking maps, I must confess that I was and still am, shall we say, a novice to the technology surrounding GIS.

Here at TOPP, I see myself as a facilitator between those who use GeoServer, those who code/develop for it, and those who are somewhere in between.  That said, I've still needed to bootstrap myself into being versed in the terminology.  So, I picked up “[GIS for Web Developers](http://www.pragprog.com/titles/sdgis)” by Scott Davis.  Since then I have thumbed through a few other books and a fair chunk of online information, but by far, this has been the most helpful in getting me started.

The book follows a fairly straightforward arc, starting with a discussion of vectors and rasters.  Two of my initial questions were answered quickly.  The first was “where does all this data come from?” and the second, “what exactly _is_ the data, anyway?”  These may seem trivial, but it's of course very hard to not see as obvious things that one works with as a matter of routine.  (I can recall being very perplexed when I was first introduced to the Web, when trying to figure out the URL.  Where was it going?  What was it doing?)  Although I can't create a Shapefile out of thin air now (Adobe Illustrator for some reason doesn't have it in its Export menu) I know that I can probably find what I need either from government websites or a small but growing community of neogeographers.  As for what's contained in the data, the answer is “a gratifyingly large amount of useful info”.  The book covers Shapefiles, PostGIS databases, and other standard formats of the trade.

The discussion makes a sharp turn and delves into command-line utilities for editing and querying data inside spatial databases.  Perhaps it was my background, but I thought that this topic might have sat more comfortably towards the back of the book, as it's good information, but with a much steeper learning curve than what came before it.  After delving very deep into the OGC web services, the book ends with a “Final Exam” of the complete process from non-geocoded data to spatial database to web browser.  If one can follow the last chapter, one understands the relevant concepts.  I think I'm nearly there.

One of the most beneficial aspects of the book was the clear definitions of terms, as the meanings of, say, DataStore and FeatureType were not intrinsically obvious to me.  It was also quite nice to see GeoServer represented so favorably in the book, both from a practical point of view and as well from a root-for-the -home-team sort of way.  But ESRI's ArcExplorer is given as much treatment as, say, MapBuilder, which is nice for comparison's sake.  I have yet to spend too much time on anything past GeoServer and [OpenLayers](http://www.openlayers.org), but that'll change in time, I'm sure.

Personally, I wished the book had delved more quantitatively into projections.  However, I recognize that my interest lies mainly in the mathematics, and the tools that people have created shield the user from some of the more unseemly calculations.  My coworkers have consistently said, “you don't need to know any of that stuff,” which may in fact be true, but keeping projections as a black box isn't quite in the spirit of the book.  It's a minor gripe, though.

All in all, I found this a great book with which to get started.  While not trying to hide from the jargon, the reader isn't bogged down with so much granularity that the plot is lost.  That's a sweet spot that most technical books miss.  I'm no expert, and won't be for a while, but at least I feel like I know what questions to ask.  And knowing how to ask the right questions is so much more difficult than finding the answers.
