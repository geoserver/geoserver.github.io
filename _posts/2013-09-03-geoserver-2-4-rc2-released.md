---
author: geoserver
comments: true
date: 2013-09-03 21:05:19+00:00
layout: post
link: http://blog.geoserver.org/2013/09/03/geoserver-2-4-rc2-released/
slug: geoserver-2-4-rc2-released
title: GeoServer 2.4-RC2 released
wordpress_id: 1593
categories:
- Announcements
---

GeoServer team is pleased to announce the release of GeoServer 2.4-RC2 with a few last minute additions:



	
  * Catalog Service Web has graduated to a formal Extension, including new admin page and many fixes

	
  * A fix for those using Tomcat Apache Portable Runtime

	
  * Removal of the VPF Extension

	
  * See the [GeoServer 2.4-RC2 release notes](#release-notes) for more details


This is our last shot before [FOSS4G](http://2013.foss4g.org) so we really need to call out to our great community and ask for your assistance with testing. There are two aspects where your your help is vital:



	
  * Our developers are not in position to test on every platform, so if we need to ask for assistance **testing in strange environments** (like [Windows](http://windows.microsoft.com) or [WildFly](http://www.wildfly.org))

	
  * In a similar fashion the developers tend to play with a few specific sample datasets which have been donated to the project for this purpose. If you can **test with your own data** and confirm everything works as expected it will save us both any surprises


To quickly report back success, drop a message on twitter with the [#GeoServer](https://twitter.com/search?q=%23GeoServer) tag!

If you discover any issue, please let us know using the [bug tracker](http://jira.codehaus.org) (Use [xircles](http://xircles.codehaus.org) to set up a CodeHaus login).


### About the GeoServer 2.4 series


The following change control requests were completed during the development of GeoServer 2.4:



	
  * [Replace old KML module with new one ](https://web.archive.org/web/20130903/http://geoserver.org/display/GEOS/GSIP+98+-+replace+old+KML+module+with+new+one)(GSIP 98)

	
  * [Allow plugins to modify WMS MapContent before map rendering](https://web.archive.org/web/20130903/http://geoserver.org/display/GEOS/GSIP+92+-+Allow+plugins+to+modify+WMS+MapContent+before+map+rendering) (GSIP 92)

	
  * [Machinery to pass thread locals down in thread pools](https://web.archive.org/web/20130903/http://geoserver.org/display/GEOS/GSIP+96+-+Machinery+to+pass+thread+locals+down+in+thread+pools) (GSIP 96, fixes WPS asych requests security issues) - also available in 2.3.4

	
  * [Promote CSS Styling module from Community to Extension](https://web.archive.org/web/20130903/http://geoserver.org/display/GEOS/GSIP+97+-+Promote+CSS+Styling+module+from+Community+to+Extension) (GSIP 97) - also available in 2.3.2

	
  * [Graduate the INSPIRE module to extension status](https://web.archive.org/web/20130903/http://geoserver.org/display/GEOS/GSIP+94+-+Graduate+the+INSPIRE+module+to+extension+status) (GSIP 94) - also available in 2.3.2

	
  * [Promote XSLT community module to extension](https://web.archive.org/web/20130903/http://geoserver.org/display/GEOS/GSIP+93+promote+XSLT+community+module+to+extension) (GSIP 93) - also available in 2.3.1

	
  * The shapefile datastore was completely rewritten (mostly as a code cleanup)


Articles and blogs during GeoServer 2.4 development:

	
  * GeoServer in a clustered configuration ([Part 1](http://blog.opengeo.org/2013/04/18/geoserver-in-a-clustered-configuration-part-1/), [Part 2](http://blog.opengeo.org/2013/04/30/geoserver-in-a-clustered-configuration-part-2/))

	
  * [New GeoServer community on Google+](http://blog.geoserver.org/2013/05/13/new-geoserver-community-on-google/)

	
  * [How to publish GDAL/MrSID image formats on a production GeoServer](http://blog.opengeo.org/2013/03/13/how-to-publish-gdalmrsid-image-formats-on-a-production-geoserver-on-windows/)

	
  * GeoServer crunch time ([Part I](http://www.lisasoft.com/blog/geoserver-crunch-time), [Part II](http://www.lisasoft.com/blog/geoserver-crunch-time-ii) and [Part III](http://www.lisasoft.com/blog/geoserver-crunch-time-iii))

	
  * FOSS4G-NA slides ([GeoServer In Production](http://blog.opengeo.org/wp-content/uploads/2013/05/GeoServerProduction.pdf), [GeoServer CSS Module](http://blog.opengeo.org/wp-content/uploads/2013/05/foss4gna2013-geoserver-css.pdf), [Scripting GeoServer with GeoScript](http://blog.opengeo.org/wp-content/uploads/2013/05/Scripting-GeoServer-with-GeoScript.pdf), [The State of GeoServer 2013](http://blog.opengeo.org/wp-content/uploads/2013/05/State-of-GeoServer-2013.pdf))

	
  * INSPIRE Conference 2013 slides ([Analysing GeoServer compatibility with INSPIRE requirements](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime?from_search=2))

	
  * FOSSGIS 2013 slides ([Introduction to GeoServer](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime))

----

## GeoServer 2.4-RC2

Released on Sep 3rd, 2013

#### Download format

- [Binary (OS independent)](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC2/geoserver-2.4-RC2-bin.zip/download)
- [Web Archive](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC2/geoserver-2.4-RC2-war.zip)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC2/geoserver-2.4-RC2.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC2/geoserver-2.4-RC2.dmg/download)
- [Source Code](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC2/geoserver-2.4-RC2-src.zip)

#### Documentation

- [HTML Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC2/geoserver-2.4-RC2-htmldoc.zip)
- [PDF Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC2/geoserver-2.4-RC2-pdfdoc.zip)
- [API Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC2/geoserver-2.4-RC2-javadoc.zip)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-app-schema-plugin.zip)
- [ArcSDE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-arcsde-plugin.zip)
- [DB2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-db2-plugin.zip)
- [H2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-h2-plugin.zip)
- [MySQL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-mysql-plugin.zip)
- [Oracle](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-oracle-plugin.zip)
- [Pregeneralized features](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-feature-pregeneralized-plugin.zip)
- [SQL Server](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-sqlserver-plugin.zip)
- [Teradata](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-teradata-plugin.zip)
- [INSPIRE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-inspire-plugin.zip)

**Coverage store**

- [GDAL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-gdal-plugin.zip)
- [Image Pyramid](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-pyramid-plugin.zip)
- [JPEG2000](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-jp2k-plugin.zip)
- [JDBC Image Mosaic](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-imagemosaic-jdbc-plugin.zip)

**Other**

- [Chart dynamic symbolizer](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-charts-plugin.zip)
- [Control flow](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-control-flow-plugin.zip)
- [Cross layer filtering](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-querylayer-plugin.zip)
- [CSS styling](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-css-plugin.zip)
- [Excel output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-excel-plugin.zip)
- [GeoSearch](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-geosearch-plugin.zip)
- [Image Map output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-imagemap-plugin.zip)
- [OGR output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-ogr-plugin.zip)
- [XSLT output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-xslt-plugin.zip)
- [WPS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-wps-plugin.zip)
- [CAS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-cas-plugin.zip)
- Monitor ([Core](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-monitor-plugin.zip), [Hibernate](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-monitor-hibernate-plugin.zip))
- [CSW](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC2/geoserver-2.4-RC2-csw-plugin.zip)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19547

## Release notes

Improvement:

* [GEOS-5985](https://osgeo-org.atlassian.net/browse/GEOS-5985) Tomcat with APR can result in full JVM crashes

Bug:

* [GEOS-5114](https://osgeo-org.atlassian.net/browse/GEOS-5114) GeoServer generates invalid PNG files when using raster symbolizers with extended color map
* [GEOS-5369](https://osgeo-org.atlassian.net/browse/GEOS-5369) CSW GetRecordById will NPE in case there are multiple record types available
* [GEOS-5689](https://osgeo-org.atlassian.net/browse/GEOS-5689) Reloading configuration with workspace specific settings results in exception
* [GEOS-5947](https://osgeo-org.atlassian.net/browse/GEOS-5947) Remove Raster Custom Dimension additional ordering
* [GEOS-5987](https://osgeo-org.atlassian.net/browse/GEOS-5987) DescribeRecord xsi:schemaLocation lacks a / just before CSW-discovery.xsd
* [GEOS-5991](https://osgeo-org.atlassian.net/browse/GEOS-5991) Any VendorOption outside TextSymbolizer fails validation in SLD 1.1
* [GEOS-5997](https://osgeo-org.atlassian.net/browse/GEOS-5997) Basic authentication filter message digest is not thread safe
* [GEOS-6000](https://osgeo-org.atlassian.net/browse/GEOS-6000) LRUAuthenticationCacheImpl TimerTask causes deadlock
* [GEOS-6003](https://osgeo-org.atlassian.net/browse/GEOS-6003) Login and password not saved in JDBC Authentication Provider.
