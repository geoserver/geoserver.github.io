---
author: Brent Owens
date: 2006-11-10
layout: post
link: http://docs.codehaus.org/display/GEOS/2006/11/10/GeoServer+1.4.0-RC3+released%21
wayback: https://web.archive.org/web/20061130033119/http://docs.codehaus.org:80/display/GEOS/2006/11/10/GeoServer+1.4.0-RC3+released%21
title: "GeoServer 1.4.0-RC3 released!"
categories:
- Announcements
---

The GeoServer team is proud to announce the latest release candidate for the 1.4 series: GeoServer 1.4.0-RC3.\
You can download it below

Some of the major changes are:

- Fixed reverse proxy issues
- Run as a windows service is back
- Avoid wfsdispath\* files accumulation in temp directories
- Shapefile delegate thread safety issues solved, and delegate can now return multiple feature types
- Better names for generated files (shape, gml.gz, pdf, kml)

----

The GeoServer 1.4.0-RC3 beta release is available for download from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/):

#### Docs

- [Release Notes](#release-notes)
- [geoserver-1.4.0-RC3-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/geoserver-1.4.0-RC3-doc.zip/download)
- [geoserver-1.4.0-RC3-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/geoserver-1.4.0-RC3-javadoc.zip/download)

#### Deployment

- [geoserver-1.4.0-RC3-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/geoserver-1.4.0-RC3-war.zip/download)
- [geoserver-1.4.0-RC3-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/geoserver-1.4.0-RC3-bin.zip/download)

#### Windows Installer

- [geoserver-1.4.0-RC3c.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/geoserver-1.4.0-RC3c.exe/download)

#### Source Code

- [geoserver-1.4.0-RC3-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/geoserver-1.4.0-RC3-src.zip/download)

#### DataStore Extensions

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/)

- [GML datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-gml-plugin.zip/download)
- [DB2 datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-db2-plugin.zip/download)
- [MySQL datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-mysql-plugin.zip/download)
- [VPF datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-vpf-plugin.zip/download)
- [WFS datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-wfs-plugin.zip/download)
- [Oracle datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/extras/geoserver-1.4.0-RC3-oracle-plugin.zip/download)

#### Extra Plugins

- Server-side [Caching](https://web.archive.org/web/20061110/http://docs.codehaus.org/display/GEOSDOC/Caching). Especially useful for tiling clients such as OpenLayers or Google Maps.

Tested with: JBoss, Jetty, Tomcat, WebLogic

GeoServer **[**License**](https://web.archive.org/web/20061110/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

Improvement:

* [GEOS-716](https://osgeo-org.atlassian.net/browse/GEOS-716) Put reverse proxy info in to GeoServer global controls
* [GEOS-776](https://osgeo-org.atlassian.net/browse/GEOS-776) Return files named after the feature type when serving compressed gzip or shapefiles

Bug:

* [GEOS-606](https://osgeo-org.atlassian.net/browse/GEOS-606) wfsdispatch -- not cleaning up after itself.
* [GEOS-656](https://osgeo-org.atlassian.net/browse/GEOS-656) SHAPE-ZIP doesn't return multiple featuretype shapefiles
* [GEOS-737](https://osgeo-org.atlassian.net/browse/GEOS-737) Wrong namespace for feature-elements?
* [GEOS-762](https://osgeo-org.atlassian.net/browse/GEOS-762) Could not locate service mapping to: (wfs,TestWfsPost) after GeoServer 1.4.0-RC1 GetFeature request
* [GEOS-786](https://osgeo-org.atlassian.net/browse/GEOS-786) Thread safety problem in shapefile feature response delegate
* [GEOS-787](https://osgeo-org.atlassian.net/browse/GEOS-787) Sample requests and other demos in GeoServer 1.4.0-RC2 do not work

Sub-task:

* [GEOS-777](https://osgeo-org.atlassian.net/browse/GEOS-777) KMZ to return good file names as well.
* [GEOS-782](https://osgeo-org.atlassian.net/browse/GEOS-782) PDF could use nice names too.

Wish:

* [GEOS-370](https://osgeo-org.atlassian.net/browse/GEOS-370) Run as a Windows Service option (for .exe Windows installer)
