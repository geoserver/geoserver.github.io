---
author: Justin Deoliveira
date: 2007-04-04
layout: post
link: http://docs.codehaus.org/display/GEOS/GeoServer+1.5.0-RC4
wayback: https://web.archive.org/web/20070817062458/http://docs.codehaus.org:80/display/GEOS/GeoServer+1.5.0-RC4
title: "GeoServer 1.5.0-RC4 Released"
categories:
- Announcements
---

GeoServer 1.5.0-RC4 has been released, check it out below.

----

GeoServer 1.5.0-RC4 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/):

- [Release Notes](#release-notes)
- [geoserver-1.5.0-RC4.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/geoserver-1.5.0-RC4.exe/download)
- [geoserver-1.5.0-RC4-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/geoserver-1.5.0-RC4-javadoc.zip/download)
- [geoserver-1.5.0-RC4-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/geoserver-1.5.0-RC4-bin.zip/download)
- [geoserver-1.5.0-RC4-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/geoserver-1.5.0-RC4-src.zip/download)
- [geoserver-1.5.0-RC4-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/geoserver-1.5.0-RC4-war.zip/download)
- [Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/extensions/)

#### DataStore Extensions

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/extensions/geoserver-1.5.0-RC4-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/extensions/geoserver-1.5.0-RC4-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/extensions/geoserver-1.5.0-RC4-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/extensions/geoserver-1.5.0-RC4-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/extensions/geoserver-1.5.0-RC4-vpf-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/extensions/geoserver-1.5.0-RC4-wfs-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/extensions/geoserver-1.5.0-RC4-oracle-plugin.zip/download)

#### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC4/extensions/geoserver-1.5.0-RC4-pyramid-plugin.zip/download)

Tested with: Jetty, Tomcat

## Release notes

Bug:

* [GEOS-989](https://osgeo-org.atlassian.net/browse/GEOS-989) no crs set when inline feature specified in the SLD parameter of a GET GetMap request
* [GEOS-992](https://osgeo-org.atlassian.net/browse/GEOS-992) KML reflector should not require a 'styles' parameter
* [GEOS-999](https://osgeo-org.atlassian.net/browse/GEOS-999) SLD editor assumes web application context always "geoserver" when building links

Task:

* [GEOS-829](https://osgeo-org.atlassian.net/browse/GEOS-829) Run cite test paying attention to lost connection error messages
* [GEOS-988](https://osgeo-org.atlassian.net/browse/GEOS-988) Updating RUNNING.txt to 1.5
* [GEOS-1009](https://osgeo-org.atlassian.net/browse/GEOS-1009) remove pyramid builder from distribution
