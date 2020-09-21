---
author: Chris Holmes
comments: true
date: 2007-08-07 20:51:05+00:00
layout: post
link: http://blog.geoserver.org/2007/08/07/help-us-test-geoserver-152/
slug: help-us-test-geoserver-152
title: Help us test GeoServer 1.5.2
wordpress_id: 64
categories:
- Announcements
---

So we were hoping to do a big announcement of GeoServer 1.5.2 today.  But our ambitious bug fixes and improvements (over [80 issues](http://jira.codehaus.org/secure/IssueNavigator.jspa?reset=true&&fixfor=13503&pid=10311&sorter/field=issuekey&sorter/order=DESC)) has come back to haunt us, and taught us an important lesson about doing release candidates first, even if 1.5.2-RC1 doesn't sound great to our ears.  We squeezed in lots of [Google Earth output](http://docs.codehaus.org/display/GEOSDOC/Google+Earth) improvements, added [GeoRSS](http://docs.codehaus.org/display/GEOSDOC/GeoRSS), improved the Google Maps demo with a [better](http://crschmidt.net/blog/archives/238/understanding-googles-projection-slightly-anyway/) [projection](http://crschmidt.net/blog/archives/243/google-projection-900913/), and added [paletted images](http://docs.codehaus.org/display/GEOSDOC/Paletted+images+tutorial) for faster and lighter image generation.  And of course those have been where we've seen a few problems.  We've uploaded the release to sourceforge, but users have already reported a few small errors with GeoRSS and Google Maps, so we're regrouping and hoping to gather any additional bug reports and do the big release announcements next week.

So in the meantime, dear readers, you can help us out a ton by [downloading](http://docs.codehaus.org/display/GEOS/GeoServer+1.5.2) the latest release, testing it out and reporting any errors that you might encounter.  The issues that we know about for this release are available [here](http://jira.codehaus.org/secure/IssueNavigator.jspa?reset=true&&fixfor=13649&pid=10311&sorter/field=priority&sorter/order=ASC), if you have one of these issues and its resolved you can try out the [nightly build](http://geo.openplans.org/nightly/1.5.x) to test our fix.  If the issue is not yet resolved then rest assured it will be soon.  So please help us out, and watch for the big 1.5.2 announcement next week.  Thanks for all your support!
