---
author: Jody Garnett
date: 2023-02-20
layout: post
title: GeoServer 2.21.4 Release
categories:
- Announcements
tags:
- Release
release: release_2211
version: 2.21.4
jira_version: 16873 
---

GeoServer [2.21.4](/release/2.21.4/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.4/geoserver-2.21.4-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.4/geoserver-2.21.4-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.4/GeoServer-2.21.4-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.4/geoserver-2.21.4-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.4/extensions/).

This is a maintenance release of the GeoServer 2.21.x series, made in conjunction with GeoTools 27.4 
and GeoWebCache 1.21.4.

Thanks to Jody Garnett (GeoCat) for making this release.

### Security Considerations

This release addresses a security vulnerability and is considered an essential upgrade for production systems:

* [CVE-2023-25158 OGC Filter SQL Injection Vulnerabilities](https://github.com/geotools/geotools/security/advisories/GHSA-99c3-qc2q-p94m) (GeoTools)
* [CVE-2023-25157 OGC Filter SQL Injection Vulnerabilities](https://github.com/geoserver/geoserver/security/advisories/GHSA-7g5f-wrx8-5ccf) (GeoServer)

For more information see [OGC Filter Injection Vulnerability Statement]({% post_url 2023-02-20-ogc-filter-injection %}). 

* [GEOT-7302 Escape user inputs in SQL queries](https://osgeo-org.atlassian.net/browse/GEOT-7302)
* [GEOS-10842 Escape user inputs in SQL queries](https://osgeo-org.atlassian.net/browse/GEOS-10842)
* [GEOS-10839 Add JDBC Configuration parameter to disable SQL comments and pretty-printing](https://osgeo-org.atlassian.net/browse/GEOS-10839)

## Community Modules

The JDBC Config module received several important fixes:

* [GEOS-10814](https://osgeo-org.atlassian.net/browse/GEOS-10814) Update jdbc config to use consistent SQL formatting

* [GEOS-10813](https://osgeo-org.atlassian.net/browse/GEOS-10813) jdbc config cache bug

* [GEOS-10829](https://osgeo-org.atlassian.net/browse/GEOS-10829) JDBC Config missing some nested layer properties

* [GEOS-10842](https://osgeo-org.atlassian.net/browse/GEOS-10842) Escape user inputs in SQL queries

## Release notes

Bug:

* [GEOS-7506](https://osgeo-org.atlassian.net/browse/GEOS-7506) shutdown.bat cannot run without JAVA\_HOME set

* [GEOS-10683](https://osgeo-org.atlassian.net/browse/GEOS-10683) FileWrapperResourceTheoryTest fails on Windows since Java 11

* [GEOS-10689](https://osgeo-org.atlassian.net/browse/GEOS-10689) OSHISystemInfoCollector holds non daemon threads, prevents clean shutdown of Tomcat

* [GEOS-10807](https://osgeo-org.atlassian.net/browse/GEOS-10807) LayerGroup with nested group POST rest op fails with null styles attribute

* [GEOS-10817](https://osgeo-org.atlassian.net/browse/GEOS-10817) Features Templating - XML HTML output doesn't escape all html and xml symbols

* [GEOS-10818](https://osgeo-org.atlassian.net/browse/GEOS-10818) Schemaless Property Accessor returns emptylist instead of null for null/not existing properties

* [GEOS-10846](https://osgeo-org.atlassian.net/browse/GEOS-10846) Enable auto-escaping for REST HTML templates

Improvement:

* [GEOS-10816](https://osgeo-org.atlassian.net/browse/GEOS-10816) OGC API Features complex features test fails since introduction of <meta> tag in HTML templates

* [GEOS-10848](https://osgeo-org.atlassian.net/browse/GEOS-10848) Column remarks documentation should be updated to reflect that functionality is supported with JNDI

* [GEOS-10851](https://osgeo-org.atlassian.net/browse/GEOS-10851) GWC S3 Blobstore Parameters  Get Converted back to plain text after an application restart

For complete information see [2.21.4 release notes](https://github.com/geoserver/geoserver/releases/tag/2.21.4).

## About GeoServer 2.21

Additional information on GeoServer 2.21 series:

- [Feature Type Customization](https://github.com/geoserver/geoserver/wiki/GSIP-207)
- [Add Styles support to LayerGroup](https://github.com/geoserver/geoserver/wiki/GSIP-205)
- [Log4j1 update or replace activity]({% post_url 2022-01-20-log4j-upgrade %})

Release notes:
( [2.21.4](https://github.com/geoserver/geoserver/releases/tag/2.21.4)
| [2.21.3](https://github.com/geoserver/geoserver/releases/tag/2.21.3)
| [2.21.2](https://github.com/geoserver/geoserver/releases/tag/2.21.2)
| [2.21.1](https://github.com/geoserver/geoserver/releases/tag/2.21.1)
| [2.21.0](https://github.com/geoserver/geoserver/releases/tag/2.21.0)
| [2.21-RC](https://github.com/geoserver/geoserver/releases/tag/2.21-RC)
)
