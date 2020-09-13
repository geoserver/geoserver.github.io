---
author: geoserver
comments: true
date: 2010-01-26 23:26:33+00:00
layout: post
link: http://blog.geoserver.org/2010/01/26/rest-security-update-for-1-7-x/
slug: rest-security-update-for-1-7-x
title: REST Security Update for 1.7.x
wordpress_id: 452
categories:
- Announcements
---

A recent [post](http://blog.geoserver.org/2010/01/26/securing-restful-services-with-geoserver-2-0-1/) describes a security issue with RESTful services in GeoServer that was fixed for GeoServer 2.0.1. A [patch](http://geoserver.org/display/GEOS/1.7.x+REST+Security+Update) has been created for 1.7.x and is now available. Any users using the restconfig plugin with GeoServer 1.7 are urged to apply the patch.

**Note** that by applying the patch the same rules as described [here](http://blog.geoserver.org/2010/01/26/securing-restful-services-with-geoserver-2-0-1/) apply. Users will have to either update systems that rely on anonymous access via GET operations or alternatively configure the security subsystem to allow them.
