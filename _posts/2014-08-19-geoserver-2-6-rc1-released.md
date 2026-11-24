---
author: geoserver
comments: true
date: 2014-08-19 01:09:22+00:00
layout: post
link: http://blog.geoserver.org/2014/08/18/geoserver-2-6-rc1-released/
slug: geoserver-2-6-rc1-released
title: GeoServer 2.6-RC1 Released
wordpress_id: 1994
categories:
- Announcements
---

The GeoServer team is happy to account the 2.6-RC1 release, now available for [download](http://geoserver.org/release/2.6-RC1/). This release contains a number of good improvements and bug fixes since the 2.6-beta release. See the [change log](#release-notes) for more details and check out the [2.6-beta announcement]({% post_url 2014-07-24-geoserver-2-6-beta-released %}) for more about what's new in the 2.6 series.

Download the release candidate now and help us by reporting any problems in the [bug tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS) or to the [mailing list](http://sourceforge.net/p/geoserver/mailman/geoserver-users/).

Spot a translation mistake? Help translate here: [GeoServer Latest localizations](https://www.transifex.com/projects/p/geoserver/)


## About GeoServer 2.6


Articles and resources for GeoServer 2.6 series:



	
  * [Raster Views in GeoServer via the CoverageView concept](http://www.geo-solutions.it/blog/overageview-concept-for-geoserver/) (GeoSolutions)

	
  * [Advanced Raster Projection in GeoServer](http://www.geo-solutions.it/blog/developers-corner-advanced-raster-projection-geoserver/) (GeoSolutions)

	
  * [Supporting Wind Barbs In GeoServer and GeoTools](http://www.geo-solutions.it/blog/developers-corner-supporting-wind-barbs-geoserver-geotools/) (GeoSolutions)

	
  * [GeoServer now supports Vector Footprints for ImageMosaic](http://www.geo-solutions.it/blog/geoserver-supports-footprints-imagemosaic/) (GeoSolutions)

## Release notes

Improvement:

* [GEOS-6207](https://osgeo-org.atlassian.net/browse/GEOS-6207) truncate labels on border
* [GEOS-6581](https://osgeo-org.atlassian.net/browse/GEOS-6581) Allow GeoServer to store styles natively in different formats
* [GEOS-6589](https://osgeo-org.atlassian.net/browse/GEOS-6589) gs-main maven/eclipse compilation issue due to xml-apis
* [GEOS-6597](https://osgeo-org.atlassian.net/browse/GEOS-6597) Avoid full namespace scan for GetFeature requests
* [GEOS-6599](https://osgeo-org.atlassian.net/browse/GEOS-6599) Do not log all SerializableRenderedImage misguided attempts to connect to a server

Bug:

* [GEOS-5996](https://osgeo-org.atlassian.net/browse/GEOS-5996) The GeoJSON outputs the legacy crs syntax
* [GEOS-6502](https://osgeo-org.atlassian.net/browse/GEOS-6502) stroke-Dasharray style partially breaks WMS getfeatureinfo
* [GEOS-6519](https://osgeo-org.atlassian.net/browse/GEOS-6519) WPS not enabling in workspace
* [GEOS-6529](https://osgeo-org.atlassian.net/browse/GEOS-6529) NullPointerException in AdvancedDispatchFilter, seen when geoserver-monitoring included
* [GEOS-6570](https://osgeo-org.atlassian.net/browse/GEOS-6570) rendering regression with geoserver 2.5.1 when WMS 1.3.0
* [GEOS-6575](https://osgeo-org.atlassian.net/browse/GEOS-6575) Rapid Concurrent REST usage can invalidate DataStore still being used
* [GEOS-6578](https://osgeo-org.atlassian.net/browse/GEOS-6578) Unable to unwrap OracleConnection from JBoss WrappedConnectionJDK6
* [GEOS-6588](https://osgeo-org.atlassian.net/browse/GEOS-6588) GeoServer.app fails to start due to switch to Java 7
* [GEOS-6596](https://osgeo-org.atlassian.net/browse/GEOS-6596) Point symbols clipped on tile edge
* [GEOS-6598](https://osgeo-org.atlassian.net/browse/GEOS-6598) Enhancement for the VectorRenderingLayerIdentifier
* [GEOS-6604](https://osgeo-org.atlassian.net/browse/GEOS-6604) WMS GetFeatureInfo using 'vendorParams: propertyName' does not working after upgrade to 2.5.x
* [GEOS-6616](https://osgeo-org.atlassian.net/browse/GEOS-6616) Clear cached attribute information during FeatureType DELETE
* [GEOS-6617](https://osgeo-org.atlassian.net/browse/GEOS-6617) Scale computation is wrong when the map is expressed in a unit other than meters
* [GEOS-6619](https://osgeo-org.atlassian.net/browse/GEOS-6619) Rendering based feature info will return just one geometry of the group that falls into the same pixel
* [GEOS-6620](https://osgeo-org.atlassian.net/browse/GEOS-6620) Style Editor Doesn't Work without CodeMirror Editor
