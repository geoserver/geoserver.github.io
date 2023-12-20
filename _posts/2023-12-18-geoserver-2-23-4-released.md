---
author: Peter Smythe
date: 2023-12-18
layout: post
title: GeoServer 2.23.4 Release
categories:
- Announcements
tags:
- Release
release: release_223
version: 2.23.4
jira_version: 16906
--- 

GeoServer [2.23.4](/release/2.23.4/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.4/geoserver-2.23.4-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.4/geoserver-2.23.4-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.4/GeoServer-2.23.4-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.4/geoserver-2.23.4-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.4/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.
GeoServer 2.23.4 is made in conjunction with GeoTools 29.4, and GeoWebCache 1.23.3. 

Thanks to Peter Smythe (AfriGIS) for making this release. 

## Release notes

Improvement:

* [GEOS-11152](https://osgeo-org.atlassian.net//browse/GEOS-11152) Improve handling special characters in the Simple SVG Renderer
* [GEOS-11154](https://osgeo-org.atlassian.net//browse/GEOS-11154) Improve handling special characters in the MapML HTML Page
* [GEOS-11176](https://osgeo-org.atlassian.net//browse/GEOS-11176) Add validation to file wrapper resource paths
* [GEOS-11188](https://osgeo-org.atlassian.net//browse/GEOS-11188) Let DownloadProcess handle download requests whose pixel size is larger than integer limits
* [GEOS-11189](https://osgeo-org.atlassian.net//browse/GEOS-11189) Add an option to throw a service exception when nearest match "allowed interval" is exceeded
* [GEOS-11193](https://osgeo-org.atlassian.net//browse/GEOS-11193) Add an option to throw an exception when the time nearest match does not fall within search limits
* [GEOS-11219](https://osgeo-org.atlassian.net//browse/GEOS-11219) Upgrade mail and activation libraries

Bug:

* [GEOS-9757](https://osgeo-org.atlassian.net//browse/GEOS-9757) Return a service exception when client provided WMS dimensions are not a match
* [GEOS-11074](https://osgeo-org.atlassian.net//browse/GEOS-11074) GeoFence may not load property file at boot
* [GEOS-11184](https://osgeo-org.atlassian.net//browse/GEOS-11184) ncwms module has a compile dependency on gs-web-core test jar 
* [GEOS-11190](https://osgeo-org.atlassian.net//browse/GEOS-11190) GeoFence: align log4j2 deps
* [GEOS-11196](https://osgeo-org.atlassian.net//browse/GEOS-11196) NPE in VectorDownload if ROI not defined
* [GEOS-11200](https://osgeo-org.atlassian.net//browse/GEOS-11200) GetFeatureInfo can fail on rendering transformations that generate a different raster
* [GEOS-11203](https://osgeo-org.atlassian.net//browse/GEOS-11203) WMS GetFeatureInfo bad WKT exception for label-geometry
* [GEOS-11206](https://osgeo-org.atlassian.net//browse/GEOS-11206) Throw nearest match mismatch exceptions only for WMS
* [GEOS-11223](https://osgeo-org.atlassian.net//browse/GEOS-11223) Layer not visible in preview/capabilities if security closes the workspace, but allows access to the layer
* [GEOS-11224](https://osgeo-org.atlassian.net//browse/GEOS-11224) Platform independent binary doesn't start properly with default data directory


For the complete list see [2.23.4](https://github.com/geoserver/geoserver/releases/tag/2.23.4) release notes. 

## Community Updates

Community module development:

* [GEOS-11209](/browse/GEOS-11209) Open ID Connect Proof Key of Code Exchange (PKCE)
* [GEOS-11212](/browse/GEOS-11212) ODIC accessToken verification using only JWKs URI

Community moduels are shared as source code to encourage collaboration. If a topic being explored is of interest to you please contact the module developer to offer assistance. 

# About GeoServer 2.23 Series

Additional information on GeoServer 2.23 series:

* [GeoServer 2.23 User Manual](https://docs.geoserver.org/2.23.x/en/user/)
* [Drop Java 8](https://github.com/geoserver/geoserver/wiki/GSIP-215)
* [GUI CSS Cleanup](https://github.com/geoserver/geoserver/wiki/GSIP-213)
* [Add the possibility to use fixed values in Capabilities for Dimension metadata](https://github.com/geoserver/geoserver/wiki/GSIP-208)
* [State of GeoServer 2.23](https://docs.google.com/presentation/d/1nRKIILXWGLMGXZ6thfJgPR9kZ6Wh8Hp1dwZdQGw2YRc/edit?usp=share_link)
* [GeoServer Feature Frenzy 2023](https://docs.google.com/presentation/d/1vE8eCrOyewoH54g8CjuoiO3pxVLToEpuvpoZWmy0wTg/edit?usp=share_link)
* [GeoServer used in fun and interesting ways](https://docs.google.com/presentation/d/1PP2qk7eH8TzAf1tvEWH7Geattd0YFh7ZEDx1_tlrRWY/edit?usp=share_link)
* [GeoServer Orientation](https://docs.google.com/presentation/d/1sh9C4dIkDRnk3quCD1PRYoiJhjI9dqnAdOScJCgQWU8/edit?usp=share_link)

Release notes:
( [2.23.4](https://github.com/geoserver/geoserver/releases/tag/2.23.4)
| [2.23.3](https://github.com/geoserver/geoserver/releases/tag/2.23.3)
| [2.23.2](https://github.com/geoserver/geoserver/releases/tag/2.23.2)
| [2.23.1](https://github.com/geoserver/geoserver/releases/tag/2.23.1)
| [2.23.0](https://github.com/geoserver/geoserver/releases/tag/2.23.0)
| [2.23-RC1](https://github.com/geoserver/geoserver/releases/tag/2.23-RC1)
) 

