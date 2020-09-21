---
author: tbarsballe
comments: false
date: 2019-01-19 00:08:17+00:00
layout: post
link: http://blog.geoserver.org/2019/01/19/geoserver-2-14-2-released/
slug: geoserver-2-14-2-released
title: GeoServer 2.14.2 Released
wordpress_id: 2997
---

We are happy to announce the release of [GeoServer 2.14.2](http://geoserver.org/release/2.14.2/). Downloads are provided ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.2/geoserver-2.14.2-bin.zip/download)|[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.2/geoserver-2.14.2-war.zip/download)|[exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.2/geoserver-2.14.2.exe/download)) along with docs ([html](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.2/geoserver-2.14.2-htmldoc.zip/download)|[pdf](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.2/geoserver-2.14.2-user-manual.pdf/download)) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.2/extensions/).

This is a stable release of the GeoServer 2.14 series and is recommended for all production systems. Users of prior releases of GeoServer are encouraged to upgrade.

This release is made in conjunction with GeoTools 20.2 and GeoWebCache 1.14.2. Thanks to all who contributed to this release.

For more information please see our release notes ([2.14.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16744) | [2.14.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16739)|[2.14.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16734)|[2.14-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16718)).


## Improvements and Fixes


This release includes a number of new features and improvements:



 	
  * WMTS Restful binding is now accessible to all users (used to be limited to admins) and works with workspace specific services

 	
  * gs:DownloadEstimator (almost always) returns true when estimating full raster downloads at native resolution

 	
  * Cannot create jp2k coverage through rest (IndexOutOfBounds)

 	
  * KML ignores sortBy parameter when querying records

 	
  * NullPointerException when using env() function with LIKE operator in CSS filters

 	
  * Can't modify existing GWC blobstore via UI without renaming

 	
  * NPE if a Jiffle Rendering Transformation is used with Channel Selection

 	
  * OpenLayers2 preview does not trigger automatically on IE8

 	
  * Bad rendering with JAI-EXT and Input/Output TransparentColor options

 	
  * Complex MongoDB generated properties are not correctly handlded in SLDs

 	
  * Move the GeoServer ENV Parametrization documentation to a more general Section

 	
  * Allow expressions in ColorMapEntry labels for GetLegendGraphic




## About GeoServer 2.14 Series


Additional information on the GeoServer 2.14 series:



 	
  * New [MongoDB extension](https://docs.geoserver.org/latest/en/user/extensions/mongodb/index.html) added

 	
  * Style editor improvements including [side by side editing](https://docs.geoserver.org/latest/en/user/styling/webadmin/index.html#style-editor-full-screen-side-by-side-mode)

 	
  * Nearest match support for [WMS dimension handling](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#edit-layer-dimensions)

 	
  * Upgrade notes documenting [REST API feature type definition change](https://docs.geoserver.org/stable/en/user/installation/upgrade.html#jts-type-bindings-geoserver-2-14-and-newer)

 	
  * [State of GeoServer 2.14](https://www.slideshare.net/jgarnett/state-of-geoserver-214) (SlideShare)

 	
  * [GeoServer Ecosystem](https://www.slideshare.net/jgarnett/geoserver-ecosystem-2018) (SlideShare)

 	
  * [GeoServer Developers Workshop](https://www.slideshare.net/jgarnett/geoserver-developers-workshop) (SlideShare)


