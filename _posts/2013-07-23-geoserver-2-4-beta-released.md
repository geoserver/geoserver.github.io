---
author: geoserver
comments: true
date: 2013-07-23 01:23:59+00:00
layout: post
link: http://blog.geoserver.org/2013/07/22/geoserver-2-4-beta-released/
slug: geoserver-2-4-beta-released
title: GeoServer 2.4-beta Released
wordpress_id: 1471
categories:
- Announcements
---

GeoServer team is pleased to announce the release of GeoServer 2.4-beta.



	
  * The headline feature is a new implementation of the KML module.  This implementation introduces a new WFS KML output format leveraging the extended data with schema KML construct. Faster KML generation (similar speeds to GML2 output) and schema compliant KML output.
It is great to have a clean implementation to start any future enhancements against, however we do encourage all organisations that depend on GeoServer for KML output to take part in testing this beta.
Thanks to the NSW Geological Survey for sponsoring this work.

	
  * A lot of under-the-hood changes have been taking place for raster support. Many of the improvements will be realised in the community modules for the NetCDF and Image Mosaic formats. One visible change of all this hard work is the configuration of band information.

	
  * Application Schema users should note that joining behaviour is now on by default.

	
  * New community module for libjpeg-turbo

	
  * New community module for WMS Earth Observation profile, this required some API changes to GeoServer core (see GSIP 92 below).

	
  * The much loved CSS module has been promoted to an extension. This is significant as it represents our first non-Java module obtaining extension status.
