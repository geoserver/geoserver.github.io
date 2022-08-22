---
author: Jody Garnett
date: 2022-08-22
layout: post
title: GeoServer 2.22-M0 Milestone Release
categories:
- Announcements
tags:
- Release
- Milestone
release: release_222
version: 2.22-M0
jira_version: 16856
---

GeoServer [2.22-M0](/release/2.22-M0/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22-M0/geoserver-2.22-M0-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22-M0/geoserver-2.22-M0-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22-M0/GeoServer-2.22-M0-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22-M0/geoserver-2.22-M0-htmldoc.zip/download), [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22-M0/extensions/), and [data directory](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22-M0/geoserver-2.22-M0-data.zip/download).

This is a milestone release previewing the GeoServer 2.22.x series for FOSS4G attendees.

Thanks to Jody Garnett and Ian Turton for making this release.

### Docker image

This release is also available as an official [Docker image](https://github.com/geoserver/docker):

```
docker pull docker.osgeo.org/geoserver:2.22-M0
docker run -it -p 80:8080 docker.osgeo.org/geoserver:2.22-M0
```

### Welcome Page Improvements

The welcome page has been improved with the ability to:

* Select workspace to browse workspace web services
* Select layer and layergroup for layer specific web services

![Welcome workspace](/img/posts/2.22/welcome-workspace.png) <br/>

### GeoPackage Sample data

The sample data directory now includes a small geopackage generated from [Natural Earth](https://www.naturalearthdata.com) data.

![World map](/img/posts/2.22/world-map.png) <br/>

## About GeoServer 2.22

Release notes:
( [2.22-M0](https://github.com/geoserver/geoserver/releases/tag/2.22-M0)
)
