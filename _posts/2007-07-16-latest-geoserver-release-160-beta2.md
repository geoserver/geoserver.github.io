---
author: Chris Holmes
comments: true
date: 2007-07-16 16:04:04+00:00
layout: post
link: http://blog.geoserver.org/2007/07/16/latest-geoserver-release-160-beta2/
slug: latest-geoserver-release-160-beta2
title: 'Latest GeoServer Release: 1.6.0-beta2'
wordpress_id: 60
categories:
- Announcements
---

The GeoServer Team is pleased to announce the latest 1.6.x release: 1.6.0-beta2.  We are hoping that our next release in this series will be a release candidate, so please help us out with testing as we work towards complete stability and reliability.  This release should actually be quite solid, but it's also got some major changes so we want another round of testing to be completely sure.

As for improvements, we've been making strides to allow GeoServer to play more nicely with Java Enterprise Edition containers.  The biggest is that we've swapped out our connection pool code to be more Java EE compliant, enabling the use of JNDI configurations (though we still lack a UI for it), and defaulting to [DBCP](http://jakarta.apache.org/commons/dbcp/).  This is a huge improvement over our old code, as it gives much more control over number of connections and can revalidate lost connections.   It also again points to the strength of the Java open source world, as we've gotten a huge improvement by just leveraging an existing library.

This release also includes better logging options, giving users settings for the logging levels and where the output goes.  Reprojection in WFS 1.1 is also working again, so GeoServer can now give you raw data reprojected on the fly.  Other improvements include integrated demos for Google Maps, Yahoo Maps and Virtual Earth, dateTimes are working again, and there are numerous small bug fixes.  The full log is on [our JIRA](#release-notes).

----

GeoServer 1.6.0-beta2 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/). SourceForge Release 523534

- [geoserver-1.6-beta2.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/geoserver-1.6-beta2.exe/download)
- [geoserver-1.6-beta2-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/geoserver-1.6-beta2-bin.zip/download)
- [geoserver-1.6-beta2-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/geoserver-1.6-beta2-src.zip/download)
- [geoserver-1.6-beta2-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/geoserver-1.6-beta2-war.zip/download)
- [geoserver-1.6.0-beta2-doc.zip](http://downloads.sourceforge.net/geoserver/geoserver-1.6-beta2-doc.zip)
- [geoserver-1.6-beta2-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/geoserver-1.6-beta2-javadoc.zip/download)

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/extensions/)

#### DataStore Extensions

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/extensions/geoserver-1.6-beta2-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/extensions/geoserver-1.6-beta2-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/extensions/geoserver-1.6-beta2-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/extensions/geoserver-1.6-beta2-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/extensions/geoserver-1.6-beta2-vpf-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/extensions/geoserver-1.6-beta2-wfs-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/extensions/geoserver-1.6-beta2-oracle-plugin.zip/download)

#### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.0-beta2/extensions/geoserver-1.6-beta2-pyramid-plugin.zip/download)

Tested with: Jetty, Tomcat

## Release notes

New Feature:

