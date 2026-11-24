---
author: geoserver
comments: true
date: 2011-12-21 22:28:44+00:00
layout: post
link: http://blog.geoserver.org/2011/12/21/geoserver-2-1-3-released/
slug: geoserver-2-1-3-released
title: GeoServer 2.1.3 Released
wordpress_id: 1017
categories:
- Announcements
- Features
---

The GeoServer team is happy to announce the release of GeoServer 2.1.3, now available for download.

For the most part this is a maintainance release consisting of bug fixes, but as usual a few new features and improvements have managed to creep in. A total of [59 issues](#release-notes) were resolved for this release. Some of the new and noteworthy include:



	
  * basic http authentication with cascaded WMS servers

	
  * WMS 1.3 support in the layer preview

	
  * transparent sorting for all data stores, not only those backed by a database

	
  * embedded OpenLayers upgraded to 2.11

	
  * a number of INSPIRE compliance improvements

	
  * support for asynchronous WPS processes


And more. Check out the [change log](#release-notes) for the entire list. A big thank you to everyone who contributed patches for this release. This includes:



	
  * Tony Young for a monitoring patch to include support for the "user-agent" header ([GEOS-4872](https://osgeo-org.atlassian.net/browse/GEOS-4872))

	
  * Tony Young again for a restconfig patch to properly calculate grid dimensions for coverages ([GEOS-4753](https://osgeo-org.atlassian.net/browse/GEOS-4753))

	
  * Rudi Hochmeister for a documentation patch providing an installation guide for Debian Linux  ([GEOS-4752](https://osgeo-org.atlassian.net/browse/GEOS-4752))

	
  * Frank Gasdorf for a completed German translation ([GEOS-4294](https://osgeo-org.atlassian.net/browse/GEOS-4294))


Contributions such as these are what keeps GeoServer moving forward. And thanks to all those who helped out by filing bug reports.

Download 2.1.3, try it out and help us to continue to improve GeoServer by providing feedback on the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users) and reporting bugs in the [issue tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS).

Thanks for using GeoServer!

----

## GeoServer 2.1.3

Released on Dec 21, 2011

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/geoserver-2.1.3-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/geoserver-2.1.3-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/geoserver-2.1.3a.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/geoserver-2.1.3.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/geoserver-2.1.3-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/geoserver-2.1.3-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/geoserver-2.1.3-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/geoserver-2.1.3-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-control-flow-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-ogr-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1.3/extensions/geoserver-2.1.3-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 17865

## Release notes

New Feature:

* [GEOS-4491](https://osgeo-org.atlassian.net/browse/GEOS-4491) AuthorityURL and Identifier
* [GEOS-4658](https://osgeo-org.atlassian.net/browse/GEOS-4658) support vocabulary attribute for keywords at the Service level (WMS)
* [GEOS-4659](https://osgeo-org.atlassian.net/browse/GEOS-4659) have an option to ouput a Layer BoundingBox in WMS GetCapabilities for every SRS supported
* [GEOS-4672](https://osgeo-org.atlassian.net/browse/GEOS-4672) Cascading WMS: Add authentication support for a remote wms store
* [GEOS-4819](https://osgeo-org.atlassian.net/browse/GEOS-4819) Suppoort for WPS asyncronous processes

Improvement:

* [GEOS-4294](https://osgeo-org.atlassian.net/browse/GEOS-4294) [patch] GeoServer german translation (DE)
* [GEOS-4753](https://osgeo-org.atlassian.net/browse/GEOS-4753) RESTConfig doesn't calculate Coverage grid/dimensions
* [GEOS-4784](https://osgeo-org.atlassian.net/browse/GEOS-4784) Workspace and DataStore i18n
* [GEOS-4804](https://osgeo-org.atlassian.net/browse/GEOS-4804) missing i18n support for username/password titles
* [GEOS-4805](https://osgeo-org.atlassian.net/browse/GEOS-4805) i18n support for user roles management column headers
* [GEOS-4806](https://osgeo-org.atlassian.net/browse/GEOS-4806) i18n support in LayerPage for "Reload feature type" label
* [GEOS-4811](https://osgeo-org.atlassian.net/browse/GEOS-4811) boolean value representation as icon in table view for UserPage - admin column
* [GEOS-4817](https://osgeo-org.atlassian.net/browse/GEOS-4817) Add Connect and Read Timeout values to Cascaded WMS Store Metadata
* [GEOS-4828](https://osgeo-org.atlassian.net/browse/GEOS-4828) missing i18n support for NewLayerPage
* [GEOS-4829](https://osgeo-org.atlassian.net/browse/GEOS-4829) Change WFS JSON output formatting of date/time to ISO 8601 (i.e. XML) date/time format
* [GEOS-4830](https://osgeo-org.atlassian.net/browse/GEOS-4830) Allow the user to force the content disposition mode and file name via kvp params
* [GEOS-4831](https://osgeo-org.atlassian.net/browse/GEOS-4831) Allow to use templated map decorations with the animator
* [GEOS-4845](https://osgeo-org.atlassian.net/browse/GEOS-4845) Make it easier to build a custom version of GeoServer
* [GEOS-4872](https://osgeo-org.atlassian.net/browse/GEOS-4872) Add User-Agent logging to Monitoring extension
* [GEOS-4879](https://osgeo-org.atlassian.net/browse/GEOS-4879) GeoServer builds reports loads of "Extension lookup occured, but ApplicationContext is unset." log messages
* [GEOS-4881](https://osgeo-org.atlassian.net/browse/GEOS-4881) WPS build takes several minutes if schemas.opengis.net is not accessible
* [GEOS-4892](https://osgeo-org.atlassian.net/browse/GEOS-4892) Upgrade OpenLayers embedded in GeoServer to version 2.11
* [GEOS-4894](https://osgeo-org.atlassian.net/browse/GEOS-4894) Add a drop down in the OL preview to work with the WMS 1.3 protocol
* [GEOS-4902](https://osgeo-org.atlassian.net/browse/GEOS-4902) Add transparent sorting support for all stores
* [GEOS-5216](https://osgeo-org.atlassian.net/browse/GEOS-5216) Allow per-workspace service security rule

Bug:

* [GEOS-3967](https://osgeo-org.atlassian.net/browse/GEOS-3967) Setting HTTP Authentication for WFS store only authenticates GetCapabilities requests
* [GEOS-4499](https://osgeo-org.atlassian.net/browse/GEOS-4499) Error running cache diskquota enforcement task java.lang.NullPointerException
* [GEOS-4572](https://osgeo-org.atlassian.net/browse/GEOS-4572) GeoServer - GWC Integration & GIF image render
* [GEOS-4646](https://osgeo-org.atlassian.net/browse/GEOS-4646) WFS Datastore + TIME support chaining
* [GEOS-4673](https://osgeo-org.atlassian.net/browse/GEOS-4673) Using type "other" for MetadataURL will lead to invalid GetCapabilities for WMS 1.1.1
* [GEOS-4708](https://osgeo-org.atlassian.net/browse/GEOS-4708) GetCapabilites fails for rasters not available to user
* [GEOS-4782](https://osgeo-org.atlassian.net/browse/GEOS-4782) ResourcePool  may fail with NPE on a catalog reload towards a configuration that has less layers than before
* [GEOS-4791](https://osgeo-org.atlassian.net/browse/GEOS-4791) GWC regression with RGBA images + jpeg format == blue images
* [GEOS-4793](https://osgeo-org.atlassian.net/browse/GEOS-4793) lack of namespace datastore parameter for cascaded WFS breaks WFS queries
* [GEOS-4796](https://osgeo-org.atlassian.net/browse/GEOS-4796) Removing all workspaces will cause an NPE at the first namespace related operation
* [GEOS-4798](https://osgeo-org.atlassian.net/browse/GEOS-4798) NPE on keyword parsing from remote WMS
* [GEOS-4827](https://osgeo-org.atlassian.net/browse/GEOS-4827) NewLayerPage : Message Containers are not correctly updated if switching data stores back and force
* [GEOS-4832](https://osgeo-org.atlassian.net/browse/GEOS-4832) GeoServer WPS does not support stored responses
* [GEOS-4842](https://osgeo-org.atlassian.net/browse/GEOS-4842) GeoServer WPS fails to open a remote zipped shapefile
* [GEOS-4846](https://osgeo-org.atlassian.net/browse/GEOS-4846) WFS-T transactions indefinite wait
* [GEOS-4847](https://osgeo-org.atlassian.net/browse/GEOS-4847) filtering workspaces broken due to unknown property 'default'
* [GEOS-4851](https://osgeo-org.atlassian.net/browse/GEOS-4851) Safeguard catalog and configuration code from concurrent access
* [GEOS-4853](https://osgeo-org.atlassian.net/browse/GEOS-4853) KML Time template does not work anymore due to XSDateTimeBinding changes
* [GEOS-4854](https://osgeo-org.atlassian.net/browse/GEOS-4854) WFS-T XML POST Fails
* [GEOS-4859](https://osgeo-org.atlassian.net/browse/GEOS-4859) Configuring Cascaded WFS Layers doesn't capture and store basic layer metadata from remote service
* [GEOS-4862](https://osgeo-org.atlassian.net/browse/GEOS-4862) Asynch process execution will be stuck forever in "process started" state if an error occurs while encoding the process results
* [GEOS-4863](https://osgeo-org.atlassian.net/browse/GEOS-4863) WPS back link to store resources uses the parameter "mime", it should be "mimetype"
* [GEOS-4871](https://osgeo-org.atlassian.net/browse/GEOS-4871) Using Monitoring into an Oracle DB fails due to use of reserved word RESOURCE as a column name
* [GEOS-4874](https://osgeo-org.atlassian.net/browse/GEOS-4874) Map decoration horizonal centering does not account for the decoration size
* [GEOS-4880](https://osgeo-org.atlassian.net/browse/GEOS-4880) WMS 1.3 CapabiltiesSystemTest will fail if schemas.opengis.net is not accessible
* [GEOS-4887](https://osgeo-org.atlassian.net/browse/GEOS-4887) EnvelopePanel rounds bounds coordinates to three decimals
* [GEOS-4889](https://osgeo-org.atlassian.net/browse/GEOS-4889) Parameter expansion does not work in mixed content stroke css parameters
* [GEOS-4891](https://osgeo-org.atlassian.net/browse/GEOS-4891) uom rescaling for graphic fills and strokes does not work
* [GEOS-4893](https://osgeo-org.atlassian.net/browse/GEOS-4893) GeoServer own on the fly meta-tiling won't work with WMS 1.3
* [GEOS-4896](https://osgeo-org.atlassian.net/browse/GEOS-4896) Animator won't work over a layer list
* [GEOS-4899](https://osgeo-org.atlassian.net/browse/GEOS-4899) GeoServer hang up on transaction including xsi:schemaLocation
* [GEOS-4905](https://osgeo-org.atlassian.net/browse/GEOS-4905) Cascading WMS 1.3 servers using the "CRS:XYZ" crs results in maps with wrong proportions
* [GEOS-4908](https://osgeo-org.atlassian.net/browse/GEOS-4908) WMS cascading does not work anymore if a proxy is required for external connections
* [GEOS-4973](https://osgeo-org.atlassian.net/browse/GEOS-4973) Clicking on 'WFS service' in the GeoServer menu immediatly gives an error
* [GEOS-5035](https://osgeo-org.atlassian.net/browse/GEOS-5035) Latent bounding box exception for WMS with small extent

Task:

* [GEOS-4803](https://osgeo-org.atlassian.net/browse/GEOS-4803) set style on html text input components that miss it
* [GEOS-4808](https://osgeo-org.atlassian.net/browse/GEOS-4808) Move WFSV back into community land
