---
author: bmmpxf
comments: true
date: 2009-04-30 14:35:48+00:00
layout: post
link: http://blog.geoserver.org/2009/04/30/geoserver-174-released/
slug: geoserver-174-released
title: GeoServer 1.7.4 Released
wordpress_id: 211
categories:
- Polls
- Tutorials
tags:
- release
---

The GeoServer Team is happy to announce the the release of [GeoServer 1.7.4](http://geoserver.org/display/GEOS/GeoServer+1.7.4), the fifth stable version in the 1.7 series.

This release contains some new features, many having to do with improved map rendering options.  We have introduced [WMS decoration](http://docs.geoserver.org/1.7.4/user/advanced/wmsdecoration.html), which provides a framework for adding images such as compasses and legends to WMS requests using absolute, not spatial, positioning.  The GetFeatureInfo request, often used when clicking on an OpenLayers map, now has a parameter that can be adjusted to allow for looser tolerance, eliminating the need to click precisely on the feature.  GetFeatureInfo also now observes the filters in the SLD, so as to prevent displaying information about a hidden feature.  (Thanks to [SATA Hi-Tech Services](http://www.sata-hts.com/), an Italian company specializing in data security solutions, for providing funding for the GetFeatureInfo improvements.)  Those who work with labels on your map will be pleased to note that label conflict resolution (the selective display of labels to prevent visual collisions) can now be turned off if desired.  Finally, we have the ability to generate [custom legends for raster files](http://geoserver.org/display/GEOS/Raster+Legends+Explained) via the GetLegendGraphic request.

And, as usual, a whole host of [bug fixes](http://jira.codehaus.org/browse/GEOS/fixforversion/14787) (over 50!) have been incorporated into this release.  [Give it a try!](http://geoserver.org/display/GEOS/GeoServer+1.7.4)

Development work on the 1.7 series will begin to wind down in favor of [GeoServer 2.0](http://blog.geoserver.org/2009/04/20/see-the-new-ui/), but we anticipate the release of 1.7.5 within the next two months.
