---
author: geoserver
comments: true
date: 2009-10-15 16:44:15+00:00
layout: post
link: http://blog.geoserver.org/2009/10/15/geoserver-2-0-rc2-released/
slug: geoserver-2-0-rc2-released
title: GeoServer 2.0-RC2 Released
wordpress_id: 338
categories:
- Announcements
---

The GeoServer team is pleased to announce the release of (hopefully) the final release candidate of version 2.0: [GeoServer 2.0-RC2](http://geoserver.org/display/GEOS/GeoServer+2.0-RC2)!

The main focus of this release was getting every little detail in order for 2.0.0.  There were a number of critical issues discovered that have been fixed, and much work was done on the documentation.  But the community did slide in one major new feature, a new plugin called 'Web security GUI', that enables GUI based editing of GeoServer's security configuration.  It hopefully will eventually move to the core, but for now is a great example of the advantages of the new Wicket UI technology - one of the major features of the 2.0 release.  The security GUI plugin can be added without having to change the core files at all, and is an example of how others can build extensions to the core GeoServer services and UI.

The other major feature of 2.0 is the [app-schema](http://docs.geoserver.org/2.0-RC2/user/data/app-schema/index.html) work, and there have been a number of bug fixes for this release candidate.  More importantly, there's now a lot of great documentation by the CSIRO team on how to get set up with [feature chaining](http://docs.geoserver.org/2.0-RC2/user/data/app-schema/feature-chaining.html), and [data access integration](http://docs.geoserver.org/2.0-RC2/user/data/app-schema/data-access-integration.html), as well as a great [tutorial](http://docs.geoserver.org/2.0-RC2/user/data/app-schema/tutorial.html).

This release also marks the branching of 2.0.x to make way for some great new improvements on trunk.  The [GeoSolutions](http://www.geo-solutions.it/) team is working on [bringing Hibernate](http://blog.geoserver.org/2009/08/27/hibernate-and-geoserver-seeking-for-scalability-and-robustness/) in to the GeoServer catalog, so it can be backed by a database for even greater scalability and robustness.  And Justin Deoliveira is [doing work](http://geoserver.org/display/GEOS/GSIP+36+-+Resource+-+Publishing+Split+and+Virtual+Configuration) to have one GeoServer configuration handle a number of different services and security permissions at once.  These will be the highlights of the 2.1.x release, and please get in touch if you can help with funding or development time.  Also being discussed is WFS 2.0, GML 3.2 and WMS 1.3, all of which could move forward with more support.

Thanks to everyone who made the 2.0-RC2 release possible.  And please [download](http://geoserver.org/display/GEOS/GeoServer+2.0-RC2) it and let us know what you think.  If there are no major problems this release will become 2.0.0.
