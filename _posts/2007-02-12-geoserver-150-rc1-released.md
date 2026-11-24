---
author: Brent Owens
comments: true
date: 2007-02-12 19:36:51+00:00
layout: post
link: http://blog.geoserver.org/2007/02/12/geoserver-150-rc1-released/
slug: geoserver-150-rc1-released
title: GeoServer 1.5.0-RC1 released
wordpress_id: 23
categories:
- Announcements
---

We have just released our first release candidate for the 1.5 series of GeoServer that you can download below. The main feature of 1.5 is support for 'raster' formats, like geotiff, arcgrid, gtopo30, and more.  These are accessible not just through the WMS, but there also through the new Web Coverage Service (WCS) interface.Â  In line with GeoServer's mission of making geospatial data more accessible, this allows access to the raw information of rasters, just as WFS does for vector formats.  The WCS is passing all OGC compliance tests, and we plan on getting it certified when we go to 1.5.0.  This release brings many fixes and improvements and it is also now backwards compatible to 1.3 and 1.4 data directories, so you do not have to port your data over to the new structure. Along with speed improvements, it also had a little reorganization of the user interface and has a couple tutorials to go along with it:




Since this is a release candidate, we would appreciate it if you could all download it and give it a quick try. Mostly for testing the backwards compatibility to old data directories, and for deployment in your existing systems to make sure there is no loss in functionality.


Along with this release are some coverage data assistance [tools](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/Coverage%20Tools%200.2/CoverageTools-0.2.exe/download) from Geo-Solutions. They will make your life of processing coverage data easier. It is in an early release stage so please report any bugs or problems back to us. We will be adding more documentation to it in the mean time.

----

The GeoServer 1.5.0-RC1 release is available for download from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC1/):

#### Docs

- [Task Tracker](#release-notes)
- [geoserver-1.4.0-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0/geoserver-1.4.0-doc.zip/download)
- [geoserver-1.4.0-RC3-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC3/geoserver-1.4.0-RC3-javadoc.zip/download)

#### Deployment

- [geoserver-1.5.0-RC1-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC1/geoserver-1.5.0-RC1-war.zip/download)
- [geoserver-1.5.0-RC1-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC1/geoserver-1.5.0-RC1-bin.zip/download)

#### Windows Installer

- [geoserver-1.5.0-RC1.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC1/geoserver-1.5.0-RC1.exe/download)

#### Source Code

- [geoserver-1.5.0-RC1-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC1/geoserver-1.5.0-RC1-src.zip/download)

#### DataStore Extensions

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0/extensions/)

- [ArcSDE datastore](http://prdownloads.sourceforge.net/geoserver/geoserver-1.4.0-arcsde-plugin.zip?download)
- [GML datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0/extensions/geoserver-1.4.0-gml-plugin.zip/download)
- [DB2 datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0/extensions/geoserver-1.4.0-db2-plugin.zip/download)
- [MySQL datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0/extensions/geoserver-1.4.0-mysql-plugin.zip/download)
- [VPF datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0/extensions/geoserver-1.4.0-vpf-plugin.zip/download)
- [WFS datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0/extensions/geoserver-1.4.0-wfs-plugin.zip/download)
- [Oracle datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0/extensions/geoserver-1.4.0-oracle-plugin.zip/download)

#### Extra Plugins and Tools

- Server-side [Caching](http://docs.codehaus.org/display/GEOSDOC/Caching). Especially useful for tiling clients such as OpenLayers or Google Maps.
- [Windows Service Wrapper](http://docs.codehaus.org/display/GEOSDOC/Windows+Service+Wrapper): Run GeoServer as a service.
- [Coverage Tools v0.2](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/Coverage%20Tools%200.2/CoverageTools-0.2.exe/download)

Tested with: JBoss, Jetty, Tomcat, WebLogic

GeoServer **[**License**](http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

New Feature:

* [GEOS-861](https://osgeo-org.atlassian.net/browse/GEOS-861) Bundle Simone's coverage tools with geoserver
* [GEOS-876](https://osgeo-org.atlassian.net/browse/GEOS-876) Release testing script

Improvement:

* [GEOS-860](https://osgeo-org.atlassian.net/browse/GEOS-860) Clean up UI
* [GEOS-872](https://osgeo-org.atlassian.net/browse/GEOS-872) Preview SLD in the style editor page
* [GEOS-878](https://osgeo-org.atlassian.net/browse/GEOS-878) Have a usable minimal configuration

Bug:

* [GEOS-838](https://osgeo-org.atlassian.net/browse/GEOS-838) GeoServer WMS and WFS should not require JAI to be installed
* [GEOS-853](https://osgeo-org.atlassian.net/browse/GEOS-853) Geoserver cannot handle files outside the data dir anymore
* [GEOS-859](https://osgeo-org.atlassian.net/browse/GEOS-859) Get it passing all CITE tests
* [GEOS-871](https://osgeo-org.atlassian.net/browse/GEOS-871) Map preview does not work with projected data, and shows distorted maps with unprojected ones
* [GEOS-873](https://osgeo-org.atlassian.net/browse/GEOS-873) Pre-release test to see if the package contains the latest EPSG database
* [GEOS-877](https://osgeo-org.atlassian.net/browse/GEOS-877) Geoserver 1.5.x must load 1.4.x data dirs without issues
* [GEOS-883](https://osgeo-org.atlassian.net/browse/GEOS-883) Scale computation does not conform to OGC standard
* [GEOS-893](https://osgeo-org.atlassian.net/browse/GEOS-893) Misconfigured datastore prevents geoserver startup

Task:

* [GEOS-707](https://osgeo-org.atlassian.net/browse/GEOS-707) Remove wicket jars from version control
* [GEOS-867](https://osgeo-org.atlassian.net/browse/GEOS-867) Slim down the size of GeoServer download
