---
author: aaime
comments: true
date: 2016-02-25 18:46:31+00:00
layout: post
link: http://blog.geoserver.org/2016/02/25/geoserver-2-7-6-released/
slug: geoserver-2-7-6-released
title: GeoServer 2.7.6 released
wordpress_id: 2625
categories:
- Announcements
tags:
- release
---

The GeoServer team is happy to announce the release of GeoServer 2.7.6. [Download bundles](https://sourceforge.net/projects/geoserver/files/GeoServer/2.7.6/) are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.6/geoserver-2.7.6-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.6/geoserver-2.7.6-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.6/geoserver-2.7.6.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.6/geoserver-2.7.6.exe/download)) along with documentation and extensions.

The release contains 17 fixes compared to 2.7.5, including improvements in the WMS cascading, a deadlock fix for admins re-configuring GWC while under load, a fix for a regression with SqlViews using more than one geometry field, and a WPS file descriptor leak, and some other WMS related fixes. For a full list, see the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=12102).

GeoServer 2.7.6 is the last maintenance release of the GeoServer 2.7.x series, users are recommended to upgrade to 2.8.x or just wait next month for 2.9.0 to be released as stable.

Thanks to everyone taking part, reporting issues and making pull requests, and also thanks to Andrea Aime ([GeoSolutions](http://www.geo-solutions.it/)) for this release.

This release is made in conjunction with [GeoTools 13.6](http://geotoolsnews.blogspot.com/2016/02/geotools-136-released.html).
