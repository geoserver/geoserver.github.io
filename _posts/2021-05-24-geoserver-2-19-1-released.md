---
author: Jody Garnett
layout: post
title: GeoServer 2.19.1 Released
categories:
- Announcements
tags:
- Release
release: release_219
version: 2.19.1
jira_version: 16816
---

We are happy to announce GeoServer [2.19.1](/release/2.19.1/) release is available for download  ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.1/geoserver-2.19.1-bin.zip/download) and [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.1/geoserver-2.19.1-war.zip/download)) along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.1/geoserver-2.19.1-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.1/extensions/).

This GeoServer 2.19.1 release was produced in conjunction with GeoTools 25.1 and GeoWebCache 1.19.1. this is a stable release recommended for production systems.

Thanks to everyone who contributed, and to Jody Garnett (GeoCat) for making this release.

## Improvements and Fixes

Several new features are included in this release:

* GetFeatureInfo can now includes ColorMap labels for the location clicked, check out the [tutorial](https://docs.geoserver.org/stable/en/user/tutorials/GetFeatureInfo/raster.html).
* A new styling vendor option `inclusion` to [control control legend generation](https://docs.geoserver.org/stable/en/user/styling/sld/extensions/rendering-selection.html) for WMS GetLegendGraphic using values of `legendOnly`, `mapOnly`, or `normal` to define how a style element is used.

Notable improvements:

* Improve parameter extractor logging
* Customization of complex GeoJSON WFS output is now available for other data stores, previously this was restricted attributes marked ``@dataType`` by the AppSchema plugin.
- SLD Service now places a limit, configured by system variable ``-Dorg.geoserver.sldService.maxUniqueRange=1024``, of the number of unique intervals.

Fixes included in this release:

- Fix elevation key-value-pair parser (used in WMS GetMap) handling of edge cases such as zero intervals 
- Fix importer application of gridset bounds, (ot was not working correctly when GWC DiskQuote in use)
- Inspire schemas URL updated to their new HTTPS location
- WCS 2.0 slicing on lat/long fix, was sometimes returning adjacent pixel
- WMS Layers with dimensions were missing from GetCapabilities when using catalog security challenge mode.
- App Schema download was missing a required jar.
- Improvements helping coverage format compatibility with file references
- Address GeoFence interaction with non global named tree container
- Address WPS Download animation out of memory issues
- Address rendering process regression with use of vendor option `sortByGroup` resulting in "internal error rendering process failed"

Internal:

- Upgrade to commons-io 2.8.0
- Autoformat maven ``pom.xml`` files

For details check the [2.19.1](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16816) release notes.

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

Release notes ( [2.19.1](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16816) \| [2.19.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16814) \| [2.19-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16766) )

