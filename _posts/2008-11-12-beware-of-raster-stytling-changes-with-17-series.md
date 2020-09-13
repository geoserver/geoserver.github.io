---
author: simone.giannecchini
comments: true
date: 2008-11-12 18:57:57+00:00
layout: post
link: http://blog.geoserver.org/2008/11/12/beware-of-raster-stytling-changes-with-17-series/
slug: beware-of-raster-stytling-changes-with-17-series
title: Beware of Raster styling changes with 1.7 series
wordpress_id: 147
categories:
- Developer notes
- Features
- Tips and Tricks
tags:
- raster
- RasterSymbolizer
- SLD
- wms
---

Starting with the 1.7.0 release GeoServer comes with a pretty decent (well, at least IMHO :-) ) implementation of the SLD 1.0 RasterSymbolizer element (check [here ](http://docs.codehaus.org/display/GEOTOOLS/Raster+Symbolizer+support)for a technical discussion on the implementation). On a side this means that we can try to style raster data as well as verctor data. On the other side, this means that if you update GeoServer from an older installation, let's say 1.6.4 you can get into troubles with preexisting raster data since **the old default raster.sld in no longer legal**. [Here](https://svn.codehaus.org/geoserver/branches/1.6.x/configuration/release/styles/raster.sld) you can find the old raster.sld, while [here](https://svn.codehaus.org/geoserver/tags/1.7.2/data/release/styles/raster.sld) you can find the new one. which works for 1.7.x and successive releases. Long story short, rationale behind this is that with older geoServer releases we did not have a RasterSymbolizer implementation hence we were simply ignoring most elements of the raster.sld file. From 1.7.0 and on we have a decent RasterSymbolizer implementation, hence the old raster.sld style can no longer be used lightly since it makes assumptions on the underlying data. As a result the new default raster style is just an empty stub.

Summarising, if you are updating GeoSerber from 1.6.x or older, make sure to check to replace the raster.sld with the new onw.

Ciao a tutti.
