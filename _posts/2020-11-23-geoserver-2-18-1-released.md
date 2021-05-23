---
author: Andrea Aime
comments: false
date: 2020-11-23
layout: post
title: GeoServer 2.18.1 Released
categories:
- Announcements
tags:
- Release
release: release_218
version: 2.18.1
jira_version: 16800
---

We are pleased to announce the release of GeoServer [2.18.1](http://geoserver.org/release/2.18.1/) with downloads (
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.1/geoserver-2.18.1-war.zip/download) |
[bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.1/geoserver-2.18.1-bin.zip/download) ),
[documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.1/geoserver-2.18.1-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.1/extensions/).

This release is made in conjunction with GeoTools 24.1 and GeoWebCache 1.18.1. This is a stable release recommended for production systems.

Thanks to everyone who contributed, and Alessandro Parma, Andrea Aime (GeoSolutions) for making this release.

### Improvements and Fixes

This release includes a number of improvements. Notable improvements:

  * New option allow to tile cache WMS requests that align to gridsets, even if ``tiled=true`` is not present.
  * New process grouping features by attribute, and then selecting a single one out of the group, in particular, the feature with the min or max value of a given attribute. Can be used either as a rendering transformation or a stand-alone WPS process.
  * GeoFence integrated UI allows to configure security rules by IP address ranges.

Fixes included in this release:

  * Better WPS packaging, including the required CSV libraries.
  * Better support for WMS XML post requests in workspace local services.
  * Addressed incompatibility with macOS 11 preventing startup

For more information check the [2.18.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16800) release notes.

### Community Updates

For developers building from source, our community modules are a great place to collaborate on functionality and improvements.

  * The "feature template" module has received assorted improvements

## About GeoServer 2.17

Additional information on GeoServer 2.18 series:
  
  * State of GeoServer 2.18 ([slides](https://docs.google.com/presentation/d/1Q0pHRUcvucAuHDeZPoeDJG4UY5izwbqo8ZawUdk9xYM/edit?usp=sharing))
  * GeoServer Orientation
  ([slides](https://t.co/fvBTLMia6f?amp=1)|[video](https://youtu.be/bdkk5eVR674))
  * Release Notes
  ([2.18.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16800)
  | [2.18.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16796)
  | [2.18-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16783))


