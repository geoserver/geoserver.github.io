---
author: geoserver
comments: true
date: 2013-04-23 17:15:09+00:00
layout: post
link: http://blog.geoserver.org/2013/04/23/geoserver-2-3-1-released/
slug: geoserver-2-3-1-released
title: GeoServer 2.3.1 released
wordpress_id: 1387
---

The GeoServer team is happy to announce the release of GeoServer 2.3.1, now available for download.

This is the first bug-fix release of the 2.3.x stable series, and packs 34 changes between bug fixes and improvements in different departments. Here is an highlight:



	
  * The [XSLT output format generator](http://docs.geoserver.org/stable/en/user/extensions/xslt/index.html) module graduated from community to official extension (work performed GeoSolutions Andrea Aime with sponsorship from the City of Wien)

	
  * A couple of changes in the SQL Server data increase performance, provided you enable the relevant flags. One is the ability to transfer geometries in SQL Server native format, as opposed to using WKB, which avoids the slow WKB generation routines included in SQL Server, the other allows to disable native paging, which can sometimes lead the SQL Server query planner to create bad data access plans ([GEOS-5750](https://osgeo-org.atlassian.net/browse/GEOS-5750) and [GEOS-5314](https://osgeo-org.atlassian.net/browse/GEOS-5314)). The native geometry serialization was sponsored by Norwegian Directorate for Nature Management and performed by Bouvet, thanks to Stewart Loving-Gibbard for the paging patch.

	
  * A new flag has been added to prevent the resolution of XML external entities (normally enabled by default in XML parsers), which can be used to prevent some kinds of XML attacks ([GEOS-5273](https://osgeo-org.atlassian.net/browse/GEOS-5273) and [GEOS-5314](https://osgeo-org.atlassian.net/browse/GEOS-5314)). The work was performed by GeoSolution under sponsorship from the City of Wien.

	
  * Some SLD related fixes ([GEOS-4214](https://osgeo-org.atlassian.net/browse/GEOS-4214), [GEOS-5767](https://osgeo-org.atlassian.net/browse/GEOS-5767)) (thanks to GeoSolutions's Andrea and Carlo for those)

	
  * A bunch of improvements in the monitoring extension ([GEOS-5725](https://osgeo-org.atlassian.net/browse/GEOS-5725), [GEOS-5732](https://osgeo-org.atlassian.net/browse/GEOS-5732), [GEOS-5758](https://osgeo-org.atlassian.net/browse/GEOS-5758) and [GEOS-5766](https://osgeo-org.atlassian.net/browse/GEOS-5766)) (thanks to OpenGeo's Justin Deoliveria and Ian Schneider for those, plus one from Andrea)

	
  * Fixed an issue that prevented GeoServer from serving back GetMap requests under Windows when using the JRE ([GEOS-5768](https://osgeo-org.atlassian.net/browse/GEOS-5768)) (thanks goes to GeoSolutions' Simone for this one)

	
  * GWC will now respect the layer HTTP caching settings, and a memory leak has been fixed in respect to the WFS-T integration ([GEOS-5686](https://osgeo-org.atlassian.net/browse/GEOS-5686), [GEOS-5659](https://osgeo-org.atlassian.net/browse/GEOS-5659))  (thanks' to OpenGeo's Ian Schneider for these)

	
  * The German translation maintainers fixed an encoding problem which resulted in weird chars appearing in the GeoServer UI ([GEOS-5641](https://osgeo-org.atlassian.net/browse/GEOS-5641)) (thanks goes to Frank Gasdorf and Oskar Fonts for their continuous work on UI internationalization)

	
  * GeoServer UI is completely available in _**Dutch, German **_and _**Korean **_(thanks goes to Wouter van Nifterick, Frank Gasdorf, Stefan Engelhardt, Minpa Lee and others), feel free to review and contribute at [Transifex.com](https://www.transifex.com/projects/p/geoserver_stable)

	
  * Finally, a few fixes and improvements in the security subsystem ([GEOS-5698](https://osgeo-org.atlassian.net/browse/GEOS-5698), [GEOS-5751](https://osgeo-org.atlassian.net/browse/GEOS-5751), [GEOS-5753](https://osgeo-org.atlassian.net/browse/GEOS-5753), [GEOS-5783](https://osgeo-org.atlassian.net/browse/GEOS-5783)) (thanks to Christian Mueller for his continuous work on the security subsystem)


And there is more, you can find everything in the GeoServer [release notes.](#release-notes) Also, looking at the corresponding [GeoTools 9.1 release notes](#release-notes) we can find some extra goodies:



	
  * Improved support for sparse shapefiles ([GEOT-2791](https://osgeo-org.atlassian.net/browse/GEOT-2791)) (thanks to Dieter DePaepe)

	
  * Added support for UUID data type in PostGis data stores ([GEOT-4414](https://osgeo-org.atlassian.net/browse/GEOT-4414)) (thanks to Shane StClair)


Download GeoServer 2.3.1, try it out, and provide feedback on the [GeoServer mailing list](https://web.archive.org/web/20130423/http://geoserver.org/display/GEOS/Mailing+Lists).

Thanks again for using GeoServer!

----

## GeoServer 2.3.1

Released on April 22 2013

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/geoserver-2.3.1-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/geoserver-2.3.1-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/geoserver-2.3.1.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/geoserver-2.3.1.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/geoserver-2.3.1-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/geoserver-2.3.1-htmldoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/geoserver-2.3.1-javadoc.zip/download)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-sqlserver-plugin.zip/download)
- [Teradata](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-teradata-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-jp2k-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-control-flow-plugin.zip/download)
- [Cross layer filtering](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-querylayer-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-ogr-plugin.zip/download)
- [XSLT output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-xslt-plugin.zip/download)

- [WPS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-wps-plugin.zip/download)
- [CAS](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-cas-plugin.zip/download)
- Monitor ([Core](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-monitor-plugin.zip/download), [Hibernate](https://sourceforge.net/projects/geoserver/files/GeoServer/2.3.1/extensions/geoserver-2.3.1-monitor-hibernate-plugin.zip/download))

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19153

## Release notes

Improvement:

* [GEOS-5686](https://osgeo-org.atlassian.net/browse/GEOS-5686) allow integrated gwc to use expires setting in layer
* [GEOS-5752](https://osgeo-org.atlassian.net/browse/GEOS-5752) Graduate the XSLT module to extension status
* [GEOS-5753](https://osgeo-org.atlassian.net/browse/GEOS-5753) Add "Test connection" for JDBCAuthentication Provicer
* [GEOS-5775](https://osgeo-org.atlassian.net/browse/GEOS-5775) WMS GetCapabilities file should be given a meaningful name

Bug:

* [GEOS-4214](https://osgeo-org.atlassian.net/browse/GEOS-4214) Parameter substitution seems to not work for CssParameter stroke in WMS
* [GEOS-5215](https://osgeo-org.atlassian.net/browse/GEOS-5215) [GUI][users management] problem removing users due to ordered list
* [GEOS-5273](https://osgeo-org.atlassian.net/browse/GEOS-5273) external SLD reference in getMap allows access to host filesystem because of external entities
* [GEOS-5314](https://osgeo-org.atlassian.net/browse/GEOS-5314) MSSQL query planner fails to optimize access to queries with both native paging and spatial indexes, workaround needed
* [GEOS-5641](https://osgeo-org.atlassian.net/browse/GEOS-5641) german translation wrong encoded?
* [GEOS-5659](https://osgeo-org.atlassian.net/browse/GEOS-5659) Every WFS update leaks memory in the GWC WFS listener
* [GEOS-5698](https://osgeo-org.atlassian.net/browse/GEOS-5698) Numerous issues with the Security "roles" web-interface
* [GEOS-5707](https://osgeo-org.atlassian.net/browse/GEOS-5707) External entity reference in WFS POST request allows access to host filesystem
* [GEOS-5710](https://osgeo-org.atlassian.net/browse/GEOS-5710) GetLegendGraphic fails with a layergroup containing a coverage invisble at current scale
* [GEOS-5716](https://osgeo-org.atlassian.net/browse/GEOS-5716) Reduce repeated setup need in securty tests
* [GEOS-5725](https://osgeo-org.atlassian.net/browse/GEOS-5725) Monitor plugin causes request failure when versions mismatch
* [GEOS-5732](https://osgeo-org.atlassian.net/browse/GEOS-5732) monitor chokes on wfs inserts when bounding box logging enabled
* [GEOS-5733](https://osgeo-org.atlassian.net/browse/GEOS-5733) WCS 1.1 multipart output has newlines in HTTP response heades, that is invalid
* [GEOS-5734](https://osgeo-org.atlassian.net/browse/GEOS-5734) WCS 1.1 GetCoverage response fails in multipart mode
* [GEOS-5740](https://osgeo-org.atlassian.net/browse/GEOS-5740) Failure to compute lat/lon bounds when native srs is not found and declared srs is not EPSG:4326
* [GEOS-5742](https://osgeo-org.atlassian.net/browse/GEOS-5742) Py scripting extension wps hook has upstream incompatibilities
* [GEOS-5749](https://osgeo-org.atlassian.net/browse/GEOS-5749) Failed to find response for output format jsonp
* [GEOS-5750](https://osgeo-org.atlassian.net/browse/GEOS-5750) Add option to use SQL Server native geometry serialization
* [GEOS-5751](https://osgeo-org.atlassian.net/browse/GEOS-5751) JDBCAuthenticationProvider does not work if a user is not registered as GeoServer user
* [GEOS-5757](https://osgeo-org.atlassian.net/browse/GEOS-5757) Build fails on Windows due to unreleased input streams in security subsystem
* [GEOS-5758](https://osgeo-org.atlassian.net/browse/GEOS-5758) Monitoring module build fails on windows because the H2 data source is not disposed of
* [GEOS-5765](https://osgeo-org.atlassian.net/browse/GEOS-5765) Bug in Alpha Aware Quantizer
* [GEOS-5766](https://osgeo-org.atlassian.net/browse/GEOS-5766) MonitorInputStream ignores maxSize
* [GEOS-5767](https://osgeo-org.atlassian.net/browse/GEOS-5767) Expressing graphic-margin as an array results in exceptions during rendering
* [GEOS-5768](https://osgeo-org.atlassian.net/browse/GEOS-5768) WMS GetMap fails on recent JRE installations on Windows
* [GEOS-5770](https://osgeo-org.atlassian.net/browse/GEOS-5770) JSON-GeometryCollection-Bug
* [GEOS-5774](https://osgeo-org.atlassian.net/browse/GEOS-5774) Time parsing is not thread safe
* [GEOS-5781](https://osgeo-org.atlassian.net/browse/GEOS-5781) Grid coverage readers might alter the hints provided during construction, resource pool should do a defensive copy of them
* [GEOS-5782](https://osgeo-org.atlassian.net/browse/GEOS-5782) Trying to upload a non existing file to rest config in "external" mode results in NPE
* [GEOS-5783](https://osgeo-org.atlassian.net/browse/GEOS-5783) SSL redirect to wrong path

Task:

* [GEOS-5735](https://osgeo-org.atlassian.net/browse/GEOS-5735) Create Download link for 2.3.x nightly build
