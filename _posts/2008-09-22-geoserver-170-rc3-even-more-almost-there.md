---
author: bmmpxf
comments: true
date: 2008-09-22 20:50:02+00:00
layout: post
link: http://blog.geoserver.org/2008/09/22/geoserver-170-rc3-even-more-almost-there/
slug: geoserver-170-rc3-even-more-almost-there
title: 'GeoServer 1.7.0-RC3: Even More Almost There'
wordpress_id: 133
---

We seem to be releasing something every week now, a testament to our tireless developers and input of the community.  Last week, we released [1.6.5](https://web.archive.org/web/20080922/http://geoserver.org/display/GEOS/GeoServer+1.6.5), which is still the official stable release at the time of writing.  However, we are closer than ever to a stable release of the 1.7.0 branch, and today we release the third release candidate of 1.7.0 to the wider world.  Among others, there were two pernicious bugs that caused FeatureTypes and coverages to disappear in certain circumstances.  (Yikes!)  No more, though.  In total, there are [19 bug fixes](#release-notes) in since RC2, and as usual, we encourage you to test out the latest version.  Will the fourth release candidate be the charm?  Stay tuned.

----

#### GeoServer 1.7.0-RC3 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/).

Released on (DATE). SourceForge Release 627487

- [Release Notes](#release-notes)
- [geoserver-1.7.0-RC3.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/geoserver-1.7.0-RC3.exe/download) (Win32 self-installing executable)
- [geoserver-1.7.0-RC3-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/geoserver-1.7.0-RC3-bin.zip/download) (UNIX binary)
- [geoserver-1.7.0-RC3-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/geoserver-1.7.0-RC3-src.zip/download) (Source code)
- [geoserver-1.7.0-RC3-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/geoserver-1.7.0-RC3-war.zip/download) (Web archive)

#### [Extensions download page](https://sourceforge.net/projects/geoserver/files/OldFiles/1.7.0/)

**DataStore Extensions**

- [GeoWebCache](https://sourceforge.net/projects/geoserver/files/OldFiles/1.7.0/geoserver-1.7.0-RC3-gwc-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/extensions/geoserver-1.7.0-RC3-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/extensions/geoserver-1.7.0-RC3-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/extensions/geoserver-1.7.0-RC3-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/extensions/geoserver-1.7.0-RC3-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/extensions/geoserver-1.7.0-RC3-vpf-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/extensions/geoserver-1.7.0-RC3-wfsv-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/extensions/geoserver-1.7.0-RC3-oracle-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/extensions/geoserver-1.7.0-RC3-h2-plugin.zip/download)

**Coverage Extensions**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/extensions/geoserver-1.7.0-RC3-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC3/extensions/geoserver-1.7.0-RC3-pyramid-plugin.zip/download)

## Release notes

Improvement:

* [GEOS-2216](https://osgeo-org.atlassian.net/browse/GEOS-2216) PropertyFileWatcher overzealously checks for file changes limiting scalability
* [GEOS-2220](https://osgeo-org.atlassian.net/browse/GEOS-2220) Dispatcher generates charset releated exceptions due to lack of null checks
* [GEOS-2230](https://osgeo-org.atlassian.net/browse/GEOS-2230) GetFeature WFS 1.0 does an undeeded count query most of the times

Bug:

* [GEOS-2187](https://osgeo-org.atlassian.net/browse/GEOS-2187) the link to openlayers in the home of geoserver it is mistaken
* [GEOS-2188](https://osgeo-org.atlassian.net/browse/GEOS-2188) All raster layers in WMS capabalities have the same description
* [GEOS-2191](https://osgeo-org.atlassian.net/browse/GEOS-2191) wfs 1.1 describe feature type uses wrong base url for schemas
* [GEOS-2194](https://osgeo-org.atlassian.net/browse/GEOS-2194) KML shapefile rendering
* [GEOS-2197](https://osgeo-org.atlassian.net/browse/GEOS-2197) Erro creating new coverage
* [GEOS-2202](https://osgeo-org.atlassian.net/browse/GEOS-2202) WMS reprojection requires Bulsa-Wolf parameters to be specified
* [GEOS-2203](https://osgeo-org.atlassian.net/browse/GEOS-2203) Configuration drops feature types is the datastore cannot connect
* [GEOS-2206](https://osgeo-org.atlassian.net/browse/GEOS-2206) set ServiceProvider information in wfs 1.1 capabilities document from server configuration
* [GEOS-2208](https://osgeo-org.atlassian.net/browse/GEOS-2208) GeoServer 1.7.x can randomly eat the data dir
* [GEOS-2212](https://osgeo-org.atlassian.net/browse/GEOS-2212) Rollback fails on large datasets, even with as few as 20 revisions.
* [GEOS-2215](https://osgeo-org.atlassian.net/browse/GEOS-2215) Configuration loading NPE's if the datastore cannot be loaded
* [GEOS-2218](https://osgeo-org.atlassian.net/browse/GEOS-2218) OWSUtils.getter fails to locate getters
* [GEOS-2221](https://osgeo-org.atlassian.net/browse/GEOS-2221) OWSUtils application generates sizeable amount of heap garbage
* [GEOS-2226](https://osgeo-org.atlassian.net/browse/GEOS-2226) Intersection filter doesn't return results
* [GEOS-2240](https://osgeo-org.atlassian.net/browse/GEOS-2240) GetCapabilities response contains duplicate layers
* [GEOS-2241](https://osgeo-org.atlassian.net/browse/GEOS-2241) wms path does not survive save / load cycle
