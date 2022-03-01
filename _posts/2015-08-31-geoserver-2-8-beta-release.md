---
author: geoserver
comments: true
date: 2015-08-31 14:47:19+00:00
layout: post
link: http://blog.geoserver.org/2015/08/31/geoserver-2-8-beta-release/
slug: geoserver-2-8-beta-release
title: GeoServer 2.8-beta released
wordpress_id: 2292
categories:
- Announcements
- Vulnerability
---

We are happy to announce the release of [GeoServer 2.8-beta](http://geoserver.org/release/2.8-beta/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8-beta/geoserver-2.8-beta-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8-beta/geoserver-2.8-beta-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8-beta/geoserver-2.8-beta.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8-beta/geoserver-2.8-beta.exe/download)) along with docs and extensions.

GeoServer 2.8 has a wide range of new features, behind the scenes changes, and a several of important security updates. This is beta release of GeoServer made in conjunction with GeoTools 14-beta.

This beta release is made available for collaboration with our user list (and is not intended for production). The beta release marks the of a feature freeze, we appreciate any and all testing during this period as we prepare for a September release.

New capabilities:



	
  * Read/write [PostGIS curve support](http://docs.geoserver.org/latest/en/user/webadmin/data/layers.html#curves-support-vector)

	
  * ContrastEnhancement can now be [refined](http://docs.geoserver.org/latest/en/user/styling/sld-reference/rastersymbolizer.html#contrastenhancement) with choice of algorithm

	
  * New vendor options to [sort spatial data with respect z-order](http://docs.geoserver.org/latest/en/user/styling/sld-extensions/z-order/index.html) (within a layer or across multiple layers)

	
  * Return of a popular feature from GeoServer 1.0 - the ability to [filter a vector layer contents](http://docs.geoserver.org/latest/en/user/webadmin/data/layers.html#restricting-features-showing-up-in-the-layer) prior to publication (great for layers such as point-of-interest that have several kinds of content in one table)

	
  * REST API for [security access control](http://docs.geoserver.org/latest/en/user/rest/api/accesscontrol.html) (a popular request for those configuring GeoServer remotely)

	
  * Importer [REST API](http://docs.geoserver.org/latest/en/user/extensions/importer/rest_reference.html) can include processing steps (using gdalwarp/gdal_translate/gdaladdo transformations to prepare data for publication, [with a number of ready to use examples](http://docs.geoserver.org/latest/en/user/extensions/importer/rest_examples.html))

	
  * Import REST API available to allows a [granules to be added to an existing mosaic](http://docs.geoserver.org/latest/en/user/extensions/importer/rest_examples.html#adding-a-new-granule-into-an-existing-mosaic)

	
  * Application Schema configuration files [can now be managed](http://docs.geoserver.org/latest/en/user/rest/examples/curl.html#uploading-an-app-schema-mapping-file) via REST API

	
  * GetMap support for [by layer interpolation](http://docs.geoserver.org/latest/en/user/services/wms/vendor.html#interpolations) methods

	
  * When creating a new style (or importing new data) you can choose to [generate a new SLD or CSS style](http://docs.geoserver.org/latest/en/user/webadmin/data/styles.html#add-a-style)

	
  * New shape symbol (extshape://arrow) with parameters dynamically controlling proportions

	
  * Target maps using multiple scripts by specifying more than one font in the SLD, the fonts will be tested in turn to see which one can display a particular label, or portion of label (e.g., for multiscript labels, mix of latin/arabic/chinese/...)

	
  * New map projections supported: sinusoidal, gnomonic, meteosat second generation, general oblique, added new [custom AUTO codes for gnomonic and stereographic](http://docs.geoserver.org/latest/en/user/services/wms/nonstandardautonamespace.html)

	
  * When JAI-EXT is enabled, the image mosaic can support images with different color models (.e.g, gray, paletted and color in the same mosaic)


Fixes and improvements:

	
  * Significant increase in GML 3.X encoding speed

	
  * Pretty print option for style REST API

	
  * Allow environment variables to be used in [freemarker template files](http://docs.geoserver.org/latest/en/user/tutorials/freemarker.html)

	
  * GeoWebCache parameter filters can now be set via GUI

	
  * INSPIRE metadata entry is now more forgiving and can be entered on a layer by layer basis

	
  * Fix for XXE security vulnerability has been [revised](https://osgeo-org.atlassian.net/browse/GEOS-7095) and now functions in a [JBoss environment](https://osgeo-org.atlassian.net/browse/GEOS-7139)

	
  * Faster startup for installations with large number of Oracle layers

	
  * The CSV output format can now handle WFS GetFeature join results (will transparently flatten the joined features)


Internal changes:

	
  * [JAI-Ext](https://github.com/geosolutions-it/jai-ext) integration for geospatial specific image processing operations, adding direct support for NODATA in raster sources. Disabled by default, [needs to be enabled using a system variable.](http://docs.geoserver.org/latest/en/user/webadmin/server/JAI.html#jai-ext)

	
  * Replacement of vecmath with EJML matrix library

	
  * Due to license restrictions the oracle extension no longer includes an Oracle JDBC driver, see the [user guide](http://docs.geoserver.org/latest/en/user/data/database/oracle.html#oracle-install) for manual install instructions.


Community update:

	
  * We would like to welcome [Stefano Costa](https://github.com/ridethepenguin) (GeoSolutions) as a new committer!

	
  * Developers guide refresh covering [release cycle](http://docs.geoserver.org/latest/en/developer/policies/community-process.html#release-cycle), updating [PSC](http://docs.geoserver.org/latest/en/developer/policies/psc.html) members, and fixing tutorials

	
  * Responsible disclosure expectations covered on the [website](http://geoserver.org/comm/) and [user guide](http://docs.geoserver.org/latest/en/user/introduction/gettinginvolved.html#bug-tracking)


See [release notes](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=10164) for more information.

Thanks to Jody (Boundless) for publishing this beta, and the entire GeoServer team for an enormous effort bringing this release together.


## About GeoServer 2.8


GeoServer 2.8 is [scheduled](http://geoserver.org/roadmap/) for September release. For more information:



	
  * [XEE Vunerability](http://blog.geoserver.org/2015/06/27/geoserver-xee-vulnerability/) (GeoServer)

	
  * [Z ordering features within and across feature types and layers](http://docs.geoserver.org/latest/en/user/styling/sld-extensions/z-order/index.html#z-ordering-features-within-and-across-feature-types-and-layers) (User Manual)

	
  * [JAI-Ext, the Open Source replacement for Oracle JAI](http://www.geo-solutions.it/blog/developers-corner-jai-ext-the-open-source-replacement-for-oracle-jai/) (GeoSolutions)

	
  * [Customizable arrow in GeoServer](http://www.geo-solutions.it/blog/customizable-arrow-geoserver/) (GeoSolutions)

	
  * [PostGIS Curve Support](http://www.geo-solutions.it/blog/postgis-curves-in-geoserver/) (GeoSolutions)

	
  * [Improved NetCDF/GRIB support in GeoServer](http://www.geo-solutions.it/blog/netcdf-grib-support-geoserver/) (GeoSolutions)


For additional details see the [2.8-beta](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=10164) and [2.8-M0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=10163) release notes.


## New Community Modules


In addition to the formal GeoServer 2.8 release our code base has a community area for ideas an experimentation:



	
  * WCS and WPS output formats based on gdal_translate to provide a greater range of output formats

	
  * Embedded GeoFence server, REST API and GUI is the result of a productive collaboration between GeoSolutions and Boundless offering greater rule-based control of GeoServer security

	
  * [MongoDB DataStore](http://boundlessgeo.com/2015/07/mongodb-collaboration/) enabling GeoServer to publish from this popular JSON based document database (no zip packaging, needs volunteer)


Community modules should be considered a work-in-progress and are subject to quality assurance, documentation IP checks and a maintainer before being considered ready for release.
