---
author: Justin Deoliveira
comments: true
date: 2008-10-27 05:12:30+00:00
layout: post
link: http://blog.geoserver.org/2008/10/27/geoserver-170-released/
slug: geoserver-170-released
title: GeoServer 1.7.0 Released
wordpress_id: 142
categories:
- Announcements
- Features
---

The GeoServer team is proud to announce the release of GeoServer 1.7.0, available below for download. This is a very big release for GeoServer as the 1.7.x series brings some exciting new features and improvements.

Security in 1.7 has been improved by allowing access control at the [layer/feature type level](https://web.archive.org/web/20081027/http://geoserver.org/display/GEOS/GSIP+19+-+Per+layer+security), in addition to the [service level](https://web.archive.org/web/20081027/http://geoserver.org/display/GEOSDOC/2.6+Security+subsystem). This allows users to secure data in a much more granular way. There has also been much work done to better performance for GeoServer 1.7. The short of which is faster rendering with WMS, as well as faster data access with Shapefile, PostGIS, and ArcSDE. For those interested in the specifics check out the [presentation](http://presentations.opengeo.org/2008_FOSS4G/WebMapServerPerformance-FOSS4G2008.pdf) given by Andrea Aime at FOSS4G this year in South Africa. Also of note for this release is a retrofit of the built in [OpenLayers](http://openlayers.org) map preview. The preview interface now allows for filtering and controlling various rendering aspects such as anti-aliasing and image format.

The folks from [GeoSolutions](http://www.geo-solutions.it/) have also been quite busy as usual and have once again made some great improvements on the raster/coverage side of things. GeoServer now supports [additional raster formats](https://web.archive.org/web/20081027/http://geoserver.org/display/GEOSDOC/ImageIO-ext+GDAL+extensions) such as ECW, MrSID, and JPEG 2000. This has been achieved by leveraging the [GDAL](http://www.gdal.org/) library. As well as additional formats GeoSolutions has also provided the ability to perform much more powerful coverage portrayal via the SLD [RasterSymbolizer](https://web.archive.org/web/20081027/http://docs.codehaus.org/display/GEOTOOLS/Raster+Symbolizer+support) construct. With support for RasterSymbolizer users can now do channel selection, define color maps, perform contrast enhancement, and more. Special thanks to GeoSolutions.

As the GeoServer community expands, so does the number of translations to support other languages. 1.7 brings a Dutch and a Russian translation. Thanks to Leon Vanberio and Maxim Dubinin for their great contributions. And special thanks to all users who helped us test the 1.7 release candidates and filed bugs in the tracker.

Not only is GeoServer 1.7.0 a big release for users, it's also a notable one for developers. Some major improvements have been done to the GeoServer core which will act as building blocks for features in future releases. This involves a change to the internal feature model which now allows the modeling of complex feature relationships; something that gets us closer to achieving full community schema support. There have also been changes to the back-end configuration subsystem which now has a much cleaner API for developers writing plug-ins and user interface components. It will also serve as the base for supporting additional persistence mechanisms such as hibernate and other O/R mappers.

And as usual a heap of bugs were fixed for this release. Over [200 issues](#release-notes) were handled for 1.7.0.

Download, try it out, and let us know what you think. Comments and feedback are always welcome on the [mailing list](mailto:geoserver-users@lists.sourceforge.net). The community is always interested to hear how people are using GeoServer. Also stay tuned for the 1.7.1 release, due out in a month or so, which will include some exciting new improvements to Google Earth and KML support.

----

## GeoServer 1.7.0

Released on Oct 27, 2008

#### Choose a download format:

- [UNIX / Mac OS X Binary](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/geoserver-1.7.0a-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/geoserver-1.7.0a-war.zip/download)
- [Documentation (Site Export)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/geoserver-1.7.0-doc.zip/download)
- [Release Notes](#release-notes)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/geoserver-1.7.0a.exe/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/geoserver-1.7.0a-src.zip/download)
- [Java Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/geoserver-1.7.0-javadoc.zip/download)

#### GeoServer Extensions

**DataStore Extensions**

- [GeoWebCache](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/extensions/geoserver-1.7.0-gwc-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/extensions/geoserver-1.7.0-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/extensions/geoserver-1.7.0-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/extensions/geoserver-1.7.0-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/extensions/geoserver-1.7.0-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/extensions/geoserver-1.7.0-vpf-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/extensions/geoserver-1.7.0-oracle-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/extensions/geoserver-1.7.0-h2-plugin.zip/download)

**Coverage Extensions**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/extensions/geoserver-1.7.0-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/extensions/geoserver-1.7.0-pyramid-plugin.zip/download)

**Service Extensions**

- [Versioning WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/extensions/geoserver-1.7.0-wfsv-plugin.zip/download)

#### GeoServer on [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0/).

SourceForge Release 635199.

## Release notes

Improvement:

* [GEOS-1883](https://osgeo-org.atlassian.net/browse/GEOS-1883) GeoServer should pick up environment variables
* [GEOS-1968](https://osgeo-org.atlassian.net/browse/GEOS-1968) ServiceException toString() should include the extra exceptionText messages
* [GEOS-2030](https://osgeo-org.atlassian.net/browse/GEOS-2030) KMZ KMPLACEMARK option to add placemarks to raster image
* [GEOS-2048](https://osgeo-org.atlassian.net/browse/GEOS-2048) Make the KML reflector handle regionation requests
* [GEOS-2256](https://osgeo-org.atlassian.net/browse/GEOS-2256) Translation of Geoserver in Russian
* [GEOS-9398](https://osgeo-org.atlassian.net/browse/GEOS-9398) [Community][wps-remote] Async Request Management Proposal

Bug:

* [GEOS-1821](https://osgeo-org.atlassian.net/browse/GEOS-1821) SLD filters broken
* [GEOS-1946](https://osgeo-org.atlassian.net/browse/GEOS-1946) Oracle 10g Error Performing SQL query (TRUE AND TRUE)
* [GEOS-1952](https://osgeo-org.atlassian.net/browse/GEOS-1952) No KVP reader error for strict GetDiff request
* [GEOS-1960](https://osgeo-org.atlassian.net/browse/GEOS-1960) Configuration keeps reverting to namespace topp
* [GEOS-1961](https://osgeo-org.atlassian.net/browse/GEOS-1961) SRS 900913 (and others) not shown from 1.6.3 on
* [GEOS-1973](https://osgeo-org.atlassian.net/browse/GEOS-1973) Data directory relative path are not preserved anymore on trunk
* [GEOS-1977](https://osgeo-org.atlassian.net/browse/GEOS-1977) Arcsites preview turns from red to blue when using jpeg and disabling antialiasign
* [GEOS-1978](https://osgeo-org.atlassian.net/browse/GEOS-1978) Modifying SLD does not appear to take effect without restart
* [GEOS-1993](https://osgeo-org.atlassian.net/browse/GEOS-1993) KML sitemap is broken
* [GEOS-1994](https://osgeo-org.atlassian.net/browse/GEOS-1994) KML polygon symbolizer requires localhost:8080
* [GEOS-1995](https://osgeo-org.atlassian.net/browse/GEOS-1995) Geosearch - offSetSupported() always returns false for KML
* [GEOS-2003](https://osgeo-org.atlassian.net/browse/GEOS-2003) EPSG:54004 in user_projections/epsg.properties has missing bracket
* [GEOS-2118](https://osgeo-org.atlassian.net/browse/GEOS-2118) GeoServer loses the namespaces for individual layers in a layergroup
* [GEOS-2214](https://osgeo-org.atlassian.net/browse/GEOS-2214) FeatureID Filter returns Wrong Result for shapefiles
* [GEOS-2223](https://osgeo-org.atlassian.net/browse/GEOS-2223) DescribeLayer fails with a NullPointerException if the VERSION parameter is not set
* [GEOS-2225](https://osgeo-org.atlassian.net/browse/GEOS-2225) KML regionating does not return the top features in big datasets
* [GEOS-2243](https://osgeo-org.atlassian.net/browse/GEOS-2243) CoverageInfo.getCoverage(envelope,dim) always uses the same CRS as sourceCRS and destCRS instead of using the original coverage CRS as destCRS
* [GEOS-2273](https://osgeo-org.atlassian.net/browse/GEOS-2273) Cleanup GeoServerExtensions when functional/integration tests end
* [GEOS-2279](https://osgeo-org.atlassian.net/browse/GEOS-2279) Fix wms overlay demo
* [GEOS-2299](https://osgeo-org.atlassian.net/browse/GEOS-2299) Too many connections to PostGIS
* [GEOS-2309](https://osgeo-org.atlassian.net/browse/GEOS-2309) fix yahoo maps and virtual earth georss demos
* [GEOS-2328](https://osgeo-org.atlassian.net/browse/GEOS-2328) German, French, Portuguese and Spanish L10N seems to be broken
* [GEOS-2478](https://osgeo-org.atlassian.net/browse/GEOS-2478) Upgrade 1.6.5 -> 1.7.0 SLD trouble

Task:

* [GEOS-1682](https://osgeo-org.atlassian.net/browse/GEOS-1682) release directory contains jars
* [GEOS-2133](https://osgeo-org.atlassian.net/browse/GEOS-2133) GWC needs to test that configuration gets loaded
