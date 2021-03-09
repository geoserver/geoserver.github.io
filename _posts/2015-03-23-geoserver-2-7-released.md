---
author: geoserver
comments: true
date: 2015-03-23 12:00:23+00:00
layout: post
link: http://blog.geoserver.org/2015/03/23/geoserver-2-7-released/
slug: geoserver-2-7-released
title: GeoServer 2.7 released
wordpress_id: 2164
categories:
- Announcements
tags:
- clustering
- color
- CSS
- GeoServer
- release
- security
- SLD
- styling
- wcs
- wms
- wps
---

The GeoServer team is pleased to announce the latest major release of GeoServer: [version 2.7](http://geoserver.org/release/2.7.0).

**Quick links:**



	
  * [Windows installer](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.0/geoserver-2.7.0.exe/download)

	
  * [OS X installer](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.0/geoserver-2.7.0.dmg/download)

	
  * [OS-independent binary](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.0/geoserver-2.7.0-bin.zip/download)

	
  * [Web Archive (WAR)](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.0/geoserver-2.7.0-war.zip/download)

	
  * [More downloads...](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.0/)

	
  * [User Manual](http://docs.geoserver.org/2.7.0/user)


This release includes a variety of improvements and fixes provided by and for the community over the past six months since GeoServer 2.6 was released. (See our [release schedule](https://github.com/geoserver/geoserver/wiki/Release-Schedule).) While many of these high-level features have been highlighted in [previous](http://blog.geoserver.org/2015/02/21/geoserver-2-7-rc1-released/) [posts](http://blog.geoserver.org/2015/01/22/geoserver-2-7-beta-released/), we'd like to list them in brief here, with links to documentation so you can learn more.


### Color composition and color blending


These are two new extensions to the rendering engine that allows for greater control over how overlapping layers in a map are merged together. Instead of just placing layers on top of others (with or without transparency), there is now a [range of filters and effects](http://docs.geoserver.org/2.7.0/user/styling/sld-extensions/composite-blend/modes.html), such as "multiply", "darken", and "hard light".

![](/img/uploads/dem-multiply.jpg)

Please see the documentation for [an example on how to create inner line effects](http://docs.geoserver.org/2.7.0/user/styling/sld-extensions/composite-blend/example.html) such as the image below:

![](/img/uploads/nurc-NaturalEarthRaster_nurc-states1.jpg)

Thanks to [Cleveland Metroparks](http://www.clevelandmetroparks.com/) for sponsoring this improvement.


### Relative time support in WMS/WCS


GeoServer has long had the ability to specify dates/times in requests to subset data. Up until now these dates/times needed to be absolute. Support has now been added for specifying [relative time](http://docs.geoserver.org/2.7.0/user/services/wms/time.html#specifying-a-relative-interval), for example:



	
  * Last 36 hours from the present (`PT36H/PRESENT`)

	
  * Day after December 25 2012: (`2010-12-25T00:00:00.0Z/P1D`)


Thanks to [Jonathan Meyer](http://gisjedi.com/) for this improvement.


### WPS clustering


There are quite a few improvements to the [Web Processing Service](http://docs.geoserver.org/latest/en/user/extensions/wps/index.html) module, courtesy of Andrea Aime and [GeoSolutions](http://www.geo-solutions.it/). (Please note that [WPS is still an extension](http://docs.geoserver.org/2.7.0/user/extensions/wps/install.html).)

GeoServer has a new WPS extension point allowing GeoServer nodes in the same cluster to share the status of current WPS requests. This is particularly important for asynchronous requests, as the client polling for the progress/results might not be hitting the same node that’s currently running the request.

This [initial implementation](http://docs.geoserver.org/2.7.0/user/extensions/wps/hazelcast-clustering.html) leverages the Hazelcast library to share the information about the current process status using a replicated map.


### WPS security


GeoServer now has the ability to connect WPS processes to the standard role-based security system. This means that administrators can now [determine what users and groups can access or execute](http://docs.geoserver.org/2.7.0/user/extensions/wps/security.html), making WPS usage safer and more secure.

![](/img/uploads/wpssecurity1.png)


### WPS limits


In addition to limiting the users and groups that can access WPS processes, GeoServer now also has the ability to [set WPS input execution limits](http://docs.geoserver.org/2.7.0/user/extensions/wps/security.html#input-limits) (such as timeout values), ensuring that a runaway process can't cause a system to fail due to utilizing too many resources. Limits can be set globally and on a per-process basis.

![](/img/uploads/execution.png)


### WPS dismiss


A client that connects to the WPS now not only has the ability to execute processes, but also [the ability to dismiss/kill processes](http://docs.geoserver.org/2.7.0/user/extensions/wps/operations.html#dismiss). Also new is the ability for the administrator to see the current processes that are being executed on the system.

![](/img/uploads/statuspage.png)


### CSS extension refresh


The popular CSS extension, originally written by David Winslow of [Boundless](http://boundlessgeo.com), allows users to [style layers using a CSS-like syntax instead of SLD](http://docs.geoserver.org/2.7.0/user/extensions/css/). This extension has now been entirely rewritten in native Java. The functionality remains the same, though with improvements in speed and stability.

![](/img/uploads/css1.png)

Thanks to Andrea Aime from [GeoSolutions](http://www.geo-solutions.it/) for this improvement.


### New CSS workshop


There is also now [a full workshop-sized tutorial devoted to using CSS in GeoServer](http://docs.geoserver.org/2.7.0/user/extensions/css/workshop/index.html). This expands upon the basic tutorial, and goes into greater detail, providing a powerful learning resource for anyone who wants to learn how to style maps with CSS.

Thanks to Jody Garnett from [Boundless](http://boundlessgeo.com) for donating the workshop to the community.


### **Cascade WFS Stored Queries**


Thanks to Sampo for adding support for c[ascaded WFS stored queries](/img/uploads/csqconfigure2.png).

[![](/img/uploads/csqconfigure-1024x533.png)](http://blog.geoserver.org/2015/03/23/geoserver-2-7-released/csqconfigure/)


### Try out the new version


See the full list of changes linked from the [release page](http://geoserver.org/release/2.7.0), and please read these [previous](http://blog.geoserver.org/2015/02/21/geoserver-2-7-rc1-released/) [posts](http://blog.geoserver.org/2015/01/22/geoserver-2-7-beta-released/) for more information on these new features. While no software is ever bug-free, we fully stand behind this release, and believe it will provide you with a better, more stable, and featured-filled GeoServer. Thanks!

**[Download GeoServer 2.7](http://geoserver.org/release/2.7.0)**


## About GeoServer 2.7


Articles and resources for GeoServer 2.7 series:



	
  * [Using WMS time to explore your data](http://boundlessgeo.com/2015/03/using-wms-time-to-explore-your-data/)

	
  * Status of GeoServer WPS ([slides](https://2015.foss4g-na.org/sites/default/files/slides/gs_wps_foss4g_na_2015.pdf)|[video](https://www.youtube.com/watch?v=itYS3cTw-b4))

	
  * [Color blending and compositing implemented for GeoServer 2.7](http://www.geo-solutions.it/blog/color-blending-in-geoserver/)

	
  * [CSS Workshop is Live on GeoServer User Manual](http://www.how2map.com/2015/02/css-workshop-is-live-on-geoserver-user.html)

	
  * [Protecting GeoServer with CAS in an Enterprise environment](http://www.geo-solutions.it/blog/geoserver-and-cas/)

	
  * [SOLR power shining through GeoServer OGC services](http://www.geo-solutions.it/blog/solr-power-shining-through-geoserver-ogc-services/)


