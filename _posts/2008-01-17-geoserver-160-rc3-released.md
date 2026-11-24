---
author: Justin Deoliveira
comments: true
date: 2008-01-17 18:24:56+00:00
layout: post
link: http://blog.geoserver.org/2008/01/17/geoserver-160-rc3-released/
slug: geoserver-160-rc3-released
title: GeoServer 1.6.0-RC3 Released!
wordpress_id: 83
categories:
- Announcements
---

We are happy to announce the third release candidate for 1.6.0. You can grab it from [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/).

That coveted 1.6.0 release is getting closer and closer and we are almost there. The previous release candidate brought out some performance related issues.  A memory leak issue and a problem with filter parsing leading to stack overflows. These have been fixed along with some other minor bugs addressed as well. For a complete list of all the good stuff check out the [changelog](#release-notes).

Special thanks to everyone who tried out RC2 and reported issues. You can continue to help us get the official 1.6.0 release out by trying out this release candidate and reporting any issues in the [bug tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS).

----

GeoServer 1.6.0-RC3 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/). SourceForge Release 569264

- [Release Notes](#release-notes)
- [geoserver-1.6.0-RC3.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/geoserver-1.6.0-RC3.exe/download)
- [geoserver-1.6.0-RC3-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/geoserver-1.6.0-RC3-bin.zip/download)
- [geoserver-1.6.0-RC3-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/geoserver-1.6.0-RC3-src.zip/download)
- [geoserver-1.6.0-RC3-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/geoserver-1.6.0-RC3-war.zip/download)
- [geoserver-1.6.0-RC3-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/geoserver-1.6.0-RC3-doc.zip/download)
- [geoserver-1.6.0-RC3-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/geoserver-1.6.0-RC3-javadoc.zip/download)

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/extensions/)

#### WFS Extensions

- [Versioning WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/extensions/geoserver-1.6.0-RC3-wfsv-plugin.zip/download)

#### DataStore Extensions

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/extensions/geoserver-1.6.0a-RC3-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/extensions/geoserver-1.6.0-RC3-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/extensions/geoserver-1.6.0-RC3-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/extensions/geoserver-1.6.0-RC3-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/extensions/geoserver-1.6.0-RC3-vpf-plugin.zip/download)
- [WFS](http://downloads.sourceforge.net/geoserver/geoserver-1.6.0-RC3-wfs-plugin.zip)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/extensions/geoserver-1.6.0-RC3-oracle-plugin.zip/download)

#### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-RC3/extensions/geoserver-1.6.0-RC3-pyramid-plugin.zip/download)

Tested with: Jetty, Tomcat

## Release notes

Improvement:

* [GEOS-1663](https://osgeo-org.atlassian.net/browse/GEOS-1663) Try harder not to report "client closed socket" stack traces

Bug:

* [GEOS-1492](https://osgeo-org.atlassian.net/browse/GEOS-1492) Attempting to create FeatureType causes NoSuchFieldError exception
* [GEOS-1643](https://osgeo-org.atlassian.net/browse/GEOS-1643) GeoServer 1.6.0-rc2 wont' start on Glassfish due to an issue in web.xml
* [GEOS-1654](https://osgeo-org.atlassian.net/browse/GEOS-1654) Don't double-load when hitting the "apply" button
* [GEOS-1656](https://osgeo-org.atlassian.net/browse/GEOS-1656) NPE thrown when pointing shapefile datastore configuration to a non existing path
* [GEOS-1667](https://osgeo-org.atlassian.net/browse/GEOS-1667) All geometric filter return a blank image on wms + shapefiles + geoserver 1.6.x
* [GEOS-1668](https://osgeo-org.atlassian.net/browse/GEOS-1668) Memory leak in WMS response handling
* [GEOS-1669](https://osgeo-org.atlassian.net/browse/GEOS-1669) Exception reports by mistake n times the same message instead of using the messages got from the stack trace
* [GEOS-1674](https://osgeo-org.atlassian.net/browse/GEOS-1674) FeatureType configuration panel allows to enter -1 as the srs and submit
* [GEOS-1675](https://osgeo-org.atlassian.net/browse/GEOS-1675) query filter gives no results and throws a StackOverflowError if filter has too many features.
* [GEOS-1678](https://osgeo-org.atlassian.net/browse/GEOS-1678) admin page contains freudian slip: GeoSever

Task:

* [GEOS-1639](https://osgeo-org.atlassian.net/browse/GEOS-1639) Turn versioning datastore into an extension
* [GEOS-1648](https://osgeo-org.atlassian.net/browse/GEOS-1648) add jsqlparser.jar to the ArcSDE extension dependencies for download
