---
author: Andrea Aime
date: 2022-09-15
layout: post
title: GeoServer 2.20.6 Released
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_220
version: 2.20.6
jira_version: 16858
---

We are happy to announce GeoServer [2.20.6](/release/2.20.6/) release is available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.6/geoserver-2.20.6-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.6/geoserver-2.20.6-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.6/GeoServer-2.20.6-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.6/geoserver-2.20.6-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.6/extensions/).

This is the last planned maintenance release for the 2.20.x series, please consider upgrading to the 2.21.x series. 
This release was made in conjunction with GeoTools 26.6 and GeoWebCache 1.20.4.

### Improvements and Fixes

* It's now possible to use the REST API to reset caches for a single store or a single layer.
* GeoFence role filtering was improved.
* OSHI was updated to allow gathering OS statistics on Apple M2 as well.
* Assorted small improvements to the status page.
* An infinite recursion in GWC transparent integration with WMS was spotted and fixed (affected vector tiles and layers with a meta-tiling factor of 1, when the "TILED" parameter was turned off).
* The GWC module was split so that its REST API can be excluded (for completely headless installs).

For the full list of fixes and improvements, see [2.20.6 release notes](https://github.com/geoserver/geoserver/releases/tag/2.20.6).

## About GeoServer 2.20

Additional information on GeoServer 2.20 series:

* [Log4J2 zero day vulnerability assessment]({% post_url 2021-12-13-logj4-rce-statement %})
* [Internationalization of title and abstract](https://docs.geoserver.org/latest/en/user/services/internationalization/index.html)
* [State of GeoServer 2.20 edition](https://docs.google.com/presentation/d/19Cmld0_VFePh1g4qUSfqNWWB0t-teClFpT3eUqpYGos/edit?usp=sharing)
* [Windows Installer](https://docs.geoserver.org/stable/en/user/installation/win_installer.html) 

Release notes:
( [2.20.6](https://github.com/geoserver/geoserver/releases/tag/2.20.6)
\| [2.20.5](https://github.com/geoserver/geoserver/releases/tag/2.20.5)
\| [2.20.4](https://github.com/geoserver/geoserver/releases/tag/2.20.4)
 \| [2.20.3](https://github.com/geoserver/geoserver/releases/tag/2.20.3)
\| [2.20.2](https://github.com/geoserver/geoserver/releases/tag/2.20.2)
 \| [2.20.1](https://github.com/geoserver/geoserver/releases/tag/2.20.1)
\| [2.20.0](https://github.com/geoserver/geoserver/releases/tag/2.20.0)
 \| [2.20-RC](https://github.com/geoserver/geoserver/releases/tag/2.20-RC) )