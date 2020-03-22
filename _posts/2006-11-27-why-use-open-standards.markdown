---
author: Brent Owens
comments: true
date: 2006-11-27 21:50:29+00:00
layout: post
link: http://blog.geoserver.org/2006/11/27/why-use-open-standards/
slug: why-use-open-standards
title: Why use open standards?
wordpress_id: 11
---

Why use Open Services

GeoServer is strongly committed to open standards for its geospatial web services. Currently this is strongly centered around the Open Geospatial Consortium's Open Web Services architecture, as they have the largest consensus among industry and government, and have some very high quality specifications. But GeoServer remains un-ideological about the particular standard, as long as it is fully open and widely supported.

This insistence on open standards is practical, if immense amounts of geospatial information are to be truly accessible it will only be possible through widely used open standards. The GIS industry has always had a myriad of formats, making the combination of data from different sources an exercise in frustration, spending massive amounts of time and money with data conversion, or simply scrapping the conversion and duplicating the work of gathering the data. The Internet and Web Services open up new possibilities for quickly obtaining geographic data, but unless open standards are utilized users will have to decide which geospatial web they want to access, obtaining the appropriate client software for each. Imagine if Netscape and Internet explorer had different Internets - if the browser wars had extended to servers, instead of having an open source standard with Apache - then users today would have to decide which Internet they wanted to get their information from, depending on which browser they were using.

Relying on a non-open standard for exchanging geographic information ensures that it can only be exchanged with others who have bought the same system. The cost to entry to that geospatial web is whatever the server vendor chooses to charge, and the only geographic information available will be by ones who could afford the cost, or who are in the good graces of the company providing the software. An open standard enables competition in an open marketplace for providing geospatial servers. There is no lock-in to the initial choice, as it is easy to switch one vendor's implementation for another, or even to migrate to an open source solution (and back if the oss solution did not fully meet the needs). Without an open standard such migrations would involve a replacing the whole system, not just the component needing improvement.

Several mainstream technology corporations are jumping into the geospatial game, giving away access to their geographic information, allowing users to add additional information. But without open standards and a variety of implementations users will have to pick which proprietary geospatial web to join, instead of creating an open Geospatial Web where all information about a place is searchable and available.

It is getting easier and easier to roll a mapping application, directly connecting a PostGIS or MySQL database to a simple web mapping front end. Putting standards between the display of the map ([WMS](http://udig.refractions.net/confluence/display/GOWS/WMS)), getting the raw data ([WFS](http://udig.refractions.net/confluence/display/GOWS/WFS)) or the updating of information (WFS-T) can seem like an extra hassle for implementors. But doing so allows anyone to access the same information that is displayed, and overlay and combine it with other geographic information, providing more context and the potential of generating new information from analysis. With a self built system there is generally only one way to display the information, the one provided. If an open standard is used then it can be used in a desktop GIS, web applications, 3d viewers, or specially built geographic visualization.

(we should have a picture of a client here getting data from a bunch of different WMSes and even a WFS, as a concrete visualization of what is possible with standards - even a before/after picture, of just putting one's data up on the web, and then one's data overlaid on lots and lots of context from diverse sources)
