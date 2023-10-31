---
author: Peter Smythe
date: 2023-10-30
layout: post
title: GeoServer 2.23.3 Release
categories:
- Announcements
tags:
- Release
- Vulnerability
release: release_223
version: 2.23.3
jira_version: 16897
--- 

GeoServer [2.23.3](/release/2.23.3/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.3/geoserver-2.23.3-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.3/geoserver-2.23.3-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.3/GeoServer-2.23.3-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.3/geoserver-2.23.3-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.3/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.
GeoServer 2.23.3 is made in conjunction with GeoTools 29.3, and GeoWebCache 1.23.2. 

Thanks to Peter Smythe (AfriGIS) for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is considered an essential upgrade for production systems.

* [GEOS-11030](/browse/GEOS-11030) Update jetty-server to 9.4.51.v20230217

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

Also, another reminder of the [URL check security setting](https://docs.geoserver.org/maintain/en/user/security/urlchecks.html) that was introduced to series 2.22.x and 2.23.x (but turned off by default) and is now enabled by default for series 2.24.x. If you are not yet in a position to upgrade to 2.24.0 you may wish to enable the recommended setting already.

## Release notes

New Feature:

* [GEOS-11000](https://osgeo-org.atlassian.net//browse/GEOS-11000) WPS process to provide elevation profile for a linestring

Improvement:

* [GEOS-10856](https://osgeo-org.atlassian.net//browse/GEOS-10856) geoserver monitor plugin - scaling troubles
* [GEOS-11081](https://osgeo-org.atlassian.net//browse/GEOS-11081) Add option to disable GetFeatureInfo transforming raster layers
* [GEOS-11087](https://osgeo-org.atlassian.net//browse/GEOS-11087) Fix IsolatedCatalogFacade unnecessary performance overhead
* [GEOS-11089](https://osgeo-org.atlassian.net//browse/GEOS-11089) Performance penalty adding namespaces while loading catalog
* [GEOS-11090](https://osgeo-org.atlassian.net//browse/GEOS-11090) Use Catalog streaming API in WorkspacePage
* [GEOS-11099](https://osgeo-org.atlassian.net//browse/GEOS-11099) ElasticSearch DataStore Documentation Update for RESPONSE_BUFFER_LIMIT
* [GEOS-11100](https://osgeo-org.atlassian.net//browse/GEOS-11100) Add opacity parameter to the layer definitions in WPS-Download download maps
* [GEOS-11102](https://osgeo-org.atlassian.net//browse/GEOS-11102) Allow configuration of the CSV date format
* [GEOS-11114](https://osgeo-org.atlassian.net//browse/GEOS-11114) Improve extensibility in Pre-Authentication scenarios
* [GEOS-11116](https://osgeo-org.atlassian.net//browse/GEOS-11116) GetMap/GetFeatureInfo with groups and view params can with mismatched layers/params
* [GEOS-11120](https://osgeo-org.atlassian.net//browse/GEOS-11120) Create aggregates filterFunction in OSEO to support STAC Datacube extension implementation
* [GEOS-11130](https://osgeo-org.atlassian.net//browse/GEOS-11130) Sort parent role dropdown in Add a new role
* [GEOS-11142](https://osgeo-org.atlassian.net//browse/GEOS-11142) Add mime type mapping for yaml files
* [GEOS-11148](https://osgeo-org.atlassian.net//browse/GEOS-11148) Update response headers for the Resources REST API
* [GEOS-11149](https://osgeo-org.atlassian.net//browse/GEOS-11149) Update response headers for the Style Publisher
* [GEOS-11153](https://osgeo-org.atlassian.net//browse/GEOS-11153) Improve handling special characters in the WMS OpenLayers Format
* [GEOS-11155](https://osgeo-org.atlassian.net//browse/GEOS-11155) Add the X-Content-Type-Options header

Bug:

* [GEOS-10452](https://osgeo-org.atlassian.net//browse/GEOS-10452) Use of Active Directory authorisation seems broken since 2.15.2 (LDAP still works)
* [GEOS-11032](https://osgeo-org.atlassian.net//browse/GEOS-11032) Unlucky init order with GeoWebCacheExtension  gwcFacade before DiskQuotaMonitor
* [GEOS-11138](https://osgeo-org.atlassian.net//browse/GEOS-11138) Jetty unable to start  cvc-elt.1.a / org.xml.sax.SAXParseException
* [GEOS-11140](https://osgeo-org.atlassian.net//browse/GEOS-11140) WPS download can leak image references in the RasterCleaner
* [GEOS-11145](https://osgeo-org.atlassian.net//browse/GEOS-11145) The GUI "wait spinner" is not visible any longer
* [GEOS-11166](https://osgeo-org.atlassian.net//browse/GEOS-11166) OGC API Maps HTML representation fail without datetime parameter

Task:

* [GEOS-10248](https://osgeo-org.atlassian.net//browse/GEOS-10248) WPSInitializer NPE failure during GeoServer reload
* [GEOS-11030](https://osgeo-org.atlassian.net//browse/GEOS-11030) Update jetty-server to 9.4.51.v20230217
* [GEOS-11084](https://osgeo-org.atlassian.net//browse/GEOS-11084) Update text field css styling to look visually distinct
* [GEOS-11091](https://osgeo-org.atlassian.net//browse/GEOS-11091) Upgrade spring-security to 5.7.10
* [GEOS-11092](https://osgeo-org.atlassian.net//browse/GEOS-11092) acme-ldap.jar is compiled with Java 8
* [GEOS-11094](https://osgeo-org.atlassian.net//browse/GEOS-11094) Bump org.hsqldb:hsqldb:2.7.1 to 2.7.2
* [GEOS-11124](https://osgeo-org.atlassian.net//browse/GEOS-11124) Update json dependency to 20230227 in geowebcache-rest
* [GEOS-11141](https://osgeo-org.atlassian.net//browse/GEOS-11141) production consideration for logging configuration hardening

For the complete list see [2.23.3](https://github.com/geoserver/geoserver/releases/tag/2.23.3) release notes. 

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
( [2.23.3](https://github.com/geoserver/geoserver/releases/tag/2.23.3)
| [2.23.2](https://github.com/geoserver/geoserver/releases/tag/2.23.2)
| [2.23.1](https://github.com/geoserver/geoserver/releases/tag/2.23.1)
| [2.23.0](https://github.com/geoserver/geoserver/releases/tag/2.23.0)
| [2.23-RC1](https://github.com/geoserver/geoserver/releases/tag/2.23-RC1)
) 

