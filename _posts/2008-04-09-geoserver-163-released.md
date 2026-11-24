---
author: bmmpxf
comments: true
date: 2008-04-09 15:25:46+00:00
layout: post
link: http://blog.geoserver.org/2008/04/09/geoserver-163-released/
slug: geoserver-163-released
title: GeoServer 1.6.3 Released
wordpress_id: 99
categories:
- Announcements
---

The GeoServer team would like to announce the release of 1.6.3.  This is a stable release containing over 30 patches and improvements since 1.6.2.

One of the more visible additions is support for [watermarking](http://geoserver.org/display/GEOSDOC/Watermarking).  People have been asking for this for some time, so thanks to [GeoSolutions](http://www.geo-solutions.it) for implementing it.  Also, coverage reprojection now works much better.  Thanks to Martin Desruisseaux of [Geomatys](http://www.geomatys.fr) for the continued support on the GeoServer CRS subsystem.  KML generation has been optimized (faster, less memory consumption) especially when dealing with large geometries.  GeoServer supports so many projections natively, but that can have its downsides, namely when certain clients aren't prepared for the size of the capabilities document!  Now the [SRS list can be limited](http://geoserver.org/display/GEOSDOC/Common+OWS+Configuration) in the WMS capabilities.  Special thanks to Gabriel Roldán for the above two features.

You can view the 1.6.3 [changelog](#release-notes) for details, and download from geoserver.org. Thanks to the community for continually improving GeoServer.  Please continue to submit those [bug reports](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS) and feature requests.

----

#### GeoServer 1.6.3 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/).

SourceForge Release 590810

- [geoserver-1.6.3.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/geoserver-1.6.3.exe/download) (Win32 self-installing executable)
- [geoserver-1.6.3-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/geoserver-1.6.3-bin.zip/download) (UNIX binary)
- [geoserver-1.6.3-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/geoserver-1.6.3-src.zip/download) (Source code)
- [geoserver-1.6.3-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/geoserver-1.6.3-war.zip/download) (Web archive)
- [geoserver-1.6.3-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/geoserver-1.6.3-doc.zip/download) (Documentation)
- [geoserver-1.6.3-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/geoserver-1.6.3-javadoc.zip/download) (Java Documentation)

#### DataStore Extensions

- **NEW!** [GeoWebCache](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/extensions/geoserver-1.6.0-gwc-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/extensions/geoserver-1.6.3-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/extensions/geoserver-1.6.3-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/extensions/geoserver-1.6.3-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/extensions/geoserver-1.6.3-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/extensions/geoserver-1.6.3-vpf-plugin.zip/download)
- [WFS](http://downloads.sourceforge.net/geoserver/geoserver-1.6.3-wfs-plugin.zip)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/extensions/geoserver-1.6.3-oracle-plugin.zip/download)

[Extensions download page](https://sourceforge.net/project/showfiles.php?group_id=25086&package_id=129885)

#### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.3/extensions/geoserver-1.6.3-pyramid-plugin.zip/download)

Tested with: Jetty, Tomcat

## Release notes

New Feature:

* [GEOS-806](https://osgeo-org.atlassian.net/browse/GEOS-806) Add watermarking (e.g. show copyright notice, logo, etc) to wms output

Improvement:

* [GEOS-1596](https://osgeo-org.atlassian.net/browse/GEOS-1596) Document how to use the wfs strict/lax parsing settings
* [GEOS-1704](https://osgeo-org.atlassian.net/browse/GEOS-1704) Mock testing directory cannot be deleted on windows, we need to add a Data.close() method
* [GEOS-1731](https://osgeo-org.atlassian.net/browse/GEOS-1731) Add option to change the encoding to georss requests
* [GEOS-1769](https://osgeo-org.atlassian.net/browse/GEOS-1769) Document watermarking
* [GEOS-1784](https://osgeo-org.atlassian.net/browse/GEOS-1784) We should advertise we support user defined symbolization in WMS capabilities
* [GEOS-1819](https://osgeo-org.atlassian.net/browse/GEOS-1819) FeatureWrapper performance and memory usage improvements
* [GEOS-1820](https://osgeo-org.atlassian.net/browse/GEOS-1820) Add explanation of the different downloadables
* [GEOS-1830](https://osgeo-org.atlassian.net/browse/GEOS-1830) Allow to limit the list of available CRS's in WMS GetCapabilities

Bug:

* [GEOS-1037](https://osgeo-org.atlassian.net/browse/GEOS-1037) Projection handling not correct for Stereographic projection
* [GEOS-1283](https://osgeo-org.atlassian.net/browse/GEOS-1283) error "org.geotools.renderer.lite.StreamingRenderer - Wrong number of attributes expected 1 got 2"
* [GEOS-1486](https://osgeo-org.atlassian.net/browse/GEOS-1486) Cannot create new SLD for ArcSDE FeatureType
* [GEOS-1720](https://osgeo-org.atlassian.net/browse/GEOS-1720) Grid coverage reprojection degrades image quality in an unacceptable way
* [GEOS-1756](https://osgeo-org.atlassian.net/browse/GEOS-1756) wfsv requests do not handle application schema namespaces when they are not declared
* [GEOS-1775](https://osgeo-org.atlassian.net/browse/GEOS-1775) Service URLs are path dependent
* [GEOS-1791](https://osgeo-org.atlassian.net/browse/GEOS-1791) Favicon not working (and other images as well)
* [GEOS-1797](https://osgeo-org.atlassian.net/browse/GEOS-1797) WMS Reflector does not deal with coverages
* [GEOS-1801](https://osgeo-org.atlassian.net/browse/GEOS-1801) geojson output format does not handle queries for multiple feature types
* [GEOS-1804](https://osgeo-org.atlassian.net/browse/GEOS-1804) WMS requests returning blank depending on bounds
* [GEOS-1805](https://osgeo-org.atlassian.net/browse/GEOS-1805) missing logs directory in binary distribution
* [GEOS-1806](https://osgeo-org.atlassian.net/browse/GEOS-1806) Image Pyramid extension archive contains no .jar files
* [GEOS-1808](https://osgeo-org.atlassian.net/browse/GEOS-1808) Lack of Url Encoding
* [GEOS-1810](https://osgeo-org.atlassian.net/browse/GEOS-1810) version attribute in DescribeLayer response is wrong
* [GEOS-1811](https://osgeo-org.atlassian.net/browse/GEOS-1811) BBOX filters created by the SLDParser cannot be encoded or cloned properly
* [GEOS-1813](https://osgeo-org.atlassian.net/browse/GEOS-1813) MapPreview links do not specify version=1.1.1
* [GEOS-1815](https://osgeo-org.atlassian.net/browse/GEOS-1815) ensure all xml output explicity sets charset from GeoServer.getCharSet()
* [GEOS-1816](https://osgeo-org.atlassian.net/browse/GEOS-1816) WFS DescribeFeatureType does not work anymore if the layer prefix is not provided
* [GEOS-1832](https://osgeo-org.atlassian.net/browse/GEOS-1832) WMS GetCapabilities returns <SRS>EPSG:</SRS> when there are no feature types defined
* [GEOS-1833](https://osgeo-org.atlassian.net/browse/GEOS-1833) CoverageInfos bounding boxes are not aggregated for the main WMS Layer in GetCapabilities
* [GEOS-1837](https://osgeo-org.atlassian.net/browse/GEOS-1837) Postgis backend is spamming logs
* [GEOS-1850](https://osgeo-org.atlassian.net/browse/GEOS-1850) Rotated images are not displayed correctly anymore (regression)

Task:

* [GEOS-1591](https://osgeo-org.atlassian.net/browse/GEOS-1591) Provide instructions on how to set admin password
* [GEOS-1618](https://osgeo-org.atlassian.net/browse/GEOS-1618) pass describe feature type cite tests
* [GEOS-1682](https://osgeo-org.atlassian.net/browse/GEOS-1682) release directory contains jars
* [GEOS-1803](https://osgeo-org.atlassian.net/browse/GEOS-1803) update geoserver link to geoserver.org
* [GEOS-1809](https://osgeo-org.atlassian.net/browse/GEOS-1809) "Documentation" and "Wiki" links on front Admin page should point to geoserver.org, not Codehaus
* [GEOS-1828](https://osgeo-org.atlassian.net/browse/GEOS-1828) Announcement items
* [GEOS-1835](https://osgeo-org.atlassian.net/browse/GEOS-1835) Update user guide for WMS SRS list filtering
