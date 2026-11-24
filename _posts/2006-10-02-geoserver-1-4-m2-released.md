---
author: Brent Owens
date: 2006-10-02
layout: post
link: http://docs.codehaus.org/display/GEOS/2006/10/02/GeoServer+1.4-M2+Released
wayback: https://web.archive.org/web/20061025005340/http://docs.codehaus.org:80/display/GEOS/2006/10/02/GeoServer+1.4-M2+Released
title: "GeoServer 1.4-M2 Released"
categories:
- Announcements
---

The GeoServer team is proud to announce the release of 1.4.0 Milestone 2 (beta)!\
You can download it here: <https://web.archive.org/web/20061007110725/http://docs.codehaus.org/display/GEOS/Latest>

Here are the feature changes on the release:

- Upgraded MapBuilder demo version
- WMS Base-map option
- GetFeatureInfo now supports reprojection
- KML Reprojection (also in 1.3.4)

The issue log for this release is here:\
[release notes](#release-notes)

Base on Geotools 2.2.0 (tag = 2.2.0)

----

The GeoServer 1.4-M2 beta release is available for download from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/OldFiles/1.4.0-M2/):

#### Docs

- [Release Notes](#release-notes)
- [geoserver-1.4.0-M2_beta-docs.zip](http://prdownloads.sourceforge.net/geoserver/geoserver-1.4.0-M2_beta-doc.zip?download)
- [geoserver-1.4.0-M2_beta-javadoc.zip](http://prdownloads.sourceforge.net/geoserver/geoserver-1.4.0-M2_beta-javadoc.zip?download)

#### Deployment

- [geoserver-1.4-M2_beta-war.zip](http://prdownloads.sourceforge.net/geoserver/geoserver-1.4.0-M2_beta-war.zip?download)
- [geoserver-1.4-M2_beta-bin.tar.gz](http://prdownloads.sourceforge.net/geoserver/geoserver-1.4.0-M2_beta-bin.zip.zip?download)

#### Windows Installer

- [geoserver-1.4.0-M2.exe](https://sourceforge.net/projects/geoserver/files/OldFiles/1.4.0-M2/geoserver-1.4.0-M2.exe/download)

#### Source Code

- [geoserver-1.4-M2_beta-src.zip](http://prdownloads.sourceforge.net/geoserver/geoserver-1.4.0-M2_beta-src.zip?download)

#### DataStore Extensions

[Extensions download page](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/)

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-arcsde-ext1.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-db2-ext.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-mysql-ext.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-vpf-ext.zip/download)
- [WFS datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-wfs-ext.zip/download)
- [Oracle datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-oracle-ext.zip/download)

Tested with: JBoss, Jetty, Tomcat, Resin

GeoServer **[License](https://web.archive.org/web/20061002/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

Improvement:

* [GEOS-614](https://osgeo-org.atlassian.net/browse/GEOS-614) Upgrade embedded Jetty
* [GEOS-718](https://osgeo-org.atlassian.net/browse/GEOS-718) Improve tiger_roads SLD

Bug:

* [GEOS-706](https://osgeo-org.atlassian.net/browse/GEOS-706) demo data for release missing
* [GEOS-710](https://osgeo-org.atlassian.net/browse/GEOS-710) WMS: version check for GetLegendGraphic is incorrect
* [GEOS-713](https://osgeo-org.atlassian.net/browse/GEOS-713) GetFeatureInfo does not reproject
* [GEOS-714](https://osgeo-org.atlassian.net/browse/GEOS-714) geoserver-1.3.4-war file not deploying on Solaris/Tomcat 5.5.17 - seems to have been built on a PC - has PC formatted path in web.xml for data file - and xml parsing errors
* [GEOS-720](https://osgeo-org.atlassian.net/browse/GEOS-720) WMS GetFeatureInfo should work even if the SRS is not specified in the request

Task:

* [GEOS-651](https://osgeo-org.atlassian.net/browse/GEOS-651) Move 1.4.x developers guide to GEOSOC
