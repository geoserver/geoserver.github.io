---
author: Chris Holmes
date: 2006-10-16
layout: post
link: http://docs.codehaus.org/display/GEOS/2006/10/16/GeoServer+1.4.0-RC1+Released%21
wayback: https://web.archive.org/web/20061029015142/http://docs.codehaus.org:80/display/GEOS/2006/10/16/
title: "GeoServer 1.4.0-RC1 Released!"
categories:
- Announcements
---

The GeoServer team is proud to announce the first release candidate of the 1.4 series. You can download the release below. The big push of 1.4.0 is the transition of GeoServer's architecture to [Spring](http://www.springframework.org/) to be more programmer friendly, allowing modular addition of new plug-in services. There are also improvements for KML, [OSCache](https://web.archive.org/web/20061016/http://docs.codehaus.org/display/GEOSDOC/Caching) integration, fixes for Out of Memory errors, filters directly in WMS requests, and many more.

Other nice improvements include GML2-GZIP and Shapefile output fixes, ability to include metadata urls, proper mime type output, transparent PDF output and proper contact info in the WMS.

The full list is in the [release notes](#release-notes) below.

----

The GeoServer 1.4.0-RC1 beta release is available for download from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC1/):

#### Docs

- [Release Notes](#release-notes)
- [geoserver-1.4.0-RC1a-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC1/geoserver-1.4.0-RC1a-doc.zip/download)
- [geoserver-1.4.0-RC1a-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC1/geoserver-1.4.0-RC1a-javadoc.zip/download)

#### Deployment

- [geoserver-1.4.0-RC1a-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC1/geoserver-1.4.0-RC1a-war.zip/download)
- [geoserver-1.4.0-RC1a-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC1/geoserver-1.4.0-RC1a-bin.zip/download)

#### Windows Installer

- [geoserver-1.4.0-RC1b.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC1/geoserver-1.4.0-RC1b.exe/download)

#### Source Code

- [geoserver-1.4.0-RC1a-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC1/geoserver-1.4.0-RC1a-src.zip/download)

#### DataStore Extensions

[Extensions download page](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/GeoServer%20Extras%201.4.x/)

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/GeoServer%20Extras%201.4.x/arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/GeoServer%20Extras%201.4.x/db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/GeoServer%20Extras%201.4.x/mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/GeoServer%20Extras%201.4.x/vpf-plugin.zip/download)
- [WFS datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/GeoServer%20Extras%201.4.x/wfs-plugin.zip/download)
- [Oracle datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/GeoServer%20Extras%201.4.x/oracle-plugin.zip/download)

Tested with: JBoss, Jetty, Tomcat

GeoServer **[License](https://web.archive.org/web/20061016/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

New Feature:

* [GEOS-712](https://osgeo-org.atlassian.net/browse/GEOS-712) Integrate OSCache for caching wms/wfs responses

Improvement:

* [GEOS-530](https://osgeo-org.atlassian.net/browse/GEOS-530) Improve error messages for disabled WMS/WFS
* [GEOS-605](https://osgeo-org.atlassian.net/browse/GEOS-605) Maven 1.0 to Maven 2.0
* [GEOS-695](https://osgeo-org.atlassian.net/browse/GEOS-695) Spanish translation updated for 1.4.x
* [GEOS-704](https://osgeo-org.atlassian.net/browse/GEOS-704) KML reprojection
* [GEOS-728](https://osgeo-org.atlassian.net/browse/GEOS-728) Move to gt2 2.2.1 once released
* [GEOS-730](https://osgeo-org.atlassian.net/browse/GEOS-730) Improve KML point styling

Bug:

* [GEOS-574](https://osgeo-org.atlassian.net/browse/GEOS-574) Japanese garbage characters in WMS Get Feature Info
* [GEOS-610](https://osgeo-org.atlassian.net/browse/GEOS-610) Configure Metadata URL for Geoserver
* [GEOS-660](https://osgeo-org.atlassian.net/browse/GEOS-660) WFS SHAPE-ZIP results empty
* [GEOS-661](https://osgeo-org.atlassian.net/browse/GEOS-661) SHAPE-ZIP returns empty files when real files do exist
* [GEOS-680](https://osgeo-org.atlassian.net/browse/GEOS-680) SLD Editor Images not working in war
* [GEOS-692](https://osgeo-org.atlassian.net/browse/GEOS-692) GML2-GZIP output not working
* [GEOS-693](https://osgeo-org.atlassian.net/browse/GEOS-693) GeoServer.getMimeType() returns incorect Charset name
* [GEOS-709](https://osgeo-org.atlassian.net/browse/GEOS-709) Transparent PDF not generating with transparent background
* [GEOS-715](https://osgeo-org.atlassian.net/browse/GEOS-715) Shapefile big decimal error
* [GEOS-721](https://osgeo-org.atlassian.net/browse/GEOS-721) Contact info not included in capabilities document
* [GEOS-729](https://osgeo-org.atlassian.net/browse/GEOS-729) Geoserver crashes with OOM after WMS stress testing
* [GEOS-731](https://osgeo-org.atlassian.net/browse/GEOS-731) GeoServer should not require primary keys for oracle/db2
* [GEOS-732](https://osgeo-org.atlassian.net/browse/GEOS-732) Data_dirs defined in the web.xml file are not picked up
* [GEOS-733](https://osgeo-org.atlassian.net/browse/GEOS-733) web.xml not loaded properly in binary and windows distributions of 1.4

Task:

* [GEOS-312](https://osgeo-org.atlassian.net/browse/GEOS-312) Complete refactoring aiming to code base modularization
* [GEOS-652](https://osgeo-org.atlassian.net/browse/GEOS-652) Documentation: Writing Guidelines
* [GEOS-678](https://osgeo-org.atlassian.net/browse/GEOS-678) Developer intro

Sub-task:

* [GEOS-724](https://osgeo-org.atlassian.net/browse/GEOS-724) Hexidecimal translation
* [GEOS-725](https://osgeo-org.atlassian.net/browse/GEOS-725) Raster vs vector output
