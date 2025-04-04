---
author: Gabriel Roldan
date: 2025-04-04
layout: post
title: GeoServer 2.27.0 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_227
version: 2.27.0
jira_version: 16917
--- 

GeoServer [2.27.0](/release/2.27.0/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.0/geoserver-2.27.0-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.0/geoserver-2.27.0-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.0/GeoServer-2.27.0-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.0/geoserver-2.27.0-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.0/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 2.27.0 is made in conjunction with GeoTools 33.0, GeoWebCache 1.27.0, and ImageIO-EXT 1.4.15.

This release graduates the OGC API Features module to extension status, ensures all OGC services pass CITE compliance tests, and adds performance improvements to the catalog loader that significantly reduces startup times for large deployments. The release also includes Smart Data Loader override rules and addresses several security vulnerabilities. Thanks to extensive community testing through our new user forum, we're confident in recommending this release for production use.

Thanks to Gabriel Roldan (Camptocamp) and Jody Garnett (GeoCat) for making this release and to all contributors who helped with this release cycle.

## Community Testing

  This release cycle featured an extensive community testing effort, with our new [discourse communication channels](https://discourse.osgeo.org/c/geoserver/) playing a central role in pre-release
  validation.

  Testers helped identify and resolve several important issues:

  - **Performance** Improvements: Daniel Calliess verified faster startup times and validated the GeoFence plugin functionality.
  - **Security Enhancements**: Georg and Roar Brænden provided detailed feedback on the new Content Security Policy (CSP)
    implementation, helping refine the upgrade instructions.
  - **Catalog Robustness**: Andrea tested the new parallel catalog loader across various data directory configurations,
    identifying and helping resolve concurrency
  edge cases.
  - **Documentation**: Emanuele Tajariol collaborated with Daniel to update GeoFence plugin documentation.
  - **Standards Implementation**: Landry Breuil validated the OGC API Features extension on behalf of the geOrchestra community.

  The GeoServer team is grateful to all community members who participated in this testing effort. Their feedback was instrumental in addressing issues before
  release and ensuring a smooth upgrade experience for users.

  Special thanks to Andrea, Jody, Peter, and Gabriel for their diligent work reviewing feedback and addressing issues throughout the preflight testing period.

<!--
This release cycle we asked our new user forum to test a nightly build.

Daniel Calliess reported indicating startup was slightly faster, and helped double check download links, and GeoFence plugin.
Thanks to Georg for extensive testing and feedback on the CSP Header Policy, working Jody to include the reminder to double check your PROXY_BASE_URL setting before upgrading to 2.27.0.
Thanks to Roar Brænden for testing the effects of new CSP Header Policy and provided feedback for the update instructions.
Thanks to Andrea for testing the catalog loader on several data directories and helping resolve concurrency issues.
Jody helped troubleshoot catalog startup with extensions; and welcome page when starting with an empty "no workspace" data directory.
Thanks to Emanuele Tajariol for working with Daniel on updating the GeoFence plugin docs and wiki.
Thanks to Landry Breuil for testing ogc-api-features on behalf of the geOrchestra community.

Finally, thanks to Andrea, Peter and Gabriel for reviewing feedback and addressing issues thorughout the 2.27.0 preflight testing period.
-->

## Security Considerations

This release addresses several security vulnerabilities, and is a recommended upgrade for production systems.

* [GEOS-11714](https://osgeo-org.atlassian.net/browse/GEOS-11714) CVE-2024-45747 High
* [GEOS-11777](https://osgeo-org.atlassian.net/browse/GEOS-11777) CVE-2025-30146 High

The following vulnerabilities addressed in previous releases are scheduled for Tuesday 22 April 22 public disclosure:

* [GEOS-11778](https://osgeo-org.atlassian.net/browse/GEOS-11778) CVE-2025-30145 High
* [GEOS-11776](https://osgeo-org.atlassian.net/browse/GEOS-11776) CVE-2025-27505 Moderate
* [GEOS-11794](https://osgeo-org.atlassian.net/browse/GEOS-11794) CVE-2024-29198 Moderate
* [GEOS-11717](https://osgeo-org.atlassian.net/browse/GEOS-11717) CVE-2024-40625 Moderate

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## OGC API FeaturesService Extension

The OGC API Features module has officially graduated from community status to become a supported GeoServer extension.
This implementation of the modern, web-friendly [OGC API - Features](https://ogcapi.ogc.org/features/) standard provides
a RESTful API alternative to traditional WFS services.

Key capabilities include:

- Feature collection discovery and access
- Spatial and attribute filtering using CQL2
- Multiple output formats (GeoJSON, HTML, etc.)
- Service-level operations across multiple collections

This graduation is the result of a collaborative code sprint with developers from Camptocamp, GeoSolutions, and GeoCat joining forces.
As part of this effort, the module now passes OGC CITE compliance tests, ensuring proper interoperability with other OGC-compliant systems.

Special thanks to the French "**Commissariat général au développement durable du Ministère chargé de l'Ecologie**" for
sponsoring this work as part of the [Collectif Interopérabilité et mise en Commun de Composants Logiciels pour les plateformes de données (CICCLO)](https://www.afigeo.asso.fr/communication-cicclo-presentation-plus-detaillee-du-projet-et-communique-de-presse/) project.

For more information, see the [GSIP-230](https://github.com/geoserver/geoserver/wiki/GSIP-230) OGC API Features Extension proposal, and the [extension user docs](https://docs.geoserver.org/2.27.x/en/user/services/features/index.html).

## OGC CITE Compliance

A significant effort has been made in this release to ensure GeoServer passes the OGC CITE compliance tests across all supported services.
This work improves the quality and interoperability of GeoServer with other OGC-compliant systems.

* [GEOS-11729](https://osgeo-org.atlassian.net/browse/GEOS-11729) Pass WCS 1.0 certification OGC CITE tests
* [GEOS-11730](https://osgeo-org.atlassian.net/browse/GEOS-11730) Pass WCS 1.1 certification OGC CITE tests
* [GEOS-11780](https://osgeo-org.atlassian.net/browse/GEOS-11780) Pass WCS 2.0 certification OGC CITE tests
* [GEOS-11731](https://osgeo-org.atlassian.net/browse/GEOS-11731) Pass WFS 1.0 certification OGC CITE tests
* [GEOS-11732](https://osgeo-org.atlassian.net/browse/GEOS-11732) Pass WFS 1.1 certification OGC CITE tests
* [GEOS-11733](https://osgeo-org.atlassian.net/browse/GEOS-11733) Pass WFS 2.0 certification OGC CITE tests
* [GEOS-11734](https://osgeo-org.atlassian.net/browse/GEOS-11734) Pass WMS 1.1 certification OGC CITE tests
* [GEOS-11735](https://osgeo-org.atlassian.net/browse/GEOS-11735) Pass WMS 1.3 certification OGC CITE tests
* [GEOS-11779](https://osgeo-org.atlassian.net/browse/GEOS-11779) Pass WMTS 1.0 certification OGC CITE tests
* [GEOS-11736](https://osgeo-org.atlassian.net/browse/GEOS-11736) Pass OGC API Features 1.0 certification OGC CITE tests
* [GEOS-11752](https://osgeo-org.atlassian.net/browse/GEOS-11752) Pass GeoTIFF 1.1 certification OGC CITE tests
* [GEOS-11753](https://osgeo-org.atlassian.net/browse/GEOS-11753) Pass GPKG 1.2 certification OGC CITE tests

This compliance work involved fixing numerous issues related to exception handling, version negotiation, and service behavior.

Restoring CITE Compliance has been a project goal for a number of years; and an ongoing [sponsorship goal]({% post_url 2019-09-18-join-me-in-funding-an-important-geoserver-initiative %})
for the GeoServer project. Thanks to prior sponsors of this activity [activity]({% post_url 2019-11-14-cite-test-automation-request-for-proposal %})
[Gaia3D](https://gaia3d.com), and [OSGeo:UK](https://uk.osgeo.org).

Thanks to Peter Smythe and Angelos Tzotsos for working with Open Source Geospatial Foundation to [provided access](https://www.osgeo.org/partners/ogc/) to CITE Certification for this release.

<!-- placeholder for live image provided by ogc -->

Special thanks to Andrea Aime for leveraging, extending, and improving the OGC CITE conformance testing infrastructure
that was developed during the OGC API Features work, and methodically applying it to ensure all GeoServer services
now pass their respective compliance tests.


## Improved Catalog Loading

GeoServer 2.27.0 includes significant performance improvements for server startup with the promotion of the "datadir catalog loader" from a community module to
the GeoServer core. This enhanced loader dramatically improves startup times for deployments with large data directories through parallel processing.

The performance gains are substantial, as shown by these benchmark results:

**NFS/10Gbps Storage**:
- 16K layers: reduced from 5.8s to 3.3s (1.8× faster)
- 100K layers: reduced from 1.9min to 28.3s (4.1× faster)
- 1M layers: reduced from 21.3min to 5.9min (3.6× faster)

**NVMe Gen5/ZFS Storage**:
- 16K layers: reduced from 3.5s to 1.3s (2.7× faster)
- 100K layers: reduced from 21.2s to 3.2s (6.5× faster)
- 1M layers: reduced from 3.4min to 24.6s (8.3× faster)

The new loader uses work-stealing thread pools for catalog processing while ensuring thread safety. This enhancement is particularly valuable for large enterprise deployments where startup time has been a bottleneck.

The loader is enabled by default but can be disabled or tuned if needed as explained in the [data directory](https://docs.geoserver.org/2.27.x/en/user/datadirectory/setting.html#configuration) documentation.

## MapML Enhancement

The MapML extension continues to receive significant updates:

* [GEOS-11605](https://osgeo-org.atlassian.net/browse/GEOS-11605) MapML Support custom TCRS projections from existing GridSets

    A new MapML TCRS Settings menu is available in the GeoServer UI on the Settings section:

    <img src="/img/posts/2.27/mapml_tcrs_menu.png" alt="MapML_tcrs_menu" style="display:block;"/>

    It provides a selector containing available GridSets. Administrator can select GridSets from the left list that will be converted to TiledCRSs.

    <img src="/img/posts/2.27/mapml_tcrs_selector.png" alt="MapML_tcrs_selector" style="display:block;"/>
    
    Check out the [documentation](https://docs.geoserver.org/2.27.x/en/user/extensions/mapml/installation.html#tiledcrs) for more insights.

* [GEOS-11561](https://osgeo-org.atlassian.net/browse/GEOS-11561) Client-Delegating MapML Proxy
* [GEOS-11577](https://osgeo-org.atlassian.net/browse/GEOS-11577) Rename MapML \<layer-\> to \<map-layer\>, rename viewer bundle to mapml.js
* [GEOS-11666](https://osgeo-org.atlassian.net/browse/GEOS-11666) Update MapML viewer to latest release 0.16.0

These changes provide better integration and more powerful capabilities for creating web maps with MapML.

## Smart Data Loader Enhancements

The Smart Data Loader has been improved with override rules, making it more flexible for data management scenarios:

* [GEOS-11741](https://osgeo-org.atlassian.net/browse/GEOS-11741) Enhancing Smart Data Loader with Override Rules

    The Smart Data Loader plugin automates the creation of XSD schemas and App-Schema mapping files, significantly simplifying the configuration of complex feature data in GeoServer.

    With the new override rules capability, you can now customize how database tables are mapped to feature types without modifying the database schema, providing greater control and flexibility when working with complex or legacy data structures.

    <img src="/img/posts/2.27/smart-loader-overrides.png" alt="Smart_Data_Loader_override_rules" style="display:block; width:50%;"/>

    For more details on using Smart Override Rules, see the [official documentation](https://docs.geoserver.org/main/en/user/community/smart-data-loader/data-store.html#smart-override-rules).


* [GEOS-11691](https://osgeo-org.atlassian.net/browse/GEOS-11691) Smart data loader accepts bigint and bigserial but not int8 postgresql type alias


## GeoFence Improvements

The GeoFence extension has received several significant improvements:

* [GEOS-11702](https://osgeo-org.atlassian.net/browse/GEOS-11702) GeoFence: major libs update
* [GEOS-11704](https://osgeo-org.atlassian.net/browse/GEOS-11704) GeoFence: filter rule list by IP address
* [GEOS-11705](https://osgeo-org.atlassian.net/browse/GEOS-11705) GeoFence: make rules valid within a date range
* [GEOS-11526](https://osgeo-org.atlassian.net/browse/GEOS-11526) GeoFence: slow GeoServer response when there are many roles and layergroups

These improvements make GeoFence more flexible and powerful for implementing fine-grained security policies.

## Performance Improvements

Several performance improvements have been implemented in this release:

* [GEOS-11580](https://osgeo-org.atlassian.net/browse/GEOS-11580) Improve embedded GWC meta-tiling performance
* [GEOS-11766](https://osgeo-org.atlassian.net/browse/GEOS-11766) Speed up CRS and store factory lookups during catalog loading
* [GEOS-11722](https://osgeo-org.atlassian.net/browse/GEOS-11722) Coverage view reader partially ignores multithreaded loading
* [GEOS-11739](https://osgeo-org.atlassian.net/browse/GEOS-11739) Excessive memory usage for WMS KML output format
* [GEOS-11760](https://osgeo-org.atlassian.net/browse/GEOS-11760) Fix a potential OOM in the KML transformation

## Other Improvements

* [GEOS-11468](https://osgeo-org.atlassian.net/browse/GEOS-11468) Coverage REST API URL Checks
* [GEOS-11562](https://osgeo-org.atlassian.net/browse/GEOS-11562) Default Gzip filter setting in web.xml does not compress application/javascript
* [GEOS-11564](https://osgeo-org.atlassian.net/browse/GEOS-11564) WPS calls to internal WFS will handle requests with version=2.0.0
* [GEOS-11578](https://osgeo-org.atlassian.net/browse/GEOS-11578) WMTS Multidim extension, allow usage of a sidecar in a separate store
* [GEOS-11585](https://osgeo-org.atlassian.net/browse/GEOS-11585) Patch Spectrum to work with Wicket's CSP
* [GEOS-11586](https://osgeo-org.atlassian.net/browse/GEOS-11586) Patch CodeMirror to work with Wicket's CSP
* [GEOS-11612](https://osgeo-org.atlassian.net/browse/GEOS-11612) Add system property support for Proxy base URL -> use headers activation
* [GEOS-11624](https://osgeo-org.atlassian.net/browse/GEOS-11624) Split Geopackage extension into separate modules to reduce dependencies
* [GEOS-11625](https://osgeo-org.atlassian.net/browse/GEOS-11625) Add "Challenge Anonymous Sessions" Option to AuthKey Filter
* [GEOS-11645](https://osgeo-org.atlassian.net/browse/GEOS-11645) Control FreeMarker template access
* [GEOS-11651](https://osgeo-org.atlassian.net/browse/GEOS-11651) Support env parametrization on OIDC filter
* [GEOS-11669](https://osgeo-org.atlassian.net/browse/GEOS-11669) Patch jscolor to work with Wicket's CSP


## Library Updates

GeoServer 2.27.0 includes updates to many core libraries:

* [GEOS-11770](https://osgeo-org.atlassian.net/browse/GEOS-11770) Update to jai-ext 1.1.31
* [GEOS-11771](https://osgeo-org.atlassian.net/browse/GEOS-11771) Update to Imageio-EXT 1.4.15
* [GEOS-11590](https://osgeo-org.atlassian.net/browse/GEOS-11590) Upgrade log4j to 2.24.1 and slf4j to 2.0.16
* [GEOS-11608](https://osgeo-org.atlassian.net/browse/GEOS-11608) Update Bouncy Castle Crypto package from bcprov-jdk15on:1.69 to bcprov-jdk18on:1.79
* [GEOS-11609](https://osgeo-org.atlassian.net/browse/GEOS-11609) Bump XStream from 1.4.20 to 1.4.21
* [GEOS-11685](https://osgeo-org.atlassian.net/browse/GEOS-11685) Bump jetty.version from 9.4.56.v20240826 to 9.4.57.v20241219
* [GEOS-11631](https://osgeo-org.atlassian.net/browse/GEOS-11631) Update MySQL driver to 9.1.0
* [GEOS-11743](https://osgeo-org.atlassian.net/browse/GEOS-11743) Upgrade Oracle JDBC driver \(ojdbc\) from 8 to 11
* [GEOS-11754](https://osgeo-org.atlassian.net/browse/GEOS-11754) Update to mapfish-print-v2 2.3.3

## Bug Fixes

Many bugs have been fixed in this release, including:

* [GEOS-4533](https://osgeo-org.atlassian.net/browse/GEOS-4533), [GEOS-7967](https://osgeo-org.atlassian.net/browse/GEOS-7967) Fixed WPS demo builder chaining issues
* [GEOS-11494](https://osgeo-org.atlassian.net/browse/GEOS-11494) WFS GetFeature request with a propertyname parameter fails when layer attributes are customized
* [GEOS-11524](https://osgeo-org.atlassian.net/browse/GEOS-11524) CSW: default queryables mapping not generated
* [GEOS-11540](https://osgeo-org.atlassian.net/browse/GEOS-11540) OGC API queryables features call not working in JSON
* [GEOS-11607](https://osgeo-org.atlassian.net/browse/GEOS-11607) KML WMS GetMap is performing a heavy database load query
* [GEOS-11658](https://osgeo-org.atlassian.net/browse/GEOS-11658) Time editor dumps stack trace in UI if the start or end time values are intervals
* [GEOS-11664](https://osgeo-org.atlassian.net/browse/GEOS-11664) Update REST security paths
* [GEOS-11667](https://osgeo-org.atlassian.net/browse/GEOS-11667) Make WMTS work in strict cite compliance mode
* [GEOS-11668](https://osgeo-org.atlassian.net/browse/GEOS-11668) WMTS home page capabilities link uses 1.1.1 as the version, and the wrong version negotiation approach
* [GEOS-11684](https://osgeo-org.atlassian.net/browse/GEOS-11684) GDAL no longer included in Docker image
* [GEOS-11792](https://osgeo-org.atlassian.net/browse/GEOS-11792) Default Service Capabilities shown on initial start with no workspaces
* [GEOS-11796](https://osgeo-org.atlassian.net/browse/GEOS-11796) Deadlocks During GeoServer Startup When Loading Style Group Layer Groups

## Community Module Updates

* [GEOS-11781](https://osgeo-org.atlassian.net/browse/GEOS-11781) Community cleanup fall 2024
* Removed abandoned community modules:
  * [GEOS-11641](https://osgeo-org.atlassian.net/browse/GEOS-11641) Remove the abandoned community module webservice-test
  * [GEOS-11642](https://osgeo-org.atlassian.net/browse/GEOS-11642) Remove the gwc-distributed community module

## Full Release Notes

For the complete list of changes, see [2.27.0](https://github.com/geoserver/geoserver/releases/tag/2.27.0) release notes.


## About GeoServer 2.27 Series

Additional information on GeoServer 2.27 series:

* [GeoServer 2.27 User Manual](https://docs.geoserver.org/2.27.x/en/user/)
* [GeoServer 2025 Roadmap]({% post_url 2025-01-13-roadmap %})

Release notes:
([2.27.0](https://github.com/geoserver/geoserver/releases/tag/2.27.0))

