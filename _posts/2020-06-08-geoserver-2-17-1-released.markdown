---
author: jgarnett
comments: false
date: 2020-06-08 19:57:03+00:00
layout: post
link: http://blog.geoserver.org/2020/06/08/geoserver-2-17-1-released/
slug: geoserver-2-17-1-released
title: GeoServer 2.17.1 Released
wordpress_id: 3132
---




We are pleased to announce the release of GeoServer [2.17.1](http://geoserver.org/release/2.17.1/) with downloads ([war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.1/geoserver-2.17.1-war.zip/download)|[zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.1/geoserver-2.17.1-war.zip/download)), [documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.1/geoserver-2.17.1-war.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.1/extensions/).







This release is made in conjunction with GeoTools 23.1 and GeoWebCache 1.17.1. This is a stable release recommended for production systems.







Thanks to everyone who contributed, and Jody Garnett (GeoCat) for making this release. Additional thanks to Jukka, Charles, Jody and Graham for helping test on the GeoServer [user list](http://geoserver.org/comm/). Testing in a wide range of environments is important for the community, and we appreciate seeing more people involved.







### Improvements and Fixes







This release includes a number of improvements, including:







  * SLD Service Extension now supports percentages when generating rule titles, or individual colormap entries
  * SLD Service generation fix to avoid duplicating classes in generated style






Fixes included in this release:







  * WMS Legend decoration fix to correct image size calculation, and to display legend for raster layers
  * Fix WPS DownloadMap process to support use of WMS Legend decoration
  * Fix for vector tile generation, taking into account line width to prevent gaps between tiles 






For more information check the [2.17.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16785) release notes.







### Community Updates







For developers building from source, our community modules are a great place to collaborate on functionality and improvements.







  * A [GSR community module](https://docs.geoserver.org/latest/en/user/community/gsr/index.html) is now available providing an GeoService REST compatibility API.
  * Backup restore development continues, with an option to exclude select content during restore 
  * We have removed all references to the spatialite datastore from our documentation as this extension has not been produced for some time. Those wishing to work with spatialite can do so via the ogr datastore.






## About GeoServer 2.17







Features, presentations and reference material on the 2.17 series:







  * New security tab on each [layer](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#edit-layer-security), [layer group](https://docs.geoserver.org/latest/en/user/data/webadmin/layergroups.html#edit-a-layer-group) and [workspace](https://docs.geoserver.org/latest/en/user/data/webadmin/workspaces.html#edit-a-workspace) page
  * Option to use [date created and date modified](https://github.com/geoserver/geoserver/wiki/GSIP-179) to sort UI lists
  * New [resource browser extension](https://docs.geoserver.org/latest/en/user/configuration/tools/resource/index.html)
  * New [Mapbox style extension](https://docs.geoserver.org/latest/en/user/styling/mbstyle/index.html)
  * FOSDEM GeoServer Orientation presentation ([slides](https://www.slideshare.net/jgarnett/geoserver-orientation)|[video](https://ftp.fau.de/fosdem/2020/AW1.126/geoserver.mp4))
  * [Full OSM data directory](https://www.geosolutionsgroup.com/blog/geoserver-osm-styles-full-data-directory-available/) for GeoServer available on GitHub
  * [Code of Conduct](https://github.com/geoserver/geoserver/blob/master/CODE_OF_CONDUCT.md)
  * Release Notes ([2.17.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16785)|[2.17.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16782))








