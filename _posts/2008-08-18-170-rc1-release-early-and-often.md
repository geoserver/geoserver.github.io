---
author: bmmpxf
comments: true
date: 2008-08-18 15:33:38+00:00
layout: post
link: http://blog.geoserver.org/2008/08/18/170-rc1-release-early-and-often/
slug: 170-rc1-release-early-and-often
title: '1.7.0-RC1: Release Early And Often'
wordpress_id: 119
categories:
- Announcements
---

Our mantra around here is "release early and often" and we're certainly holding to that these days.  The GeoServer team is woking on three (yes, three) parallel tracks of GeoServer.  First, there is the [stable](https://web.archive.org/web/20080818/http://geoserver.org/display/GEOS/Stable) branch, currently at [1.6.4](https://web.archive.org/web/20080818/http://geoserver.org/display/GEOS/GeoServer+1.6.4), which is current recommended version for those who need rock-solid dependability and minimal fuss.  Last week, we [unveiled]({% post_url 2008-08-11-a-new-ui-is-dawning %}) the [first alpha of GeoServer 2.0](https://web.archive.org/web/20080818/http://geoserver.org/display/GEOS/GeoServer+2.0.0-alpha1), which brings a [new UI](https://web.archive.org/web/20080818/http://geoserver.org/display/GEOS/GSIP+23+-+Wicket+UI) and new customization options.

But today we're proud to unveil the first release candidate of GeoServer 1.7.0.  We have received plenty of feedback from users, and there has been a great deal of work done to bring this one out of beta.  This version provides many new features, such as [Xlink support for WFS 1.1](https://web.archive.org/web/20080818/http://geoserver.org/display/GEOS/WFS+1.1+XLink), full implementation of WCS 1.1.1, and per layer security.  I personally like the new OpenLayers toolbar, which allows for dynamic updating of the configuration options.  Special thanks goes out to [GeoSolutions](http://www.geo-solutions.it/) for all of their hard work on the [GDAL](http://www.gdal.org/) [extensions](https://web.archive.org/web/20080818/http://geoserver.org/display/GEOSDOC/ImageIO-ext+GDAL+extensions).

So please download 1.7.0-RC1 and give it a spin.  Over 30 bugs and features have been fixed and implemented (respectively) since our last beta.

----

#### GeoServer 1.7.0-RC1 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/).

Released on (DATE). SourceForge Release 619896

