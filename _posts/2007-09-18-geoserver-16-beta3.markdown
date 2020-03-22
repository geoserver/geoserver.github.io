---
author: Chris Holmes
comments: true
date: 2007-09-18 19:59:48+00:00
layout: post
link: http://blog.geoserver.org/2007/09/18/geoserver-16-beta3/
slug: geoserver-16-beta3
title: GeoServer 1.6-beta3
wordpress_id: 70
categories:
- Announcements
---

The GeoServer Project is pleased to announce the release of the third beta of 1.6.0, now [available for download](http://docs.codehaus.org/display/GEOS/GeoServer+1.6.0-beta3).  The main focus of this release has been a number of performance improvements, done by Andrea Aime.  These center around the WMS, and can be seen most clearly on layers that do not have any labels.  Soon we should improve the labeling as well, so keep an eye, since GeoServer is getting legitimately _fast.  _Other improvements include fixes in reprojection in the WFS, with some of the WFS 1.1 work being backported to WFS 1.0.  This allows us to do things like digitize on top of Yahoo! Maps and save the points back to GeoServer, where it automatically puts it in the right projection for the dataset.  The final improvement for beta 3 is our GeoJSON implementation is now part of the standard distribution instead of a separate download.  I for one am excited about this, as it's about the only coding I've done in the past year.

Also, if you're attending [FOSS4G](http://www.foss4g2007.org/) then please find us, we love talking to people who are actually making use of GeoServer.  Many of us will be at [TOPP](http://topp.openplans.org)'s booth, and perhaps we will try to pull together a BOF or something.  And of course will be at the workshop and sessions on GeoServer.  See you there!
