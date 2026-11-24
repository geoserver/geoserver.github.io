---
author: geoserver
comments: true
date: 2012-04-06 16:47:08+00:00
layout: post
link: http://blog.geoserver.org/2012/04/06/geoserver-2-2-beta/
slug: geoserver-2-2-beta
title: GeoServer 2.2-beta Released
wordpress_id: 1029
categories:
- Announcements
---

We're happy to announce to the beta release of GeoServer 2.2-beta and encourage you to download it, try out the great new features, and let us know if there are any bugs. Since this is the first beta release, we recommend against deploying it in a production environment without first undertaking extensive testing. That said, we’re hoping to move to release candidates soon, so any and all testing will help this process move along faster.

The release of a new major version update is a big deal (the [last one]({% post_url 2011-05-12-geoserver-2-1 %}) was 11 months ago) and, while you may have heard about some of the new features on the developer list, here they are all in one place:

**Referencing**



	
  * **NTv2 and NADCon Support** allows for datum transformations with cm level precision (instead of the usual 4m, when all goes well). Both will activate only if the grid files are present in the data dir, so by default the mere presence of the method is harmless, but generally speaking this is very good news for whoever needs to increase reprojection accuracy. Thanks to Andrea Aime and Oscar Fonts.**
**

	
  * A new **[reprojection console](http://osgeo-org.1560.n6.nabble.com/Little-reprojection-console-tt4631340.html) **allows users to make sure the transformations are actually using the grids by picking two coordinate systems and transforming a single point back and forth. Thanks Andrea.

	
  * Better support for un-referenced data with the new **[EPSG:40400](http://docs.geotools.org/latest/userguide/library/referencing/crs.html)** code that identifies a coordinate system made up of a generic 2D Cartesian plane.


**Data access**



	
  * **[Database-level security](http://geo-solutions.blogspot.com/2012/01/developers-corner-introducing-database.html) **implements the ability to use DBMS session startup and teardown scripts to alter user access the database during a specific request while falling back on connection pooling when the request is complete. Thanks to [Astrium GEO-Information Services](http://www.astrium-geo.com/) for sponsoring GeoSolutions to make this improvement.

	
  * **[Sorting and paging](http://geo-solutions.blogspot.com/2011/12/wfs-for-masses-adding-support-for.html)** is now available in all WFS versions (in 1.0 and 1.1 as a vendor param) via the sortBy and startIndex/maxFeature parameters. Thanks to Justin Deoliveira and Andrea.

	
  * A new experimental **OGR data store** provides access to  a rich set of readable formats without needing special bridge libraries.

	
  * The **[image collection](http://docs.geotools.org/latest/userguide/library/coverage/image-collection.html)** coverage store allows users to serve un-referenced data through WMS using image/pixel space as the coordinate system. Thanks to [SFMTA](http://www.sfmta.com) for sponsoring OpenGeo to complete this work.


**Security**



	
  * A major retrofit of the GeoServer **[security subsystem](http://docs.geoserver.org/latest/en/user/security/index.html)** adding support for a number of new authentication mechanisms including **[LDAP](http://docs.geoserver.org/latest/en/user/security/tutorials/ldap/index.html)**, **[digest](http://docs.geoserver.org/latest/en/user/security/tutorials/digest/index.html)** and **[X.509](http://docs.geoserver.org/latest/en/user/security/tutorials/cert/index.html)** certificate authentication, and more. These improvements also includes the addition of **[user groups](http://docs.geoserver.org/latest/en/user/security/usergrouprole/usergroups.html)**. This is a continuation of work started by Christian Mueller as a Google Summer of Code project;  thanks to [NOAA](http://www.noaa.gov/) for sponsoring OpenGeo to help Christian and Justin bring it to completion.


**Web Feature Source (WFS)**



	
  * Support for **[WFS 2.0](https://web.archive.org/web/20120406/http://geoserver.org/display/GEOS/GSIP+61+-+WFS+2.0)** adds some interesting new capabilities to the WFS protocol such as paging, stored queries, and extended operators. Thanks to [IGN France](http://www.ign.fr/) for sponsoring OpenGeo to make this improvement.


**Web Map Service (WMS)**



	
  * Support for additional dimensions brings [**time and elevation**](http://geo-solutions.blogspot.com/2011/06/time-and-elevation-support-in-geoserver.html) support to both vector and raster data. And, with support for time, comes support for **[animation in WMS](http://docs.geoserver.org/stable/en/user/tutorials/animreflector.html)**. Thanks to Andrea on both counts.

	
  * **[Rendering transformations](https://web.archive.org/web/20120406/http://docs.codehaus.org/display/GEOTOOLS/Rendering+transformations) **provide a bridge between WPS and WMS and allow for very powerful visualization capabilities for processing through normal WMS. Thanks again, Andrea.


**Web Processing Service (WPS)**



	
  * New WPS features include support for asynchronous process execution and a variety of new processes.


**Virtual Services**



	
  * [Virtual services](http://docs.geoserver.org/latest/en/user/services/virtual-services.html) allow GeoServer to support the notion of multitenancy, enabling a single GeoServer instance to publish multiple service endpoints. Thanks to NOAA for sponsoring OpenGeo to complete this improvement and a special thanks to Micah Wengren of NOAA for his leadership on the project.

	
  * **[Workspace local settings](https://web.archive.org/web/20120406/http://geoserver.org/display/GEOS/GSIP+67+-+Workspace+Local+Settings)** allow for specifying service settings such as contact information,  proxy settings, and output format settings on a per workspace basis.

	
  * **[Styles and layer groups](https://web.archive.org/web/20120406/http://geoserver.org/display/GEOS/GSIP+73+-+Workspace+Local+Styles+and+Layer+Groups)** can also now be defined on a per workspace basis.


**GeoWebCache**



	
  * A **GeoWebCache configuration GUI** is now available directly from within the GeoServer web admin interface, including: the ability to define new grid sets, specify which layers to cache, seed or truncate the cache, and more. Big thanks to Gabriel and the GeoWebCache team for furthering improving integration between GeoWebCache in GeoServer.


**Wow! **And that isn't even everything, many [other](#release-notes) bug fixes and improvements have made it into the 2.2 series as well.

Everyone who uses GeoServer should have at least one or two items in the above list to be excited about. Download GeoServer 2.2-beta, try it out, and please provide feedback and report any issues on the [GeoServer mailing list](https://web.archive.org/web/20120406/http://geoserver.org/display/GEOS/Mailing+Lists).  As with any beta version, _be sure to backup your data directory before upgrading_.

**FOSS4G North America**

Be sure to catch Andrea and Justin's [State of GeoServer](http://foss4g-na.org/schedule/the-state-of-geoserver/) and [What's new in GeoServer 2.2](http://foss4g-na.org/schedule/whats-new-in-geoserver-2-0/) presentations at [FOSS4G North America](http://foss4g-na.org/) to learn more about the exciting new features in GeoServer 2.1 and GeoServer 2.2. The conference takes place in Washington DC from April 10 through April 12 and on-site registration is available on a first come first serve basis for $350.

**Thanks again for using GeoServer!**

**Download GeoServer 2.2-beta**

----

## GeoServer 2.2-beta1

Released on 04/05/2012

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/geoserver-2.2-beta1-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/geoserver-2.2-beta1-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/geoserver-2.2-beta1.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/geoserver-2.2-beta1.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/geoserver-2.2-beta1-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/geoserver-2.2-beta1-htmldoc.zip/download)
- [PDF Documentation](http://downloads.sourceforge.net/geoserver/geoserver-2.2-beta1-pdfdoc.zip)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/geoserver-2.2-beta1-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-ogr-plugin.zip/download)
- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta1/extensions/geoserver-2.2-beta1-wps-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 18401

## Release notes

New Feature:

* [GEOS-2312](https://osgeo-org.atlassian.net/browse/GEOS-2312) Extend map generation pluggability
* [GEOS-4511](https://osgeo-org.atlassian.net/browse/GEOS-4511) WFS 2.0
* [GEOS-4634](https://osgeo-org.atlassian.net/browse/GEOS-4634) WFS 2.0 - Joins
* [GEOS-4684](https://osgeo-org.atlassian.net/browse/GEOS-4684) WFS 2.0 - Extended Operators
* [GEOS-4687](https://osgeo-org.atlassian.net/browse/GEOS-4687) WFS 2.0 - SOAP
* [GEOS-4838](https://osgeo-org.atlassian.net/browse/GEOS-4838) Allow services to be configured on a workspace by workspace basis
* [GEOS-4924](https://osgeo-org.atlassian.net/browse/GEOS-4924) Workspace local settings
* [GEOS-4962](https://osgeo-org.atlassian.net/browse/GEOS-4962) Styles and Layer groups per workspace
* [GEOS-4963](https://osgeo-org.atlassian.net/browse/GEOS-4963) Finer grained admin security
* [GEOS-4977](https://osgeo-org.atlassian.net/browse/GEOS-4977) Make gwc tile requests engage in control-flow for all protocols (wms-c, tms, wmts)
* [GEOS-5010](https://osgeo-org.atlassian.net/browse/GEOS-5010) Make GWC requests go through the GeoServer Dispatcher so they can be throttled by the control-flow module
* [GEOS-5016](https://osgeo-org.atlassian.net/browse/GEOS-5016) Drop layer prefix names in layers within a local workspace

Improvement:

* [GEOS-230](https://osgeo-org.atlassian.net/browse/GEOS-230) Allow multiple 'profiles'
* [GEOS-3411](https://osgeo-org.atlassian.net/browse/GEOS-3411) Make sure reverse proxy filter uses  RequestUtil.buildURL properly
* [GEOS-4460](https://osgeo-org.atlassian.net/browse/GEOS-4460) Better GWC integation - mid term goals
* [GEOS-4461](https://osgeo-org.atlassian.net/browse/GEOS-4461) Enhance Excel WFS output plugin, including adding support for Excel 2007 workbooks
* [GEOS-4496](https://osgeo-org.atlassian.net/browse/GEOS-4496) Support app-schema in WFS GML 3.2 output
* [GEOS-4535](https://osgeo-org.atlassian.net/browse/GEOS-4535) Better namespace encoding for app-schema GML 3.2 WFS responses
* [GEOS-4548](https://osgeo-org.atlassian.net/browse/GEOS-4548) Migrating to Spring 3.0.5 and Spring Security 3.0.5
* [GEOS-4554](https://osgeo-org.atlassian.net/browse/GEOS-4554) Adding user groups to the security architecture
* [GEOS-4611](https://osgeo-org.atlassian.net/browse/GEOS-4611) Avoid unnecessary reloads caused by FileWatcher
* [GEOS-4631](https://osgeo-org.atlassian.net/browse/GEOS-4631) Switching to Java 6 for Version 2.2.x
* [GEOS-4632](https://osgeo-org.atlassian.net/browse/GEOS-4632) Add CQL_FILTER support to WCS as well
* [GEOS-4652](https://osgeo-org.atlassian.net/browse/GEOS-4652) Support building GeoServer with Maven 3
* [GEOS-4691](https://osgeo-org.atlassian.net/browse/GEOS-4691) Fire the POST_INSERT event after a transaction that contains inserts
* [GEOS-4706](https://osgeo-org.atlassian.net/browse/GEOS-4706) Cut over to GeoTools port of GSProcess implementations
* [GEOS-4730](https://osgeo-org.atlassian.net/browse/GEOS-4730) Use a soft cache in resource pool
* [GEOS-4750](https://osgeo-org.atlassian.net/browse/GEOS-4750) Improve raster concurrency
* [GEOS-4837](https://osgeo-org.atlassian.net/browse/GEOS-4837) geosearch : add i18n support for sitemap panel (welcome page)
* [GEOS-4903](https://osgeo-org.atlassian.net/browse/GEOS-4903) superfluous sorted collection used in WMS.getDimensionCollection
* [GEOS-4957](https://osgeo-org.atlassian.net/browse/GEOS-4957) add end date support for WMS time dimension
* [GEOS-4985](https://osgeo-org.atlassian.net/browse/GEOS-4985) Add getPrefixedName() to LayerGroupInfo
* [GEOS-4990](https://osgeo-org.atlassian.net/browse/GEOS-4990) Fix to Monitoring HTTP API documentation
* [GEOS-5009](https://osgeo-org.atlassian.net/browse/GEOS-5009) Provide a way for the dispatcher to call a service operation avoiding reflection, for cases where it impacts performance
* [GEOS-5029](https://osgeo-org.atlassian.net/browse/GEOS-5029) findbugs error removal for web demo module

Bug:

* [GEOS-1303](https://osgeo-org.atlassian.net/browse/GEOS-1303) Add a projection console for users to try point and envelope reprojection by hand
* [GEOS-2646](https://osgeo-org.atlassian.net/browse/GEOS-2646) ReverseProxyFilter does not take into account the possibility that geoserver will be the root applications
* [GEOS-3842](https://osgeo-org.atlassian.net/browse/GEOS-3842) Geoserver cannot read database fields with unicode datatypes (nchar, nvarchar)
* [GEOS-4390](https://osgeo-org.atlassian.net/browse/GEOS-4390) Release guide sample CQL filter does not work anymore
* [GEOS-4451](https://osgeo-org.atlassian.net/browse/GEOS-4451) Direct raster path error with colormapped imagery and transparent color
* [GEOS-4599](https://osgeo-org.atlassian.net/browse/GEOS-4599) Xalan removal caused build failure in webservice-test
* [GEOS-4610](https://osgeo-org.atlassian.net/browse/GEOS-4610) FileWatcher.java does not recognize restored files
* [GEOS-4612](https://osgeo-org.atlassian.net/browse/GEOS-4612) Build failure in community/dds in geoserver-trunk-nightly caused by WMS changes
* [GEOS-4619](https://osgeo-org.atlassian.net/browse/GEOS-4619) Build failure in web and wcs1_1 and release caused by stale gt-temporal and gt-db2 dependencies
* [GEOS-4621](https://osgeo-org.atlassian.net/browse/GEOS-4621) Build failure in wms_1_1_1 DimensionsRasterGetFeatureInfoTest
* [GEOS-4622](https://osgeo-org.atlassian.net/browse/GEOS-4622) Build failure in community/python breaks geoserver-trunk-nightly
* [GEOS-4644](https://osgeo-org.atlassian.net/browse/GEOS-4644) Build failure in wcs1_0 GetCoverageTest testElevation{First,Second}
* [GEOS-4657](https://osgeo-org.atlassian.net/browse/GEOS-4657) main's org.geoserver.catalog.impl.CatalogBuilderTest#testLargeNDMosaic breaking on Windows
* [GEOS-4666](https://osgeo-org.atlassian.net/browse/GEOS-4666) GridReaderLayer breaks reader caching on trunk
* [GEOS-4667](https://osgeo-org.atlassian.net/browse/GEOS-4667) OutputTransparentColor not honored anymore on trunk
* [GEOS-4689](https://osgeo-org.atlassian.net/browse/GEOS-4689) Stale WGS84 axis order in KMLUtils breaks Maven 3 build
* [GEOS-4704](https://osgeo-org.atlassian.net/browse/GEOS-4704) DescribeCoverage 1.1.1 response has "wcs:AnyValue" instead of "ows:AnyValue"
* [GEOS-4818](https://osgeo-org.atlassian.net/browse/GEOS-4818) Unexpected WFS 2.0 response to WFS 1.1 request in SampleDataAccessWfsTest
* [GEOS-4844](https://osgeo-org.atlassian.net/browse/GEOS-4844) JAI causes ArrayIndexOutOfBoundsException
* [GEOS-4864](https://osgeo-org.atlassian.net/browse/GEOS-4864) NPE in DimensionHelper when feature store is empty
* [GEOS-4897](https://osgeo-org.atlassian.net/browse/GEOS-4897) GeoServer won't animate a standard WMS request with multiple times/elevation and animated gif output
* [GEOS-4956](https://osgeo-org.atlassian.net/browse/GEOS-4956) WMS time extent does not properly encode dates with negative years
* [GEOS-4960](https://osgeo-org.atlassian.net/browse/GEOS-4960) SQL view params support broken on trunk for WFS service
* [GEOS-4984](https://osgeo-org.atlassian.net/browse/GEOS-4984) layer groups in different workspaces with same local name show up with identical names in global wms capabilities doc
* [GEOS-5007](https://osgeo-org.atlassian.net/browse/GEOS-5007) Every call to CatalogConfiguration.getTile(layerName) forces the tile config to be depersisted from the file system
* [GEOS-5014](https://osgeo-org.atlassian.net/browse/GEOS-5014) PropertyIsGreatherThan bad typo in documents

Task:

* [GEOS-4473](https://osgeo-org.atlassian.net/browse/GEOS-4473) Update GeoServer's GDAL doc
* [GEOS-4474](https://osgeo-org.atlassian.net/browse/GEOS-4474) Make GDAL dependencies a standard Extension (make sure GDAL won't go in the standard Geoserver WAR as default)
* [GEOS-4512](https://osgeo-org.atlassian.net/browse/GEOS-4512) WFS 2.0 - Basic WFS
* [GEOS-4513](https://osgeo-org.atlassian.net/browse/GEOS-4513) WFS 2.0 - Transaction and Locking
* [GEOS-4514](https://osgeo-org.atlassian.net/browse/GEOS-4514) WFS 2.0 - Stored Queries
* [GEOS-4515](https://osgeo-org.atlassian.net/browse/GEOS-4515) WFS 2.0 - Filter 2.0
* [GEOS-4682](https://osgeo-org.atlassian.net/browse/GEOS-4682) Upgrade WPS to JAITools 1.2.0
* [GEOS-4938](https://osgeo-org.atlassian.net/browse/GEOS-4938) Add GUAVA dependency to root pom on 2.2.x
* [GEOS-4987](https://osgeo-org.atlassian.net/browse/GEOS-4987) Make integrated GWC support LayerGroups local to a workspace - reconciliate with GSIP 73
