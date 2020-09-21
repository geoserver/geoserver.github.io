---
author: geoserver
comments: true
date: 2014-05-21 04:55:07+00:00
layout: post
link: http://blog.geoserver.org/2014/05/21/geoserver-2-5-1-released/
slug: geoserver-2-5-1-released
title: GeoServer 2.5.1 Released
wordpress_id: 1885
categories:
- Announcements
---

The GeoServer team is happy to announce the release of [GeoServer 2.5.1](http://geoserver.org/release/stable/). Download bundles are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5.1/geoserver-2.5.1-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5.1/geoserver-2.5.1-war.zip), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5.1/geoserver-2.5.1.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5.1/geoserver-2.5.1.exe/download))  along with documentation and extensions.

GeoServer 2.5.1 is the next the stable release of GeoServer and is recommended for production deployment. Thanks to everyone taking part, submitting fixes and new functionality:



	
  * By popular request Top/Bottom labels when configuring layer group order

	
  * You can now identify GeoServer "nodes" in a cluster by configuring a label and color in the UI. Documentation and example in the [user guide](http://docs.geoserver.org/stable/en/user/production/identify.html).

	
  * Have you ever run GeoServer and not quite gotten your file permissions correct? GeoServer now has better logging when it cannot your data directory and is required to "fall back" to the embedded data directory during start up.

	
  * We have a new GRIB community module (community modules are not in the release until they pass a QA check, but great to see new development taking shape)

	
  * Documentation on the jp2kak extension now in the [user guide](http://docs.geoserver.org/stable/en/user/extensions/jp2k.html)

	
  * Additional documentation for the image mosaic in the [user guide](http://docs.geoserver.org/stable/en/user/data/raster/imagemosaic.html) with tutorials covering the [plugin](http://docs.geoserver.org/stable/en/user/tutorials/image_mosaic_plugin/imagemosaic.html), [raster time-series](http://docs.geoserver.org/stable/en/user/tutorials/imagemosaic_timeseries/imagemosaic_timeseries.html), [time and elevation](http://docs.geoserver.org/stable/en/user/tutorials/imagemosaic_timeseries/imagemosaic_time-elevationseries.html) and [footprint management](http://docs.geoserver.org/stable/en/user/tutorials/imagemosaic_footprint/imagemosaic_footprint.html).

	
  * WCS 2.0 support continues to improve with DescribeCoverage now supporting null values

	
  * Central Authentication Service (CAS) authentication has received a lot of QA this release and is now available in the GeoServer 2.5.x series.

	
  * Thanks to Andrea and Jody (GeoSolutions and Boundless) for publishing this release

	
  * Check the [release notes](https://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20202) for more details

	
  * This release is made in conjunction with GeoTools 11.1




# About GeoServer 2.5


Articles and resources for GeoServer 2.5 series:



	
  * [GeoServer now supports Vector Footprints for ImageMosaic](http://www.geo-solutions.it/blog/geoserver-supports-footprints-imagemosaic/)

	
  * [Harvesting Metadata using CSW](http://boundlessgeo.com/2014/04/harvesting-metadata-using-csw/)

	
  * [Caveats in GeoServer JNDI configuration](http://www.geo-solutions.it/blog/developers-corner-caveats-geoserver-jndi-configuration/)

	
  * [Supporting Wind Barbs In GeoServer and GeoTools](http://www.geo-solutions.it/blog/developers-corner-supporting-wind-barbs-geoserver-geotools/)

	
  * [Deterministic rendering order in SLDs](http://boundlessgeo.com/2014/04/deterministic-rendering-order-in-sld/)

	
  * [Secure GeoServer connections to Postgres for Heroku](http://boundlessgeo.com/2014/02/secure-connections-heroku/)

	
  * [Labelling a MultiPoint geometry with WPS](http://boundlessgeo.com/2014/02/labelling-a-multipoint-geometry-with-wps/)

	
  * GeoServer 2.5-beta announcement reviews [key features of this release](http://blog.geoserver.org/2014/01/21/geoserver-2-5-beta-released/):

	
    * WCS 2.0 and WCS 2.0 Earth Observation have been added (thanks to DLR and Eumesat for funding this)

	
    * The addition of a batch importer to making setting up GeoServer easier (thanks to [MapStory](http://mapstory.org/)).

	
    * High performance PNG encoder based on [PNGJ library](https://code.google.com/p/pngj/) (Andrea Aime). Improved JPEG performance using [libjpegturbo](http://libjpeg-turbo.virtualgl.org/) available as an optional extension (Simone Giannecchini and Daniele Romagnoli)

	
    * Use of ST_Simplify to improve PostGIS rendering performance (a collaboration with Andrea and Jonathan Moules).

	
    * New implementation of GetFeatureInfo that takes into account symbol shapes, offsets, and dynamic line widths into account (thanks to Eskilstuna municipality for funding this).




	
  * [Using GeoServer at IGN to create new digital maps](http://blog.geoserver.org/2014/01/07/using-geoserver-at-ign-the-french-national-mapping-agency-to-create-new-digital-maps/) is an impressive look at advanced styling deployed by the french mapping agency

	
  * [Labelling a MultiPoint geometry with WPS](http://boundlessgeo.com/2014/02/labelling-a-multipoint-geometry-with-wps/) (Boundless) is a good example of integrating WPS and Styling

	
  * [Achieving extreme GeoServer Scalability with new Marlin vector rasterizer](http://geo-solutions.blogspot.it/2014/02/geoserver-improved-scalability.html) (GeoSolutions) shows an exciting JRE extension that can be used for improved performance. If you are using GeoServer with a large number of CPU cores you owe yourself an hour to try this out.

	
  * [DXF output format promoted to official extension for GeoServer](http://geo-solutions.blogspot.it/2014/01/geoserver-dxf.html) (GeoSolutions)

	
  * [Active Directory based security in GeoServer through LDAP](http://geo-solutions.blogspot.it/2014/01/geoserver-activedirectory.html) (GeoSolutions)



