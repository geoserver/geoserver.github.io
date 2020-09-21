---
author: Gabriel Roldan
comments: true
date: 2007-10-31 04:53:41+00:00
layout: post
link: http://blog.geoserver.org/2007/10/30/geoserver-154-released/
slug: geoserver-154-released
title: GeoServer 1.5.4 Released
wordpress_id: 73
categories:
- Announcements
---

The GeoServer team is pleased to announce the availability of the latest stable release, [1.5.4](http://docs.codehaus.org/display/GEOS/GeoServer+1.5.4).

This release mostly cleans up stuff for Google Earth and Maps.  Generated maps now line up perfectly on Google Maps, with a fix to the projection code.  This allows us to replace the Google Maps overlay demo with OpenLayers, so it works with GMaps, Yahoo! Maps and Virtual Earth.  Google Earth will now zoom to the exact location of the dataset, and has further support for 'time' elements.

There are additionally a few improvements for Oracle users, including proper Shapefile output, and the ability to run in an Oracle Application Server.  Also new is Arabic rendering support and fixes for serving additional content through GeoServer.

Full changelog is located [here](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&styleName=Html&version=13609).

This release is based off the brand new GeoTools 2.3.5 stable release.

Thanks to all the users and contributors who helped out with testing and feature suggestions, this project would not be possible without all of you.
