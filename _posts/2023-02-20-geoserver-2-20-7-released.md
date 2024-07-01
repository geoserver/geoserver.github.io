---
author: Andrea Aime
date: 2023-02-20
layout: post
title: GeoServer 2.20.7 Released
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_220
version: 2.20.7
jira_version: 16864
---

GeoServer [2.20.7](/release/2.20.7/) release is available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.7/geoserver-2.20.7-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.7/geoserver-2.20.7-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.7/GeoServer-2.20.7-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.7/geoserver-2.20.7-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.7/extensions/).

This series has previously reached end-of-life, with a release being issued to address an urdent security vulnerability. Please apply this upgrade as a mitigation measure only. Upgrade to 2.22.x series for community support.

Thanks to Andrea Aime (GeoSolutions) for making this update available on behalf of the GeoNode project.

This release was made in conjunction with GeoTools 26.7.

### Security Considerations

This release addresses a security vulnerability and is considered an essential upgrade for production systems:

* [CVE-2023-25158 OGC Filter SQL Injection Vulnerabilities](https://github.com/geotools/geotools/security/advisories/GHSA-99c3-qc2q-p94m) (GeoTools)
* [CVE-2023-25157 OGC Filter SQL Injection Vulnerabilities](https://github.com/geoserver/geoserver/security/advisories/GHSA-7g5f-wrx8-5ccf) (GeoServer)

For more information see [OGC Filter Injection Vulnerability Statement]({% post_url 2023-02-20-ogc-filter-injection %}). 

* [GEOT-7302 Escape user inputs in SQL queries](https://osgeo-org.atlassian.net/browse/GEOT-7302)
* [GEOS-10842 JDBCConfig: escape user inputs in SQL queries](https://osgeo-org.atlassian.net/browse/GEOS-10842)
* [GEOS-10839 JDBCConfig: add JDBC Configuration parameter to disable SQL comments and pretty-printing](https://osgeo-org.atlassian.net/browse/GEOS-10839)

**2024-06-30 Update:** The following mitigation has been provided:

* [CVE-2024-36401](https://github.com/geoserver/geoserver/security/advisories/GHSA-6jj6-gm7p-fcvv) Remote Code Execution (RCE) vulnerability in evaluating property name expressions

  A [patch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.7/geoserver-2.20.7-patches.zip/download) (replacing `gt-app-schema`, `gt-complex` and `gt-xsd-core` jars) has been provided by Andrea (GeoSolutions)

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. .


### Improvements and Fixes

For the full list of fixes and improvements, see [2.20.7 release notes](https://github.com/geoserver/geoserver/releases/tag/2.20.7).

## About GeoServer 2.20

Additional information on GeoServer 2.20 series:

* [Log4J2 zero day vulnerability assessment]({% post_url 2021-12-13-logj4-rce-statement %})
* [Internationalization of title and abstract](https://docs.geoserver.org/latest/en/user/services/internationalization/index.html)
* [State of GeoServer 2.20 edition](https://docs.google.com/presentation/d/19Cmld0_VFePh1g4qUSfqNWWB0t-teClFpT3eUqpYGos/edit?usp=sharing)
* [Windows Installer](https://docs.geoserver.org/stable/en/user/installation/win_installer.html) 

Release notes:
( [2.20.7](https://github.com/geoserver/geoserver/releases/tag/2.20.7)
\| [2.20.6](https://github.com/geoserver/geoserver/releases/tag/2.20.6)
\| [2.20.5](https://github.com/geoserver/geoserver/releases/tag/2.20.5)
\| [2.20.4](https://github.com/geoserver/geoserver/releases/tag/2.20.4)
 \| [2.20.3](https://github.com/geoserver/geoserver/releases/tag/2.20.3)
\| [2.20.2](https://github.com/geoserver/geoserver/releases/tag/2.20.2)
 \| [2.20.1](https://github.com/geoserver/geoserver/releases/tag/2.20.1)
\| [2.20.0](https://github.com/geoserver/geoserver/releases/tag/2.20.0)
 \| [2.20-RC](https://github.com/geoserver/geoserver/releases/tag/2.20-RC) )
