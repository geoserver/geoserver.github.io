---
author: geoserver
comments: true
date: 2014-10-03 16:15:27+00:00
layout: post
link: http://blog.geoserver.org/2014/10/03/geoserver-2-6-0-released/
slug: geoserver-2-6-0-released
title: GeoServer 2.6.0 Released
wordpress_id: 2019
categories:
- Announcements
tags:
- Features
- release
---

The GeoServer team is pleased to account the greatly anticipated 2.6.0 release. This release is now available for [download](http://geoserver.org/release/2.6.0/) with [zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.0/geoserver-2.6.0-bin.zip), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.0/geoserver-2.6.0-war.zip), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.0/geoserver-2.6.0.dmg) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.6.0/geoserver-2.6.0.exe) bundles available (see the [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20399) for details on last minute fixes).

Thanks to the user list for testing the 2.6-beta and 2.6-RC1, this collaboration and testing really helped smooth our migration to Java 7. The [Code Sprint ](http://blog.geoserver.org/2014/09/14/java-code-sprint/)at FOSS4G was able to fill in gaps testing oracle curve support, the marlin extension on a range of platforms, and providing [documentation](http://docs.geoserver.org/latest/en/user/styling/sld-extensions/pointsymbols.html#shape-symbols) introducing wind barbs and inline custom marks.

Thanks to Ian Turton, Jody Garnett and Kevin Smith for assisting in this release. This release is made in conjunction with GeoTools 12.0.


### Java 7


_Ensure you are using Oracle o OpenJDK Java 7._

Support for Java 7 is not only a new feature for GeoServer 2.6.0 - **Java 7 is a requirement**.

The [installation](http://docs.geoserver.org/latest/en/user/installation/java.html) instructions have been updated for windows, mac and linux users. Mac users will have an easy upgrade as GeoServer.app includes an appropriate Java 7 virtual machine.


### New and Improved


New functionality:



	
  * **WFS Cascade: **WFS Cascade has been updated to use a brand new GeoTools wfs client implementation.

	
  * **Curve support for GML and WMS:** GeoServer curve support has been added for interaction with Oracle Spatial. To configure look for Linearization tolerance when configuring your layer. As outlined in the FOSS4G presentation we are seeking interested parties to implement or fund curve support for PostGIS and SQL Server.

	
  * **Advanced Projection Handling:** Considerable care has been taken in the handling of raster data across the dateline and in polar projections.

	
  * **Coverage Views: **recombine bands from different sources into a multi-band coverage (use "configure new coverage view" when creating a new layer).

[![Coverage View Band Selection](/img/uploads/coverage_view-300x1141.png)](http://blog.geoserver.org/2014/10/03/geoserver-2-6-0-released/coverage_view/)

	
  * **Vector footprints support in image mosaics**: you can now cut out of your images the "bad" parts using vector footprints, setup as sidecar wkb/wkt files, or as a global footprints shapefile

	
  * **Pluggable Styles: **this change allows greater integration with the CSS Extension (and opens the door for even more style languages in the future)

	
  * **Wind Barbs and WKT Graphics:** for [greater creative control](http://docs.geoserver.org/latest/en/user/styling/sld-extensions/pointsymbols.html#shape-symbols).

	
  * **Printing: **new implementation from our friends at MapFish (based on MapFish 2.x).

	
  * **Scripting community module: **a great new editor for editing scripts directly from the web application

[![GeoScript Editor for GeoServer](/img/uploads/edit_script-300x217.png)](http://blog.geoserver.org/2014/10/03/geoserver-2-6-0-released/edit_script/)

	
  * **New raster formats:** NetCDF and GRIB support, for anyone dealing with multidimensional data. NetCDF is also supported as a WCS output format, and it allows to extract data hypercubes out of your WCS server. Finally, it is also possible to build multidimensional mosaics of NetCDF and GRIB files, and add to the using the harvest REST API.

	
  * **Language and Internationalisation:** Turkish support has been added and French, Korean, Polish, Romanian are all caught up with the latest developments. Spot a translation mistake? Help translate here: [GeoServer Latest localizations](https://www.transifex.com/projects/p/geoserver/)




## About GeoServer 2.6


Articles and resources for GeoServer 2.6 series:



	
  * [GeoServer at FOSS4G](http://blog.geoserver.org/2014/10/01/geoserver-at-foss4g/)

	
    * [State of GeoServer and GeoTools 2014](http://vimeo.com/106835755) ([slides](http://www.slideshare.net/jgarnett/state-of-geoserver-geotools-and-friends-2014))




	
  * [Raster Views in GeoServer via the CoverageView concept](http://www.geo-solutions.it/blog/overageview-concept-for-geoserver/) (GeoSolutions)

	
  * [Advanced Raster Projection in GeoServer](http://www.geo-solutions.it/blog/developers-corner-advanced-raster-projection-geoserver/) (GeoSolutions)

	
  * [Supporting Wind Barbs In GeoServer and GeoTools](http://www.geo-solutions.it/blog/developers-corner-supporting-wind-barbs-geoserver-geotools/) (GeoSolutions)

	
  * [GeoServer now supports Vector Footprints for ImageMosaic](http://www.geo-solutions.it/blog/geoserver-supports-footprints-imagemosaic/) (GeoSolutions)

	
  * [2.6-RC1 announcement](http://blog.geoserver.org/2014/08/18/geoserver-2-6-rc1-released/) and [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?version=20536&styleName=&projectId=10311)

	
  * [2.6-beta announcement](http://blog.geoserver.org/2014/07/24/geoserver-2-6-beta-released/) and [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20172)


