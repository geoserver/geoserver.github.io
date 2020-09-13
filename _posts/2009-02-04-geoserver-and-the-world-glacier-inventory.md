---
author: bmmpxf
comments: true
date: 2009-02-04 16:50:08+00:00
layout: post
link: http://blog.geoserver.org/2009/02/04/geoserver-and-the-world-glacier-inventory/
slug: geoserver-and-the-world-glacier-inventory
title: GeoServer and the World Glacier Inventory
wordpress_id: 184
categories:
- User perspectives
---

The most common question I hear from GeoServer users is:  "Who else is using GeoServer?"  So when I find a great example of GeoServer in the wild, I like to pass it along.

The [National Snow and Ice Data Center](http://nsidc.org/) in Boulder, Colorado has a large collection of freely downloadable data, and they are [serving this data with KML](http://nsidc.org/data/virtual_globes/) for viewing in virtual globe environments such as [Google Earth](http://geoserver.org/display/GEOSDOC/Google+Earth).  Buried in their [Google Earth Technical Experiments](http://nsidc.org/data/virtual_globes/beta.html) page, they have the [World Glacier Inventory](http://nsidc.org/data/virtual_globes/noaa/NSIDC_WorldGlacierInventory.kml), the location and attributes of thousands of glaciers throughout the world.

The NSIDC uses GeoServer to serve this data and to export KML files.  Lisa Ballagh of the NSIDC recently [gave a talk at the American Geophysical Union conference](http://www.youtube.com/watch?v=f2KgK0UKRtU) in San Francisco, where she described why and how her organization uses GeoServer. This short talk is interesting and well worth a watch, and the images of glaciers as they have changed over time are truly striking.

[Check out the NSIDC site](http://nsidc.org/data/virtual_globes/), [download the WGI data](http://nsidc.org/data/virtual_globes/noaa/NSIDC_WorldGlacierInventory.kml), and view it in Google Earth.  And look for the World Glacier Inventory to be available on Google Maps soon, as part of [GeoServer's integration with Google's Geo Search](http://blog.geoserver.org/2008/05/13/geoserver-and-googles-geo-search/).
