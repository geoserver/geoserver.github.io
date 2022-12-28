---
author: Andrea Aime
date: 2022-12-28
layout: post
title: GeoServer 2.21.3 Release
categories:
- Announcements
tags:
- Release
release: release_2211
version: 2.21.3
jira_version: 16869 
---

GeoServer [2.21.3](/release/2.21.3/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.3/geoserver-2.21.3-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.3/geoserver-2.21.3-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.3/GeoServer-2.21.3-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.3/geoserver-2.21.3-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.3/extensions/).

This is a maintenance release of the GeoServer 2.21.x series, made in conjunction with GeoTools 27.3 
and GeoWebCache 1.21.3.

Thanks to Andrea Aime (GeoSolutions) and Jody Garnett (GeoCat) for making this release.

## Notables changes

Among the many changes included in this release, we'd like to point out:

* Ability to report PostgreSQL column comments in WFS DescribeFeatureType output (needs a store flag to enable).
* Ability to turn on and off GetFeature output formats, much like the existing WMS controls over GetMap/GetFeatureInfo output formats.
* Fixed concurrent edit of users, roles and data access rules thorough the REST API.
* Fixed database connection leak while editing SQL views in the GUI.


## Release notes

Bug fixes:

- [GEOS-4727](https://osgeo-org.atlassian.net/browse/GEOS-4727) Editing SQL views seems to be leaking connections

- [GEOS-10632](https://osgeo-org.atlassian.net/browse/GEOS-10632) Make sure GetLegendGraphics honors the WMS memory service limits

- [GEOS-10667](https://osgeo-org.atlassian.net/browse/GEOS-10667) WFS: inconsistent srsDimension=4 with topp:tasmania\_roads layer

- [GEOS-10707](https://osgeo-org.atlassian.net/browse/GEOS-10707) GeoFence internal LayerGroup Limit merge inconsistency

- [GEOS-10710](https://osgeo-org.atlassian.net/browse/GEOS-10710) Features Templating backward mapping with back xpath \('../my/property/name'\) doesn't work

- [GEOS-10714](https://osgeo-org.atlassian.net/browse/GEOS-10714) DefaultGeoServerFacade throws ConcurrentModificationException for workspace settings and services

- [GEOS-10729](https://osgeo-org.atlassian.net/browse/GEOS-10729) Concurrent access on data access rules \(authorization\) can lead to loss of configured catalog mode, and lost rules

- [GEOS-10731](https://osgeo-org.atlassian.net/browse/GEOS-10731) GWC variable Parameterization does not work with geoserver-environment.properties due to the bean initialization order

- [GEOS-10736](https://osgeo-org.atlassian.net/browse/GEOS-10736) OSEO product creation via REST API fails if the product id starts with a valid ISO date

- [GEOS-10737](https://osgeo-org.atlassian.net/browse/GEOS-10737) GeoCSS misses support for labelInFeatureInfo and labelAttributeName vendor options

- [GEOS-10741](https://osgeo-org.atlassian.net/browse/GEOS-10741) Remove deprecated YUI usage

- [GEOS-10753](https://osgeo-org.atlassian.net/browse/GEOS-10753) GeoServer can create GML output that is not valid XML

- [GEOS-10757](https://osgeo-org.atlassian.net/browse/GEOS-10757) CITE: WMS <Style> has elements in wrong order \(DTD validation\)

Improvements:

- [GEOS-10673](https://osgeo-org.atlassian.net/browse/GEOS-10673) Add example of using FlatGeobuf granules to the Vector Mosaic documentation

- [GEOS-10696](https://osgeo-org.atlassian.net/browse/GEOS-10696) Allow configuration of Output Format types allowed in GetFeature

- [GEOS-10717](https://osgeo-org.atlassian.net/browse/GEOS-10717) XStreamServiceLoader performance improvement with XStreamPersister caching

- [GEOS-10718](https://osgeo-org.atlassian.net/browse/GEOS-10718) \[OIDC\] the OIDC plugin does not currently take into account the id\_token\_hint parameter

- [GEOS-10735](https://osgeo-org.atlassian.net/browse/GEOS-10735) Obfuscate secret key in S3 Blob Store, avoiding requiring reentry when editing and HTML source visibility

- [GEOS-10746](https://osgeo-org.atlassian.net/browse/GEOS-10746) STAC Sortables should be a subset of the configured queryables

- [GEOS-10755](https://osgeo-org.atlassian.net/browse/GEOS-10755) WCS 2.0 module should not use string concatenation to build XML

- [GEOS-10762](https://osgeo-org.atlassian.net/browse/GEOS-10762) Allow enabling auto-escaping for WMS GetFeatureInfo HTML templates

- [GEOS-10773](https://osgeo-org.atlassian.net/browse/GEOS-10773) Enable localized MapML responses that use WMS language parameter

- [GEOS-10777](https://osgeo-org.atlassian.net/browse/GEOS-10777) Update MapML viewer to latest release

- [GEOS-10790](https://osgeo-org.atlassian.net/browse/GEOS-10790) Allow to control map transparency in DownloadMapProcess

- [GEOS-10810](https://osgeo-org.atlassian.net/browse/GEOS-10810) Enable internationalized layer label / MapML document title

New Features:

- [GEOS-10716](https://osgeo-org.atlassian.net/browse/GEOS-10716) Build schema for simple feature types leveraging column descriptions, when available

- [GEOS-10734](https://osgeo-org.atlassian.net/browse/GEOS-10734) SpatialJSON WFS output format community module

- [GEOS-10758](https://osgeo-org.atlassian.net/browse/GEOS-10758) OGCAPI - Features - Add storageCrs property for Collections

Tasks:

- [GEOS-10721](https://osgeo-org.atlassian.net/browse/GEOS-10721) Bump jettison from 1.4.1 to 1.5.1

- [GEOS-10775](https://osgeo-org.atlassian.net/browse/GEOS-10775) Update XMLUnit to 1.6

See also the [2.21.3 release notes](https://github.com/geoserver/geoserver/releases/tag/2.21.3).

## About GeoServer 2.21

Additional information on GeoServer 2.21 series:

* [Feature Type Customization](https://github.com/geoserver/geoserver/wiki/GSIP-207)
* [Add Styles support to LayerGroup](https://github.com/geoserver/geoserver/wiki/GSIP-205)
* [Log4j1 update or replace activity]({% post_url 2022-01-20-log4j-upgrade %})

Release notes:
( [2.21.3](https://github.com/geoserver/geoserver/releases/tag/2.21.3)
| [2.21.2](https://github.com/geoserver/geoserver/releases/tag/2.21.2)
| [2.21.1](https://github.com/geoserver/geoserver/releases/tag/2.21.1)
| [2.21.0](https://github.com/geoserver/geoserver/releases/tag/2.21.0)
| [2.21-RC](https://github.com/geoserver/geoserver/releases/tag/2.21-RC)
)
