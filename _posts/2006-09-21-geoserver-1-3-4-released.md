---
author: Brent Owens
date: 2006-09-21
layout: post
link: http://docs.codehaus.org/display/GEOS/2006/09/21/GeoServer+1.3.4+released
wayback: https://web.archive.org/web/20070214030534/http://docs.codehaus.org:80/display/GEOS/2006/09/21/GeoServer+1.3.4+released
title: "GeoServer 1.3.4 released"
categories:
- Announcements
---

The GeoServer team is proud to announce the latest version: 1.3.4.\
It features a new and improved MapBuilder client, more robust SLD support for KML output, and a fix for control over decimal places in returned KML.

You can grab the release below.

----

The GeoServer 1.3.4 release is available for download from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.4/):

#### Docs

- [Release Notes](#release-notes)
- [Task Tracker](http://jira.codehaus.org/browse/GEOS?report=com.atlassian.jira.plugin.system.project:roadmap-panel)
- [geoserver-1.3.4-docs.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.4/geoserver-1.3.4-docs.zip/download)

#### Deployment

- [geoserver-1.3.4a-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.4/geoserver-1.3.4a-war.zip/download)
- [geoserver-1.3.4a-bin.tar.gz](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.4/geoserver-1.3.4a-bin.tar.gz/download)

#### Windows Installer

- [geoserver-1.3.4a.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.4/geoserver-1.3.4a.exe/download)

#### Source Code

- [geoserver-1.3.4a-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.4/geoserver-1.3.4a-src.zip/download)

#### DataStore Extensions

[Extensions download page](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/)

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-arcsde-ext1.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-db2-ext.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-mysql-ext.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-vpf-ext.zip/download)
- [WFS datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-wfs-ext.zip/download)
- [Oracle datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-oracle-ext.zip/download)

Tested with: JBoss, Jetty, Tomcat, Resin

GeoServer **[License](https://web.archive.org/web/20060921/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

Improvement:

* [GEOS-664](https://osgeo-org.atlassian.net/browse/GEOS-664) Spanish translation of the interface

Bug:

* [GEOS-498](https://osgeo-org.atlassian.net/browse/GEOS-498) Japanese localization
* [GEOS-670](https://osgeo-org.atlassian.net/browse/GEOS-670) KML geometry output limited to 4 decimal places
* [GEOS-682](https://osgeo-org.atlassian.net/browse/GEOS-682) KML line style missing from polygon symbolizer
* [GEOS-735](https://osgeo-org.atlassian.net/browse/GEOS-735) The appears to be a virus in the windows 1.3.4 installer.
