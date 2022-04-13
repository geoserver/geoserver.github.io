---
author: Andrea Aime
date: 2022-04-11
layout: post
title: GeoServer 2.19.6 Released
categories:
- Announcements
tags:
- Release
release: release_219
version: 2.19.6
jira_version: 16843
---

GeoServer [2.19.6](/release/2.19.6/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.6/geoserver-2.19.6-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.6/geoserver-2.19.6-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.6/GeoServer-2.19.6-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.6/geoserver-2.19.6-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.6/extensions/).

This is an extra maintenance release of the 2.19.x series recommended for production systems. This release was made in conjunction with GeoTools 25.6.

Thanks to everyone who contributed, and to Andrea Aime (GeoSolutions) for making this release.

### Security Considerations

This release includes several security enhancements and is a recommended upgrade for production systems.

This release includes two improvements addressing [Jiffle and GeoTools RCE vulnerabilities]({% post_url 2022-04-11-geoserver-2-jiffle-jndi-rce %}):

* [GEOS-10458](https://osgeo-org.atlassian.net/browse/GEOS-10458) Upgrade to JAI-EXT 1.1.22

* [GEOT-7115](https://osgeo-org.atlassian.net/browse/GEOT-7115) Streamline JNDI lookups
  
This release also includes:

* [GEOS-10445](https://osgeo-org.atlassian.net/browse/GEOS-10445) Upgrade springframework from 5.1.20.RELEASE to 5.2.20.RELEASE
  
  Although GeoServer [assessment]({% post_url 2022-04-01-spring %}) did not identify any issue we have now updated the the spring framework library.

### Improvements and Fixes

Fixes:

* [GEOS-10437](https://osgeo-org.atlassian.net/browse/GEOS-10437) Breaking SLD 1.1 style by REST upload

* [GEOS-10336](https://osgeo-org.atlassian.net/browse/GEOS-10336) INSPIRE failure: version not propagated in GetCapabilities LegendURL

* [GEOS-9978](https://osgeo-org.atlassian.net/browse/GEOS-9978) WMS vendor parameter CLIP - ignores TIME/CQL\_FILTER and other parameters when using with ImageMosaic

Tasks:

* [GEOS-10303](https://osgeo-org.atlassian.net/browse/GEOS-10303) Upgrade to jackson 2.13.2

For more information see [2.19.6 release notes](https://github.com/geoserver/geoserver/releases/tag/2.19.6).

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

Release notes ( [2.19.6](https://github.com/geoserver/geoserver/releases/tag/2.19.6)
\| [2.19.5](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16839)
\| [2.19.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16832)
\| [2.19.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16824)
\| [2.19.2](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16821)
\| [2.19.1](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16816)
\| [2.19.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16814)
\| [2.19-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa? projectId=10000&version=16766) )