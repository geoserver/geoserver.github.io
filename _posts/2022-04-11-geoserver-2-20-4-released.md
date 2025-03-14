---
author: Andrea Aime
date: 2022-04-11
layout: post
title: GeoServer 2.20.4 Released
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_220
version: 2.20.4
jira_version: 16838
---

GeoServer [2.20.4](/release/2.20.4/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.4/geoserver-2.20.4-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.4/geoserver-2.20.4-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.4/GeoServer-2.20.4-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.4/geoserver-2.20.4-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.4/extensions/).

This is a stable release of the 2.20.x series recommended for production systems. This release was made in conjunction with GeoTools 26.4.

Thanks to everyone who contributed, and to Andrea Aime (GeoSolutions) and Jody Garnett (GeoCat) for making this release.


### Security Considerations

This release includes several security enhancements and is a recommended upgrade for production systems.

This release includes two improvements addressing [Jiffle and GeoTools RCE vulnerabilities]({% post_url 2022-04-11-geoserver-2-jiffle-jndi-rce %}):

* [GEOS-10458](https://osgeo-org.atlassian.net/browse/GEOS-10458) Upgrade to JAI-EXT 1.1.22

* [GEOT-7115](https://osgeo-org.atlassian.net/browse/GEOT-7115) Streamline JNDI lookups

This release also includes:

* [GEOS-10445](https://osgeo-org.atlassian.net/browse/GEOS-10445) Upgrade springframework from 5.1.20.RELEASE to 5.2.20.RELEASE
  
  Although GeoServer [assessment]({% post_url 2022-04-01-spring %}) did not identify any issue we have now updated the the spring framework library.

**2024-06-30 Update:** The following mitigation has been provided:

* [CVE-2024-36401](https://github.com/geoserver/geoserver/security/advisories/GHSA-6jj6-gm7p-fcvv) Remote Code Execution (RCE) vulnerability in evaluating property name expressions (Critical)

  [geoserver-2.20.4-patches](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.4/geoserver-2.20.4-patches.zip/download) (replacing `gt-app-schema`, `gt-complex` and `gt-xsd-core` jars) has been provided by Andrea (GeoSolutions)

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

### Add Styles support to LayerGroup

Allows layer group (layer mode `SINGLE` or `OPAQUE`) list alternate styles in addition to the default one. Each alternate style is
defined by a named configuration of layers and styles providing a unique visual representation.

* [GEOS-10252](https://osgeo-org.atlassian.net/browse/GEOS-10252) Add Styles support to LayerGroup
* [GEOS-10274](https://osgeo-org.atlassian.net/browse/GEOS-10274) Geofence follow up LayerGroup Style addition

For more information see [GSIP-205 Add Styles support to LayerGroup](https://github.com/geoserver/geoserver/wiki/GSIP-205) proposa.

### Improvements and Fixes

Improvements:

* [GEOS-10434](https://osgeo-org.atlassian.net/browse/GEOS-10434) Externalized GeoServer environment properties

* [GEOS-10427](https://osgeo-org.atlassian.net/browse/GEOS-10427) Improve access check in ImportProcess

* [GEOS-10409](https://osgeo-org.atlassian.net/browse/GEOS-10409) Improve deletion of WPS Execute input temp files

Fixes:

* [GEOS-10437](https://osgeo-org.atlassian.net/browse/GEOS-10437) Breaking SLD 1.1 style by REST upload

* [GEOS-10419](https://osgeo-org.atlassian.net/browse/GEOS-10419) NullPointerException from GeoServerOAuthAuthenticationFilter

* [GEOS-10418](https://osgeo-org.atlassian.net/browse/GEOS-10418) Bad request sent to GeoFence when matching roles only

* [GEOS-10401](https://osgeo-org.atlassian.net/browse/GEOS-10401) WPS GetExecutionResult doesn't validate the mimetype parameter

* [GEOS-10400](https://osgeo-org.atlassian.net/browse/GEOS-10400) Disabling WMS dynamic styling does not affect GetLegendGraphic requests

* [GEOS-10393](https://osgeo-org.atlassian.net/browse/GEOS-10393) WFS-T deletes the wrong features \(and further BatchManager issues\)

* [GEOS-9978](https://osgeo-org.atlassian.net/browse/GEOS-9978) WMS vendor parameter CLIP - ignores TIME/CQL\_FILTER and other parameters when using with ImageMosaic

Tasks:

* [GEOS-10445](https://osgeo-org.atlassian.net/browse/GEOS-10445) Upgrade springframework from 5.1.20.RELEASE to 5.2.20.RELEASE

* [GEOS-10303](https://osgeo-org.atlassian.net/browse/GEOS-10303) Upgrade to jackson 2.13.2

For more information see [2.20.4 release notes](https://github.com/geoserver/geoserver/releases/tag/2.20.4).

## About GeoServer 2.20

Additional information on GeoServer 2.20 series:

* [Jiffle and GeoTools RCE vulnerabilities]({% post_url 2022-04-11-geoserver-2-jiffle-jndi-rce %})
* [Spring RCE Spring4Shell CVE-2022-22965 assessment]({% post_url 2022-04-01-spring %})
* [Log4J2 zero day vulnerability assessment]({% post_url 2021-12-13-logj4-rce-statement %})
* [Internationalization of title and abstract](https://docs.geoserver.org/latest/en/user/services/internationalization/index.html)
* [State of GeoServer 2.20 edition](https://docs.google.com/presentation/d/19Cmld0_VFePh1g4qUSfqNWWB0t-teClFpT3eUqpYGos/edit?usp=sharing)
* [Windows Installer](https://docs.geoserver.org/stable/en/user/installation/win_installer.html) 

Release notes: ( [2.20.4](https://github.com/geoserver/geoserver/releases/tag/2.20.4)
\| [2.20.3](https://github.com/geoserver/geoserver/releases/tag/2.20.3)
\| [2.20.2](https://github.com/geoserver/geoserver/releases/tag/2.20.2)
\| [2.20.1](https://github.com/geoserver/geoserver/releases/tag/2.20.1)
\| [2.20.0](https://github.com/geoserver/geoserver/releases/tag/2.20.0)
\| [2.20-RC](https://github.com/geoserver/geoserver/releases/tag/2.20-RC) )
