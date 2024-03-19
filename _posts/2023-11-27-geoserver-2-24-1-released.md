---
author: Jody Garnett
date: 2023-11-27
layout: post
title: GeoServer 2.24.1 Release
categories:
- Announcements
tags:
- Release
release: release_224
version: 2.24.1
jira_version: 16904
--- 

GeoServer [2.24.1](/release/2.24.1/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.1/geoserver-2.24.1-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.1/geoserver-2.24.1-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.1/GeoServer-2.24.1-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.1/geoserver-2.24.1-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.1/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 2.24.1 is made in conjunction with GeoTools 30.1, and GeoWebCache 1.24.1. 

Thanks to Jody Garnett (GeoCat) for making this release.

## Security Considerations

This release addresses security vulnerabilities and is considered an essential upgrade for production systems.

- [CVE-2023-51444](https://github.com/geoserver/geoserver/security/advisories/GHSA-9v5q-2gwq-q9hq) Arbitrary file upload vulnerability in REST Coverage Store API (High).

-   [CVE-2024-23819](https://github.com/geoserver/geoserver/security/advisories/GHSA-7x76-57fr-m5r5) Stored Cross-Site Scripting (XSS) vulnerability in MapML HTML Page (Moderate).

-   [CVE-2024-23640](https://github.com/geoserver/geoserver/security/advisories/GHSA-fcpm-hchj-mh72) Stored Cross-Site Scripting (XSS) vulnerability in WMS OpenLayers Format (Moderate).

-   [CVE-2024-23821](https://github.com/geoserver/geoserver/security/advisories/GHSA-88wc-fcj9-q3r9) Stored Cross-Site Scripting (XSS) vulnerability in GWC Demos Page (Moderate).

-   [CVE-2024-23643](https://github.com/geoserver/geoserver/security/advisories/GHSA-56r3-f536-5gf7) Stored Cross-Site Scripting (XSS) vulnerability in GWC Seed Form (Moderate).

-   [CVE-2024-23642](https://github.com/geoserver/geoserver/security/advisories/GHSA-fg9v-56hw-g525) Stored Cross-Site Scripting (XSS) vulnerability in Simple SVG Renderer (Moderate).


See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Release notes

Improvement:

* [GEOS-11152](https://osgeo-org.atlassian.net/browse/GEOS-11152) Improve handling special characters in the Simple SVG Renderer
* [GEOS-11153](https://osgeo-org.atlassian.net/browse/GEOS-11153) Improve handling special characters in the WMS OpenLayers Format
* [GEOS-11154](https://osgeo-org.atlassian.net/browse/GEOS-11154) Improve handling special characters in the MapML HTML Page
* [GEOS-11155](https://osgeo-org.atlassian.net/browse/GEOS-11155) Add the X-Content-Type-Options header
* [GEOS-11173](https://osgeo-org.atlassian.net/browse/GEOS-11173) Default to using HttpOnly session cookies
* [GEOS-11176](https://osgeo-org.atlassian.net/browse/GEOS-11176) Add validation to file wrapper resource paths
* [GEOS-11188](https://osgeo-org.atlassian.net/browse/GEOS-11188) Let DownloadProcess handle download requests whose pixel size is larger than integer limits
* [GEOS-11189](https://osgeo-org.atlassian.net/browse/GEOS-11189) Add an option to throw a service exception when nearest match "allowed interval" is exceeded
* [GEOS-11193](https://osgeo-org.atlassian.net/browse/GEOS-11193) Add an option to throw an exception when the time nearest match does not fall within search limits

Bug:

* [GEOS-11074](https://osgeo-org.atlassian.net/browse/GEOS-11074) GeoFence may not load property file at boot
* [GEOS-11166](https://osgeo-org.atlassian.net/browse/GEOS-11166) OGC API Maps HTML representation fail without datetime parameter
* [GEOS-11184](https://osgeo-org.atlassian.net/browse/GEOS-11184) ncwms module has a compile dependency on gs-web-core test jar 
* [GEOS-11190](https://osgeo-org.atlassian.net/browse/GEOS-11190) GeoFence: align log4j2 deps
* [GEOS-11196](https://osgeo-org.atlassian.net/browse/GEOS-11196) NPE in VectorDownload if ROI not defined
* [GEOS-11200](https://osgeo-org.atlassian.net/browse/GEOS-11200) GetFeatureInfo can fail on rendering transformations that generate a different raster
* [GEOS-11203](https://osgeo-org.atlassian.net/browse/GEOS-11203) WMS GetFeatureInfo bad WKT exception for label-geometry
* [GEOS-11206](https://osgeo-org.atlassian.net/browse/GEOS-11206) Throw nearest match mismatch exceptions only for WMS

For the complete list see [2.24.1](https://github.com/geoserver/geoserver/releases/tag/2.24.1) release notes. 

## Community Module Updates

### OAuth2 OpenID-Connect improvements

Two improvements have been made to the community module for OAuth2 OpenID-Connect authentication:

* [GEOS-11209](https://osgeo-org.atlassian.net/browse/GEOS-11209) Open ID Connect Proof Key of Code Exchange (PKCE)
* [GEOS-11212](https://osgeo-org.atlassian.net/browse/GEOS-11212) OIDC accessToken verification using only JWKs URI

In addition the module includes an ``OIDC_LOGGING`` profile and [updated documentation](https://docs.geoserver.org/stable/en/user/community/oauth2/oidc.html) covering new settings and troubleshooting guidance.

Thanks Jody Garnett for these improvements on behalf of GeoBeyond.

note: Over the course of 2024 the OAuth2 plugins will [need to be rewritten](https://github.com/geoserver/geoserver/wiki/Jakarta-EE) for spring-framework 6. Interested parties are encouraged to reach out to geoserver-devel email list; ideally we would like to see this functionality implemented and included as part of GeoServer.

# About GeoServer 2.24 Series

Additional information on GeoServer 2.24 series:

* [GeoServer 2.24 User Manual](https://docs.geoserver.org/2.24.x/en/user/)
* [State of GeoServer 2.24](https://docs.google.com/presentation/d/1clOEsaUBzVVXZqCUHWvbyxPRAgRjSbmsOtCk06Zi068/edit?usp=share_link) (foss4g-na presentation)
* [Control remote HTTP requests sent by GeoTools/GeoServer](https://github.com/geoserver/geoserver/wiki/GSIP-218)
* [Multiple CRS authority support, planetary CRS](https://github.com/geoserver/geoserver/wiki/GSIP-219)
* [Extensive GeoServer Printing improvements](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html)
* [Upgraded security policy](https://github.com/geoserver/geoserver/wiki/GSIP-220)

Release notes:
( [2.24.1](https://github.com/geoserver/geoserver/releases/tag/2.24.1)
| [2.24.0](https://github.com/geoserver/geoserver/releases/tag/2.24.0)
| [2.24-RC](https://github.com/geoserver/geoserver/releases/tag/2.24-RC)
) 

GeoServer is an [Open Source Geospatial Foundation](https://www.osgeo.org/projects/geoserver/) project supported by a mix of volunteer and [service provider](https://geoserver.org/support/) activity. We reply on [sponsorship](https://geoserver.org/sponsor/) to fund activities beyond the reach of individual contributors.
