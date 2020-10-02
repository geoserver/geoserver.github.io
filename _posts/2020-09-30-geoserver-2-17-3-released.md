---
author: Andrea Aime
comments: false
date: 2020-09-30
layout: post
title: GeoServer 2.17.3 Released
categories:
- Announcements
tags:
- Release
---


We are pleased to announce the release of GeoServer [2.17.3](http://geoserver.org/release/2.17.3/) with downloads ([war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.3/geoserver-2.17.3-war.zip/download)|[bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.3/geoserver-2.17.3-bin.zip/download)), [documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.3/geoserver-2.17.3-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.3/extensions/).



This release is made in conjunction with GeoTools 23.3 and GeoWebCache 1.17.3. This is a maintenance release recommended for production systems.


Thanks to everyone who contributed, and Alessandro Parma, Andrea Aime (GeoSolutions) for making this release.



### Improvements and Fixes

This release includes a number of improvements. Notable improvements:


  * SLDService can now advertise supported classification methods (for future proofing clients, in case new methods are added later down the road). A new standard deviation based classification method has been added.
  * App-schema generating simple feature outputs (pure mapping) can now be used with all the common simple feature formats too, like shapefile, CSV, KML and so on.
  * It's possible to disable auto-complete of the UI login
  * Importer has been optimized to avoid full directory scans while importing single files. This coupled with similar optimizations in image mosaic harvesting, speeds up significantly harvesting new files via importer, when contained in directories having many files.
  * The vector tiles output can now get full benefit from a pre-generalized data source, reading the features at the resolution required to generate the vector tiles (was previously using the highest resolution available).
  * The Jiffle process/rendering transformation can now generate multi-band outputs, and its performance received a few improvements.

Fixes included in this release:

  * Memory management of raster GDAL sources has been improved.
  * Layer preview with strict WMS compliance was not working any longer, this has been fixed.


For more information check the [2.17.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16794) release notes.


### Community Updates

For developers building from source, our community modules are a great place to collaborate on functionality and improvements.


  * The wfs-templating module has received a few improvements, and has been renamed to features-templating, to clarify it can be used with OGC API - Feautures, as well as WFS.


## About GeoServer 2.17


Features, presentations and reference material on the 2.17 series:


  * New security tab on each [layer](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#edit-layer-security), [layer group](https://docs.geoserver.org/latest/en/user/data/webadmin/layergroups.html#edit-a-layer-group) and [workspace](https://docs.geoserver.org/latest/en/user/data/webadmin/workspaces.html#edit-a-workspace) page
  * Option to use [date created and date modified](https://github.com/geoserver/geoserver/wiki/GSIP-179) to sort UI lists
  * New [resource browser extension](https://docs.geoserver.org/latest/en/user/configuration/tools/resource/index.html)
  * New [Mapbox style extension](https://docs.geoserver.org/latest/en/user/styling/mbstyle/index.html)
  * FOSDEM GeoServer Orientation presentation ([slides](https://www.slideshare.net/jgarnett/geoserver-orientation)|[video](https://ftp.fau.de/fosdem/2020/AW1.126/geoserver.mp4))
  * [Full OSM data directory](https://www.geosolutionsgroup.com/blog/geoserver-osm-styles-full-data-directory-available/) for GeoServer available on GitHub
  * [Code of Conduct](https://github.com/geoserver/geoserver/blob/master/CODE_OF_CONDUCT.md)
  * Release Notes ([2.17.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16789)|[2.17.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16785)|[2.17.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16782)|[2.17-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16766))








