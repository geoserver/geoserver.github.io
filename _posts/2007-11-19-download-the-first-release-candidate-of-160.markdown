---
author: Chris Holmes
comments: true
date: 2007-11-19 14:43:09+00:00
layout: post
link: http://blog.geoserver.org/2007/11/19/download-the-first-release-candidate-of-160/
slug: download-the-first-release-candidate-of-160
title: Download the first Release Candidate of 1.6.0
wordpress_id: 78
categories:
- Announcements
---

We are pleased to announce GeoServer 1.6.0-RC1 is available for [download](http://docs.codehaus.org/display/GEOS/1.6.0-RC1) (try [direct from sourceforge](http://sourceforge.net/project/showfiles.php?group_id=25086&package_id=38410&release_id=554392) if that link isn't working).  Since beta4 the team has has closed over 60 issues, tightening up every single detail.  This is easily the most solid first release candidate that we've ever issued, as we are wanting to have as few release candidates as possible.  So if you have not upgraded to the 1.6.x series then now is the time to do so, to ensure that any problems that may arise get fixed as quickly as possible, before 1.6.0.

The 1.6.x series is a major leap forward from 1.5, with major leaps in performance, WFS 1.1 support, and the new ['versioning' WFS](http://docs.codehaus.org/display/GEOS/Versioning+WFS).  There is also much better [support for Google Earth](http://docs.codehaus.org/display/GEOSDOC/Google+Earth) and [Google Maps/Virtual Earth/Yahoo! Maps](http://docs.codehaus.org/display/GEOSDOC/Google+Maps), leveraging better integration with [OpenLayers](http://openlayers.org).  There is also a new integrated [security subsystem](http://docs.codehaus.org/display/GEOSDEV/Geoserver+security+implementation%2C+initial+version), built on [Acegi](http://www.acegisecurity.org/), to provide role-based access control to GeoServer resources.  But the real reason to upgrade to 1.6.0 is a ton of bug fixes, all the rough edges are getting sanded down, so that most all features 'just work', no matter what you throw at them.  So please [download](http://docs.codehaus.org/display/GEOS/1.6.0-RC1) and let us know how it goes.
