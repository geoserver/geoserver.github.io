---
author: Brent Owens
comments: true
date: 2007-02-12 19:36:51+00:00
layout: post
link: http://blog.geoserver.org/2007/02/12/geoserver-150-rc1-released/
slug: geoserver-150-rc1-released
title: GeoServer 1.5.0-RC1 released
wordpress_id: 23
categories:
- Announcements
---

We have just released our first release candidate for the 1.5 series of GeoServer that you can download [here](http://docs.codehaus.org/display/GEOS/GeoServer+1.5.0-RC1). The main feature of 1.5 is support for 'raster' formats, like geotiff, arcgrid, gtopo30, and more.  These are accessible not just through the WMS, but there also through the new Web Coverage Service (WCS) interface.Â  In line with GeoServer's mission of making geospatial data more accessible, this allows access to the raw information of rasters, just as WFS does for vector formats.  The WCS is passing all OGC compliance tests, and we plan on getting it certified when we go to 1.5.0.  This release brings many fixes and improvements and it is also now backwards compatible to 1.3 and 1.4 data directories, so you do not have to port your data over to the new structure. Along with speed improvements, it also had a little reorganization of the user interface and has a couple tutorials to go along with it:




Since this is a release candidate, we would appreciate it if you could all download it and give it a quick try. Mostly for testing the backwards compatibility to old data directories, and for deployment in your existing systems to make sure there is no loss in functionality.


Along with this release are some coverage data assistance [tools](http://downloads.sourceforge.net/geoserver/CoverageTools-0.2.exe?use_mirror=easynews) from Geo-Solutions. They will make your life of processing coverage data easier. It is in an early release stage so please report any bugs or problems back to us. We will be adding more documentation to it in the mean time.
