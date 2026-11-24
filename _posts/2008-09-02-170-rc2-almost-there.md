---
author: bmmpxf
comments: true
date: 2008-09-02 15:46:15+00:00
layout: post
link: http://blog.geoserver.org/2008/09/02/170-rc2-almost-there/
slug: 170-rc2-almost-there
title: '1.7.0-RC2: Almost There'
wordpress_id: 120
categories:
- Announcements
---

We've received some good feedback from the community on the first release candidate of version 1.7.0, and have made some improvements that we wanted to share with you.  This second release candidate is more stable and features some code-tightening as well (MIME types are now case insensitive, a limited SRS list persists again, [and more](#release-notes).)  This is the most stable release yet of the new 1.7.0 branch and we encourage you to try it out.  If all goes according to plan, we should have a final release around the corner.

----

#### GeoServer 1.7.0-RC2 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/).

Released on August 29, 2008. SourceForge Release 622753

- [Release Notes](#release-notes)
- [geoserver-1.7.0-RC2a.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/geoserver-1.7.0-RC2a.exe/download) (Win32 self-installing executable)
- [geoserver-1.7.0-RC2a-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/geoserver-1.7.0-RC2a-bin.zip/download) (UNIX binary)
- [geoserver-1.7.0-RC2a-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/geoserver-1.7.0-RC2a-src.zip/download) (Source code)
- [geoserver-1.7.0-RC2a-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/geoserver-1.7.0-RC2a-war.zip/download) (Web archive)
- [geoserver-1.7.0-RC2-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/geoserver-1.7.0-RC2-doc.zip/download) (Documentation export from geoserver.org)
- [geoserver-1.7.0-RC2a-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/geoserver-1.7.0-RC2a-javadoc.zip/download) (Java Documentation)

#### [Extensions download page](https://sourceforge.net/projects/geoserver/files/OldFiles/1.7.0/)

**DataStore Extensions**

- [GeoWebCache](https://sourceforge.net/projects/geoserver/files/OldFiles/1.7.0/geoserver-1.7.0-RC2-gwc-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/extensions/geoserver-1.7.0-RC2-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/extensions/geoserver-1.7.0-RC2-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/extensions/geoserver-1.7.0-RC2-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/extensions/geoserver-1.7.0-RC2-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/extensions/geoserver-1.7.0-RC2-vpf-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/extensions/geoserver-1.7.0-RC2-wfsv-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/extensions/geoserver-1.7.0-RC2-oracle-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/extensions/geoserver-1.7.0-RC2-h2-plugin.zip/download)

**Coverage Extensions**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/extensions/geoserver-1.7.0-RC2-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC2/extensions/geoserver-1.7.0-RC2-pyramid-plugin.zip/download)

## Release notes

Improvement:

* [GEOS-654](https://osgeo-org.atlassian.net/browse/GEOS-654) Register GetMapProducers directly and remove the factories
* [GEOS-2176](https://osgeo-org.atlassian.net/browse/GEOS-2176) Better deal with invalid filters

Bug:

* [GEOS-2131](https://osgeo-org.atlassian.net/browse/GEOS-2131) Unable to send WMS request for multiple layers of same feature with different filter
* [GEOS-2166](https://osgeo-org.atlassian.net/browse/GEOS-2166) Check there are no references before removing layers and stores
* [GEOS-2167](https://osgeo-org.atlassian.net/browse/GEOS-2167) Removing layers part of a base layer group causes exception
* [GEOS-2168](https://osgeo-org.atlassian.net/browse/GEOS-2168) 'openlayers' alias for 'application/openlayers' no longer works for wms
* [GEOS-2170](https://osgeo-org.atlassian.net/browse/GEOS-2170) MIIME-Type matching shall be case insensitive
* [GEOS-2171](https://osgeo-org.atlassian.net/browse/GEOS-2171) limited list of SRS
* [GEOS-2178](https://osgeo-org.atlassian.net/browse/GEOS-2178) asking for an extension with a custom ApplicationContext returns the cached value from the internal ApplicationContext
* [GEOS-2185](https://osgeo-org.atlassian.net/browse/GEOS-2185) KML link on demo page leads to KML document with invalid links

Task:

* [GEOS-2132](https://osgeo-org.atlassian.net/browse/GEOS-2132) Add dependency excludes to gwc plugin to avoid unwanted jars when auto-including it in release
* [GEOS-2133](https://osgeo-org.atlassian.net/browse/GEOS-2133) GWC needs to test that configuration gets loaded
