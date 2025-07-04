---
author: Jody Garnett
date: 2025-05-13
layout: post
title: GeoServer 2.26.3 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_226
version: 2.26.3
jira_version: 16943
--- 

GeoServer [2.26.3](/release/2.26.3/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.3/geoserver-2.26.3-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.3/geoserver-2.26.3-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.3/GeoServer-2.26.3-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.3/geoserver-2.26.3-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.3/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.
GeoServer 2.26.3 is made in conjunction with GeoTools 32.3, and GeoWebCache 1.26.3. 

Thanks to Jody Garnett and Andrea Aime (GeoSolutions) for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is considered an critical update for existing installations.

* [CVE-2025-30220](https://github.com/geoserver/geoserver/security/advisories/GHSA-jj54-8f66-c5pc) XML External Entity (XXE) Processing Vulnerability in GeoServer WFS Service (High)

* [CVE-2025-30145](https://github.com/geoserver/geoserver/security/advisories/GHSA-gr67-pwcv-76gf) Denial-of-service (DoS) Vulnerability in Jiffle process (High)

* [CVE-2025-27505](https://github.com/geoserver/geoserver/security/advisories/GHSA-h86g-x8mm-78m5) Missing Authorization on REST API Index (Moderate)

The use of the CVE system allows the GeoServer team to reach a wider audience than blog posts. See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

## Release notes

New Feature:

* [GEOS-11797](https://osgeo-org.atlassian.net/browse/GEOS-11797) Add support for Jiffle expressions in coverage view setup
* [GEOS-11800](https://osgeo-org.atlassian.net/browse/GEOS-11800) Implement GeoServer WPS SpatioTemporalZonalStatistics process

Improvement:

* [GEOS-11757](https://osgeo-org.atlassian.net/browse/GEOS-11757) Optimize ConfigurationPasswordEncryptionHelper to Cache Encrypted Fields by Store Type
* [GEOS-11761](https://osgeo-org.atlassian.net/browse/GEOS-11761) Add support for the clip vendor parameter to WCS as well
* [GEOS-11766](https://osgeo-org.atlassian.net/browse/GEOS-11766) Speed up CRS and store factory lookups during catalog loading
* [GEOS-11793](https://osgeo-org.atlassian.net/browse/GEOS-11793) WPS Read Value from Coverage Position
* [GEOS-11804](https://osgeo-org.atlassian.net/browse/GEOS-11804) Disallow usage of var in GeoServer source code

Bug:

* [GEOS-10844](https://osgeo-org.atlassian.net/browse/GEOS-10844) Exclude xml-apis from build
* [GEOS-11274](https://osgeo-org.atlassian.net/browse/GEOS-11274) Cannot get a JSON legend with an external reference to a non published directory
* [GEOS-11620](https://osgeo-org.atlassian.net/browse/GEOS-11620) Smart Data Loader plugin for GeoServer 2.26 produces a Mapping file data source definition and tries to establish a connection pool, but fails
* [GEOS-11664](https://osgeo-org.atlassian.net/browse/GEOS-11664) Update REST security paths
* [GEOS-11684](https://osgeo-org.atlassian.net/browse/GEOS-11684) GDAL no longer included in Docker image
* [GEOS-11689](https://osgeo-org.atlassian.net/browse/GEOS-11689) IOUtilsTest should not ping an external web site
* [GEOS-11690](https://osgeo-org.atlassian.net/browse/GEOS-11690) Bug in Externalize printing configuration folder
* [GEOS-11696](https://osgeo-org.atlassian.net/browse/GEOS-11696) AdminRequestCallback not loaded due to spring bean name conflict
* [GEOS-11700](https://osgeo-org.atlassian.net/browse/GEOS-11700) GeoFence fails in recognizing some caller IP address
* [GEOS-11703](https://osgeo-org.atlassian.net/browse/GEOS-11703) HEAD and OPTIONS requests on the REST API return a 403
* [GEOS-11707](https://osgeo-org.atlassian.net/browse/GEOS-11707) Ogr2OgrWfsTest test failures with GDAL 3.10.1
* [GEOS-11710](https://osgeo-org.atlassian.net/browse/GEOS-11710) Running Jiffle on coverage views causes the NODATA to be lost
* [GEOS-11713](https://osgeo-org.atlassian.net/browse/GEOS-11713) Concurrent LDAP builds fail on Jenkins
* [GEOS-11716](https://osgeo-org.atlassian.net/browse/GEOS-11716) WFS POST requests fail if a layer is misconfigured
* [GEOS-11720](https://osgeo-org.atlassian.net/browse/GEOS-11720) AttributeTypeInfoImpl doesn't quote names properly
* [GEOS-11722](https://osgeo-org.atlassian.net/browse/GEOS-11722) Coverage view reader partially ignores multithreaded loading
* [GEOS-11739](https://osgeo-org.atlassian.net/browse/GEOS-11739) Excessive memory usage for WMS KML output format
* [GEOS-11747](https://osgeo-org.atlassian.net/browse/GEOS-11747) GeoServer does not throw JAI runtime exceptions
* [GEOS-11751](https://osgeo-org.atlassian.net/browse/GEOS-11751) Symbolizer URL in GetLegendGraphic JSON Request is Broken
* [GEOS-11755](https://osgeo-org.atlassian.net/browse/GEOS-11755) AbstractCatalogFacade leaves dangling references to temporary Catalog
* [GEOS-11756](https://osgeo-org.atlassian.net/browse/GEOS-11756) GeoServerDataDirectory's default workspace location is wrong
* [GEOS-11760](https://osgeo-org.atlassian.net/browse/GEOS-11760) Fix a potential OOM in the KML transformation
* [GEOS-11767](https://osgeo-org.atlassian.net/browse/GEOS-11767) Regression: OL preview always uses JPEG format
* [GEOS-11769](https://osgeo-org.atlassian.net/browse/GEOS-11769) Race conditions in LayerGroupHelper when the default catalog is not fully initialized
* [GEOS-11774](https://osgeo-org.atlassian.net/browse/GEOS-11774) Logout with OAuth plugin will give error if logged in locally
* [GEOS-11776](https://osgeo-org.atlassian.net/browse/GEOS-11776) CVE-2025-27505 Moderate
* [GEOS-11792](https://osgeo-org.atlassian.net/browse/GEOS-11792) Default Service Capabilities shown on initial start with no workspaces
* [GEOS-11795](https://osgeo-org.atlassian.net/browse/GEOS-11795) Incorrect clipping of point geometries in vector tiles
* [GEOS-11818](https://osgeo-org.atlassian.net/browse/GEOS-11818) PageUniqueProcess regression after [GEOT-7628]

Task:

* [GEOS-11682](https://osgeo-org.atlassian.net/browse/GEOS-11682) Add tests for WMS SLD XML request reader
* [GEOS-11701](https://osgeo-org.atlassian.net/browse/GEOS-11701) Update JAI-Ext to 1.1.28
* [GEOS-11743](https://osgeo-org.atlassian.net/browse/GEOS-11743) Upgrade Oracle JDBC driver (ojdbc) from 8 to 11
* [GEOS-11763](https://osgeo-org.atlassian.net/browse/GEOS-11763) Update jai-ext to latest version (1.1.30)
* [GEOS-11770](https://osgeo-org.atlassian.net/browse/GEOS-11770) Update to jai-ext 1.1.31
* [GEOS-11771](https://osgeo-org.atlassian.net/browse/GEOS-11771) Update to Imageio-EXT 1.4.15
* [GEOS-11791](https://osgeo-org.atlassian.net/browse/GEOS-11791) Postpone controller logging after data validation

For the complete list see [2.26.3](https://github.com/geoserver/geoserver/releases/tag/2.26.3) release notes. 

## Community Updates

Community module development:

* [GEOS-11694](https://osgeo-org.atlassian.net/browse/GEOS-11694) OpenID connect: allow caching authentication when an expiration is declared in the access token
* [GEOS-11711](https://osgeo-org.atlassian.net/browse/GEOS-11711) Clickhouse DGGS stores fails to aggregate on dates
* [GEOS-11715](https://osgeo-org.atlassian.net/browse/GEOS-11715) STAC sortby won't work with "properties." prefixed names
* [GEOS-11723](https://osgeo-org.atlassian.net/browse/GEOS-11723) DGGS data store should be able to translate also intersection with multipolygon
* [GEOS-11725](https://osgeo-org.atlassian.net/browse/GEOS-11725) Environment parameters resolving is not working on Smart data loader
* [GEOS-11738](https://osgeo-org.atlassian.net/browse/GEOS-11738) Prevent error when oidc provider sends empty "&state="
* [GEOS-11741](https://osgeo-org.atlassian.net/browse/GEOS-11741) Enhancing Smart Data Loader with Override Rules
* [GEOS-11762](https://osgeo-org.atlassian.net/browse/GEOS-11762) Feature Templates by feature type can not be listed via GeoServer Rest API
* [GEOS-11783](https://osgeo-org.atlassian.net/browse/GEOS-11783) Longitudinal profile process should allow for input chaining
* [GEOS-11784](https://osgeo-org.atlassian.net/browse/GEOS-11784) The longitudinal profile process should limit the number of points it can extract
* [GEOS-11785](https://osgeo-org.atlassian.net/browse/GEOS-11785) The longitudinal profile process should respect cancellation
* [GEOS-11786](https://osgeo-org.atlassian.net/browse/GEOS-11786) Longitudinal profile process: general performance improvements
* [GEOS-11811](https://osgeo-org.atlassian.net/browse/GEOS-11811) Features templating editor is unable to update and save the template body

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.26 Series

Additional information on GeoServer 2.26 series:

* [GeoServer 2.26 User Manual](https://docs.geoserver.org/2.26.x/en/user/)
* [GeoServer 2024 Q3 Developer Update]({% post_url 2024-07-22-developer-update %}) 
* [Raster Attribute Table extension](https://github.com/geoserver/geoserver/wiki/GSIP-222)
* [Community module graduation, amending generality rule](https://github.com/geoserver/geoserver/wiki/GSIP-223)
* [Individual contributor clarification](https://github.com/geoserver/geoserver/wiki/GSIP-224)
* [Migrate geoserver-users from SourceForge to discourse](https://github.com/geoserver/geoserver/wiki/GSIP-225)

Release notes:
( [2.26.3](https://github.com/geoserver/geoserver/releases/tag/2.26.3)
| [2.26.2](https://github.com/geoserver/geoserver/releases/tag/2.26.2)
| [2.26.1](https://github.com/geoserver/geoserver/releases/tag/2.26.1)
| [2.26.0](https://github.com/geoserver/geoserver/releases/tag/2.26.0)
| [2.26-M0](https://github.com/geoserver/geoserver/releases/tag/2.26-M0)
) 

