---
author: geoserver
comments: true
date: 2012-12-24 14:02:32+00:00
layout: post
link: http://blog.geoserver.org/2012/12/24/geoserver-2-2-3-released/
slug: geoserver-2-2-3-released
title: GeoServer 2.2.3 released
wordpress_id: 1289
---

The GeoServer team is happy to announce the release of GeoServer 2.2.3, now available for [download](http://geoserver.org/display/GEOS/GeoServer+2.2.3).

This is the latest release of the stable 2.2 series and contains some small new features and interesting fixes:



	
  * [[GEOS-3885](http://jira.codehaus.org/browse/GEOS-3885)] - Update Freemarker templates through REST API

	
  * [[GEOS-5325](http://jira.codehaus.org/browse/GEOS-5325)] - Add title and abstract to LayerGroupInfo

	
  * [[GEOS-5462](http://jira.codehaus.org/browse/GEOS-5462)] - The rendering thread can block forever under request cancellation

	
  * [[GEOS-5479](http://jira.codehaus.org/browse/GEOS-5479)] - Error in Documentation: </PropertyName> tag used instead of </Literal>

	
  * [[GEOS-5483](http://jira.codehaus.org/browse/GEOS-5483)] - json output in WPS extension does not work due to missing library

	
  * [[GEOS-5485](http://jira.codehaus.org/browse/GEOS-5485)] - Border artifacts when reprojecting single banded (scientific) raster data


Also, looking at the corresponding GeoTools release changelog we have the following extra goodies in:

	
  * better support for chaining rendering transformations

	
  * fixes to time/date handling in CQL

	
  * Oracle specific SDO_NN function to find the N nearest objects to a given location


We also welcome our newest committer, Davide Savazzi, and thank him for the work on Freemarker template through the REST API and the title and abstract support in layer groups, as well as the SDO_NN work back in GeoTools.

[Download GeoServer 2.2.3](http://geoserver.org/display/GEOS/GeoServer+2.2.3), try it out, and provide feedback on the [GeoServer mailing list](http://geoserver.org/display/GEOS/Mailing+Lists).

Thanks again for using GeoServer!


