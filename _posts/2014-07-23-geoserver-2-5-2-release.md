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

	
  * Check the [release notes](#release-notes) for more details

	
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

	
  * GeoServer 2.5-beta announcement reviews [key features of this release]({% post_url 2014-01-21-geoserver-2-5-beta-released %}):

	
    * WCS 2.0 and WCS 2.0 Earth Observation have been added (thanks to DLR and Eumesat for funding this)

	
    * The addition of a batch importer to making setting up GeoServer easier (thanks to [MapStory](http://mapstory.org/)).

	
    * High performance PNG encoder based on [PNGJ library](https://code.google.com/p/pngj/) (Andrea Aime). Improved JPEG performance using [libjpegturbo](http://libjpeg-turbo.virtualgl.org/) available as an optional extension (Simone Giannecchini and Daniele Romagnoli)

	
    * Use of ST_Simplify to improve PostGIS rendering performance (a collaboration with Andrea and Jonathan Moules).

	
    * New implementation of GetFeatureInfo that takes into account symbol shapes, offsets, and dynamic line widths into account (thanks to Eskilstuna municipality for funding this).




	
  * [Using GeoServer at IGN to create new digital maps]({% post_url 2014-01-07-using-geoserver-at-ign-the-french-national-mapping-agency-to-create-new-digital-maps %}) is an impressive look at advanced styling deployed by the french mapping agency

	
  * [Labelling a MultiPoint geometry with WPS](http://boundlessgeo.com/2014/02/labelling-a-multipoint-geometry-with-wps/) (Boundless) is a good example of integrating WPS and Styling

	
  * [Achieving extreme GeoServer Scalability with new Marlin vector rasterizer](http://geo-solutions.blogspot.it/2014/02/geoserver-improved-scalability.html) (GeoSolutions) shows an exciting JRE extension that can be used for improved performance. If you are using GeoServer with a large number of CPU cores you owe yourself an hour to try this out.

	
  * [DXF output format promoted to official extension for GeoServer](http://geo-solutions.blogspot.it/2014/01/geoserver-dxf.html) (GeoSolutions)

	
  * [Active Directory based security in GeoServer through LDAP](http://geo-solutions.blogspot.it/2014/01/geoserver-activedirectory.html) (GeoSolutions)

## Release notes

New Feature:

* [GEOS-6514](https://osgeo-org.atlassian.net/browse/GEOS-6514) Restrict MIME types for WMS GetMap and GetFeatureInfo requests

Improvement:

* [GEOS-6541](https://osgeo-org.atlassian.net/browse/GEOS-6541) Document usage of transformation functions in CSS
* [GEOS-6569](https://osgeo-org.atlassian.net/browse/GEOS-6569) Support booleans in MapJSONFormat

Bug:

* [GEOS-4834](https://osgeo-org.atlassian.net/browse/GEOS-4834) Animated GIF do not properly support transparency
* [GEOS-4943](https://osgeo-org.atlassian.net/browse/GEOS-4943) /geoserver/accessDenied.jsp not found
* [GEOS-5318](https://osgeo-org.atlassian.net/browse/GEOS-5318) cross-site scripting vulnerability in layer preview pages
* [GEOS-5545](https://osgeo-org.atlassian.net/browse/GEOS-5545) Two different SLD's that seem to be connected
* [GEOS-5676](https://osgeo-org.atlassian.net/browse/GEOS-5676) Add information about strong cryptography installation in the user guide
* [GEOS-6385](https://osgeo-org.atlassian.net/browse/GEOS-6385) Rendering-based GetFeatureInfo does not work properly against polygons stroked but not filled
* [GEOS-6386](https://osgeo-org.atlassian.net/browse/GEOS-6386) Problems with SQL-Views in PostGIS
* [GEOS-6441](https://osgeo-org.atlassian.net/browse/GEOS-6441) Geometries jumping the dateline generate reprojection artifacts on datum shift
* [GEOS-6476](https://osgeo-org.atlassian.net/browse/GEOS-6476) Animate reflector request fails due to NPE in WMS-EO Plugin
* [GEOS-6493](https://osgeo-org.atlassian.net/browse/GEOS-6493) WFS GetFeature with feature bounds enabled can leak connections
* [GEOS-6501](https://osgeo-org.atlassian.net/browse/GEOS-6501) Links in workspace specific WPS GetCapabilities are incorrect
* [GEOS-6503](https://osgeo-org.atlassian.net/browse/GEOS-6503) WPS won't work with  workspace specific urls, a 404 is returned
* [GEOS-6504](https://osgeo-org.atlassian.net/browse/GEOS-6504) If one of the top level service configuration files fails to load, the whole startup fails
* [GEOS-6548](https://osgeo-org.atlassian.net/browse/GEOS-6548) Java 7 Security Policy
* [GEOS-6549](https://osgeo-org.atlassian.net/browse/GEOS-6549) CSS Module takes a long time to Submit on certain CSS (Weird Issue)
* [GEOS-6552](https://osgeo-org.atlassian.net/browse/GEOS-6552) GeoServer WPS python script does not work for Layer results
* [GEOS-6564](https://osgeo-org.atlassian.net/browse/GEOS-6564) WCS GranuleStack for mosaic contains duplicate entries
* [GEOS-6575](https://osgeo-org.atlassian.net/browse/GEOS-6575) Rapid Concurrent REST usage can invalidate DataStore still being used
* [GEOS-6582](https://osgeo-org.atlassian.net/browse/GEOS-6582) GeoServer fails to report the current process task in the status response

Task:

* [GEOS-6537](https://osgeo-org.atlassian.net/browse/GEOS-6537) Improve documentation about JNDI connection pool configuration
* [GEOS-6577](https://osgeo-org.atlassian.net/browse/GEOS-6577) Update imageio-ext version referred in the docs
* [GEOS-6580](https://osgeo-org.atlassian.net/browse/GEOS-6580) OWS Dispatcher log could be improved
