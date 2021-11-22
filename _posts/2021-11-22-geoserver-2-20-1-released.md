---
author: Jody Garnett
date: 2021-11-22
layout: post
title: GeoServer 2.20.1 Released
categories:
- Announcements
tags:
- Release
release: release_220
version: 2.20.1
jira_version: 16831
---

We are happy to announce GeoServer [2.20.1](/release/2.20.1/) release is available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.1/geoserver-2.20.1-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.1/geoserver-2.20.1-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.1/GeoServer-2.20.1-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.1/geoserver-2.20.1-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.1/extensions/).

This is a stable release of the 2.20.x series recommended for production systems. This release was made in conjunction with GeoTools 26.1.

### Windows installer

We are pleased to announce the return of the GeoServer windows installer.


![Windows Installer](/img/posts/2.20/windows-installer.png)<br/>
*Windows installer in action*

Thanks to Sander and the GeoCat team for completing this work on behalf of the GeoServer PSC, everyone on the user list who helped test, and Stefan Overkamp for supplying screen snaps for the documentation.

Reference:

* [Windows Insatller](https://docs.geoserver.org/stable/en/user/installation/win_installer.html) (User Guide)

### Improvements and Fixes

New Feature

* [GEOS-10228](https://osgeo-org.atlassian.net/browse/GEOS-10228) Wrap the category text values of a legend

Improvements:

* [GEOS-10298](https://osgeo-org.atlassian.net/browse/GEOS-10298) OpenSearch REST management API: allow creation of products via PUT
* [GEOS-10265](https://osgeo-org.atlassian.net/browse/GEOS-10265) WFS-T Bulk Transaction optimization
* [GEOS-10268](https://osgeo-org.atlassian.net/browse/GEOS-10268) Null Support in Features Templating

Fixes:

* [GEOS-10299](https://osgeo-org.atlassian.net/browse/GEOS-10299) Reprojection console can now work with AUTO codes
* [GEOS-10292](https://osgeo-org.atlassian.net/browse/GEOS-10292) Fixed issue changing worker pool size in raster access
* [GEOS-10289](https://osgeo-org.atlassian.net/browse/GEOS-10289) Improve Shapefile Directory performance when working with a huge number of files
* [GEOS-10282](https://osgeo-org.atlassian.net/browse/GEOS-10282) GeoServer translations files incorrectly decoded assuming UTF-8 causing translation files like GeoServerApplication\_de.properties leading characters represented as question marks
* [GEOS-10281](https://osgeo-org.atlassian.net/browse/GEOS-10281) GeoServer log level was not being picked up with during Catalog reload
* [GEOS-10277](https://osgeo-org.atlassian.net/browse/GEOS-10277) Add a special keyword for semi-colon as a CSV Separator in WFS request
* [GEOS-10273](https://osgeo-org.atlassian.net/browse/GEOS-10273) GeofenceAccesManager index out of bound issue when requesting nested layerGroups

### Community Updates

For developers building from source, our community modules are a great place to collaborate on functionality and improvements.

* [GEOS-10301](https://osgeo-org.atlassian.net/browse/GEOS-10301) The ogc-api community module resolved conflicting woodstax parser preventing editing of SLD styles

## About GeoServer 2.20

Additional information on GeoServer 2.20 series:

* [Internationalization of title and abstract](https://docs.geoserver.org/latest/en/user/services/internationalization/index.html)
* [State of GeoServer 2.20 edition](https://docs.google.com/presentation/d/19Cmld0_VFePh1g4qUSfqNWWB0t-teClFpT3eUqpYGos/edit?usp=sharing)
* [Windows Insatller](https://docs.geoserver.org/stable/en/user/installation/win_installer.html) 
* Release notes: [2.20.1](https://github.com/geoserver/geoserver/releases/tag/2.20.1), [2.20.0](https://github.com/geoserver/geoserver/releases/tag/2.20.0), [2.20-RC](https://github.com/geoserver/geoserver/releases/tag/2.20-RC)
