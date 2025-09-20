---
author: Jody Garnett
date: 2025-09-22
layout: post
title: GeoServer 2.28-M0 Milestone Release
categories:
- Announcements
tags:
- Release
release: release_228
version: 2.28-M0
jira_version: 17009
---

GeoServer [2.28-M0](/release/2.28-M0/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28-M0/geoserver-2.28-M0-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28-M0/geoserver-2.28-M0-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28-M0/GeoServer-2.28-M0-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28-M0/geoserver-2.28-M0-htmldoc.zip/download), [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28-M0/extensions/), and [data directory](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28-M0/geoserver-2.28-M0-data.zip/download).

This is a milestone release previewing the GeoServer 2.28.x series to let everyone try out our new ImageN raster processing engine.

This release is made as part of the [GeoServer 3 "Milestone 1"]() activity. It is made in conjunction with
[ImageN 0.4.0](https://github.com/eclipse-imagen/imagen/releases/tag/0.4.0),
[ImageIO-Ext 2.0.0-M0](https://github.com/geosolutions-it/imageio-ext/releases/tag/2.0.0-M0),
[GeoTools 34-M0](https://github.com/geotools/geotools/releases/tag/34-M0),
[mapfish-print-v2 2.4-M0](https://github.com/mapfish/mapfish-print-v2/releases/tag/release%2F2.4-M0),
and [GeoWebCache 1.28-M0]().

Thanks to Jody Garnett (GeoCat) and Ian Turton for making this release.

### Milestone Release

Milestone releases are a chance to share what we have been working on, and ask you to try it with your own data:

* A new **Eclipse ImageN** (pronounced "imagine") processing engine.
  
  This project combining Java Advanced Imaging (donated by Oracle) and JAI-Ext (donated by GeoSolutions) into a single image processing engine optmized for a modern Java environment.

* Speaking of modern Java Environment GeoServer now requires **Java 17 minimum**. Java 11 no longer supported. GeoServer is testing with Long Term Support releases: Java 17 LTS and Java 21 LTS.

* Lots of build improvements with the highlight being a **bill-of-materials** "geotools" pom.xml file to share managing versions across GeoTools, GeoWebCache and GeoServer

* A new community module **gs-sec-oidc-plugin** under active development.
  
  This plugin will be taking over the responsibilities of **gs-oauth2** plugins when they are retired for GeoServer 3.

We know a few things are broken in our release process:

* javadocs download is empty

  This is due to changing to JDK 17, and a large number of javadoc warrnings we now need to resolve.

* GeoServer 2.28-M0 artifacts were not published to repo.osgeo.org

## About GeoServer 2.28

Release notes:
( [2.28-M0](https://github.com/geoserver/geoserver/releases/tag/2.28-M0)
)
