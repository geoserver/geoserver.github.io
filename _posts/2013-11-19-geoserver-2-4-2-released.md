---
author: geoserver
comments: true
date: 2013-11-19 13:58:59+00:00
layout: post
link: http://blog.geoserver.org/2013/11/19/geoserver-2-4-2-released/
slug: geoserver-2-4-2-released
title: GeoServer 2.4.2 released
wordpress_id: 1709
tags:
- localization
---

The GeoServer team is pleased to announce the release of GeoServer 2.4.2:



	
  * GeoServer 2.4.2 download page


This is a stable release containing [bug fixes and incremental improvements](#release-notes), including:



	
  * Total matched feature count available in JSON output (contributed by Paul Biskup)

	
  * Ability to control how scale hints are computed in WMS 1.1 (contributed by Roy Braam and Mauricio Pazos)

	
  * Support for randomized symbol fills in both SLD and CSS (thanks to New South Wales Geological survey for sponsoring it)

	
  * Better support for data with 3D coordinates using GML3/GeoJSON, and associated improvements in the SQL Server backend (thanks to IGEA, Croatia, for sponsoring this work)

	
  * WCS 1.0 can be disabled

	
  * Several translation updates and improvements, thanks to the translation team. In no particular order: Polish, Korean, German, Lithuanian, Spanish, Romanian, French

	
  * Several small fixes in the docs (thanks to all the good people that contributed them!)


This release is made in conjunction with [GeoTools 10.2](http://geotoolsnews.blogspot.it/2013/11/geotools-102-released.html).

Spot a translation mistake? Help translate here: [GeoServer Stable localisation](https://www.transifex.com/projects/p/geoserver_stable/)


### About the GeoServer 2.4 series


The following change control requests were completed during the development of GeoServer 2.4:



	
  * [Replace old KML module with new one ](https://web.archive.org/web/20131119/http://geoserver.org/display/GEOS/GSIP+98+-+replace+old+KML+module+with+new+one)(GSIP 98)

	
  * [Allow plugins to modify WMS MapContent before map rendering](https://web.archive.org/web/20131119/http://geoserver.org/display/GEOS/GSIP+92+-+Allow+plugins+to+modify+WMS+MapContent+before+map+rendering) (GSIP 92)

	
  * [Machinery to pass thread locals down in thread pools](https://web.archive.org/web/20131119/http://geoserver.org/display/GEOS/GSIP+96+-+Machinery+to+pass+thread+locals+down+in+thread+pools) (GSIP 96, fixes WPS asych requests security issues) - also available in 2.3.4

	
  * [Promote CSS Styling module from Community to Extension](https://web.archive.org/web/20131119/http://geoserver.org/display/GEOS/GSIP+97+-+Promote+CSS+Styling+module+from+Community+to+Extension) (GSIP 97) - also available in 2.3.2

	
  * [Graduate the INSPIRE module to extension status](https://web.archive.org/web/20131119/http://geoserver.org/display/GEOS/GSIP+94+-+Graduate+the+INSPIRE+module+to+extension+status) (GSIP 94) - also available in 2.3.2

	
  * [Promote XSLT community module to extension](https://web.archive.org/web/20131119/http://geoserver.org/display/GEOS/GSIP+93+promote+XSLT+community+module+to+extension) (GSIP 93) - also available in 2.3.1

	
  * The shapefile datastore was completely rewritten (mostly as a code cleanup)


Articles and blogs during GeoServer 2.4 development:

	
  * [GeoServer 2.4.0 Release Highlights]({% post_url 2013-10-02-geoserver-2-4-0-release-highlights %})

	
  * [GeoServer FOSS4G 2013](GeoServer FOSS4G 2013) ([State of GeoServer](http://www.slideshare.net/jgarnett/state-of-geo-server-foss4g-2013-26387643), [Introduction](http://www.slideshare.net/geosolutions/geoserver-an-introduction-for-beginners), [Steroids](https://www.slideshare.net/geosolutions/gs-steroids-sgiannecfoss4g20130103), [GeoFence](https://www.slideshare.net/geosolutions/advanced-geoserver-security-with-geofence), [RasterData](https://www.slideshare.net/geosolutions/raster-data-in-geoserver-and-geotools-achievements-issues-and-future-developments-27175325), [Spatio-Temporal](https://www.slideshare.net/geosolutions/geoserver-for-spatiotemporal-data-handling-with-examples-for-metoc-and-remote-sensing), [Cartographic Rendering](https://www.slideshare.net/geosolutions/advanced-cartographic-map-rendering-in-geoserver-27175092) )

	
  * [Translation Interview]({% post_url 2013-09-03-geoserver-translation-interview %})

	
  * GeoServer in a clustered configuration ([Part 1](http://blog.opengeo.org/2013/04/18/geoserver-in-a-clustered-configuration-part-1/), [Part 2](http://blog.opengeo.org/2013/04/30/geoserver-in-a-clustered-configuration-part-2/))

	
  * [New GeoServer community on Google+]({% post_url 2013-05-13-new-geoserver-community-on-google %})

	
  * [How to publish GDAL/MrSID image formats on a production GeoServer](http://blog.opengeo.org/2013/03/13/how-to-publish-gdalmrsid-image-formats-on-a-production-geoserver-on-windows/)

	
  * GeoServer crunch time ([Part I](http://www.lisasoft.com/blog/geoserver-crunch-time), [Part II](http://www.lisasoft.com/blog/geoserver-crunch-time-ii) and [Part III](http://www.lisasoft.com/blog/geoserver-crunch-time-iii))

	
  * FOSS4G-NA slides ([GeoServer In Production](http://blog.opengeo.org/wp-content/uploads/2013/05/GeoServerProduction.pdf), [GeoServer CSS Module](http://blog.opengeo.org/wp-content/uploads/2013/05/foss4gna2013-geoserver-css.pdf), [Scripting GeoServer with GeoScript](http://blog.opengeo.org/wp-content/uploads/2013/05/Scripting-GeoServer-with-GeoScript.pdf), [The State of GeoServer 2013](http://blog.opengeo.org/wp-content/uploads/2013/05/State-of-GeoServer-2013.pdf))

	
  * INSPIRE Conference 2013 slides ([Analysing GeoServer compatibility with INSPIRE requirements](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime?from_search=2))

	
  * FOSSGIS 2013 slides ([Introduction to GeoServer](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime))

----

## GeoServer 2.4.2

Released on November 19 2013

#### Download format

- [Binary (OS independent)](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.2/geoserver-2.4.2-bin.zip/download)
- [Web Archive](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.2/geoserver-2.4.2-war.zip)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4.2/geoserver-2.4.2.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4.2/geoserver-2.4.2.dmg/download)
- [Source Code](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.2/geoserver-2.4.2-src.zip)

#### Documentation

- [HTML Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.2/geoserver-2.4.2-htmldoc.zip)
- [API Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.2/geoserver-2.4.2-javadoc.zip)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-app-schema-plugin.zip)
- [ArcSDE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-arcsde-plugin.zip)
- [DB2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-db2-plugin.zip)
- [H2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-h2-plugin.zip)
- [MySQL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-mysql-plugin.zip)
- [Oracle](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-oracle-plugin.zip)
- [Pregeneralized features](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-feature-pregeneralized-plugin.zip)
- [SQL Server](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-sqlserver-plugin.zip)
- [Teradata](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-teradata-plugin.zip)
- [VPF](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-vpf-plugin.zip)
- [INSPIRE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-inspire-plugin.zip)

**Coverage store**

- [GDAL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-gdal-plugin.zip)
- [Image Pyramid](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-pyramid-plugin.zip)
- [JPEG2000](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-jp2k-plugin.zip)
- [JDBC Image Mosaic](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-imagemosaic-jdbc-plugin.zip)

**Other**

- [Chart dynamic symbolizer](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-charts-plugin.zip)
- [Control flow](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-control-flow-plugin.zip)
- [Cross layer filtering](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-querylayer-plugin.zip)
- [CSS styling](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-css-plugin.zip)
- [Excel output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-excel-plugin.zip)
- [GeoSearch](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-geosearch-plugin.zip)
- [Image Map output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-imagemap-plugin.zip)
- [OGR output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-ogr-plugin.zip)
- [XSLT output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-xslt-plugin.zip)
- [WPS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-wps-plugin.zip)
- [CAS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-cas-plugin.zip)
- Monitor ([Core](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-monitor-plugin.zip), [Hibernate](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-monitor-hibernate-plugin.zip))
- [CSW](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.2/geoserver-2.4.2-csw-plugin.zip)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19613

## Release notes

New Feature:

* [GEOS-6111](https://osgeo-org.atlassian.net/browse/GEOS-6111) Support repeated and randomized graphic fills in polygons

Improvement:

* [GEOS-6088](https://osgeo-org.atlassian.net/browse/GEOS-6088) Add support for count in json output
* [GEOS-6129](https://osgeo-org.atlassian.net/browse/GEOS-6129) Typo in documentation regarding antialias "format_options" parameter
* [GEOS-6159](https://osgeo-org.atlassian.net/browse/GEOS-6159) Document the kmlOutputMode enviroment variable

Bug:

* [GEOS-5487](https://osgeo-org.atlassian.net/browse/GEOS-5487) WCS 1.0.0 can't be disabled
* [GEOS-5555](https://osgeo-org.atlassian.net/browse/GEOS-5555) WFS 2.0.0 GetFeature ignores maxFeatures (update docs to make it clear it's called count there)
* [GEOS-5941](https://osgeo-org.atlassian.net/browse/GEOS-5941) Error ELEM_INFO STARTING_OFFSET when reading geometry collections from Oracle
* [GEOS-5962](https://osgeo-org.atlassian.net/browse/GEOS-5962) Log error when skipping faulty layers or layer groups during caps document generation
* [GEOS-5971](https://osgeo-org.atlassian.net/browse/GEOS-5971) Update sample requests in the docs for WFS 2.0
* [GEOS-6072](https://osgeo-org.atlassian.net/browse/GEOS-6072) Printing plugin misses Xerces JAR
* [GEOS-6079](https://osgeo-org.atlassian.net/browse/GEOS-6079) Saving styles from the Admin UI use the wrong encoding on some systems
* [GEOS-6083](https://osgeo-org.atlassian.net/browse/GEOS-6083) Wrong character encoding
* [GEOS-6087](https://osgeo-org.atlassian.net/browse/GEOS-6087) Forms don't handle non-ASCII characters correctly
* [GEOS-6099](https://osgeo-org.atlassian.net/browse/GEOS-6099) Layergroup titles not shown on layerpreview
* [GEOS-6113](https://osgeo-org.atlassian.net/browse/GEOS-6113) Exception : The input argument(s) may not be null with gs:Contour
* [GEOS-6122](https://osgeo-org.atlassian.net/browse/GEOS-6122) WFS GeoJSON output format strips z from 3d data
* [GEOS-6123](https://osgeo-org.atlassian.net/browse/GEOS-6123) WFS-T 1.1 transactions with 2.5D data either fail to parse or silently drop the third ordinate
* [GEOS-6126](https://osgeo-org.atlassian.net/browse/GEOS-6126) JP2K Extension is missing as a profile in web/app
* [GEOS-6128](https://osgeo-org.atlassian.net/browse/GEOS-6128) On the fly metatiling can return repeated tiles at (very) high zoom levels
* [GEOS-6135](https://osgeo-org.atlassian.net/browse/GEOS-6135) NPE when trying to access a OGR generated output format via WFS 2.0
* [GEOS-6151](https://osgeo-org.atlassian.net/browse/GEOS-6151) WPS can report progress percentage above 100 with asynch process execution

Wish:

* [GEOS-2996](https://osgeo-org.atlassian.net/browse/GEOS-2996) Have Mac GeoServer launcher use menu bar
