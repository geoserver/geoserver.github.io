---
author: Chris Holmes
comments: true
date: 2007-08-07 20:51:05+00:00
layout: post
link: http://blog.geoserver.org/2007/08/07/help-us-test-geoserver-152/
slug: help-us-test-geoserver-152
title: Help us test GeoServer 1.5.2
wordpress_id: 64
categories:
- Announcements
---

So we were hoping to do a big announcement of GeoServer 1.5.2 today.  But our ambitious bug fixes and improvements (over [80 issues](#release-notes)) has come back to haunt us, and taught us an important lesson about doing release candidates first, even if 1.5.2-RC1 doesn't sound great to our ears.  We squeezed in lots of [Google Earth output](https://web.archive.org/web/20070807/http://docs.codehaus.org/display/GEOSDOC/Google+Earth) improvements, added [GeoRSS](https://web.archive.org/web/20070807/http://docs.codehaus.org/display/GEOSDOC/GeoRSS), improved the Google Maps demo with a [better](http://crschmidt.net/blog/archives/238/understanding-googles-projection-slightly-anyway/) [projection](http://crschmidt.net/blog/archives/243/google-projection-900913/), and added [paletted images](https://web.archive.org/web/20070807/http://docs.codehaus.org/display/GEOSDOC/Paletted+images+tutorial) for faster and lighter image generation.  And of course those have been where we've seen a few problems.  We've uploaded the release to sourceforge, but users have already reported a few small errors with GeoRSS and Google Maps, so we're regrouping and hoping to gather any additional bug reports and do the big release announcements next week.

So in the meantime, dear readers, you can help us out a ton by downloading the latest release, testing it out and reporting any errors that you might encounter.  The issues that we know about for this release are available [here](#release-notes), if you have one of these issues and its resolved you can try out the [nightly build](https://web.archive.org/web/20070807/http://geo.openplans.org/nightly/1.5.x) to test our fix.  If the issue is not yet resolved then rest assured it will be soon.  So please help us out, and watch for the big 1.5.2 announcement next week.  Thanks for all your support!

----

GeoServer 1.5.2 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/). SourceForge Release 529565

- [Release Notes](#release-notes)
- [geoserver-1.5.2.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/geoserver-1.5.2.exe/download)
- [geoserver-1.5.2-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/geoserver-1.5.2-bin.zip/download)
- [geoserver-1.5.2-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/geoserver-1.5.2-src.zip/download)
- [geoserver-1.5.2-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/geoserver-1.5.2-war.zip/download)
- [geoserver-1.5.2-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/geoserver-1.5.2-doc.zip/download)
- [geoserver-1.5.2-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/geoserver-1.5.2-javadoc.zip/download)

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/extensions/)

#### DataStore Extensions

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/extensions/geoserver-1.5.2-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/extensions/geoserver-1.5.2-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/extensions/geoserver-1.5.2-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/extensions/geoserver-1.5.2-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/extensions/geoserver-1.5.2-vpf-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/extensions/geoserver-1.5.2-wfs-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/extensions/geoserver-1.5.2-oracle-plugin.zip/download)

#### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.2/extensions/geoserver-1.5.2-pyramid-plugin.zip/download)

Tested with: Jetty, Tomcat

## Release notes

New Feature:

* [GEOS-1053](https://osgeo-org.atlassian.net/browse/GEOS-1053) GeoRSS support

Improvement:

* [GEOS-196](https://osgeo-org.atlassian.net/browse/GEOS-196) Add template system to getFeatureInfo
* [GEOS-908](https://osgeo-org.atlassian.net/browse/GEOS-908) add optional ogc:Filter to kml_reflect-or
* [GEOS-963](https://osgeo-org.atlassian.net/browse/GEOS-963) custom description in KML-output
* [GEOS-994](https://osgeo-org.atlassian.net/browse/GEOS-994) Better labels on lines in KML
* [GEOS-1061](https://osgeo-org.atlassian.net/browse/GEOS-1061) Improvement for GeoServer Layer Grouping
* [GEOS-1102](https://osgeo-org.atlassian.net/browse/GEOS-1102) Find a way to have 256 color images and antialiasing at the same time
* [GEOS-1104](https://osgeo-org.atlassian.net/browse/GEOS-1104) Add syntax highlighting to SLD editor page
* [GEOS-1105](https://osgeo-org.atlassian.net/browse/GEOS-1105) Sorts featureTypes Collection before the Capabilities is generated.
* [GEOS-1141](https://osgeo-org.atlassian.net/browse/GEOS-1141) improve kml / georss titles
* [GEOS-1150](https://osgeo-org.atlassian.net/browse/GEOS-1150) Investigate removing extra 'document'
* [GEOS-1151](https://osgeo-org.atlassian.net/browse/GEOS-1151) Better name than GeoServer for root KML Document (and maybe kml reflect)
* [GEOS-1154](https://osgeo-org.atlassian.net/browse/GEOS-1154) make kml pretty
* [GEOS-1156](https://osgeo-org.atlassian.net/browse/GEOS-1156) Add spearfish demo data set
* [GEOS-1165](https://osgeo-org.atlassian.net/browse/GEOS-1165) Bounding box is null (unknown) when geometry field isn't queried
* [GEOS-1172](https://osgeo-org.atlassian.net/browse/GEOS-1172) Have Geoserver serve static files included in the data dir
* [GEOS-1173](https://osgeo-org.atlassian.net/browse/GEOS-1173) Make sure standard exception reports do contain all messages of nested exceptions
* [GEOS-1174](https://osgeo-org.atlassian.net/browse/GEOS-1174) Make sure proper charset encoding is used reading xml config files as well as when publishing files with FilePublisher
* [GEOS-1175](https://osgeo-org.atlassian.net/browse/GEOS-1175) Improve GetFeatureInfo output templates
* [GEOS-1177](https://osgeo-org.atlassian.net/browse/GEOS-1177) Edit feature type, no lat/lon bbox available?
* [GEOS-1178](https://osgeo-org.atlassian.net/browse/GEOS-1178) RSS and KML output very slow on layers with lots of features
* [GEOS-1179](https://osgeo-org.atlassian.net/browse/GEOS-1179) Template loader is not able to distinguish between two feature types with the same name (but different namespace)
* [GEOS-1182](https://osgeo-org.atlassian.net/browse/GEOS-1182) GetFeatureInfo is not able to handle layer groups
* [GEOS-1187](https://osgeo-org.atlassian.net/browse/GEOS-1187) GetFeatureInfo HTML and txt deletages are eating exceptions
* [GEOS-1194](https://osgeo-org.atlassian.net/browse/GEOS-1194) WMS DescribeFeatureType NPE's if the layer is not avaiable, instead of giving a good error message
* [GEOS-1195](https://osgeo-org.atlassian.net/browse/GEOS-1195) MetaTiler returns wrong tile when zoomin in on projected layers
* [GEOS-1196](https://osgeo-org.atlassian.net/browse/GEOS-1196) KML generating from Oracle Datastore failes if source SRS is NULL
* [GEOS-1200](https://osgeo-org.atlassian.net/browse/GEOS-1200) Google maps + GeoRSS demo
* [GEOS-1225](https://osgeo-org.atlassian.net/browse/GEOS-1225) Change KML reflectors defaults
* [GEOS-1245](https://osgeo-org.atlassian.net/browse/GEOS-1245) Put asKML link on the OpenLayers Preview Pages
* [GEOS-1246](https://osgeo-org.atlassian.net/browse/GEOS-1246) Set `<scale>` param for KML icons to 0.20
* [GEOS-1251](https://osgeo-org.atlassian.net/browse/GEOS-1251) Templates for Time in KML
* [GEOS-1266](https://osgeo-org.atlassian.net/browse/GEOS-1266) Make it so the preview page shows formats other than openlayers
* [GEOS-1267](https://osgeo-org.atlassian.net/browse/GEOS-1267) Investigate better mercator projection for google maps

Bug:

* [GEOS-953](https://osgeo-org.atlassian.net/browse/GEOS-953) Namespace ignored in WFS gml for feature member name from oracle sources.
* [GEOS-1042](https://osgeo-org.atlassian.net/browse/GEOS-1042) Sample usa-population request with jpeg output format swaps colors
* [GEOS-1058](https://osgeo-org.atlassian.net/browse/GEOS-1058) template loading relative to feature type does not work when feature type config dir not != name of feature type
* [GEOS-1080](https://osgeo-org.atlassian.net/browse/GEOS-1080) KML Multiple Points
* [GEOS-1081](https://osgeo-org.atlassian.net/browse/GEOS-1081) kmattr and kmscore do not make it past the kml reflector
* [GEOS-1087](https://osgeo-org.atlassian.net/browse/GEOS-1087) Make it so that the source release is buildable
* [GEOS-1124](https://osgeo-org.atlassian.net/browse/GEOS-1124) Geometry type ignored/not recognized by Oracle datastore
* [GEOS-1126](https://osgeo-org.atlassian.net/browse/GEOS-1126) Have a way to specify if the CRS declared is a "reproject to" or a "force"one
* [GEOS-1129](https://osgeo-org.atlassian.net/browse/GEOS-1129) shutdown.sh does not work, still referneces stop.jar
* [GEOS-1132](https://osgeo-org.atlassian.net/browse/GEOS-1132) GeoServer.destroy() does not releases ArcSDE connection pools
* [GEOS-1137](https://osgeo-org.atlassian.net/browse/GEOS-1137) WFS and WMS FeatureId filter parsing broken
* [GEOS-1139](https://osgeo-org.atlassian.net/browse/GEOS-1139) Have the demo requests page show the results too (frames)
* [GEOS-1140](https://osgeo-org.atlassian.net/browse/GEOS-1140) KMATTR only works on polygons, not points or lines
* [GEOS-1152](https://osgeo-org.atlassian.net/browse/GEOS-1152) kml ignores scale when rendering rules
* [GEOS-1153](https://osgeo-org.atlassian.net/browse/GEOS-1153) when template fails in kml description, invalid document is produced
* [GEOS-1155](https://osgeo-org.atlassian.net/browse/GEOS-1155) Class cast exceptions with PostPreProcessFilterSplittingVisitor
* [GEOS-1157](https://osgeo-org.atlassian.net/browse/GEOS-1157) kml reprojection broken
* [GEOS-1170](https://osgeo-org.atlassian.net/browse/GEOS-1170) Partial Buffer2 strategy gatherint servlet output stream too early
* [GEOS-1171](https://osgeo-org.atlassian.net/browse/GEOS-1171) Make sure non ASCII chars do not break WFS over shapefile
* [GEOS-1180](https://osgeo-org.atlassian.net/browse/GEOS-1180) Cache control headers aren't working anymore
* [GEOS-1190](https://osgeo-org.atlassian.net/browse/GEOS-1190) wms capabilities fails when no srid set in postgis
* [GEOS-1201](https://osgeo-org.atlassian.net/browse/GEOS-1201) html code don't validate for the OpenLayers preview generated
* [GEOS-1203](https://osgeo-org.atlassian.net/browse/GEOS-1203) Png image preview OOMs with reprojection in the mix
* [GEOS-1205](https://osgeo-org.atlassian.net/browse/GEOS-1205) Data store list is not sorted, hard to find stuff inside of it...
* [GEOS-1211](https://osgeo-org.atlassian.net/browse/GEOS-1211) Wrong scale computation in previewing projected layers
* [GEOS-1214](https://osgeo-org.atlassian.net/browse/GEOS-1214) Inline feature parser does not take into account the CRS when parsing the feature type
* [GEOS-1215](https://osgeo-org.atlassian.net/browse/GEOS-1215) Returned coverage dimensions do not always match those requested
* [GEOS-1218](https://osgeo-org.atlassian.net/browse/GEOS-1218) Shapefile with thousands of points not entirely served by GeoServer
* [GEOS-1223](https://osgeo-org.atlassian.net/browse/GEOS-1223) Do not force reprojection if no geometry properties are around
* [GEOS-1233](https://osgeo-org.atlassian.net/browse/GEOS-1233) Legend graphics are not antialiased
* [GEOS-1241](https://osgeo-org.atlassian.net/browse/GEOS-1241) Points aren't picking up KML name from SLD label
* [GEOS-1243](https://osgeo-org.atlassian.net/browse/GEOS-1243) GetLegendGraphic does not work with anything complicated (labels I think?)
* [GEOS-1247](https://osgeo-org.atlassian.net/browse/GEOS-1247) superoverlays break at high zoom levels
* [GEOS-1250](https://osgeo-org.atlassian.net/browse/GEOS-1250) Remote external graphics fail for KML points
* [GEOS-1258](https://osgeo-org.atlassian.net/browse/GEOS-1258) Fast bbox computation missing for Oracle
* [GEOS-1260](https://osgeo-org.atlassian.net/browse/GEOS-1260) GetLegendGraphics sample request fails
* [GEOS-1261](https://osgeo-org.atlassian.net/browse/GEOS-1261) Multiple feature types with the same name and different namespace make insert code fail
* [GEOS-1264](https://osgeo-org.atlassian.net/browse/GEOS-1264) SVG point wont' display and validate
* [GEOS-1268](https://osgeo-org.atlassian.net/browse/GEOS-1268) MetaTiling on google maps only works when zoomed in
* [GEOS-1270](https://osgeo-org.atlassian.net/browse/GEOS-1270) preview window shouldn't show pdf and svg options for coverages

Task:

* [GEOS-972](https://osgeo-org.atlassian.net/browse/GEOS-972) QA and package coverage tools
* [GEOS-1103](https://osgeo-org.atlassian.net/browse/GEOS-1103) Investigate TileCache through Jython
* [GEOS-1169](https://osgeo-org.atlassian.net/browse/GEOS-1169) update chinese translation
* [GEOS-1202](https://osgeo-org.atlassian.net/browse/GEOS-1202) Update documentation to refer to webapps/geoserver instead of server/geoserver
* [GEOS-1237](https://osgeo-org.atlassian.net/browse/GEOS-1237) Remove overview window from default openlayers output
* [GEOS-1244](https://osgeo-org.atlassian.net/browse/GEOS-1244) Document that remote tilecache needs a later version of TileCache

Sub-task:

* [GEOS-977](https://osgeo-org.atlassian.net/browse/GEOS-977) Improve KML reflector
* [GEOS-1075](https://osgeo-org.atlassian.net/browse/GEOS-1075) Investigate previews with multiple maps
