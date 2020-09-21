---
author: sfarber
comments: true
date: 2007-06-12 19:26:21+00:00
layout: post
link: http://blog.geoserver.org/2007/06/12/geoserver-arcsde-rasters-in-geoserver-151/
slug: geoserver-arcsde-rasters-in-geoserver-151
title: GeoServer ArcSDE Rasters in GeoServer-1.5.1
wordpress_id: 52
categories:
- Announcements
---

With the recent release of GeoServer-1.5.1, the GeoServer ArcSDE Extension has gained the ability to serve ArcSDE raster datasets, as well as the vector datasets it's been serving so far.

Detailed instructions can be found on the [GeoServer ArcSDE Plugin page](http://docs.codehaus.org/display/GEOSDOC/ArcSDE+DataStore), and if any crack coders out there want to see support for more ArcSDE raster formats (other than the 3/4-band unsigned byte format we currently support) then help us get coding!

If you're itching to see an example in action, check out [this map](http://64.119.128.70/geoserver/wms?bbox=33000.25,774000.25,332999.75,961999.75&styles=&Format=application/openlayers&request=GetMap&layers=massgis:GISDATA.IMG_COQ2005&width=800&height=470&srs=EPSG:26986) or [this map](http://64.119.128.70/geoserver/wms?bbox=17158.282150121104,802092.6629727356,348896.05662356125,960035.9428434585&request=GetMap&layers=massgis:GISDATA.IMG_COQ2005,massgis:GISDATA.ACECS_POLY,massgis:GISDATA.TOWNS_POLY,massgis:GISDATA.NAVTEQRDS_ARC,massgis:GISDATA.OPENSPACE_POLY&width=800&height=600&srs=EPSG:26986&styles=,,,GISDATA.NAVTEQRDS_ARC::ForOrthos,&Format=application/openlayers).

Happy rasters!
