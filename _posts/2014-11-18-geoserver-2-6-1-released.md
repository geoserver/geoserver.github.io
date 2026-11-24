---
author: geoserver
comments: true
date: 2014-11-18 09:06:14+00:00
layout: post
link: http://blog.geoserver.org/2014/11/18/geoserver-2-6-1-released/
slug: geoserver-2-6-1-released
title: GeoServer 2.6.1 released
wordpress_id: 2041
---

The GeoServer team is happy to announce the release of [GeoServer 2.6.1](http://geoserver.org/release/2.6.1/). Download bundles are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.1/geoserver-2.6.1-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.1/geoserver-2.6.1-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.1/geoserver-2.6.1.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.1/geoserver-2.6.1.exe/download))  along with documentation and extensions.

GeoServer 2.6.1 is the next the stable release of GeoServer and is recommended for production deployment. Thanks to everyone taking part, submitting fixes and new functionality:



	
  * Fix for slow rendering of maps with lots of layers coming from a spatial database, reported by numerous users

	
  * Improvements in rendering labels over transparent maps

	
  * Fix for rendering tiled raster data, it could occasionally miss portions of the data

	
  * Fixes for WFS 2.0 joins

	
  * Better memory management when HTTP gzip-ping large amounts of GML/CSV/JSON data

	
  * Multidimensional WCS 2.0 outputs (NetCDF downloads) now support subsetting in CRS other than WGS84

	
  * An option to disable JAI native warp, which can cause some instability when reprojecting certain raster data sets

	
  * Some improvements in the GeoPackage outputs (still a community module, available via nightly builds)

	
  * Check the [release notes](#release-notes) for more details

	
  * This release is made in conjunction with GeoTools 12.1


Thanks to Andrea (GeoSolutions) for this release


# About GeoServer 2.6


Articles and resources for GeoServer 2.6 series:



	
  * [GeoServer at FOSS4G]({% post_url 2014-10-01-geoserver-at-foss4g %})

	
    * [State of GeoServer and GeoTools 2014](http://vimeo.com/106835755) ([slides](http://www.slideshare.net/jgarnett/state-of-geoserver-geotools-and-friends-2014))




	
  * [Raster Views in GeoServer via the CoverageView concept](http://www.geo-solutions.it/blog/overageview-concept-for-geoserver/) (GeoSolutions)

	
  * [Advanced Raster Projection in GeoServer](http://www.geo-solutions.it/blog/developers-corner-advanced-raster-projection-geoserver/) (GeoSolutions)

	
  * [Supporting Wind Barbs In GeoServer and GeoTools](http://www.geo-solutions.it/blog/developers-corner-supporting-wind-barbs-geoserver-geotools/) (GeoSolutions)

	
  * [GeoServer now supports Vector Footprints for ImageMosaic](http://www.geo-solutions.it/blog/geoserver-supports-footprints-imagemosaic/) (GeoSolutions)

	
  * [2.6.0 announcement]({% post_url 2014-10-03-geoserver-2-6-0-released %}) and [change log]({% post_url 2014-10-03-geoserver-2-6-0-released %}#release-notes)

	
  * [2.6-RC1 announcement]({% post_url 2014-08-19-geoserver-2-6-rc1-released %}) and [change log]({% post_url 2014-08-19-geoserver-2-6-rc1-released %}#release-notes)

	
  * [2.6-beta announcement]({% post_url 2014-07-24-geoserver-2-6-beta-released %}) and [change log]({% post_url 2014-07-24-geoserver-2-6-beta-released %}#release-notes)

## Release notes

Improvement:

* [GEOS-5034](https://osgeo-org.atlassian.net/browse/GEOS-5034) Non-advertised layers should appear in the layer-specific virtual service GetCapabilities document
* [GEOS-6603](https://osgeo-org.atlassian.net/browse/GEOS-6603) Add a button for disabling native warp
* [GEOS-6681](https://osgeo-org.atlassian.net/browse/GEOS-6681) New REST GET parameter for disabling exception logging when 404 is returned
* [GEOS-6697](https://osgeo-org.atlassian.net/browse/GEOS-6697) Avoid adding "null" messages in exception reports
* [GEOS-6708](https://osgeo-org.atlassian.net/browse/GEOS-6708) Allow GeoPkg datastore to create data stores relative to data directory.
* [GEOS-6711](https://osgeo-org.atlassian.net/browse/GEOS-6711) Introduce mapper parameters and webservice based mapper in authkey
* [GEOS-6717](https://osgeo-org.atlassian.net/browse/GEOS-6717) Improve store param hover labels

Bug:

* [GEOS-5149](https://osgeo-org.atlassian.net/browse/GEOS-5149) WFS 2.0 spatial join failed
* [GEOS-5312](https://osgeo-org.atlassian.net/browse/GEOS-5312) CSV WFS output format doesn't deal with Windows newlines
* [GEOS-5486](https://osgeo-org.atlassian.net/browse/GEOS-5486) Poor text with java 7 and Transparency
* [GEOS-6426](https://osgeo-org.atlassian.net/browse/GEOS-6426) Administration UI does not work properly with Internet Explorer 11
* [GEOS-6686](https://osgeo-org.atlassian.net/browse/GEOS-6686) MBTiles and GeoPkg are not correctly shown in LayerPreview available formats
* [GEOS-6691](https://osgeo-org.atlassian.net/browse/GEOS-6691) Geoserver causes a query SELECT NULL AS TABLE_CAT... to be generated by JDBC over and over again
* [GEOS-6692](https://osgeo-org.atlassian.net/browse/GEOS-6692) multidimensional output in WCS 2.0 only supports WGS84 subsetting
* [GEOS-6693](https://osgeo-org.atlassian.net/browse/GEOS-6693) Demo request page can product bad urls without slash
* [GEOS-6701](https://osgeo-org.atlassian.net/browse/GEOS-6701) Provide better error messages when wfs sortby attribute does not exists
* [GEOS-6703](https://osgeo-org.atlassian.net/browse/GEOS-6703) IOUtils.zipDirectory created zip without directory entries
* [GEOS-6707](https://osgeo-org.atlassian.net/browse/GEOS-6707) SortBy property name validation breaks app-schema
* [GEOS-6714](https://osgeo-org.atlassian.net/browse/GEOS-6714) Geoserver Logs page inaccessible
* [GEOS-6719](https://osgeo-org.atlassian.net/browse/GEOS-6719) Shapefile output format can leak JDBC connections
* [GEOS-6733](https://osgeo-org.atlassian.net/browse/GEOS-6733) Database performance regression
* [GEOS-6735](https://osgeo-org.atlassian.net/browse/GEOS-6735) CSSHandler leaves file handles open
* [GEOS-6748](https://osgeo-org.atlassian.net/browse/GEOS-6748) PointPlacement with Rotation in TextSymbolizer gives NullPointerException
* [GEOS-6750](https://osgeo-org.atlassian.net/browse/GEOS-6750) Raster rendering might read a row/col less in some cases
* [GEOS-6751](https://osgeo-org.atlassian.net/browse/GEOS-6751) WFS can OOM when gzipping large compressible output
* [GEOS-6762](https://osgeo-org.atlassian.net/browse/GEOS-6762) CSW capabilities param/constraints section can grow indefinitely when using a CSW CapabilitiesDecorator
* [GEOS-6763](https://osgeo-org.atlassian.net/browse/GEOS-6763) polygon.xml generated with reference to default_line.sld
* [GEOS-6802](https://osgeo-org.atlassian.net/browse/GEOS-6802) WFS Features are read from external server but not delivered, potentially related to "gml:Surface"
* [GEOS-6852](https://osgeo-org.atlassian.net/browse/GEOS-6852) Position error for raster in an image mosaic
