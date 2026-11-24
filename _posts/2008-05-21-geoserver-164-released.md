---
author: bmmpxf
comments: false
date: 2008-05-21 17:53:02+00:00
layout: post
link: http://blog.geoserver.org/2008/05/21/geoserver-164-released/
slug: geoserver-164-released
title: GeoServer 1.6.4 Released
wordpress_id: 111
categories:
- Announcements
---

The GeoServer development team would like to announce the release of GeoServer 1.6.4.  Primarily a bugfix release, it contains over 30 [patches and improvements](#release-notes) since 1.6.3.   This version contains better support for the [GeoWebCache plugin](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6.4/geoserver-1.6.4-gwc-plugin.zip/download) (if you haven't checked out [GeoWebCache](https://geowebcache.osgeo.org/) you [very much should](http://google-opensource.blogspot.com/2008/05/accelerate-your-maps-with-geowebcache.html).)  There is now better default formatting of KML output, including including support for paging.  The Windows installer has been updated and now has better compatibility with Windows Vista.  Also, support for [Freemarker templates](http://freemarker.sourceforge.net/) for coverage layers has been added.

You can view the full [changelog](#release-notes) for more details.  Thanks to everyone who submitted patches!  Please keep them coming.  I've been hearing rumors about the features planned for future releases, so exciting developments look like they are coming down the line.  Stay tuned!  (Or better yet, [get involved](https://web.archive.org/web/20080521/http://geoserver.org/display/GEOSDOC/0.2+How+to+Help)!)

----

#### GeoServer 1.6.4 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.4/).

SourceForge Release ID: 600717

- [Release Notes](#release-notes)
- [geoserver-1.6.4b.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.4/geoserver-1.6.4b.exe/download) (Win32 self-installing executable)
- [geoserver-1.6.4b-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.4/geoserver-1.6.4b-bin.zip/download) (UNIX binary)
- [geoserver-1.6.4b-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.4/geoserver-1.6.4b-src.zip/download) (Source code)
- [geoserver-1.6.4b-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.4/geoserver-1.6.4b-war.zip/download) (Web archive)
- [geoserver-1.6.4b-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.4/geoserver-1.6.4b-doc.zip/download) (Documentation export from geoserver.org)
- [geoserver-1.6.4b-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.4/geoserver-1.6.4b-javadoc.zip/download) (Java Documentation)

#### [Extensions download page](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6.4/)

##### DataStore Extensions

- [GeoWebCache](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6.4/geoserver-1.6.4-gwc-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.4/extensions/geoserver-1.6.4-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.4/extensions/geoserver-1.6.4-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.4/extensions/geoserver-1.6.4-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.4/extensions/geoserver-1.6.4-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.4/extensions/geoserver-1.6.4-vpf-plugin.zip/download)
- [WFS](http://downloads.sourceforge.net/geoserver/geoserver-1.6.4-wfs-plugin.zip)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.4/extensions/geoserver-1.6.4-oracle-plugin.zip/download)

##### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.4/extensions/geoserver-1.6.4-pyramid-plugin.zip/download)

## Release notes

Improvement:

* [GEOS-1857](https://osgeo-org.atlassian.net/browse/GEOS-1857) Change project icons to match geoserver.org
* [GEOS-1858](https://osgeo-org.atlassian.net/browse/GEOS-1858) Better default formatting for KML
* [GEOS-1869](https://osgeo-org.atlassian.net/browse/GEOS-1869) Use Hints.JTS_COORDINATE_SEQUENCE_FACTORY un WFS GetFeature queries and CoordinateSequence in the encoder
* [GEOS-1874](https://osgeo-org.atlassian.net/browse/GEOS-1874) Switch all read only tests to a "one time setup" architecture
* [GEOS-1890](https://osgeo-org.atlassian.net/browse/GEOS-1890) GeoServer installation on Windows Vista yields error "This program may not have installed correctly"
* [GEOS-1891](https://osgeo-org.atlassian.net/browse/GEOS-1891) Add template support for coverage layers
* [GEOS-1904](https://osgeo-org.atlassian.net/browse/GEOS-1904) Dump data loading stack traces with a normal logging configuration, as it is now it makes error diagnosis just too hard
* [GEOS-1918](https://osgeo-org.atlassian.net/browse/GEOS-1918) Add a servlet filter that does the reverse proxy work in translating html and javascript urls to the proxy based ones
* [GEOS-1925](https://osgeo-org.atlassian.net/browse/GEOS-1925) PointSymbolizer on polygon features results in an icon at the edge of the polygon (should be inside)

Bug:

* [GEOS-1655](https://osgeo-org.atlassian.net/browse/GEOS-1655) Proxy base URL seems does not work as expected
* [GEOS-1829](https://osgeo-org.atlassian.net/browse/GEOS-1829) Spatial filters do not handle functions as second argument
* [GEOS-1855](https://osgeo-org.atlassian.net/browse/GEOS-1855) empty PNG8 images not transparent in IE6
* [GEOS-1856](https://osgeo-org.atlassian.net/browse/GEOS-1856) ConcurrentModificationException under heavy load in xml module configuration
* [GEOS-1860](https://osgeo-org.atlassian.net/browse/GEOS-1860) SLD filter reprojection introduction broke generic binary filter
* [GEOS-1863](https://osgeo-org.atlassian.net/browse/GEOS-1863) Multiple bbox computation issues in projected layers (both feature type info panel and preview)
* [GEOS-1864](https://osgeo-org.atlassian.net/browse/GEOS-1864) GetMapKvpRequestReader eats CRS decoding exceptions
* [GEOS-1866](https://osgeo-org.atlassian.net/browse/GEOS-1866) WFS getCapabilities link fails when feature type has no keywords configured
* [GEOS-1868](https://osgeo-org.atlassian.net/browse/GEOS-1868) org.vfny.geoserver.config.CoverageConfig causes memory overflow
* [GEOS-1873](https://osgeo-org.atlassian.net/browse/GEOS-1873) Problem adding new features using WFS-T
* [GEOS-1875](https://osgeo-org.atlassian.net/browse/GEOS-1875) WFS GetFeature NPE's instead of reporting the wrong layer name was chosen
* [GEOS-1878](https://osgeo-org.atlassian.net/browse/GEOS-1878) Attributes containing apostrophes fail on insert/update using WFS-T
* [GEOS-1886](https://osgeo-org.atlassian.net/browse/GEOS-1886) Deadlock with concurrent reprojecting WFS requests
* [GEOS-1892](https://osgeo-org.atlassian.net/browse/GEOS-1892) Labeling does not seem to continue to display once the feature symbology is told to go away.
* [GEOS-1908](https://osgeo-org.atlassian.net/browse/GEOS-1908) GeoServer Documentation link is broken on Windows installs
* [GEOS-1909](https://osgeo-org.atlassian.net/browse/GEOS-1909) CITE WFS 1.1 failure after prepared statement usage in postgis data store
* [GEOS-1915](https://osgeo-org.atlassian.net/browse/GEOS-1915) GeoServer NPE's when we try to configure a PostGIS table that's not registered in geometry_columns
* [GEOS-1917](https://osgeo-org.atlassian.net/browse/GEOS-1917) Configuration deployment plugin does not build anymore with maven 2.0.9
* [GEOS-1923](https://osgeo-org.atlassian.net/browse/GEOS-1923) CSV module gets built as part of release process
* [GEOS-1927](https://osgeo-org.atlassian.net/browse/GEOS-1927) Point placement ruined when previous polygon symbolizer is used
* [GEOS-1935](https://osgeo-org.atlassian.net/browse/GEOS-1935) Regression: GetFeatureInfo NPE's
* [GEOS-1937](https://osgeo-org.atlassian.net/browse/GEOS-1937) Trying to clean up the cache results in a NPE
* [GEOS-1939](https://osgeo-org.atlassian.net/browse/GEOS-1939) Sorting WFS 1.1.0 cite tests broken
* [GEOS-1940](https://osgeo-org.atlassian.net/browse/GEOS-1940) WCS capabilities do include invalid links (CITE failure)
* [GEOS-2242](https://osgeo-org.atlassian.net/browse/GEOS-2242) Geoserver doesn't parse the EU-Projection called WigeoEU (EPSG:40103), Error in parsing Parameter "central_parallel" was not expected.

Task:

* [GEOS-1898](https://osgeo-org.atlassian.net/browse/GEOS-1898) Backport paging support from trunk to 1.6.4

Sub-task:

* [GEOS-1870](https://osgeo-org.atlassian.net/browse/GEOS-1870) Update GeoJSON output format to use CoordinateSequence instead of Coordinate[]
* [GEOS-1871](https://osgeo-org.atlassian.net/browse/GEOS-1871) Update ShapeZipOutputFormat to use CoordinateSequence instead of Coordinate[]
