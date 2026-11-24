---
author: Chris Holmes
comments: true
date: 2007-09-18 19:59:48+00:00
layout: post
link: http://blog.geoserver.org/2007/09/18/geoserver-16-beta3/
slug: geoserver-16-beta3
title: GeoServer 1.6-beta3
wordpress_id: 70
categories:
- Announcements
---

The GeoServer Project is pleased to announce the release of the third beta of 1.6.0, now available for download.  The main focus of this release has been a number of performance improvements, done by Andrea Aime.  These center around the WMS, and can be seen most clearly on layers that do not have any labels.  Soon we should improve the labeling as well, so keep an eye, since GeoServer is getting legitimately _fast.  _Other improvements include fixes in reprojection in the WFS, with some of the WFS 1.1 work being backported to WFS 1.0.  This allows us to do things like digitize on top of Yahoo! Maps and save the points back to GeoServer, where it automatically puts it in the right projection for the dataset.  The final improvement for beta 3 is our GeoJSON implementation is now part of the standard distribution instead of a separate download.  I for one am excited about this, as it's about the only coding I've done in the past year.

Also, if you're attending [FOSS4G](http://www.foss4g2007.org/) then please find us, we love talking to people who are actually making use of GeoServer.  Many of us will be at [TOPP](http://topp.openplans.org)'s booth, and perhaps we will try to pull together a BOF or something.  And of course will be at the workshop and sessions on GeoServer.  See you there!

----

GeoServer 1.6-beta3 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/). SourceForge Release 540351

- [Release Notes](#release-notes)
- [geoserver-1.6-beta3.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/geoserver-1.6-beta3.exe/download)
- [geoserver-1.6-beta3-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/geoserver-1.6-beta3-bin.zip/download)
- [geoserver-1.6-beta3-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/geoserver-1.6-beta3-src.zip/download)
- [geoserver-1.6-beta3-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/geoserver-1.6-beta3-war.zip/download)
- [geoserver-1.6-beta3-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/extensions/geoserver-1.6-beta3-doc.zip/download)
- [geoserver-1.6-beta3-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/geoserver-1.6-beta3-javadoc.zip/download)

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/extensions/)

#### DataStore Extensions

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/extensions/geoserver-1.6-beta3-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/extensions/geoserver-1.6-beta3-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/extensions/geoserver-1.6-beta3-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/extensions/geoserver-1.6-beta3-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/extensions/geoserver-1.6-beta3-vpf-plugin.zip/download)
- [WFS](http://downloads.sourceforge.net/geoserver/geoserver-1.6-beta3-wfs-plugin.zip)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/extensions/geoserver-1.6-beta3-oracle-plugin.zip/download)

#### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta3/extensions/geoserver-1.6-beta3-pyramid-plugin.zip/download)

Tested with: Jetty, Tomcat

## Release notes

New Feature:

* [GEOS-1276](https://osgeo-org.atlassian.net/browse/GEOS-1276) Bring GeoJSON in to main distribution

Improvement:

* [GEOS-1185](https://osgeo-org.atlassian.net/browse/GEOS-1185) DescribeFeature fails if no namespace is declared
* [GEOS-1297](https://osgeo-org.atlassian.net/browse/GEOS-1297) Make GeoServer fly
* [GEOS-1312](https://osgeo-org.atlassian.net/browse/GEOS-1312) Bring back 1 bit rendering
* [GEOS-1323](https://osgeo-org.atlassian.net/browse/GEOS-1323) Make sure the admin link in the installer points to localhost not 127.0.0.1, improve the description of the demo
* [GEOS-1338](https://osgeo-org.atlassian.net/browse/GEOS-1338) Metatiler and pure RGB images (no alpha) generate striped output
* [GEOS-1341](https://osgeo-org.atlassian.net/browse/GEOS-1341) Using format_options=antialias:none against a 3-16 colors image results in an exception
* [GEOS-1343](https://osgeo-org.atlassian.net/browse/GEOS-1343) Bring WFS cascading in

Bug:

* [GEOS-1304](https://osgeo-org.atlassian.net/browse/GEOS-1304) srsName specified in wfs getfeature request ignored
* [GEOS-1307](https://osgeo-org.atlassian.net/browse/GEOS-1307) Figure out the palette from the style when not using antialiasing, and use minimal colors (2, 4, 16 or 256 depending on the number used in the styles)
* [GEOS-1310](https://osgeo-org.atlassian.net/browse/GEOS-1310) Make sure default styles are fast and look good even when non antialiased
* [GEOS-1311](https://osgeo-org.atlassian.net/browse/GEOS-1311) MultiPolygons not properly mapped to MultiSurface in java 6
* [GEOS-1321](https://osgeo-org.atlassian.net/browse/GEOS-1321) GetFeature OOM's with WFS 1.1 and big data sets
* [GEOS-1329](https://osgeo-org.atlassian.net/browse/GEOS-1329) Don't use image transaparency unless required by the user
* [GEOS-1332](https://osgeo-org.atlassian.net/browse/GEOS-1332) kvp bounding box parsing ignores srs
* [GEOS-1333](https://osgeo-org.atlassian.net/browse/GEOS-1333) Allow queries and inserts using CRS other than the native one
* [GEOS-1335](https://osgeo-org.atlassian.net/browse/GEOS-1335) class cast exception when going to admin/index.do
