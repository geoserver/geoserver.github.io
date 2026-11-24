---
author: Justin Deoliveira
date: 2005-10-21
layout: post
link: http://docs.codehaus.org/display/GEOS/2005/10/21/Geoserver+1.3.0+RC4+Released
wayback: https://web.archive.org/web/20060716145526/http://docs.codehaus.org:80/display/GEOS/2005/10/21/Geoserver+1.3.0+RC4+Released
title: "Geoserver 1.3.0 RC4 Released"
categories:
- Announcements
---

Geoserver 1.3.0 RC4 has been released, check it out below.

----

The release candiate GeoServer 1.3.0-RC4 is available for testing from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC4/):

#### Docs

- [Release Notes](#release-notes)
- [geoserver-1.3.0-RC4-docs.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC4/geoserver-1.3.0-RC4-docs.zip/download)

#### Deployment

- [geoserver-1.3.0-RC4-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC4/geoserver-1.3.0-RC4-war.zip/download)
- [geoserver-1.3.0-RC4-bin.tar.gz](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC4/geoserver-1.3.0-RC4-bin.tar.gz/download)

#### Windows Installer

- [geoserver-1.3.0.RC4.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC4/geoserver-1.3.0.RC4.exe/download)

#### Source Code

- [geoserver-1.3.0-RC4-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC4/geoserver-1.3.0-RC4-src.zip/download)

Tested with: Jetty, Tomcat

GeoServer **[License](https://web.archive.org/web/20051021/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

Improvement:

* [GEOS-412](https://osgeo-org.atlassian.net/browse/GEOS-412) Default distribution should write logs to disk

Bug:

* [GEOS-258](https://osgeo-org.atlassian.net/browse/GEOS-258) /wfs/GetFeature works not too well with i18n data
* [GEOS-400](https://osgeo-org.atlassian.net/browse/GEOS-400) WMS SVG request doesn't return any results
* [GEOS-413](https://osgeo-org.atlassian.net/browse/GEOS-413) WMS layers looking for config files in default location
* [GEOS-421](https://osgeo-org.atlassian.net/browse/GEOS-421) GetLegendGraphic does not finds the required style in a multiple styles remote SLD document
