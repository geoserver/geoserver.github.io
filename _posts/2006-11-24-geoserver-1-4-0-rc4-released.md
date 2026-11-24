---
author: Brent Owens
date: 2006-11-24
layout: post
link: http://docs.codehaus.org/display/GEOS/GeoServer+1.4.0-RC4
wayback: https://web.archive.org/web/20061130210609/http://docs.codehaus.org:80/display/GEOS/GeoServer+1.4.0-RC4
title: "GeoServer 1.4.0-RC4 Released"
categories:
- Announcements
---

GeoServer 1.4.0-RC4 has been released, check it out below.

----

The GeoServer 1.4.0-RC4 beta release is available for download from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC4/):

#### Docs

- [Release Notes](#release-notes)
- [Task Tracker](#release-notes)
- [geoserver-1.4.0-RC4-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC4/geoserver-1.4.0-RC4-doc.zip/download)
- [geoserver-1.4.0-RC3-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/geoserver-1.4.0-RC3-javadoc.zip/download)

#### Deployment

- [geoserver-1.4.0-RC4-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC4/geoserver-1.4.0-RC4-war.zip/download)
- [geoserver-1.4.0-RC4-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC4/geoserver-1.4.0-RC4-bin.zip/download)

#### Windows Installer

- [geoserver-1.4.0-RC4.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC4/geoserver-1.4.0-RC4.exe/download)

#### Source Code

- [geoserver-1.4.0-RC4-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC4/geoserver-1.4.0-RC4-src.zip/download)

#### DataStore Extensions

- [Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/)
- [GML datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-gml-plugin.zip/download)
- [DB2 datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-db2-plugin.zip/download)
- [MySQL datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-mysql-plugin.zip/download)
- [VPF datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-vpf-plugin.zip/download)
- [WFS datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-wfs-plugin.zip/download)
- [Oracle datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-oracle-plugin.zip/download)

#### Extra Plugins

- Server-side [Caching](https://web.archive.org/web/20061124/http://docs.codehaus.org/display/GEOSDOC/Caching). Especially useful for tiling clients such as OpenLayers or Google Maps.
- [Windows Service Wrapper](https://web.archive.org/web/20061124/http://docs.codehaus.org/display/GEOSDOC/Windows+Service+Wrapper): Run GeoServer as a service.

Tested with: JBoss, Jetty, Tomcat, WebLogic

GeoServer **[License](https://web.archive.org/web/20061124/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

Improvement:

* [GEOS-797](https://osgeo-org.atlassian.net/browse/GEOS-797) Better error reporting for shape-zip output when there is no geometry

Bug:

* [GEOS-439](https://osgeo-org.atlassian.net/browse/GEOS-439) ERROR in SVG GetMap with Oracle
* [GEOS-789](https://osgeo-org.atlassian.net/browse/GEOS-789) Incorrect results with concurrent users
* [GEOS-793](https://osgeo-org.atlassian.net/browse/GEOS-793) Put windows service wrapper in a separate download.
* [GEOS-795](https://osgeo-org.atlassian.net/browse/GEOS-795) SVG files generated with getmap cannot be seen in Firefox
* [GEOS-796](https://osgeo-org.atlassian.net/browse/GEOS-796) On the fly log level change is not possible anymore in 1.4.0rcX
* [GEOS-798](https://osgeo-org.atlassian.net/browse/GEOS-798) Multiple geometry columns no longer recognized in the renderer
* [GEOS-799](https://osgeo-org.atlassian.net/browse/GEOS-799) conf/ directory should be top level in binary distributions
* [GEOS-801](https://osgeo-org.atlassian.net/browse/GEOS-801) External data dir issues
* [GEOS-803](https://osgeo-org.atlassian.net/browse/GEOS-803) External data dir with /data folder does not work as suggested in the user guide
* [GEOS-804](https://osgeo-org.atlassian.net/browse/GEOS-804) Log4jFormatter does not log exceptions, making server debug really hard
