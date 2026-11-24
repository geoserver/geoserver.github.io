---
author: bmmpxf
comments: true
date: 2008-10-15 13:54:42+00:00
layout: post
link: http://blog.geoserver.org/2008/10/15/170-rc4-fourth-time-is-the-charm/
slug: 170-rc4-fourth-time-is-the-charm
title: '1.7.0-RC4: Fourth Time Is The Charm?'
wordpress_id: 138
categories:
- Announcements
---

Today we have a new release candidate of GeoServer 1.7.x for everyone's testing pleasure.  We don't wish to invoke [Zeno's Dichotomy Paradox](http://en.wikipedia.org/wiki/Dichotomy_paradox), but we are in fact very close to the release.  In truth this release candidate only includes [six new bug fixes](#release-notes) (the most notable regarding projection persistence and Google Earth overlays).  If it seems like we're going release candidate crazy, rest assured that it is only because we want to ensure that 1.7.0 will be a stable release and not a beta that was rushed out the door.  Give it a try!

----

#### GeoServer 1.7.0-RC4 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/).

Released on October 14, 2008. SourceForge Release 632409

- [Release Notes](#release-notes)
- [geoserver-1.7.0-RC4.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/geoserver-1.7.0-RC4.exe/download) (Win32 self-installing executable)
- [geoserver-1.7.0-RC4-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/geoserver-1.7.0-RC4-bin.zip/download) (UNIX/Mac OS X binary)
- [geoserver-1.7.0-RC4-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/geoserver-1.7.0-RC4-src.zip/download) (Source code)
- [geoserver-1.7.0-RC4-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/geoserver-1.7.0-RC4-war.zip/download) (Web archive)

#### [Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/extensions/)

**DataStore Extensions**

- [GeoWebCache](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/extensions/geoserver-1.7.0-RC4-gwc-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/extensions/geoserver-1.7.0-RC4-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/extensions/geoserver-1.7.0-RC4-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/extensions/geoserver-1.7.0-RC4-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/extensions/geoserver-1.7.0-RC4-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/extensions/geoserver-1.7.0-RC4-vpf-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/extensions/geoserver-1.7.0-RC4-wfsv-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/extensions/geoserver-1.7.0-RC4-oracle-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/extensions/geoserver-1.7.0-RC4-h2-plugin.zip/download)

**Coverage Extensions**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/extensions/geoserver-1.7.0-RC4-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC4/extensions/geoserver-1.7.0-RC4-pyramid-plugin.zip/download)

## Release notes

Improvement:

* [GEOS-2262](https://osgeo-org.atlassian.net/browse/GEOS-2262) GeoJSON output format does not use the set server character set
* [GEOS-2266](https://osgeo-org.atlassian.net/browse/GEOS-2266) add some kml tests

Bug:

* [GEOS-2258](https://osgeo-org.atlassian.net/browse/GEOS-2258) kml reflector produces links with bounding box
* [GEOS-2259](https://osgeo-org.atlassian.net/browse/GEOS-2259) SRS handling not saved to info.xml
* [GEOS-2265](https://osgeo-org.atlassian.net/browse/GEOS-2265) SchemaIndex in xml parser / encoder leaks memory
* [GEOS-2268](https://osgeo-org.atlassian.net/browse/GEOS-2268) request to kml reflector on a remote server gives back a networklink to localhost
* [GEOS-2275](https://osgeo-org.atlassian.net/browse/GEOS-2275) WMS reprojection failures