* [GEOS-778](https://osgeo-org.atlassian.net/browse/GEOS-778) GeoServer JDBC DataStore should be able to use external J2EE/JNDI Connection pools

Improvement:

* [GEOS-196](https://osgeo-org.atlassian.net/browse/GEOS-196) Add template system to getFeatureInfo
* [GEOS-1013](https://osgeo-org.atlassian.net/browse/GEOS-1013) Timestamp fields are encoded as simple dates
* [GEOS-1021](https://osgeo-org.atlassian.net/browse/GEOS-1021) Pipe all geoserver/geotools logging into commons-logging in geoserver
* [GEOS-1061](https://osgeo-org.atlassian.net/browse/GEOS-1061) Improvement for GeoServer Layer Grouping
* [GEOS-1156](https://osgeo-org.atlassian.net/browse/GEOS-1156) Add spearfish demo data set
* [GEOS-1165](https://osgeo-org.atlassian.net/browse/GEOS-1165) Bounding box is null (unknown) when geometry field isn't queried
* [GEOS-1173](https://osgeo-org.atlassian.net/browse/GEOS-1173) Make sure standard exception reports do contain all messages of nested exceptions
* [GEOS-1175](https://osgeo-org.atlassian.net/browse/GEOS-1175) Improve GetFeatureInfo output templates
* [GEOS-1182](https://osgeo-org.atlassian.net/browse/GEOS-1182) GetFeatureInfo is not able to handle layer groups
* [GEOS-1186](https://osgeo-org.atlassian.net/browse/GEOS-1186) Map preview does not work in cite strict compatibility mode
* [GEOS-1187](https://osgeo-org.atlassian.net/browse/GEOS-1187) GetFeatureInfo HTML and txt deletages are eating exceptions
* [GEOS-1188](https://osgeo-org.atlassian.net/browse/GEOS-1188) NullpointerException handling filters generated in GetFeatureInfo requests
* [GEOS-1193](https://osgeo-org.atlassian.net/browse/GEOS-1193) Service exception reporting is always verbose
* [GEOS-1194](https://osgeo-org.atlassian.net/browse/GEOS-1194) WMS DescribeFeatureType NPE's if the layer is not avaiable, instead of giving a good error message
* [GEOS-1195](https://osgeo-org.atlassian.net/browse/GEOS-1195) MetaTiler returns wrong tile when zoomin in on projected layers
* [GEOS-1200](https://osgeo-org.atlassian.net/browse/GEOS-1200) Google maps + GeoRSS demo

Bug:

* [GEOS-902](https://osgeo-org.atlassian.net/browse/GEOS-902) Grave performance regression in WMS performance on trunk
* [GEOS-971](https://osgeo-org.atlassian.net/browse/GEOS-971) Geoserver trunk cannot parse inline features anymore
* [GEOS-1022](https://osgeo-org.atlassian.net/browse/GEOS-1022) UI-based logfile control partially broken because of commons-logging functionality
* [GEOS-1107](https://osgeo-org.atlassian.net/browse/GEOS-1107) Improper handling of lost database connection
* [GEOS-1130](https://osgeo-org.atlassian.net/browse/GEOS-1130) Test the shapefile renderer for WMS
* [GEOS-1135](https://osgeo-org.atlassian.net/browse/GEOS-1135) Yahoo maps + GeoRSS demo
* [GEOS-1136](https://osgeo-org.atlassian.net/browse/GEOS-1136) Microsoft virtual earth + georss demo
* [GEOS-1144](https://osgeo-org.atlassian.net/browse/GEOS-1144) Confirm that Mapbuilder's WFS-T tools still work with geoserver 1.6
* [GEOS-1176](https://osgeo-org.atlassian.net/browse/GEOS-1176) WFS 1.1.0 : Wrong format for a xs:dateTime(PostGIS timeStamp) attribute
* [GEOS-1180](https://osgeo-org.atlassian.net/browse/GEOS-1180) Cache control headers aren't working anymore
* [GEOS-1190](https://osgeo-org.atlassian.net/browse/GEOS-1190) wms capabilities fails when no srid set in postgis
* [GEOS-1201](https://osgeo-org.atlassian.net/browse/GEOS-1201) html code don't validate for the OpenLayers preview generated
* [GEOS-1204](https://osgeo-org.atlassian.net/browse/GEOS-1204) Remove old filter usage from Geoserver code
* [GEOS-1205](https://osgeo-org.atlassian.net/browse/GEOS-1205) Data store list is not sorted, hard to find stuff inside of it...
* [GEOS-1206](https://osgeo-org.atlassian.net/browse/GEOS-1206) Target srs is not taken into consideration
* [GEOS-1208](https://osgeo-org.atlassian.net/browse/GEOS-1208) Geometries are not getting encoded anymore?
* [GEOS-1209](https://osgeo-org.atlassian.net/browse/GEOS-1209) min Idle param in PostGIS has slightly unexpected behavior
* [GEOS-1210](https://osgeo-org.atlassian.net/browse/GEOS-1210) Some log messages are not making it from the code to the logfiles with the commons-logging cutover
* [GEOS-1213](https://osgeo-org.atlassian.net/browse/GEOS-1213) WMS GetMap SLD=xxx parameter incorrectly parsed
* [GEOS-1214](https://osgeo-org.atlassian.net/browse/GEOS-1214) Inline feature parser does not take into account the CRS when parsing the feature type
* [GEOS-1216](https://osgeo-org.atlassian.net/browse/GEOS-1216) Have Logging config set Java Logger levels to mirror log4j configuration file

Sub-task:

* [GEOS-303](https://osgeo-org.atlassian.net/browse/GEOS-303) Reprojection in the WFS
