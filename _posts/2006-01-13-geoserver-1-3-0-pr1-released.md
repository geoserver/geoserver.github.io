---
author: Brent Owens
date: 2006-01-13
layout: post
link: http://docs.codehaus.org/display/GEOS/GeoServer+1.3.0-PR1
wayback: https://web.archive.org/web/20060624094646/http://docs.codehaus.org:80/display/GEOS/GeoServer+1.3.0-PR1
title: "GeoServer 1.3.0-PR1 Released"
categories:
- Announcements
---

GeoServer 1.3.0-PR1 has been released, check it out below.

----

The pre-release GeoServer 1.3.0-PR1 is available for testing from the *[SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-PR1/)*:

#### Docs

- *[Release Notes](#release-notes)*
- *[geoserver-1.3.0-PR1-docs.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-PR1/geoserver-1.3.0-PR1-docs.zip/download)*

#### Deployment

- *[geoserver-1.3.0-PR1-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-PR1/geoserver-1.3.0-PR1-war.zip/download)*
- *[geoserver-1.3.0-PR1-bin.tar.gz](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-PR1/geoserver-1.3.0-PR1-bin.tar.gz/download)*

#### Windows Installer

- *[geoserver-1.3.0-PR1.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-PR1/geoserver-1.3.0-PR1.exe/download)*

#### Source Code

- *[geoserver-1.3.0-PR1-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-PR1/geoserver-1.3.0-PR1-src.zip/download)*

#### DataStore Extensions

- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-PR1/extensions/geoserver-1.3.0-db2-ext.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-PR1/extensions/geoserver-1.3.0-mysql-ext.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-PR1/extensions/geoserver-1.3.0-vpf-ext.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-PR1/extensions/geoserver-1.3.0-wfs-ext.zip/download)

Tested with: Jetty, Tomcat

GeoServer **[License](https://web.archive.org/web/20060113/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

New Feature:

* [GEOS-371](https://osgeo-org.atlassian.net/browse/GEOS-371) Add GeoTools DB2 plug-in

Improvement:

* [GEOS-447](https://osgeo-org.atlassian.net/browse/GEOS-447) Make it so geoserserver start-up doesn't look like someone yakked.

Bug:

* [GEOS-280](https://osgeo-org.atlassian.net/browse/GEOS-280) "GetCapabilities" does not depend on service-level
* [GEOS-367](https://osgeo-org.atlassian.net/browse/GEOS-367) HTTP Error 500 creating FeatureType on PostGis table inside a schema
* [GEOS-449](https://osgeo-org.atlassian.net/browse/GEOS-449) Postgis mishandles Filter.NONE in removeFeatures()
* [GEOS-469](https://osgeo-org.atlassian.net/browse/GEOS-469) Grabbing inappropriate columns for wms
* [GEOS-475](https://osgeo-org.atlassian.net/browse/GEOS-475) bbox ignored with Batik SVG producer backed by PostgisDataStore
* [GEOS-495](https://osgeo-org.atlassian.net/browse/GEOS-495) IndexedDataStore issues
* [GEOS-497](https://osgeo-org.atlassian.net/browse/GEOS-497) Default Namespace Configuration Parameter does not persist in configuration.
* [GEOS-504](https://osgeo-org.atlassian.net/browse/GEOS-504) Encoding bug for Japanese localization
* [GEOS-508](https://osgeo-org.atlassian.net/browse/GEOS-508) GeoServer: JAI fails
* [GEOS-509](https://osgeo-org.atlassian.net/browse/GEOS-509) Schema validation with data directory
* [GEOS-515](https://osgeo-org.atlassian.net/browse/GEOS-515) WFS transaction fails
* [GEOS-520](https://osgeo-org.atlassian.net/browse/GEOS-520) Generated mapbuilder sample has hardcoded localhost

Task:

* [GEOS-374](https://osgeo-org.atlassian.net/browse/GEOS-374) Commit first working KML version
* [GEOS-472](https://osgeo-org.atlassian.net/browse/GEOS-472) Combine various eclipse set up information
* [GEOS-490](https://osgeo-org.atlassian.net/browse/GEOS-490) Replace userBasic transaction demo requests with ones that work
* [GEOS-512](https://osgeo-org.atlassian.net/browse/GEOS-512) Cut down doc size
* [GEOS-513](https://osgeo-org.atlassian.net/browse/GEOS-513) Documentation overview clean-up
* [GEOS-516](https://osgeo-org.atlassian.net/browse/GEOS-516) Create a datastores extras artifact for 1.3.0 release
