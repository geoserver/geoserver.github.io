---
author: geoserver
comments: true
date: 2013-01-23 11:37:27+00:00
layout: post
link: http://blog.geoserver.org/2013/01/23/geoserver-2-2-4-released/
slug: geoserver-2-2-4-released
title: GeoServer 2.2.4 released
wordpress_id: 1302
---

The GeoServer team is happy to announce the release of GeoServer 2.2.4, now available for [download](http://geoserver.org/display/GEOS/GeoServer+2.2.4).

This is the latest release of the stable 2.2 series. The changes that might interest the most users are:



	
  * the monitoring extension module just got promoted to official extension [[GEOS-5538](http://jira.codehaus.org/browse/GEOS-5538)]

	
  * the status page does not throw errors after catalog reloads anymore [[GEOS-5371](http://jira.codehaus.org/browse/GEOS-5371)]

	
  * one critical fix in the REST configuration of freemarker templates [[GEOS-5533](http://jira.codehaus.org/browse/GEOS-5533)]


The changelog also contains the following minor bug fixes

	
  * [[GEOS-5338](http://jira.codehaus.org/browse/GEOS-5338)] - Filter function IEEERemainder mishbehaves in SLD

	
  * [[GEOS-5537](http://jira.codehaus.org/browse/GEOS-5537)] - Tiling artifacts with RasterSymbolizer using bilinear interpolation (when oversampling raster)

	
  * [[GEOS-5551](http://jira.codehaus.org/browse/GEOS-5551)] - WFS 1.0 capabilities will NPE with misconfigured OGR and XSLT output formats

	
  * [[GEOS-5565](http://jira.codehaus.org/browse/GEOS-5565)] - workspace admin unable to create sql view

	
  * [[GEOS-5570](http://jira.codehaus.org/browse/GEOS-5570)] - QueryProcess fails if called with an OGC filter (either 1.0 or 1.1)

	
  * [[GEOS-5197](http://jira.codehaus.org/browse/GEOS-5197)] - Use the layer abstract as the GeoRSS channel description

	
  * [[GEOS-5561](http://jira.codehaus.org/browse/GEOS-5561)] - Missing i18n support for ReprojectPage

	
  * [[GEOS-5562](http://jira.codehaus.org/browse/GEOS-5562)] - Missing i18n support for WorkspaceEditPage

	
  * [[GEOS-5563](http://jira.codehaus.org/browse/GEOS-5563)] - slight mixed up order of Y-parameters in AffineTransformPanel


Also, looking at the corresponding GeoTools release changelog we have the following extra goodies in:

	
  * improvements in the WFS cascading, we can now better interact with remote WFS servers running on TinyOWS and ArcGIS

	
  * imageio-ext was upgraded to version 1.1.6, which means from now on GeoServer uses GDAL 1.9 to extends the range of raster formats it supports


[Download GeoServer 2.2.4](http://geoserver.org/display/GEOS/GeoServer+2.2.4), try it out, and provide feedback on the [GeoServer mailing list](http://geoserver.org/display/GEOS/Mailing+Lists).

Thanks again for using GeoServer!


