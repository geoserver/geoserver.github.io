---
author: Brent Owens
date: 2005-11-17
layout: post
link: http://docs.codehaus.org/display/GEOS/GeoServer+1.3.0-RC6
wayback: https://web.archive.org/web/20060624095003/http://docs.codehaus.org:80/display/GEOS/GeoServer+1.3.0-RC6
title: "GeoServer 1.3.0-RC6 Released"
categories:
- Announcements
---

GeoServer 1.3.0-RC6 has been released, check it out below.

----

The release candiate GeoServer 1.3.0-RC6 is available for testing from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC6/):

#### Docs

- [Release Notes](#release-notes)
- [geoserver-1.3.0-RC6-docs.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC6/geoserver-1.3.0-RC6-docs.zip/download)

#### Deployment

- [geoserver-1.3.0-RC6-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC6/geoserver-1.3.0-RC6-war.zip/download)
- [geoserver-1.3.0-RC6-bin.tar.gz](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC6/geoserver-1.3.0-RC6-bin.tar.gz/download)

#### Windows Installer

- [geoserver-1.3.0-RC6.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC6/geoserver-1.3.0-RC6.exe/download)

#### Source Code

- [geoserver-1.3.0-RC6-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC6/geoserver-1.3.0-RC6-src.zip/download)

Tested with: Jetty, Tomcat

GeoServer **[License](https://web.archive.org/web/20051117/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

New Feature:

* [GEOS-422](https://osgeo-org.atlassian.net/browse/GEOS-422) Default SLD
* [GEOS-430](https://osgeo-org.atlassian.net/browse/GEOS-430) handle html-based form POST

Improvement:

* [GEOS-440](https://osgeo-org.atlassian.net/browse/GEOS-440) The SLD_BODY input stream is using a InputStream implementation with serious non-ascii issues.
* [GEOS-450](https://osgeo-org.atlassian.net/browse/GEOS-450) citeConformanceHack option should set gmlPrefixing as well

Bug:

* [GEOS-325](https://osgeo-org.atlassian.net/browse/GEOS-325) DescribeResponse doesn't support booleans
* [GEOS-362](https://osgeo-org.atlassian.net/browse/GEOS-362) PostGIS without GEOS
* [GEOS-396](https://osgeo-org.atlassian.net/browse/GEOS-396) Demo's don't work. MapBuild No Work - Socket Service Exception
* [GEOS-426](https://osgeo-org.atlassian.net/browse/GEOS-426) Fast SVG Renderer only handles concrete Geometry types.
* [GEOS-427](https://osgeo-org.atlassian.net/browse/GEOS-427) Batik SVG Renderer requires internet connection
* [GEOS-437](https://osgeo-org.atlassian.net/browse/GEOS-437) Multipoints not getting into GML output
* [GEOS-444](https://osgeo-org.atlassian.net/browse/GEOS-444) URL encoding
* [GEOS-445](https://osgeo-org.atlassian.net/browse/GEOS-445) GetFeatureInfo -- html not closing body/html
* [GEOS-446](https://osgeo-org.atlassian.net/browse/GEOS-446) Faulty  VPF datastore factory can cause errors in shapefiles

Wish:

* [GEOS-436](https://osgeo-org.atlassian.net/browse/GEOS-436) boundedBy element per featureMember
