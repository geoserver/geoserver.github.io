---
author: Jody Garnett
date: 2022-02-24
layout: post
title: GeoServer 2.20.3 Released
categories:
- Announcements
tags:
- Release
release: release_220
version: 2.20.3
jira_version: 16838
---

GeoServer [2.20.3](/release/2.20.3/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.3/geoserver-2.20.3-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.3/geoserver-2.20.3-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.3/GeoServer-2.20.3-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.3/geoserver-2.20.3-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.3/extensions/).

This is a stable release of the 2.20.x series recommended for production systems. This release was made in conjunction with GeoTools 26.3.

### Security Considerations

This release includes several security enhancements and is a recommended upgrade for production systems.

This release includes two improvements limiting Server-side request forgery (SSRF) opportunities:

* [GEOS-10389](https://osgeo-org.atlassian.net/browse/GEOS-10389) Introduce ``ENTITY_RESOLUTION_ALLOWLIST`` parameter to further restrict external entity resolution.

  See the user guide on [external entities resolution](https://docs.geoserver.org/latest/en/user/production/config.html#production-config-external-entities) for instructions on use. Keep in mind that the application schema plugin requires external entity resolution to local files be available. The global setting required by application schema been renamed to [Unrestricted XML External Entity Resolution](https://docs.geoserver.org/latest/en/user/configuration/globalsettings.html#config-globalsettings-external-entities).
  
* [GEOS-10384](https://osgeo-org.atlassian.net/browse/GEOS-10384) Change GetMap to URIKvpParser.
  
  This improvements is used in conjunction with WMS dynamic styling setting [disabling of SLD and SLD_BODY parameters](https://docs.geoserver.org/latest/en/user/services/wms/webadmin.html#disabling-usage-of-dynamic-styling-in-getmap-and-getfeatureinfo-requests). By handling SLD and SLD_BODY as URI values we can avoid [well-known java side-effect](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=4434494) when comparing URL values.

We would like to thank GeoCat for addressing these two issues on behalf of Fisheries and Oceans Canada. If you wish to report a security vulnerability, please visit our website for [instructions on responsible reporting](http://geoserver.org/issues/).

### Improvements and Fixes

Improvements:

* [GEOS-10367](https://osgeo-org.atlassian.net/browse/GEOS-10367) Allow GetTimeSeries to have a maximum times limit separate than WMS max dimensions

Fixes:

* [GEOS-10379](https://osgeo-org.atlassian.net/browse/GEOS-10379) WCS 2.0 requested ScaleSize not being respected when crossing the dateline

* [GEOS-10377](https://osgeo-org.atlassian.net/browse/GEOS-10377) Layers and Layer Groups get default abstract in capabilities document when none set in configuration.

* [GEOS-10373](https://osgeo-org.atlassian.net/browse/GEOS-10373) GetTimeSeries does not work on source data with time ranges

* [GEOS-10362](https://osgeo-org.atlassian.net/browse/GEOS-10362) Username remains in roles.xml after user removal operation

* [GEOS-10316](https://osgeo-org.atlassian.net/browse/GEOS-10316) Regression in 2.20.x: Unable to specify JAVA\_OPTS for startup.sh

* [GEOS-10066](https://osgeo-org.atlassian.net/browse/GEOS-10066) CSS ArrayList class cast exception in layer rendering

* [GEOS-9785](https://osgeo-org.atlassian.net/browse/GEOS-9785) Invalid argument type=null when trying to use gs:Download WPS identifier

* [GEOS-9770](https://osgeo-org.atlassian.net/browse/GEOS-9770) Cascading WMS server sets invalid I and J when using EPSG:3006 on GetFeatureInfo calls

For more information see [2.20.3 release notes](https://github.com/geoserver/geoserver/releases/tag/2.20.3).

## About GeoServer 2.20

Additional information on GeoServer 2.20 series:

* [Log4J2 zero day vulnerability assessment]({% post_url 2021-11-22-logj4-rce-statement %})
* [Internationalization of title and abstract](https://docs.geoserver.org/latest/en/user/services/internationalization/index.html)
* [State of GeoServer 2.20 edition](https://docs.google.com/presentation/d/19Cmld0_VFePh1g4qUSfqNWWB0t-teClFpT3eUqpYGos/edit?usp=sharing)
* [Windows Installer](https://docs.geoserver.org/stable/en/user/installation/win_installer.html) 

Release notes: ( [2.20.3](https://github.com/geoserver/geoserver/releases/tag/2.20.3) \| [2.20.2](https://github.com/geoserver/geoserver/releases/tag/2.20.2) \| [2.20.1](https://github.com/geoserver/geoserver/releases/tag/2.20.1) \| [2.20.0](https://github.com/geoserver/geoserver/releases/tag/2.20.0) \| [2.20-RC](https://github.com/geoserver/geoserver/releases/tag/2.20-RC) )
