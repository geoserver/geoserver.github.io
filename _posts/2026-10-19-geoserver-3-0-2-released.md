---
author: Jody Garnett
date: 2026-10-19
layout: post
title: GeoServer 3.0.2 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_30
version: 3.0.2
jira_version: 18102
--- 

GeoServer [3.0.2](/release/3.0.2/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.2/geoserver-3.0.2-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.2/geoserver-3.0.2-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.2/GeoServer-3.0.2-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.2/geoserver-3.0.2-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/3.0.2/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 3.0.2 includes the latest [GeoTools 35.2](https://github.com/geotools/geotools/releases/tag/35.2), [GeoWebCache 2.0.2](https://github.com/GeoWebCache/geowebcache/releases/tag/2.0.2), along with [mapfish-print-v2 2.5.2](https://github.com/mapfish/mapfish-print-v2/releases/tag/release%2F2.5.2) and [ImageN 0.9.3](https://github.com/eclipse-imagen/imagen/releases/tag/0.9.3). There is a new [GeoServer Cloud 3.0.2](https://github.com/geoserver/geoserver-cloud/releases/tag/v3.0.2) release - representing the first time an updated GeoServer Cloud is made available on release day.

Thanks to Jody Garnett (GeoCat) for making this release, Andrea Aime (GeoSolutions) for testing, and Gabriel Roldan (Camptocamp) for the GeoServer Cloud release.

## Security Considerations

This release addresses security vulnerabilities and is an important upgrade for production systems. Details about the fixes will be provided at the start of November.

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## OGC API Maps 1.0

The OGC API Maps community module has been aligned with the final [OGC API - Maps 1.0.0](https://docs.ogc.org/is/20-058/20-058.html) standard.

* **Dataset map**: Draw several collections into a single map, choosing and ordering them with the `collections` parameter.
  The map preview provides a palette to select collections, the first one drawn at the bottom.

  <a href="/img/posts/3.0.2/dataset-map.png" target="_blank" rel="noopener">
    <img src="/img/posts/3.0.2/dataset-map.png" alt="OGC API Maps dataset map preview" class="screensnap"/>
  </a>

* **Filtering**: Maps can be filtered using CQL2 Text, CQL2 JSON or ECQL, using the queryable attributes of each collection.

  <a href="/img/posts/3.0.2/map-preview.png" target="_blank" rel="noopener">
    <img src="/img/posts/3.0.2/map-preview.png" alt="OGC API Maps preview with filter" class="screensnap"/>
  </a>

* **Conformance**: Each optional conformance class (subsetting, scaling, background, crs, output formats, and more)
  can be enabled or disabled from the **Services > Mapping** settings page.
  Invalid parameters are now reported as a bad request rather than an internal error.

  <a href="/img/posts/3.0.2/maps-cql2-conformance.png" target="_blank" rel="noopener">
    <img src="/img/posts/3.0.2/maps-cql2-conformance.png" alt="OGC API Maps CQL2 conformance table" class="screensnap"/>
  </a>

For more information see [OGC API Maps](https://docs.geoserver.org/3.0.x/en/user/community/ogc-api/maps/) in the user manual.

Thanks to Andrea Aime (GeoSolutions) for the OGC API - Maps development, and Jody Garnett (GeoCat) for the 3.0.x backport and improvements to the conformance table editor.

* [GEOS-12161](https://osgeo-org.atlassian.net/browse/GEOS-12161) Align OGC API Maps to v1.0.0
* [GEOS-12163](https://osgeo-org.atlassian.net/browse/GEOS-12163) Expose filtering in OGC API Maps
* [GEOS-12167](https://osgeo-org.atlassian.net/browse/GEOS-12167) Add dataset map support in OGC API Maps

## GeoFence for GeoServer 3

The GeoFence extensions are now available for GeoServer 3, completing **Milestone 4: Integration** of the [GeoServer 3 crowdfunding campaign](/sponsor/gs3-crowdfunding).

GeoFence has been updated to Jakarta EE, Spring Framework 7 and Hibernate 7:

* The `geofence` plugin now communicates with a standalone GeoFence server using REST,
  as Spring remoting is no longer available.
* The embedded `geofence-server` requires a PostgreSQL / PostGIS database, H2 is no longer supported.
* The GeoFence admin page is found under the **Security** menu, showing the active engine and GeoFence services URL.

<a href="/img/posts/3.0.2/geofence-admin.png" target="_blank" rel="noopener">
  <img src="/img/posts/3.0.2/geofence-admin.png" alt="GeoFence admin page general settings" class="screensnap"/>
</a>

Existing GeoFence users should review the [migration guide](https://docs.geoserver.org/3.0.x/en/user/extensions/geofence-server/migration/) before upgrading, as the datasource configuration file has been renamed and the GeoFence authentication provider has been removed.

Thanks to Emanuele Tajariol (GeoSolutions) for this work, and to the [GeoServer 3 crowdfunding sponsors](/sponsor/gs3-crowdfunding) for making it possible.

{% include gs3-sponsors.html %}

* [GEOS-12192](https://osgeo-org.atlassian.net/browse/GEOS-12192) GeoFence: align to GeoServer3

## Release notes

New Feature:

* [GEOS-12180](https://osgeo-org.atlassian.net/browse/GEOS-12180) Add support for multi-layer tile caching (coalescing) in GWC

Improvement:

* [GEOS-10029](https://osgeo-org.atlassian.net/browse/GEOS-10029) Use XML schema in applicationContext files
* [GEOS-12154](https://osgeo-org.atlassian.net/browse/GEOS-12154) Improve URL validation in SLD processing
* [GEOS-12170](https://osgeo-org.atlassian.net/browse/GEOS-12170) Centralize CRS list management across OGC APIs
* [GEOS-12176](https://osgeo-org.atlassian.net/browse/GEOS-12176) Encrypt URL parameters with AES instead of DES
* [GEOS-12177](https://osgeo-org.atlassian.net/browse/GEOS-12177) Do not hardcode algorithms in the security tests
* [GEOS-12179](https://osgeo-org.atlassian.net/browse/GEOS-12179) Name the keystore file after its format, and refuse a mismatched one
* [GEOS-12183](https://osgeo-org.atlassian.net/browse/GEOS-12183) CSS can trigger a bean loading circularity during startup
* [GEOS-12184](https://osgeo-org.atlassian.net/browse/GEOS-12184) WCS Img coverage encoders subtly depend on gt-image
* [GEOS-12187](https://osgeo-org.atlassian.net/browse/GEOS-12187) GeoJSON vector tiles are empty when the layer is meta-tiled
* [GEOS-12195](https://osgeo-org.atlassian.net/browse/GEOS-12195) Refactoring of service resolution in Dispatcher
* [GEOS-12198](https://osgeo-org.atlassian.net/browse/GEOS-12198) Support single-tenant Microsoft Entra ID authentication
* [GEOS-12199](https://osgeo-org.atlassian.net/browse/GEOS-12199) Apply the catalog's entity resolver consistently to stored query parsing
* [GEOS-12203](https://osgeo-org.atlassian.net/browse/GEOS-12203) OIDC: let the identity provider assert the built-in "admin" account
* [GEOS-12205](https://osgeo-org.atlassian.net/browse/GEOS-12205) Support GDAL 3.12+ new Raster Attribute Table data types
* [GEOS-12207](https://osgeo-org.atlassian.net/browse/GEOS-12207) Layer preview feature info works poorly with long attribute names/values
* [GEOS-12208](https://osgeo-org.atlassian.net/browse/GEOS-12208) RAT table view does not scroll any longer
* [GEOS-12209](https://osgeo-org.atlassian.net/browse/GEOS-12209) Allow admins to request all layers from CSW endpoints
* [GEOS-12211](https://osgeo-org.atlassian.net/browse/GEOS-12211) WPS: clean up GDAL configuration parsing
* [GEOS-12218](https://osgeo-org.atlassian.net/browse/GEOS-12218) The print extension ships with a snapshot jar
* [GEOS-12231](https://osgeo-org.atlassian.net/browse/GEOS-12231) Extension lookups take a global fair lock to read the JSONP setting
* [GEOS-12234](https://osgeo-org.atlassian.net/browse/GEOS-12234) Report invalid connection settings when saving JDBC user/group, role and authentication services
* [GEOS-12235](https://osgeo-org.atlassian.net/browse/GEOS-12235) Centralize remote IP resolution into a servlet filter
* [GEOS-12237](https://osgeo-org.atlassian.net/browse/GEOS-12237) The style editor layer preview breaks with invalid chars in style names
* [GEOS-12238](https://osgeo-org.atlassian.net/browse/GEOS-12238) CSW: Clearer exception in DirectDownload invalid requests
* [GEOS-12239](https://osgeo-org.atlassian.net/browse/GEOS-12239) Read JDBC user and role property values as text
* [GEOS-12240](https://osgeo-org.atlassian.net/browse/GEOS-12240) Clearer stored query error messages when query id is too long

Bug:

* [GEOS-12053](https://osgeo-org.atlassian.net/browse/GEOS-12053) OGCAPI Features unable to disable core or enable draft / community standards
* [GEOS-12056](https://osgeo-org.atlassian.net/browse/GEOS-12056) OGC API CQL conformance URIs are wrong
* [GEOS-12123](https://osgeo-org.atlassian.net/browse/GEOS-12123) Login failure in FIPS mode for GeoServerDigestPasswordEncoder
* [GEOS-12143](https://osgeo-org.atlassian.net/browse/GEOS-12143) Cannot create a tiled layer from the "tile caching" layer tab any longer
* [GEOS-12159](https://osgeo-org.atlassian.net/browse/GEOS-12159) ReprojectingFeatureCollection throws ClassCastException reprojecting per-feature geometry between two Geographic 3D CRSs
* [GEOS-12172](https://osgeo-org.atlassian.net/browse/GEOS-12172) Some testcases have overly verbose logging
* [GEOS-12174](https://osgeo-org.atlassian.net/browse/GEOS-12174) Blob store creation fails under containerd — missing depends-on on gwcBlobStoreAggregator
* [GEOS-12193](https://osgeo-org.atlassian.net/browse/GEOS-12193) "Encode coordinates measures" gives different geometries per GML version
* [GEOS-12200](https://osgeo-org.atlassian.net/browse/GEOS-12200) GS3: Style Editor Color Helper layout broken
* [GEOS-12206](https://osgeo-org.atlassian.net/browse/GEOS-12206) WMTS Multidim operations (DescribeDomains/GetHistogram/...) do not honor datasecurity
* [GEOS-12213](https://osgeo-org.atlassian.net/browse/GEOS-12213) Changing the workspace of a WMS/WMTS cascaded store does not update its layers
* [GEOS-12216](https://osgeo-org.atlassian.net/browse/GEOS-12216) Datadir loader fails on cross-workspace resource references
* [GEOS-12225](https://osgeo-org.atlassian.net/browse/GEOS-12225) Session ID rotates on every request when the admin password is still the default
* [GEOS-12229](https://osgeo-org.atlassian.net/browse/GEOS-12229) Backup and restore: after a job has been stopped, later backups and restores end STOPPED
* [GEOS-12230](https://osgeo-org.atlassian.net/browse/GEOS-12230) Backup and restore: a full restore loses cascaded WMS/WMTS layers and workspace layer groups, and can empty its own archive

Task:

* [GEOS-11975](https://osgeo-org.atlassian.net/browse/GEOS-11975) MapML extension / GeoServer 3.0 SNAPSHOT with MapML extension won't start
* [GEOS-12160](https://osgeo-org.atlassian.net/browse/GEOS-12160) Add URL checks to wps-download-plugin
* [GEOS-12171](https://osgeo-org.atlassian.net/browse/GEOS-12171) Update to ImageN 0.9.3
* [GEOS-12181](https://osgeo-org.atlassian.net/browse/GEOS-12181) Update gs-web-app to jetty.ee11 testing
* [GEOS-12186](https://osgeo-org.atlassian.net/browse/GEOS-12186) Update to JakartaEE Servlet
* [GEOS-12188](https://osgeo-org.atlassian.net/browse/GEOS-12188) GS3: jetty e11 de-dup warnings due to servlet-api compile scope
* [GEOS-12192](https://osgeo-org.atlassian.net/browse/GEOS-12192) GeoFence: align to GeoServer3
* [GEOS-12241](https://osgeo-org.atlassian.net/browse/GEOS-12241) MapFish Print 2.5.2 Update

For the complete list see [3.0.2](https://github.com/geoserver/geoserver/releases/tag/3.0.2) release notes. 

## Community Updates

Community module development:

* [GEOS-12161](https://osgeo-org.atlassian.net/browse/GEOS-12161) Align OGC API Maps to v1.0.0
* [GEOS-12163](https://osgeo-org.atlassian.net/browse/GEOS-12163) Expose filtering in OGC API Maps
* [GEOS-12167](https://osgeo-org.atlassian.net/browse/GEOS-12167) Add dataset map support in OGC API Maps
* [GEOS-12178](https://osgeo-org.atlassian.net/browse/GEOS-12178) FIPS community module
* [GEOS-12182](https://osgeo-org.atlassian.net/browse/GEOS-12182) Support Azure SAS token authentication for COG stores
* [GEOS-12191](https://osgeo-org.atlassian.net/browse/GEOS-12191) GS3: TilesServiceInfoImpl and ImagesServiceInfoImpl both configure tiles.xml
* [GEOS-12219](https://osgeo-org.atlassian.net/browse/GEOS-12219) Remove the gwc-sqlite community module
* [GEOS-12221](https://osgeo-org.atlassian.net/browse/GEOS-12221) WPS Longitudinal Profile: compute distances on the ground
* [GEOS-12222](https://osgeo-org.atlassian.net/browse/GEOS-12222) JWT-Header: Improvements and documentation clarifications
* [GEOS-12236](https://osgeo-org.atlassian.net/browse/GEOS-12236) Support conformance classes in OGC API Styles

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 3.0 Series

Additional information on GeoServer 3.0 series:

* [GeoServer 3.0 User Manual](https://docs.geoserver.org/3.0.x/en/user/)
* [GeoServer 3.0-RC, a crowdfunded success story]({% post_url 2026-04-21-geoserver-3-rc-crowdfunding-success %})
* [GSIP-221](https://github.com/geoserver/geoserver/wiki/GSIP-221) MkDocs Migration
* [GSIP-226](https://github.com/geoserver/geoserver/wiki/GSIP-226) GeoServer 3
* [GSIP-233](https://github.com/geoserver/geoserver/wiki/GSIP-233) Community Pending Profile
* [GSIP-236](https://github.com/geoserver/geoserver/wiki/GSIP-236) Lightening up the Core for GeoServer 3
* [GSIP-238](https://github.com/geoserver/geoserver/wiki/GSIP-238) UI / UX Refresh
* [GSIP 239](https://github.com/geoserver/geoserver/wiki/GSIP-239) Promote OIDC Community Module to Extension

Release notes:
( [3.0.2](https://github.com/geoserver/geoserver/releases/tag/3.0.2)
| [3.0.1](https://github.com/geoserver/geoserver/releases/tag/3.0.1)
| [3.0.0](https://github.com/geoserver/geoserver/releases/tag/3.0.0)
) 
