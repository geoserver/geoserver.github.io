---
author: Andrea Aime
date: 2023-02-20
layout: post
title: GeoServer 2.19.7 Released
categories:
- Announcements
tags:
- Release
release: release_219
version: 2.19.7
jira_version: 16845
---

GeoServer [2.19.7](/release/2.19.7/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.7/geoserver-2.19.7-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.7/geoserver-2.19.7-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.7/GeoServer-2.19.7-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.7/geoserver-2.19.7-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.7/extensions/).

This series has previously reached end-of-life, with an extra maintenance release being issued to address an urgent security vulnerability. Please apply this upgrade as a mitigation measure only. Upgrade to 2.22.x series for community support.

Thanks to Andrea Amime (GeoSolutions) for making this update available on behalf of GeoSolutions customers.

This release was made in conjunction with GeoTools 25.7.

### Security Considerations

This release addresses a security vulnerability and is considered an essential upgrade for production systems:

* [CVE-2023-25158 OGC Filter SQL Injection Vulnerabilities](https://github.com/geotools/geotools/security/advisories/GHSA-99c3-qc2q-p94m) (GeoTools)
* [CVE-2023-25157 OGC Filter SQL Injection Vulnerabilities](https://github.com/geoserver/geoserver/security/advisories/GHSA-7g5f-wrx8-5ccf) (GeoServer)

For more information see [OGC Filter Injection Vulnerability Statement]({% post_url 2023-02-20-ogc-filter-injection %}). 

* [GEOT-7302 Escape user inputs in SQL queries](https://osgeo-org.atlassian.net/browse/GEOT-7302)
* [GEOS-10842 JDBCConfig: escape user inputs in SQL queries](https://osgeo-org.atlassian.net/browse/GEOS-10842)
* [GEOS-10839 JDBCConfig: add JDBC Configuration parameter to disable SQL comments and pretty-printing](https://osgeo-org.atlassian.net/browse/GEOS-10839)

### Improvements and Fixes

For more information see [2.19.7 release notes](https://github.com/geoserver/geoserver/releases/tag/2.19.7).

## About GeoServer 2.19

 Additional information on GeoServer 2.19 series:
 
 * [Jiffle and GeoTools RCE vulnerabilities]({% post_url 2022-04-11-geoserver-2-jiffle-jndi-rce %})
 * [Log4J2 zero day vulnerability assessment]({% post_url 2021-12-13-logj4-rce-statement %})
 * [WMS GetFeatureInfo includes labels from ColorMap ](https://docs.geoserver.org/stable/en/user/tutorials/ GetFeatureInfo/raster.html)
 * [Promote WMTS multidim to extension](https://github.com/geoserver/geoserver/wiki/GSIP-196)
 * [Promote WPS-Download to extension](https://github.com/geoserver/geoserver/wiki/GSIP-195)
 * [Promote params-extractor to extension](https://github.com/geoserver/geoserver/wiki/GSIP-194)
 * [Promote GWC-S3 to extension](https://github.com/geoserver/geoserver/wiki/GSIP-193)
 * [Promote WPS-JDBC to extension status](https://github.com/geoserver/geoserver/wiki/GSIP-197)
 * [Promote MapML to extension status](https://github.com/geoserver/geoserver/wiki/GSIP-200)
 * [GeoServer repository transition to main branch](main-branch.html)

Release notes
( [2.19.7](https://github.com/geoserver/geoserver/releases/tag/2.19.7)
\| [2.19.6](https://github.com/geoserver/geoserver/releases/tag/2.19.6)
\| [2.19.5](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16839)
\| [2.19.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16832)
\| [2.19.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16824)
\| [2.19.2](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16821)
\| [2.19.1](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16816)
\| [2.19.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16814)
\| [2.19-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa? projectId=10000&version=16766) )