---
author: aaime
comments: false
date: 2020-01-22 11:35:27+00:00
layout: post
link: http://blog.geoserver.org/2020/01/22/geoserver-2-16-2-released/
slug: geoserver-2-16-2-released
title: GeoServer 2.16.2 released
wordpress_id: 3086
---




We are pleased to announce the release of GeoServer [2.16.2](http://geoserver.org/release/2.16.2/) with downloads ([war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.2/geoserver-2.16.2-war.zip/download)|[zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.2/geoserver-2.16.2-bin.zip/download)), documentation ([html](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.2/geoserver-2.16.2-htmldoc.zip/download)|[pdf](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.2/geoserver-2.16.2-user-manual.pdf/download)) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.2/extensions/).







This is a stable release recommended for production systems.







### Improvements and Fixes







This release includes a number of improvements, including:







  * Support for vector custom dimensions (in addition to time and elevation)
  * Allow limiting the number of concurrent jobs in the importer extension
  * Default style descriptions wording improvement (as they are visible in capabilities documents)






Fixes included in this release:







  * The REST API fixes regarding datastore and feature type handling (see notes for details)
  * Fixed 100% CPU usage at idle on data directories with tens of thousands of layers
  * Don't delay startup on an unresponsive cascaded WMS server
  * Make sure to truncate fully tile caches with parameters
  * Make GWC caching kick in also when using local workspaces along with non qualified layer names
  * And various others!






For more information check the [2.16.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16773) release notes.







### Community Updates







For developers building from source, our community modules are a great place to collaborate on functionality and improvements.







  * The [templated JSON-LD](https://docs.geoserver.org/stable/en/user/community/json-ld/index.html) output format, supporting both simple and complex features, has been backported to 2.16.x. We are grateful for the sponsorship of the [French geological survey – BRGM](https://www.brgm.eu/) and the [French environmental information systems research center – INSIDE](https://github.com/INSIDE-information-systems/), which made its development possible.






## About GeoServer 2.16







Features, presentations and reference material on the 2.16 series:







  * State of GeoServer 2.16 ([video](https://media.ccc.de/v/bucharest-169-state-of-geoserver-2019)|[slides](https://docs.google.com/presentation/d/1eVD8H023fp-mbiP8vNX2GFDXTDnciRUW7MJ57hJpzoY/edit?usp=sharing))
  * GeoServer Feature Frenzy 2019 ([video](https://media.ccc.de/v/bucharest-170-geoserver-feature-frenzy)|[slides](https://docs.google.com/presentation/d/1AfQyNenkpq-bT-EN1ef_y_50CyIKwZKnzleTQUcBu_M/edit?usp=sharing))
  * New [SLDService extension](https://docs.geoserver.org/stable/en/user/extensions/sldservice/index.html) using data classification for style generation
  * New [authentication key extension](https://docs.geoserver.org/stable/en/user/extensions/authkey/index.html) available
  * Server [status page](https://docs.geoserver.org/stable/en/user/configuration/status.html#system-status) now includes system status details
  * GDAL 2.x binaries are now used for GDAL [image formats](https://docs.geoserver.org/stable/en/user/data/raster/gdal.html) along with  OGR [WFS output](https://docs.geoserver.org/stable/en/user/extensions/ogr.html) and [WPS output](https://docs.geoserver.org/stable/en/user/extensions/ogr.html#ogr-based-wps-output-format) formats
  * Release Notes ([2.16.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16769)|[2.16.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16765)|[2.16-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16750))








