---
author: Jody Garnett
date: 2022-01-24
layout: post
title: GeoServer 2.20.2 Released
categories:
- Announcements
tags:
- Release
- Vulnerability
release: release_220
version: 2.20.2
jira_version: 16835
---

We are happy to announce GeoServer [2.20.2](/release/2.20.2/) release is available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.2/geoserver-2.20.2-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.2/geoserver-2.20.2-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.2/GeoServer-2.20.2-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.2/geoserver-2.20.2-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.2/extensions/).

This is a stable release of the 2.20.x series recommended for production systems. This release was made in conjunction with GeoTools 26.2 and GeoWebCache 1.20.1.

### Security Considerations

This release includes several security enhancements and is a recommended upgrade for production systems:

* GeoServer uses the earlier log4j1 library and is not subject to the Log4j2 remote code execution vulnerabilities reported worldwide. For a detailed discussion please read [GeoServer Log4J2 zero day vulnerability assessment]({% post_url 2021-11-22-logj4-rce-statement %}).

  The release of GeoServer includes a patched version of log4j1 which does not include any remote loggers or socket communication.

If you wish to report a security vulnerability, please visit our website for [instructions on responsible reporting](http://geoserver.org/issues/).

### Mark Factory Precedence

When rendering maps with lots of individual graphics, looking up the correct implementation (known as a MarkFactory) can be time consuming.

WMS Settings have new capability to filter out any mark factories not being used, and provide an order to prioritise the ones being used.

For more information see [WMS Web Administration](https://docs.geoserver.org/stable/en/user/services/wms/webadmin.html#mark-factory-precedence) (user guide).

### Source Code

For developers building from source, we have committed a ``.gitattributes`` file to help preserve consistent line encoding across our repository.

With this change it is no longer necessary to set your global configuration to ``core.autocrlf=input``.

Use ``git reset`` as outlined below if encounter difficulty updating your checkout:
```
git pull --rebase
git reset --hard
```

### Improvements and Fixes

* WMS rendering preserves region of interest when clipping working with palette based images
* Importer improvements to better report failed imports and clean up stale importer contents
* WCS return coverages whose native BBOX are slightly outside of the dateline
* Reduce the CPU load of returning Server Status information using OSHI on windows

For more information see [2.20.2 release notes](https://github.com/geoserver/geoserver/releases/tag/2.20.2).


## About GeoServer 2.20

Additional information on GeoServer 2.20 series:

* [Log4J2 zero day vulnerability assessment]({% post_url 2021-11-22-logj4-rce-statement %})
* [Internationalization of title and abstract](https://docs.geoserver.org/latest/en/user/services/internationalization/index.html)
* [State of GeoServer 2.20 edition](https://docs.google.com/presentation/d/19Cmld0_VFePh1g4qUSfqNWWB0t-teClFpT3eUqpYGos/edit?usp=sharing)
* [Windows Installer](https://docs.geoserver.org/stable/en/user/installation/win_installer.html) 

Release notes: ( [2.20.2](https://github.com/geoserver/geoserver/releases/tag/2.20.2) \| [2.20.1](https://github.com/geoserver/geoserver/releases/tag/2.20.1) \| [2.20.0](https://github.com/geoserver/geoserver/releases/tag/2.20.0) \| [2.20-RC](https://github.com/geoserver/geoserver/releases/tag/2.20-RC) )
