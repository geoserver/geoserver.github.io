---
author: Peter Smythe
date: 2024-03-19
layout: post
title: GeoServer 2.25.0 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_225
version: 2.25.0
jira_version: 16915
--- 

GeoServer [2.25.0](/release/2.25.0/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.0/geoserver-2.25.0-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.0/geoserver-2.25.0-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.0/GeoServer-2.25.0-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.0/geoserver-2.25.0-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.0/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 2.25.0 is made in conjunction with GeoTools 31.0, and GeoWebCache 1.25.0. 

Thanks to Peter Smythe for making this release. Thanks to Levy Steve, Peter Smythe, Jody Garnett, and Mark Prins for testing the 2.25.0 release.

## Security Considerations

This release addresses several security vulnerabilities, all of which require admin access.

* If you have updated to GeoServer 2.24.2 Release or GeoServer 2.23.5 Release you are already patched. 
* If you are working with a [commercial support provider](/support/) that volunteers with the geoserver-security email list they are already informed.

Vulnerabilities:

- [CVE-2023-51444](https://github.com/geoserver/geoserver/security/advisories/GHSA-9v5q-2gwq-q9hq) Arbitrary file upload vulnerability in REST Coverage Store API (High).
- [CVE-2023-41877](https://github.com/geoserver/geoserver/security/advisories/GHSA-8g7v-vjrc-x4g5) GeoServer log file path traversal vulnerability (High).
- [CVE-2024-23634](https://github.com/geoserver/geoserver/security/advisories/GHSA-75m5-hh4r-q9gx) Arbitrary file renaming vulnerability in REST Coverage/Data Store API (Moderate).
- [CVE-2024-23643](https://github.com/geoserver/geoserver/security/advisories/GHSA-56r3-f536-5gf7) Stored Cross-Site Scripting (XSS) vulnerability in GWC Seed Form (Moderate).
- [CVE-2024-23821](https://github.com/geoserver/geoserver/security/advisories/GHSA-88wc-fcj9-q3r9) Stored Cross-Site Scripting (XSS) vulnerability in GWC Demos Page (Moderate).
- [CVE-2024-23819](https://github.com/geoserver/geoserver/security/advisories/GHSA-7x76-57fr-m5r5) Stored Cross-Site Scripting (XSS) vulnerability in MapML HTML Page (Moderate).
- [CVE-2024-23818](https://github.com/geoserver/geoserver/security/advisories/GHSA-fcpm-hchj-mh72) Stored Cross-Site Scripting (XSS) vulnerability in WMS OpenLayers Format (Moderate).
- [CVE-2024-23642](https://github.com/geoserver/geoserver/security/advisories/GHSA-fg9v-56hw-g525) Stored Cross-Site Scripting (XSS) vulnerability in Simple SVG Renderer (Moderate).
- [CVE-2024-23640](https://github.com/geoserver/geoserver/security/advisories/GHSA-9rfr-pf2x-g4xf) Stored Cross-Site Scripting (XSS) vulnerability in Style Publisher (Moderate).
- [CVE-2023-51445](https://github.com/geoserver/geoserver/security/advisories/GHSA-fh7p-5f6g-vj2w) Stored Cross-Site Scripting (XSS) vulnerability in REST Resources API (Moderate).
- [CVE-2024-34711](https://github.com/geoserver/geoserver/security/advisories/GHSA-mc43-4fqr-c965) Improper ENTITY_RESOLUTION_ALLOWLIST URI validation in XML Processing (SSRF) (High 7.3)
* [CVE-2025-21621](https://github.com/geoserver/geoserver/security/advisories/GHSA-w66h-j855-qr72) Reflected Cross-Site Scripting (XSS) vulnerability in WMS GetFeatureInfo HTML format (Moderate)

The use of the CVE system allows the GeoServer team to reach a wider audience than blog posts.

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

We would like to thank everyone who contributed to reporting, verifying and fixing the above vulnerabilities (see each CVE for appropriate credits). A special thank you to Steve Ikeoka for reporting most of the issues and doing the majority of the actual fixes. 

The use of the CVE system allows the GeoServer team to reach a wider audience than blog posts. See the project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Upgrade Notes

We have a number of configuration changes when [updating an existing system](https://docs.geoserver.org/latest/en/user/installation/upgrade.html):

* The longstanding ``ENTITY_RESOLUTION_ALLOWLIST`` [setting](https://docs.geoserver.org/latest/en/user/production/config.html#external-entities-resolution) has been recommended as a way to control the locations available for external entity resolution when parsing XML documents and requests.

  The default has changed from `*` (allowing any location) to allowing the recommended `www.w3.org`, `schemas.opengis.net`, `www.opengis.net` locations used for OGC Web Services, along with the `inspire.ec.europa.eu/schemas` location used by our friends in Europe.

* The FreeMarker Template HTML Auto-escaping is [now enabled by default](https://docs.geoserver.org/latest/en/user/production/config.html#production-config-freemarker-escaping).

* The [spring security firewall](https://docs.geoserver.org/latest/en/user/production/config.html#production-config-spring-firewall) is now enabled by default.

* A new [configuration setting](https://docs.geoserver.org/latest/en/user/production/config.html#static-web-files) is available to limit content served from the `geoserver/www` folder. 

  If you have not met the ``www`` folder before it is used to share content, and there is a tutorial [serving static files](https://docs.geoserver.org/latest/en/user/tutorials/staticfiles.html).

* We do add recommendations to [production considerations](https://docs.geoserver.org/latest/en/user/production/config.html) over time, if you have not checked that page in a while please review.

Thanks to Steve Ikeoka and Jody Garnett for these improvements.

## JTS fast polygon intersection enabled by default

The JTS [Next Generation polygon intersection algorithm](https://lin-ear-th-inking.blogspot.com/2020/05/jts-overlay-next-generation.html) has been enabled by default, which will improve performance of a number of operations, including WPS processes and the vector tiles generation.
We deem the functionality well tested enough that it should be opened to the majority of users, even if it's still possible to turn it off by adding the ``-Djts.overlay=old``.

![](/img/posts/2.25/intersection-canada-flag.png)

## MapML Extension

The MapML extension is receiving a number of updates and improvements, with more to come in the following months.
It's now possible to declare "Tiled CRS" as the CRS for a layer, with the implication not just of the CRS, but also of the gridset that will be used by the MapML viewer:

![](/img/posts/2.25/mapml-crs.png)

This portion builds on top of the work done months ago to support astronomical CRSs, which allows GeoServer to support multiple CRS authorities.

The MapML preview links are now using the new MapML output format, while the old dedicated REST controller has been removed. This allows for better integration of the MapML format in the GeoServer ecosystem. The MapML viewer has also been updated to the latest version:

![](/img/posts/2.25/mapml-viewer.png)

Thanks to Joseph Miller and Andrea Aime (GeoSolutions) for this work, and Natural Resources Canada for sponsoring it.

## Community Module Updates

Much of the new activity in GeoServer starts as a community module. We'd like to remind you that these modules are
not yet supported, and invite you to join the effort by participating in their development, as well as testing them
and providing feedback.

### Raster Attribute Table community module

Developed as part of [GEOS-11175](https://osgeo-org.atlassian.net/browse/GEOS-11175), the Raster Attribute Table community module
uses the GDAL Raster Attribute Table (RAT) to provide a way to associate attribute information for individual pixel values within the raster, to create styles as well as to provide a richer GetFeatureInfo output.

![](/img/posts/2.25/rat-ui.png)

![](/img/posts/2.25/rat-map.png)
   
For more information see the [user guide](https://docs.geoserver.org/latest/en/user/community/rat/index.html).

We'd like to thank Andrea Aime (GeoSolutions) for the development and NOAA for sponsoring.

### Graticules for WMS maps

The graticules community module, developed as part of [GEOS-11216](https://osgeo-org.atlassian.net/browse/GEOS-11216),  provides 
a datastore generating graticules for WMS maps, along with a rendering transformation that can be used to label them.
The module can be used to draw a graticule in WMS maps, as well as to download them as part of WFS (or in combination with the WPS download module).

![](/img/posts/2.25/graticule-store.png)

![](/img/posts/2.25/graticules.png)

We'd like to thank Ian Turton for development and GeoSolutions for sponsoring the work. 

### GeoServer monitor Kafka storage
   
The monitoring Kafka storage module, developed as part of [GEOS-11150](https://osgeo-org.atlassian.net/browse/GEOS-11150), allows storing the requests captured by the [monitoring extension](https://docs.geoserver.org/latest/en/user/extensions/monitoring/index.html) into a Kafka topic.

![](/img/posts/2.25/kafka-monitor.png)
  
We'd like to thank Simon Hofer for sharing his work with the community. To learn more about the module, how to install and use it, see the [user-guide](https://docs.geoserver.org/latest/en/user/community/monitor-kafka/index.html).

### JWT Headers
  
The JWT headers module has been developed as part of [GEOS-11317](https://osgeo-org.atlassian.net/browse/GEOS-11317).

![](/img/posts/2.25/jwt-logo.png)

The module is a new authentication filter that can read [JWT Headers](https://docs.geoserver.org/latest/en/user/community/jwt-headers/index.html), as well as general JSON payloads and simple strings, to identify a user, as well as to extract their roles. 
The combination of Apache [mod_auth_openidc](https://github.com/OpenIDC/mod_auth_openidc) with [geoserver-jwt-headers-plugin]() provides an alternative to using the [geoserver-sec-oauth2-openid-connect-plugin](https://docs.geoserver.org/latest/en/user/community/oauth2/oidc.html) plugin.

We'd like to thank David Blasby (GeoCat) for this work on this module.

## Developer Updates

### ResourceStore / Paths API Change

Developers should keep in mind some important maintenance work performed by Niels Charlier on the use absolute and relative paths in the `ResourceStore`. See the [Developers Guide](https://docs.geoserver.org/latest/en/developer/programming-guide/config/resource.html) for more information.

This does not affect end users.

### Experimental Java 21 support

GeoServer, along with GeoTools and GeoWebCache, are now tested to build and pass tests with Java 21.

This is not yet an endorsement to run GeoServer in production with Java 21. We are looking ahead at the [2024 roadmap]({% post_url 2024-01-03-roadmap %}), and are making sure the basics are covered for the newer Java releases. 

## Full Release notes

New Feature:

* [GEOS-11225](https://osgeo-org.atlassian.net/browse/GEOS-11225) [AuthKey] AuthKey synchronize the user/group automatically

MapML:

* [GEOS-10438](https://osgeo-org.atlassian.net/browse/GEOS-10438) ENTITY_RESOLUTION_ALLOWLIST property not parsing empty setting
* [GEOS-11207](https://osgeo-org.atlassian.net/browse/GEOS-11207) Refactor MapML MVC controller as GetMap-based operation with standard parameter format
* [GEOS-11221](https://osgeo-org.atlassian.net/browse/GEOS-11221) mkdocs preflight rst fixes
* [GEOS-11289](https://osgeo-org.atlassian.net/browse/GEOS-11289) Enable Spring Security StrictHttpFirewall by default
* [GEOS-11297](https://osgeo-org.atlassian.net/browse/GEOS-11297) Escape WMS GetFeatureInfo HTML output by default
* [GEOS-11300](https://osgeo-org.atlassian.net/browse/GEOS-11300) Centralize access to static web files

Improvement:

* [GEOS-11306](https://osgeo-org.atlassian.net/browse/GEOS-11306) Java 17 does not support GetFeature lazy JDBC count(*)
* [GEOS-11130](https://osgeo-org.atlassian.net/browse/GEOS-11130) Sort parent role dropdown in Add a new role
* [GEOS-11142](https://osgeo-org.atlassian.net/browse/GEOS-11142) Add mime type mapping for yaml files
* [GEOS-11148](https://osgeo-org.atlassian.net/browse/GEOS-11148) Update response headers for the Resources REST API
* [GEOS-11149](https://osgeo-org.atlassian.net/browse/GEOS-11149) Update response headers for the Style Publisher
* [GEOS-11152](https://osgeo-org.atlassian.net/browse/GEOS-11152) Improve handling special characters in the Simple SVG Renderer
* [GEOS-11153](https://osgeo-org.atlassian.net/browse/GEOS-11153) Improve handling special characters in the WMS OpenLayers Format
* [GEOS-11155](https://osgeo-org.atlassian.net/browse/GEOS-11155) Add the X-Content-Type-Options header
* [GEOS-11173](https://osgeo-org.atlassian.net/browse/GEOS-11173) Default to using HttpOnly session cookies
* [GEOS-11176](https://osgeo-org.atlassian.net/browse/GEOS-11176) Add validation to file wrapper resource paths
* [GEOS-11213](https://osgeo-org.atlassian.net/browse/GEOS-11213) Improve REST external upload method unzipping
* [GEOS-11222](https://osgeo-org.atlassian.net/browse/GEOS-11222) Include Conformance Class for "Search" from OGC API - Features Part 5 proposal
* [GEOS-11226](https://osgeo-org.atlassian.net/browse/GEOS-11226) Enable JTS OverlayNG by default
* [GEOS-11246](https://osgeo-org.atlassian.net/browse/GEOS-11246) Schemaless plugin performance for WFS
* [GEOS-11247](https://osgeo-org.atlassian.net/browse/GEOS-11247) Avoid HTML annotations special status in APIBodyProcessor
* [GEOS-11248](https://osgeo-org.atlassian.net/browse/GEOS-11248) Move version header handling from APIBodyMethodProcessor to APIDispatcher
* [GEOS-11260](https://osgeo-org.atlassian.net/browse/GEOS-11260) JNDI tutorial uses outdated syntax
* [GEOS-11288](https://osgeo-org.atlassian.net/browse/GEOS-11288) Improve input validation in ClasspathPublisher
* [GEOS-11289](https://osgeo-org.atlassian.net/browse/GEOS-11289) Enable Spring Security StrictHttpFirewall by default
* [GEOS-11298](https://osgeo-org.atlassian.net/browse/GEOS-11298) When a Raster Attribute Table is available, expose its attributes in GetFeatureInfo
* [GEOS-11327](https://osgeo-org.atlassian.net/browse/GEOS-11327) Add warning about using embedded data directories
* [GEOS-11334](https://osgeo-org.atlassian.net/browse/GEOS-11334) Update MapML viewer to release 0.13.1

Bug:

* [GEOS-11050](https://osgeo-org.atlassian.net/browse/GEOS-11050) jdbc-store broken by changes to Paths.names
* [GEOS-11051](https://osgeo-org.atlassian.net/browse/GEOS-11051) Env parametrization does not save correctly in AuthKey extension
* [GEOS-11145](https://osgeo-org.atlassian.net/browse/GEOS-11145) The GUI "wait spinner" is not visible any longer
* [GEOS-11182](https://osgeo-org.atlassian.net/browse/GEOS-11182) Avoid legends with duplicated entries
* [GEOS-11187](https://osgeo-org.atlassian.net/browse/GEOS-11187) Configuring a raster with NaN as NODATA results in two NaN in the nodata band description
* [GEOS-11190](https://osgeo-org.atlassian.net/browse/GEOS-11190) GeoFence: align log4j2 deps
* [GEOS-11203](https://osgeo-org.atlassian.net/browse/GEOS-11203) WMS GetFeatureInfo bad WKT exception for label-geometry
* [GEOS-11224](https://osgeo-org.atlassian.net/browse/GEOS-11224) Platform independent binary doesn't start properly with default data directory
* [GEOS-11250](https://osgeo-org.atlassian.net/browse/GEOS-11250) WFS GeoJSON encoder fails with an exception if an infinity number is used in the geometry
* [GEOS-11278](https://osgeo-org.atlassian.net/browse/GEOS-11278) metadata: only selected tab is submitted
* [GEOS-11312](https://osgeo-org.atlassian.net/browse/GEOS-11312) Used memory calculation fix on legend WMS request
* [GEOS-11266](https://osgeo-org.atlassian.net/browse/GEOS-11266) csw-iso: missing fields in summary response
* [GEOS-11312](https://osgeo-org.atlassian.net/browse/GEOS-11312) Inconsistent Memory Units in Legend Image Creation
* [GEOS-11335](https://osgeo-org.atlassian.net/browse/GEOS-11335) A layer in an authority other than EPSG may fail to reload after restart

Task:

* [GEOS-11242](https://osgeo-org.atlassian.net/browse/GEOS-11242) Remove the Xalan library
* [GEOS-11315](https://osgeo-org.atlassian.net/browse/GEOS-11315) Revert to CORS commented out
* [GEOS-11318](https://osgeo-org.atlassian.net/browse/GEOS-11318) Update postgresql to 42.7.2
* [GEOS-11134](https://osgeo-org.atlassian.net/browse/GEOS-11134) Feedback on download bundles: README, RUNNING, GPL html files
* [GEOS-11141](https://osgeo-org.atlassian.net/browse/GEOS-11141) production consideration for logging configuration hardening
* [GEOS-11159](https://osgeo-org.atlassian.net/browse/GEOS-11159) Update mapfish-print-lib 2.3.0
* [GEOS-11180](https://osgeo-org.atlassian.net/browse/GEOS-11180) Update ImageIO-EXT to 1.4.9
* [GEOS-11181](https://osgeo-org.atlassian.net/browse/GEOS-11181) Update jai-ext to 1.1.25
* [GEOS-11186](https://osgeo-org.atlassian.net/browse/GEOS-11186) Fix maven enforcer failFast
* [GEOS-11220](https://osgeo-org.atlassian.net/browse/GEOS-11220) Upgrade Hazelcast from 5.3.1 to 5.3.6
* [GEOS-11245](https://osgeo-org.atlassian.net/browse/GEOS-11245) Update OSHI from 6.2.2 to 6.4.10
* [GEOS-11316](https://osgeo-org.atlassian.net/browse/GEOS-11316) Update Spring version to 5.3.32

For the complete list see [2.25.0](https://github.com/geoserver/geoserver/releases/tag/2.25.0) release notes. 

## Community Updates

Community module development:

* [GEOS-11305](https://osgeo-org.atlassian.net/browse/GEOS-11305) Add layer information in the models backing STAC
* [GEOS-11146](https://osgeo-org.atlassian.net/browse/GEOS-11146) Fix MBTiles output format test
* [GEOS-11184](https://osgeo-org.atlassian.net/browse/GEOS-11184) ncwms module has a compile dependency on gs-web-core test jar 
* [GEOS-11209](https://osgeo-org.atlassian.net/browse/GEOS-11209) Open ID Connect Proof Key of Code Exchange (PKCE)
* [GEOS-11212](https://osgeo-org.atlassian.net/browse/GEOS-11212) OIDC accessToken verification using only JWKs URI
* [GEOS-11219](https://osgeo-org.atlassian.net/browse/GEOS-11219) Upgraded mail and activation libraries for SMTP compatibility
* [GEOS-11293](https://osgeo-org.atlassian.net/browse/GEOS-11293) Improve performance of wps-lontigudinal-profile
* [GEOS-11216](https://osgeo-org.atlassian.net/browse/GEOS-11216) Create a datastore to produce graticules for WMS maps.

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.25 Series

Additional information on GeoServer 2.25 series:

* [GeoServer 2.25 User Manual](https://docs.geoserver.org/2.25.x/en/user/)
* [GeoServer 2024 Roadmap Plannings]({% post_url 2024-01-03-roadmap %}) 

Release notes:
( [2.25.0](https://github.com/geoserver/geoserver/releases/tag/2.25.0)
| [2.25-RC](https://github.com/geoserver/geoserver/releases/tag/2.25-RC)
) 

