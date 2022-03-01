---
author: jgarnett
comments: false
date: 2019-11-28 18:12:15+00:00
layout: post
link: http://blog.geoserver.org/2019/11/28/geoserver-2-16-1-released/
slug: geoserver-2-16-1-released
title: GeoServer 2.16.1 released
wordpress_id: 3074
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_216
version: 2.16.1
jira_version: 16769
---




We are pleased to announce the release of GeoServer [2.16.1](http://geoserver.org/release/2.16.1/) with downloads ([war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.1/geoserver-2.16.1-war.zip/download)|[zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.1/geoserver-2.16.1-bin.zip/download)), documentation ([html](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.1/geoserver-2.16.1-htmldoc.zip/download)|[pdf](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.1/geoserver-2.16.1-user-manual.pdf/download)) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.1/extensions/).







This is a stable release recommended for production systems.







Note: Our builds detected a change in Oracle JDK 8u221 URL handling; this release was made with 8u202 as a result. Future releases will be made using OpenJDK.







### Improvements and Fixes







This release includes a number of improvements, including:







  * The REST API now supports configuring the WMTS 
  * New hideEmptyRules LEGEND_OPTION to hide rules not matching any features






Fixes included in this release:







  * SLDService generated raster classifiers are not overwriting the default style any longer
  * Monitoring extension fixed to respect GEOSERVER_AUDIT_PATH setting
  * Cascaded WMTS now makes use of provided credentials






For more information check the [2.16.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16769) release notes.







### Security Updates







Please update your production instance of GeoServer to receive the latest security updates and fixes.







If you encounter a security vulnerability in GeoServer please respect our [responsible disclosure policy](http://geoserver.org/comm/).







### Community Updates







For developers building from source, our community modules are a great place to collaborate on functionality and improvements.







  * ncWMS GetTimeSeries now supports time ranges with period and excludes nodata from results
  * hz-cluster improved synchronization events






## About GeoServer 2.16

Features, presentations and reference material on the 2.16 series:

* State of GeoServer 2.16 ([video](https://media.ccc.de/v/bucharest-169-state-of-geoserver-2019)\|[slides](https://docs.google.com/presentation/d/1eVD8H023fp-mbiP8vNX2GFDXTDnciRUW7MJ57hJpzoY/edit?usp=sharing))
* GeoServer Feature Frenzy 2019 ([video](https://media.ccc.de/v/bucharest-170-geoserver-feature-frenzy)\|[slides](https://docs.google.com/presentation/d/1AfQyNenkpq-bT-EN1ef_y_50CyIKwZKnzleTQUcBu_M/edit?usp=sharing))
* New [SLDService extension](https://docs.geoserver.org/stable/en/user/extensions/sldservice/index.html) using data classification for style generation
* New [authentication key extension](https://docs.geoserver.org/stable/en/user/extensions/authkey/index.html) available
* Server [status page](https://docs.geoserver.org/stable/en/user/configuration/status.html#system-status) now includes system status details
* GDAL 2.x binaries are now used for GDAL [image formats](https://docs.geoserver.org/stable/en/user/data/raster/gdal.html) along with OGR [WFS output](https://docs.geoserver.org/stable/en/user/extensions/ogr.html) and [WPS output](https://docs.geoserver.org/stable/en/user/extensions/ogr.html#ogr-based-wps-output-format) formats
* Release Notes ( [2.16.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16769) \| [2.16.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16765) \| [2.16-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16750) )







