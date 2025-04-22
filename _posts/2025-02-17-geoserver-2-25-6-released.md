---
author: Peter Smythe
date: 2025-02-17
layout: post
title: GeoServer 2.25.6 Release
categories:
- Announcements
tags:
- Release
release: release_225
version: 2.25.6
jira_version: 17008
--- 

GeoServer [2.25.6](/release/2.25.6/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.6/geoserver-2.25.6-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.6/geoserver-2.25.6-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.6/GeoServer-2.25.6-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.6/geoserver-2.25.6-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.6/extensions/).

This series has now reached end-of-life, and it is recommended to plan an upgrade to 2.26.x or the upcoming 2.27.0 soon.  
GeoServer 2.25.6 is made in conjunction with GeoTools 31.6, and GeoWebCache 1.25.4. 

Thanks to Jody Garnett (GeoCat) and Andrea Aime (GeoSolutions) for making this release. 

## Security Considerations

This release addresses several security vulnerabilities, and is a recommended upgrade for production systems.

* [CVE-2025-27505](https://github.com/geoserver/geoserver/security/advisories/GHSA-h86g-x8mm-78m5) Missing Authorization on REST API Index (Moderate 5.3)

* [CVE-2024-38524](https://github.com/geoserver/geoserver/security/advisories/GHSA-jm79-7xhw-6f6f) GWC Home Page exposes sensitive server information (Moderate 5.3)

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Release notes

Improvement:

* [GEOS-11651](https://osgeo-org.atlassian.net/browse/GEOS-11651) Support env parametrization on OIDC filter
* [GEOS-11652](https://osgeo-org.atlassian.net/browse/GEOS-11652) Externalize printing configuration folder
* [GEOS-11677](https://osgeo-org.atlassian.net/browse/GEOS-11677) Hide version info on GWC home page

Bug:

* [GEOS-10844](https://osgeo-org.atlassian.net/browse/GEOS-10844) Exclude xml-apis from build
* [GEOS-11649](https://osgeo-org.atlassian.net/browse/GEOS-11649) welcome page per-layer is not respecting global service enablement 
* [GEOS-11664](https://osgeo-org.atlassian.net/browse/GEOS-11664) Update REST security paths
* [GEOS-11672](https://osgeo-org.atlassian.net/browse/GEOS-11672) GWC virtual services available with empty contents
* [GEOS-11690](https://osgeo-org.atlassian.net/browse/GEOS-11690) Bug in Externalize printing configuration folder
* [GEOS-11694](https://osgeo-org.atlassian.net/browse/GEOS-11694) OpenID connect: allow caching authentication when an expiration is declared in the access token
* [GEOS-11696](https://osgeo-org.atlassian.net/browse/GEOS-11696) AdminRequestCallback not loaded due to spring bean name conflict
* [GEOS-11700](https://osgeo-org.atlassian.net/browse/GEOS-11700) GeoFence fails in recognizing some caller IP address
* [GEOS-11707](https://osgeo-org.atlassian.net/browse/GEOS-11707) Ogr2OgrWfsTest test failures with GDAL 3.10.1
* [GEOS-11711](https://osgeo-org.atlassian.net/browse/GEOS-11711) Clickhouse DGGS stores fails to aggregate on dates
* [GEOS-11713](https://osgeo-org.atlassian.net/browse/GEOS-11713) Concurrent LDAP builds fail on Jenkins
* [GEOS-11715](https://osgeo-org.atlassian.net/browse/GEOS-11715) STAC sortby won't work with "properties." prefixed names
* [GEOS-11716](https://osgeo-org.atlassian.net/browse/GEOS-11716) WFS POST requests fail if a layer is misconfigured

Task:

* [GEOS-11650](https://osgeo-org.atlassian.net/browse/GEOS-11650) Update dependencies for monitoring-kafka module
* [GEOS-11659](https://osgeo-org.atlassian.net/browse/GEOS-11659) Apply Palantir Java format on GeoServer
* [GEOS-11671](https://osgeo-org.atlassian.net/browse/GEOS-11671) Upgrade H3 dependency to 3.7.3
* [GEOS-11682](https://osgeo-org.atlassian.net/browse/GEOS-11682) Add tests for WMS SLD XML request reader
* [GEOS-11685](https://osgeo-org.atlassian.net/browse/GEOS-11685) Bump jetty.version from 9.4.56.v20240826 to 9.4.57.v20241219
* [GEOS-11701](https://osgeo-org.atlassian.net/browse/GEOS-11701) Update JAI-Ext to 1.1.28

For the complete list see [2.25.6](https://github.com/geoserver/geoserver/releases/tag/2.25.6) release notes. 

## Community Updates

Community module development:

* [GEOS-11686](https://osgeo-org.atlassian.net/browse/GEOS-11686) Clickhouse DGGS stores cannot properly read dates
* [GEOS-11687](https://osgeo-org.atlassian.net/browse/GEOS-11687) OGC API packages contain gs-web-core

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.25 Series

Additional information on GeoServer 2.25 series:

* [GeoServer 2.25 User Manual](https://docs.geoserver.org/2.25.x/en/user/)
* [GeoServer 2024 Roadmap Plannings]({% post_url 2024-01-03-roadmap %}) 
* [Raster Attribute Table extension](https://github.com/geoserver/geoserver/wiki/GSIP-222)
* [Individual contributor clarification](https://github.com/geoserver/geoserver/wiki/GSIP-224)

Release notes:
( [2.25.6](https://github.com/geoserver/geoserver/releases/tag/2.25.6)
| [2.25.5](https://github.com/geoserver/geoserver/releases/tag/2.25.5)
| [2.25.4](https://github.com/geoserver/geoserver/releases/tag/2.25.4)
| [2.25.3](https://github.com/geoserver/geoserver/releases/tag/2.25.3)
| [2.25.2](https://github.com/geoserver/geoserver/releases/tag/2.25.2)
| [2.25.1](https://github.com/geoserver/geoserver/releases/tag/2.25.1)
| [2.25.0](https://github.com/geoserver/geoserver/releases/tag/2.25.0)
| [2.25-RC](https://github.com/geoserver/geoserver/releases/tag/2.25-RC)
) 

