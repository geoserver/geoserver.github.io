---
author: geoserver
comments: true
date: 2013-09-20 11:12:44+00:00
layout: post
link: http://blog.geoserver.org/2013/09/20/geoserver-2-4-released/
slug: geoserver-2-4-released
title: GeoServer 2.4 Released!
wordpress_id: 1605
categories:
- Announcements
- Features
tags:
- localization
---

The GeoServer team is pleased to announce the final release of GeoServer 2.4.0. Some great final bug fixes reported from 2.4-RC2 made it into this release. Check out the [change log](#release-notes) for the details. More Information about the new and noteworthy of the GeoServer 2.4 series can be found [here](http://blog.geoserver.org/2013/09/03/geoserver-2-4-rc2-released/).

Its worth to announce that GeoServer is available in for more languages: Spanish, French, Polish and Romanian. Many thanks to [Jorge Sanz](https://www.transifex.com/accounts/profile/xurxosanz/), [Alexandre Gacon](https://www.transifex.com/accounts/profile/AlexGacon/), [Jaros?aw P?kal](https://www.transifex.com/accounts/profile/phiocouek/) and [Sorin C?linic?](https://www.transifex.com/accounts/profile/csorin/) for their contributions. Again, feel free to join a translation team and review existing translations at [Transifex](https://www.transifex.com/projects/p/geoserver_stable).

A special thank you to those who helped test all the beta and release candidates.

Download the new release, try it out, and be sure to report any issues found in the [bug tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS) or on the [mailing list](https://web.archive.org/web/20130920/http://geoserver.org/display/GEOS/Mailing+Lists). Thanks for using GeoServer!


### About the GeoServer 2.4 series


The following change control requests were completed during the development of GeoServer 2.4:



	
  * [Replace old KML module with new one ](https://web.archive.org/web/20130920/http://geoserver.org/display/GEOS/GSIP+98+-+replace+old+KML+module+with+new+one)(GSIP 98)

	
  * [Allow plugins to modify WMS MapContent before map rendering](https://web.archive.org/web/20130920/http://geoserver.org/display/GEOS/GSIP+92+-+Allow+plugins+to+modify+WMS+MapContent+before+map+rendering) (GSIP 92)

	
  * [Machinery to pass thread locals down in thread pools](https://web.archive.org/web/20130920/http://geoserver.org/display/GEOS/GSIP+96+-+Machinery+to+pass+thread+locals+down+in+thread+pools) (GSIP 96, fixes WPS asych requests security issues) - also available in 2.3.4

	
  * [Promote CSS Styling module from Community to Extension](https://web.archive.org/web/20130920/http://geoserver.org/display/GEOS/GSIP+97+-+Promote+CSS+Styling+module+from+Community+to+Extension) (GSIP 97) - also available in 2.3.2

	
  * [Graduate the INSPIRE module to extension status](https://web.archive.org/web/20130920/http://geoserver.org/display/GEOS/GSIP+94+-+Graduate+the+INSPIRE+module+to+extension+status) (GSIP 94) - also available in 2.3.2

	
  * [Promote XSLT community module to extension](https://web.archive.org/web/20130920/http://geoserver.org/display/GEOS/GSIP+93+promote+XSLT+community+module+to+extension) (GSIP 93) - also available in 2.3.1

	
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

## GeoServer 2.4.0

Released on Sept 18, 2013

#### Download format

- [Binary (OS independent)](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.0/geoserver-2.4.0-bin.zip/download)
- [Web Archive](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.0/geoserver-2.4.0-war.zip)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4.0/geoserver-2.4.0.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4.0/geoserver-2.4.0.dmg/download)
- [Source Code](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.0/geoserver-2.4.0-src.zip)

#### Documentation

- [HTML Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.0/geoserver-2.4.0-htmldoc.zip)
- [PDF Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.0/geoserver-2.4.0-pdfdoc.zip)
- [API Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.0/geoserver-2.4.0-javadoc.zip)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-app-schema-plugin.zip)
- [ArcSDE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-arcsde-plugin.zip)
- [DB2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-db2-plugin.zip)
- [H2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-h2-plugin.zip)
- [MySQL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-mysql-plugin.zip)
- [Oracle](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-oracle-plugin.zip)
- [Pregeneralized features](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-feature-pregeneralized-plugin.zip)
- [SQL Server](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-sqlserver-plugin.zip)
- [Teradata](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-teradata-plugin.zip)
- [VPF](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-vpf-plugin.zip)
- [INSPIRE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-inspire-plugin.zip)

**Coverage store**

- [GDAL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-gdal-plugin.zip)
- [Image Pyramid](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-pyramid-plugin.zip)
- [JPEG2000](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-jp2k-plugin.zip)
- [JDBC Image Mosaic](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-imagemosaic-jdbc-plugin.zip)

**Other**

- [Chart dynamic symbolizer](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-charts-plugin.zip)
- [Control flow](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-control-flow-plugin.zip)
- [Cross layer filtering](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-querylayer-plugin.zip)
- [CSS styling](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-css-plugin.zip)
- [Excel output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-excel-plugin.zip)
- [GeoSearch](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-geosearch-plugin.zip)
- [Image Map output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-imagemap-plugin.zip)
- [OGR output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-ogr-plugin.zip)
- [XSLT output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-xslt-plugin.zip)
- [WPS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-wps-plugin.zip)
- [CAS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-cas-plugin.zip)
- Monitor ([Core](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-monitor-plugin.zip), [Hibernate](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4.0/geoserver-2.4.0-monitor-hibernate-plugin.zip))

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19565

## Release notes

Bug:

* [GEOS-5763](https://osgeo-org.atlassian.net/browse/GEOS-5763) Cascade WMS fails with HTTP connection pooling on.
* [GEOS-5819](https://osgeo-org.atlassian.net/browse/GEOS-5819) Build failure in LDAPAuthenticationProviderTest
* [GEOS-6015](https://osgeo-org.atlassian.net/browse/GEOS-6015) GeoJSON uses wrong mime type
* [GEOS-6016](https://osgeo-org.atlassian.net/browse/GEOS-6016) GeoServer won't open shapefile stores created with previous versions when the fstype param is set
* [GEOS-6017](https://osgeo-org.atlassian.net/browse/GEOS-6017) Layer preview GML 3.2 dropdown choice doesn't work
* [GEOS-6023](https://osgeo-org.atlassian.net/browse/GEOS-6023) 2.4 RC2 - modifying the rest security, rest anonymous access does not show workspaces anymore
* [GEOS-6024](https://osgeo-org.atlassian.net/browse/GEOS-6024) 2.4-RC2 - rest PUT for style reference (and possibly other references) does not work anymore
* [GEOS-6027](https://osgeo-org.atlassian.net/browse/GEOS-6027) Wrong lookat generated in kml superoverlays if when the layer bbox happens to be contained only in some higher level tile
* [GEOS-6028](https://osgeo-org.atlassian.net/browse/GEOS-6028) Superoverlay outputs are not always visible from the start (one needs to zoom in)
* [GEOS-6029](https://osgeo-org.atlassian.net/browse/GEOS-6029) KML: force output in 4326 even if the request calls for a different SRS
* [GEOS-6034](https://osgeo-org.atlassian.net/browse/GEOS-6034) Explicit GetMap with KML output defaulted to download mode, now it defaults to refresh mode
* [GEOS-6035](https://osgeo-org.atlassian.net/browse/GEOS-6035) [App-schema] GetPropertyValue operation not supported
* [GEOS-6039](https://osgeo-org.atlassian.net/browse/GEOS-6039) Monitoring audit logging broken
* [GEOS-6042](https://osgeo-org.atlassian.net/browse/GEOS-6042) NPE in monitoring module while handling a KML reflector
