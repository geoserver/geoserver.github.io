---
author: Ian Turton
date: 2023-05-23
layout: post
title: GeoServer 2.23.1 Release
categories:
- Announcements
tags:
- Release
release: release_223
version: 2.23.1
jira_version: 16888
---

GeoServer [2.23.1](/release/2.23.1/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.1/geoserver-2.23.1-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.1/geoserver-2.23.1-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.1/GeoServer-2.23.1-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.1/geoserver-2.23.1-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.1/extensions/).

This is a stable release of GeoServer suitable for production systems, made in conjunction with GeoTools 29.1 and GeoWebCache 1.23.0.

We are grateful to Ian Turton (Astun Technology Ltd) for making this release. 

# Release notes - GeoServer - 2.23.1

### Bug

[GEOS-8162](https://osgeo-org.atlassian.net/browse/GEOS-8162) CSV Data store does not support relative store paths

[GEOS-10837](https://osgeo-org.atlassian.net/browse/GEOS-10837) geopackage output fails when `java.io.tmpdir` 
on network share

[GEOS-10912](https://osgeo-org.atlassian.net/browse/GEOS-10912) jms-cluster fails to clone grid coverage layer on other nodes

[GEOS-10920](https://osgeo-org.atlassian.net/browse/GEOS-10920) Excel output format packaging misses dependencies, cannot produce .xls

[GEOS-10921](https://osgeo-org.atlassian.net/browse/GEOS-10921) Double escaping of HTML with enabled features-templating

[GEOS-10922](https://osgeo-org.atlassian.net/browse/GEOS-10922) Features templating exception on text/plain format

[GEOS-10932](https://osgeo-org.atlassian.net/browse/GEOS-10932) csw-iso: should only add `'xsi:nil = false'` 
attribute

[GEOS-10934](https://osgeo-org.atlassian.net/browse/GEOS-10934) CSW does not show title/abstract on welcome page

[GEOS-10946](https://osgeo-org.atlassian.net/browse/GEOS-10946) WMS `GetLegendGraphic` throws 
`FootprintsTransformation` cannot be cast to `ProcessFunctionException`

[GEOS-10950](https://osgeo-org.atlassian.net/browse/GEOS-10950) Performance regression in 
`DescribeFeatureType` across all feature types

[GEOS-10955](https://osgeo-org.atlassian.net/browse/GEOS-10955) STAC templates are initialised in the wrong location

[GEOS-10957](https://osgeo-org.atlassian.net/browse/GEOS-10957) Support `ResourceAccessManager` 
implementations returning custom subclasess of `AccessLimits`

[GEOS-10969](https://osgeo-org.atlassian.net/browse/GEOS-10969) Empty `CQL_FILTER` parameter should be ignored

[GEOS-10975](https://osgeo-org.atlassian.net/browse/GEOS-10975) JMS clustering reports error about 
`ReferencedEnvelope` type not being whitelisted in XStream

[GEOS-10985](https://osgeo-org.atlassian.net/browse/GEOS-10985) B/R of GeoServer catalog is broken with GeoServer 2.23.0

### Improvement

[GEOS-10858](https://osgeo-org.atlassian.net/browse/GEOS-10858) jdbc-config turns off isolated workspace support

[GEOS-10898](https://osgeo-org.atlassian.net/browse/GEOS-10898) Preserve key order in STAC responses coming from JSONB columns

[GEOS-10923](https://osgeo-org.atlassian.net/browse/GEOS-10923) Use default writing params on `GeoTIFFPPIO`

[GEOS-10940](https://osgeo-org.atlassian.net/browse/GEOS-10940) Update MapML viewer to release 0.11.0

### Task

[GEOS-10859](https://osgeo-org.atlassian.net/browse/GEOS-10859) OGC API: swagger-api 4.15.5 upgrade

For the complete list see [2.23.1](https://github.com/geoserver/geoserver/releases/tag/2.23.1) release notes.

## About GeoServer 2.23 Series

Release notes:
( 
[2.23.1](https://github.com/geoserver/geoserver/releases/tag/2.23.1)
| [2.23.0](https://github.com/geoserver/geoserver/releases/tag/2.23.0)
| [2.23-RC1](https://github.com/geoserver/geoserver/releases/tag/2.23-RC1)
)

* [Drop Java 8](https://github.com/geoserver/geoserver/wiki/GSIP-215)
* [GUI CSS Cleanup](https://github.com/geoserver/geoserver/wiki/GSIP-213)
* [Add the possibility to use fixed values in Capabilities for Dimension metadata](https://github.com/geoserver/geoserver/wiki/GSIP-208)
