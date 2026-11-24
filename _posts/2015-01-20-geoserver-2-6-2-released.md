---
author: geoserver
comments: true
date: 2015-01-20 10:48:15+00:00
layout: post
link: http://blog.geoserver.org/2015/01/20/geoserver-2-6-2-released/
slug: geoserver-2-6-2-released
title: GeoServer 2.6.2 released
wordpress_id: 2066
---

The GeoServer team is happy to announce the release of [GeoServer 2.6.2](http://geoserver.org/release/2.6.2/). Download bundles are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.2/geoserver-2.6.2-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.2/geoserver-2.6.2-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.2/geoserver-2.6.2.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.2/geoserver-2.6.2.exe/download))  along with documentation and extensions.

GeoServer 2.6.2 is the next the stable release of GeoServer and is recommended for production deployment. Thanks to everyone taking part, submitting fixes and new functionality:



	
  * The issue with GZIP encoding breaking CSS download in some browsers has been fixed

	
  * Have the pre-generalized store use again the simplified geometries against the PostGIS store (regressed in 2.6.0)

	
  * Relative paths in SLD using a "file://image.png" syntax are supported again (regressed in 2.6.0)

	
  * Removing also layer groups and styles contained in the workspace when the workspace is deleted

	
  * Make WCS 2.0 / WCS EO more lenient when the workspace is not specified in requests, or when a single mosaic granule is requested in EO requests

	
  * Allow disabling "advanced projection handling" for raster data via a system variable (for the few cases in which it misbehaves, fixes are underway, please do report if you see issues)

	
  * A number of minor fixes to WCS capabilities and GetCoverage handling

	
  * Added icelandic language support in the INSPIRE plugin

	
  * Check the [release notes](#release-notes) for more details

	
  * This release is made in conjunction with GeoTools 12.2


Thanks to Andrea (GeoSolutions), Jody and Kevin (Boundless) for this release


# About GeoServer 2.6


Articles and resources for GeoServer 2.6 series:



	
  * [GeoServer at FOSS4G]({% post_url 2014-10-01-geoserver-at-foss4g %})

	
    * [State of GeoServer and GeoTools 2014](http://vimeo.com/106835755) ([slides](http://www.slideshare.net/jgarnett/state-of-geoserver-geotools-and-friends-2014))




	
  * [Raster Views in GeoServer via the CoverageView concept](http://www.geo-solutions.it/blog/overageview-concept-for-geoserver/) (GeoSolutions)

	
  * [Advanced Raster Projection in GeoServer](http://www.geo-solutions.it/blog/developers-corner-advanced-raster-projection-geoserver/) (GeoSolutions)

	
  * [Supporting Wind Barbs In GeoServer and GeoTools](http://www.geo-solutions.it/blog/developers-corner-supporting-wind-barbs-geoserver-geotools/) (GeoSolutions)

	
  * [GeoServer now supports Vector Footprints for ImageMosaic](http://www.geo-solutions.it/blog/geoserver-supports-footprints-imagemosaic/) (GeoSolutions)

	
  * [2.6.0 announcement]({% post_url 2014-10-03-geoserver-2-6-0-released %}) and [change log]({% post_url 2014-10-03-geoserver-2-6-0-released %}#release-notes)

	
  * [2.6-RC1 announcement]({% post_url 2014-08-19-geoserver-2-6-rc1-released %}) and [change log]({% post_url 2014-08-19-geoserver-2-6-rc1-released %}#release-notes)

	
  * [2.6-beta announcement]({% post_url 2014-07-24-geoserver-2-6-beta-released %}) and [change log]({% post_url 2014-07-24-geoserver-2-6-beta-released %}#release-notes)

## Release notes

Improvement:

* [GEOS-6759](https://osgeo-org.atlassian.net/browse/GEOS-6759) Add support for OverviewManagement in WCS2.0 getCoverage requests
* [GEOS-6800](https://osgeo-org.atlassian.net/browse/GEOS-6800) sldservice: improvements to docs, tests and some bugfixes
* [GEOS-6803](https://osgeo-org.atlassian.net/browse/GEOS-6803) Add a system variable to disable advanced raster projection  for direct raster rendering
* [GEOS-6805](https://osgeo-org.atlassian.net/browse/GEOS-6805) Support for WCS 2.0 request without defining workspace in coverageId
* [GEOS-6808](https://osgeo-org.atlassian.net/browse/GEOS-6808) WCS-EO DescribeEOCoverageSet should be more lenient about time parsing
* [GEOS-6809](https://osgeo-org.atlassian.net/browse/GEOS-6809) WCS 2.0 DescribeCoverage should be able to handle single granules

Bug:

* [GEOS-6395](https://osgeo-org.atlassian.net/browse/GEOS-6395) WMS Animator parameter is misspelled
* [GEOS-6573](https://osgeo-org.atlassian.net/browse/GEOS-6573) `<Priority>` tag not processed by SLD1.1 engine
* [GEOS-6627](https://osgeo-org.atlassian.net/browse/GEOS-6627) GWC causes a wrong handling of the ImageIO and ImageIO-Ext plugins
* [GEOS-6687](https://osgeo-org.atlassian.net/browse/GEOS-6687) INSPIRE extension misses the icelandic language
* [GEOS-6723](https://osgeo-org.atlassian.net/browse/GEOS-6723) Pregeneralized Features module not using extra geometries against PostGIS store
* [GEOS-6752](https://osgeo-org.atlassian.net/browse/GEOS-6752) Styles and layer groups contained in a workspace are not removed when the workspace is deleted
* [GEOS-6757](https://osgeo-org.atlassian.net/browse/GEOS-6757) WCS 2.0 should force latLon only when the related flag is enabled
* [GEOS-6772](https://osgeo-org.atlassian.net/browse/GEOS-6772) CRS Transformation breaks BBOX validation in GetFeature in strict CITE compliance mode
* [GEOS-6775](https://osgeo-org.atlassian.net/browse/GEOS-6775) Slow web UI with Firefox
* [GEOS-6779](https://osgeo-org.atlassian.net/browse/GEOS-6779) Test failure on netcdf-out build
* [GEOS-6782](https://osgeo-org.atlassian.net/browse/GEOS-6782) NPE after WCS GetCoverage request for nonexistent coverage
* [GEOS-6783](https://osgeo-org.atlassian.net/browse/GEOS-6783) CoverageViewReader should setup a compliant ImageLayout
* [GEOS-6785](https://osgeo-org.atlassian.net/browse/GEOS-6785) WCS GetCapabilities 1.1.1 has invalid metadataType attribute
* [GEOS-6827](https://osgeo-org.atlassian.net/browse/GEOS-6827) Regression: Resource refactor broke relative graphic url using "file://" protocol
* [GEOS-6940](https://osgeo-org.atlassian.net/browse/GEOS-6940) Exception on Layer Preview
