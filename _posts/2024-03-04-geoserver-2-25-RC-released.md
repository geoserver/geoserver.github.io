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

For more information please see the user guide [Update Instructions](https://docs.geoserver.org/2.25.x/en/user/installation/upgrade.html).

In general we do not like to update defaults, preferring to add notes to [production considerations](https://docs.geoserver.org/2.25.x/en/user/production/config.html) with our recommendations. If you have not checked that page in a while please review.

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

Thanks to Jody Garnett (GeoCat) for [this initiative](https://github.com/geoserver/geoserver/wiki/GSIP-221) -- we hope that these changes make the documentation more accessable to our community!

![](/img/posts/2.25/mkdocs-preview.png)

## Security Considerations

This a reminder to update to GeoServer 2.24.2 Release (or GeoServer 2.35.5 Release).

Alongside the upcoming GeoServer 2.25.0 release we will "publicly disclose" a list of Common Vulnerabilities and Exposures that have been addressed previously.
 
* If you are working with a [commercial support provider](/support/) that volunteers with the geoserver-security email list they are already informed.
* If you have updated to GeoServer 2.24.2 Release (or GeoServer 2.23.5 Release) you are already patched.

I hope you enjoy our team's effort to improve communication. The use of the CVE system allows us to reach a wider audience than reads these blog posts.

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

## Release notes

New Feature:

* [GEOS-11175](https://osgeo-org.atlassian.net/browse/GEOS-11175) Raster Attribute Table community module
* [GEOS-11225](https://osgeo-org.atlassian.net/browse/GEOS-11225) [AuthKey] AuthKey synchronize the user/group automatically

Improvement:

* [GEOS-11130](https://osgeo-org.atlassian.net/browse/GEOS-11130) Sort parent role dropdown in Add a new role
* [GEOS-11142](https://osgeo-org.atlassian.net/browse/GEOS-11142) Add mime type mapping for yaml files
* [GEOS-11148](https://osgeo-org.atlassian.net/browse/GEOS-11148) Update response headers for the Resources REST API
* [GEOS-11149](https://osgeo-org.atlassian.net/browse/GEOS-11149) Update response headers for the Style Publisher
* [GEOS-11152](https://osgeo-org.atlassian.net/browse/GEOS-11152) Improve handling special characters in the Simple SVG Renderer
* [GEOS-11153](https://osgeo-org.atlassian.net/browse/GEOS-11153) Improve handling special characters in the WMS OpenLayers Format
* [GEOS-11154](https://osgeo-org.atlassian.net/browse/GEOS-11154) Improve handling special characters in the MapML HTML Page
* [GEOS-11155](https://osgeo-org.atlassian.net/browse/GEOS-11155) Add the X-Content-Type-Options header
* [GEOS-11173](https://osgeo-org.atlassian.net/browse/GEOS-11173) Default to using HttpOnly session cookies
* [GEOS-11176](https://osgeo-org.atlassian.net/browse/GEOS-11176) Add validation to file wrapper resource paths
* [GEOS-11213](https://osgeo-org.atlassian.net/browse/GEOS-11213) Improve REST external upload method unzipping
* [GEOS-11216](https://osgeo-org.atlassian.net/browse/GEOS-11216) Create a datastore to produce graticules for WMS maps.
* [GEOS-11222](https://osgeo-org.atlassian.net/browse/GEOS-11222) Include Conformance Class for "Search" from OGC API - Features Part 5 proposal
* [GEOS-11226](https://osgeo-org.atlassian.net/browse/GEOS-11226) Enable JTS OverlayNG by default
* [GEOS-11232](https://osgeo-org.atlassian.net/browse/GEOS-11232) Add Zoom scaled layer templates to MapML
* [GEOS-11242](https://osgeo-org.atlassian.net/browse/GEOS-11242) Remove the Xalan library
* [GEOS-11246](https://osgeo-org.atlassian.net/browse/GEOS-11246) Schemaless plugin performance for WFS
* [GEOS-11247](https://osgeo-org.atlassian.net/browse/GEOS-11247) Avoid HTML annotations special status in APIBodyProcessor
* [GEOS-11248](https://osgeo-org.atlassian.net/browse/GEOS-11248) Move version header handling from APIBodyMethodProcessor to APIDispatcher
* [GEOS-11260](https://osgeo-org.atlassian.net/browse/GEOS-11260) JNDI tutorial uses outdated syntax
* [GEOS-11277](https://osgeo-org.atlassian.net/browse/GEOS-11277) Have MapML TCRS instances work as actual coordinate reference systems
* [GEOS-11288](https://osgeo-org.atlassian.net/browse/GEOS-11288) Improve input validation in ClasspathPublisher
* [GEOS-11289](https://osgeo-org.atlassian.net/browse/GEOS-11289) Enable Spring Security StrictHttpFirewall by default
* [GEOS-11297](https://osgeo-org.atlassian.net/browse/GEOS-11297) Escape WMS GetFeatureInfo HTML output by default
* [GEOS-11298](https://osgeo-org.atlassian.net/browse/GEOS-11298) When a Raster Attribute Table is available, expose its attributes in GetFeatureInfo
* [GEOS-11305](https://osgeo-org.atlassian.net/browse/GEOS-11305) Add layer information in the models backing STAC

Bug:

* [GEOS-11050](https://osgeo-org.atlassian.net/browse/GEOS-11050) jdbc-store broken by changes to Paths.names
* [GEOS-11051](https://osgeo-org.atlassian.net/browse/GEOS-11051) Env parametrization does not save correctly in AuthKey extension
* [GEOS-11145](https://osgeo-org.atlassian.net/browse/GEOS-11145) The GUI "wait spinner" is not visible any longer
* [GEOS-11182](https://osgeo-org.atlassian.net/browse/GEOS-11182) Avoid legends with duplicated entries
* [GEOS-11184](https://osgeo-org.atlassian.net/browse/GEOS-11184) ncwms module has a compile dependency on gs-web-core test jar 
* [GEOS-11187](https://osgeo-org.atlassian.net/browse/GEOS-11187) Configuring a raster with NaN as NODATA results in two NaN in the nodata band description
* [GEOS-11190](https://osgeo-org.atlassian.net/browse/GEOS-11190) GeoFence: align log4j2 deps
* [GEOS-11203](https://osgeo-org.atlassian.net/browse/GEOS-11203) WMS GetFeatureInfo bad WKT exception for label-geometry
* [GEOS-11224](https://osgeo-org.atlassian.net/browse/GEOS-11224) Platform independent binary doesn't start properly with default data directory
* [GEOS-11250](https://osgeo-org.atlassian.net/browse/GEOS-11250) WFS GeoJSON encoder fails with an exception if an infinity number is used in the geometry
* [GEOS-11278](https://osgeo-org.atlassian.net/browse/GEOS-11278) metadata: only selected tab is submitted
* [GEOS-11286](https://osgeo-org.atlassian.net/browse/GEOS-11286) MapML HTML backlinks are not workspace aware
* [GEOS-11287](https://osgeo-org.atlassian.net/browse/GEOS-11287) MapML throws unclear exceptions when asked to produce maps in unsupported CRSs

Task:

* [GEOS-11134](https://osgeo-org.atlassian.net/browse/GEOS-11134) Feedback on download bundles: README, RUNNING, GPL html files
* [GEOS-11141](https://osgeo-org.atlassian.net/browse/GEOS-11141) production consideration for logging configuration hardening
* [GEOS-11159](https://osgeo-org.atlassian.net/browse/GEOS-11159) Update mapfish-print-lib 2.3.0
* [GEOS-11180](https://osgeo-org.atlassian.net/browse/GEOS-11180) Update ImageIO-EXT to 1.4.9
* [GEOS-11181](https://osgeo-org.atlassian.net/browse/GEOS-11181) Update jai-ext to 1.1.25
* [GEOS-11186](https://osgeo-org.atlassian.net/browse/GEOS-11186) Fix maven enforcer failFast
* [GEOS-11220](https://osgeo-org.atlassian.net/browse/GEOS-11220) Upgrade Hazelcast from 5.3.1 to 5.3.6
* [GEOS-11245](https://osgeo-org.atlassian.net/browse/GEOS-11245) Update OSHI from 6.2.2 to 6.4.10
* [GEOS-11316](https://osgeo-org.atlassian.net/browse/GEOS-11316) Update Spring version to 5.3.32

For the complete list see [2.25-RC](https://github.com/geoserver/geoserver/releases/tag/2.25-RC) release notes. 

## Community Updates

Community module development:

* [GEOS-11146](/browse/GEOS-11146) Fix MBTiles output format test
* [GEOS-11150](/browse/GEOS-11150) Community module geoserver-monitor-kafka
* [GEOS-11209](/browse/GEOS-11209) Open ID Connect Proof Key of Code Exchange (PKCE)
* [GEOS-11212](/browse/GEOS-11212) OIDC accessToken verification using only JWKs URI
* [GEOS-11219](/browse/GEOS-11219) Upgraded mail and activation libraries for SMTP compatibility
* [GEOS-11293](/browse/GEOS-11293) Improve performance of wps-lontigudinal-profile

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.25 Series

Additional information on GeoServer 2.25 series:

* [GeoServer 2.25 User Manual](https://docs.geoserver.org/2.25.x/en/user/)
* [GeoServer 2024 Roadmap Plannings]({% post_url 2024-01-03-roadmap %}) 
* [MkDocs Proposal](https://github.com/geoserver/geoserver/wiki/GSIP-221)

Release notes:
( [2.25-RC](https://github.com/geoserver/geoserver/releases/tag/2.25-RC)
) 

