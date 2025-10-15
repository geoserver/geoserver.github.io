---
author: Jody Garnett
date: 2025-10-14
layout: post
title: GeoServer 2.28.0 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_228
version: 2.28.0
jira_version: 17471
--- 

GeoServer [2.28.0](/release/2.28.0/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.0/geoserver-2.28.0-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.0/geoserver-2.28.0-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.0/GeoServer-2.28.0-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.0/geoserver-2.28.0-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.0/extensions/).

This is a stable release of GeoServer, recommended for production use.
GeoServer 2.28.0 is made in conjunction with GeoTools 34.0, GeoWebCache 1.28.0, ImageIO-Ext 2.0.0, and ImageN 0.9.0.

Thanks to Jody Garnett (GeoCat) for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is an important upgrade for production systems.

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Upgrade instructions

Please take note of the [Upgrade Instructions](https://docs.geoserver.org/2.28.x/en/user/installation/upgrade.html), specifically:

* This release requires **Java 17 LTS** minimum, **Java 11 is no longer supported**.

  GeoServer is tested with Long Term Support releases: Java 17 LTS and Java 21 LTS.
  For more information see [Java Considerations](https://docs.geoserver.org/2.28.x/en/user/production/java.html) in the user manual.

* The global setting Unrestricted XML External Entity Resolution has been replaced with the `ENTITY_RESOLUTION_UNRESTRICTED` application property.
  
  This change primarily affects application schema users that have not yet adopted ``ENTITY_RESOLUTION_ALLOWLIST``. See [update instructions](https://docs.geoserver.org/2.28.x/en/user/installation/upgrade.html#entity-resolution-unrestricted-application-property-geoserver-2-26-4-and-newer) for details.

* Due to a [user interface change](https://docs.geoserver.org/2.28.x/en/user/installation/upgrade.html#keystore-password-link-geoserver-2-26-and-newer),
  it is no longer necessary to generate a masterpw.info when upgrading an older data directory.

  If this file is present from an earlier upgrade, it is still considered a security warning and is noted on the welcome page.

## Image Processing Engine updated

Updating the image processing engine used by GeoServer to be Java 17 compatible is one of the first major objectives of the GeoServer 3 crowdfunding activity. We are pleased to provide the upgrade from Java Advanced Imaging 1.1.3 to Eclipse ImageN 0.9.0 as part of the GeoServer 2.28.0 release.

<img src="/img/posts/2.28/imagen-migration.png" alt="JAI 1.1.3 to ImageN 0.9.0 Migration" style="display:block; margin-left:auto; margin-right:auto; scale:70%;"/>

Eclipse ImageN 0.9.0 is a stable release of two established codebases (Java Advanced Imaging and JAI-Ext) combined together into a single project. ImageN 1.0.0 will be released once the team has had an opportunity to increase the test coverage and update the user manual, over the course of the GeoServer 3.0 series. 

Thanks to the Jody (GeoCat), Andrea and Daniele (GeoSolutions) for this work and GeoServer 3 Crowdfunding for accomplishing this key objective for the future of GeoServer. We would also like to thank the Eclipse Foundation for working with Oracle to finally make this Sun Microsystems technology open source, alongside OpenJDK.

For more information see [Eclipse ImageN](https://eclipse-imagen.github.io/imagen/) and updated Wikipedia Entry for [Java Advanced Imaging](https://en.wikipedia.org/wiki/Java_Advanced_Imaging).

## Legend: Symbology Encoding Functions

This release includes a long-awaited improvement for legend graphic generation - creating a legend graphic when the Symbology Encoding `Recode`, `Interpolate` and `Categorize` functions are used.

``` xml
<Fill>
  <CssParameter name="fill">
    <ogc:Function name="Recode">
      <!-- Value to Transform -->
      <ogc:Function name="strTrim">
        <ogc:PropertyName>SUB_REGION</ogc:PropertyName>
      </ogc:Function>
      <!-- Map of input to output values -->
      <ogc:Literal>N Eng</ogc:Literal>   <ogc:Literal>#6495ED</ogc:Literal>
      <ogc:Literal>Mid Atl</ogc:Literal> <ogc:Literal>#B0C4DE</ogc:Literal>
      <ogc:Literal>S Atl</ogc:Literal>   <ogc:Literal>#00FFFF</oac:Literal>
      <ogc:Literal>E N Cen</ogc:Literal> <ogc:Literal>#9ACD32</ogc:Literal>
      <ogc:Literal>E S Cen</ogc:Literal> <ogc:Literal>#00FA9A</ogc:Literal>
      <ogc:Literal>W N Cen</ogc:Literal> <ogc:Literal>#FFF8DC</ogc:Literal>
      <ogc:Literal>W S Cen</ogc:Literal> <ogc:Literal>#F5DEB3</ogc:Literal>
      <ogc:Literal>Mtn</ogc:Literal>     <ogc:Literal>#F4A460</ogc:Literal>
      <ogc:Literal>Pacific</ogc:Literal> <ogc:Literal>#87CEEB</ogc:Literal>
    </ogc:Function>
  </CssParameter>
</Fill>
```

<img src="/img/posts/2.28/se-fn-legend.png" alt="Symbology Encoding Legend"/>

Thanks to Andrea (GeoSolutions) for this improvement.

* [GEOS-8002](https://osgeo-org.atlassian.net/browse/GEOS-8002) LegendGraphic does not display when using transformation functions (recode, interpolate, categorize)

## OAuth2 OpenID Connect community modules

A new community module **sec-oidc** is now available based directly on Spring Security Core.  This new community module is intended as a direct replacement for the existing **sec-oauth2-geonode**, **sec-oauth2-github**, **sec-oauth2-google**, and **sec-oauth2-openid-connect**plugins which have reached end of life.

<img src="/img/posts/2.28/oidc-keycloak.png" alt="keycloak settings" style="display:block; margin-left:auto; margin-right:auto; scale:70%;"/>

For more information see [OAUTH2 OIDC](https://docs.geoserver.org/2.28.x/en/user/community/oidc/index.html) in the user manual. Extensive information (and notes) are provided for working with Google, GitHub, Microsoft Azure, and Keycloak.  We are really pleased that the new OIDC community plugin is available alongside the existing OAuth2 implementations for comparison and testing.

The initial work was performed by Andreas Watermeyer (ITS Digital Solutions), and completed for GeoServer 2.28.0 by  David Blasby (GeoCat), Ian Turton, and Alessio Fabiani (GeoSolutions). Thanks to the GeoServer 3 Crowdfunding sponsors for supporting this important development.

## Developer Updates

A number of significant changes affect developers working on the GeoServer codebase:

* The change to Java 17 LTS minimum brings new language features to the codebase 

* Java 17 build improvements 

* Maven bill-of-materials import to manage both GeoTools library modules and syncrhonize third-party dependencies with the GeoTools project.

Thanks to Gabriel Roldan (Camptocamp) for working on these activities on behalf of GeoServer 3 sponsors.

### GeoTools bill-of-materials 

## Release notes

New Feature:

* [GEOS-11949](https://osgeo-org.atlassian.net/browse/GEOS-11949) Support MS Excel download from WPS-download
* [GEOS-11800](https://osgeo-org.atlassian.net/browse/GEOS-11800) Implement GeoServer WPS SpatioTemporalZonalStatistics process
* [GEOS-11911](https://osgeo-org.atlassian.net/browse/GEOS-11911) Application property ROOT_LOGIN_ENABLED

Improvement:

* [GEOS-11297](https://osgeo-org.atlassian.net/browse/GEOS-11297) Escape WMS GetFeatureInfo HTML output by default
* [GEOS-11934](https://osgeo-org.atlassian.net/browse/GEOS-11934) Image processing tile cache: better logging and deeper cleanups
* [GEOS-11788](https://osgeo-org.atlassian.net/browse/GEOS-11788) Apply feedback from CSP testing
* [GEOS-11833](https://osgeo-org.atlassian.net/browse/GEOS-11833) Unnecessary antiCache parameter on some GUI images
* [GEOS-11837](https://osgeo-org.atlassian.net/browse/GEOS-11837) MapML Support for LayerGroups
* [GEOS-11867](https://osgeo-org.atlassian.net/browse/GEOS-11867) Improve entity resolution
* [GEOS-11892](https://osgeo-org.atlassian.net/browse/GEOS-11892) Column mentioning user that performed last modification for layers and stores list UI
* [GEOS-11938](https://osgeo-org.atlassian.net/browse/GEOS-11938) Add support for property selection in OGC API Features

Bug:

* [GEOS-11823](https://osgeo-org.atlassian.net/browse/GEOS-11823) Quality Degradation in Scanned Map Rendering (GeoServer 2.25.3 onward)
* [GEOS-11944](https://osgeo-org.atlassian.net/browse/GEOS-11944) GetLegendGraphic Fails When Using RasterSymbolizer With Interval ColorMap And ENV variables
* [GEOS-11946](https://osgeo-org.atlassian.net/browse/GEOS-11946) DirectRasterRenderer may fail on creating AlphaBand from ROI using Lookup
* [GEOS-11957](https://osgeo-org.atlassian.net/browse/GEOS-11957) Cannot logout due remember-me cookie with oidc 
* [GEOS-10728](https://osgeo-org.atlassian.net/browse/GEOS-10728) Cannot download GeoPackage if the source data contains UUID types
* [GEOS-11274](https://osgeo-org.atlassian.net/browse/GEOS-11274) Cannot get a JSON legend with an external reference to a non published directory
* [GEOS-11620](https://osgeo-org.atlassian.net/browse/GEOS-11620) Smart Data Loader plugin for GeoServer 2.26 produces a Mapping file data source definition and tries to establish a connection pool, but fails
* [GEOS-11688](https://osgeo-org.atlassian.net/browse/GEOS-11688) After restart unable to load External Style SLD when requesting multiple tiles
* [GEOS-11708](https://osgeo-org.atlassian.net/browse/GEOS-11708) STAC breadcrumbs rendering as plain text
* [GEOS-11751](https://osgeo-org.atlassian.net/browse/GEOS-11751) Symbolizer URL in GetLegendGraphic JSON Request is Broken
* [GEOS-11808](https://osgeo-org.atlassian.net/browse/GEOS-11808) Attribute names containing characters the XML Encoder can't handle are accepted for input, causing errors
* [GEOS-11832](https://osgeo-org.atlassian.net/browse/GEOS-11832) count=0 service exception for some formats
* [GEOS-11857](https://osgeo-org.atlassian.net/browse/GEOS-11857) Random NPE In LocalWorkspaceCallback
* [GEOS-11860](https://osgeo-org.atlassian.net/browse/GEOS-11860) MapML does not match raster rendering geometry simplification behavior
* [GEOS-11862](https://osgeo-org.atlassian.net/browse/GEOS-11862) Layer Preview and Tile Layers page dropdown links broken after updating table
* [GEOS-11863](https://osgeo-org.atlassian.net/browse/GEOS-11863) Use GetTile or GetMap requests in <map-tile src> for cached raster coverages where appropriate
* [GEOS-11865](https://osgeo-org.atlassian.net/browse/GEOS-11865) MapDownloadProcess washes out 1 band gray images when transparency is on
* [GEOS-11866](https://osgeo-org.atlassian.net/browse/GEOS-11866) Prevent requests setting variables that should only be set by GeoServer
* [GEOS-11879](https://osgeo-org.atlassian.net/browse/GEOS-11879) Xalan causes a java.lang.NoClassDefFoundError
* [GEOS-11902](https://osgeo-org.atlassian.net/browse/GEOS-11902) More compact, easier to maintain conformance configuration UI
* [GEOS-11910](https://osgeo-org.atlassian.net/browse/GEOS-11910) JMS Cluster settings Section is not showing properly
* [GEOS-11917](https://osgeo-org.atlassian.net/browse/GEOS-11917) INSPIRE configuration does not get properly saved when OGC API module is included
* [GEOS-11931](https://osgeo-org.atlassian.net/browse/GEOS-11931) GeoServer binary package fails to start after Jetty 9.x to 10.0.25 upgrade

Task:

* [GEOS-11956](https://osgeo-org.atlassian.net/browse/GEOS-11956) Fix build server WfsCompatibilityTest failure (when testing against "local" GeoServer on port 8080)
* [GEOS-11813](https://osgeo-org.atlassian.net/browse/GEOS-11813) Create REST API For Security Providers
* [GEOS-11814](https://osgeo-org.atlassian.net/browse/GEOS-11814) Create a REST API for Filter Chains
* [GEOS-11815](https://osgeo-org.atlassian.net/browse/GEOS-11815) Create authentication filter REST API
* [GEOS-11831](https://osgeo-org.atlassian.net/browse/GEOS-11831) OseoDispatcherCallback improvements
* [GEOS-11852](https://osgeo-org.atlassian.net/browse/GEOS-11852) Remove master password info page
* [GEOS-11853](https://osgeo-org.atlassian.net/browse/GEOS-11853) Clarify keystore vs master vs root password
* [GEOS-11854](https://osgeo-org.atlassian.net/browse/GEOS-11854) Generation of security/masterpw.info no longer required
* [GEOS-11855](https://osgeo-org.atlassian.net/browse/GEOS-11855) global settings cog warning in release data directory
* [GEOS-11869](https://osgeo-org.atlassian.net/browse/GEOS-11869) Replace entity resolution setting with application property
* [GEOS-11881](https://osgeo-org.atlassian.net/browse/GEOS-11881) Update postgis-jdbc
* [GEOS-11882](https://osgeo-org.atlassian.net/browse/GEOS-11882) Cleanup postgis-jdbc dependencies
* [GEOS-11932](https://osgeo-org.atlassian.net/browse/GEOS-11932) Upgrade Oracle JDBC driver to Java 17

For the complete list see [2.28.0](https://github.com/geoserver/geoserver/releases/tag/2.28.0) release notes. 

## Community Updates

Community module development:

* [GEOS-11848](https://osgeo-org.atlassian.net/browse/GEOS-11848) Migrate use of JAITools to JAI-Ext
* [GEOS-11951](https://osgeo-org.atlassian.net/browse/GEOS-11951) Add PMTiles DataStore community module for reading Protomaps vector tiles
* [GEOS-11816](https://osgeo-org.atlassian.net/browse/GEOS-11816) Features templating OGC API fetch by ID fails
* [GEOS-11819](https://osgeo-org.atlassian.net/browse/GEOS-11819) Make smart data loader skip unsupported column types
* [GEOS-11822](https://osgeo-org.atlassian.net/browse/GEOS-11822) OGC API procesess basic implementation
* [GEOS-11829](https://osgeo-org.atlassian.net/browse/GEOS-11829) Features templating ability to override schema
* [GEOS-11839](https://osgeo-org.atlassian.net/browse/GEOS-11839) New Community Module for WPS Download in NetCDF output format for spatiotemporal coverages
* [GEOS-11870](https://osgeo-org.atlassian.net/browse/GEOS-11870) Singlestore(MemSql) datastore community module
* [GEOS-11885](https://osgeo-org.atlassian.net/browse/GEOS-11885) Smart Data Loader does not support postgresql UUID data type
* [GEOS-11887](https://osgeo-org.atlassian.net/browse/GEOS-11887) Features Templating does not returns content type and charset header on OGC-API

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

## Developer updates

* [GEOS-11845](https://osgeo-org.atlassian.net/browse/GEOS-11845) GSIP-232 Upgrade GeoServer and GeoWebCache Build to Java 17
* [GEOS-11943](https://osgeo-org.atlassian.net/browse/GEOS-11943) remove PDF generation of manual from build process
* [GEOS-11952](https://osgeo-org.atlassian.net/browse/GEOS-11952) GeoServer 2.28.0 Release cleanup
* [GEOS-11836](https://osgeo-org.atlassian.net/browse/GEOS-11836) Upgrade ErrorProne to 2.31.0
* [GEOS-11843](https://osgeo-org.atlassian.net/browse/GEOS-11843) Use Spring framework BOM to manage Spring and Spring Security dependencies
* [GEOS-11851](https://osgeo-org.atlassian.net/browse/GEOS-11851) Remove unnecessary javac lint suppressions
* [GEOS-11858](https://osgeo-org.atlassian.net/browse/GEOS-11858) Update to PMD 7.14 and enable unnecessary suppression rule

# About GeoServer 2.28 Series

Additional information on GeoServer 2.28 series:

* [GeoServer 2.28 User Manual](https://docs.geoserver.org/2.28.x/en/user/)

Release notes:
( [2.28.0](https://github.com/geoserver/geoserver/releases/tag/2.28.0)
| [2.28-M0](https://github.com/geoserver/geoserver/releases/tag/2.28-M0)
) 

