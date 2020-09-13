---
author: geoserver
comments: true
date: 2009-10-27 04:24:45+00:00
layout: post
link: http://blog.geoserver.org/2009/10/26/geoserver-2-0-released/
slug: geoserver-2-0-released
title: GeoServer 2.0 Released!
wordpress_id: 344
categories:
- Announcements
- Features
---

It has been a long time coming but it is finally here. GeoServer 2.0 has been officially released and is available for [download](http://geoserver.org/display/GEOS/GeoServer+2.0.0). The 2.0 release marks a major milestone for the GeoServer project. A special thanks to all the developers who worked hard for this release, all the users who contributed bug reports, and for those who provided feedback by testing out the 2.0 release candidates.

So what is new in 2.0? The first new feature that people will notice is a completely new web administration interface. Based on the [Wicket](http://wicket.apache.org/) framework the new user interface provides a much more integrated and streamlined application for configuring GeoServer. Wicket makes developing ajax enabled applications trivial by doing all the hard work for you.

[![GeoServer_ Welcome-1-1](http://geoserver.wpengine.com/wp-content/uploads/2009/10/GeoServer_-Welcome-1-1-300x2151.jpg)](http://geoserver.org/display/GEOS/2.0+New+and+Noteworthy)

One of the powerful features of Wicket for the developer is extensibility. Wicket allows one to plug-in components dynamically. This means that developers can now easily write plug-ins and extensions for the GeoServer UI. And some have already done so. Francesco Izzi and the developers from the [geoSDI](http://www.geosdi.org/) project have contributed a plug-in for configuring the GeoServer security sub system. Special thanks for the great contribution.

![GeoServer_ Users list](http://geoserver.wpengine.com/wp-content/uploads/2009/10/GeoServer_-Users-list-300x95.jpg)

The 2.0 release also hails the home coming of the "complex features" branch and true support for application schemas. Led by Ben Caradoc-Davies and Rini Angreani, developers from CSIRO have made this functionality available in the core of GeoServer. Special thanks to them and to [AuScope](http://www.auscope.org.au/) for funding the work. Check out the [documentation](http://docs.geoserver.org/trunk/en/user/data/app-schema/index.html) for more information about getting started with application schemas.

New features has not been the only focus of 2.0. Much work has also gone into scalability and performance in order to ensure that GeoServer continues to improve not only in terms of new features, but also that it continues to get faster.

Much of this work came in preparation for the [WMS Shootout](http://www.slideshare.net/gatewaygeomatics.com/wms-performance-shootout) at FOSS4G in Sydney this year. Great thanks goes out to Andrea Aime for not only representing GeoServer in this benchmarking exercise, but also for the countless number of hours he has poured into improving GeoServer performance and robustness.

As with any release many minor features and bug fixes have gone into 2.0. Be sure to check out the [GeoServer Past Present Future](http://www.slideshare.net/jdeolive/geoserver-past-present-future-2009) talk given at FOSS4G that provides an overview of what else has gone on this year in preparation for 2.0.

[Download](http://geoserver.org/display/GEOS/GeoServer+2.0.0) 2.0 now and try it out. Please help us to continue to improve GeoServer by reporting any issues you encounter on the [mailing list](mailto:geoserver-users@lists.sourceforge.net) and [bug tracker](http://jira.codehaus.org/browse/GEOS).
