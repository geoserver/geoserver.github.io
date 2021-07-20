---
author: Jody Garnett
layout: post
title: GeoServer 2.19.2 Released
categories:
- Announcements
tags:
- Release
release: release_219
version: 2.19.2
jira_version: 16821
---

We are happy to announce GeoServer [2.19.2](/release/2.19.2/) release is available for download  ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.2/geoserver-2.19.2-bin.zip/download) and [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.2/geoserver-2.19.2-war.zip/download)) along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.2/geoserver-2.19.2-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.2/extensions/).

This GeoServer 2.19.2 release was produced in conjunction with GeoTools 25.2, this is a stable release recommended for production systems.

Thanks to everyone who contributed, and to Jody Garnett (GeoCat) for making this release.

## Improvements and Fixes

New features are included in this release:

* [GEOS-5239](https://osgeo-org.atlassian.net/browse/GEOS-5239) Implement \(Krovak\) North Orientated projection

Notable improvements:

* [GEOS-10149](https://osgeo-org.atlassian.net/browse/GEOS-10149) Improve Catalog Parametrization documentation

* [GEOS-10098](https://osgeo-org.atlassian.net/browse/GEOS-10098) Upgrade version of wicket and jquery used by GeoServer

* [GEOS-10064](https://osgeo-org.atlassian.net/browse/GEOS-10064) Improving WPS Raster Download - download time

* [GEOS-10009](https://osgeo-org.atlassian.net/browse/GEOS-10009) Improve logging on lock providers

Fixes included in this release:

* [GEOS-10114](https://osgeo-org.atlassian.net/browse/GEOS-10114) Geofence server UI, error when changing the layerType from layer details tab.

* [GEOS-10113](https://osgeo-org.atlassian.net/browse/GEOS-10113) Geofence REST NPE when requesting rule with void Layer details

* [GEOS-10037](https://osgeo-org.atlassian.net/browse/GEOS-10037) WMTS Multidimensional extension make layers encoding fail on TileLayers not being GeoServerTileLayers

* [GEOS-9804](https://osgeo-org.atlassian.net/browse/GEOS-9804) The default style of the layergroup is propagated in the layer as default style


For details check the [2.19.2](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16821) release notes.

## About GeoServer 2.19

Additional information on GeoServer 2.19 series:

* [WMS GetFeatureInfo includes labels from ColorMap ](https://docs.geoserver.org/stable/en/user/tutorials/GetFeatureInfo/raster.html)

* [Promote WMTS multidim to extension](https://github.com/geoserver/geoserver/wiki/GSIP-196)

* [Promote WPS-Download to extension](https://github.com/geoserver/geoserver/wiki/GSIP-195)

* [Promote params-extractor to extension](https://github.com/geoserver/geoserver/wiki/GSIP-194)

* [Promote GWC-S3 to extension](https://github.com/geoserver/geoserver/wiki/GSIP-193)

* [Promote WPS-JDBC to extension status](https://github.com/geoserver/geoserver/wiki/GSIP-197)

* [Promote MapML to extension status](https://github.com/geoserver/geoserver/wiki/GSIP-200)

* [GeoServer repository transition to main branch](main-branch.html)

Release notes ( [2.19.2](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16821)\| [2.19.1](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16816) \| [2.19.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16814) \| [2.19-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16766) )

