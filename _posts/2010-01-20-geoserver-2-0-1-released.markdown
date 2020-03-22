---
author: geoserver
comments: true
date: 2010-01-20 22:56:18+00:00
layout: post
link: http://blog.geoserver.org/2010/01/20/geoserver-2-0-1-released/
slug: geoserver-2-0-1-released
title: GeoServer 2.0.1 Released
wordpress_id: 420
categories:
- Announcements
- Features
---

With a large number of users upgrading to GeoServer 2.0, it's no wonder we've had so many fixes and improvements make it into [GeoServer 2.0.1](http://geoserver.org/display/GEOS/GeoServer+2.0.1), now available for download.

Possibly the most significant change since 2.0.0 has been the addition of the [RESTful API](http://docs.geoserver.org/2.0.x/en/user/extensions/rest/index.html?highlight=rest%20api) to the security sub system.  Previously, users were able to connect in a read-only capacity to otherwise secure services through RESTful GET requests.  While this is a good fix for GeoServer, it does mean that users who were previously relying on anonymous read access to secure services must now authenticate before they can access them.  [More details are available](http://docs.geoserver.org/2.0.x/en/user/security/sec_rest.html) for those who are interested.

Other changes include usability changes to the administration UI, an updated Windows installer that now contains service and console installation options, and over 100 other [issues fixed](http://jira.codehaus.org/browse/GEOS/fixforversion/15897).

We encourage you to [download](http://geoserver.org/display/GEOS/GeoServer+2.0.1) the latest version and take it for a spin and report any issues you encounter to the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users) or [bug tracker](http://jira.codehaus.org/browse/GEOS).

As always, we owe a debt of gratitude to all those that have contributed bug reports, fixes, patches and features.  A special thanks goes out to [LISAsoft](http://www.lisasoft.com/) for managing this release.
