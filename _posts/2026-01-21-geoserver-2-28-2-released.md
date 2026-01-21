---
author: Gabriel Roldan
date: 2026-01-21
layout: post
title: GeoServer 2.28.2 Release
categories:
- Announcements
tags:
- Release
release: release_228
version: 2.28.2
jira_version: 17604
--- 

GeoServer [2.28.2](/release/2.28.2/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.2/geoserver-2.28.2-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.2/geoserver-2.28.2-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.2/GeoServer-2.28.2-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.2/geoserver-2.28.2-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.2/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 2.28.2 is made in conjunction with GeoTools 34.2, and GeoWebCache 1.28.2. 

Thanks to Gabriel Roldan for making this release. 

## Release notes

Improvement:

* [GEOS-11996](https://osgeo-org.atlassian.net/browse/GEOS-11996) Security for STAC/Opensearch for EO
* [GEOS-12012](https://osgeo-org.atlassian.net/browse/GEOS-12012) Switching CSVPPIO Strategy from ATTRIBUTES_ONLY_STRATEGY to WKT_STRATEGY
* [GEOS-12023](https://osgeo-org.atlassian.net/browse/GEOS-12023) Improve developer logging during catalog resources loading and WMS capabilities requests
* [GEOS-12024](https://osgeo-org.atlassian.net/browse/GEOS-12024) Add Git branch name in GEOSERVER_NODE_OPTS

Bug:

* [GEOS-10509](https://osgeo-org.atlassian.net/browse/GEOS-10509) WFS Request fails when XML POST body is larger than 8kB
* [GEOS-11926](https://osgeo-org.atlassian.net/browse/GEOS-11926) ogcapi plugin makes WFS advertising an outputFormat which is actually unavailable
* [GEOS-11979](https://osgeo-org.atlassian.net/browse/GEOS-11979) CloseableIterators not closed by OGC API Features

Sub-task:


For the complete list see [2.28.2](https://github.com/geoserver/geoserver/releases/tag/2.28.2) release notes. 

## Community Updates

Community module development:

* [GEOS-11947](https://osgeo-org.atlassian.net/browse/GEOS-11947) Add the ability to skip numberMatched in STAC/OpenSearch for EO responses
* [GEOS-12000](https://osgeo-org.atlassian.net/browse/GEOS-12000) Ignore DescribeFeatureType requests without typeName in Features Templating schemas override
* [GEOS-12007](https://osgeo-org.atlassian.net/browse/GEOS-12007) Add AWS credential chain authentication UI and documentation for GeoParquet
* [GEOS-12013](https://osgeo-org.atlassian.net/browse/GEOS-12013) Support vector datasets ingestion in VectorMosaic via REST

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.28 Series

Additional information on GeoServer 2.28 series:

* [GeoServer 2.28 User Manual](https://docs.geoserver.org/2.28.x/en/user/)
* [GeoServer 2025 Q4 Developer Update]({% post_url 2025-10-14-developer-update %})* [Advertise and Enforce Attribute Restrictions](https://github.com/geoserver/geoserver/wiki/GSIP-234)

Release notes:
( [2.28.2](https://github.com/geoserver/geoserver/releases/tag/2.28.2)
| [2.28.1](https://github.com/geoserver/geoserver/releases/tag/2.28.1)
| [2.28.0](https://github.com/geoserver/geoserver/releases/tag/2.28.0)
| [2.28-M0](https://github.com/geoserver/geoserver/releases/tag/2.28-M0)
) 

