---
author: Brent Owens
date: 2006-08-16
layout: post
link: http://docs.codehaus.org/display/GEOS/2006/08/16/GeoServer+1.4-M1+release
wayback: https://web.archive.org/web/20061019132952/http://docs.codehaus.org:80/display/GEOS/2006/08/16/GeoServer+1.4-M1+release
title: "GeoServer 1.4-M1 release"
categories:
- Announcements
---

The GeoServer team is proud to announce the release of version 1.4-M1.\
This is a milestone release for the new Spring-based architecture that will greatly benefit the project by allowing for community plug-ins. To read about the new architecture head over to the wiki: <https://web.archive.org/web/20060816/http://docs.codehaus.org/display/GEOSDEV/4+Programmers+Guide>

You can download the release here: <https://web.archive.org/web/20061010024811/http://docs.codehaus.org/display/GEOS/GeoServer+1.4-M1>

----

The GeoServer 1.4-M1 release is available for download from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-M1/):

#### Docs

- [Release Notes](#release-notes)
- [geoserver-1.4.0-M1-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-M1/geoserver-1.4.0-M1-javadoc.zip/download)

#### Deployment

- [geoserver-1.4.0-M1-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-M1/geoserver-1.4.0-M1-war.zip/download)
- [geoserver-1.4.0-M1-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-M1/geoserver-1.4.0-M1-bin.zip/download)

#### Windows Installer

- [geoserver-1.4.0-M1.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-M1/geoserver-1.4.0-M1.exe/download)

#### Source Code

- [geoserver-1.4.0-M1-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-M1/geoserver-1.4.0-M1-src.zip/download)

#### DataStore Extensions

[Extensions download page](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/)

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-arcsde-ext1.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-db2-ext.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-mysql-ext.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-vpf-ext.zip/download)
- [WFS datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-wfs-ext.zip/download)
- [Oracle datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-oracle-ext.zip/download)

Tested with: JBoss, Jetty, Tomcat, Resin

GeoServer **[License](https://web.archive.org/web/20060816/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

Improvement:

* [GEOS-633](https://osgeo-org.atlassian.net/browse/GEOS-633) Factor out map producer into Spring extension point
* [GEOS-664](https://osgeo-org.atlassian.net/browse/GEOS-664) Spanish translation of the interface

Bug:

* [GEOS-671](https://osgeo-org.atlassian.net/browse/GEOS-671) UserBasic- WMS preview broken
* [GEOS-672](https://osgeo-org.atlassian.net/browse/GEOS-672) UserBasic- WFS-T demo broken
* [GEOS-673](https://osgeo-org.atlassian.net/browse/GEOS-673) demo request null pointer exception with transactionUpdateGeom
* [GEOS-674](https://osgeo-org.atlassian.net/browse/GEOS-674) Map preview page out of date
* [GEOS-675](https://osgeo-org.atlassian.net/browse/GEOS-675) SLD editor images missing
* [GEOS-676](https://osgeo-org.atlassian.net/browse/GEOS-676) SLD post is broken
* [GEOS-677](https://osgeo-org.atlassian.net/browse/GEOS-677) binary release .bat files broken

Task:

* [GEOS-642](https://osgeo-org.atlassian.net/browse/GEOS-642) Documentation: Maven Quickstart
* [GEOS-643](https://osgeo-org.atlassian.net/browse/GEOS-643) Documentation: Eclipse Quickstart
* [GEOS-644](https://osgeo-org.atlassian.net/browse/GEOS-644) Documentation: GeoServer Architecture
* [GEOS-645](https://osgeo-org.atlassian.net/browse/GEOS-645) Documentation: GeoServer Platform
* [GEOS-646](https://osgeo-org.atlassian.net/browse/GEOS-646) Documentation: A Simple PlugIn
* [GEOS-648](https://osgeo-org.atlassian.net/browse/GEOS-648) Documentation: Modules
* [GEOS-650](https://osgeo-org.atlassian.net/browse/GEOS-650) Documentation: Extension Points
* [GEOS-653](https://osgeo-org.atlassian.net/browse/GEOS-653) Developer Guide TOC
* [GEOS-655](https://osgeo-org.atlassian.net/browse/GEOS-655) Cite Tests
