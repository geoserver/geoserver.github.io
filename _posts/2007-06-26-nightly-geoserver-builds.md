---
author: Chris Holmes
comments: true
date: 2007-06-26 15:15:38+00:00
layout: post
link: http://blog.geoserver.org/2007/06/26/nightly-geoserver-builds/
slug: nightly-geoserver-builds
title: Nightly GeoServer Builds
wordpress_id: 45
categories:
- Tips and Tricks
---

Another hint for those wanting the latest and greatest versions of GeoServer.  We've now got a nightly build server going, making snapshots of the latest code for the 1.5.x branch and trunk, at [http://geo.openplans.org/nightly/](http://geo.openplans.org/nightly/).  We do our best to fix a raft of bugs for each new release, and downloading a nightly build will get you access to those without having to figure out subversion and maven and all our other build tools.  If you see that a bug you're interested in was recently fixed you can download the next nightly, test it out and give us feedback.  That helps the GeoServer developers immensely, so we can be sure that our actual releases are as close to bug free as possible.  If you've got your '[data directory](http://docs.codehaus.org/display/GEOSDOC/3+GeoServer+Data+Directory)' set up properly with GeoServer than upgrading to a nightly should be a cinch, allowing you to test out the latest improvements with your already configured data.
