---
author: geoserver
comments: true
date: 2014-10-24 13:16:02+00:00
layout: post
link: http://blog.geoserver.org/2014/10/24/geoserver-2-5-3-released/
slug: geoserver-2-5-3-released
title: GeoServer 2.5.3 released
wordpress_id: 2036
---

The GeoServer team is happy to announce the release of [GeoServer 2.5.3](http://geoserver.org/release/2.5.3/). Download bundles are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5.3/geoserver-2.5.3-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5.3/geoserver-2.5.3-war.zip), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5.3/geoserver-2.5.3.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5.3/geoserver-2.5.3.exe/download))  along with documentation and extensions.

GeoServer 2.5.3 is the next the stable release of GeoServer and is recommended for production deployment. Thanks to everyone taking part, submitting fixes and new functionality:



	
  * A new process, PagedUnique, to efficiently grab large amounts of unique values from a layer column

	
  * Legend preview functionality in the style editor

	
  * A long awaited fix for poor font rendering when creating transparent map

	
  * Some fixes in WFS 2.0 joins

	
  * GeoJSON CRS syntax has been updated to the current valid one (we were using a old legacy one)

	
  * Some GetFeatureInfo further fixes for complex styles

	
  * Fix scale computation when the CRS unit of measure is not meters

	
  * Some WMS 1.3 rendering fixes with image mosaics

	
  * Avoid invalid reports of leaked connections when using SHAPE-ZIP output format against SQL views whose SQL is no more valid

	
  * Check the [release notes](#release-notes) for more details

	
  * This release is made in conjunction with GeoTools 11.3




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

* [GEOS-6530](https://osgeo-org.atlassian.net/browse/GEOS-6530) WPS PagedUnique Process

Improvement:

* [GEOS-5034](https://osgeo-org.atlassian.net/browse/GEOS-5034) Non-advertised layers should appear in the layer-specific virtual service GetCapabilities document
* [GEOS-6409](https://osgeo-org.atlassian.net/browse/GEOS-6409) Building the PDF Docs fails
* [GEOS-6491](https://osgeo-org.atlassian.net/browse/GEOS-6491) Add legend preview in the style edit pages
* [GEOS-6597](https://osgeo-org.atlassian.net/browse/GEOS-6597) Avoid full namespace scan for GetFeature requests
* [GEOS-6697](https://osgeo-org.atlassian.net/browse/GEOS-6697) Avoid adding "null" messages in exception reports
* [GEOS-6711](https://osgeo-org.atlassian.net/browse/GEOS-6711) Introduce mapper parameters and webservice based mapper in authkey
* [GEOS-6717](https://osgeo-org.atlassian.net/browse/GEOS-6717) Improve store param hover labels

Bug:

* [GEOS-5149](https://osgeo-org.atlassian.net/browse/GEOS-5149) WFS 2.0 spatial join failed
* [GEOS-5312](https://osgeo-org.atlassian.net/browse/GEOS-5312) CSV WFS output format doesn't deal with Windows newlines
* [GEOS-5486](https://osgeo-org.atlassian.net/browse/GEOS-5486) Poor text with java 7 and Transparency
* [GEOS-5571](https://osgeo-org.atlassian.net/browse/GEOS-5571) GwcSettingsPage WicketException if the user adds a new standard gridset
* [GEOS-5996](https://osgeo-org.atlassian.net/browse/GEOS-5996) The GeoJSON outputs the legacy crs syntax
* [GEOS-6186](https://osgeo-org.atlassian.net/browse/GEOS-6186) Some files that should probably reside in GEOSERVER_DATA_DIR are placed in working directory
* [GEOS-6323](https://osgeo-org.atlassian.net/browse/GEOS-6323) Take ND coverages dimensions into account when checking size limits
* [GEOS-6379](https://osgeo-org.atlassian.net/browse/GEOS-6379) Unable to add new default gridsets
* [GEOS-6489](https://osgeo-org.atlassian.net/browse/GEOS-6489) Reading SLD by REST changes attribute value breaks geoserver on update
* [GEOS-6502](https://osgeo-org.atlassian.net/browse/GEOS-6502) stroke-Dasharray style partially breaks WMS getfeatureinfo
* [GEOS-6519](https://osgeo-org.atlassian.net/browse/GEOS-6519) WPS not enabling in workspace
* [GEOS-6529](https://osgeo-org.atlassian.net/browse/GEOS-6529) NullPointerException in AdvancedDispatchFilter, seen when geoserver-monitoring included
* [GEOS-6570](https://osgeo-org.atlassian.net/browse/GEOS-6570) rendering regression with geoserver 2.5.1 when WMS 1.3.0
* [GEOS-6572](https://osgeo-org.atlassian.net/browse/GEOS-6572) WMS GetFeatureInfo Request Returns Too Many Features
* [GEOS-6578](https://osgeo-org.atlassian.net/browse/GEOS-6578) Unable to unwrap OracleConnection from JBoss WrappedConnectionJDK6
* [GEOS-6596](https://osgeo-org.atlassian.net/browse/GEOS-6596) Point symbols clipped on tile edge
* [GEOS-6598](https://osgeo-org.atlassian.net/browse/GEOS-6598) Enhancement for the VectorRenderingLayerIdentifier
* [GEOS-6604](https://osgeo-org.atlassian.net/browse/GEOS-6604) WMS GetFeatureInfo using 'vendorParams: propertyName' does not working after upgrade to 2.5.x
* [GEOS-6616](https://osgeo-org.atlassian.net/browse/GEOS-6616) Clear cached attribute information during FeatureType DELETE
* [GEOS-6617](https://osgeo-org.atlassian.net/browse/GEOS-6617) Scale computation is wrong when the map is expressed in a unit other than meters
* [GEOS-6619](https://osgeo-org.atlassian.net/browse/GEOS-6619) Rendering based feature info will return just one geometry of the group that falls into the same pixel
* [GEOS-6628](https://osgeo-org.atlassian.net/browse/GEOS-6628) NullPointerException when setting empty ParameterFilter in the Layer Caching Panel
* [GEOS-6632](https://osgeo-org.atlassian.net/browse/GEOS-6632) Cross-site scripting vulnerability in WMS exceptions
* [GEOS-6641](https://osgeo-org.atlassian.net/browse/GEOS-6641) WCS Helper gridCoverageRequests multidim splitter doesn't close Featureiterator
* [GEOS-6645](https://osgeo-org.atlassian.net/browse/GEOS-6645) NPE when trying to reload bands with empty range
* [GEOS-6649](https://osgeo-org.atlassian.net/browse/GEOS-6649) Update headers to (c) OSGeo
* [GEOS-6651](https://osgeo-org.atlassian.net/browse/GEOS-6651) ImageMosaic layers do not show images when version=1.3.0
* [GEOS-6701](https://osgeo-org.atlassian.net/browse/GEOS-6701) Provide better error messages when wfs sortby attribute does not exists
* [GEOS-6707](https://osgeo-org.atlassian.net/browse/GEOS-6707) SortBy property name validation breaks app-schema
* [GEOS-6714](https://osgeo-org.atlassian.net/browse/GEOS-6714) Geoserver Logs page inaccessible
* [GEOS-6719](https://osgeo-org.atlassian.net/browse/GEOS-6719) Shapefile output format can leak JDBC connections
* [GEOS-6762](https://osgeo-org.atlassian.net/browse/GEOS-6762) CSW capabilities param/constraints section can grow indefinitely when using a CSW CapabilitiesDecorator
