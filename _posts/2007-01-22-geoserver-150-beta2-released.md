---
author: Brent Owens
comments: true
date: 2007-01-22 18:02:04+00:00
layout: post
link: http://blog.geoserver.org/2007/01/22/geoserver-150-beta2-released/
slug: geoserver-150-beta2-released
title: GeoServer 1.5.0-beta2 released
wordpress_id: 19
categories:
- Announcements
---

We have released our second beta version of GeoServer 1.5.0. It contains many bug fixes and improvements. You can find the download below. Another useful feature it has is the ability to add coverages outside of your data directory.




Our next round of releases before the official 1.5.0 release are going to contain several larger changes that should clean up the UI and also introduce a suite of useful coverage tools, such as a Pyramid Builder and an Image Mosaic tool. This beta release will help us figure out what users want and need for the official release. So please try it out and give us lots of feedback either on our mailing list or on this blog.

----

The GeoServer 1.5.0-beta2 beta release is available for download from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-beta2/):\
Thanks to the [Geo-Solutions](http://www.geo-solutions.it) team for putting all their hard work into this release.\
This release sports various improvements in the WCS service and in coverage handling in general.\
Moreover the Oracle datastore provides much better performance than in the past (up to 4 times faster), check it out.

***Notice***: You will need **JAI** and **ImageIO** installed in your JRE in order to run this version of GeoServer. Future versions will contain the jars bundled with the download, and you will not need to manually install them.

#### Docs

- [geoserver-1.5.0-beta2-javadoc.zip](http://prdownloads.sourceforge.net/geoserver/geoserver-1.5.0-beta1-javadoc.zip?download)
- [Task Tracker](#release-notes)

#### Deployment

- [geoserver-1.5.0-beta2-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-beta2/geoserver-1.5.0-beta2-war.zip/download)
- [geoserver-1.5.0-beta2-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-beta2/geoserver-1.5.0-beta2-bin.zip/download)

#### Windows Installer

- [geoserver-1.5.0-beta2.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-beta2/geoserver-1.5.0-beta2.exe/download)

#### Source Code

- [geoserver-1.5.0-beta2-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-beta2/geoserver-1.5.0-beta2-src.zip/download)

#### DataStore Extensions

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-beta2/extensions/)

- [GML datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-beta2/extensions/geoserver-1.5.0-beta2-gml-plugin.zip/download)
- [DB2 datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-beta2/extensions/geoserver-1.5.0-beta2-db2-plugin.zip/download)
- [MySQL datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-beta2/extensions/geoserver-1.5.0-beta2-mysql-plugin.zip/download)
- [VPF datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-beta2/extensions/geoserver-1.5.0-beta2-vpf-plugin.zip/download)
- [WFS datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-beta2/extensions/geoserver-1.5.0-beta2-wfs-plugin.zip/download)
- [Oracle datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-beta2/extensions/geoserver-1.5.0-beta2-oracle-plugin.zip/download)

#### Extra Plugins

- Server-side [Caching](http://docs.codehaus.org/display/GEOSDOC/Caching). Especially useful for tiling clients such as OpenLayers or Google Maps.
- [Windows Service Wrapper](http://docs.codehaus.org/display/GEOSDOC/Windows+Service+Wrapper): Run GeoServer as a service.

Tested with: JBoss, Jetty, Tomcat, WebLogic

GeoServer **[License](http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

Improvement:

* [GEOS-791](https://osgeo-org.atlassian.net/browse/GEOS-791) Add coverages to the Map Preview page
* [GEOS-840](https://osgeo-org.atlassian.net/browse/GEOS-840) Add a buffer parameter to wms requests, so that soft information about the best meta-buffer can be provided by the user

Bug:

* [GEOS-746](https://osgeo-org.atlassian.net/browse/GEOS-746) CoverageStores should allow for data urls outside geoserver_data_dir, like FeatureStores do
* [GEOS-820](https://osgeo-org.atlassian.net/browse/GEOS-820) GML 2.1.2 schemas don't validate in Xerces
* [GEOS-823](https://osgeo-org.atlassian.net/browse/GEOS-823) License.txt and gpl.txt missing from 1.5 release files
* [GEOS-855](https://osgeo-org.atlassian.net/browse/GEOS-855) BaseMap layers overwrite other layers as well
