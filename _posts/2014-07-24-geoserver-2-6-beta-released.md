---
author: geoserver
comments: true
date: 2014-07-24 22:47:34+00:00
layout: post
link: http://blog.geoserver.org/2014/07/24/geoserver-2-6-beta-released/
slug: geoserver-2-6-beta-released
title: GeoServer 2.6-beta Released
wordpress_id: 1910
categories:
- Announcements
tags:
- beta
- complex features schema GSIP
- Features
- localization
- release
- SLD
- style
- styling
- windows
---

The GeoServer team is overjoyed to announce the release of GeoServer [2.6-beta](http://geoserver.org/release/2.6-beta/).

I hope you are enjoying the new website - the download page for [2.6-beta](http://geoserver.org/release/2.6-beta/) provides links to the expected [zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6-beta/geoserver-2.6-beta-bin.zip), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6-beta/geoserver-2.6-beta-war.zip), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6-beta/geoserver-2.6-beta.dmg) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6-beta/geoserver-2.6-beta.exe) bundles. For this release we are experimenting with providing source downloads directly from the GitHub [2.6-beta tag](https://github.com/geoserver/geoserver/releases/tag/2.6-beta).


> _As a development release, 2.6-beta is considered experimental and is provided for testing purposes. This release is not recommended for production (even if you are excited by the new features)._


This release is made in conjunction with GeoTools 12-beta. Thanks to Kevin for making a beta release of GeoWebCache [1.6.0-beta](http://sourceforge.net/projects/geowebcache/files/geowebcache/1.6.0-beta/) with relatively little notice.


### What to expect ... and what we expect from you


A complete [change log](#release-notes) is available from the issue tracker. We will ask you to wait for 2.6.0 before we let Andrea write a [pretty]({% post_url 2014-01-21-geoserver-2-5-beta-released %}) blog with pictures illustrating what features have been added. Instead 2.6-beta is my chance to ask you to _**download GeoServer 2.6-beta for testing**_.


> _Testing is a key part of the open source [social contract](http://www.how2map.com/2013/09/opensource-and-social-contract.html). The GeoServer team have identified a few areas where we would like to ask for help. This is your best chance to identify issues early while we still have time to do something about it. For those making use of [commercial support](http://geoserver.org/support/) ask your vendor about their plans for 2.6-beta testing. We would like to ensure the functionality you depend on is ready to go for a Q2 release._


When testing Geoserver 2.6-beta please let us know on the [user list](http://geoserver.org/comm/) (or [#GeoServer](https://twitter.com/search?q=%23geoserver)) how it works for you. We will be sure to thank you in the final release announcement and product presentations.

**Java 7 Testing**

With Oracle [retiring Java 6](http://www.oracle.com/technetwork/java/eol-135779.html) security updates the time has come to raise the minimum bar to Java 7.


> _We know a lot of downstream projects (such as [OSGeo Live](http://live.osgeo.org/en/index.html)) have been waiting for GeoServer to support Java 7. Thanks to CSIRO, Boundless, GeoSolutions for providing Java 7 build environments allowing us to make this transition in a responsible fashion._


Testing:



	
  * This is a major testing priority on all platforms.

	
  * Windows 7: The start.bat used by the run manually install has trouble running as an administrator. We recommend installing as a service of this release ([GEOS-5687](https://osgeo-org.atlassian.net/browse/GEOS-6587))

	
  * Mac: You will need to install Oracle Java 7 (as OpenJDK 7 is not yet available for OSX). We have not yet figured out how to run GeoServer.App with Java 7 ([GEOS-6588](https://osgeo-org.atlassian.net/browse/GEOS-6588)) and are open to suggestions.


References:

	
  * Documentation: [Java Considerations](http://docs.geoserver.org/latest/en/user/production/java.html) and [Installation](http://docs.geoserver.org/latest/en/user/installation/index.html)

	
  * Change Control: [GSIP 112 Update master to Java 7](https://github.com/geoserver/geoserver/wiki/GSIP-112---Upgrade-master-to-Java-7)


**WFS Cascade**

This is a really exciting change, swapping out our gt-wfs client code for a new gt-wfs-ng implementation with a new GML parser / encoder.  After comparing quality of the two implementations we decided to go all in with this transition .. and thus would really like your help testing.

We would like to hear back on cascading the following configurations:



	
  * [GeoServer](http://geoserver.org)

	
  * [deegree](http://www.deegree.org)

	
  * [MapServer](http://mapserver.org)

	
  * [tinyows](http://mapserver.org/tinyows/) - there is a critical fix about axis order in tinyows trunc. It corrects (finally!) the output ... but perhaps not yet the filters?

	
  * [ArcGIS](http://resources.arcgis.com/en/help/main/10.1/index.html#//0154000004mm000000)

	
  * [Other](http://www.opengeospatial.org/resource/products) - any other WFS you are working with!


Testing:

	
  * Pay special attention to the flags used for axis order. There are different flags to account for each way a WFS implementation can get confused. You will find some implementations expect the wrong axis order on request, but are capable of producing the correct axis order output.

	
  * We especially ask our friends in Europe to test WFS services published for INSPIRE compliance


This was an epic amount of work by Niels and we have a couple of new features waiting in the wings based on the success of this transition.

**Curves support for GML and WMS**

A large amount of work has been put into extending the Geometry implementation used by GeoServer.


> _We have experimented with several approaches over the years (including ISO 19107 and a code sprint with the deegree project) and it is great to finally have a solution. As a long time user of the JTS Topology Suite we have been limited to a Point, Line and Polygon model of Geometry. Andrea has very carefully extended these base classes in to allow for both GML output and rendering. The trick is using a tolerance to convert the the arcs and circles into line work for geometry processing._


Testing for the 2.6-beta release is limited to those with Oracle Spatial. If you are interested in funding/volunteering support for PostGIS please contact the geoserver-devel email list.

Testing:



	
  * Look for "_Linearization tolerance"_ when configuring your layer.


**Advanced projection handling for raster**

We would like to hear feedback on how maps that cross the date line (or are in a polar projection) have improved for you.

Testing:



	
  * No special settings needed


Reference:

	
  * [Advanced Raster Projection in GeoServer](http://www.geo-solutions.it/blog/developers-corner-advanced-raster-projection-geoserver/) (GeoSolutions)


**Coverage Views**

We struggled a bit with how to name this great new feature, however if you work with raster data this is your chance to recombine bands from different sources into a multi-band coverage.

Testing:



	
  * Use "_Configure new Coverage view_" when creating a new layer


References:

	
  * [Coverage Views](http://docs.geoserver.org/latest/en/user/data/raster/coverageview.html) (GeoServer User Manual)

	
  * [Raster Views in GeoServer via the CoverageView concept](http://www.geo-solutions.it/blog/overageview-concept-for-geoserver/) (GeoSolutions)


**Startup Testing**

Yes this is an ominous item to ask you to test.


> _GeoServer 2.6 simplifies where configuration files are stored on disk. Previous versions were willing to spread configuration files between the webapps folder, the data directory and any additional directories on request. For GeoServer 2.6 configuration files are limited to the data directory as a step towards improving clustering support and growing our JDBC Config story._


Testing:



	
  * No special settings needed

	
  * Special request to check files that are edited by hand on disk (such security settings and free marker templates)


References:

	
  * Change Control: [GSIP 106 ResourceStore API](https://github.com/geoserver/geoserver/wiki/GSIP%20106)


**Pluggable Styles**

For everyone happy with the CSS Style Extension we would like to ask you to test a change to the style edit page (allowing you to create a CSS or SLD style from the start).

Testing:



	
  * Install CSS Extension and look for a new option when creating a style


Reference:

	
  * Change Control: [GSIP 117 Pluggable Styles](https://github.com/geoserver/geoserver/wiki/GSIP-117)


**Wind barbs and WKT Graphics**

I am really happy to see this popular extension folded into the main GeoServer application.

Testing:



	
  * Check GeoTools [WKT Marks](http://docs.geotools.org/latest/userguide/library/render/wkt.html) for examples you can use in your SLD file


References:

	
  * [Supporting Wind Barbs In GeoServer and GeoTools](http://www.geo-solutions.it/blog/developers-corner-supporting-wind-barbs-geoserver-geotools/) (GeoSolutions)


**New Formats and Functionality**

We have new implementations of a couple of modules:



	
  * Printing - new implementation from our friends at MapFish

	
  * Scripting - includes a UI for editing scripts from the Web Administration Application


A final shout out to ask for help testing new formats:

	
  * NetCDF

	
  * Rib

	
  * OGR


**Language Support**

We are happy to announce the first release having support for Turkish. Many thanks to Engin Gem and the whole [translation team](https://www.transifex.com/projects/p/geoserver/language/tr/) for the initial contribution. All modules, core, extensions, and community modules have been translated within 8 month. Great success!

French, Korean, Polish, Romanian were corrected and updated to the latest developments. Thanks to all GeoServer Transifex translators and Frank for managing!

Spot a translation mistake? Help translate here: [GeoServer Latest localizations](https://www.transifex.com/projects/p/geoserver/)


## About GeoServer 2.6


Articles and resources for GeoServer 2.6 series:



	
  * [Raster Views in GeoServer via the CoverageView concept](http://www.geo-solutions.it/blog/overageview-concept-for-geoserver/) (GeoSolutions)

	
  * [Advanced Raster Projection in GeoServer](http://www.geo-solutions.it/blog/developers-corner-advanced-raster-projection-geoserver/) (GeoSolutions)

	
  * [Supporting Wind Barbs In GeoServer and GeoTools](http://www.geo-solutions.it/blog/developers-corner-supporting-wind-barbs-geoserver-geotools/) (GeoSolutions)

	
  * [GeoServer now supports Vector Footprints for ImageMosaic](http://www.geo-solutions.it/blog/geoserver-supports-footprints-imagemosaic/) (GeoSolutions)

## Release notes

New Feature:

* [GEOS-4592](https://osgeo-org.atlassian.net/browse/GEOS-4592) WMS OutputFormat black listing
* [GEOS-6449](https://osgeo-org.atlassian.net/browse/GEOS-6449) Create GRIB community module
* [GEOS-6478](https://osgeo-org.atlassian.net/browse/GEOS-6478) Dynamic dimensions value module
* [GEOS-6514](https://osgeo-org.atlassian.net/browse/GEOS-6514) Restrict MIME types for WMS GetMap and GetFeatureInfo requests
* [GEOS-6528](https://osgeo-org.atlassian.net/browse/GEOS-6528) Change master password using REST API
* [GEOS-6530](https://osgeo-org.atlassian.net/browse/GEOS-6530) WPS PagedUnique Process

Improvement:

* [GEOS-3719](https://osgeo-org.atlassian.net/browse/GEOS-3719) GWC docs suggest URL replacement is the thing to do
* [GEOS-4149](https://osgeo-org.atlassian.net/browse/GEOS-4149) Make continuous wrapping for raster layers work like it does for vector layers (and other projection goodies too)
* [GEOS-5143](https://osgeo-org.atlassian.net/browse/GEOS-5143) Update CodeMirror to the 4.x series
* [GEOS-5609](https://osgeo-org.atlassian.net/browse/GEOS-5609) Config arguments for input parameters (e.g. Allowed Values)
* [GEOS-5670](https://osgeo-org.atlassian.net/browse/GEOS-5670) Clarify GeoServer Version / Java Version in docs
* [GEOS-6268](https://osgeo-org.atlassian.net/browse/GEOS-6268) Typo in monitoring documentation
* [GEOS-6325](https://osgeo-org.atlassian.net/browse/GEOS-6325) Allow styling language choice to be fully pluggable
* [GEOS-6372](https://osgeo-org.atlassian.net/browse/GEOS-6372) Add coverageBands customization capability on layer configuration
* [GEOS-6408](https://osgeo-org.atlassian.net/browse/GEOS-6408) Provide better logging when required to fall back on embedded data directory
* [GEOS-6455](https://osgeo-org.atlassian.net/browse/GEOS-6455) GridCoverageFactory hints initialization
* [GEOS-6457](https://osgeo-org.atlassian.net/browse/GEOS-6457) Make the dispatched Operation available in Dispatcher.REQUEST thread local
* [GEOS-6458](https://osgeo-org.atlassian.net/browse/GEOS-6458) Allow plugins to customize XStreamPersister (register custom converters, aliases and the like)
* [GEOS-6464](https://osgeo-org.atlassian.net/browse/GEOS-6464) Interpolation of data instead of images for non-RGBA rasters
* [GEOS-6483](https://osgeo-org.atlassian.net/browse/GEOS-6483) Add Wicket UI for Community Script Module
* [GEOS-6484](https://osgeo-org.atlassian.net/browse/GEOS-6484) Improve bbox reprojection accuracy
* [GEOS-6491](https://osgeo-org.atlassian.net/browse/GEOS-6491) Add legend preview in the style edit pages
* [GEOS-6499](https://osgeo-org.atlassian.net/browse/GEOS-6499) Upgrade ImageIO-Ext version from 1.1.9 to 1.1.10 on GeoServer
* [GEOS-6506](https://osgeo-org.atlassian.net/browse/GEOS-6506) Allow custom namespaces for scripted processes
* [GEOS-6524](https://osgeo-org.atlassian.net/browse/GEOS-6524) Allow python wps processes to fill the input and output Parameter metadata section
* [GEOS-6534](https://osgeo-org.atlassian.net/browse/GEOS-6534) AbstractURLPublisher doesn't support conditional get
* [GEOS-6535](https://osgeo-org.atlassian.net/browse/GEOS-6535) Allow scripted processes to advertise progress status
* [GEOS-6536](https://osgeo-org.atlassian.net/browse/GEOS-6536) Provide GeoServerLifecycleHandler a callback right before reload starts
* [GEOS-6543](https://osgeo-org.atlassian.net/browse/GEOS-6543) GSIP-115: CoverageView support
* [GEOS-6546](https://osgeo-org.atlassian.net/browse/GEOS-6546) Add support for wps namespaced scripts with the rest api
* [GEOS-6567](https://osgeo-org.atlassian.net/browse/GEOS-6567) Reimplement AuthenticationCache using Guava Cache
* [GEOS-6569](https://osgeo-org.atlassian.net/browse/GEOS-6569) Support booleans in MapJSONFormat

Bug:

* [GEOS-2935](https://osgeo-org.atlassian.net/browse/GEOS-2935) Support for Oracle curve geometries
* [GEOS-3983](https://osgeo-org.atlassian.net/browse/GEOS-3983) Restconfig, reading and writing styles modifies them.
* [GEOS-4834](https://osgeo-org.atlassian.net/browse/GEOS-4834) Animated GIF do not properly support transparency
* [GEOS-4943](https://osgeo-org.atlassian.net/browse/GEOS-4943) /geoserver/accessDenied.jsp not found
* [GEOS-4991](https://osgeo-org.atlassian.net/browse/GEOS-4991) Problem with WMSGetFeatureInfo request when map cross the 180 dateline
* [GEOS-5318](https://osgeo-org.atlassian.net/browse/GEOS-5318) cross-site scripting vulnerability in layer preview pages
* [GEOS-5676](https://osgeo-org.atlassian.net/browse/GEOS-5676) Add information about strong cryptography installation in the user guide
* [GEOS-6109](https://osgeo-org.atlassian.net/browse/GEOS-6109) CAS login request exposes internal server URL
* [GEOS-6110](https://osgeo-org.atlassian.net/browse/GEOS-6110) CAS logout request is incorrect
* [GEOS-6211](https://osgeo-org.atlassian.net/browse/GEOS-6211) Assorted CSS documentation glitches
* [GEOS-6323](https://osgeo-org.atlassian.net/browse/GEOS-6323) Take ND coverages dimensions into account when checking size limits
* [GEOS-6373](https://osgeo-org.atlassian.net/browse/GEOS-6373) Persisters fails writing temporary file
* [GEOS-6381](https://osgeo-org.atlassian.net/browse/GEOS-6381) Missing user roles if using Authkey Authentication Filter
* [GEOS-6391](https://osgeo-org.atlassian.net/browse/GEOS-6391) Unable to get 5x5 test coverage when configuring a layer with footprint in some cases.
* [GEOS-6394](https://osgeo-org.atlassian.net/browse/GEOS-6394) importer cannot handle jagged geojson
* [GEOS-6402](https://osgeo-org.atlassian.net/browse/GEOS-6402) DXF format_options:layers
* [GEOS-6441](https://osgeo-org.atlassian.net/browse/GEOS-6441) Geometries jumping the dateline generate reprojection artifacts on datum shift
* [GEOS-6443](https://osgeo-org.atlassian.net/browse/GEOS-6443) GSIP 112 - Upgrade to Java 7
* [GEOS-6445](https://osgeo-org.atlassian.net/browse/GEOS-6445) IOUtils.xStreamPersist fails if /tmp on a different filesystem
* [GEOS-6452](https://osgeo-org.atlassian.net/browse/GEOS-6452) CAS doesn't work with GeoServer 2.5
* [GEOS-6456](https://osgeo-org.atlassian.net/browse/GEOS-6456) wrong CSW GetRecords numberOfRecordsReturned
* [GEOS-6459](https://osgeo-org.atlassian.net/browse/GEOS-6459) gs-printing tests depend on online resources
* [GEOS-6463](https://osgeo-org.atlassian.net/browse/GEOS-6463) WMS 1.3 GetCapabilities with JDBCConfig throws ClassCastException
* [GEOS-6476](https://osgeo-org.atlassian.net/browse/GEOS-6476) Animate reflector request fails due to NPE in WMS-EO Plugin
* [GEOS-6482](https://osgeo-org.atlassian.net/browse/GEOS-6482) Scale line pixel wrong location causes failure in GetMapIntegrationTest
* [GEOS-6485](https://osgeo-org.atlassian.net/browse/GEOS-6485) Build failure in GWCIntegrationTest caused by GeoTools CRS.transform change
* [GEOS-6492](https://osgeo-org.atlassian.net/browse/GEOS-6492) Styles.Handler parser accesses uninstantiated GeoServerDataDirectory bean
* [GEOS-6493](https://osgeo-org.atlassian.net/browse/GEOS-6493) WFS GetFeature with feature bounds enabled can leak connections
* [GEOS-6495](https://osgeo-org.atlassian.net/browse/GEOS-6495) Allow specification of min/max/domain attributes in python process input arguments
* [GEOS-6498](https://osgeo-org.atlassian.net/browse/GEOS-6498) SLD REST upload fails (HTTP 500) when SLD has ExternalGraphics
* [GEOS-6505](https://osgeo-org.atlassian.net/browse/GEOS-6505) Build failure in RESTMapperTest in path with spaces
* [GEOS-6507](https://osgeo-org.atlassian.net/browse/GEOS-6507) DescribeProcess should return the default value in literal input description
* [GEOS-6515](https://osgeo-org.atlassian.net/browse/GEOS-6515) Reprojection of ImageMosaic from native gives / by 0 error (regression?)
* [GEOS-6517](https://osgeo-org.atlassian.net/browse/GEOS-6517) Build failure caused by  GSIP 113 security filter change in gs-wms CapabilitiesIntegrationTest
* [GEOS-6522](https://osgeo-org.atlassian.net/browse/GEOS-6522) Add support for raw inputs and outputs to GeoServer WPS
* [GEOS-6525](https://osgeo-org.atlassian.net/browse/GEOS-6525) WMTS getTile request ignores STYLE parameter (or Geoserver provides invalid styles on WMTS getCapabilities)
* [GEOS-6533](https://osgeo-org.atlassian.net/browse/GEOS-6533) FilePublisher does not decode requestURI
* [GEOS-6542](https://osgeo-org.atlassian.net/browse/GEOS-6542) import can fail on windows due to file locking
* [GEOS-6548](https://osgeo-org.atlassian.net/browse/GEOS-6548) Java 7 Security Policy
* [GEOS-6551](https://osgeo-org.atlassian.net/browse/GEOS-6551) GSIP 106 ResourceStore API changes cause build failure in gs-main in path with spaces
* [GEOS-6552](https://osgeo-org.atlassian.net/browse/GEOS-6552) GeoServer WPS python script does not work for Layer results
* [GEOS-6560](https://osgeo-org.atlassian.net/browse/GEOS-6560) ModificationProxy cloning has issues on OSX
* [GEOS-6564](https://osgeo-org.atlassian.net/browse/GEOS-6564) WCS GranuleStack for mosaic contains duplicate entries
* [GEOS-6574](https://osgeo-org.atlassian.net/browse/GEOS-6574) Installation path locations for windows vista, windows 7, windows 8
* [GEOS-6579](https://osgeo-org.atlassian.net/browse/GEOS-6579) Wrong kvp parser for interpolation for WCS version 1.0.0

Task:

* [GEOS-6339](https://osgeo-org.atlassian.net/browse/GEOS-6339) Add documentation to ImageMosaic module
* [GEOS-6393](https://osgeo-org.atlassian.net/browse/GEOS-6393) Addition of documentation about Footprint management
* [GEOS-6537](https://osgeo-org.atlassian.net/browse/GEOS-6537) Improve documentation about JNDI connection pool configuration
* [GEOS-6550](https://osgeo-org.atlassian.net/browse/GEOS-6550) Update printing plugin dependencies to 2.1.0
* [GEOS-6576](https://osgeo-org.atlassian.net/browse/GEOS-6576) Modify gs-grib module after moving coverage-multidim modules from Geotools
* [GEOS-6577](https://osgeo-org.atlassian.net/browse/GEOS-6577) Update imageio-ext version referred in the docs
* [GEOS-6580](https://osgeo-org.atlassian.net/browse/GEOS-6580) OWS Dispatcher log could be improved
