---
author: geoserver
comments: true
date: 2015-07-24 07:32:17+00:00
layout: post
link: http://blog.geoserver.org/2015/07/24/geoserver-2-7-2-released/
slug: geoserver-2-7-2-released
title: GeoServer 2.7.2 released
wordpress_id: 2282
categories:
- Announcements
---

The GeoServer team is happy to announce the release of [GeoServer 2.7.2](http://geoserver.org/release/2.7.2/). Download bundles are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.2/geoserver-2.7.2-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.2/geoserver-2.7.2-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.2/geoserver-2.7.2.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7.2/geoserver-2.7.2.exe/download))  along with documentation and extensions.

GeoServer 2.7.2 is a stable release of GeoServer recommended for production deployment. Thanks to everyone taking part, submitting fixes and new functionality including:



	
  * Importer raster improvements, added support for GDAL based file optimization when importing rasters, also, it is now possible to add add granules to a mosaic (and optimize them with GDAL in the process)

	
  * Importer vector improvements, now one can import data into non JDBC data stores too

	
  * Some improvements in the documentation on using GDAL based data sources in Windows

	
  * More tweaks on the XXE vulnerability fixes (we left it open just enough not to break OGC compliance)

	
  * Properly rendering GeoTiff files with flipped Y axis

	
  * Making sure WPS really stops answering requests when not enabled

	
  * Improvements in NetCDF handling of reprojected requests

	
  * For a full list, see the [release notes](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=10601).


Also, as a heads up for Oracle users, the Oracle store does not ship anymore with the JDBC driver (due to redistribution limitations imposed by Oracle). For details see the updated the oracle installation instructions [here](http://docs.geoserver.org/stable/en/user/data/database/oracle.html#oracle-install).

Thanks to Andrea (GeoSolutions) and Kevin (Boundless) for this release.
