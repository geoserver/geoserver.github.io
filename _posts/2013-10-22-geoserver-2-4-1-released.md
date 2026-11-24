---
author: geoserver
comments: true
date: 2013-10-22 01:43:22+00:00
layout: post
link: http://blog.geoserver.org/2013/10/21/geoserver-2-4-1-released/
slug: geoserver-2-4-1-released
title: GeoServer 2.4.1 Released
wordpress_id: 1692
categories:
- Announcements
tags:
- localization
---

The GeoServer team is pleased to announce the release of GeoServer 2.4.1:



	
  * GeoServer 2.4.1 download page


This is a stable release containing [bug fixes and incremental improvements](#release-notes), including:



	
  * CSW admin page

	
  * Fixed deployment without web jars

	
  * Polygon fill margin vendor option in CSS

	
  * Automatically link CSW (ISO) records to the respective WMS/WFS/WCS sources


This release is made in conjunction with [GeoTools 10.1](http://geotoolsnews.blogspot.com.au/2013/10/geotools-101-released.html).

Spot a translation mistake? Help translate here: [GeoServer Stable localisation](https://www.transifex.com/projects/p/geoserver_stable/)


### About the GeoServer 2.4 series


The following change control requests were completed during the development of GeoServer 2.4:



	
  * [Replace old KML module with new one ](https://web.archive.org/web/20131022/http://geoserver.org/display/GEOS/GSIP+98+-+replace+old+KML+module+with+new+one)(GSIP 98)

	
  * [Allow plugins to modify WMS MapContent before map rendering](https://web.archive.org/web/20131022/http://geoserver.org/display/GEOS/GSIP+92+-+Allow+plugins+to+modify+WMS+MapContent+before+map+rendering) (GSIP 92)

	
  * [Machinery to pass thread locals down in thread pools](https://web.archive.org/web/20131022/http://geoserver.org/display/GEOS/GSIP+96+-+Machinery+to+pass+thread+locals+down+in+thread+pools) (GSIP 96, fixes WPS asych requests security issues) - also available in 2.3.4

	
  * [Promote CSS Styling module from Community to Extension](https://web.archive.org/web/20131022/http://geoserver.org/display/GEOS/GSIP+97+-+Promote+CSS+Styling+module+from+Community+to+Extension) (GSIP 97) - also available in 2.3.2

	
  * [Graduate the INSPIRE module to extension status](https://web.archive.org/web/20131022/http://geoserver.org/display/GEOS/GSIP+94+-+Graduate+the+INSPIRE+module+to+extension+status) (GSIP 94) - also available in 2.3.2

	
  * [Promote XSLT community module to extension](https://web.archive.org/web/20131022/http://geoserver.org/display/GEOS/GSIP+93+promote+XSLT+community+module+to+extension) (GSIP 93) - also available in 2.3.1

	
  * The shapefile datastore was completely rewritten (mostly as a code cleanup)


Articles and blogs during GeoServer 2.4 development:

	
  * [GeoServer 2.4.0 Release Highlights]({% post_url 2013-10-02-geoserver-2-4-0-release-highlights %})

	
  * [GeoServer FOSS4G 2013](GeoServer FOSS4G 2013) ([State of GeoServer](http://www.slideshare.net/jgarnett/state-of-geo-server-foss4g-2013-26387643), [Introduction](http://www.slideshare.net/geosolutions/geoserver-an-introduction-for-beginners), [Steroids](https://www.slideshare.net/geosolutions/gs-steroids-sgiannecfoss4g20130103), [GeoFence](https://www.slideshare.net/geosolutions/advanced-geoserver-security-with-geofence), [RasterData](https://www.slideshare.net/geosolutions/raster-data-in-geoserver-and-geotools-achievements-issues-and-future-developments-27175325), [Spatio-Temporal](https://www.slideshare.net/geosolutions/geoserver-for-spatiotemporal-data-handling-with-examples-for-metoc-and-remote-sensing), [Cartographic Rendering](https://www.slideshare.net/geosolutions/advanced-cartographic-map-rendering-in-geoserver-27175092) )

	
  * [Translation Interview]({% post_url 2013-09-03-geoserver-translation-interview %})

	
  * GeoServer in a clustered configuration ([Part 1](https://web.archive.org/web/20131022/http://blog.opengeo.org/2013/04/18/geoserver-in-a-clustered-configuration-part-1/), [Part 2](https://web.archive.org/web/20131022/http://blog.opengeo.org/2013/04/30/geoserver-in-a-clustered-configuration-part-2/))

	
  * [New GeoServer community on Google+]({% post_url 2013-05-13-new-geoserver-community-on-google %})

	
  * [How to publish GDAL/MrSID image formats on a production GeoServer](https://web.archive.org/web/20131022/http://blog.opengeo.org/2013/03/13/how-to-publish-gdalmrsid-image-formats-on-a-production-geoserver-on-windows/)

	
  * GeoServer crunch time ([Part I](https://web.archive.org/web/20131022/http://www.lisasoft.com/blog/geoserver-crunch-time), [Part II](https://web.archive.org/web/20131022/http://www.lisasoft.com/blog/geoserver-crunch-time-ii) and [Part III](https://web.archive.org/web/20131022/http://www.lisasoft.com/blog/geoserver-crunch-time-iii))

	
  * FOSS4G-NA slides ([GeoServer In Production](https://web.archive.org/web/20131022/http://blog.opengeo.org/wp-content/uploads/2013/05/GeoServerProduction.pdf), [GeoServer CSS Module](https://web.archive.org/web/20131022/http://blog.opengeo.org/wp-content/uploads/2013/05/foss4gna2013-geoserver-css.pdf), [Scripting GeoServer with GeoScript](https://web.archive.org/web/20131022/http://blog.opengeo.org/wp-content/uploads/2013/05/Scripting-GeoServer-with-GeoScript.pdf), [The State of GeoServer 2013](https://web.archive.org/web/20131022/http://blog.opengeo.org/wp-content/uploads/2013/05/State-of-GeoServer-2013.pdf))

	
  * INSPIRE Conference 2013 slides ([Analysing GeoServer compatibility with INSPIRE requirements](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime?from_search=2))

	
  * FOSSGIS 2013 slides ([Introduction to GeoServer](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime))

----

## GeoServer 2.4.1

Released on 21 October 2013

#### Download format

- [Binary (OS independent)](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.1/geoserver-2.4.1-bin.zip/download)
- [Web Archive](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.1/geoserver-2.4.1-war.zip)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4.1/geoserver-2.4.1.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4.1/geoserver-2.4.1.dmg/download)
- [Source Code](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.1/geoserver-2.4.1-src.zip)

#### Documentation

- [HTML Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.1/geoserver-2.4.1-htmldoc.zip)
- [API Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.1/geoserver-2.4.1-javadoc.zip)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-app-schema-plugin.zip)
- [ArcSDE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-arcsde-plugin.zip)
- [DB2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-db2-plugin.zip)
- [H2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-h2-plugin.zip)
- [MySQL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-mysql-plugin.zip)
- [Oracle](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-oracle-plugin.zip)
- [Pregeneralized features](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-feature-pregeneralized-plugin.zip)
- [SQL Server](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-sqlserver-plugin.zip)
- [Teradata](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-teradata-plugin.zip)
- [VPF](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-vpf-plugin.zip)
- [INSPIRE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-inspire-plugin.zip)

**Coverage store**

- [GDAL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-gdal-plugin.zip)
- [Image Pyramid](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-pyramid-plugin.zip)
- [JPEG2000](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-jp2k-plugin.zip)
- [JDBC Image Mosaic](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-imagemosaic-jdbc-plugin.zip)

**Other**

- [Chart dynamic symbolizer](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-charts-plugin.zip)
- [Control flow](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-control-flow-plugin.zip)
- [Cross layer filtering](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-querylayer-plugin.zip)
- [CSS styling](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-css-plugin.zip)
- [Excel output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-excel-plugin.zip)
- [GeoSearch](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-geosearch-plugin.zip)
- [Image Map output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-imagemap-plugin.zip)
- [OGR output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-ogr-plugin.zip)
- [XSLT output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-xslt-plugin.zip)
- [WPS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-wps-plugin.zip)
- [CAS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-cas-plugin.zip)
- Monitor ([Core](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-monitor-plugin.zip), [Hibernate](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-monitor-hibernate-plugin.zip))
- [CSW](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.1/geoserver-2.4.1-csw-plugin.zip)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19584

## Release notes

Improvement:

* [GEOS-5983](https://osgeo-org.atlassian.net/browse/GEOS-5983) Add a way for styling to know what kind of KML output mode we are using
* [GEOS-5984](https://osgeo-org.atlassian.net/browse/GEOS-5984) Add support for polygon fill margin vendor option in CSS
* [GEOS-6011](https://osgeo-org.atlassian.net/browse/GEOS-6011) Publish records for layer groups too
* [GEOS-6012](https://osgeo-org.atlassian.net/browse/GEOS-6012) Automatically link CSW (ISO) records to the respective WMS/WFS/WCS sources
* [GEOS-6063](https://osgeo-org.atlassian.net/browse/GEOS-6063) Allow creation of imagemap for points using a wellknownname  different from circle
* [GEOS-6077](https://osgeo-org.atlassian.net/browse/GEOS-6077) Create an endpoint for webapps to authenticate against

Bug:

* [GEOS-5054](https://osgeo-org.atlassian.net/browse/GEOS-5054) Role lookup fails on secured LDAP servers
* [GEOS-5858](https://osgeo-org.atlassian.net/browse/GEOS-5858) Inconsistent representation of workspace specific styles in rest
* [GEOS-5938](https://osgeo-org.atlassian.net/browse/GEOS-5938) CSW lacks an admin page
* [GEOS-5963](https://osgeo-org.atlassian.net/browse/GEOS-5963) Cannot use all CSS standard colors in CSS styling module
* [GEOS-5972](https://osgeo-org.atlassian.net/browse/GEOS-5972) GeoServer cannot be started without web jars, in particular web-security removal prevents startup
* [GEOS-5975](https://osgeo-org.atlassian.net/browse/GEOS-5975) Css styling extension doesn't work under jre6 (yes on jre7)
* [GEOS-5995](https://osgeo-org.atlassian.net/browse/GEOS-5995) Deadlock firing an ApplicationEvent
* [GEOS-6047](https://osgeo-org.atlassian.net/browse/GEOS-6047) dependency for community importer-bdb module com.sleepycat:je:jar:4.1.10 not found in repositories
* [GEOS-6051](https://osgeo-org.atlassian.net/browse/GEOS-6051) SQLServer - native geometry serialization delivers incomplete geometry
* [GEOS-6062](https://osgeo-org.atlassian.net/browse/GEOS-6062) When using an empty Abstract in SLD an exception is thrown
* [GEOS-6091](https://osgeo-org.atlassian.net/browse/GEOS-6091) Support CSW requests with different types in query and in outputschema.
* [GEOS-6093](https://osgeo-org.atlassian.net/browse/GEOS-6093) Spaces in custom dimension values
