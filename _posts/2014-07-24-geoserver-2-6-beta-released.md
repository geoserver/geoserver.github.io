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


<blockquote>_As a development release, 2.6-beta is considered experimental and is provided for testing purposes. This release is not recommended for production (even if you are excited by the new features)._</blockquote>


This release is made in conjunction with GeoTools 12-beta. Thanks to Kevin for making a beta release of GeoWebCache [1.6.0-beta](http://sourceforge.net/projects/geowebcache/files/geowebcache/1.6.0-beta/) with relatively little notice.


### What to expect ... and what we expect from you


A complete [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20172) is available from the issue tracker. We will ask you to wait for 2.6.0 before we let Andrea write a [pretty](http://blog.geoserver.org/2014/01/21/geoserver-2-5-beta-released/) blog with pictures illustrating what features have been added. Instead 2.6-beta is my chance to ask you to _**download GeoServer 2.6-beta for testing**_.


<blockquote>_Testing is a key part of the open source [social contract](http://www.how2map.com/2013/09/opensource-and-social-contract.html). The GeoServer team have identified a few areas where we would like to ask for help. This is your best chance to identify issues early while we still have time to do something about it. For those making use of [commercial support](http://geoserver.org/support/) ask your vendor about their plans for 2.6-beta testing. We would like to ensure the functionality you depend on is ready to go for a Q2 release._</blockquote>


When testing Geoserver 2.6-beta please let us know on the [user list](http://geoserver.org/comm/) (or [#GeoServer](https://twitter.com/search?q=%23geoserver)) how it works for you. We will be sure to thank you in the final release announcement and product presentations.

**Java 7 Testing**

With Oracle [retiring Java 6](http://www.oracle.com/technetwork/java/eol-135779.html) security updates the time has come to raise the minimum bar to Java 7.


<blockquote>_We know a lot of downstream projects (such as [OSGeo Live](http://live.osgeo.org/en/index.html)) have been waiting for GeoServer to support Java 7. Thanks to CSIRO, Boundless, GeoSolutions for providing Java 7 build environments allowing us to make this transition in a responsible fashion._</blockquote>


Testing:



	
  * This is a major testing priority on all platforms.

	
  * Windows 7: The start.bat used by the run manually install has trouble running as an administrator. We recommend installing as a service of this release ([GEOS-5687](https://jira.codehaus.org/browse/GEOS-6587))

	
  * Mac: You will need to install Oracle Java 7 (as OpenJDK 7 is not yet available for OSX). We have not yet figured out how to run GeoServer.App with Java 7 ([GEOS-6588](https://jira.codehaus.org/browse/GEOS-6588)) and are open to suggestions.


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


<blockquote>_We have experimented with several approaches over the years (including ISO 19107 and a code sprint with the deegree project) and it is great to finally have a solution. As a long time user of the JTS Topology Suite we have been limited to a Point, Line and Polygon model of Geometry. Andrea has very carefully extended these base classes in to allow for both GML output and rendering. The trick is using a tolerance to convert the the arcs and circles into line work for geometry processing._</blockquote>


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


<blockquote>_GeoServer 2.6 simplifies where configuration files are stored on disk. Previous versions were willing to spread configuration files between the webapps folder, the data directory and any additional directories on request. For GeoServer 2.6 configuration files are limited to the data directory as a step towards improving clustering support and growing our JDBC Config story._</blockquote>


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