- [Release Notes](#release-notes)
- [geoserver-1.7.0-RC1.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/geoserver-1.7.0-RC1.exe/download) (Win32 self-installing executable)
- [geoserver-1.7.0-RC1-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/geoserver-1.7.0-RC1-bin.zip/download) (UNIX binary)
- [geoserver-1.7.0-RC1-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/geoserver-1.7.0-RC1-src.zip/download) (Source code)
- [geoserver-1.7.0-RC1-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/geoserver-1.7.0-RC1-war.zip/download) (Web archive)
- [geoserver-1.7.0-RC1-doc.zip](http://downloads.sourceforge.net/geoserver/geoserver-1.7.0-RC1-doc.zip) (Documentation export from geoserver.org)
- [geoserver-1.7.0-RC1-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/geoserver-1.7.0-RC1-javadoc.zip/download) (Java Documentation)

#### [Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/extensions/)

**DataStore Extensions**

- [GeoWebCache](http://downloads.sourceforge.net/geoserver/geoserver-1.7.0-RC1-gwc-plugin.zip)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/extensions/geoserver-1.7.0-RC1-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/extensions/geoserver-1.7.0-RC1-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/extensions/geoserver-1.7.0-RC1-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/extensions/geoserver-1.7.0-RC1-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/extensions/geoserver-1.7.0-RC1-vpf-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/extensions/geoserver-1.7.0-RC1-wfsv-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/extensions/geoserver-1.7.0-RC1-oracle-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/extensions/geoserver-1.7.0-RC1-h2-plugin.zip/download)

**Coverage Extensions**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/extensions/geoserver-1.7.0-RC1-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-RC1/extensions/geoserver-1.7.0-RC1-pyramid-plugin.zip/download)

## Release notes

Improvement:

* [GEOS-458](https://osgeo-org.atlassian.net/browse/GEOS-458) Have WMS capabilities document report contact information
* [GEOS-533](https://osgeo-org.atlassian.net/browse/GEOS-533) make FORMAT not mandatory for GetFeatureInfo
* [GEOS-1616](https://osgeo-org.atlassian.net/browse/GEOS-1616) WFS 1.0 GetFeature accepts srsName in GET requests, but ignores it in POST ones
* [GEOS-1707](https://osgeo-org.atlassian.net/browse/GEOS-1707) WFS 1.1.0 xml reader on trunk does not look at "strict" parameter
* [GEOS-2121](https://osgeo-org.atlassian.net/browse/GEOS-2121) Change of buffer size in ShapeZipOutputFormat

Bug:

* [GEOS-597](https://osgeo-org.atlassian.net/browse/GEOS-597) sql-injection
* [GEOS-1038](https://osgeo-org.atlassian.net/browse/GEOS-1038) New ArcSDE featuretypes aren't compatible with their default output
* [GEOS-1290](https://osgeo-org.atlassian.net/browse/GEOS-1290) time templates shoud by default understand dates produced by postgis
* [GEOS-1694](https://osgeo-org.atlassian.net/browse/GEOS-1694) Bridge to old style service API disregards content disposition
* [GEOS-1702](https://osgeo-org.atlassian.net/browse/GEOS-1702) KVPRequestReader throws exception when it should ignore the parameter
* [GEOS-1708](https://osgeo-org.atlassian.net/browse/GEOS-1708) NPE when making a WFS 1.0 GetFeature with a bbox but no property name
* [GEOS-1730](https://osgeo-org.atlassian.net/browse/GEOS-1730) enable kvp parsers to engage only on a particular service / version / request
* [GEOS-1834](https://osgeo-org.atlassian.net/browse/GEOS-1834) WCS 1.0 cite negotiation tests do pass only if WCS 1.1 module is not around
* [GEOS-1900](https://osgeo-org.atlassian.net/browse/GEOS-1900) NullPointerException evaluating between filter in an SLD
* [GEOS-1971](https://osgeo-org.atlassian.net/browse/GEOS-1971) "SRS List" link in FeatureType Edit form yields 404
* [GEOS-2001](https://osgeo-org.atlassian.net/browse/GEOS-2001) WellKnownNames aren't right in SLD
* [GEOS-2025](https://osgeo-org.atlassian.net/browse/GEOS-2025) Global max features not honored anymore on trunk
* [GEOS-2036](https://osgeo-org.atlassian.net/browse/GEOS-2036) WMS layer groups , max coordinates are garbage
* [GEOS-2045](https://osgeo-org.atlassian.net/browse/GEOS-2045) Geoserver does not start when installed on a path with spaces
* [GEOS-2051](https://osgeo-org.atlassian.net/browse/GEOS-2051) Caching configurations are not loaded anymore
* [GEOS-2054](https://osgeo-org.atlassian.net/browse/GEOS-2054) Wms Reflect not correctly reproiecting layer from srs=epsg:3003 to srs=epsg:4326
* [GEOS-2059](https://osgeo-org.atlassian.net/browse/GEOS-2059) WMS Reprojection does not work for postgis if geometries have no embedded srs
* [GEOS-2064](https://osgeo-org.atlassian.net/browse/GEOS-2064) Make GeoServer pass the official wfs 1.1 cite test suite
* [GEOS-2065](https://osgeo-org.atlassian.net/browse/GEOS-2065) Test passing by accident on the new WFS 1.1 test suite
* [GEOS-2068](https://osgeo-org.atlassian.net/browse/GEOS-2068) Fix WFS 1.1 xlink failures
* [GEOS-2073](https://osgeo-org.atlassian.net/browse/GEOS-2073) Failure to reproject bounding box in KML
* [GEOS-2078](https://osgeo-org.atlassian.net/browse/GEOS-2078) WMS reflector code is therad unsafe
* [GEOS-2125](https://osgeo-org.atlassian.net/browse/GEOS-2125) Exception on changing LayerGroup Configuration

Task:

* [GEOS-1548](https://osgeo-org.atlassian.net/browse/GEOS-1548) get story straight about urn style srsName
* [GEOS-1965](https://osgeo-org.atlassian.net/browse/GEOS-1965) Most "new configuration" files are missing license headers
* [GEOS-2015](https://osgeo-org.atlassian.net/browse/GEOS-2015) Crash on startup
* [GEOS-2107](https://osgeo-org.atlassian.net/browse/GEOS-2107) Setup packages and instructions to install imageio-ext extensions for GeoServer
* [GEOS-2122](https://osgeo-org.atlassian.net/browse/GEOS-2122) Remove H2 from default build
