---
author: geoserver
comments: true
date: 2012-11-26 22:42:28+00:00
layout: post
link: http://blog.geoserver.org/2012/11/26/geoserver-2-2-2-released/
slug: geoserver-2-2-2-released
title: GeoServer 2.2.2 Released
wordpress_id: 1279
categories:
- Announcements
- Features
---

The GeoServer team is happy to announce the release of GeoServer 2.2.2, now available for [download](http://geoserver.org/display/GEOS/GeoServer+2.2.2).

This is the latest release of the stable 2.2 series and contains a number of good fixes and improvements including:



	
  * [[GEOS-5157](https://jira.codehaus.org/browse/GEOS-5157)] - Can't configure MediaType in INSPIRE extension

	
  * [[GEOS-5376](https://jira.codehaus.org/browse/GEOS-5376)] - Line sizes with UOM in legend decoration are doubly scaled when using DPI

	
  * [[GEOS-5377](https://jira.codehaus.org/browse/GEOS-5377)] - WMS GetFeatureInfo fails when post filter required

	
  * [[GEOS-5388](https://jira.codehaus.org/browse/GEOS-5388)] - Confusing 'Bad credentials forroot' exception in verbose_logging mode when logged in as admin or root

	
  * [[GEOS-5395](https://jira.codehaus.org/browse/GEOS-5395)] - Catalog reload breaks GWC integration, update sequence upgrade and namespace/workspace consistency

	
  * [[GEOS-5402](https://jira.codehaus.org/browse/GEOS-5402)] - Subclasses of GeoServerPreAuthenticationFilter do not map local admin roles to global admin roles

	
  * [[GEOS-5366](https://jira.codehaus.org/browse/GEOS-5366)] - Better heuristic for OWS Request filenames


A number of great fixes came in via community pull requests:

	
  * [Image mosaic filtering fixes](https://github.com/geoserver/geoserver/pull/45)

	
  * [Removing json-lib conflict with GWC](https://github.com/geoserver/geoserver/pull/55)

	
  * [Property handling of POST/PUT requests for proxy module](https://github.com/geoserver/geoserver/pull/71)


Special thanks to Carlo Cancellieri, Jared Erickson, and Andreas Hocevar for their contributions.

And last but not least we saw two new interesting community modules surface for this release:

	
  * [XSLT output format generator plugin for WFS ](http://docs.geoserver.org/latest/en/user/community/xslt/index.html)

	
  * [JSR-223 based scripting extension](http://docs.geoserver.org/latest/en/user/community/scripting/index.html)


Both are available as community nightly builds.

[Download GeoServer 2.2.2](http://geoserver.org/display/GEOS/GeoServer+2.2.2), try it out, and provide feedback on the [GeoServer mailing list](http://geoserver.org/display/GEOS/Mailing+Lists).

Thanks again for using GeoServer!
