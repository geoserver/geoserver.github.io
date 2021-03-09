---
author: geoserver
comments: true
date: 2013-03-18 19:42:49+00:00
layout: post
link: http://blog.geoserver.org/2013/03/18/geoserver-2-3-0-released-first-official-osgeo-release/
slug: geoserver-2-3-0-released-first-official-osgeo-release
title: GeoServer 2.3.0 released, first official OSGeo release!
wordpress_id: 1363
---

The GeoServer team is happy to announce the release of GeoServer 2.3.0, available for [download](http://geoserver.org/display/GEOS/GeoServer+2.3.0).

This release contains six months worth of improvements and fixes to the GeoServer code base. Including several important new features and improvements such as:



	
  * A pluggable configuration subsystem (for the catalog and service configuration)

	
  * GeoWebCache clustering and disk quota improvements

	
  * More powerful layer groups and better control of the WMS capabilities layer tree

	
  * Several security subsystem improvements

	
  * WPS process whitelist (control which processes your WPS is exposing)

	
  * WMS dimensions support improvements (units, custom dimensions)

	
  * JSON and JSONP output format support in many OGC operations

	
  * The monitoring module finally graduating to official extension

	
  * Raster re-projection quality improvements and speedups

	
  * INSPIRE module improvements for the WFS protocol

	
  * A newfound ability to catalogue all components of GeoServer via a REST API


For those daring enough to try out nightly builds the 2.3.x series also offers a new scripting extension allowing you to write WPS processes and small applications in your preferred scripting language. Also included as a nightly community module available is a complete WCS 2.0 service implementation.

More information about the new features of the 2.3.x stream can be found in the  [GeoServer 2.3-beta release announcement](http://blog.geoserver.org/2013/01/29/geoserver-2-3-beta-released/).

[![OSGeo Project](/img/uploads/OSGeo_project1.png)](http://blog.geoserver.org/2013/03/18/geoserver-2-3-0-released-first-official-osgeo-release/osgeo_project/)The good news do not stop there. GeoServer has finally completed the OSGeo incubation and it's now an official OSGeo project. Many thanks to all that participated, in particular Jody Garnett for constantly pushing forward, Landon Blake for mentoring us, and all the people that participated to the FOSS4G-AU code sprint in which all of the grunt work of provenance review was done. We want to thank in particular Jody Garnett, Adam Brown, Karin Stronkhorst, Luca Morandini and Joshua Vote for the hard work.

And last but not least there have been some bug fixes since the RC1 release, you can find a full list in the GeoServer 2.3.0 [changelog](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=19111). Included in this list, for those willing to try out [nightly builds](http://gridlock.opengeo.org/geoserver/2.3.x/community-latest/), is a new[ fast WMS JPEG](http://geo-solutions.blogspot.it/2013/03/libjpeg-turbo.html) encoder based on [libjpeg-turbo](http://libjpeg-turbo.virtualgl.org/) which should give a nice boost to your raster data serving.

[Download GeoServer 2.3](http://geoserver.org/display/GEOS/GeoServer+2.3.0), try it out, and provide feedback on the [GeoServer mailing list](http://geoserver.org/display/GEOS/Mailing+Lists).  As with any new version, _be sure to backup your data directory before upgrading_.

**Thanks again for using GeoServer!**

**[Download GeoServer 2.3](http://geoserver.org/display/GEOS/GeoServer+2.3.0)**




