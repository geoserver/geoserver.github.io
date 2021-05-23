---
author: Andrea Aime
comments: false
date: 2021-01-20
layout: post
title: GeoServer 2.18.2 Released
categories:
- Announcements
tags:
- Release
release: release_218
version: 2.18.2
jira_version: 16803
---

We are pleased to announce the release of GeoServer [2.18.2](http://geoserver.org/release/2.18.2/) with downloads (
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.2/geoserver-2.18.2-war.zip/download) |
[bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.2/geoserver-2.18.2-bin.zip/download) ),
[documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.2/geoserver-2.18.2-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.2/extensions/).

This release is made in conjunction with GeoTools 24.2 and GeoWebCache 1.18.2. This is a stable release recommended for production systems.

Thanks to everyone who contributed, and Alessandro Parma, Andrea Aime (GeoSolutions) for making this release.

### Improvements and Fixes

This release includes a number of fixes in core and extensions:

  * Improved GWC seeding scalability (also check GWC 1.18.2 release notes).
  * Fixed back-links generation during WPS asynchronous requests, when a proxy base URL is used.
  * Fixed a GeoFence server packaging issue.
  * A number of dependent libraries have been upgraded, including the PostgreSQL and MySQL JDBC drivers, HTTP components, Guava.

### Community Updates

Things get really interesting when looking at functionality provided by community modules:

  * The [new support for COGs](https://docs.geoserver.org/stable/en/user/community/cog/index.html) based on ImageIO Ext landed in a community module, adding it adds support for COG in both the GeoTIFF reader and image mosaic. Support for harvesting COG granules is also added in the REST API.
  * A deadlock in JDBCConfig has been resolved, along with issues related to high load when GeoServer has just started up.
  * The WPS download "map" and "animation" processes sport improved legend support.

For more information check the [2.18.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16803) release notes.

## About GeoServer 2.18

Additional information on GeoServer 2.18 series:
  
  * State of GeoServer 2.18 ([slides](https://docs.google.com/presentation/d/1Q0pHRUcvucAuHDeZPoeDJG4UY5izwbqo8ZawUdk9xYM/edit?usp=sharing))
  * GeoServer Orientation
  ([slides](https://t.co/fvBTLMia6f?amp=1)|[video](https://youtu.be/bdkk5eVR674))
  * Release Notes
  ( [2.18.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16803)
  | [2.18.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16800)
  | [2.18.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16796)
  | [2.18-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16783))


