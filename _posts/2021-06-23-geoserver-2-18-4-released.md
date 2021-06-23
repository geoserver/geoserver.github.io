---
author: Andrea Aime
layout: post
title: GeoServer 2.18.4 Released
categories:
- Announcements
tags:
- Release
release: release_218
version: 2.18.4
jira_version: 16819
---

We are happy to announce GeoServer [2.18.4](/release/2.18.4/) release is available for download  ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.4/geoserver-2.18.4-bin.zip/download) and [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.4/geoserver-2.18.4-war.zip/download)) along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.4/geoserver-2.18.4-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.4/extensions/).

This GeoServer 2.18.4 release was produced in conjunction with GeoTools 24.4 and GeoWebCache 1.18.4. This is a maintenance release recommended for production systems.

Thanks to everyone who contributed, and to Alessandro Parma (GeoSolutions) and Andrea Aime (GeoSolutions) for making this release.

## Improvements and Fixes

This release includes support for the Krovak North Orientated projection. In addition to this new features, a few notable improvements are included:

- [Upgrade version of wicket and jquery used by GeoServer](https://osgeo-org.atlassian.net/browse/GEOS-10098).
- SLDService can now [limit max unique values](https://osgeo-org.atlassian.net/browse/GEOS-10030) for uniqueInterval classification vector data (to avoid generating too many rules).
- Better logging in lock management and parameters extractor

Fixes included in this release:

- [GEOS-10057](https://osgeo-org.atlassian.net/browse/GEOS-10057) Escape style editor page user input
- [GEOS-10056](https://osgeo-org.atlassian.net/browse/GEOS-10056) Rename schemaless-mongo plug-in to mongodb-schemaless
- [GEOS-10055](https://osgeo-org.atlassian.net/browse/GEOS-10055) Escape SRS demo page user input
- [GEOS-10051](https://osgeo-org.atlassian.net/browse/GEOS-10051) Fix edge cases in the elevation parser
- [GEOS-10049](https://osgeo-org.atlassian.net/browse/GEOS-10049) Schemaless-features layer with name different from the mongo collection throws exception
- [GEOS-10048](https://osgeo-org.atlassian.net/browse/GEOS-10048) Schemaless-features mongoDB layer not present in WMS capabilities
- [GEOS-10031](https://osgeo-org.atlassian.net/browse/GEOS-10031) GWC loses GridSets bounds when importing data through the Importer plugin.
- [GEOS-9748](https://osgeo-org.atlassian.net/browse/GEOS-9748) Rendering process fails if vendor option sortByGroup is used


For details check the [2.18.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16819) release notes.

## About GeoServer 2.18

Additional information on GeoServer 2.18 series:
  
  * State of GeoServer 2.18 ([slides](https://docs.google.com/presentation/d/1Q0pHRUcvucAuHDeZPoeDJG4UY5izwbqo8ZawUdk9xYM/edit?usp=sharing))
  * GeoServer Orientation
  ([slides](https://t.co/fvBTLMia6f?amp=1)|[video](https://youtu.be/bdkk5eVR674))
  * Release Notes
  ( [2.18.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16819)
  | [2.18.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16808)
  | [2.18.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16803)
  | [2.18.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16800)
  | [2.18.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16796)
  | [2.18-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16783))

