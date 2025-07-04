---
author: Jody Garnett
date: 2025-05-13
layout: post
title: GeoServer 2.27.1 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_227
version: 2.27.1
jira_version: 17107
--- 

GeoServer [2.27.1](/release/2.27.1/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.1/geoserver-2.27.1-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.1/geoserver-2.27.1-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.1/GeoServer-2.27.1-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.1/geoserver-2.27.1-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.1/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 2.27.1 is made in conjunction with GeoTools 33.1, and GeoWebCache 1.27.1. 

Thanks to Jody Garnett (GeoCat) and Andrea Aime (GeoSolutions) for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is considered an critical update for production systems.

* [CVE-2025-30220](https://github.com/geoserver/geoserver/security/advisories/GHSA-jj54-8f66-c5pc) XML External Entity (XXE) Processing Vulnerability in GeoServer WFS Service (High)

* [CVE-2025-30145](https://github.com/geoserver/geoserver/security/advisories/GHSA-gr67-pwcv-76gf) Denial-of-service (DoS) Vulnerability in Jiffle process (High)  

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

## Define Coverage views using Jiffle expressions

A really powerful new features for those working with coverages. You can now create a coverage using the Jiffle "raster calculator" domain specific language.

<img src="/img/posts/2.27/covearge-jiffle-expression.png" alt="NDVI Coverage View: Jiffle Expression"/>

The use of the CVE system allows the GeoServer team to reach a wider audience than blog posts. For more information please see the [user guide](https://docs.geoserver.org/2.27.x/en/user/data/raster/coverageview.html#jiffle-expressions-to-create-coverage-views). Thanks to Andrea Aime (GeoSolutions) for this new capability.

* [GEOS-11797](https://osgeo-org.atlassian.net/browse/GEOS-11797) Add support for Jiffle expressions in coverage view setup

## Release notes

New Feature:

* [GEOS-11800](https://osgeo-org.atlassian.net/browse/GEOS-11800) Implement GeoServer WPS SpatioTemporalZonalStatistics process

Improvement:

* [GEOS-11793](https://osgeo-org.atlassian.net/browse/GEOS-11793) WPS Read Value from Coverage Position
* [GEOS-11804](https://osgeo-org.atlassian.net/browse/GEOS-11804) Disallow usage of var in GeoServer source code

Bug:

* [GEOS-11274](https://osgeo-org.atlassian.net/browse/GEOS-11274) Cannot get a JSON legend with an external reference to a non published directory
* [GEOS-11751](https://osgeo-org.atlassian.net/browse/GEOS-11751) Symbolizer URL in GetLegendGraphic JSON Request is Broken
* [GEOS-11795](https://osgeo-org.atlassian.net/browse/GEOS-11795) Incorrect clipping of point geometries in vector tiles
* [GEOS-11808](https://osgeo-org.atlassian.net/browse/GEOS-11808) Attribute names containing characters the XML Encoder can't handle are accepted for input, causing errors
* [GEOS-11817](https://osgeo-org.atlassian.net/browse/GEOS-11817) GUI spinner remains after drag and drop
* [GEOS-11818](https://osgeo-org.atlassian.net/browse/GEOS-11818) PageUniqueProcess regression after [GEOT-7628]

Task:

* [GEOS-11825](https://osgeo-org.atlassian.net/browse/GEOS-11825) Random WPS build failure on Github
* [GEOS-11826](https://osgeo-org.atlassian.net/browse/GEOS-11826) Random build failures in gs-metadata when running on Github
* [GEOS-11827](https://osgeo-org.atlassian.net/browse/GEOS-11827) Random build failures in LocalResolvetest when running on github actions
* [GEOS-11828](https://osgeo-org.atlassian.net/browse/GEOS-11828) Random test failures in WFS 2.0 CITE tests, on Github actions

For the complete list see [2.27.1](https://github.com/geoserver/geoserver/releases/tag/2.27.1) release notes. 

## Community Updates

Community module development:

* [GEOS-11816](https://osgeo-org.atlassian.net/browse/GEOS-11816) Features templating OGC API fetch by ID fails

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.27 Series

Additional information on GeoServer 2.27 series:

* [GeoServer 2.27 User Manual](https://docs.geoserver.org/2.27.x/en/user/)
* [GeoServer 2025 Q2 Developer Update]({% post_url 2025-05-13-developer-update %})
* [GeoServer 2025 Roadmap]({% post_url 2025-01-13-roadmap %})
* [Content-Security-Policy Headers](https://github.com/geoserver/geoserver/wiki/GSIP-227)
* [OGCAPI Features Extension](https://github.com/geoserver/geoserver/wiki/GSIP-230)
* [File system access isolation](https://github.com/geoserver/geoserver/wiki/GSIP-229)
* [Promote data dir catalog loader to core](https://github.com/geoserver/geoserver/wiki/GSIP-231)

Release notes:
( [2.27.1](https://github.com/geoserver/geoserver/releases/tag/2.27.1)
| [2.27.0](https://github.com/geoserver/geoserver/releases/tag/2.27.0)
) 

