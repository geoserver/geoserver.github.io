---
author: Andrea Aime
date: 2022-07-01
layout: post
title: GeoServer 2.20.5 Released
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_220
version: 2.20.5
jira_version: 16844
---

We are happy to announce GeoServer [2.20.5](/release/2.20.5/) release is available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.5/geoserver-2.20.5-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.5/geoserver-2.20.5-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.5/GeoServer-2.20.5-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.5/geoserver-2.20.5-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.5/extensions/).

This is a maintenance release of the 2.20.x series recommended for production systems. This release was made in conjunction with GeoTools 26.5 and GeoWebCache 1.20.3.

### Improvements and Fixes

* The request logger is now configurable from the UI (form the "Global settings" panel),
* Importer improvements to support REPLACE mode on raster layers (in addition to the existing support for vector ones).
* The KML-PPIO module has graduated to extension (allows KML encoding of feature collections in WPS processes). It's now included in the WPS plugin download.
* WPS fetching of remote inputs can be disabled.
* Allow controlling usage of headers in proxy base URL expansion at the workspace level.

For the full list of fixes and improvements, see [2.20.5 release notes](https://github.com/geoserver/geoserver/releases/tag/2.20.5).


## About GeoServer 2.20

Additional information on GeoServer 2.20 series:

* [Log4J2 zero day vulnerability assessment]({% post_url 2021-12-13-logj4-rce-statement %})
* [Internationalization of title and abstract](https://docs.geoserver.org/latest/en/user/services/internationalization/index.html)
* [State of GeoServer 2.20 edition](https://docs.google.com/presentation/d/19Cmld0_VFePh1g4qUSfqNWWB0t-teClFpT3eUqpYGos/edit?usp=sharing)
* [Windows Installer](https://docs.geoserver.org/stable/en/user/installation/win_installer.html) 

Release notes: ( [2.20.2](https://github.com/geoserver/geoserver/releases/tag/2.20.2) \| [2.20.1](https://github.com/geoserver/geoserver/releases/tag/2.20.1) \| [2.20.0](https://github.com/geoserver/geoserver/releases/tag/2.20.0) \| [2.20-RC](https://github.com/geoserver/geoserver/releases/tag/2.20-RC) )
