---
author: Jody Garnett
date: 2024-03-04
layout: post
title: GeoServer 2.25-RC Release
categories:
- Announcements
tags:
- Release
- Release Candidate
release: release_225
version: 2.25-RC
jira_version: 16901
--- 

GeoServer [2.25-RC](/release/2.25-RC/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25-RC/geoserver-2.25-RC-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25-RC/geoserver-2.25-RC-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25-RC/GeoServer-2.25-RC-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25-RC/geoserver-2.25-RC-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25-RC/extensions/).

This is a release candidate intended for public review and feedback.
GeoServer 2.25-RC is made in conjunction with GeoTools 31-RC, and GeoWebCache 1.25-RC. 

Thanks to Jody Garnett (GeoCat) for making this release.

## Release Candiate

Testing and providing feedback on releases is part of the open-source social contract. The development team (and their employers and customers) are responsible for sharing this great technology with you.

> The collaborative part of open-source happens now - we ask you to test this release candidate in your environment and with your data. Try out the new features, double check if the documentation makes sense, and most importantly let us know!
> 
> If you spot something that is incorrect or not working do not assume it is obvious and we will notice. We request and depend on your [email](https://geoserver.org/comm/) and [bug reports](https://geoserver.org/issues/) at this time. If you are working with [commercial support](https://geoserver.org/support/) your provider is expected to participate on your behalf.

Keeping GeoServer sustainable requires a long term community commitment. If you are unable to contribute time, [sponsorship options](https://geoserver.org/sponsor/) are available via OSGeo (we have an ambitious [2024 roadmap]({% post_url 2024-01-03-roadmap %}) for the year ahead).

## Configuration Changes

We have a number of configuration changes to keep in mind if you are updating an existing system:

* The longstanding ``ENTITY_RESOLUTION_ALLOWLIST`` [setting](https://docs.geoserver.org/2.25.x/en/user/production/config.html#external-entities-resolution) has been recommended as a way to control the locations available for external entity resolution when parsing XML documents and requests.

  The default has changed from `*` (allowing any location) to allowing the recommended `www.w3.org`, `schemas.opengis.net`, `www.opengis.net` locations used for OGC Web Services, along with the `inspire.ec.europa.eu/schemas` location used by our friends in Europe.

* The FreeMarker Template HTML Auto-escaping is [now enabled by default](https://docs.geoserver.org/2.25.x/en/user/production/config.html#production-config-freemarker-escaping).

* The [spring security firewall](https://docs.geoserver.org/2.25.x/en/user/production/config.html#production-config-spring-firewall) is now enabled by default.

* A new [configuration setting](https://docs.geoserver.org/2.25.x/en/user/production/config.html#static-web-files) is available to limit content served by `geoserver/www` folder. 

  While this folder is intended to [serve small web applications](https://docs.geoserver.org/2.25.x/en/user/tutorials/staticfiles.html) it has ended up being useful for a wide range of content.

For more information on please see the user guide [Update Instructions](https://docs.geoserver.org/2.25.x/en/user/installation/upgrade.html).

In general we do not like to update defaults, preferring to add notes to [production considerations](https://docs.geoserver.org/2.25.x/en/user/production/config.html) with our recommendations. If you have not checked that page in a while please review.

Thanks to Steve Ikeoka and Jody Garnett for these improvements.


## MkDocs

The upcoming GeoServer 2.25.0 release will feature a new look, much faster search, light and dark mode, and a responsive layout. Editing has changed from reStructuredText to the much more popular Markdown format.

*A [preview](https://jodygarnett.github.io/geoserver/) is available, which is being used to help test each page.* Testers include:

* Alexandre Gacon
* Andrea Aime
* Henning Lorenz 
* Geospatial Techno
* Peter Smythe
* Marcus Lingenfelder
* Roar Brænden

Thanks to Jody Garnett (GeoCat) for [this initiative](https://github.com/geoserver/geoserver/wiki/GSIP-221) -- we hope that these changes make the documentation more accessible to our community!

* [https://osgeo-org.atlassian.net/browse/GEOS-11221][GEOS-11221] mkdocs preflight rst fixes]()
* [GSIP 221 - MkDocs](https://github.com/geoserver/geoserver/wiki/GSIP-221)

![](/img/posts/2.25/mkdocs-preview.png)

## Security Considerations

This a reminder to update to GeoServer 2.24.2 Release (or GeoServer 2.35.5 Release).

Alongside the upcoming GeoServer 2.25.0 release we will "publicly disclose" a list of Common Vulnerabilities and Exposures that have been addressed previously.
 
* If you are working with a [commercial support provider](/support/) that volunteers with the geoserver-security email list they are already informed.
* If you have updated to GeoServer 2.24.2 Release (or GeoServer 2.23.5 Release) you are already patched.

I hope you enjoy our team's effort to improve communication. The use of the CVE system allows us to reach a wider audience than reads these blog posts.

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

## Experimental Java 21 support

GeoServer, along with GeoTools and GeoWebCache, are now tested to build and pass tests with Java 21.
While this is not yet an endorsement to run GeoServer in production with Java 21, we are keeping tabs on it and trying to make sure there the basics are covered for the newer Java releases.

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

### Raster attribute Table community module

Developed as part of [GEOS-11175](https://osgeo-org.atlassian.net/browse/GEOS-11175), the Raster Attribute Table community module
allows to leverage the GDAL Raster Attribute Table (RAT) providing a way to associate attribute information for individual pixel values within the raster, to create styles as well as to provide a richer GetFeatureInfo output.

![](/img/posts/2.25/rat-ui.png)

![](/img/posts/2.25/rat-map.png)
   
For more information see the [user guide](https://docs.geoserver.org/2.25.x/en/user/community/rat/index.html).

We'd like to thank Andrea Aime (GeoSolutions) for the development and NOAA for the sponsoring.

### Graticules for WMS maps

The graticules community module, developed as part of [GEOS-11216](https://osgeo-org.atlassian.net/browse/GEOS-11216),  provides 
a datastore generating graticules for WMS maps, along with a rendering transformation that can be used to label them.
The module can be used to draw a graticule in WMS maps, as well as to download them same as part of WFS (or in combination with the WPS download module).

![](/img/posts/2.25/graticule-store.png)

![](/img/posts/2.25/graticules.png)

We'd like to thank Ian Turton for development and GeoSolutions for sponsoring the work. 

### GeoServer monitor Kafka storage
   
The monitoring Kafka storage module, developed as part of [GEOS-11150](https://osgeo-org.atlassian.net/browse/GEOS-11150), allows to store the requests captured by the [monitoring extension](https://docs.geoserver.org/latest/en/user/extensions/monitoring/index.html) into a Kafka topic.

![](/img/posts/2.25/kafka-monitor.png)
  
We'd like to thank Simon Hofer for sharing his work with the community. To learn more about the module, how to install and use it, see the [user-guide](https://docs.geoserver.org/2.25.x/en/user/community/monitor-kafka/index.html).

### JWT Headers
  
The JWT headers module has been developed as part of [GEOS-11317](https://osgeo-org.atlassian.net/browse/GEOS-11317).

![](/img/posts/2.25/jwt-logo.png)

The module is a new authentication filter that can read [JWT Headers](https://docs.geoserver.org/2.25.x/en/user/community/jwt-headers/index.html), as well as general JSON payloads and simple strings, to identify a user, as well as to extract their roles. 
The combination of Apache [mod_auth_openidc](https://github.com/OpenIDC/mod_auth_openidc) with [geoserver-jwt-headers-plugin]() provides an alternative to use [geoserver-sec-oauth2-openid-connect-plugin](https://docs.geoserver.org/2.25.x/en/user/community/oauth2/oidc.html) plugin.

We'd like to thank David Blasby (GeoCat) for this work on this module.

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

Community module development:

* [GEOS-11305](https://osgeo-org.atlassian.net/browse/GEOS-11305) Add layer information in the models backing STAC
* [GEOS-11146](https://osgeo-org.atlassian.net/browse/GEOS-11146) Fix MBTiles output format test
* [GEOS-11184](https://osgeo-org.atlassian.net/browse/GEOS-11184) ncwms module has a compile dependency on gs-web-core test jar 
* [GEOS-11209](https://osgeo-org.atlassian.net/browse/GEOS-11209) Open ID Connect Proof Key of Code Exchange (PKCE)
* [GEOS-11212](https://osgeo-org.atlassian.net/browse/GEOS-11212) OIDC accessToken verification using only JWKs URI
* [GEOS-11219](https://osgeo-org.atlassian.net/browse/GEOS-11219) Upgraded mail and activation libraries for SMTP compatibility
* [GEOS-11293](https://osgeo-org.atlassian.net/browse/GEOS-11293) Improve performance of wps-lontigudinal-profile

# About GeoServer 2.25 Series

Additional information on GeoServer 2.25 series:

* [GeoServer 2.25 User Manual](https://docs.geoserver.org/2.25.x/en/user/)
* [GeoServer 2024 Roadmap Plannings]({% post_url 2024-01-03-roadmap %}) 
* [MkDocs Proposal](https://github.com/geoserver/geoserver/wiki/GSIP-221)

Release notes:
( [2.25-RC](https://github.com/geoserver/geoserver/releases/tag/2.25-RC)
) 

