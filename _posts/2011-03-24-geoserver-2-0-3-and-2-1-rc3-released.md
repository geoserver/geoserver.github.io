---
author: geoserver
comments: true
date: 2011-03-24 21:22:15+00:00
layout: post
link: http://blog.geoserver.org/2011/03/24/geoserver-2-0-3-and-2-1-rc3-released/
slug: geoserver-2-0-3-and-2-1-rc3-released
title: GeoServer 2.0.3 and 2.1-RC3 Released
wordpress_id: 897
categories:
- Announcements
- Features
---

This week has been a busy one for the GeoServer team with two releases coming out. The community is happy to announce the release of both [2.0.3](http://geoserver.org/display/GEOS/GeoServer+2.0.3) and [2.1-RC3](http://geoserver.org/display/GEOS/GeoServer+2.1-RC3).

GeoServer 2.0.3 is a maintenance release for the 2.0.x branch and contains [over 60 fixes and a few small new features](http://jira.codehaus.org/secure/ReleaseNote.jspa?atl_token=HmFvocRJg9&version=16507&styleName=Html&projectId=10311&Create=Create). For those who have already upgraded to 2.1 there is nothing new but those still on 2.0.2 will find:



	
  * Ability to limit the amount of raster data read and delivered in each WCS request

	
  * A host of stabilization improvements in the WFS department, allowing GeoServer to widthstand higher WFS workloads

	
  * The new [control flow](http://docs.geoserver.org/stable/en/user/extensions/querylayer/index.html) extension allowing administrators to exert finer control over the number of parallel requests a GeoServer will handle, to ensure the server cannot be overloaded by malicious users or by a spike in traffic

	
  * Ability to read the GeoServer log file directly from the user interface, without the need to hunt it down in the data directory

	
  * Improvements to the [ogr2ogr](http://docs.geoserver.org/2.0.x/en/user/extensions/ogr.html) extension, allowing for the use of the famous ogr2ogr utility to extend the number of GeoServer WFS output formats

	
  * Finer control over shapefiles returned by the [SHAPE-ZIP output format](http://docs.geoserver.org/latest/en/user/services/wfs/outputformats.html#zipped-shapefile-customisation)


This release is likely the last of the 2.0.x series as the 2.1.0 release nears completion.

The third release candidate of GeoServer 2.1 also brings a number of [bug fixes and improvements](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=17257) including:



	
  * The [querylayer](http://docs.geoserver.org/stable/en/user/community/querylayer/index.html) module which is a powerful extension that allows for cross layer filtering

	
  * Support for GML3 encoding in Atom/RSS output formats

	
  * Raster to vector conversion processes for WPS

	
  * Inclusion of WMS decorations in PDF output


And more. Check out the entire [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=17257) for more information.

Thanks to everyone who have worked hard over the past few months adding features and fixing bugs, in order to make this release happen. As usual, we encourage you to download, try it out, and provide feedback on the [users mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users).


