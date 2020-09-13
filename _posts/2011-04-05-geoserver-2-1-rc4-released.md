---
author: geoserver
comments: true
date: 2011-04-05 22:13:31+00:00
layout: post
link: http://blog.geoserver.org/2011/04/05/geoserver-2-1-rc4-released/
slug: geoserver-2-1-rc4-released
title: GeoServer 2.1-RC4 Released
wordpress_id: 917
categories:
- Announcements
---

The GeoServer team is happy to announce the fourth release candidate for 2.1, now available for [download](http://geoserver.org/display/GEOS/GeoServer+2.1-RC4).

This release brings some important bug fixes and addresses a few regressions discovered in RC3. This includes a [new parameter](http://jira.codehaus.org/browse/GEOS-4454) that will once again allow multiple GeoServer instances to run from a single data directory. This parameter, named "GWC_DISKQUOTA_DISABLED", will disable the GeoWebCache disk quota module preventing it from maintaining a lock in the data directory.

Other key fixes include an issue with the alternate and more performant method of [raster reprojection](http://jira.codehaus.org/browse/GEOS-4443) that comes with the GeoServer 2.1 series, as well as some fixes for WMS 1.3 support surrounding axis ordering issues. Check out the [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=17294) for the full list.

Thanks to everyone who tested RC3 and helped us flush out these last few issues. You can continue to help us get to the official 2.1 release by downloading and trying out RC4. Be sure to report any issues in the [bug tracker](http://jira.codehaus.org/browse/GEOS) or on the [mailing list](mailto:geoserver-users@lists.sourceforge.net).

Thanks for using GeoServer!
