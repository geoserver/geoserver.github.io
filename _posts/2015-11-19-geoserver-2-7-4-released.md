---
author: geoserver
comments: true
date: 2015-11-19 17:29:38+00:00
layout: post
link: http://blog.geoserver.org/2015/11/19/geoserver-2-7-4-released/
slug: geoserver-2-7-4-released
title: GeoServer 2.7.4 released
wordpress_id: 2410
categories:
- Announcements
---

The GeoServer team is happy to announce the release of [GeoServer 2.7.4](http://geoserver.org/release/2.7.4/). Download bundles are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.4/geoserver-2.7.4-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.4/geoserver-2.7.4-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.4/geoserver-2.7.4.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.4/geoserver-2.7.4.exe/download))  along with documentation and extensions.

GeoServer 2.7.3 is a maintenance release of GeoServer recommended for production deployment. Thanks to everyone taking part, submitting fixes and new functionality including:


## Bug





	
  * [[GEOS-3228](https://osgeo-org.atlassian.net/browse/GEOS-3228)] - Empty filter causes IndexOutOfBoundsException

	
  * [[GEOS-3432](https://osgeo-org.atlassian.net/browse/GEOS-3432)] - RESTConfig "styles" list does not get generated if a style is missing its associated sld file

	
  * [[GEOS-4986](https://osgeo-org.atlassian.net/browse/GEOS-4986)] - Creating SQL Views via RESTConfig as JSON fails

	
  * [[GEOS-6768](https://osgeo-org.atlassian.net/browse/GEOS-6768)] - externalGraphic with relative path and query parameters problem

	
  * [[GEOS-7045](https://osgeo-org.atlassian.net/browse/GEOS-7045)] - Layer Security - Catalog Mode

	
  * [[GEOS-7243](https://osgeo-org.atlassian.net/browse/GEOS-7243)] - Render (or transform) fails on Multipolygon but not on polygon

	
  * [[GEOS-7256](https://osgeo-org.atlassian.net/browse/GEOS-7256)] - Maven Cobertura plugin does not work

	
  * [[GEOS-7259](https://osgeo-org.atlassian.net/browse/GEOS-7259)] - JMS based cluster should use qualified names for Layers and Layergroups

	
  * [[GEOS-7267](https://osgeo-org.atlassian.net/browse/GEOS-7267)] - JMS Clustering should prefix Styles names with workspace

	
  * [[GEOS-7295](https://osgeo-org.atlassian.net/browse/GEOS-7295)] - OpenLayers preview does not work if authkey community module is enabled

	
  * [[GEOS-7302](https://osgeo-org.atlassian.net/browse/GEOS-7302)] - Using on the fly meta tiling in WMS request may result in rendered images not being disposed of

	
  * [[GEOS-7312](https://osgeo-org.atlassian.net/browse/GEOS-7312)] - RawDataPPIO does not close InputStreams it opens

	
  * [[GEOS-7314](https://osgeo-org.atlassian.net/browse/GEOS-7314)] - GeoTiffPPIO can return the source file of a processed coverage




## Improvement





	
  * [[GEOS-4762](https://osgeo-org.atlassian.net/browse/GEOS-4762)] - WCS should force usage of imageread

	
  * [[GEOS-7150](https://osgeo-org.atlassian.net/browse/GEOS-7150)] - Features counted twice for WFS queries with GeoJSON responses


For a full list, see the [release notes](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=11601).

Also, as a heads up for Oracle users, the Oracle store does not ship anymore with the JDBC driver (due to redistribution limitations imposed by Oracle). For details see the updated the oracle installation instructions [here](http://docs.geoserver.org/stable/en/user/data/database/oracle.html#oracle-install).

Thanks to Alessio Fabiani (GeoSolutions) for this release.

This release is made in conjunction with [GeoTools 13.4](http://geotoolsnews.blogspot.it/2015/11/geotools-134-released.html) and [GeoNode 2.4](http://geonode.org/blog/2015/11/19/geonode-2.4-released/).
