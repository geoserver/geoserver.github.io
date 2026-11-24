---
author: bmmpxf
comments: true
date: 2008-09-17 15:25:10+00:00
layout: post
link: http://blog.geoserver.org/2008/09/17/geoserver-165-released/
slug: geoserver-165-released
title: GeoServer 1.6.5 Released!
wordpress_id: 132
categories:
- Announcements
---

The GeoServer team would like to present the newest stable version of GeoServer, 1.6.5.  This is likely to be the last release of the 1.6.x branch, as development moves towards a stable version of 1.7.x.  Nevertheless, this is an important release, as it features a whopping [65 bug fixes and improvements](#release-notes).  Special thanks go to Léon van Berlo for translating GeoServer into Dutch.  This marks our eighth language, and means we now have between approximately 100 and 6904 left to go, depending on [ what source we quote](http://www.ethnologue.com/) and [how we define a language](http://en.wikipedia.org/wiki/Natural_language). We also have WMS point layers rendering correctly again, fixes regarding using the Google Maps projection, and improvements to the Map Preview area of the admin console.  You can take a look at the entire [changelog](#release-notes) if you'd like, or just download this version and check it out for yourself.  Feedback welcome!

----

#### GeoServer 1.6.5 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.5/).

Released on September 15, 2008. SourceForge Release 626557

- [Release Notes](#release-notes)
- [geoserver-1.6.5.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.5/geoserver-1.6.5.exe/download) (Win32 self-installing executable)
- [geoserver-1.6.5-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.5/geoserver-1.6.5-bin.zip/download) (UNIX binary)
- [geoserver-1.6.5-src.zip](http://downloads.sourceforge.net/geoserver/geoserver-1.6.5-src.zip) (Source code)
- [geoserver-1.6.5-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.5/geoserver-1.6.5-war.zip/download) (Web archive)
- [geoserver-1.6.5-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.5/geoserver-1.6.5-doc.zip/download) (Documentation export from geoserver.org)
- [geoserver-1.6.5-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.5/geoserver-1.6.5-javadoc.zip/download) (Java Documentation)

#### [Extensions download page](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6.5/)

**DataStore Extensions**

- [GeoWebCache](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6.5/geoserver-1.6.5-gwc-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.5/extensions/geoserver-1.6.5-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.5/extensions/geoserver-1.6.5-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.5/extensions/geoserver-1.6.5-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.5/extensions/geoserver-1.6.5-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.5/extensions/geoserver-1.6.5-vpf-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.5/extensions/geoserver-1.6.5-wfsv-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.5/extensions/geoserver-1.6.5-oracle-plugin.zip/download)
- [H2](http://downloads.sourceforge.net/geoserver/geoserver-1.6.5-h2-plugin.zip)

**Coverage Extensions**

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.5/extensions/geoserver-1.6.5-pyramid-plugin.zip/download)

## Release notes

New Feature:

* [GEOS-1933](https://osgeo-org.atlassian.net/browse/GEOS-1933) Dutch translation

Improvement:

* [GEOS-1366](https://osgeo-org.atlassian.net/browse/GEOS-1366) Allow renaming of featureTypes
* [GEOS-1416](https://osgeo-org.atlassian.net/browse/GEOS-1416) Implement order in GetLog using toFeatureVersion and fromFeatureVersion order
* [GEOS-1521](https://osgeo-org.atlassian.net/browse/GEOS-1521) Extends Acegi security system to anable HTTP methods (GET,PUT,POST....) filtering.
* [GEOS-1598](https://osgeo-org.atlassian.net/browse/GEOS-1598) ResultType is not being parsed into a ResultTypeType for GetVersionedFeature
* [GEOS-1625](https://osgeo-org.atlassian.net/browse/GEOS-1625) Expose and test GeoRSS simple/gml output formats as well
* [GEOS-1968](https://osgeo-org.atlassian.net/browse/GEOS-1968) ServiceException toString() should include the extra exceptionText messages

Bug:

* [GEOS-360](https://osgeo-org.atlassian.net/browse/GEOS-360) GetLegendGraphics error handling
* [GEOS-1038](https://osgeo-org.atlassian.net/browse/GEOS-1038) New ArcSDE featuretypes aren't compatible with their default output
* [GEOS-1293](https://osgeo-org.atlassian.net/browse/GEOS-1293) Rendererer fails to draw tiles across the dateline
* [GEOS-1657](https://osgeo-org.atlassian.net/browse/GEOS-1657) NPE thrown when configuring a shapefile with no .prj information
* [GEOS-1688](https://osgeo-org.atlassian.net/browse/GEOS-1688) null pointer exception in DefaultFilterVisitor
* [GEOS-1700](https://osgeo-org.atlassian.net/browse/GEOS-1700) wfs:FeatureCollection numberOfFeatures does not respect the maxFeatures parameter
* [GEOS-1705](https://osgeo-org.atlassian.net/browse/GEOS-1705) Some XML writters set the xml charset to its human readable form instead of its canonical form
* [GEOS-1727](https://osgeo-org.atlassian.net/browse/GEOS-1727) Error when inserting polygons into a postgis table via geoserver with wfs gml.
* [GEOS-1749](https://osgeo-org.atlassian.net/browse/GEOS-1749) comma in PostGIS money datatype causes GetFeatureInfo request to fail
* [GEOS-1766](https://osgeo-org.atlassian.net/browse/GEOS-1766) Freemarker is eating exception causes if an error occurrs scrolling over a feature collection
* [GEOS-1867](https://osgeo-org.atlassian.net/browse/GEOS-1867) MySQL error processing ogc:Filter with ogc:And clause
* [GEOS-1893](https://osgeo-org.atlassian.net/browse/GEOS-1893) Required param missing in GetFeature, funny error back
* [GEOS-1894](https://osgeo-org.atlassian.net/browse/GEOS-1894) WMS content disappears in GIF images when zoomed out too far
* [GEOS-1901](https://osgeo-org.atlassian.net/browse/GEOS-1901) Text only antialias is not working properly
* [GEOS-1916](https://osgeo-org.atlassian.net/browse/GEOS-1916) GetFeatureInfo does not properly handle multi layer filters
* [GEOS-1924](https://osgeo-org.atlassian.net/browse/GEOS-1924) GetFeatureInfo returns text response when the format is not recognize, shouldn't it return an exception instead?
* [GEOS-1932](https://osgeo-org.atlassian.net/browse/GEOS-1932) Aliasing "broken" in WFS1.1 DFT
* [GEOS-1942](https://osgeo-org.atlassian.net/browse/GEOS-1942) WMS renders point layer incorrectly
* [GEOS-1946](https://osgeo-org.atlassian.net/browse/GEOS-1946) Oracle 10g Error Performing SQL query (TRUE AND TRUE)
* [GEOS-1947](https://osgeo-org.atlassian.net/browse/GEOS-1947) Icons in KML output from Geoserver appear to be overlayed with a grey mask
* [GEOS-1948](https://osgeo-org.atlassian.net/browse/GEOS-1948) When an sld refers an external graphic that's not there, generated KML is invalid (unclosed elements)
* [GEOS-1952](https://osgeo-org.atlassian.net/browse/GEOS-1952) No KVP reader error for strict GetDiff request
* [GEOS-1955](https://osgeo-org.atlassian.net/browse/GEOS-1955) WFS-T demo broken in FF3 RC1 and IE 7
* [GEOS-1958](https://osgeo-org.atlassian.net/browse/GEOS-1958) Transaction binding in WFS 1.0 is not able to read native elements properly
* [GEOS-1959](https://osgeo-org.atlassian.net/browse/GEOS-1959) FireFox 3 and open layers home page demo garbled
* [GEOS-1961](https://osgeo-org.atlassian.net/browse/GEOS-1961) SRS 900913 (and others) not shown from 1.6.3 on
* [GEOS-1963](https://osgeo-org.atlassian.net/browse/GEOS-1963) ArcSDE datastores are disposed in DataDataStoresEditorAction.java and they never get re-opened
* [GEOS-1966](https://osgeo-org.atlassian.net/browse/GEOS-1966) WFS-T update does not accept an obvious number for a field of type bigint (PostGIS)
* [GEOS-1970](https://osgeo-org.atlassian.net/browse/GEOS-1970) Acegi filter integration is not covering the /ows path
* [GEOS-1972](https://osgeo-org.atlassian.net/browse/GEOS-1972) Inconsistent KML icon size when switching from wms overlay to vector drawing
* [GEOS-1979](https://osgeo-org.atlassian.net/browse/GEOS-1979) CQL filters causing StreamingRenderer failure
* [GEOS-1991](https://osgeo-org.atlassian.net/browse/GEOS-1991) Wrong version number in poms on 1.6.x
* [GEOS-1992](https://osgeo-org.atlassian.net/browse/GEOS-1992) rest/styles throws Exception on 1.6.x
* [GEOS-2003](https://osgeo-org.atlassian.net/browse/GEOS-2003) EPSG:54004 in user_projections/epsg.properties has missing bracket
* [GEOS-2005](https://osgeo-org.atlassian.net/browse/GEOS-2005) Dispatcher breaks on kvp parse when strict=true is used
* [GEOS-2008](https://osgeo-org.atlassian.net/browse/GEOS-2008) The links available in the mini-map preview of the featuretypes are not correct
* [GEOS-2024](https://osgeo-org.atlassian.net/browse/GEOS-2024) Caching headers issues
* [GEOS-2026](https://osgeo-org.atlassian.net/browse/GEOS-2026) Locking code can still leak connections
* [GEOS-2031](https://osgeo-org.atlassian.net/browse/GEOS-2031) WMS capabilities report an inexistent style for layer groups
* [GEOS-2032](https://osgeo-org.atlassian.net/browse/GEOS-2032) Errors in the struts UI leave the user (and the developer) with a useless error message
* [GEOS-2040](https://osgeo-org.atlassian.net/browse/GEOS-2040) AbstractFeatureInfoResponse: WmsException may occurs if Bulsa Parameters are missing when evaluating a coverage providing a point in different CRS (with respect to the one of the coverage itself).
* [GEOS-2042](https://osgeo-org.atlassian.net/browse/GEOS-2042) Labels are always centered, the label point does not take into account the visible part of the polygon
* [GEOS-2044](https://osgeo-org.atlassian.net/browse/GEOS-2044) Can't add GeoTIFF coverage if it has exactly one overview
* [GEOS-2046](https://osgeo-org.atlassian.net/browse/GEOS-2046) SLD filters aren't applied on KML output when reprojection is needed
* [GEOS-2050](https://osgeo-org.atlassian.net/browse/GEOS-2050) Proxy filter engages even if the proxying is not enabled
* [GEOS-2052](https://osgeo-org.atlassian.net/browse/GEOS-2052) Can't disable caching and remove the caching time (in feature type configuration)
* [GEOS-2057](https://osgeo-org.atlassian.net/browse/GEOS-2057) WMS raster interpolation settings are ignored
* [GEOS-2131](https://osgeo-org.atlassian.net/browse/GEOS-2131) Unable to send WMS request for multiple layers of same feature with different filter
* [GEOS-2166](https://osgeo-org.atlassian.net/browse/GEOS-2166) Check there are no references before removing layers and stores
* [GEOS-2167](https://osgeo-org.atlassian.net/browse/GEOS-2167) Removing layers part of a base layer group causes exception
* [GEOS-2187](https://osgeo-org.atlassian.net/browse/GEOS-2187) the link to openlayers in the home of geoserver it is mistaken
* [GEOS-2191](https://osgeo-org.atlassian.net/browse/GEOS-2191) wfs 1.1 describe feature type uses wrong base url for schemas
* [GEOS-2198](https://osgeo-org.atlassian.net/browse/GEOS-2198) Map preview broken in 1.6.x
* [GEOS-2222](https://osgeo-org.atlassian.net/browse/GEOS-2222) openlayers getfeatureinfo makes getmap request

Task:

* [GEOS-1880](https://osgeo-org.atlassian.net/browse/GEOS-1880) CLONE -Finish off CQL tutorial
* [GEOS-2132](https://osgeo-org.atlassian.net/browse/GEOS-2132) Add dependency excludes to gwc plugin to avoid unwanted jars when auto-including it in release
* [GEOS-2133](https://osgeo-org.atlassian.net/browse/GEOS-2133) GWC needs to test that configuration gets loaded
