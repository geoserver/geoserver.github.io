---
author: geoserver
comments: true
date: 2014-07-23 16:18:23+00:00
layout: post
link: http://blog.geoserver.org/2014/07/23/geoserver-2-5-2-release/
slug: geoserver-2-5-2-release
title: GeoServer 2.5.2 release
wordpress_id: 1904
tags:
- release
- stable
---

The GeoServer team is happy to announce the release of [GeoServer 2.5.2](http://geoserver.org/release/2.5.2/). Download bundles are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5.2/geoserver-2.5.2-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5.2/geoserver-2.5.2-war.zip), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5.2/geoserver-2.5.2.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5.2/geoserver-2.5.2.exe/download))  along with documentation and extensions.

GeoServer 2.5.2 is the next the stable release of GeoServer and is recommended for production deployment. Thanks to everyone taking part, submitting fixes and new functionality:



	
  * Some fixes in the new GetFeatureInfo engine, for unfilled polygons and dashed lines

	
  * Solved a configuration issue that might have linked two styles toghether (edit one, the other changed as well)

	
  * DBMS connection leak in some WFS GetFeature with bounds enabled

	
  * Have WPS work properly as a workspace specific service, and report the current process activity during asynchronous requests (for processes that do report what they are doing in plain english, besides offering a progress percentage)

	
  * Add a way to resctrict output formats supported by WMS GetMap and GetFeatureInfo

	
  * More docs on how to setup JNDI connection pools in GeoServer

	
  * Thanks to Andrea (GeoSolutions) for publishing this release

	
  * Check the [release notes](https://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20399) for more details

	
  * This release is made in conjunction with GeoTools 11.2




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



