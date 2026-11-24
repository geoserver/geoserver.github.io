---
author: geoserver
comments: true
date: 2012-09-21 13:39:00+00:00
layout: post
link: http://blog.geoserver.org/2012/09/21/geoserver-2-2-released/
slug: geoserver-2-2-released
title: GeoServer 2.2 Released
wordpress_id: 1140
categories:
- Announcements
- Features
---

The GeoServer team is happy to announce to the release of GeoServer 2.2 and encourage you to download it and try out the great new features. The release of a new major version update is a big deal (the [last one]({% post_url 2011-05-12-geoserver-2-1 %}) was over 16 months ago) and, while you may have heard about some of the new features on the developer list, here are the highlights all in one place:

**Referencing**



	
  * **NTv2 and NADCon Support** allows for datum transformations with cm level precision (instead of the usual 4m, when all goes well). Both will activate only if the grid files are present in the data dir, so by default the mere presence of the method is harmless, but generally speaking this is very good news for whoever needs to increase reprojection accuracy. Thanks to Oscar Fonts and Andrea Aime.**
**

	
  * Continued work for supporting **high accuracy datum transformations** that now allow for user defined transformations supplied via WKT. Thanks to the [Catalan Cartographic Institute](http://www.icc.cat) for funding the work and to Oscar and Andrea for doing the development.

	
  * A new **[reprojection console](https://web.archive.org/web/20120921/http://osgeo-org.1560.n6.nabble.com/Little-reprojection-console-tt4631340.html)** allows users to interactively test transformations of points and other geometries back and forth between the chosen CRS, and also to verify the transformation method used matches the user expectations. Thanks Andrea.

	
  * Better support for un-referenced data with the new **[EPSG:40400](http://docs.geotools.org/latest/userguide/library/referencing/crs.html)** code that identifies a coordinate system made up of a generic 2D Cartesian plane. As well as support for **EPSG:102113** as an alias for Web Mercator.


**Data access**



	
  * **[Database-level security](http://geo-solutions.blogspot.com/2012/01/developers-corner-introducing-database.html)** implements the ability to use DBMS session startup and teardown scripts to alter user access the database during a specific request while falling back on connection pooling when the request is complete. Thanks to [Astrium GEO-Information Services](https://web.archive.org/web/20120921/http://www.astrium-geo.com/) for sponsoring GeoSolutions to make this improvement.

	
  * **[Sorting and paging](http://geo-solutions.blogspot.com/2011/12/wfs-for-masses-adding-support-for.html)** is now available in all WFS versions (in 1.0 and 1.1 as a vendor param) via the sortBy and startIndex/maxFeature parameters. Thanks to Justin Deoliveira and Andrea.

	
  * A new **[lenient capabilities mode](https://web.archive.org/web/20120921/http://blog.opengeo.org/2012/07/31/managing-fault-tolerance-in-geoserver-metadata/)** that allows the GeoServer capabilities documents to remain functioning despite the presence of misconfigured layers. Thanks to David Winslow for this work.

	
  * A new experimental **OGR data store** provides access to  a rich set of readable formats without needing special bridge libraries.

	
  * The **[image collection](http://docs.geotools.org/latest/userguide/library/coverage/image-collection.html)** coverage store allows users to serve un-referenced data through WMS using image/pixel space as the coordinate system. Thanks to [SFMTA](http://www.sfmta.com) for sponsoring OpenGeo to complete this work.

	
  * [Application schema support](http://docs.geoserver.org/latest/en/user/data/app-schema/index.html) has performance, stability, and functional improvements including reduced memory footprint, SQL joining support for more efficient queries of complex information models, support for WMS, and support for GML 3.2 application schemas. Thanks to Rini Angreani, Niels Charlier, Victor Tey, Ben Caradoc-Davies, and the rest of the team at [CSIRO](http://www.csiro.au/). This work was funded through [AuScope](http://www.auscope.org.au/) by the Australian Government.

	
  * BigTiff support has received some performance and scalability improvements courtesy of upgrade to [imageio-ext 1.1.5](http://geo-solutions.blogspot.it/2012/09/imageio-ext-1.1.5.html).


**Security**



	
  * A major retrofit of the GeoServer **[security subsystem](http://docs.geoserver.org/latest/en/user/security/index.html)** adding support for a number of new authentication mechanisms including **[LDAP](http://docs.geoserver.org/latest/en/user/security/tutorials/ldap/index.html)**, **[digest](http://docs.geoserver.org/latest/en/user/security/tutorials/digest/index.html)** and **[X.509](http://docs.geoserver.org/latest/en/user/security/tutorials/cert/index.html)** certificate authentication, and more. These improvements also includes the addition of **[user groups](http://docs.geoserver.org/latest/en/user/security/usergrouprole/usergroups.html)**. This is a continuation of work started by Christian Mueller as a Google Summer of Code project;  thanks to [NOAA](http://www.noaa.gov/) for sponsoring OpenGeo to help Christian and Justin bring it to completion.


**Web Feature Source (WFS)**



	
  * Support for **[WFS 2.0](https://web.archive.org/web/20120921/http://geoserver.org/display/GEOS/GSIP+61+-+WFS+2.0)** adds some interesting new capabilities to the WFS protocol such as paging, stored queries, and extended operators. Thanks to [IGN France](http://www.ign.fr/) and [Géoportail](http://www.geoportail.gouv.fr/) for sponsoring OpenGeo to make this improvement.

	
  * Along with WFS 2.0 comes support for GML 3.2.


**Web Map Service (WMS)**



	
  * Support for additional dimensions brings [**time and elevation**](http://geo-solutions.blogspot.com/2011/06/time-and-elevation-support-in-geoserver.html) support to both vector and raster data. And, with support for time, comes support for **[animation in WMS](http://docs.geoserver.org/stable/en/user/tutorials/animreflector.html)**. Thanks to Andrea, Alessio and GeoSolutions on both counts.

	
  * **[Rendering transformations](https://web.archive.org/web/20120921/http://docs.codehaus.org/display/GEOTOOLS/Rendering+transformations)** provide a bridge between WPS and WMS and allow for very powerful visualization capabilities for processing through normal WMS. Thanks to GeoSolutions for sponsoring this work (and Andrea for implementing it).

	
  * Support for **8-bit PNG output with transparency** resulting in a nice tradeoff of performance and appealing visualization. Special thanks to Andrea for this new feature.


**Web Processing Service (WPS)**



	
  * New WPS features include support for asynchronous process execution and a variety of new processes.


**Virtual Services**



	
  * **[Virtual services](http://docs.geoserver.org/latest/en/user/services/virtual-services.html)** allow GeoServer to support the notion of multitenancy, enabling a single GeoServer instance to publish multiple service endpoints. Thanks to NOAA for sponsoring OpenGeo to complete this improvement and a special thanks to Micah Wengren of NOAA for his leadership on the project.

	
  * **[Workspace local settings](https://web.archive.org/web/20120921/http://geoserver.org/display/GEOS/GSIP+67+-+Workspace+Local+Settings)** allow for specifying service settings such as contact information,  proxy settings, and output format settings on a per workspace basis.

	
  * **[Styles and layer groups](https://web.archive.org/web/20120921/http://geoserver.org/display/GEOS/GSIP+73+-+Workspace+Local+Styles+and+Layer+Groups)** can also now be defined on a per workspace basis.


**GeoWebCache**



	
  * A **GeoWebCache configuration GUI** is now available directly from within the GeoServer web admin interface, including: the ability to define new grid sets, specify which layers to cache, seed or truncate the cache, and more. Big thanks to Gabriel and the GeoWebCache team for furthering improving integration between GeoWebCache in GeoServer.


**Wow!** And that isn't even everything, many [other](https://web.archive.org/web/20120921/https://jira.codehaus.org/sr/jira.issueviews:searchrequest-printable/temp/SearchRequest.html?jqlQuery=project+%3D+GEOS+and+status+in+%28Resolved%2C+Closed%29+and+fixVersion+in+%28%222.2%22%2C+%222.2-RC4%22%2C+%222.2-RC4%22%2C+%222.2-RC3%22%2C+%222.2-RC2%22%2C+%222.2-RC1%22%2C+%222.2-RC0%22%2C+%222.2-beta1%22%2C+%222.2-beta2%22%29&tempMax=1000) bug fixes and improvements have made it into the 2.2 series as well.

Everyone who uses GeoServer should have at least one or two items in the above list to be excited about. Download GeoServer 2.2, try it out, and provide feedback on the [GeoServer mailing list](https://web.archive.org/web/20120921/http://geoserver.org/display/GEOS/Mailing+Lists).  As with any new version, _be sure to backup your data directory before upgrading_.

**Thanks again for using GeoServer!**

**Download GeoServer 2.2**

----

## GeoServer 2.2

Released on Sept 21, 2012

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/geoserver-2.2-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/geoserver-2.2-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/geoserver-2.2.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/geoserver-2.2.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/geoserver-2.2-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/geoserver-2.2-htmldoc.zip/download)
- [PDF Documentation](http://downloads.sourceforge.net/geoserver/geoserver-2.2-pdfdoc.zip)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/geoserver-2.2-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-ogr-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2/extensions/geoserver-2.2-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 18767

## Release notes

Bug:

* [GEOS-5298](https://osgeo-org.atlassian.net/browse/GEOS-5298) WPS Execute fails with layer name clash
* [GEOS-5301](https://osgeo-org.atlassian.net/browse/GEOS-5301) CatalogBuilder.setupMetadata doesn't handle FeatureSource.getInfo() throwing exception
* [GEOS-5306](https://osgeo-org.atlassian.net/browse/GEOS-5306) GWC TransactionListener doesn't clears cache on Transaction
* [GEOS-5309](https://osgeo-org.atlassian.net/browse/GEOS-5309) Authentication Filters may create an HTTP session on authentication failure
* [GEOS-5310](https://osgeo-org.atlassian.net/browse/GEOS-5310) WPS:Reproject process fails to perform reprojections with datum change if bursa-wolf params are not available
* [GEOS-5616](https://osgeo-org.atlassian.net/browse/GEOS-5616) Missing bbox in JSON response
* [GEOS-6677](https://osgeo-org.atlassian.net/browse/GEOS-6677) Excel exports using querystring parameter PropertyName fails
