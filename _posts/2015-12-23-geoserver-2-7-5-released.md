---
author: geoserver
comments: true
date: 2015-12-23 11:42:38+00:00
layout: post
link: http://blog.geoserver.org/2015/12/23/geoserver-2-7-5-released/
slug: geoserver-2-7-5-released
title: GeoServer 2.7.5 released
wordpress_id: 2450
categories:
- Announcements
---

The GeoServer team is happy to announce the release of GeoServer 2.7.5. [Download bundles](https://sourceforge.net/projects/geoserver/files/GeoServer/2.7.5/) are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.5/geoserver-2.7.5-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.5/geoserver-2.7.5-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.5/geoserver-2.7.5.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.5/geoserver-2.7.5.exe/download))  along with documentation and extensions.

GeoServer 2.7.5 is a maintenance release of GeoServer recommended for production deployment. Thanks to everyone taking part, submitting fixes including:

Bug
[GEOS-4179] - Importer and monitoring REST resources are not thread-safe
[GEOS-7116] - Applying a CRS in Importer clears other found CRSes
[GEOS-7306] - Stored Queries don't work on App-Schema layers backed by database
[GEOS-7346] - WPS cancelling output stream ends up writing a single byte at a time

For a full list, see the [release notes](https://osgeo-org.atlassian.net/projects/GEOS/versions/11902).

The next release, 2.7.6, will mark the planned end of life for this release series. You and your organisation should now consider looking into to the 2.8 release and start testing it now.

Thanks to Ian Turton ([Astun Technology](http://astuntechnology.com)) for this release.

This release is made in conjunction with [GeoTools 13.5](http://geotoolsnews.blogspot.co.uk/2015/12/geotools-135-released.html).
