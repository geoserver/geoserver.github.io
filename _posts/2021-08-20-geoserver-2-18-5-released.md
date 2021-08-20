---
author: Andrea Aime
layout: post
title: GeoServer  Released
categories:
- Announcements
tags:
- Release
release: release_218
version: 2.18.5 
jira_version: 16822
---

We are happy to announce GeoServer [2.18.5](/release/2.18.5/) release is available for download  ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.5/geoserver-2.18.5-bin.zip/download) and [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.5/geoserver-2.18.5-war.zip/download)) along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.5/geoserver-2.18.5-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.5/extensions/).

This GeoServer 2.18.5 release was produced in conjunction with GeoTools 24.5 and GeoWebCache 1.18.4. This is a maintenance release recommended for production systems. It is also the last release of the 2.18.x series, users are warmly recommendeded to upgrade to 2.19.x, or upgrade to 2.20.0 as it gets released next month, September 2021.

Thanks to everyone who contributed, and to Alessandro Parma (GeoSolutions) and Andrea Aime (GeoSolutions) for making this release.

## Improvements and Fixes

This release improves the importer module logging, as well as the documentation on how to enable and use catalog parametrization:

- [GEOS-10194](https://osgeo-org.atlassian.net/browse/GEOS-10194) Improve importer LOGGING
- [GEOS-10149](https://osgeo-org.atlassian.net/browse/GEOS-10149) Improve Catalog Parametrization documentation

Fixes included in the release

- [GEOS-10173](https://osgeo-org.atlassian.net/browse/GEOS-10173) CoverageViewReader's format not being secured with Geofence-Geoserver
- [GEOS-10162](https://osgeo-org.atlassian.net/browse/GEOS-10162) GeoServerOAuthAuthenticationFilter creates Anonymous authentication when preAuthenticated principal is not present
- [GEOS-10193](https://osgeo-org.atlassian.net/browse/GEOS-10193) Indirect imports will drop the target table if there is any failure during the import process

For details check the [2.18.5](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16822) release notes.

## About GeoServer 2.18

Additional information on GeoServer 2.18 series:
  
  * State of GeoServer 2.18 ([slides](https://docs.google.com/presentation/d/1Q0pHRUcvucAuHDeZPoeDJG4UY5izwbqo8ZawUdk9xYM/edit?usp=sharing))
  * GeoServer Orientation
  ([slides](https://t.co/fvBTLMia6f?amp=1)|[video](https://youtu.be/bdkk5eVR674))
  * Release Notes
   ([2.18.5](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16822)
  | [2.18.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16819)
  | [2.18.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16808)
  | [2.18.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16803)
  | [2.18.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16800)
  | [2.18.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16796)
  | [2.18-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16783))

