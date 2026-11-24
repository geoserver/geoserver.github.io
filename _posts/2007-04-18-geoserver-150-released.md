---
author: Justin Deoliveira
comments: true
date: 2007-04-18 18:01:48+00:00
layout: post
link: http://blog.geoserver.org/2007/04/18/geoserver-150-released/
slug: geoserver-150-released
title: GeoServer 1.5.0 Released
wordpress_id: 32
categories:
- Announcements
---

The GeoServer Project is proud to announce the release of version 1.5.0.  This release turns GeoServer in to a complete solution for serving any type of spatial data, as the primary focus has been support for raster formats, starting with GeoTiff, ArcGrid, World Images, GTOPO30, and image mosiacs and pyramids.  As always GeoServer is focused on open standards and open data, making the rasters available as a Web Map Service, but also through the Web Coverage Service specification, which gives full access to the raw data, not just the final image.  The WCS passes all OGC Compliance tests, and will be fully certified very soon.  Other notable improvements for this release include easier adding of data through the web admin tools, better support for Google Earth KML, performance and scalability improvements, and as always a heap of bug fixes. The release can be found below.

The Web Coverage Service implementation and WMS raster support have been the result of work carried out by [GeoSolutions](http://www.geo-solutions.it), who have been a prominent member of the GeoServer community for some time. The community is glad to take this contribution and make it part of the GeoServer core and thanks GeoSolutions for their excellent work. It is amazing to see not just bug fixes and new data formats, but completely new functionality that would not be possible without the ever expanding community.

This is an exciting time for GeoServer. As we look to the future there are more interesting developments on the horizon. Among them include Versioning WFS, a full implementation of WFS 1.1, multi-dimensional raster data through the WCS, and support for security and authentication. Also expect to keep seeing improvements to performance and scalability, better support for KML, and a variety of other neat and interesting features.

----

GeoServer 1.5.0 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0/). SourceForge Release 500964

- [geoserver-1.5.0.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0/geoserver-1.5.0.exe/download)
- [geoserver-1.5.0-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0/geoserver-1.5.0-bin.zip/download)
- [geoserver-1.5.0-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0/geoserver-1.5.0-src.zip/download)
- [geoserver-1.5.0-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0/geoserver-1.5.0-war.zip/download)
- [geoserver-1.5.0-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0/geoserver-1.5.0-doc.zip/download)
- [geoserver-1.5.0-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0/geoserver-1.5.0-javadoc.zip/download)

Tested with: Jetty, Tomcat

### Extensions

[Extensions download page](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0/)

##### DataStore Extensions

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0/geoserver-1.5.0-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0/geoserver-1.5.0-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0/geoserver-1.5.0-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0/geoserver-1.5.0-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0/geoserver-1.5.0-vpf-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0/geoserver-1.5.0-wfs-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0/geoserver-1.5.0-oracle-plugin.zip/download)

##### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/OldFiles/1.5.0/geoserver-1.5.0-pyramid-plugin.zip/download)

## Release notes

New Feature:

* [GEOS-862](https://osgeo-org.atlassian.net/browse/GEOS-862) Create several WCS tutorials

Improvement:

* [GEOS-833](https://osgeo-org.atlassian.net/browse/GEOS-833) SLD editor should at least show the current SLD
* [GEOS-848](https://osgeo-org.atlassian.net/browse/GEOS-848) Reverse engineer the proper SRS from data when possible
* [GEOS-852](https://osgeo-org.atlassian.net/browse/GEOS-852) Make it so Geoserver can configure the JAI tile cache in a sensible manner
* [GEOS-864](https://osgeo-org.atlassian.net/browse/GEOS-864) GetStyles and PutStyles are not included in the capabilities document
* [GEOS-895](https://osgeo-org.atlassian.net/browse/GEOS-895) Have geoserver use the native CRS, is available

Bug:

* [GEOS-765](https://osgeo-org.atlassian.net/browse/GEOS-765) "Unable to get resolution" during a getMap request
* [GEOS-846](https://osgeo-org.atlassian.net/browse/GEOS-846) BasicFidMapper generated keys are not valid FIDs
* [GEOS-853](https://osgeo-org.atlassian.net/browse/GEOS-853) Geoserver cannot handle files outside the data dir anymore
* [GEOS-894](https://osgeo-org.atlassian.net/browse/GEOS-894) Data without native CRS cannot be reprojected

Task:

* [GEOS-868](https://osgeo-org.atlassian.net/browse/GEOS-868) Create WCS/Coverage docs
* [GEOS-964](https://osgeo-org.atlassian.net/browse/GEOS-964) Documentation for Apache/Tomcat Link & GeoServer Tomcat Installation
* [GEOS-1010](https://osgeo-org.atlassian.net/browse/GEOS-1010) update german translation
