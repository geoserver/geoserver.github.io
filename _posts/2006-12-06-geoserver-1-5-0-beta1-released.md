---
author: Brent Owens
date: 2006-12-06
layout: post
link: http://docs.codehaus.org/display/GEOS/GeoServer+1.5.0+beta1
wayback: https://web.archive.org/web/20070105012400/http://docs.codehaus.org:80/display/GEOS/GeoServer+1.5.0+beta1
title: "GeoServer 1.5.0-beta1 Released"
categories:
- Announcements
---

GeoServer 1.5.0-beta1 has been released, check it out below.

----

The GeoServer 1.5.0 beta1 beta release is available for download from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0-beta1/):\
Thanks to the [Geo-Solutions](http://geo-solutions.it) team for putting all their hard work into this release.

***Notice***: You will need **JAI** and **ImageIO** installed in your JRE in order to run this version of GeoServer. Future versions will contain the jars bundled with the download, and you will not need to manually install them.

#### Docs

- [geoserver-1.5.0-beta1-javadoc.zip](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0-beta1/geoserver-1.5.0-beta1-javadoc.zip/download)
- [Task Tracker](#release-notes)

#### Deployment

- [geoserver-1.5.0-beta1-war.zip](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0-beta1/geoserver-1.5.0-beta1-war.zip/download)
- [geoserver-1.5.0-beta1-bin.zip](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0-beta1/geoserver-1.5.0-beta1-bin.zip/download)

#### Windows Installer

- [geoserver-1.5.0-beta1.exe](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0-beta1/geoserver-1.5.0-beta1.exe/download)

#### Source Code

- [geoserver-1.5.0-beta1-src.zip](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0-beta1/geoserver-1.5.0-beta1-src.zip/download)

#### DataStore Extensions

- [Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/)
- [GML datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-gml-plugin.zip/download)
- [DB2 datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-db2-plugin.zip/download)
- [MySQL datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-mysql-plugin.zip/download)
- [VPF datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-vpf-plugin.zip/download)
- [WFS datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-wfs-plugin.zip/download)
- [Oracle datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-oracle-plugin.zip/download)

#### Extra Plugins

- Server-side [Caching](https://web.archive.org/web/20061206/http://docs.codehaus.org/display/GEOSDOC/Caching). Especially useful for tiling clients such as OpenLayers or Google Maps.
- [Windows Service Wrapper](https://web.archive.org/web/20061206/http://docs.codehaus.org/display/GEOSDOC/Windows+Service+Wrapper): Run GeoServer as a service.

Tested with: JBoss, Jetty, Tomcat, WebLogic

GeoServer **[License](https://web.archive.org/web/20061206/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

Improvement:

* [GEOS-237](https://osgeo-org.atlassian.net/browse/GEOS-237) Raster support in the WMS

Bug:

* [GEOS-624](https://osgeo-org.atlassian.net/browse/GEOS-624) IP Issues
* [GEOS-794](https://osgeo-org.atlassian.net/browse/GEOS-794) Multiple layers in XML-Getmap request aren't rendered

Task:

* [GEOS-708](https://osgeo-org.atlassian.net/browse/GEOS-708) Remove surefire property files from version control
* [GEOS-772](https://osgeo-org.atlassian.net/browse/GEOS-772) Document WMS Path

Sub-task:

* [GEOS-777](https://osgeo-org.atlassian.net/browse/GEOS-777) KMZ to return good file names as well.
* [GEOS-782](https://osgeo-org.atlassian.net/browse/GEOS-782) PDF could use nice names too.

Wish:

* [GEOS-370](https://osgeo-org.atlassian.net/browse/GEOS-370) Run as a Windows Service option (for .exe Windows installer)