The CSS module is written in Scala in part to take advantage of the excellent functional programming facilities for for calculating derived styles.

	
  * WPS processes can now operate against secured data (see GSIP 96 below)

	
  * This release is made in conjunction with [GeoTools 10-beta](http://geotoolsnews.blogspot.com.au/2013/07/geotools-10-beta-released.html)

	
  * This release is made in conjunction with GeoWebCache 1.5.0 - thanks to Kevin for publishing on such short notice.


See the [GeoServer 2.4-beta release notes](#release-notes) for more details.


### About GeoServer 2.4


GeoServer 2.4 continues our 6-month release cycle (with this beta release marking feature-complete for FOSS4G).

Volunteer opportunities:



	
  * We strongly encourage all interested parties to take part in testing GeoServer 2.4-beta

	
  * We would like to thank Frank Gasdorf and related volunteers for the excellent work translating GeoServer into additional languages
(English, Dutch, German and Korean are at 100%). If you would like to take part, or just check how far translation is going, please visit [GeoServer Localization](https://www.transifex.com/projects/p/geoserver_stable/))


The following change control requests were completed during the development of GeoServer 2.4:

	
  * [Replace old KML module with new one ](https://web.archive.org/web/20130723/http://geoserver.org/display/GEOS/GSIP+98+-+replace+old+KML+module+with+new+one)(GSIP 98)

	
  * [Allow plugins to modify WMS MapContent before map rendering](https://web.archive.org/web/20130723/http://geoserver.org/display/GEOS/GSIP+92+-+Allow+plugins+to+modify+WMS+MapContent+before+map+rendering) (GSIP 92)

	
  * [Machinery to pass thread locals down in thread pools](https://web.archive.org/web/20130723/http://geoserver.org/display/GEOS/GSIP+96+-+Machinery+to+pass+thread+locals+down+in+thread+pools) (GSIP 96) - also available in 2.3.4

	
  * [Promote CSS Styling module from Community to Extension](https://web.archive.org/web/20130723/http://geoserver.org/display/GEOS/GSIP+97+-+Promote+CSS+Styling+module+from+Community+to+Extension) (GSIP 97) - also available in 2.3.2

	
  * [Graduate the INSPIRE module to extension status](https://web.archive.org/web/20130723/http://geoserver.org/display/GEOS/GSIP+94+-+Graduate+the+INSPIRE+module+to+extension+status) (GSIP 94) - also available in 2.3.2

	
  * [Promote XSLT community module to extension](https://web.archive.org/web/20130723/http://geoserver.org/display/GEOS/GSIP+93+promote+XSLT+community+module+to+extension) (GSIP 93) - also available in 2.3.1


Articles and blogs during GeoServer 2.4 development:

	
  * GeoServer in a clustered configuration ([Part 1](http://blog.opengeo.org/2013/04/18/geoserver-in-a-clustered-configuration-part-1/), [Part 2](http://blog.opengeo.org/2013/04/30/geoserver-in-a-clustered-configuration-part-2/))

	
  * [New GeoServer community on Google+]({% post_url 2013-05-13-new-geoserver-community-on-google %})

	
  * [How to publish GDAL/MrSID image formats on a production GeoServer](http://blog.opengeo.org/2013/03/13/how-to-publish-gdalmrsid-image-formats-on-a-production-geoserver-on-windows/)

	
  * GeoServer crunch time ([Part I](http://www.lisasoft.com/blog/geoserver-crunch-time), [Part II](http://www.lisasoft.com/blog/geoserver-crunch-time-ii) and [Part III](http://www.lisasoft.com/blog/geoserver-crunch-time-iii))

	
  * FOSS4G-NA slides ([GeoServer In Production](http://blog.opengeo.org/wp-content/uploads/2013/05/GeoServerProduction.pdf), [GeoServer CSS Module](http://blog.opengeo.org/wp-content/uploads/2013/05/foss4gna2013-geoserver-css.pdf), [Scripting GeoServer with GeoScript](http://blog.opengeo.org/wp-content/uploads/2013/05/Scripting-GeoServer-with-GeoScript.pdf), [The State of GeoServer 2013](http://blog.opengeo.org/wp-content/uploads/2013/05/State-of-GeoServer-2013.pdf))

	
  * INSPIRE Conference 2013 slides ([Analysing GeoServer compatibility with INSPIRE requirements](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime?from_search=2))

	
  * FOSSGIS 2013 slides ([Introduction to GeoServer](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime))

----

## GeoServer 2.4-beta

Released on July 23, 2013

#### Download format

- [Binary (OS independent)](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-beta/geoserver-2.4-beta-bin.zip)
- [Web Archive](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-beta/geoserver-2.4-beta-war.zip)
- [Windows Installer](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-beta/geoserver-2.4-beta.exe)
- [Mac OS X Installer](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-beta/geoserver-2.4-beta.dmg)
- [Source Code](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-beta/geoserver-2.4-beta-src.zip)

#### Documentation

- [HTML Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-beta/geoserver-2.4-beta-htmldoc.zip)
- [PDF Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-beta/geoserver-2.4-beta-pdfdoc.zip)
- [API Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-beta/geoserver-2.4-beta-javadoc.zip)
- [Release Notes](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-beta/geoserver-2.4-beta-release-notes.txt)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-app-schema-plugin.zip)
- [ArcSDE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-arcsde-plugin.zip)
- [DB2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-db2-plugin.zip)
- [H2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-h2-plugin.zip)
- [MySQL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-mysql-plugin.zip)
- [Oracle](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-oracle-plugin.zip)
- [Pregeneralized features](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-feature-pregeneralized-plugin.zip)
- [SQL Server](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-sqlserver-plugin.zip)
- [Teradata](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-teradata-plugin.zip)
- [VPF](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-vpf-plugin.zip)
- [INSPIRE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-inspire-plugin.zip)

**Coverage store**

- [GDAL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-gdal-plugin.zip)
- [Image Pyramid](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-pyramid-plugin.zip)
- [JPEG2000](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-jp2k-plugin.zip)
- [JDBC Image Mosaic](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-imagemosaic-jdbc-plugin.zip)

**Other**

- [Chart dynamic symbolizer](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-charts-plugin.zip)
- [Control flow](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-control-flow-plugin.zip)
- [Cross layer filtering](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-querylayer-plugin.zip)
- [CSS styling](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-css-plugin.zip)
- [Excel output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-excel-plugin.zip)
- [GeoSearch](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-geosearch-plugin.zip)
- [Image Map output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-imagemap-plugin.zip)
- [OGR output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-ogr-plugin.zip)
- [XSLT output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-xslt-plugin.zip)
- [WPS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-wps-plugin.zip)
- [CAS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-cas-plugin.zip)
- Monitor ([Core](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-monitor-plugin.zip), [Hibernate](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-beta/geoserver-2.4-beta-monitor-hibernate-plugin.zip))

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19083

## Release notes

New Feature:

* [GEOS-4978](https://osgeo-org.atlassian.net/browse/GEOS-4978) Make it possible to configure arbitrary parameter filters for embedded GWC tile layers
* [GEOS-5700](https://osgeo-org.atlassian.net/browse/GEOS-5700) libjpeg-turbo WMS Encoder as Community Module

Improvement:

* [GEOS-1849](https://osgeo-org.atlassian.net/browse/GEOS-1849) Remove old SPI for GetMap and GetLegendGraphics
* [GEOS-2004](https://osgeo-org.atlassian.net/browse/GEOS-2004) Refactor KMSCORE to a format_option
* [GEOS-2362](https://osgeo-org.atlassian.net/browse/GEOS-2362) Remove NURC namespace
* [GEOS-2527](https://osgeo-org.atlassian.net/browse/GEOS-2527) Port GEOS-2508 to trunk
* [GEOS-2530](https://osgeo-org.atlassian.net/browse/GEOS-2530) Port GEOS-2529 to trunk
* [GEOS-4313](https://osgeo-org.atlassian.net/browse/GEOS-4313) Provide some information about the raster in the layer page
* [GEOS-5611](https://osgeo-org.atlassian.net/browse/GEOS-5611) Avoid security migration whenever possible
* [GEOS-5620](https://osgeo-org.atlassian.net/browse/GEOS-5620) New community module: WMS-EO
* [GEOS-5657](https://osgeo-org.atlassian.net/browse/GEOS-5657) ScaleLineDecoration attributes for enable/disable: background, border; or transparent
* [GEOS-5660](https://osgeo-org.atlassian.net/browse/GEOS-5660) ScaleRatioDecoration attributes for enable/disable transparency
* [GEOS-5666](https://osgeo-org.atlassian.net/browse/GEOS-5666) Various fixes for trimming
* [GEOS-5678](https://osgeo-org.atlassian.net/browse/GEOS-5678) Improve logging in geoserver.security
* [GEOS-5682](https://osgeo-org.atlassian.net/browse/GEOS-5682) Fix WCS20 ScaleToExtent and ScaleToSize operations
* [GEOS-5693](https://osgeo-org.atlassian.net/browse/GEOS-5693) Make app-schema joining the default behaviour
* [GEOS-5753](https://osgeo-org.atlassian.net/browse/GEOS-5753) Add "Test connection" for JDBCAuthentication Provicer
* [GEOS-5759](https://osgeo-org.atlassian.net/browse/GEOS-5759) KML performance improvement when kmscore=0 (raster) or kmscore=100 (vector)
* [GEOS-5775](https://osgeo-org.atlassian.net/browse/GEOS-5775) WMS GetCapabilities file should be given a meaningful name
* [GEOS-5792](https://osgeo-org.atlassian.net/browse/GEOS-5792) Enhancement to sql views - basic SQL parameter escaping
* [GEOS-5801](https://osgeo-org.atlassian.net/browse/GEOS-5801) Add option for wicket file browser not to expose other locations on the file system
* [GEOS-5805](https://osgeo-org.atlassian.net/browse/GEOS-5805) Add new options to LDAP authentication provider
* [GEOS-5826](https://osgeo-org.atlassian.net/browse/GEOS-5826) Allow access to request parameters from HTML GetFeatureInfo content.ftl templates
* [GEOS-5849](https://osgeo-org.atlassian.net/browse/GEOS-5849) Support Internationalized Labels in GetLegendGraphic
* [GEOS-5853](https://osgeo-org.atlassian.net/browse/GEOS-5853) Allow creation of a image mosaic by uploading a zip file with the necessary data and config files
* [GEOS-5854](https://osgeo-org.atlassian.net/browse/GEOS-5854) Add file browser support for GDAL formats
* [GEOS-5865](https://osgeo-org.atlassian.net/browse/GEOS-5865) Make GeoServer leverage the GeoTools multicoverage raster API
* [GEOS-5866](https://osgeo-org.atlassian.net/browse/GEOS-5866) KML feature downloads may fail when GE asks for them looking at the entire world
* [GEOS-5877](https://osgeo-org.atlassian.net/browse/GEOS-5877) Replace old KML module with the new KML2 one
* [GEOS-5890](https://osgeo-org.atlassian.net/browse/GEOS-5890) Expose grid coverage band configuration in GUI

Bug:

* [GEOS-1414](https://osgeo-org.atlassian.net/browse/GEOS-1414) Geoserver can't find logging config when it's installed (or it's data dir is located in) a path with a space in it
* [GEOS-1999](https://osgeo-org.atlassian.net/browse/GEOS-1999) SLD's `<Size>` tag does not affect Placemark elements
* [GEOS-3329](https://osgeo-org.atlassian.net/browse/GEOS-3329) Exception to add this geotif
* [GEOS-3550](https://osgeo-org.atlassian.net/browse/GEOS-3550) Geoserver fails to create mrSID data on MassGIS data
* [GEOS-3730](https://osgeo-org.atlassian.net/browse/GEOS-3730) line widths in styles are converted to whole numbers using KML output
* [GEOS-3836](https://osgeo-org.atlassian.net/browse/GEOS-3836) KML output cannot deal with non integer stroke widths
* [GEOS-3838](https://osgeo-org.atlassian.net/browse/GEOS-3838) KMZ output always contains raster representations, even when they are not required
* [GEOS-3923](https://osgeo-org.atlassian.net/browse/GEOS-3923) Pyramide
* [GEOS-4077](https://osgeo-org.atlassian.net/browse/GEOS-4077) Error reading metadata on GeoTIFF store load
* [GEOS-4097](https://osgeo-org.atlassian.net/browse/GEOS-4097) Serving KML - Console log shows "ERROR [geotools.map] - Call MapContent dispose() to prevent memory leaks"
* [GEOS-4861](https://osgeo-org.atlassian.net/browse/GEOS-4861) Including Extendeddata in kml output. Appears to have been done in GEOS-1496 but doesn't appear to work.
* [GEOS-5215](https://osgeo-org.atlassian.net/browse/GEOS-5215) [GUI][users management] problem removing users due to ordered list
* [GEOS-5302](https://osgeo-org.atlassian.net/browse/GEOS-5302) Misplaced Placemark Tag in KML output
* [GEOS-5543](https://osgeo-org.atlassian.net/browse/GEOS-5543) Creative Commons by Attribution
* [GEOS-5623](https://osgeo-org.atlassian.net/browse/GEOS-5623) GSIP 92 - Allow plugins to modify WMS MapContent before map rendering
* [GEOS-5624](https://osgeo-org.atlassian.net/browse/GEOS-5624) gs:Aggregate fails to encode output as WPS response document
* [GEOS-5628](https://osgeo-org.atlassian.net/browse/GEOS-5628) CatalogInfo objects will be cloned and rendered often useless when working against the GUI with multiple tabs open
* [GEOS-5629](https://osgeo-org.atlassian.net/browse/GEOS-5629) Monitoring and Excel modules use conflicting versions of Apache POI
* [GEOS-5630](https://osgeo-org.atlassian.net/browse/GEOS-5630) Fix Management of multivalued custom dimensions
* [GEOS-5631](https://osgeo-org.atlassian.net/browse/GEOS-5631) Build failure in wms GetFeatureInfoIntegrationTest caused by custom template leak
* [GEOS-5641](https://osgeo-org.atlassian.net/browse/GEOS-5641) german translation wrong encoded?
* [GEOS-5646](https://osgeo-org.atlassian.net/browse/GEOS-5646) Monitoring extension graduation makes chart plugin assembly pick the wrong version of jfreechart
* [GEOS-5650](https://osgeo-org.atlassian.net/browse/GEOS-5650) Build failure in wps-core SnapTest caused by leaking *ProcessFilterTest fixtures
* [GEOS-5664](https://osgeo-org.atlassian.net/browse/GEOS-5664) Improve Coverage of KVP and XML Tests for WCS 2.0
* [GEOS-5698](https://osgeo-org.atlassian.net/browse/GEOS-5698) Numerous issues with the Security "roles" web-interface
* [GEOS-5701](https://osgeo-org.atlassian.net/browse/GEOS-5701) Add support for raster with time validity interval to GeoServer
* [GEOS-5710](https://osgeo-org.atlassian.net/browse/GEOS-5710) GetLegendGraphic fails with a layergroup containing a coverage invisble at current scale
* [GEOS-5711](https://osgeo-org.atlassian.net/browse/GEOS-5711) org.geoserver.security.decorators.DecoratingWMSLayerInfo prefixName method calls itself indefinitely
* [GEOS-5715](https://osgeo-org.atlassian.net/browse/GEOS-5715) Upgrade JUnit to version 4.11, adopt a predictable test execution order
* [GEOS-5716](https://osgeo-org.atlassian.net/browse/GEOS-5716) Reduce repeated setup need in securty tests
* [GEOS-5723](https://osgeo-org.atlassian.net/browse/GEOS-5723) workspace filter wfs getfeature request can't find a non namespace prefixed typeName
* [GEOS-5724](https://osgeo-org.atlassian.net/browse/GEOS-5724) Document image mosaic support for time, elevation, property extractors and index stored in external databases
* [GEOS-5725](https://osgeo-org.atlassian.net/browse/GEOS-5725) Monitor plugin causes request failure when versions mismatch
* [GEOS-5732](https://osgeo-org.atlassian.net/browse/GEOS-5732) monitor chokes on wfs inserts when bounding box logging enabled
* [GEOS-5742](https://osgeo-org.atlassian.net/browse/GEOS-5742) Py scripting extension wps hook has upstream incompatibilities
* [GEOS-5743](https://osgeo-org.atlassian.net/browse/GEOS-5743) Build failure in gwc caused by upstream ParameterFilter changes
* [GEOS-5751](https://osgeo-org.atlassian.net/browse/GEOS-5751) JDBCAuthenticationProvider does not work if a user is not registered as GeoServer user
* [GEOS-5760](https://osgeo-org.atlassian.net/browse/GEOS-5760) Documentation not referrencing Xms correctly.
* [GEOS-5765](https://osgeo-org.atlassian.net/browse/GEOS-5765) Bug in Alpha Aware Quantizer
* [GEOS-5769](https://osgeo-org.atlassian.net/browse/GEOS-5769) JDK 7 gives a preference to the pure java PNG writer even if the native one is available
* [GEOS-5774](https://osgeo-org.atlassian.net/browse/GEOS-5774) Time parsing is not thread safe
* [GEOS-5783](https://osgeo-org.atlassian.net/browse/GEOS-5783) SSL redirect to wrong path
* [GEOS-5785](https://osgeo-org.atlassian.net/browse/GEOS-5785) Authentication GUI does not persist the changes
* [GEOS-5803](https://osgeo-org.atlassian.net/browse/GEOS-5803) "mode" not "storage" used in default monitor.properties
* [GEOS-5810](https://osgeo-org.atlassian.net/browse/GEOS-5810) Packaging error for the CAS extension
* [GEOS-5811](https://osgeo-org.atlassian.net/browse/GEOS-5811) Changing the SSL Port has no effect for filter chains already restricted to SSL requests
* [GEOS-5816](https://osgeo-org.atlassian.net/browse/GEOS-5816) Error with WCS 1.0 and GetCoverage with bilinear interpolation
* [GEOS-5820](https://osgeo-org.atlassian.net/browse/GEOS-5820) Disabling security does not work as expected
* [GEOS-5824](https://osgeo-org.atlassian.net/browse/GEOS-5824) http://..../geoserver matches wrong security filter chain
* [GEOS-5847](https://osgeo-org.atlassian.net/browse/GEOS-5847) inner LayerGroup not loaded from Catalog in nested layer groups
* [GEOS-5848](https://osgeo-org.atlassian.net/browse/GEOS-5848) Printing Module basemap no longer available
* [GEOS-5851](https://osgeo-org.atlassian.net/browse/GEOS-5851) Getting a feature source from ResourcePool always gets into a synchronized code section
* [GEOS-5852](https://osgeo-org.atlassian.net/browse/GEOS-5852) default filter chain does not create HTTP session even with session creation enabled
* [GEOS-5861](https://osgeo-org.atlassian.net/browse/GEOS-5861) KML ground overlays are not displayed sometimes when viewing the entire globe
* [GEOS-5875](https://osgeo-org.atlassian.net/browse/GEOS-5875) Expose and allow manipulation of structured coverage grid readers via rest api
* [GEOS-5884](https://osgeo-org.atlassian.net/browse/GEOS-5884) app-schema test failures due to timezone handling
* [GEOS-5891](https://osgeo-org.atlassian.net/browse/GEOS-5891) REST config upload fail in path with spaces
* [GEOS-5895](https://osgeo-org.atlassian.net/browse/GEOS-5895) When a format fails to create a reader, ResourcePool comes out with a mysterious exception about a null value

Task:

* [GEOS-3549](https://osgeo-org.atlassian.net/browse/GEOS-3549) wcs 1.0 module with multi dimensional coverage support
* [GEOS-5496](https://osgeo-org.atlassian.net/browse/GEOS-5496) Add gt-complex to app-schema plugin release descriptor
* [GEOS-5702](https://osgeo-org.atlassian.net/browse/GEOS-5702) Add libjpeg-turbo community module to nightly deploy
