---
author: Chris Holmes
comments: true
date: 2007-03-14 16:00:27+00:00
layout: post
link: http://blog.geoserver.org/2007/03/14/the-37-gigabyte-gml-file/
slug: the-37-gigabyte-gml-file
title: The 37 gigabyte GML file
wordpress_id: 28
categories:
- Developer notes
---

As GeoServer matures one of the main focuses becomes the ability to scale - dealing with both large amounts of data and large amounts of users.  I got a bit of time to play with GeoServer a week or so ago, and wanted to test out a bit of the large data side of things.  On our geoserver [demo site](http://sigma.openplans.org), we've got about 19 gigabytes of data that we're serving up.  It's all available through the WMS with OpenLayers on the front end, but the data is never exposed all at once.  One of GeoServer's strengths is the WFS, which provides access to the raw vector data, so I wanted to try to download the whole dataset.

GeoServer has some great fundamental design, as its built in such a way that data is never really held in memory, it streams from the database in to GeoTools java objects and then out to the appropriate output format.  So in theory we should be able to stream GML from databases of any size.  So that's what I did, and there were absolutely no memory errors or other problems.  Due to the verbose nature of GML the file GeoServer produced was about 37 gigabytes - containing road, landmark, and water data for the whole US, and country boundaries and place names for the world.  The data was came down at 4.97 MB/s, which I don't think is too bad for transforming it to GML on the fly.  One interesting thing I noticed that with larger datasets there's a noticeable pause before the data starts returning.  With small datasets the streaming nature of GeoServer tends to produce results right away.  So we'll have to do some investigation to see what's taking that time - hopefully it's something we have control over and not buried in PostGIS or some such.  I do believe that GeoServer can handle databases of any size, and would love to hear reports from people out there working with even bigger sets of data.

In the next couple weeks we're also going to have Justin set up a better testing suite for scalability, using [JMeter](http://jakarta.apache.org/jmeter/).  A number of people have done testing against GeoServer with it before, but in a more ad hoc way.  This will build the tests in to the source distribution, so that we are sure it gets run with every release, so we don't have any regressions.  There have been many speed improvements of late, and many more to come, so we want to be sure that other changes in the code don't accidentally affect things.  One more tidbit of scalability news, Gabriel reported that he attended a meeting where someone reported some GeoServer benchmarks, successfully supporting 1000 requests.
