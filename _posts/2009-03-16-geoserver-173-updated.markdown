---
author: Justin Deoliveira
comments: true
date: 2009-03-16 22:54:12+00:00
layout: post
link: http://blog.geoserver.org/2009/03/16/geoserver-173-updated/
slug: geoserver-173-updated
title: GeoServer 1.7.3 Updated
wordpress_id: 188
categories:
- Announcements
---

A quick note to all those who recently downloaded GeoServer 1.7.3. The release has been patched to address a [bug](http://jira.codehaus.org/browse/GEOS-2751) with the user interface. The patched release can be found on the [download page](http://geoserver.org/display/GEOS/GeoServer+1.7.3). The bug prevents a user from editing a feature type directly after it has been added. For those not wanting to upgrade the work around is to first add the feature type, then save, then reload the configuration. After a reload the feature type will be editable. Apologies for the inconvenience.
