---
author: geoserver
comments: true
date: 2010-05-25 16:00:06+00:00
layout: post
link: http://blog.geoserver.org/2010/05/25/geoserver-2-0-2-release/
slug: geoserver-2-0-2-release
title: GeoServer 2.0.2 release
wordpress_id: 687
categories:
- Announcements
tags:
- Features
- GeoServer
- release
---

To meet the growing demand for a geospatial server that meets the open standards set by the Open Geospatial Consortium, the GeoServer community has worked hard to release the new GeoServer 2.0.2.  This release includes [almost 100 bugfixes and new features](#release-notes).

As [previously mentioned]({% post_url 2010-05-17-oracle-georaster-custom-jdbc-access %}), GeoServer now provides support for Oracle Georaster, custom database layouts for image data and [polymorphism]({% post_url 2010-05-25-polymorphism-in-application-schema %}).

Have you ever wondered what geographical area an EPSG code covers? A new feature has been added to showcase the different projections visually, by showing a map of the projection's area of validity in the same CRS.  Here are three examples of this: [EPSG:2964](https://web.archive.org/web/20100525/http://demo.opengeo.org/geoserver/web/?wicket:bookmarkablePage=:org.geoserver.web.demo.SRSDescriptionPage&code=EPSG:2964), [EPSG:3032](https://web.archive.org/web/20100525/http://demo.opengeo.org/geoserver/web/?wicket:bookmarkablePage=:org.geoserver.web.demo.SRSDescriptionPage&code=EPSG:3032), [EPSG:22184](https://web.archive.org/web/20100525/http://demo.opengeo.org/geoserver/web/?wicket:bookmarkablePage=:org.geoserver.web.demo.SRSDescriptionPage&code=EPSG:22184).

To add to this, we have also added a default style preview in the layer publishing configuration.

The rendering subsystem has been improved to include [parameter substitution](http://docs.geoserver.org/stable/en/user/styling/sld-extensions/substitution.html), meaning you can pass parameters down from a GetMap request into your SLD for dynamic styling purposes.

The ability to do geometry transformations, included in GeoServer 2.0.1 without much fanfare, now has been [completely documented](http://docs.geoserver.org/stable/en/user/styling/sld-extensions/geometry-transformations.html).

Building image pyramids just got easier: gone are the times where you had to manually build each level mosaic and configure the main property file by hand.  The current pyramid extension can do this for you provided it is given a suitably configured directory set. See the [pyramid tutorial](http://docs.geoserver.org/stable/en/user/tutorials/imagepyramid/imagepyramid.html) for more details.

Finally, this release of GeoServer implements the GetStyles optional WMS method allowing a user to retrieve the definition of all styles attached to a specific WMS layer, see the following link for an example:
[http://demo.opengeo.org/geoserver/wms?request=GetStyles&layers=topp:states&service=wms&version=1.1.0](https://web.archive.org/web/20100525/http://demo.opengeo.org/geoserver/wms?request=GetStyles&layers=topp:states&service=wms&version=1.1.0)

Thanks to everyone who have worked hard over the past few months adding features and fixing bugs, in order to make this release happen.  As usual, we encourage you to [download](https://web.archive.org/web/20100525/http://geoserver.org/display/GEOS/GeoServer 2.0.2), try it out, and provide feedback on the [users mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users).

----

## Stable

Released on May 24, 2010

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/geoserver-2.0.2-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/geoserver-2.0.2-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/geoserver-2.0.2.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/geoserver-2.0.2.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/geoserver-2.0.2-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/geoserver-2.0.2-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/geoserver-2.0.2-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/geoserver-2.0.2-javadoc.zip/download)
- [Release Notes](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/release-notes-2.0.2.txt/download)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-imagemosaic-jdbc-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-charts-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-ogr-plugin.zip/download)
- [RESTConfig](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-restconfig-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.2/extensions/geoserver-2.0.2-wfsv-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 16040

## Release notes

New Feature:

* [GEOS-2566](https://osgeo-org.atlassian.net/browse/GEOS-2566) Passing down params from the WMS request into the SLD
* [GEOS-3831](https://osgeo-org.atlassian.net/browse/GEOS-3831) Add a map to the SRS description page that shows the CRS area of validity
* [GEOS-3954](https://osgeo-org.atlassian.net/browse/GEOS-3954) Support for Oracle Georaster
* [GEOS-3955](https://osgeo-org.atlassian.net/browse/GEOS-3955) Support for custom db layout for image data

Improvement:

* [GEOS-2371](https://osgeo-org.atlassian.net/browse/GEOS-2371) Pixel Tollerance for getFeatureInfo requests should be configurable on a per layer basis
* [GEOS-2581](https://osgeo-org.atlassian.net/browse/GEOS-2581) PointPlacement + followLine produces weird results
* [GEOS-3574](https://osgeo-org.atlassian.net/browse/GEOS-3574) Don't output KML point placemarks for polygon and lines unless there is an explicit point symbolizer, evolutions in KML made them un-necessary
* [GEOS-3621](https://osgeo-org.atlassian.net/browse/GEOS-3621) Adding a style whose SLD already exists on the server
* [GEOS-3622](https://osgeo-org.atlassian.net/browse/GEOS-3622) Add back the ability to reload the catalog from disk
* [GEOS-3739](https://osgeo-org.atlassian.net/browse/GEOS-3739) Add support for the polyconic projection
* [GEOS-3772](https://osgeo-org.atlassian.net/browse/GEOS-3772) Make sure verbose exceptions do not affect the chosen service strategy
* [GEOS-3775](https://osgeo-org.atlassian.net/browse/GEOS-3775) GeoServerDialog should allow for ajax validations
* [GEOS-3787](https://osgeo-org.atlassian.net/browse/GEOS-3787) Make OWS Request object mutable, subclassable, and allow dispatcher callbacks to override it
* [GEOS-3792](https://osgeo-org.atlassian.net/browse/GEOS-3792) Use full vector rendering for SVG graphics and marks in PDF and SVG
* [GEOS-3795](https://osgeo-org.atlassian.net/browse/GEOS-3795) Add support for AUTO:xxxx codes
* [GEOS-3797](https://osgeo-org.atlassian.net/browse/GEOS-3797) Make XStream persisten tolerant to unkown fields
* [GEOS-3814](https://osgeo-org.atlassian.net/browse/GEOS-3814) Expose KML default param values as a configuration option in the administration GUI
* [GEOS-3815](https://osgeo-org.atlassian.net/browse/GEOS-3815) Increase persistence on video of the lower resolution raster superoverlay tiles
* [GEOS-3823](https://osgeo-org.atlassian.net/browse/GEOS-3823) Add SLD 1.0 GetStyles support
* [GEOS-3825](https://osgeo-org.atlassian.net/browse/GEOS-3825) Allow the creation of parametrized SLD, and pass the parameter value down from GetMap
* [GEOS-3863](https://osgeo-org.atlassian.net/browse/GEOS-3863) Improve default raster icon
* [GEOS-3890](https://osgeo-org.atlassian.net/browse/GEOS-3890) A Simple PlugIn tutorial is not available in the new docs for geoserver version 2.0.x
* [GEOS-3897](https://osgeo-org.atlassian.net/browse/GEOS-3897) CSSDemo page not well suited to prepare labelled maps
* [GEOS-3898](https://osgeo-org.atlassian.net/browse/GEOS-3898) CSSDemoPage should show scale denominator
* [GEOS-3916](https://osgeo-org.atlassian.net/browse/GEOS-3916) OWS configuration cannot parse service exceptions
* [GEOS-3919](https://osgeo-org.atlassian.net/browse/GEOS-3919) Expose reference converters allowing code outside of XStreamPersister to use them
* [GEOS-3925](https://osgeo-org.atlassian.net/browse/GEOS-3925) Log profiles choosable in the GUI should reflect what's available on disk

Bug:

* [GEOS-2016](https://osgeo-org.atlassian.net/browse/GEOS-2016) java.lang.NullPointerException on GeoTiff CoverageStore Creation
* [GEOS-2017](https://osgeo-org.atlassian.net/browse/GEOS-2017) Reprojecting data coming from Oracle generate layout problems
* [GEOS-2020](https://osgeo-org.atlassian.net/browse/GEOS-2020) Sample GetCoverage request fails with "colorModel == null"
* [GEOS-2841](https://osgeo-org.atlassian.net/browse/GEOS-2841) GeoWebCache is not always able to see layers from GeoServer (Glassfish)
* [GEOS-3312](https://osgeo-org.atlassian.net/browse/GEOS-3312) Default configuration for new GeoTIFF data sources makes WMS Capabilties document invalid
* [GEOS-3337](https://osgeo-org.atlassian.net/browse/GEOS-3337) GetFeatureInfo on Layer Preview Fails Unless Workspace is Cite
* [GEOS-3408](https://osgeo-org.atlassian.net/browse/GEOS-3408) Bad shapefile DBF causes shapefile datastore to lock
* [GEOS-3634](https://osgeo-org.atlassian.net/browse/GEOS-3634) Empty layer group causes obscure error message
* [GEOS-3653](https://osgeo-org.atlassian.net/browse/GEOS-3653) GML responses forces the full vector catalog to be loaded (and eventually re-disposed of)
* [GEOS-3683](https://osgeo-org.atlassian.net/browse/GEOS-3683) JNDI factories lack the extra parameters the base factory exposes
* [GEOS-3702](https://osgeo-org.atlassian.net/browse/GEOS-3702) WCS output shows shift
* [GEOS-3718](https://osgeo-org.atlassian.net/browse/GEOS-3718) Saving new GeoTIFF store does not getting
* [GEOS-3723](https://osgeo-org.atlassian.net/browse/GEOS-3723) NPE in the GWC transaction listener on update transactions
* [GEOS-3748](https://osgeo-org.atlassian.net/browse/GEOS-3748) GeoServer loader can NPE on missing folders in the data directory
* [GEOS-3752](https://osgeo-org.atlassian.net/browse/GEOS-3752) Avoid using File.deleteOnExit in production code
* [GEOS-3756](https://osgeo-org.atlassian.net/browse/GEOS-3756) WFS Inserting a Point  (map EPSG:900913  and Layer EPSG:4326) org.geotools.referencing.operation.projection.PointOutsideEnvelopeException: 727833.38323013 outside of (-180.0,180.0)
* [GEOS-3757](https://osgeo-org.atlassian.net/browse/GEOS-3757) Request logging filter + log bodies option breaks Wicket AJAX requests
* [GEOS-3760](https://osgeo-org.atlassian.net/browse/GEOS-3760) WFS with interesects filter using Box and reprojection does not work as expected
* [GEOS-3761](https://osgeo-org.atlassian.net/browse/GEOS-3761) Reprojecting to EPSG:3031 sometimes breaks
* [GEOS-3762](https://osgeo-org.atlassian.net/browse/GEOS-3762) GeoServer 2.0 does not work under Glassfish 3.0 final
* [GEOS-3764](https://osgeo-org.atlassian.net/browse/GEOS-3764) Some raster configurations fail to persiste to due class cast exception
* [GEOS-3774](https://osgeo-org.atlassian.net/browse/GEOS-3774) org.geoserver.wfs.WFSException: Could not locate FeatureStore for
* [GEOS-3776](https://osgeo-org.atlassian.net/browse/GEOS-3776) Workspace names allow spaces and other invalid xml Name chars, breaks WFS capabilities
* [GEOS-3779](https://osgeo-org.atlassian.net/browse/GEOS-3779) DispatcherCallback.finishedCallback won't be called if there are issues writing out the output
* [GEOS-3781](https://osgeo-org.atlassian.net/browse/GEOS-3781) Dipspatcher still logs about client aborting the request in a couple of places
* [GEOS-3782](https://osgeo-org.atlassian.net/browse/GEOS-3782) GZip fiter breaks ServletResponse.flushBuffers contract
* [GEOS-3783](https://osgeo-org.atlassian.net/browse/GEOS-3783) Have LegacyCatalogImporter set 4326 set SRS to 4326 when reading latLonBoundingBox elements
* [GEOS-3784](https://osgeo-org.atlassian.net/browse/GEOS-3784) OPTIMIZE_LINE_WIDTH does not allow to re-enable the optimization on 2.0.x
* [GEOS-3796](https://osgeo-org.atlassian.net/browse/GEOS-3796) JAIInitializer sets a recycling tile factory even if tile recycling is not enabled
* [GEOS-3800](https://osgeo-org.atlassian.net/browse/GEOS-3800) Make it easier to build a pyramid following the mosaic approach
* [GEOS-3802](https://osgeo-org.atlassian.net/browse/GEOS-3802) PointSymbolizer use on polygon features plots all symbol a the top left of the output
* [GEOS-3812](https://osgeo-org.atlassian.net/browse/GEOS-3812) Update and Delete transactions fail if name space prefix is different than the declared one
* [GEOS-3819](https://osgeo-org.atlassian.net/browse/GEOS-3819) REST API generates invalid internal links
* [GEOS-3830](https://osgeo-org.atlassian.net/browse/GEOS-3830) UpdateSequence is not getting updated
* [GEOS-3833](https://osgeo-org.atlassian.net/browse/GEOS-3833) Links on Layer page lack workspace scoping
* [GEOS-3835](https://osgeo-org.atlassian.net/browse/GEOS-3835) Exception when trying to render dashed lines
* [GEOS-3837](https://osgeo-org.atlassian.net/browse/GEOS-3837) kmlplacemark setting breaking raster map generation
* [GEOS-3846](https://osgeo-org.atlassian.net/browse/GEOS-3846) ServiceInfo XStream deserialization may lead to null pointer exceptions
* [GEOS-3849](https://osgeo-org.atlassian.net/browse/GEOS-3849) Too many open files left by wicket ui
* [GEOS-3855](https://osgeo-org.atlassian.net/browse/GEOS-3855) GWC integration breaks with KML superoverlays
* [GEOS-3858](https://osgeo-org.atlassian.net/browse/GEOS-3858) NullPointerException from PreviewLayer
* [GEOS-3861](https://osgeo-org.atlassian.net/browse/GEOS-3861) GML LineStringType with 3 points where the first and last points are the same causes an exception
* [GEOS-3864](https://osgeo-org.atlassian.net/browse/GEOS-3864) GWC seeder no longer protected by ACEGI
* [GEOS-3866](https://osgeo-org.atlassian.net/browse/GEOS-3866) Query's typeName attribute not correctly parsed when using XML POST
* [GEOS-3868](https://osgeo-org.atlassian.net/browse/GEOS-3868) Rendering errors with epsg:4326 data reprojected to EPSG:28992
* [GEOS-3869](https://osgeo-org.atlassian.net/browse/GEOS-3869) GeoServer does not update Geotools namespace
* [GEOS-3870](https://osgeo-org.atlassian.net/browse/GEOS-3870) Null Pointer error on `<Abstract />` short tag in SLD
* [GEOS-3876](https://osgeo-org.atlassian.net/browse/GEOS-3876) DataStoreNamespaceUpdatingListener only works for GUI
* [GEOS-3878](https://osgeo-org.atlassian.net/browse/GEOS-3878) Changing the default workspace won't change the default namespace until restart
* [GEOS-3880](https://osgeo-org.atlassian.net/browse/GEOS-3880) WmsException: Rendering process failed with a line geometry of null length
* [GEOS-3888](https://osgeo-org.atlassian.net/browse/GEOS-3888) Rectangular graphics in tiled fills are being rendered (squished) to be square
* [GEOS-3893](https://osgeo-org.atlassian.net/browse/GEOS-3893) SLD doesn't validate when type parameter added to `<ColorMap>`
* [GEOS-3895](https://osgeo-org.atlassian.net/browse/GEOS-3895) CSSDemo fails on an emtpy catalog
* [GEOS-3896](https://osgeo-org.atlassian.net/browse/GEOS-3896) CSSDemo page fails to load in locales that use comma as the decimal separator
* [GEOS-3900](https://osgeo-org.atlassian.net/browse/GEOS-3900) LineSymbolizer: Bigger Stroke-Width produces a corner
* [GEOS-3903](https://osgeo-org.atlassian.net/browse/GEOS-3903) Drop down lists should not be sorted with case sensitivity
* [GEOS-3906](https://osgeo-org.atlassian.net/browse/GEOS-3906) CSS module swaps linecap and linejoin values
* [GEOS-3907](https://osgeo-org.atlassian.net/browse/GEOS-3907) When catalog as many vector layers (around 600), WFS transactions cause memory leaks and are very slow
* [GEOS-3908](https://osgeo-org.atlassian.net/browse/GEOS-3908) Creating two workspaces with the same URI can break WFS
* [GEOS-3913](https://osgeo-org.atlassian.net/browse/GEOS-3913) Shapefile validation disallows references to http published shapefiles
* [GEOS-3921](https://osgeo-org.atlassian.net/browse/GEOS-3921) WMS capabilities LegendURL for alternate styles misses style name
* [GEOS-3924](https://osgeo-org.atlassian.net/browse/GEOS-3924) IsDefault in GetStyles/NamedLayer/UserStyle should be 1 or 0, not true and false
* [GEOS-3937](https://osgeo-org.atlassian.net/browse/GEOS-3937) WMS request fails from a WFS data store
* [GEOS-3969](https://osgeo-org.atlassian.net/browse/GEOS-3969) CITE Testing: Missing or invalid response entity
* [GEOS-3973](https://osgeo-org.atlassian.net/browse/GEOS-3973) Errors decompressing zipped shapefiles when sending them via rest to GeoServer
* [GEOS-4007](https://osgeo-org.atlassian.net/browse/GEOS-4007) Unable to request wms getCapabilities
* [GEOS-4210](https://osgeo-org.atlassian.net/browse/GEOS-4210) XSS vulnerability in gwc module
* [GEOS-4327](https://osgeo-org.atlassian.net/browse/GEOS-4327) Layer Preview crash

Task:

* [GEOS-3809](https://osgeo-org.atlassian.net/browse/GEOS-3809) Add community artifacts to nightly builds
* [GEOS-3832](https://osgeo-org.atlassian.net/browse/GEOS-3832) show a legend preview in the layer publish page
* [GEOS-3914](https://osgeo-org.atlassian.net/browse/GEOS-3914) Make IOUtils.zipDirectory not to take ownership of its argument output stream
