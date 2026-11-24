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

	
  * Check the [release notes](#release-notes) for more details

	
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

* [GEOS-6449](https://osgeo-org.atlassian.net/browse/GEOS-6449) Create GRIB community module

Improvement:

* [GEOS-5550](https://osgeo-org.atlassian.net/browse/GEOS-5550) Top/Bottom statement on Layers Group
* [GEOS-5964](https://osgeo-org.atlassian.net/browse/GEOS-5964) Make GeoServer nodes in a cluster identifiable by label and color in the UI
* [GEOS-6372](https://osgeo-org.atlassian.net/browse/GEOS-6372) Add coverageBands customization capability on layer configuration
* [GEOS-6408](https://osgeo-org.atlassian.net/browse/GEOS-6408) Provide better logging when required to fall back on embedded data directory
* [GEOS-6455](https://osgeo-org.atlassian.net/browse/GEOS-6455) GridCoverageFactory hints initialization
* [GEOS-6465](https://osgeo-org.atlassian.net/browse/GEOS-6465) autoWrap should count "(" as being within the same string

Bug:

* [GEOS-4023](https://osgeo-org.atlassian.net/browse/GEOS-4023) layer desactivated when we push a SLD file with REST API
* [GEOS-5511](https://osgeo-org.atlassian.net/browse/GEOS-5511) Help icons on various GWC pages do nothing
* [GEOS-5532](https://osgeo-org.atlassian.net/browse/GEOS-5532) Renaming workspaces doesn't translate over to Tile Caches
* [GEOS-6109](https://osgeo-org.atlassian.net/browse/GEOS-6109) CAS login request exposes internal server URL
* [GEOS-6110](https://osgeo-org.atlassian.net/browse/GEOS-6110) CAS logout request is incorrect
* [GEOS-6114](https://osgeo-org.atlassian.net/browse/GEOS-6114) Request URL in Demo Requests exposes internal server URL
* [GEOS-6320](https://osgeo-org.atlassian.net/browse/GEOS-6320) When migrating layergroups from 2.3.x Web Admin UI can fail
* [GEOS-6410](https://osgeo-org.atlassian.net/browse/GEOS-6410) LookAt value in SimpleNetworkLinkBuilder not set correctly
* [GEOS-6411](https://osgeo-org.atlassian.net/browse/GEOS-6411) Time and elevation parameter is not passed in KML export
* [GEOS-6413](https://osgeo-org.atlassian.net/browse/GEOS-6413) The new KML encoder can leak unclosed feature iterators
* [GEOS-6414](https://osgeo-org.atlassian.net/browse/GEOS-6414) WMS-T time range query incorrect
* [GEOS-6420](https://osgeo-org.atlassian.net/browse/GEOS-6420) WMS GetFeatureInfo does reproject the featureMember geometry in GeoServer 2.5
* [GEOS-6424](https://osgeo-org.atlassian.net/browse/GEOS-6424) Importer fails to import into Oracle data in geographic coordinates
* [GEOS-6440](https://osgeo-org.atlassian.net/browse/GEOS-6440) Advanced projection handling is not enabled in WMS 1.3
* [GEOS-6448](https://osgeo-org.atlassian.net/browse/GEOS-6448) WPS RangeLookupTest Java 7 Failure
* [GEOS-6452](https://osgeo-org.atlassian.net/browse/GEOS-6452) CAS doesn't work with GeoServer 2.5
* [GEOS-6453](https://osgeo-org.atlassian.net/browse/GEOS-6453) ImageMosaic regression - WMS requests take forever to serve
* [GEOS-6454](https://osgeo-org.atlassian.net/browse/GEOS-6454) Gray + alpha images not rendered encoded correctly in PNG
* [GEOS-6463](https://osgeo-org.atlassian.net/browse/GEOS-6463) WMS 1.3 GetCapabilities with JDBCConfig throws ClassCastException
* [GEOS-6471](https://osgeo-org.atlassian.net/browse/GEOS-6471) GetFeatureWithLock expiry is not parsed when using WFS 1.1 POST requests
* [GEOS-6486](https://osgeo-org.atlassian.net/browse/GEOS-6486) WCS 1.0 capabilities generation fails when using multi-coverage readers
* [GEOS-6487](https://osgeo-org.atlassian.net/browse/GEOS-6487) Coverage band customization fails against old raster layers (making the layer unusable)
* [GEOS-6531](https://osgeo-org.atlassian.net/browse/GEOS-6531) Features disappear when I dezoom too much in WMS layer
* [GEOS-6554](https://osgeo-org.atlassian.net/browse/GEOS-6554) Sql view with oracle in Geoserver 2.5
* [GEOS-6563](https://osgeo-org.atlassian.net/browse/GEOS-6563) SQL Server import doesn't preserve geometry SRID's
* [GEOS-6594](https://osgeo-org.atlassian.net/browse/GEOS-6594) POLYGON layer from PostGIS renders white tiles

Task:

* [GEOS-3662](https://osgeo-org.atlassian.net/browse/GEOS-3662) Documentation for jp2kak extension
* [GEOS-6339](https://osgeo-org.atlassian.net/browse/GEOS-6339) Add documentation to ImageMosaic module
* [GEOS-6377](https://osgeo-org.atlassian.net/browse/GEOS-6377) Support null values on WCS 2.0 DescribeCoverage
