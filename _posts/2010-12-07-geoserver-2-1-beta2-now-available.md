---
author: geoserver
comments: true
date: 2010-12-07 00:01:27+00:00
layout: post
link: http://blog.geoserver.org/2010/12/06/geoserver-2-1-beta2-now-available/
slug: geoserver-2-1-beta2-now-available
title: GeoServer 2.1-beta2 now available
wordpress_id: 789
categories:
- Announcements
tags:
- beta
- release
- security
- ui
- wps
---

We are pleased to announce the [second beta release of GeoServer 2.1](http://geoserver.org/display/GEOS/2.1-beta2).  Big thanks goes out to [GeoSolutions](http://www.geo-solutions.it/) for stepping up to the unglamorous and thankless process of creating a release, not to mention adding lots of great new features.

GeoServer 2.1.0 is shaping up to be quite an incredible step forward.  In addition to all the great features of [the first 2.1 beta](http://blog.geoserver.org/2010/09/04/geoserver-21-beta-released/), this release brings a few more.


### Graphical File/Directory Chooser


Ever found it difficult to remember the full path when loading a shapefile or GeoTIFF?  A new improvement brings an easy graphical file and directory selection tool to browse the file system that GeoServer is on.  This is definitely a great enhancement to make GeoServer even easier to configure.

Read more about the [new file chooser](http://geo-solutions.blogspot.com/2010/11/new-file-chooser-for-geoserver.html).


### Core improvements to support database-backed catalog


GeoServer's core catalog interfaces received some tweaks to be able to more easily support different backend storage formats. The current in-memory implementation has a number of drawbacks, the most notable being that it is memory bound which means it can not scale up to large amounts of layers.  The support for specific new storage formats is still only available a community module, but these core improvements make it possible to more easily swap in and out different backends.

Read more about the improvements for [database-backed catalog](http://geoserver.org/display/GEOS/GSIP+52+-+Refactor+out+DAO+for+Catalog+and+Configuration).


### Font Improvements


Adding new fonts for your maps should now be much easier, as you can just drop font files directly in to your GeoServer data directory and they will be picked up by GeoServer.  The admin interface also will list the fonts currently available, including the ones picked up directly from the Java Virtual Machine.


### Upgrade to Spring Security 2.0.6


GeoServer has always had [Acegi Security](http://www.acegisecurity.org/) as its core, but that library got absorbed by the Spring community, and improved and upgraded to become [Spring Security](http://static.springsource.org/spring-security/site/index.html), the official security module of the [Spring portfolio](http://www.springsource.org/projects/).  This brings a number of new security protocols to GeoServer, including [OpenID](http://openid.net/) and [Windows NTLM](http://msdn.microsoft.com/en-us/library/aa378749%28VS.85%29.aspx).  It also should be easier to customize security setup, with even more powerful options.

Read more about the [upgrade to Spring Security](http://geoserver.org/display/GEOS/GSIP+54+Upgrade+Geoserver+security+to+Spring+Security+2.0).


### WCS limits


WFS and WMS both have had the ability to limit what a user can request.  Now, similar controls are in place for WCS calls as well.  Thanks to [MassGIS](http://www.mass.gov/mgis/) for funding this improvement.


### Web Processing Service (WPS) in extensions


The one thing to note from last beta release is that the WPS is [maturing](http://geo-solutions.blogspot.com/2010/11/geosolutions-helps-geoserver-wps-going.html), It has been split up in to three modules, "core", "web", and "sextante".  The latter has all the algorithms of the [Sextante](http://www.sextantegis.com/) project, but is not yet mature, so it lives in a community module.  Web and core live in a new WPS extension, meaning that **the core of WPS is now officially supported by GeoServer**.  You can find the WPS extension on the [download page](http://geoserver.org/display/GEOS/2.1-beta2), and add it to GeoServer just like any other extension.

[Read more](http://geoserver.org/display/GEOS/GSIP+55+-+Promote+WPS+to+extension) about WPS in extensions.


### And more


This release also included a number of other bug fixes and improvements.  Check out the entire [changelog](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=16728). Help us get to a stable 2.1.0 by [downloading](http://geoserver.org/display/GEOS/GeoServer+2.1-beta2) the beta and trying it out. Be sure to report any issues on the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users) or in the [bug tracker](http://jira.codehaus.org/browse/GEOS).  We appreciate any and all feedback.  We're hoping to move soon to Release Candidates, after getting one last major improvement in — **WMS 1.3**.

**[Download GeoServer 2.1-beta2](http://geoserver.org/display/GEOS/2.1-beta2)**
