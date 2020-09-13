---
author: aaime
comments: false
date: 2020-05-21 10:28:12+00:00
layout: post
link: http://blog.geoserver.org/2020/05/21/geoserver-2-16-3-released/
slug: geoserver-2-16-3-released
title: GeoServer 2.16.3 released
wordpress_id: 3130
---




We are pleased to announce the release of GeoServer [2.16.3](http://geoserver.org/release/2.16.3/) with downloads ([war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.3/geoserver-2.16.3-war.zip/download)|[zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.3/geoserver-2.16.3-bin.zip/download)), [HTML documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.3/geoserver-2.16.3-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.3/extensions/).







This is a stable release recommended for production systems.







### Improvements and Fixes







This release includes a number of improvements, including:







  * New ["clip" vendor option](https://docs.geoserver.org/maintain/en/user/services/wms/vendor.html#clip) in WMS GetMap.
  * The SLD generation service can now create classified styles with per class [percentages of occupation](https://docs.geoserver.org/maintain/en/user/extensions/sldservice/index.html#classify-raster-and-vector-data).
  * Various WMS cascading improvements, including:
    * Options to configure min/max scale denominator for cascaded WMS layers, as well as to limit the cascading requests to the declared BBOX.
    * Options to configure formats and styles used in cascading.
    * GetLegendGraphic now works with external WMS layers too.
  * The configuration UI got improved too, in particular:
    * It's possible to show dates of creation and last modification in the resource lists (layers, stores, and so on).
    * Search filters in lists are now remembered when moving across pages.
    * Data level security can be edited in a new dedicated tab at the single resource level (e.g., while in the layer page).
  * Mass truncation requests added to GWC, and the tile layer page lists layers faster
  * Monitoring can now skip post-processors, and can log the time needed to render each layer in a multi-layer request.
  * WFS supports per workspace stored queries.
  * The SQL Server now ships with the latest open source JDBC driver by Microsoft, no longer need to fetch it separately.
  * The download process (community module) can now return image mosaic single granules in their native CRS, when requesting a single one out of a heterogeneous CRS mosaic.
  * Layer level CQL filter is now respected by complex feature layers too.






Fixes included in this release:







  * WMS legend decorations  got some attention, improving their size management
  * Improved support for map wrapping while using rendering transformations generating raster data (raster to raster or vector to raster ones)
  * And various others!






For more information check the [2.16.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16773) release notes.







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
  * Release Notes ([2.16.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16773) | [2.16.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16769)|[2.16.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16765)|[2.16-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16750))








