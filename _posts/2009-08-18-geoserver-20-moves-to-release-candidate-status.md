---
author: geoserver
comments: true
date: 2009-08-18 16:18:53+00:00
layout: post
link: http://blog.geoserver.org/2009/08/18/geoserver-20-moves-to-release-candidate-status/
slug: geoserver-20-moves-to-release-candidate-status
title: GeoServer 2.0 moves to Release Candidate status
wordpress_id: 240
categories:
- Announcements
tags:
- rc
- release
- ui
---

The GeoServer Team would like to announce that GeoServer 2.0 is now out of beta and has [moved into Release Candidate status](http://geoserver.org/display/GEOS/GeoServer+2.0-RC1).

In case you haven't been following our [previous](http://blog.geoserver.org/2009/06/03/geoserver-20-now-in-beta/) [posts](http://blog.geoserver.org/2009/07/21/geoserver-20-beta2-released/), GeoServer 2.0 contains a completely redesigned user interface, using [Wicket](http://wicket.apache.org/).  Based on feedback from our beta testers, the move to RC1 consisted mainly of user interface improvements. One specific new feature to point out is that ArcSDE stores have a [better configuration panel](http://jira.codehaus.org/browse/GEOS-3310), one that simplifies requests to raster coverages.

With [55 issues fixed](http://jira.codehaus.org/browse/GEOS/fixforversion/15379), this first Release Candidate is deemed stable by the GeoServer Team.  But we need your help to verify this, so please [download this new version](http://geoserver.org/display/GEOS/GeoServer+2.0-RC1) and try it out.

**N.B.**  If you wish to connect GeoServer 2.0 to your existing data directory (from 1.7.x), beware that GeoServer 2.0 changes the directory structure a bit, so should you wish to switch back to 1.7.x, you will need to [hand edit some files](http://geoserver.org/display/GEOSDOC/Migrating+Between+1.7.x+and+2.0.x).

Thanks to everyone who helped out with this release!  Keep sending that feedback in.  Assuming no large problems are found, we should have an official release in the next month or two.
