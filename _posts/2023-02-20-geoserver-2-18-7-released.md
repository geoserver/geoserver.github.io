---
author: Andrea Aime
date: 2023-02-20
layout: post
title: GeoServer 2.18.7 Released
categories:
- Announcements
tags:
- Release
release: release_218
version: 2.18.7
jira_version: 16850
---

GeoServer [2.18.7](/release/2.18.7/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.7/geoserver-2.18.7-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.7/geoserver-2.18.7-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.7/GeoServer-2.18.7-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.7/geoserver-2.18.7-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.7/extensions/).

This series has previously reached end-of-life, with an extra maintenance release being issued to address an urgent security vulnerability. Please apply this upgrade as a mitigation measure only. Upgrade to 2.22.x series for community support.

Thanks to Andrea Aime (GeoSolutions) for making this update available on behalf of GeoSolutions customers.

This release was made in conjunction with GeoTools 24.7.

### Security Considerations

This release addresses a security vulnerability and is considered an essential upgrade for production systems:

* [CVE-2023-25158 OGC Filter SQL Injection Vulnerabilities](https://github.com/geotools/geotools/security/advisories/GHSA-99c3-qc2q-p94m) (GeoTools)
* [CVE-2023-25157 OGC Filter SQL Injection Vulnerabilities](https://github.com/geoserver/geoserver/security/advisories/GHSA-7g5f-wrx8-5ccf) (GeoServer)

For more information see [OGC Filter Injection Vulnerability Statement]({% post_url 2023-02-20-ogc-filter-injection %}). 

* [GEOT-7302 Escape user inputs in SQL queries](https://osgeo-org.atlassian.net/browse/GEOT-7302)
* [GEOS-10842 JDBCConfig: escape user inputs in SQL queries](https://osgeo-org.atlassian.net/browse/GEOS-10842)
* [GEOS-10839 JDBCConfig: add JDBC Configuration parameter to disable SQL comments and pretty-printing](https://osgeo-org.atlassian.net/browse/GEOS-10839)

### Improvements and Fixes

For more information see [2.18.7 release notes](https://github.com/geoserver/geoserver/releases/tag/2.18.7).

## About GeoServer 2.18

Additional information on GeoServer 2.18 series:

* [Jiffle and GeoTools RCE vulnerabilities]({% post_url 2022-04-11-geoserver-2-jiffle-jndi-rce %})
* [Log4J2 zero day vulnerability assessment]({% post_url 2021-12-13-logj4-rce-statement %})  
* State of GeoServer 2.18 ([slides](https://docs.google.com/presentation/d/1Q0pHRUcvucAuHDeZPoeDJG4UY5izwbqo8ZawUdk9xYM/edit?usp=sharing))
* GeoServer Orientation ([slides](https://t.co/fvBTLMia6f?amp=1)|[video](https://youtu.be/bdkk5eVR674))

Release Notes
( [2.18.7](https://github.com/geoserver/geoserver/releases/tag/2.18.7)
\| [2.18.6](https://github.com/geoserver/geoserver/releases/tag/2.18.6)
\| [2.18.5](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16822)
\| [2.18.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16819)
\| [2.18.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16808)
\| [2.18.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16803)
\| [2.18.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16800)
\| [2.18.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16796)
\| [2.18-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16783) )
