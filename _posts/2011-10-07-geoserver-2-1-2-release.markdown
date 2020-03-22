---
author: geoserver
comments: true
date: 2011-10-07 10:30:20+00:00
layout: post
link: http://blog.geoserver.org/2011/10/07/geoserver-2-1-2-release/
slug: geoserver-2-1-2-release
title: GeoServer 2.1.2 Released
wordpress_id: 1013
categories:
- Announcements
---

The GeoServer team is pleased to announce the release of [GeoServer 2.1.2](http://geoserver.org/display/GEOS/GeoServer+2.1.2). This is mostly a bug-fixing release, with a number of minor improvements in the administration UI and REST configuration. There are however a couple new features that you might be interested in:



	
  * The ability to mark a layer as "non advertised". Layers flagged this way won't appear in the capabilities document, making it a good way to add a layer group without having to tell the world about the layers included in it, and for any "work in progress" or temporary layer that the administrator does not want the world to see.

	
  * The imagemosaic-jdbc extension learned to load raster data from [PostGIS 2.0 WKT raster](http://trac.osgeo.org/postgis/wiki/WKTRaster). Mind, the support is pretty new and the [configuration](http://docs.geotools.org/latest/userguide/library/coverage/pgraster.html) is not for the faint of heart, but we're excited about this new developement and look forward to learn about how it works for you. Thanks to Christian Mueller for working on this.


We would also like to thank some GeoServer users that went the extra mile and contributed code and documentation patches for this release:

	
  * Lucas Heezen for contributing a REST configuration flag that allows to filter out geometryless feature types from a store ([GEOS-4741](http://jira.codehaus.org/browse/GEOS-4741))

	
  * John Hudson for adding the "ISO 19115:2003" as a type option in Layer Metadata URL ([GEOS-4595](http://jira.codehaus.org/browse/GEOS-4595))

	
  * German Osin for making sure stores are workspace qualified in REST config feature type list ([GEOS-4772](http://jira.codehaus.org/browse/GEOS-4772))

	
  * Milton Jonathan for fixing an issue occurring in REST config when switching a layer from one store to another ([GEOS-4740](http://jira.codehaus.org/browse/GEOS-4740))

	
  * Tony Young for a automatic configuration of SRS and bounds when publishing a layer via REST config ([GEOS-4596](http://jira.codehaus.org/browse/GEOS-4596))

	
  * Tim Schaub for fixing a double encoding issue in WFS exception reporting ([GEOS-4680](http://jira.codehaus.org/browse/GEOS-4680))

	
  * David Collins for a number of improvements to the user guide


Contributions like these help keep GeoServer responsive to the needs of our community and allow us to continue providing a stable and useful product. Thank you!
Thanks also go to [GeoSolutions](http://www.geo-solutions.it/) for sponsoring this release.

Please [download GeoServer 2.1.2](http://geoserver.org/display/GEOS/GeoServer+2.1.2), try it out, and provide feedback on the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users). Your feedback helps GeoServer to continue to improve.
