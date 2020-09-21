---
author: jgarnett
comments: false
date: 2020-07-21 13:58:17+00:00
layout: post
link: http://blog.geoserver.org/2020/07/21/geoserver-2-17-2-released/
slug: geoserver-2-17-2-released
title: GeoServer 2.17.2 Released
wordpress_id: 3136
categories:
- Announcements
---




We are pleased to announce the release of GeoServer [2.17.2](http://geoserver.org/release/2.17.2/) with downloads ([war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.2/geoserver-2.17.2-war.zip/download)|[zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.2/geoserver-2.17.2-war.zip/download)), [documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.2.3/geoserver-2.17.2-war.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.2/extensions/).







This release is made in conjunction with GeoTools 23.2 and GeoWebCache 1.17.2. This is a stable release recommended for production systems.







Thanks to everyone who contributed, and Jody Garnett (GeoCat) for making this release. Additional thanks to everyone who participated in the July bug-fix sprint organized by GeoSolutions.







### Improvements and Fixes







This release includes a number of improvements, including:







  * GetFeatureInfo templates can now be used for GeoJSON output
  * The WPS download community module can now generate elevation models accounting for vertical grid shift when changing datum.
  * Oracle extension now ready to use with included JDBC driver, the driver changed to a "Oracle Free Use Terms and Conditions" license allowing us to distribute.
  * PostreSQL driver, Oracle driver, Eclipse EMF library, spring-framework, and spring-security version updates.
  * Image Mosaic REST API can now be used to update the native bbox when harvesting or deleting granules






Fixes included in this release:







  * GetFeatureInfo fixed to work on raster layer dynamically produced by a rendering transformation.
  * Lots of WMTS fixes resolving SRS list duplicates and handling of otherSrs.
  * SLD Service handling of percentages with custom classes
  * Layer preview fix, was miscounting number of pages when security restrictions used to limit number of layers available
  * Binary download on windows fixed to autodect Java when spaces used in path
  * WFS Cascade fixed to remove duplicate SRS elements when connecting to WFS 2.0.0 layer
  * MongoDB extension fixed, was missing a jar
  * Database use of select distinct in the WPS Unique process fixed 
  * Image mosaic fixes for WPS download process bbox generation, and  WMS  GetMap respect of CLIP vendor parameter,
  * GeoPackage supports raster tables with special characters






For more information check the [2.17.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16789) release notes.







### Community Updates







For developers building from source, our community modules are a great place to collaborate on functionality and improvements.







  * The JSON-LD module is under active development with templating now supporting [filtering, environmental variable substitution](https://docs.geoserver.org/latest/en/user/community/json-ld/configuration.html#filtering-support). Thanks to the sponsorship of the[ French geological survey – BRGM](https://www.brgm.eu) and the[ French environmental information systems research center – INSIDE](https://github.com/INSIDE-information-systems/).
  * The GSR community module working on packaging, addressed a startup problem.






## About GeoServer 2.17







Features, presentations and reference material on the 2.17 series:







  * New security tab on each [layer](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#edit-layer-security), [layer group](https://docs.geoserver.org/latest/en/user/data/webadmin/layergroups.html#edit-a-layer-group) and [workspace](https://docs.geoserver.org/latest/en/user/data/webadmin/workspaces.html#edit-a-workspace) page
  * Option to use [date created and date modified](https://github.com/geoserver/geoserver/wiki/GSIP-179) to sort UI lists
  * New [resource browser extension](https://docs.geoserver.org/latest/en/user/configuration/tools/resource/index.html)
  * New [Mapbox style extension](https://docs.geoserver.org/latest/en/user/styling/mbstyle/index.html)
  * FOSDEM GeoServer Orientation presentation ([slides](https://www.slideshare.net/jgarnett/geoserver-orientation)|[video](https://ftp.fau.de/fosdem/2020/AW1.126/geoserver.mp4))
  * [Full OSM data directory](https://www.geosolutionsgroup.com/blog/geoserver-osm-styles-full-data-directory-available/) for GeoServer available on GitHub
  * [Code of Conduct](https://github.com/geoserver/geoserver/blob/master/CODE_OF_CONDUCT.md)
  * Release Notes ([2.17.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16789)|[2.17.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16785)|[2.17.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16782)|[2.17-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16766))








