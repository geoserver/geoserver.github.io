---
author: Jody Garnett
date: 2026-06-11
layout: post
title: GeoServer 3.0.0 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_30
version: 3.0.0
jira_version: 17404
--- 

GeoServer [3.0.0](/release/3.0.0/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.0/geoserver-3.0.0-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.0/geoserver-3.0.0-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.0/GeoServer-3.0.0-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.0/geoserver-3.0.0-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.0/extensions/).

This is a stable release of GeoServer 3.0.x series.
GeoServer 3.0.0 is made in conjunction with GeoTools 35.0, and GeoWebCache 2.0.0. 

Thanks to Jody Garnett (GeoCat), and Peter Smythe (AfriGIS) for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is an important upgrade for production systems.

* [GEOS-12043](https://osgeo-org.atlassian.net/browse/GEOS-12043) CVE-2025-27511 JNDI Vulnerability in DB2 Store Connection
* [GEOS-11920](https://osgeo-org.atlassian.net/browse/GEOS-11920) CVE-2025-58175 Server-Side Request Forgery (SSRF) Vulnerability in XML entity resolution
* [GEOS-11918](https://osgeo-org.atlassian.net/browse/GEOS-11918) CVE-2025-52465 Arbitrary file write vulnerability in Master Password Dump Page
* [GEOS-11777](https://osgeo-org.atlassian.net/browse/GEOS-11777) CVE-2024-45747 Server-Side Template Injection (SSTI) vulnerability in processing FreeMarker templates

The use of the CVE system allows the GeoServer team to reach a wider audience than blog posts. 

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Welcome to GeoServer 3

We are overjoyed to share the initial release of GeoServer 3 with our community, this is the final stretch of a long road, a year of development, and a lot of planning and support to make it all happen. Thanks to all the organizations and individuals supporting GeoServer 3.

<a href="/img/posts/3.0/welcome-global.png" target="_blank" rel="noopener">
  <img src="/img/posts/3.0/welcome-global.png" alt="GeoServer 3" class="screensnap"
     style="max-width: 95%"/>
</a>

### Straightforward upgrade

Special care has been taken to ensure a seamless upgrade from GeoServer 2.28.x:

1. Important: We have made **no changes** to the GeoServer Data Directory.

2. A few modules have migrated from core to extensions:

   * [WCS 1.0](https://docs.geoserver.org/latest/en/user/services/wcs/install/) and [WCS 1.1](https://docs.geoserver.org/latest/en/user/services/wcs/install/)
   * [World Image](https://docs.geoserver.org/latest/en/user/data/raster/arcgrid/#arcgrid_install) and [ArcGRID](https://docs.geoserver.org/latest/en/user/data/raster/arcgrid/#arcgrid_install) raster data sources.
   * [KML](https://docs.geoserver.org/main/en/user/extensions/kml/) output format
    
   The pure Java `H2` database is no longer provided.
   
3. The [log file location](https://docs.geoserver.org/latest/en/user/configuration/logging/#logging_location) setting
   is now managed using the `GEOSERVER_LOG_LOCATION` application property.
   
4. The NetCDF index support has been simplified and is now self-contained. With this improvement, NetCDF
   no longer needs a database or local `.idx` files to operate.
   
   Instructions are provided for how to clean up these now unused files.
   
5. The new [OIDC](https://docs.geoserver.org/main/en/user/extensions/oidc/) plugin is now available
   as a full extension.
   
   This plugin takes over the responsibilities of the previously available `Keycloak` and `OAuth2` plugins.
   For guidance on upgrading please see the detailed  [migration guide](https://docs.geoserver.org/main/en/user/extensions/oidc/migrating/).

Please see the [upgrade instructions](https://docs.geoserver.org/latest/en/user/installation/upgrade3/) for details.

### Thanks to the GeoServer 3 Sponsors

GeoServer 3 would not exist without the organizations and individuals who supported the [GeoServer 3 crowdfunding campaign](/sponsor/gs3-crowdfunding). Their sponsorship made this work possible. We also want to share a [final message to reflect over the campaign, its results, and thank again everyone that participate]({% post_url 2026-06-11-geoserver-3-0-0-here-crowdfunding %}).

{% include gs3-sponsors.html %}

## New Context-Driven User Experience

GeoServer 3 features a new "context-driven" user experience, which we really hope you enjoy.

* **Search**: Using the left hand side search field to find information. Autocomplete results are shown as you type, and results are listed in a tree which can be navigated below.

  <a href="/img/posts/3.0/context-search.png" target="_blank" rel="noopener">
    <img src="/img/posts/3.0/context-search.png" alt="User Interface Search" class="screensnap"/>
  </a>
  
* **Context**: Clicking on a search item establishes the context which is shown as breadcrumbs along the top of the page.
  A drop-down context menu provides quick access to actions that can be performed.

  <a href="/img/posts/3.0/context-menu.png" target="_blank" rel="noopener">
    <img src="/img/posts/3.0/context-menu.png" alt="User Interface Context Menu" class="screensnap"/>
  </a>
  
* **Page**: Page content adjusts to the current context. The welcome page adjusts to showing the layer tile and description, along with preview links, sample data downloads, metadata and data links configured.

  <a href="/img/posts/3.0/welcome-layer.png" target="_blank" rel="noopener">
    <img src="/img/posts/3.0/welcome-layer.png" alt="User Interface Welcome Layer Page" class="screensnap"/>
  </a>
  
* **Menu**: The menu bar at the top of the page provides login on the right hand side, and access to the familiar GeoServer top-level menus. Many of these pages now adjust their content to reflect the current context.

  <a href="/img/posts/3.0/menus.png" target="_blank" rel="noopener">
    <img src="/img/posts/3.0/menus.png" alt="User Interface Top Level Menus" class="screensnap"/>
  </a>

* **Feedback**: Admins are provided additional context-menu commands, and per-layer feedback and shortcuts,
  making the application easier and faster to use.

  <a href="/img/posts/3.0/welcome-layer-feedback.png " target="_blank" rel="noopener">
    <img src="/img/posts/3.0/welcome-layer-feedback.png " alt="User Interface Feedback" class="screensnap"
     style="max-width: 50%"/>
  </a>

For more information see the [user guide](https://docs.geoserver.org/main/en/user/webadmin/).

Thanks to Stefano Bovio (GeoSolutions), Jody Garnett (GeoCat), and others for this major improvement.

### New User Interface Responsive Design Theme

GeoServer now provides a responsive-design theme:

* **Navigation**: Navigation is reduced to a hamburger menu when using a narrow width display.

  <a href="/img/posts/3.0/menus-responsive.png" target="_blank" rel="noopener">
    <img src="/img/posts/3.0/menus-responsive.png" alt="Responsive Theme: Menus" class="screensnap"
     style="max-width: 50%"/>
  </a>

* **Forms**: Forms have adopted a two-column layout adapting to page width.
  
  <a href="/img/posts/3.0/form-two-column.png" target="_blank" rel="noopener">
    <img src="/img/posts/3.0/form-two-column.png" alt="Responsive Theme: Form two-column layerout" class="screensnap"
     style="max-width: 50%"/>
  </a>

Thanks to Stefano Bovio (GeoSolutions) for leading this frequently requested improvement, the entire GeoServer 3 team for implementing and checking, and testers at AfriGIS and GeoCat for verifying and updating screenshots.

### New Layer Preview

A new full-screen layer preview is provided using the latest OpenLayers library.

<a href="/img/posts/3.0/ol-preview.png" target="_blank" rel="noopener">
  <img src="/img/posts/3.0/ol-preview.png" alt="New full screen layer preview" class="screensnap"/>
</a>

Thanks to Stefano Bovio (GeoSolutions) for the welcome improvement.

## Updated Environment

GeoServer 3 requires Tomcat 11.0.x and Jetty 12.1 application servers. We are really pleased with this accomplishment after completing our transition to Spring Framework 7 and Jakarta EE Servlet API 6.1.

We have been extensively testing GeoServer 3 with Java 17 and Java 21, maintaining the same Java runtime baseline as GeoServer 2.28.x. Java 25 is subject to automated testing, but we are going to hold off recommending it until the user community has had an opportunity to try it out and report back.

If you are wondering about the compatibility between the Java web stack and GeoServer, here is a table showing the various supported options:

| GeoServer        | Java   | Tomcat        | Jetty      | Java EE       | Jakarta EE      |
| ---------------- | ------ | ------------- | ---------- | ------------- | ---------------- |
| GeoServer 3.0    | 17, 21 | Tomcat 11.0.x | Jetty 12.1 |               | Servlet API 6.1 |
| Not supported    |       | Tomcat 10.1.x | Jetty 12.0 |               | Servlet API 6.0 |
| Not supported    |       | Tomcat 10.0.x | Jetty 11.0 |               | Servlet API 5.0 |
| GeoServer 2.28.x | 17, 21 | Tomcat 9.x   |            | Servlet API 4 |                  |
| GeoServer 2.28.x | 17, 21 |              | Jetty 9.4  | Servlet API 3.1 |                |
{: .compat-table }

For more information see [container considerations](https://docs.geoserver.org/latest/en/user/production/container/).

Thanks to the entire GeoServer 3 team and [crowdfunding campaign](/sponsor/gs3-crowdfunding) for this major accomplishment, representing the completion of Milestone 3.

## OAuth2 OpenID Connect Extension

The new OAuth2 OpenID Connect Security Integration (OIDC) plugin is now an official extension.

The transition to Spring Security 7 was one of the big tasks accomplished for GeoServer 3. This work includes the creation of a new `OIDC` plugin. The new plugin has taken over the responsibilities of previously available `Keycloak` and `OAuth2` plugins.

For guidance on upgrading please see the detailed  [migration guide](https://docs.geoserver.org/main/en/user/extensions/oidc/migrating/).

Thanks to Alessio Fabiani and others for this important improvement. Special thanks to everyone who provided feedback and testing during the 3.0-RC timeframe, your success has allowing this module to graduate to full extension for 3.0.0 release.

## New Documentation

The long-awaited transition to Markdown documentation has finally arrived. Welcome to our new [User Manual](https://docs.geoserver.org/latest/en/user/).  The GeoServer 2.x documentation is available using the version switcher at the top of the page.

<a href="https://docs.geoserver.org/main/en/user/">
  <img src="/img/posts/3.0/user-manual.png" alt="The new user manual" class="screensnap"/>
</a>

Please help out by fixing any remaining [small issues](https://docs.geoserver.org/latest/en/docguide/quickfix/) or log an issue for Peter to address. The [documentation guide has been updated with Markdown guidance](https://docs.geoserver.org/main/en/docguide/markdown/) complete with visual examples.

Thanks to Peter Smythe (AfriGIS) and Jody Garnett (GeoCat) for working on this activity which ended up being an incredible amount of work.

### Pending Community Modules

Tee documentation contains a new heading for [pending community modules](https://docs.geoserver.org/main/en/user/community/#pending-community-modules) that are seeking public use and support in order
to graduate to an extension.

A pending community been declared ready for feedback by the development team responsible and is available for general download alongside each release. The user manual indicates what specific support is needed for the module to be ready for production as a full extension.

## Release notes

New Feature:

* [GEOS-12063](https://osgeo-org.atlassian.net/browse/GEOS-12063) GSIP-238 - GeoServer 3 UI / UX Refresh
* [GEOS-12132](https://osgeo-org.atlassian.net/browse/GEOS-12132) GSIP 239 ‐ Promote OIDC Community Module to Extension

Improvement:

* [GEOS-11581](https://osgeo-org.atlassian.net/browse/GEOS-11581) Set up leaner attribute transformations when attribute customization is enabled
* [GEOS-11886](https://osgeo-org.atlassian.net/browse/GEOS-11886) Sort entries in all .properties files alphabetically
* [GEOS-11918](https://osgeo-org.atlassian.net/browse/GEOS-11918) CVE-2025-52465 Arbitrary file write vulnerability in Master Password Dump Page
* [GEOS-12015](https://osgeo-org.atlassian.net/browse/GEOS-12015) Switch tests using H2 to GeoPackage
* [GEOS-12023](https://osgeo-org.atlassian.net/browse/GEOS-12023) Improve developer logging during catalog resources loading and WMS capabilities requests
* [GEOS-12024](https://osgeo-org.atlassian.net/browse/GEOS-12024) Add Git branch name in GEOSERVER_NODE_OPTS
* [GEOS-12070](https://osgeo-org.atlassian.net/browse/GEOS-12070) REST Support for CRSs
* [GEOS-12072](https://osgeo-org.atlassian.net/browse/GEOS-12072) Remove deprecated REST endpoint on the DataStoreFileController
* [GEOS-12077](https://osgeo-org.atlassian.net/browse/GEOS-12077) Remove H2/DB based index and binary index from CoverageMultidim/NetCDF stores
* [GEOS-12081](https://osgeo-org.atlassian.net/browse/GEOS-12081) Update MapML.js (<mapml-viewer> custom element suite) to v0.17.0
* [GEOS-12082](https://osgeo-org.atlassian.net/browse/GEOS-12082) CoverageStore - quick fail for incorrect files
* [GEOS-12083](https://osgeo-org.atlassian.net/browse/GEOS-12083) Skip brute force login delays when checking for default administrator password
* [GEOS-12103](https://osgeo-org.atlassian.net/browse/GEOS-12103) Reduce contention in concurrent requests

Bug:

* [GEOS-10509](https://osgeo-org.atlassian.net/browse/GEOS-10509) WFS Request fails when XML POST body is larger than 8kB
* [GEOS-10877](https://osgeo-org.atlassian.net/browse/GEOS-10877) [B/R Community Module] Restore Tasklet always fails on resources validation
* [GEOS-11777](https://osgeo-org.atlassian.net/browse/GEOS-11777) CVE-2024-45747 Server-Side Template Injection (SSTI) vulnerability in processing FreeMarker templates
* [GEOS-11903](https://osgeo-org.atlassian.net/browse/GEOS-11903) WPS does not respect raw response output selection when there are multiple outputs
* [GEOS-11916](https://osgeo-org.atlassian.net/browse/GEOS-11916) Data directory migration performed on built-in default security configuration
* [GEOS-11920](https://osgeo-org.atlassian.net/browse/GEOS-11920) CVE-2025-58175 Server-Side Request Forgery (SSRF) Vulnerability in XML entity resolution
* [GEOS-11926](https://osgeo-org.atlassian.net/browse/GEOS-11926) ogcapi plugin makes WFS advertising an outputFormat which is actually unavailable
* [GEOS-11930](https://osgeo-org.atlassian.net/browse/GEOS-11930) OGC-API extension breaks security REST API 
* [GEOS-11942](https://osgeo-org.atlassian.net/browse/GEOS-11942) ImagePPIO does not run any longer
* [GEOS-11964](https://osgeo-org.atlassian.net/browse/GEOS-11964) Metadata Bulk Operations: wicket error
* [GEOS-11965](https://osgeo-org.atlassian.net/browse/GEOS-11965) KMZ export incorrectly references remote icon URLs instead of embedding them in the KMZ archive
* [GEOS-11981](https://osgeo-org.atlassian.net/browse/GEOS-11981) POST /security/authproviders | 400: Unsupported className
* [GEOS-11988](https://osgeo-org.atlassian.net/browse/GEOS-11988) Fix bug: preserve metaTilingThreads=0 in saneConfig()
* [GEOS-11999](https://osgeo-org.atlassian.net/browse/GEOS-11999) The version of Jetty (12) no longer supports web.xml CORS configuration
* [GEOS-12043](https://osgeo-org.atlassian.net/browse/GEOS-12043) CVE-2025-27511 JNDI Vulnerability in DB2 Store Connection
* [GEOS-12065](https://osgeo-org.atlassian.net/browse/GEOS-12065) WMS Layer REST PUT always returns 500 due to Collections.emptySet() in getRemoteStyleInfos()
* [GEOS-12073](https://osgeo-org.atlassian.net/browse/GEOS-12073) Remove log location configuration from Admin Console and REST API
* [GEOS-12084](https://osgeo-org.atlassian.net/browse/GEOS-12084) TemplateController REST endpoints accept non-existent workspace, store, and resource names
* [GEOS-12085](https://osgeo-org.atlassian.net/browse/GEOS-12085) LocalSettingsController does not validate workspace existence
* [GEOS-12092](https://osgeo-org.atlassian.net/browse/GEOS-12092) DescribeFeatureType fails to render a single option restriction in JSON format
* [GEOS-12112](https://osgeo-org.atlassian.net/browse/GEOS-12112) OIDC OAuth2 login principals should also expose GeoServer user properties
* [GEOS-12114](https://osgeo-org.atlassian.net/browse/GEOS-12114) GeoServer fails to start on FIPS-enabled system due to unsupported SHA1PRNG SecureRandom
* [GEOS-12115](https://osgeo-org.atlassian.net/browse/GEOS-12115) Jetty 12.1.9 is not parsing Windows working directory settings
* [GEOS-12118](https://osgeo-org.atlassian.net/browse/GEOS-12118) ReprojectingFeatureCollection can fail with ClassCastException while inserting CompoundCurve via WFS-T

Task:

* [GEOS-11941](https://osgeo-org.atlassian.net/browse/GEOS-11941) Clean up Java 17 javadoc warnings
* [GEOS-11987](https://osgeo-org.atlassian.net/browse/GEOS-11987) ImageN 0.9.1 migration requires renaming of registryFile.jai to registryFile.imagen
* [GEOS-12004](https://osgeo-org.atlassian.net/browse/GEOS-12004) Make WMS indepependent of WFS
* [GEOS-12005](https://osgeo-org.atlassian.net/browse/GEOS-12005) Remove GeoServer H2 extension
* [GEOS-12006](https://osgeo-org.atlassian.net/browse/GEOS-12006) GWC, removal of leftover H2 references
* [GEOS-12011](https://osgeo-org.atlassian.net/browse/GEOS-12011) Move KML module to extension
* [GEOS-12016](https://osgeo-org.atlassian.net/browse/GEOS-12016) Move WCS 1.1 module to extension
* [GEOS-12017](https://osgeo-org.atlassian.net/browse/GEOS-12017) Move WCS 1.0 to extension
* [GEOS-12018](https://osgeo-org.atlassian.net/browse/GEOS-12018) Switch GeoServer tests away from H2
* [GEOS-12019](https://osgeo-org.atlassian.net/browse/GEOS-12019) Turn arcgrid and worldimage formats into plugins
* [GEOS-12025](https://osgeo-org.atlassian.net/browse/GEOS-12025) Split WMS 1.1 and 1.3
* [GEOS-12040](https://osgeo-org.atlassian.net/browse/GEOS-12040) Updating BouncyCatle libraries to LTS 2.73.10
* [GEOS-12041](https://osgeo-org.atlassian.net/browse/GEOS-12041) Update Spring LDAP to 4.0.1
* [GEOS-12064](https://osgeo-org.atlassian.net/browse/GEOS-12064) CSS: add documentation for localized @title and @abstract metadata
* [GEOS-12071](https://osgeo-org.atlassian.net/browse/GEOS-12071) Remove the WPS remote module
* [GEOS-12110](https://osgeo-org.atlassian.net/browse/GEOS-12110) Make use of XMLUtils for better integration with GeoTools.getEntityResolver()
* [GEOS-12136](https://osgeo-org.atlassian.net/browse/GEOS-12136) IOTestUtils.createRandomDirectory() replacing mkdir call to more recent java.nio.files API
* [GEOS-12137](https://osgeo-org.atlassian.net/browse/GEOS-12137) Update OSHI from 6.8.2 to 7.3.0

Sub-task:

* [GEOS-12066](https://osgeo-org.atlassian.net/browse/GEOS-12066) Present keywords as a table
* [GEOS-12067](https://osgeo-org.atlassian.net/browse/GEOS-12067) Add Full Screen OpenLayers 10.8.0 layer preview
* [GEOS-12086](https://osgeo-org.atlassian.net/browse/GEOS-12086) Keyboard navigation for file browser

For the complete list see [3.0.0](https://github.com/geoserver/geoserver/releases/tag/3.0.0) release notes. 

## Community Updates

Community module development:

* [GEOS-11904](https://osgeo-org.atlassian.net/browse/GEOS-11904) OGC API Processes: add support for envelope input/output
* [GEOS-11905](https://osgeo-org.atlassian.net/browse/GEOS-11905) OGC API processes status response lacks jobid and links to self
* [GEOS-11906](https://osgeo-org.atlassian.net/browse/GEOS-11906) OGC API Processes: use correct error code for access to results when execution is not complete
* [GEOS-11907](https://osgeo-org.atlassian.net/browse/GEOS-11907) OGC API Processes: support multiple raw responses
* [GEOS-11908](https://osgeo-org.atlassian.net/browse/GEOS-11908) OGC API Processes page should be pageable
* [GEOS-11909](https://osgeo-org.atlassian.net/browse/GEOS-11909) Add support for OGC API Echo process
* [GEOS-11915](https://osgeo-org.atlassian.net/browse/GEOS-11915) OGC API Processes: improve support for binary input and output
* [GEOS-11972](https://osgeo-org.atlassian.net/browse/GEOS-11972) GSIP 233 - Community Pending Release Profile
* [GEOS-11980](https://osgeo-org.atlassian.net/browse/GEOS-11980) Add support for uploading a single parquet file to GeoServer via REST
* [GEOS-11983](https://osgeo-org.atlassian.net/browse/GEOS-11983) GSR /query fails with HTTP 500 when where parameter is empty
* [GEOS-12000](https://osgeo-org.atlassian.net/browse/GEOS-12000) Ignore DescribeFeatureType requests without typeName in Features Templating schemas override
* [GEOS-12002](https://osgeo-org.atlassian.net/browse/GEOS-12002) hz-cluster: homepage pop-up fails
* [GEOS-12007](https://osgeo-org.atlassian.net/browse/GEOS-12007) Add AWS credential chain authentication UI and documentation for GeoParquet
* [GEOS-12013](https://osgeo-org.atlassian.net/browse/GEOS-12013) Support vector datasets ingestion in VectorMosaic via REST
* [GEOS-12044](https://osgeo-org.atlassian.net/browse/GEOS-12044) STAC search endpoint should report invalid collection names as invalid parameters instead of internal errors
* [GEOS-12061](https://osgeo-org.atlassian.net/browse/GEOS-12061) New Community Module for PNG-WIND output format for wind datasets
* [GEOS-12062](https://osgeo-org.atlassian.net/browse/GEOS-12062) Add DuckDB datastore community extension (gs-duckdb)
* [GEOS-12069](https://osgeo-org.atlassian.net/browse/GEOS-12069) Align the hazelcast version in hz-cluster to the rest of GeoServer
* [GEOS-12074](https://osgeo-org.atlassian.net/browse/GEOS-12074) Remove activeMQ-broker community module
* [GEOS-12089](https://osgeo-org.atlassian.net/browse/GEOS-12089) GWC sqlite community module breaks legend preview in style page
* [GEOS-12098](https://osgeo-org.atlassian.net/browse/GEOS-12098) Rename JWT Header assembly so it is collected for nightly downloads
* [GEOS-12101](https://osgeo-org.atlassian.net/browse/GEOS-12101) Workspace styles not persisted to disk after restore
* [GEOS-12119](https://osgeo-org.atlassian.net/browse/GEOS-12119) Workspace-scoped OGC API Styles endpoint returns styles from other workspaces
* [GEOS-12129](https://osgeo-org.atlassian.net/browse/GEOS-12129) Longitudinal profile positive altitude includes first elevation as ascent from zero

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 3.0 Series

Additional information on GeoServer 3.0 series:

* [GeoServer 3.0 User Manual](https://docs.geoserver.org/3.0.x/en/user/)
* [GeoServer 3.0-RC, a crowdfunded success story]({% post_url 2026-04-21-geoserver-3-rc-crowdfunding-success %})* [GSIP-221](https://github.com/geoserver/geoserver/wiki/GSIP-221) MkDocs Migration
* [GSIP-226](https://github.com/geoserver/geoserver/wiki/GSIP-226) GeoServer 3
* [GSIP-233](https://github.com/geoserver/geoserver/wiki/GSIP-233) Community Pending Profile
* [GSIP-236](https://github.com/geoserver/geoserver/wiki/GSIP-236) Lightening up the Core for GeoServer 3
* [GSIP-238](https://github.com/geoserver/geoserver/wiki/GSIP-238) UI / UX Refresh
* [GSIP 239](https://github.com/geoserver/geoserver/wiki/GSIP-239) Promote OIDC Community Module to Extension

Release notes:
( [3.0.0](https://github.com/geoserver/geoserver/releases/tag/3.0.0)
| [3.0-RC](https://github.com/geoserver/geoserver/releases/tag/3.0-RC)
) 

