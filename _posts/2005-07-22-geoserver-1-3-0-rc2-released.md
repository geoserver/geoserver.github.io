---
author: David Blasby
date: 2005-07-22
layout: post
link: http://docs.codehaus.org/display/GEOS/GeoServer+1.3.0-RC2
wayback: https://web.archive.org/web/20060624094659/http://docs.codehaus.org:80/display/GEOS/GeoServer+1.3.0-RC2
title: "GeoServer 1.3.0-RC2 Released"
categories:
- Announcements
---

GeoServer 1.3.0-RC2 has been released, check it out below.

----

The release candiate GeoServer 1.3.0-RC2 is available for testing from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC2/):

- [Release Notes](#release-notes)
- [geoserver-1.3.0-RC2-bin.tar.gz](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC2/geoserver-1.3.0-RC2-bin.tar.gz/download)
- [geoserver-1.3.0-RC2-docs.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC2/geoserver-1.3.0-RC2-docs.zip/download)
- [geoserver-1.3.0-RC2.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC2/geoserver-1.3.0-RC2.exe/download)
- [geoserver-1.3.0-RC2-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC2/geoserver-1.3.0-RC2-src.zip/download)
- [geoserver-1.3.0-RC2-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC2/geoserver-1.3.0-RC2-war.zip/download)

Tested with: Jetty

## Release notes

Improvement:

* [GEOS-376](https://osgeo-org.atlassian.net/browse/GEOS-376) Removed JAI dependency

Bug:

* [GEOS-261](https://osgeo-org.atlassian.net/browse/GEOS-261) Incorrect error code for badly formed gml:bbox
* [GEOS-296](https://osgeo-org.atlassian.net/browse/GEOS-296) Deleting namespaces, which are in use blocks restart of GeoServer
* [GEOS-310](https://osgeo-org.atlassian.net/browse/GEOS-310) Data.getFeatureTypeInfo seems to not correctly find FeatureTypes
* [GEOS-335](https://osgeo-org.atlassian.net/browse/GEOS-335) TestWfsPost doesn't support BASIC authentication (CONTAINS A FIX)
* [GEOS-353](https://osgeo-org.atlassian.net/browse/GEOS-353) SQL Datetime field insert failure
* [GEOS-363](https://osgeo-org.atlassian.net/browse/GEOS-363) Missing path in startup.bat
* [GEOS-365](https://osgeo-org.atlassian.net/browse/GEOS-365) LiteRenderer2 still dependent on JAI
* [GEOS-366](https://osgeo-org.atlassian.net/browse/GEOS-366) java.lang.ArrayIndexOutOfBoundsException in Log4JFormatter.init()
* [GEOS-368](https://osgeo-org.atlassian.net/browse/GEOS-368) SAX transaction parser cuts down multiline string attribute values.
* [GEOS-369](https://osgeo-org.atlassian.net/browse/GEOS-369) Filter Functions don't work, ExpressionSAXParser misses implementation
