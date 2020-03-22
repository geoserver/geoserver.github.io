---
author: Chris Holmes
comments: true
date: 2008-03-07 20:16:24+00:00
layout: post
link: http://blog.geoserver.org/2008/03/07/geoserver-162-upgrade-security-release/
slug: geoserver-162-upgrade-security-release
title: 'GeoServer 1.6.2 upgrade: security release'
wordpress_id: 90
categories:
- Announcements
---

GeoServer 1.6.2 is now available for [download here](http://geoserver.org/display/GEOS/GeoServer+1.6.2). This is a **Security Release**, which means it contains [fixes](http://jira.codehaus.org/browse/GEOS/fixforversion/14115) for two Security Vulnerabilities.   We highly recommend that you upgrade to this version.  We found out about both these vulnerabilities in the past couple days, and made an effort to fix them and get this release out as quickly as possible.  One of the issues also affects older versions of GeoServer.  We are not doing a security release for it at this time for all the older versions, but have [clear instructions](http://geoserver.org/display/GEOS/Security+issue+-+Disable+demoRequest) on how to update one file to disable the page where the exploit is possible.  We highly recommend that any production instances of GeoServer follow this, it should be easier to do than a full upgrade.
