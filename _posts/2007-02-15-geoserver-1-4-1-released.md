---
author: Brent Owens
date: 2007-02-15
layout: post
link: http://docs.codehaus.org/display/GEOS/GeoServer+1.4.1
wayback: https://web.archive.org/web/20070814051149/http://docs.codehaus.org:80/display/GEOS/GeoServer+1.4.1
title: "GeoServer 1.4.1 Released"
categories:
- Announcements
---

GeoServer 1.4.1 has been released, check it out below.

----

The GeoServer 1.4.1 release is available for download from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.1/):

#### Docs

- [Task Tracker](#release-notes)
- [geoserver-1.4.1-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.1/geoserver-1.4.1-doc.zip/download)
- [geoserver-1.4.0-RC3-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/geoserver-1.4.0-RC3-javadoc.zip/download)

#### Deployment

- [geoserver-1.4.1-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.1/geoserver-1.4.1-war.zip/download)
- [geoserver-1.4.1-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.1/geoserver-1.4.1-bin.zip/download)

#### Windows Installer

- [geoserver-1.4.1.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.1/geoserver-1.4.1.exe/download)

#### Source Code

- [geoserver-1.4.1-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.1/geoserver-1.4.1-src.zip/download)

#### DataStore Extensions

- [Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.1/extensions/)
- [ArcSDE datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.1/extensions/geoserver-1.4.1-arcsde-plugin.zip/download)
- [GML datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.1/extensions/geoserver-1.4.1-gml-plugin.zip/download)
- [DB2 datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.1/extensions/geoserver-1.4.1-db2-plugin.zip/download)
- [MySQL datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.1/extensions/geoserver-1.4.1-mysql-plugin.zip/download)
- [VPF datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.1/extensions/geoserver-1.4.1-vpf-plugin.zip/download)
- [WFS datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.1/extensions/geoserver-1.4.1-wfs-plugin.zip/download)
- [Oracle datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.1/extensions/geoserver-1.4.1-oracle-plugin.zip/download)

#### Extra Plugins

- Server-side [Caching](https://web.archive.org/web/20070215/http://docs.codehaus.org/display/GEOSDOC/Caching). Especially useful for tiling clients such as OpenLayers or Google Maps.
- [Windows Service Wrapper](https://web.archive.org/web/20070215/http://docs.codehaus.org/display/GEOSDOC/Windows+Service+Wrapper): Run GeoServer as a service.

Tested with: JBoss, Jetty, Tomcat, WebLogic

GeoServer **[License](https://web.archive.org/web/20070215/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

Improvement:

* [GEOS-441](https://osgeo-org.atlassian.net/browse/GEOS-441) Handling Post requests from a form
* [GEOS-864](https://osgeo-org.atlassian.net/browse/GEOS-864) GetStyles and PutStyles are not included in the capabilities document

Bug:

* [GEOS-734](https://osgeo-org.atlassian.net/browse/GEOS-734) Using minimal configuration triggers all sorts of errors
* [GEOS-825](https://osgeo-org.atlassian.net/browse/GEOS-825) InlineFeatures in SLD-POST not rendering
* [GEOS-846](https://osgeo-org.atlassian.net/browse/GEOS-846) BasicFidMapper generated keys are not valid FIDs
* [GEOS-853](https://osgeo-org.atlassian.net/browse/GEOS-853) Geoserver cannot handle files outside the data dir anymore
* [GEOS-855](https://osgeo-org.atlassian.net/browse/GEOS-855) BaseMap layers overwrite other layers as well
* [GEOS-866](https://osgeo-org.atlassian.net/browse/GEOS-866) Update old links on welcome.do page
* [GEOS-871](https://osgeo-org.atlassian.net/browse/GEOS-871) Map preview does not work with projected data, and shows distorted maps with unprojected ones
* [GEOS-874](https://osgeo-org.atlassian.net/browse/GEOS-874) GetMap requests specifying SLD=url in place of LAYERS= and STYLES= don't work.
* [GEOS-883](https://osgeo-org.atlassian.net/browse/GEOS-883) Scale computation does not conform to OGC standard
* [GEOS-893](https://osgeo-org.atlassian.net/browse/GEOS-893) Misconfigured datastore prevents geoserver startup
* [GEOS-897](https://osgeo-org.atlassian.net/browse/GEOS-897) Have GeoServerDataDirectory support prehistoric external data dir

Task:

* [GEOS-722](https://osgeo-org.atlassian.net/browse/GEOS-722) Write Junit tests for KML

Sub-task:

* [GEOS-723](https://osgeo-org.atlassian.net/browse/GEOS-723) KML Decimal precision
