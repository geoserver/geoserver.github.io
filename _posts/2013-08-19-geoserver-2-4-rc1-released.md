---
author: geoserver
comments: true
date: 2013-08-19 17:37:26+00:00
layout: post
link: http://blog.geoserver.org/2013/08/19/geoserver-2-4-rc1-released/
slug: geoserver-2-4-rc1-released
title: GeoServer 2.4-RC1 released
wordpress_id: 1533
---

GeoServer team is pleased to announce the release of GeoServer 2.4-RC1. This release contains a set of bug fixes and minor improvements compared to 2.4-beta, including:



	
  * Some love to the layer group edit page, fixing style editing

	
  * Improvements in the CSS extension editor

	
  * A number of fixes in the CSW community module (scheduled to graduate to extension real soon now)

	
  * Making GML3 GetFeatureInfo output work against rasters too

	
  * A bunch of minor fixes to the new KML module


See the [GeoServer 2.4-RC1 release notes](#release-notes) for more details.

The next release candidate is scheduled in two weeks. If we don't hear about major bugs reported against 2.4-RC1, we'll release it as 2.4.0:  user community, your turn, **please test RC1 now and let us know if anything major does not work as you expected**. If you discover any issue, report it in our [bug tracker](https://web.archive.org/web/20130819/http://jira.codehaus.org) and if you still do not have a login, you can create one at [Codehaus](https://web.archive.org/web/20130819/http://xircles.codehaus.org) (valid for all Codehaus services, including the GeoServer bug tracker they are graciously hosting for us).


### About the GeoServer 2.4 series


GeoServer 2.4 continues our 6-month release cycle.

Volunteer opportunities:



	
  * We strongly encourage all interested parties to take part in testing GeoServer 2.4-RC1


The following change control requests were completed during the development of GeoServer 2.4:

	
  * [Replace old KML module with new one ](https://web.archive.org/web/20130819/http://geoserver.org/display/GEOS/GSIP+98+-+replace+old+KML+module+with+new+one)(GSIP 98)

	
  * [Allow plugins to modify WMS MapContent before map rendering](https://web.archive.org/web/20130819/http://geoserver.org/display/GEOS/GSIP+92+-+Allow+plugins+to+modify+WMS+MapContent+before+map+rendering) (GSIP 92)

	
  * [Machinery to pass thread locals down in thread pools](https://web.archive.org/web/20130819/http://geoserver.org/display/GEOS/GSIP+96+-+Machinery+to+pass+thread+locals+down+in+thread+pools) (GSIP 96, fixes WPS asych requests security issues) - also available in 2.3.4

	
  * [Promote CSS Styling module from Community to Extension](https://web.archive.org/web/20130819/http://geoserver.org/display/GEOS/GSIP+97+-+Promote+CSS+Styling+module+from+Community+to+Extension) (GSIP 97) - also available in 2.3.2

	
  * [Graduate the INSPIRE module to extension status](https://web.archive.org/web/20130819/http://geoserver.org/display/GEOS/GSIP+94+-+Graduate+the+INSPIRE+module+to+extension+status) (GSIP 94) - also available in 2.3.2

	
  * [Promote XSLT community module to extension](https://web.archive.org/web/20130819/http://geoserver.org/display/GEOS/GSIP+93+promote+XSLT+community+module+to+extension) (GSIP 93) - also available in 2.3.1

	
  * The shapefile datastore was completely rewritten (mostly as a code cleanup)


Articles and blogs during GeoServer 2.4 development:

	
  * GeoServer in a clustered configuration ([Part 1](https://web.archive.org/web/20130819/http://blog.opengeo.org/2013/04/18/geoserver-in-a-clustered-configuration-part-1/), [Part 2](https://web.archive.org/web/20130819/http://blog.opengeo.org/2013/04/30/geoserver-in-a-clustered-configuration-part-2/))

	
  * [New GeoServer community on Google+]({% post_url 2013-05-13-new-geoserver-community-on-google %})

	
  * [How to publish GDAL/MrSID image formats on a production GeoServer](https://web.archive.org/web/20130819/http://blog.opengeo.org/2013/03/13/how-to-publish-gdalmrsid-image-formats-on-a-production-geoserver-on-windows/)

	
  * GeoServer crunch time ([Part I](https://web.archive.org/web/20130819/http://www.lisasoft.com/blog/geoserver-crunch-time), [Part II](https://web.archive.org/web/20130819/http://www.lisasoft.com/blog/geoserver-crunch-time-ii) and [Part III](https://web.archive.org/web/20130819/http://www.lisasoft.com/blog/geoserver-crunch-time-iii))

	
  * FOSS4G-NA slides ([GeoServer In Production](https://web.archive.org/web/20130819/http://blog.opengeo.org/wp-content/uploads/2013/05/GeoServerProduction.pdf), [GeoServer CSS Module](https://web.archive.org/web/20130819/http://blog.opengeo.org/wp-content/uploads/2013/05/foss4gna2013-geoserver-css.pdf), [Scripting GeoServer with GeoScript](https://web.archive.org/web/20130819/http://blog.opengeo.org/wp-content/uploads/2013/05/Scripting-GeoServer-with-GeoScript.pdf), [The State of GeoServer 2013](https://web.archive.org/web/20130819/http://blog.opengeo.org/wp-content/uploads/2013/05/State-of-GeoServer-2013.pdf))

	
  * INSPIRE Conference 2013 slides ([Analysing GeoServer compatibility with INSPIRE requirements](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime?from_search=2))

	
  * FOSSGIS 2013 slides ([Introduction to GeoServer](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime))

----

## GeoServer 2.4-RC1

Released on August 19th 2013

#### Download format

- [Binary (OS independent)](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC1/geoserver-2.4-RC1-bin.zip/download)
- [Web Archive](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC1/geoserver-2.4-RC1-war.zip)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC1/geoserver-2.4-RC1.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC1/geoserver-2.4-RC1.dmg/download)
- [Source Code](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC1/geoserver-2.4-RC1-src.zip)

#### Documentation

- [HTML Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC1/geoserver-2.4-RC1-htmldoc.zip)
- [API Documentation](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC1/geoserver-2.4-RC1-javadoc.zip)
- [Release Notes](http://sourceforge.net/projects/geoserver/files/GeoServer/2.4-RC1/geoserver-2.4-RC1-release-notes.txt)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-app-schema-plugin.zip)
- [ArcSDE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-arcsde-plugin.zip)
- [DB2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-db2-plugin.zip)
- [H2](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-h2-plugin.zip)
- [MySQL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-mysql-plugin.zip)
- [Oracle](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-oracle-plugin.zip)
- [Pregeneralized features](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-feature-pregeneralized-plugin.zip)
- [SQL Server](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-sqlserver-plugin.zip)
- [Teradata](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-teradata-plugin.zip)
- [VPF](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-vpf-plugin.zip)
- [INSPIRE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-inspire-plugin.zip)

**Coverage store**

- [GDAL](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-gdal-plugin.zip)
- [Image Pyramid](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-pyramid-plugin.zip)
- [JPEG2000](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-jp2k-plugin.zip)
- [JDBC Image Mosaic](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-imagemosaic-jdbc-plugin.zip)

**Other**

- [Chart dynamic symbolizer](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-charts-plugin.zip)
- [Control flow](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-control-flow-plugin.zip)
- [Cross layer filtering](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-querylayer-plugin.zip)
- [CSS styling](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-css-plugin.zip)
- [Excel output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-excel-plugin.zip)
- [GeoSearch](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-geosearch-plugin.zip)
- [Image Map output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-imagemap-plugin.zip)
- [OGR output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-ogr-plugin.zip)
- [XSLT output format](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-xslt-plugin.zip)
- [WPS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-wps-plugin.zip)
- [CAS](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-cas-plugin.zip)
- Monitor ([Core](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-monitor-plugin.zip), [Hibernate](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.4-RC1/geoserver-2.4-RC1-monitor-hibernate-plugin.zip))

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 19446

## Release notes

Improvement:

* [GEOS-5647](https://osgeo-org.atlassian.net/browse/GEOS-5647) WMS-EO Wizard
* [GEOS-5761](https://osgeo-org.atlassian.net/browse/GEOS-5761) maxDisplacement works for simple TextSymbolizers as well
* [GEOS-5907](https://osgeo-org.atlassian.net/browse/GEOS-5907) Add Legend panel to CSS demo
* [GEOS-5931](https://osgeo-org.atlassian.net/browse/GEOS-5931) GeoServerDataDirectory.findDataFile shouldn't force to return a File when not-dealing with an actual file.

Bug:

* [GEOS-1802](https://osgeo-org.atlassian.net/browse/GEOS-1802) superfluous xml-apis JAR in binary distribution
* [GEOS-2866](https://osgeo-org.atlassian.net/browse/GEOS-2866) Changes on contact and jai pages are non cancellable
* [GEOS-2867](https://osgeo-org.atlassian.net/browse/GEOS-2867) Changes to WFS service level and gml config are non cancellable
* [GEOS-3064](https://osgeo-org.atlassian.net/browse/GEOS-3064) Problem handling complex axis definitions
* [GEOS-3883](https://osgeo-org.atlassian.net/browse/GEOS-3883) reprojection error being applied to each processing tile with in a requested image subset.
* [GEOS-4005](https://osgeo-org.atlassian.net/browse/GEOS-4005) Unable to use parameter substitution with Google Earth plugin/KML
* [GEOS-4063](https://osgeo-org.atlassian.net/browse/GEOS-4063) ImageMosaic plugin can't read dataset
* [GEOS-4393](https://osgeo-org.atlassian.net/browse/GEOS-4393) WMS-request on ECW-datastores seems to consume all available memory
* [GEOS-4480](https://osgeo-org.atlassian.net/browse/GEOS-4480) Style in layer group cannot be changed
* [GEOS-4584](https://osgeo-org.atlassian.net/browse/GEOS-4584) Cannot change default style on layer groups
* [GEOS-4655](https://osgeo-org.atlassian.net/browse/GEOS-4655) Style change on layer group page is not reflected on a page immediately
* [GEOS-5245](https://osgeo-org.atlassian.net/browse/GEOS-5245) Integrated GWC capabilities documents generate awkward file name and type
* [GEOS-5640](https://osgeo-org.atlassian.net/browse/GEOS-5640) DPI format_option seems not work on PointSymbolizers without a size tag
* [GEOS-5651](https://osgeo-org.atlassian.net/browse/GEOS-5651) Uploading smaller freemarker template file leads to invalid file on server
* [GEOS-5681](https://osgeo-org.atlassian.net/browse/GEOS-5681) Relative path to watermark file does not work as advertised
* [GEOS-5685](https://osgeo-org.atlassian.net/browse/GEOS-5685) GeoWebCache not WMS 1.3.0 compliant
* [GEOS-5703](https://osgeo-org.atlassian.net/browse/GEOS-5703) TurboJPEG issue: BandSelect on images with alpha
* [GEOS-5704](https://osgeo-org.atlassian.net/browse/GEOS-5704) TurboJPEG issue: ImageMosaic TurboJpeg encoding may throw IllegalArgumentException
* [GEOS-5842](https://osgeo-org.atlassian.net/browse/GEOS-5842) List of drives is invisible for Adding store
* [GEOS-5860](https://osgeo-org.atlassian.net/browse/GEOS-5860) GetLegend request doesn't work with Rendering Transformations
* [GEOS-5870](https://osgeo-org.atlassian.net/browse/GEOS-5870) Submitting incomplete styles wipes style
* [GEOS-5881](https://osgeo-org.atlassian.net/browse/GEOS-5881) LayerGroup page does not mandate the specification of the CRS
* [GEOS-5886](https://osgeo-org.atlassian.net/browse/GEOS-5886) GWC service capabilities should not be listed, GWC is not a OGC service (WMTS is)
* [GEOS-5906](https://osgeo-org.atlassian.net/browse/GEOS-5906) Gathering attribute statistics in the CSS demo page should be optional
* [GEOS-5921](https://osgeo-org.atlassian.net/browse/GEOS-5921) Disabling anonymous authentication for the GUI results in an HTTP redirect loop
* [GEOS-5923](https://osgeo-org.atlassian.net/browse/GEOS-5923) Adjust aspect ratio of KML ground overlays
* [GEOS-5929](https://osgeo-org.atlassian.net/browse/GEOS-5929) CSS demo page does not allow to style raster layers
* [GEOS-5930](https://osgeo-org.atlassian.net/browse/GEOS-5930) NPE errors when running through CSW tutorial
* [GEOS-5934](https://osgeo-org.atlassian.net/browse/GEOS-5934) CSW service does not automatically create its own service info
* [GEOS-5937](https://osgeo-org.atlassian.net/browse/GEOS-5937) Internal CSW store does not see changes to the mapping file until GeoServer is restarted
* [GEOS-5942](https://osgeo-org.atlassian.net/browse/GEOS-5942) GetFeatureInfo with GML3 output will fail on raster layers
* [GEOS-5943](https://osgeo-org.atlassian.net/browse/GEOS-5943) KML wfs output format does not properly set the output file name
* [GEOS-5953](https://osgeo-org.atlassian.net/browse/GEOS-5953) Trying to change the style of a layer in a group wil have (visually) no effect
* [GEOS-5954](https://osgeo-org.atlassian.net/browse/GEOS-5954) Capabilities resource error handling is not applied to layer groups
* [GEOS-5955](https://osgeo-org.atlassian.net/browse/GEOS-5955) Reosurce error handling drop down choice is not internationalized
* [GEOS-5960](https://osgeo-org.atlassian.net/browse/GEOS-5960) Test connection does not work in LDAP Authentication Provider config with ActiveDirectory
* [GEOS-5961](https://osgeo-org.atlassian.net/browse/GEOS-5961) GetFeatureInfo doesn't round scales
* [GEOS-5973](https://osgeo-org.atlassian.net/browse/GEOS-5973) KMLReflectorTest failure on Java 7

Task:

* [GEOS-1676](https://osgeo-org.atlassian.net/browse/GEOS-1676) verify org.vfny.geoserver.servlets.AbstractService is actually not used anymore and remove/deprecate
* [GEOS-5896](https://osgeo-org.atlassian.net/browse/GEOS-5896) Document uconfiguration of GDAL_DRIVER_PATH on Windows
* [GEOS-5966](https://osgeo-org.atlassian.net/browse/GEOS-5966) Switch GetFeatureInfo minimum search area to 5 pixels
