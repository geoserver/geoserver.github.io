---
author: geoserver
comments: true
date: 2011-10-07 10:30:20+00:00
layout: post
link: http://blog.geoserver.org/2011/10/07/geoserver-2-1-2-release/
slug: geoserver-2-1-2-release
title: GeoServer 2.1.2 Released
wordpress_id: 1013
categories:
- Announcements
---

The GeoServer team is pleased to announce the release of GeoServer 2.1.2. This is mostly a bug-fixing release, with a number of minor improvements in the administration UI and REST configuration. There are however a couple new features that you might be interested in:



	
  * The ability to mark a layer as "non advertised". Layers flagged this way won't appear in the capabilities document, making it a good way to add a layer group without having to tell the world about the layers included in it, and for any "work in progress" or temporary layer that the administrator does not want the world to see.

	
  * The imagemosaic-jdbc extension learned to load raster data from [PostGIS 2.0 WKT raster](http://trac.osgeo.org/postgis/wiki/WKTRaster). Mind, the support is pretty new and the [configuration](http://docs.geotools.org/latest/userguide/library/coverage/pgraster.html) is not for the faint of heart, but we're excited about this new developement and look forward to learn about how it works for you. Thanks to Christian Mueller for working on this.


We would also like to thank some GeoServer users that went the extra mile and contributed code and documentation patches for this release:

	
  * Lucas Heezen for contributing a REST configuration flag that allows to filter out geometryless feature types from a store ([GEOS-4741](https://osgeo-org.atlassian.net/browse/GEOS-4741))

	
  * John Hudson for adding the "ISO 19115:2003" as a type option in Layer Metadata URL ([GEOS-4595](https://osgeo-org.atlassian.net/browse/GEOS-4595))

	
  * German Osin for making sure stores are workspace qualified in REST config feature type list ([GEOS-4772](https://osgeo-org.atlassian.net/browse/GEOS-4772))

	
  * Milton Jonathan for fixing an issue occurring in REST config when switching a layer from one store to another ([GEOS-4740](https://osgeo-org.atlassian.net/browse/GEOS-4740))

	
  * Tony Young for a automatic configuration of SRS and bounds when publishing a layer via REST config ([GEOS-4596](https://osgeo-org.atlassian.net/browse/GEOS-4596))

	
  * Tim Schaub for fixing a double encoding issue in WFS exception reporting ([GEOS-4680](https://osgeo-org.atlassian.net/browse/GEOS-4680))

	
  * David Collins for a number of improvements to the user guide


Contributions like these help keep GeoServer responsive to the needs of our community and allow us to continue providing a stable and useful product. Thank you!
Thanks also go to [GeoSolutions](http://www.geo-solutions.it/) for sponsoring this release.

Please download GeoServer 2.1.2, try it out, and provide feedback on the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users). Your feedback helps GeoServer to continue to improve.

----

## GeoServer 2.1.2

Released on October 6, 2011

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/geoserver-2.1.2-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/geoserver-2.1.2-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/geoserver-2.1.2.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/geoserver-2.1.2.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/geoserver-2.1.2-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/geoserver-2.1.2-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/geoserver-2.1.2-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/geoserver-2.1.2-javadoc.zip/download)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-control-flow-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-ogr-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-wfsv-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.2/extensions/geoserver-2.1.2-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 17445

## Release notes

New Feature:

* [GEOS-4663](https://osgeo-org.atlassian.net/browse/GEOS-4663) Add support for ADD and MULTIPLY operations between two coverages
* [GEOS-4741](https://osgeo-org.atlassian.net/browse/GEOS-4741) Filter for geometry featuretypes
* [GEOS-4777](https://osgeo-org.atlassian.net/browse/GEOS-4777) Allow layers to be available, but not advertised in the capabilities documents

Improvement:

* [GEOS-4158](https://osgeo-org.atlassian.net/browse/GEOS-4158) enable env parameter in getlegendgraphic
* [GEOS-4557](https://osgeo-org.atlassian.net/browse/GEOS-4557) Show the store type in the store list page
* [GEOS-4595](https://osgeo-org.atlassian.net/browse/GEOS-4595) Add ISO 19115:2003 as a type option in Layer Metadata URL
* [GEOS-4596](https://osgeo-org.atlassian.net/browse/GEOS-4596) RESTConfig doesn't auto-configure Coverages (SRS/Bounds) like it does with FeatureTypes/WMS
* [GEOS-4664](https://osgeo-org.atlassian.net/browse/GEOS-4664) Allows RangeLookup (reclassifier) process to specify noData and outputPixelsValues
* [GEOS-4676](https://osgeo-org.atlassian.net/browse/GEOS-4676) Add content disposition header for raster outputs as well (inline mode)
* [GEOS-4677](https://osgeo-org.atlassian.net/browse/GEOS-4677) Expose the "reset" command via rest-config as well
* [GEOS-4712](https://osgeo-org.atlassian.net/browse/GEOS-4712) Add file logging option to the monitoring module
* [GEOS-4743](https://osgeo-org.atlassian.net/browse/GEOS-4743) Allow OwsUtils to handle path properties
* [GEOS-4744](https://osgeo-org.atlassian.net/browse/GEOS-4744) Allow for selection of rows by object and index in GeoServerTablePanel
* [GEOS-4745](https://osgeo-org.atlassian.net/browse/GEOS-4745) Allow CatalogBuilder lookupSRS and setupBounds methods to work against "detached" catalog objects
* [GEOS-4774](https://osgeo-org.atlassian.net/browse/GEOS-4774) Present dropdown choice for DataStore parameters that provide a list of options

Bug:

* [GEOS-3735](https://osgeo-org.atlassian.net/browse/GEOS-3735) Not Disjoint Filter does not work properly with ArcSDE datastore
* [GEOS-4257](https://osgeo-org.atlassian.net/browse/GEOS-4257) Default workspace cannot be set after deleting the default layers, stores, workspaces
* [GEOS-4358](https://osgeo-org.atlassian.net/browse/GEOS-4358) Exception page when creating a workspace named "default"
* [GEOS-4494](https://osgeo-org.atlassian.net/browse/GEOS-4494) WMS layer setup will trip code that assumes a layer always has a style
* [GEOS-4528](https://osgeo-org.atlassian.net/browse/GEOS-4528) Layer using MySQL select
* [GEOS-4587](https://osgeo-org.atlassian.net/browse/GEOS-4587) NPE and potential memory leak on concurrent load of DescribeFeatureType with custom schemas
* [GEOS-4591](https://osgeo-org.atlassian.net/browse/GEOS-4591) WCS 1.1.1 XML GetCoverage wtih SDE datastore produces ParameterNotFoundException
* [GEOS-4615](https://osgeo-org.atlassian.net/browse/GEOS-4615) WMS 1.1.1 geotiff output format uses incorrect mime type
* [GEOS-4637](https://osgeo-org.atlassian.net/browse/GEOS-4637) Don't complain about invalid SLD when using geometry transformations
* [GEOS-4643](https://osgeo-org.atlassian.net/browse/GEOS-4643) GetFeatureInfo and SLD substitution fails
* [GEOS-4649](https://osgeo-org.atlassian.net/browse/GEOS-4649) ogr based wfs output parsing error 						 X
* [GEOS-4651](https://osgeo-org.atlassian.net/browse/GEOS-4651) GetFeatureInfo + GML output + click on a empty area = service exception
* [GEOS-4653](https://osgeo-org.atlassian.net/browse/GEOS-4653) GWC caches affected by a style not deleted upon deletion of a style through the REST config API
* [GEOS-4656](https://osgeo-org.atlassian.net/browse/GEOS-4656) Configuring a mosaic with a lot of files can result in "too many open files"
* [GEOS-4668](https://osgeo-org.atlassian.net/browse/GEOS-4668) WFS reprojection won't work on a secured layer
* [GEOS-4680](https://osgeo-org.atlassian.net/browse/GEOS-4680) double encoding of special characters in WFS service exceptions
* [GEOS-4686](https://osgeo-org.atlassian.net/browse/GEOS-4686) Secured coverage wrappers will dispose the readers making fruther reads impossible
* [GEOS-4692](https://osgeo-org.atlassian.net/browse/GEOS-4692) restconfig tests leave test db files in module root
* [GEOS-4697](https://osgeo-org.atlassian.net/browse/GEOS-4697) cannot choose layer to include in a layergroup
* [GEOS-4710](https://osgeo-org.atlassian.net/browse/GEOS-4710) Image mosaics configured on the GUI will return just a single tile
* [GEOS-4720](https://osgeo-org.atlassian.net/browse/GEOS-4720) Opacity of the underlying layer affects the upper layer in Geoserver 2.1.x.
* [GEOS-4723](https://osgeo-org.atlassian.net/browse/GEOS-4723) Font sizes not changing with changes to &format_options=dpi:
* [GEOS-4733](https://osgeo-org.atlassian.net/browse/GEOS-4733) Querylayer module won't work properly in WFS 1.1 spatial queries over geographic data
* [GEOS-4735](https://osgeo-org.atlassian.net/browse/GEOS-4735) Layer cache not truncated on transactions over point layers
* [GEOS-4736](https://osgeo-org.atlassian.net/browse/GEOS-4736) Cache not truncated for layer groups upon feature edits
* [GEOS-4737](https://osgeo-org.atlassian.net/browse/GEOS-4737) Encoding of GWC tiles coming from an embedded raster layer fail due to premature disposal of the metatile
* [GEOS-4740](https://osgeo-org.atlassian.net/browse/GEOS-4740) Trying to update a FeatureTypeInfo to point to a new StoreInfo leads to error
* [GEOS-4772](https://osgeo-org.atlassian.net/browse/GEOS-4772) in FeatureTypeListResource catalog.getDataStoreByName use only DataStore Name
* [GEOS-4775](https://osgeo-org.atlassian.net/browse/GEOS-4775) Configuring Cascaded Layers via the REST API (wmsLayers) doesn't parse basic metadata from remote service
* [GEOS-4778](https://osgeo-org.atlassian.net/browse/GEOS-4778) Virtual services do not play well with layer groups
* [GEOS-4779](https://osgeo-org.atlassian.net/browse/GEOS-4779) Log location system variable override ignored when the logs are reconfigured at runtime
* [GEOS-4780](https://osgeo-org.atlassian.net/browse/GEOS-4780) Cascaded WMS Layers not available from rest/layers/`<layername>`.xml endpoint
* [GEOS-4788](https://osgeo-org.atlassian.net/browse/GEOS-4788) Mosaic background color transparency broken
