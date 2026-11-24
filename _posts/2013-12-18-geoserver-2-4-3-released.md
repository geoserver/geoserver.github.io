---
author: geoserver
comments: true
date: 2013-12-18 07:21:53+00:00
layout: post
link: http://blog.geoserver.org/2013/12/18/geoserver-2-4-3-released/
slug: geoserver-2-4-3-released
title: GeoServer 2.4.3 Released
wordpress_id: 1736
categories:
- Announcements
tags:
- localization
- release
---

The GeoServer team is pleased to announce the release of GeoServer 2.4.2:



	
  * GeoServer 2.4.3 download page


This is a stable release containing [bug fixes and incremental improvements](#release-notes), including:



	
  * A great performance  improvement for those using sql views

	
  * Fix for defining a workspace style using CSS extension

	
  * Workspace styles can now manage their own images and graphics

	
  * Thanks to all those who contributed fixes, and documentation corrections, for this release.


This release is made in conjunction with [GeoTools 10.3](http://geotoolsnews.blogspot.com.au/2013/12/geotools-103-released.html).

Spot a translation mistake? Help translate here: [GeoServer Stable localisation](https://www.transifex.com/projects/p/geoserver_stable/)


### About the GeoServer 2.4 series


The following change control requests were completed during the development of GeoServer 2.4:



	
  * [Replace old KML module with new one ](https://web.archive.org/web/20131218/http://geoserver.org/display/GEOS/GSIP+98+-+replace+old+KML+module+with+new+one)(GSIP 98)

	
  * [Allow plugins to modify WMS MapContent before map rendering](https://web.archive.org/web/20131218/http://geoserver.org/display/GEOS/GSIP+92+-+Allow+plugins+to+modify+WMS+MapContent+before+map+rendering) (GSIP 92)

	
  * [Machinery to pass thread locals down in thread pools](https://web.archive.org/web/20131218/http://geoserver.org/display/GEOS/GSIP+96+-+Machinery+to+pass+thread+locals+down+in+thread+pools) (GSIP 96, fixes WPS asych requests security issues) - also available in 2.3.4

	
  * [Promote CSS Styling module from Community to Extension](https://web.archive.org/web/20131218/http://geoserver.org/display/GEOS/GSIP+97+-+Promote+CSS+Styling+module+from+Community+to+Extension) (GSIP 97) - also available in 2.3.2

	
  * [Graduate the INSPIRE module to extension status](https://web.archive.org/web/20131218/http://geoserver.org/display/GEOS/GSIP+94+-+Graduate+the+INSPIRE+module+to+extension+status) (GSIP 94) - also available in 2.3.2

	
  * [Promote XSLT community module to extension](https://web.archive.org/web/20131218/http://geoserver.org/display/GEOS/GSIP+93+promote+XSLT+community+module+to+extension) (GSIP 93) - also available in 2.3.1

	
  * The shapefile datastore was completely rewritten (mostly as a code cleanup)


Articles and blogs during GeoServer 2.4 development:

	
  * [GeoServer 2.4.0 Release Highlights]({% post_url 2013-10-02-geoserver-2-4-0-release-highlights %})

	
  * [GeoServer FOSS4G 2013](GeoServer FOSS4G 2013) ([State of GeoServer](http://www.slideshare.net/jgarnett/state-of-geo-server-foss4g-2013-26387643), [Introduction](http://www.slideshare.net/geosolutions/geoserver-an-introduction-for-beginners), [Steroids](https://www.slideshare.net/geosolutions/gs-steroids-sgiannecfoss4g20130103), [GeoFence](https://www.slideshare.net/geosolutions/advanced-geoserver-security-with-geofence), [RasterData](https://www.slideshare.net/geosolutions/raster-data-in-geoserver-and-geotools-achievements-issues-and-future-developments-27175325), [Spatio-Temporal](https://www.slideshare.net/geosolutions/geoserver-for-spatiotemporal-data-handling-with-examples-for-metoc-and-remote-sensing), [Cartographic Rendering](https://www.slideshare.net/geosolutions/advanced-cartographic-map-rendering-in-geoserver-27175092))

	
  * [Translation Interview]({% post_url 2013-09-03-geoserver-translation-interview %})

	
  * GeoServer in a clustered configuration ([Part 1](https://web.archive.org/web/20131218/http://blog.opengeo.org/2013/04/18/geoserver-in-a-clustered-configuration-part-1/), [Part 2](https://web.archive.org/web/20131218/http://blog.opengeo.org/2013/04/30/geoserver-in-a-clustered-configuration-part-2/))

	
  * [New GeoServer community on Google+]({% post_url 2013-05-13-new-geoserver-community-on-google %})

	
  * [How to publish GDAL/MrSID image formats on a production GeoServer](https://web.archive.org/web/20131218/http://blog.opengeo.org/2013/03/13/how-to-publish-gdalmrsid-image-formats-on-a-production-geoserver-on-windows/)

	
  * GeoServer crunch time ([Part I](https://web.archive.org/web/20131218/http://www.lisasoft.com/blog/geoserver-crunch-time), [Part II](https://web.archive.org/web/20131218/http://www.lisasoft.com/blog/geoserver-crunch-time-ii) and [Part III](https://web.archive.org/web/20131218/http://www.lisasoft.com/blog/geoserver-crunch-time-iii))

	
  * FOSS4G-NA slides ([GeoServer In Production](https://web.archive.org/web/20131218/http://blog.opengeo.org/wp-content/uploads/2013/05/GeoServerProduction.pdf), [GeoServer CSS Module](https://web.archive.org/web/20131218/http://blog.opengeo.org/wp-content/uploads/2013/05/foss4gna2013-geoserver-css.pdf), [Scripting GeoServer with GeoScript](https://web.archive.org/web/20131218/http://blog.opengeo.org/wp-content/uploads/2013/05/Scripting-GeoServer-with-GeoScript.pdf), [The State of GeoServer 2013](https://web.archive.org/web/20131218/http://blog.opengeo.org/wp-content/uploads/2013/05/State-of-GeoServer-2013.pdf))

	
  * INSPIRE Conference 2013 slides ([Analysing GeoServer compatibility with INSPIRE requirements](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime?from_search=2))

	
  * FOSSGIS 2013 slides ([Introduction to GeoServer](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime))

----

## GeoServer 2.4.3

Released on December 18 2013

#### Download format

- [Binary (OS independent)](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.3/geoserver-2.4.3-bin.zip/download)
- [Web Archive](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.3/geoserver-2.4.3-war.zip)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4.3/geoserver-2.4.3.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4.3/geoserver-2.4.3.dmg/download)
- [Source Code](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.3/geoserver-2.4.3-src.zip)

#### Documentation

- [HTML Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.3/geoserver-2.4.3-htmldoc.zip)
- [PDF Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.3/geoserver-2.4.3-pdfdoc.zip)
- [API Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.3/geoserver-2.4.3-javadoc.zip)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-app-schema-plugin.zip)
- [ArcSDE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-arcsde-plugin.zip)
- [DB2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-db2-plugin.zip)
- [H2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-h2-plugin.zip)
- [MySQL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-mysql-plugin.zip)
- [Oracle](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-oracle-plugin.zip)
- [Pregeneralized features](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-feature-pregeneralized-plugin.zip)
- [SQL Server](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-sqlserver-plugin.zip)
- [Teradata](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-teradata-plugin.zip)
- [VPF](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-vpf-plugin.zip)
- [INSPIRE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-inspire-plugin.zip)

**Coverage store**

- [GDAL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-gdal-plugin.zip)
- [Image Pyramid](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-pyramid-plugin.zip)
- [JPEG2000](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-jp2k-plugin.zip)
- [JDBC Image Mosaic](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-imagemosaic-jdbc-plugin.zip)

**Other**

- [Chart dynamic symbolizer](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-charts-plugin.zip)
- [Control flow](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-control-flow-plugin.zip)
- [Cross layer filtering](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-querylayer-plugin.zip)
- [CSS styling](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-css-plugin.zip)
- [Excel output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-excel-plugin.zip)
- [GeoSearch](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-geosearch-plugin.zip)
- [Image Map output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-imagemap-plugin.zip)
- [OGR output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-ogr-plugin.zip)
- [XSLT output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-xslt-plugin.zip)
- [WPS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-wps-plugin.zip)
- [CAS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-cas-plugin.zip)
- Monitor ([Core](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-monitor-plugin.zip), [Hibernate](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-monitor-hibernate-plugin.zip))
- [CSW](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.3/geoserver-2.4.3-csw-plugin.zip)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19728

## Release notes

Bug:

* [GEOS-5317](https://osgeo-org.atlassian.net/browse/GEOS-5317) Fetching data from sql views uses more queries than strictly necessary
* [GEOS-5523](https://osgeo-org.atlassian.net/browse/GEOS-5523) Document special behaviour for connection strings with oracle NG
* [GEOS-6005](https://osgeo-org.atlassian.net/browse/GEOS-6005) GeoServer re-computes sql-view feature type structure for each request
* [GEOS-6101](https://osgeo-org.atlassian.net/browse/GEOS-6101) Controlling legend appearance with LEGEND_OPTIONS Documentation has small error
* [GEOS-6152](https://osgeo-org.atlassian.net/browse/GEOS-6152) Update download links pointing to old gridlock site to ares.boundlessgeo.org
* [GEOS-6161](https://osgeo-org.atlassian.net/browse/GEOS-6161) jdbcconfig doesn't copy out sample scripts on first run
* [GEOS-6162](https://osgeo-org.atlassian.net/browse/GEOS-6162) jdbcconfig attempts database connection regardless of being enabled/disabled
* [GEOS-6166](https://osgeo-org.atlassian.net/browse/GEOS-6166) Typo in Filter Function Reference documentation
* [GEOS-6170](https://osgeo-org.atlassian.net/browse/GEOS-6170) WPS distribution package lacks ant jars, breaks startup
* [GEOS-6176](https://osgeo-org.atlassian.net/browse/GEOS-6176) Create a new workspace specific style breaks CSS extension user interface
* [GEOS-6193](https://osgeo-org.atlassian.net/browse/GEOS-6193) LDAP test connection is broken when using userGroupService
* [GEOS-6194](https://osgeo-org.atlassian.net/browse/GEOS-6194) Backport to 2.4.x fix to LDAPAuthenticationProvider to support sAMAccountName={1} as a filter
* [GEOS-6197](https://osgeo-org.atlassian.net/browse/GEOS-6197) Coarse raster resolution when a coverage layer is used along with vector ones, and the buffer parameter is specified
* [GEOS-6201](https://osgeo-org.atlassian.net/browse/GEOS-6201) Missing abstract definition of layer group in gwc integration
* [GEOS-6212](https://osgeo-org.atlassian.net/browse/GEOS-6212) Control flow can log a negative number of active requests when requests fail to parse
* [GEOS-6215](https://osgeo-org.atlassian.net/browse/GEOS-6215) workspace styles can only use images/graphics from global workspace
* [GEOS-6326](https://osgeo-org.atlassian.net/browse/GEOS-6326) Error when trying to publish a new ImageMosaic layer
