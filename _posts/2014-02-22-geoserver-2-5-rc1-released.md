---
author: geoserver
comments: true
date: 2014-02-22 22:07:27+00:00
layout: post
link: http://blog.geoserver.org/2014/02/22/geoserver-2-5-rc1-released/
slug: geoserver-2-5-rc1-released
title: GeoServer 2.5-RC1 Released
wordpress_id: 1796
categories:
- Announcements
---

The GeoServer team is happy to announce the release of GeoServer 2.5-RC1. Download bundles are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5-RC1/geoserver-2.5-RC1-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5-RC1/geoserver-2.5-RC1-war.zip), [dmg](https://sourceforge.net/projects/geoserver/files/GeoServer/2.5-RC1/geoserver-2.5-RC1.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.5-RC1/geoserver-2.5-RC1.exe/download))  along with documentation and extensions.

GeoServer 2.5 is shaping up to be a great milestone and we would like to thank all those who have downloaded 2.5-beta and submitted feedback and pull requests.



	
  * A couple map rendering issues have been fixed with better white space handling for CSS labels and crisp SVG symbols rendering.

	
  * Konstantin Surzhin has provided many small user interface fixes

	
  * Mauro Bartolomeoli has been untangling a conflict between the css extension and the printing modules.

	
  * Thanks to Andrea for his hard work, and constant review of pull requests.

	
  * Thanks to Jody Garnett and Boundless facilitating this weeks release.

	
  * Check the [release notes](#release-notes) for more details

	
  * This release is made in conjunction with [GeoTools 11-RC1](http://geotoolsnews.blogspot.com.au/2014/02/geotools-11-rc1-released.html).


With all this help GeoServer 2.5 is on track for release in March. We would like to encourage you to download the release candidate and test with your data. This will both help you avoid any surprises, and assist the team in bringing you the best possible GeoServer.


# About GeoServer 2.5


Articles and resources for GeoServer 2.5 series:



	
  * GeoServer 2.5-beta announcement reviews [key features of this release]({% post_url 2014-01-21-geoserver-2-5-beta-released %}):

	
    * WCS 2.0 and WCS 2.0 Earth Observation have been added (thanks to DLR and Eumesat for funding this)

	
    * The addition of a batch importer to making setting up GeoServer easier (thanks to [MapStory](https://web.archive.org/web/20140222/http://mapstory.org/)).

	
    * High performance PNG encoder based on [PNGJ library](https://code.google.com/p/pngj/) (Andrea Aime). Improved JPEG performance using [libjpegturbo](http://libjpeg-turbo.virtualgl.org/) available as an optional extension (Simone Giannecchini and Daniele Romagnoli)

	
    * Use of ST_Simplify to improve PostGIS rendering performance (a collaboration with Andrea and Jonathan Moules).

	
    * New implementation of GetFeatureInfo that takes into account symbol shapes, offsets, and dynamic line widths into account (thanks to Eskilstuna municipality for funding this).




	
  * [Using GeoServer at IGN to create new digital maps]({% post_url 2014-01-07-using-geoserver-at-ign-the-french-national-mapping-agency-to-create-new-digital-maps %}) is an impressive look at advanced styling deployed by the french mapping agency

	
  * [Labelling a MultiPoint geometry with WPS](https://web.archive.org/web/20140222/http://boundlessgeo.com/2014/02/labelling-a-multipoint-geometry-with-wps/) (Boundless) is a good example of integrating WPS and Styling

	
  * [Achieving extreme GeoServer Scalability with new Marlin vector rasterizer](http://geo-solutions.blogspot.it/2014/02/geoserver-improved-scalability.html) (GeoSolutions) shows an exciting JRE extension that can be used for improved performance. If you are using GeoServer with a large number of CPU cores you owe yourself an hour to try this out.

	
  * [DXF output format promoted to official extension for GeoServer](http://geo-solutions.blogspot.it/2014/01/geoserver-dxf.html) (GeoSolutions)

	
  * [Active Directory based security in GeoServer through LDAP](http://geo-solutions.blogspot.it/2014/01/geoserver-activedirectory.html) (GeoSolutions)

----

## GeoServer 2.5-RC1

Released on Feb 21 2014

#### Download format

- [Binary (OS independent)](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5-RC1/geoserver-2.5-RC1-bin.zip/download)
- [Web Archive](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5-RC1/geoserver-2.5-RC1-war.zip)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.5-RC1/geoserver-2.5-RC1.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.5-RC1/geoserver-2.5-RC1.dmg/download)
- [Source Code](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5-RC1/geoserver-2.5-RC1-src.zip)

#### Documentation

- [HTML Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5-RC1/geoserver-2.5-RC1-htmldoc.zip)
- [API Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5-RC1/geoserver-2.5-RC1-javadoc.zip)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-app-schema-plugin.zip)
- [ArcSDE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-arcsde-plugin.zip)
- [DB2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-db2-plugin.zip)
- [H2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-h2-plugin.zip)
- [MySQL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-mysql-plugin.zip)
- [Oracle](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-oracle-plugin.zip)
- [Pregeneralized features](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-feature-pregeneralized-plugin.zip)
- [SQL Server](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-sqlserver-plugin.zip)
- [Teradata](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-teradata-plugin.zip)
- [VPF](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-vpf-plugin.zip)
- [INSPIRE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-inspire-plugin.zip)

**Coverage store**

- [GDAL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-gdal-plugin.zip)
- [Image Pyramid](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-pyramid-plugin.zip)
- [JPEG2000](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-jp2k-plugin.zip)
- [JDBC Image Mosaic](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-imagemosaic-jdbc-plugin.zip)

**Other**

- [Chart dynamic symbolizer](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-charts-plugin.zip)
- [Control flow](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-control-flow-plugin.zip)
- [Cross layer filtering](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-querylayer-plugin.zip)
- [CSS styling](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-css-plugin.zip)
- [Excel output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-excel-plugin.zip)
- [GeoSearch](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-geosearch-plugin.zip)
- [Image Map output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-imagemap-plugin.zip)
- [OGR output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-ogr-plugin.zip)
- [XSLT output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-xslt-plugin.zip)
- [WPS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-wps-plugin.zip)
- [CAS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-cas-plugin.zip)
- Monitor ([Core](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-monitor-plugin.zip), [Hibernate](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-monitor-hibernate-plugin.zip))
- [CSW](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-csw-plugin.zip)
- Importer ([Core](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-importer-plugin.zip), [BerkeleyDB Backend](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-importer-bdb-plugin.zip))
- [WCS 2.0 EO](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-wcs2_0-eo-plugin.zip)
- [DXF output format for WFS/WPS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-dxf-plugin.zip)
- [WMS libJpegTurbo output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.5-RC1/geoserver-2.5-RC1-libjpeg-turbo-plugin.zip)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19927

## Release notes

Improvement:

* [GEOS-5028](https://osgeo-org.atlassian.net/browse/GEOS-5028) findbugs error removal for restconfig module
* [GEOS-6184](https://osgeo-org.atlassian.net/browse/GEOS-6184) DynamicColorMap rendering transformation
* [GEOS-6256](https://osgeo-org.atlassian.net/browse/GEOS-6256) add "purge" parameter to REST delete
* [GEOS-6328](https://osgeo-org.atlassian.net/browse/GEOS-6328) Use direct read when CoverageBuilder creates a sample 5x5 coverage
* [GEOS-6330](https://osgeo-org.atlassian.net/browse/GEOS-6330) REST HTML interface links to coverages contain coveragestores against instead of coverages
* [GEOS-6341](https://osgeo-org.atlassian.net/browse/GEOS-6341) Associate css style as default for a layer from the css demo page

Bug:

* [GEOS-5729](https://osgeo-org.atlassian.net/browse/GEOS-5729) Antialiasing can not be turned off for svg-symbols
* [GEOS-5777](https://osgeo-org.atlassian.net/browse/GEOS-5777) Cascading WMS fails if source image is an indexed one with nbits < 8
* [GEOS-5970](https://osgeo-org.atlassian.net/browse/GEOS-5970) POST-ing wps requests fails at the dispatcher level when using curl
* [GEOS-6046](https://osgeo-org.atlassian.net/browse/GEOS-6046) Geometry transformation validation fails in SE 1.1
* [GEOS-6052](https://osgeo-org.atlassian.net/browse/GEOS-6052) Geoserver does not start when a virtualtable misses the geometry section with oracle JNDI datastore
* [GEOS-6148](https://osgeo-org.atlassian.net/browse/GEOS-6148) GEoServer 2.4.1 saves new layers with broken coordinates if locale uses spaces for thousands separator
* [GEOS-6150](https://osgeo-org.atlassian.net/browse/GEOS-6150) Exception when rendering PostGIS layer with conditional CQL/SLD using decimal/float values for integer attribute
* [GEOS-6190](https://osgeo-org.atlassian.net/browse/GEOS-6190) WTMS has no style in GetCapabilities
* [GEOS-6210](https://osgeo-org.atlassian.net/browse/GEOS-6210) CSS Extension does not allow whitespace in compound labels
* [GEOS-6216](https://osgeo-org.atlassian.net/browse/GEOS-6216) app-schema WFS 2.0.0 lat-lon axis ordering wrong and inconsistent with core GeoServer WFS behaviour
* [GEOS-6299](https://osgeo-org.atlassian.net/browse/GEOS-6299) 1bit Raster Transparency with transparent color, rendering failure
* [GEOS-6304](https://osgeo-org.atlassian.net/browse/GEOS-6304) Remove stax-api-1.0.1.jar from excel extension
* [GEOS-6310](https://osgeo-org.atlassian.net/browse/GEOS-6310) GeoRSS output uses the wrong mime type
* [GEOS-6312](https://osgeo-org.atlassian.net/browse/GEOS-6312) OpenLayers output format is not listed in WMS 1.3 capabilities document
* [GEOS-6314](https://osgeo-org.atlassian.net/browse/GEOS-6314) Allow JSON id generation to be optional
* [GEOS-6317](https://osgeo-org.atlassian.net/browse/GEOS-6317) GetRecordById is not accepted in POST requests
* [GEOS-6321](https://osgeo-org.atlassian.net/browse/GEOS-6321) Make sure to use the proper coverageName when dealing with multiple coverages
* [GEOS-6322](https://osgeo-org.atlassian.net/browse/GEOS-6322) Automatically generate the PDF documentation during the release process
* [GEOS-6324](https://osgeo-org.atlassian.net/browse/GEOS-6324) Unable to configure WPS per workspace
* [GEOS-6331](https://osgeo-org.atlassian.net/browse/GEOS-6331) JDBCConfig only shows first page when paging a list of entries
* [GEOS-6336](https://osgeo-org.atlassian.net/browse/GEOS-6336) NetCDF output format: coordinates represent cell's center
* [GEOS-6338](https://osgeo-org.atlassian.net/browse/GEOS-6338) GetFeatureInfo does not handle symbols whose size is expressed via UOM
* [GEOS-6344](https://osgeo-org.atlassian.net/browse/GEOS-6344) PNGJWriter logs exceptions at warning level even if the client closed the connection
* [GEOS-6347](https://osgeo-org.atlassian.net/browse/GEOS-6347) csw release packages misses the web-csw jar
* [GEOS-6351](https://osgeo-org.atlassian.net/browse/GEOS-6351) Printing plugin and CSS plugin are incompatible

Task:

* [GEOS-6305](https://osgeo-org.atlassian.net/browse/GEOS-6305) Remove unnecessary jar from WPS module archive
