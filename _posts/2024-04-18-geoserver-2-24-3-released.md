---
author: Andrea Aime
date: 2024-04-18
layout: post
title: GeoServer 2.24.3 Release
categories:
- Announcements
tags:
- Release
release: release_224
version: 2.24.3
jira_version: 16912
--- 

GeoServer [2.24.3](/release/2.24.3/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.3/geoserver-2.24.3-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.3/geoserver-2.24.3-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.3/GeoServer-2.24.3-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.3/geoserver-2.24.3-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.3/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.
GeoServer 2.24.3 is made in conjunction with GeoTools 30.3, and GeoWebCache 1.24.3. 

Thanks to Andrea Aime (GeoSolutions) for making this release.

### Security Considerations

**2024-06-30 Update:** The following mitigation has been provided:

* [CVE-2024-36401](https://github.com/geoserver/geoserver/security/advisories/GHSA-6jj6-gm7p-fcvv) Remote Code Execution (RCE) vulnerability in evaluating property name expressions (Critical)

  [geoserver-2.24.3-patches.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.3/geoserver-2.24.3-patches.zip/download) (replacing `gt-app-schema`, `gt-complex` and `gt-xsd-core` jars) has been provided by Andrea (GeoSolutions)

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 


## Release notes

New Feature:

* [GEOS-11077](https://osgeo-org.atlassian.net/browse/GEOS-11077) Implement Requirement Class "Search" from OGC API - Features Part 5 proposal
* [GEOS-11225](https://osgeo-org.atlassian.net/browse/GEOS-11225) [AuthKey] AuthKey synchronize the user/group automatically
* [GEOS-11267](https://osgeo-org.atlassian.net/browse/GEOS-11267) csw-iso: multiple mappings should also have multiple queryable mappings
* [GEOS-11279](https://osgeo-org.atlassian.net/browse/GEOS-11279) metadata: allow same field on multiple tabs

Improvement:

* [GEOS-11260](https://osgeo-org.atlassian.net/browse/GEOS-11260) JNDI tutorial uses outdated syntax
* [GEOS-11276](https://osgeo-org.atlassian.net/browse/GEOS-11276) Use style_body to define CSS style for a layer
* [GEOS-11288](https://osgeo-org.atlassian.net/browse/GEOS-11288) Improve input validation in ClasspathPublisher
* [GEOS-11306](https://osgeo-org.atlassian.net/browse/GEOS-11306) Java 17 does not support GetFeature lazy JDBC count(*)
* [GEOS-11327](https://osgeo-org.atlassian.net/browse/GEOS-11327) Add warning about using embedded data directories
* [GEOS-11329](https://osgeo-org.atlassian.net/browse/GEOS-11329) Update MapML viewer to release 0.13.0
* [GEOS-11334](https://osgeo-org.atlassian.net/browse/GEOS-11334) Update MapML viewer to release 0.13.1
* [GEOS-11342](https://osgeo-org.atlassian.net/browse/GEOS-11342) STAC should exclude items when the collection in path is wrong
* [GEOS-11347](https://osgeo-org.atlassian.net/browse/GEOS-11347) STAC Landing Page links should include root link
* [GEOS-11359](https://osgeo-org.atlassian.net/browse/GEOS-11359) Update MapML viewer to release 0.13.2

Bug:

* [GEOS-11174](https://osgeo-org.atlassian.net/browse/GEOS-11174) GWC rest api returns erroneous truncated response when gzip http encoding is enabled 
* [GEOS-11205](https://osgeo-org.atlassian.net/browse/GEOS-11205) Layer page: style image fails if it is in isolated workspace
* [GEOS-11236](https://osgeo-org.atlassian.net/browse/GEOS-11236) WFS 2.0.0/GetFeature - Shapefile - "We have had issues trying to flip axis"
* [GEOS-11256](https://osgeo-org.atlassian.net/browse/GEOS-11256) Cannot retrieve LegendGraphic from a PostGIS datastore with 'hideEmptyRules' and 'Support on the fly geometry simplification' enabled
* [GEOS-11263](https://osgeo-org.atlassian.net/browse/GEOS-11263) hideEmptyRules not working in JSON LegendGraphic
* [GEOS-11266](https://osgeo-org.atlassian.net/browse/GEOS-11266) csw-iso: missing fields in summary response
* [GEOS-11278](https://osgeo-org.atlassian.net/browse/GEOS-11278) metadata: only selected tab is submitted
* [GEOS-11285](https://osgeo-org.atlassian.net/browse/GEOS-11285) GWC REST Content-Encoding gzip returns broken response
* [GEOS-11290](https://osgeo-org.atlassian.net/browse/GEOS-11290) With Oauth enabled, anon users get random auth requests
* [GEOS-11291](https://osgeo-org.atlassian.net/browse/GEOS-11291) GeoFence: Cleanup stale log4j references
* [GEOS-11299](https://osgeo-org.atlassian.net/browse/GEOS-11299) Performance regression in GeoJSON output generated in EPSG:900913
* [GEOS-11312](https://osgeo-org.atlassian.net/browse/GEOS-11312) Inconsistent Memory Units in Legend Image Creation
* [GEOS-11335](https://osgeo-org.atlassian.net/browse/GEOS-11335) A layer in an authority other than EPSG may fail to reload after restart

Task:

* [GEOS-11307](https://osgeo-org.atlassian.net/browse/GEOS-11307) Update apache-commons-lang3 to version 3.14.0 for Java 17 and Java 21 support
* [GEOS-11316](https://osgeo-org.atlassian.net/browse/GEOS-11316) Update Spring version to 5.3.32
* [GEOS-11360](https://osgeo-org.atlassian.net/browse/GEOS-11360) Upgrade Apache POI from 4.1.1 to 5.2.5
* [GEOS-11362](https://osgeo-org.atlassian.net/browse/GEOS-11362) Upgrade Spring libs from 5.3.32 to 5.3.33

For the complete list see [2.24.3](https://github.com/geoserver/geoserver/releases/tag/2.24.3) release notes. 

## Community Updates

Community module development:

* [GEOS-11305](/browse/GEOS-11305) Add layer information in the models backing STAC
* [GEOS-11330](/browse/GEOS-11330) OAuth2 kid verification should be optional
* [GEOS-11339](/browse/GEOS-11339) Introducing the Features Autopopulate Community Plugin
* [GEOS-11340](/browse/GEOS-11340) WFS Freemarker HTML Outputformat
* [GEOS-11345](/browse/GEOS-11345) STAC Conformance URIs need to be updated to v1.0.0
* [GEOS-11348](/browse/GEOS-11348) JMS cluster does not allow to publish style via REST "2 step" approach
* [GEOS-11358](/browse/GEOS-11358) Feature-Autopopulate Update operation does not apply the Update Element filter

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.24 Series

Additional information on GeoServer 2.24 series:

* [GeoServer 2.24 User Manual](https://docs.geoserver.org/2.24.x/en/user/)
* [Control remote HTTP requests sent by GeoTools/GeoServer](https://github.com/geoserver/geoserver/wiki/GSIP-218)
* [State of GeoServer 2.24.1](https://docs.google.com/presentation/d/1X7iU1fd47frfh1EsN_CdUll0qtMMgPXkkMjaTbejj3g/edit?usp=sharing) (foss4g-asia presentation)
* [Multiple CRS authority support, planetary CRS](https://github.com/geoserver/geoserver/wiki/GSIP-219)
* [Extensive GeoServer Printing improvements](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html)
* [Upgraded security policy](https://github.com/geoserver/geoserver/wiki/GSIP-220)

Release notes:
( [2.24.3](https://github.com/geoserver/geoserver/releases/tag/2.24.3)
| [2.24.2](https://github.com/geoserver/geoserver/releases/tag/2.24.2)
| [2.24.1](https://github.com/geoserver/geoserver/releases/tag/2.24.1)
| [2.24.0](https://github.com/geoserver/geoserver/releases/tag/2.24.0)
| [2.24-RC](https://github.com/geoserver/geoserver/releases/tag/2.24-RC)
) 

