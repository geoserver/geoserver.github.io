---
author: geoserver
comments: true
date: 2014-01-20 20:25:00+00:00
layout: post
link: http://blog.geoserver.org/2014/01/20/geoserver-2-4-4-released/
slug: geoserver-2-4-4-released
title: GeoServer 2.4.4 Released
wordpress_id: 1764
categories:
- Announcements
tags:
- localization
---

The GeoServer team is pleased to announce the release of GeoServer 2.4.4:



	
  * GeoServer 2.4.4 download page


This is a stable release containing [bug fixes and incremental improvements](#release-notes), including:



	
  * Role service implementation based on LDAP

	
  * CSV output for app-schema simple features level zero

	
  * WPS GeoTiff tiling improvements

	
  * Layer rendering robustness issues relating to mis specified fonts

	
  * Fixes to Symbology Encoding Halo parsing

	
  * And more! Checkout of the [change log](#release-notes) for the full list


Thanks to all those who contributed fixes, and documentation corrections, for this release. This release is made in conjunction with [GeoTools 10.4](http://geotoolsnews.blogspot.com.au/2014/01/geotools-104-released.html).

Spot a translation mistake? Help translate here: [GeoServer Stable localization](https://www.transifex.com/projects/p/geoserver_stable/)


### About the GeoServer 2.4 series


The following change control requests were completed during the development of GeoServer 2.4:



	
  * [Replace old KML module with new one ](https://web.archive.org/web/20140120/http://geoserver.org/display/GEOS/GSIP+98+-+replace+old+KML+module+with+new+one)(GSIP 98)

	
  * [Allow plugins to modify WMS MapContent before map rendering](https://web.archive.org/web/20140120/http://geoserver.org/display/GEOS/GSIP+92+-+Allow+plugins+to+modify+WMS+MapContent+before+map+rendering) (GSIP 92)

	
  * [Machinery to pass thread locals down in thread pools](https://web.archive.org/web/20140120/http://geoserver.org/display/GEOS/GSIP+96+-+Machinery+to+pass+thread+locals+down+in+thread+pools) (GSIP 96, fixes WPS asych requests security issues) - also available in 2.3.4

	
  * [Promote CSS Styling module from Community to Extension](https://web.archive.org/web/20140120/http://geoserver.org/display/GEOS/GSIP+97+-+Promote+CSS+Styling+module+from+Community+to+Extension) (GSIP 97) - also available in 2.3.2

	
  * [Graduate the INSPIRE module to extension status](https://web.archive.org/web/20140120/http://geoserver.org/display/GEOS/GSIP+94+-+Graduate+the+INSPIRE+module+to+extension+status) (GSIP 94) - also available in 2.3.2

	
  * [Promote XSLT community module to extension](https://web.archive.org/web/20140120/http://geoserver.org/display/GEOS/GSIP+93+promote+XSLT+community+module+to+extension) (GSIP 93) - also available in 2.3.1

	
  * The shapefile datastore was completely rewritten (mostly as a code cleanup)


Articles and blogs during GeoServer 2.4 development:

	
  * [GeoServer 2.4.0 Release Highlights]({% post_url 2013-10-02-geoserver-2-4-0-release-highlights %})

	
  * [GeoServer FOSS4G 2013](GeoServer FOSS4G 2013) ([State of GeoServer](http://www.slideshare.net/jgarnett/state-of-geo-server-foss4g-2013-26387643), [Introduction](http://www.slideshare.net/geosolutions/geoserver-an-introduction-for-beginners), [Steroids](https://www.slideshare.net/geosolutions/gs-steroids-sgiannecfoss4g20130103), [GeoFence](https://www.slideshare.net/geosolutions/advanced-geoserver-security-with-geofence), [RasterData](https://www.slideshare.net/geosolutions/raster-data-in-geoserver-and-geotools-achievements-issues-and-future-developments-27175325), [Spatio-Temporal](https://www.slideshare.net/geosolutions/geoserver-for-spatiotemporal-data-handling-with-examples-for-metoc-and-remote-sensing), [Cartographic Rendering](https://www.slideshare.net/geosolutions/advanced-cartographic-map-rendering-in-geoserver-27175092))

	
  * [Translation Interview]({% post_url 2013-09-03-geoserver-translation-interview %})

	
  * GeoServer in a clustered configuration ([Part 1](http://blog.opengeo.org/2013/04/18/geoserver-in-a-clustered-configuration-part-1/), [Part 2](http://blog.opengeo.org/2013/04/30/geoserver-in-a-clustered-configuration-part-2/))

	
  * [New GeoServer community on Google+]({% post_url 2013-05-13-new-geoserver-community-on-google %})

	
  * [How to publish GDAL/MrSID image formats on a production GeoServer](http://blog.opengeo.org/2013/03/13/how-to-publish-gdalmrsid-image-formats-on-a-production-geoserver-on-windows/)

	
  * GeoServer crunch time ([Part I](http://www.lisasoft.com/blog/geoserver-crunch-time), [Part II](http://www.lisasoft.com/blog/geoserver-crunch-time-ii) and [Part III](http://www.lisasoft.com/blog/geoserver-crunch-time-iii))

	
  * FOSS4G-NA slides ([GeoServer In Production](http://blog.opengeo.org/wp-content/uploads/2013/05/GeoServerProduction.pdf), [GeoServer CSS Module](http://blog.opengeo.org/wp-content/uploads/2013/05/foss4gna2013-geoserver-css.pdf), [Scripting GeoServer with GeoScript](http://blog.opengeo.org/wp-content/uploads/2013/05/Scripting-GeoServer-with-GeoScript.pdf), [The State of GeoServer 2013](http://blog.opengeo.org/wp-content/uploads/2013/05/State-of-GeoServer-2013.pdf))

	
  * INSPIRE Conference 2013 slides ([Analysing GeoServer compatibility with INSPIRE requirements](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime?from_search=2))

	
  * FOSSGIS 2013 slides ([Introduction to GeoServer](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime))

----

## GeoServer 2.4.4

Released on Jan 20, 2014

#### Download format

- [Binary (OS independent)](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.4/geoserver-2.4.4-bin.zip/download)
- [Web Archive](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.4/geoserver-2.4.4-war.zip)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4.4/geoserver-2.4.4.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4.4/geoserver-2.4.4.dmg/download)
- [Source Code](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.4/geoserver-2.4.4-src.zip)

#### Documentation

- [HTML Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.4/geoserver-2.4.4-htmldoc.zip)
- [PDF Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.4/geoserver-2.4.4-pdfdoc.zip)
- [API Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.4/geoserver-2.4.4-javadoc.zip)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-app-schema-plugin.zip)
- [ArcSDE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-arcsde-plugin.zip)
- [DB2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-db2-plugin.zip)
- [H2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-h2-plugin.zip)
- [MySQL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-mysql-plugin.zip)
- [Oracle](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-oracle-plugin.zip)
- [Pregeneralized features](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-feature-pregeneralized-plugin.zip)
- [SQL Server](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-sqlserver-plugin.zip)
- [Teradata](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-teradata-plugin.zip)
- [VPF](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-vpf-plugin.zip)
- [INSPIRE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-inspire-plugin.zip)

**Coverage store**

- [GDAL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-gdal-plugin.zip)
- [Image Pyramid](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-pyramid-plugin.zip)
- [JPEG2000](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-jp2k-plugin.zip)
- [JDBC Image Mosaic](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-imagemosaic-jdbc-plugin.zip)

**Other**

- [Chart dynamic symbolizer](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-charts-plugin.zip)
- [Control flow](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-control-flow-plugin.zip)
- [Cross layer filtering](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-querylayer-plugin.zip)
- [CSS styling](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-css-plugin.zip)
- [Excel output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-excel-plugin.zip)
- [GeoSearch](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-geosearch-plugin.zip)
- [Image Map output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-imagemap-plugin.zip)
- [OGR output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-ogr-plugin.zip)
- [XSLT output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-xslt-plugin.zip)
- [WPS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-wps-plugin.zip)
- [CAS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-cas-plugin.zip)
- Monitor ([Core](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-monitor-plugin.zip), [Hibernate](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-monitor-hibernate-plugin.zip))
- [CSW](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.4/geoserver-2.4.4-csw-plugin.zip)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19861

## Release notes

Improvement:

* [GEOS-5813](https://osgeo-org.atlassian.net/browse/GEOS-5813) Add a RoleService implementation using LDAP as a source
* [GEOS-6218](https://osgeo-org.atlassian.net/browse/GEOS-6218) Enable CSV outputFormat for complex features with SF0 schema
* [GEOS-6251](https://osgeo-org.atlassian.net/browse/GEOS-6251) labels from multiple attributes are not rendered if one attributes value is NULL
* [GEOS-6258](https://osgeo-org.atlassian.net/browse/GEOS-6258) GeoWebCache 304 responses treated as errors by monitoring extension
* [GEOS-6275](https://osgeo-org.atlassian.net/browse/GEOS-6275) [WPS CORE] - Improve the GeoTIFF PPIO Tiling Management

Bug:

* [GEOS-5944](https://osgeo-org.atlassian.net/browse/GEOS-5944) Layer rendering fails if font-style etc are missing
* [GEOS-6124](https://osgeo-org.atlassian.net/browse/GEOS-6124) "halo" defaults not being actioned (with SLD/SE 1.1)
* [GEOS-6171](https://osgeo-org.atlassian.net/browse/GEOS-6171) "Disk used" to say "N/A" when quota off
* [GEOS-6247](https://osgeo-org.atlassian.net/browse/GEOS-6247) KML points not extruding
* [GEOS-6257](https://osgeo-org.atlassian.net/browse/GEOS-6257) Using rest api from IE browser fails
* [GEOS-6301](https://osgeo-org.atlassian.net/browse/GEOS-6301) kml module is missing from source zip release file
