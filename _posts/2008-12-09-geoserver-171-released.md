---
author: Justin Deoliveira
comments: true
date: 2008-12-09 16:55:52+00:00
layout: post
link: http://blog.geoserver.org/2008/12/09/geoserver-171-released/
slug: geoserver-171-released
title: GeoServer 1.7.1 Released
wordpress_id: 158
categories:
- Announcements
- Features
- Tips and Tricks
---

The GeoServer team is happy to announce the release of GeoServer 1.7.1!

The biggest improvement in this release is better **Google Earth support**.   Using revamped KML output (known as the [KML "reflector"](https://web.archive.org/web/20081209/http://geoserver.org/display/GEOSDOC/01-KML+Reflector)) GeoServer can now output [vector super-overlays](https://web.archive.org/web/20081209/http://geoserver.org/display/GEOSDOC/07-KML+Super-Overlays).  Prior to this version, data served by GeoServer when viewed in Google Earth would only update when the the camera stopped.  With super-overlays, however, views are updated dynamically.  Data is also broken up into [regions](https://web.archive.org/web/20081209/http://geoserver.org/display/GEOSDOC/08-KML+Regionation) which are used to sort features into a hierarchy so that more prominent features are visible at higher zoom levels and less prominent features become visible at lower zoom levels. Super-overlays also work on raster datasets, providing lower resolutions versions of imagery (overviews) at higher zoom levels and higher resolutions at lower zoom levels.

All of this is is a huge step for GeoServer, as it is now the first major GIS server to return placemarks, lines, and polygons with the super-overlay mechanism.  This means that serving data through Google Earth is a more seamless experience; your data will look like it is naturally part of Google Earth.  And with super-overlays, you can serve large amounts of data with minimal performance issues.

In addition to super-overlays, GeoServer now has support for adding a [height attribute](https://web.archive.org/web/20081209/http://geoserver.org/display/GEOSDOC/04-KML+Height+and+Time) to features (also known as "extrudes"), which allows Google Earth to [render data in 3-D](https://web.archive.org/web/20081209/http://geoserver.org/display/GEOSDOC/04-Height+Templates). Height information is specified via a template, similar to how one specifies [time attributes](https://web.archive.org/web/20081209/http://geoserver.org/display/GEOSDOC/02-Time+Templates) to create animations.  We have a nice tutorial on how to use the [height feature with super-overlays](https://web.archive.org/web/20081209/http://geoserver.org/display/GEOSDOC/05-Super+Overlays+and+Extrudes+with+Building+Data), to see this in action, but here's a quick screenshot.

[
![](http://geoserver.org/download/attachments/13565962/google_earth2.png)
](http://geoserver.org/download/attachments/13565962/google_earth2.png)

Although the default mode of output using the improved [KML reflector](https://web.archive.org/web/20081209/http://geoserver.org/display/GEOSDOC/01-KML+Reflector) is now the super-overlay mode, the previous default, [refresh](https://web.archive.org/web/20081209/http://geoserver.org/display/GEOSDOC/01-KML+Reflector-modes) mode, is still available. Also available is a [download](https://web.archive.org/web/20081209/http://geoserver.org/display/GEOSDOC/01-KML+Reflector-modes) mode which outputs a self-contained KML file, useful for situations where server access is not necessary or possible.

Special thanks go out to David Winslow for all the great work implementing all the new KML functionality.

This version has more than just improved Google Earth support.  GeoServer now has an official [SQL Server extension](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/extensions/geoserver-1.7.1-sqlserver-plugin.zip/download) (described [previously]({% post_url 2008-11-11-146 %})). In addition, there is a new and improved [Oracle extension](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/extensions/geoserver-1.7.1-oracleng-plugin.zip/download) which provides better performance and security from the previous version.

Further improving the visualization experience is [GeoWebCache](http://geowebcache.org), a WMS tile-caching program.  Previously available as an extension (and still available as a [standalone product](http://geowebcache.org)), GeoWebCache is now built-in to GeoServer and can vastly accelerate map rendering.  We will be talking more about GeoWebCache in a future post.

Finally, this version includes a new [drag and drop installer](https://sourceforge.net/projects/geoserver/files/OldFiles/1.7.1/geoserver-1.7.1.dmg/download) for Mac OS X users.

As always with any GeoServer release a heap of other improvements and bug fixes are included. A total of [98 issues](#release-notes) were handled for this release.

We're very excited about this release, and we encourage you to download, try it out, and let us know what you think. Comments and feedback are always welcome on the [mailing list](mailto:geoserver-users@lists.sourceforge.net), as the community is always interested to hear how people are using GeoServer. Stay tuned for the 1.7.2 release, slated for release in the next month or so, which will include new breakthroughs in support for [GeoSearch]({% post_url 2008-05-13-geoserver-and-googles-geo-search %}).

----

## GeoServer 1.7.1

Released on 12/08/2008

#### Choose a download format:

- [UNIX Binary](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/geoserver-1.7.1a-bin.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/geoserver-1.7.1a.exe/download)
- [Mac Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/geoserver-1.7.1a.dmg/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/geoserver-1.7.1a-war.zip/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/geoserver-1.7.1-src.zip/download)

#### Documentation

- [Documentation (Site Export)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/geoserver-1.7.1-doc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/geoserver-1.7.1-javadoc.zip/download)
- [Release Notes](#release-notes)

#### GeoServer Extensions

**DataStore Extensions**

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/extensions/geoserver-1.7.1-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/extensions/geoserver-1.7.1-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/extensions/geoserver-1.7.1-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/extensions/geoserver-1.7.1-mysql-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/extensions/geoserver-1.7.1-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/extensions/geoserver-1.7.1-vpf-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/extensions/geoserver-1.7.1-oracle-plugin.zip/download)
- [Oracle NG](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/extensions/geoserver-1.7.1-oracleng-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/extensions/geoserver-1.7.1-h2-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/extensions/geoserver-1.7.1a-geosearch-plugin.zip/download)

**Coverage Extensions**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/extensions/geoserver-1.7.1-gdal-plugin.zip/download)

**Service Extensions**

- [Versioning WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/extensions/geoserver-1.7.1-wfsv-plugin.zip/download)

#### GeoServer on [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.1/).

SourceForge Release 645413.

## Release notes

New Feature:

* [GEOS-1933](https://osgeo-org.atlassian.net/browse/GEOS-1933) Dutch translation
* [GEOS-2311](https://osgeo-org.atlassian.net/browse/GEOS-2311) Cannot encode WFS 1.0 transction
* [GEOS-2315](https://osgeo-org.atlassian.net/browse/GEOS-2315) WFSV xml readers do not support "strict=true"
* [GEOS-2318](https://osgeo-org.atlassian.net/browse/GEOS-2318) Move the wfsv module to extension
* [GEOS-2319](https://osgeo-org.atlassian.net/browse/GEOS-2319) Legend generation fails if the size is missing in a ExternalGraphic element
* [GEOS-2333](https://osgeo-org.atlassian.net/browse/GEOS-2333) Disabling services has no more effect
* [GEOS-2335](https://osgeo-org.atlassian.net/browse/GEOS-2335) Per layer security subsystem initializes before the catalog, leading to spurious error messages
* [GEOS-2338](https://osgeo-org.atlassian.net/browse/GEOS-2338) KML super overlays
* [GEOS-2340](https://osgeo-org.atlassian.net/browse/GEOS-2340) default templates per namespace
* [GEOS-2342](https://osgeo-org.atlassian.net/browse/GEOS-2342) FeatureType configuration blows up when using name aliases
* [GEOS-2344](https://osgeo-org.atlassian.net/browse/GEOS-2344) Fix web.xml duplication (and add web.xml validation)
* [GEOS-2367](https://osgeo-org.atlassian.net/browse/GEOS-2367) A single error in catalog loading may prevent GeoServer from starting up
* [GEOS-2387](https://osgeo-org.atlassian.net/browse/GEOS-2387) Oracle-NG parameter issues
* [GEOS-2390](https://osgeo-org.atlassian.net/browse/GEOS-2390) HTML "about" page for layers
* [GEOS-2399](https://osgeo-org.atlassian.net/browse/GEOS-2399) Need a way to specify the encoding of shapefiles generated with SHAPE-ZIP output format
* [GEOS-2400](https://osgeo-org.atlassian.net/browse/GEOS-2400) Issues migrating from 1.6.x to 1.7.0
* [GEOS-2403](https://osgeo-org.atlassian.net/browse/GEOS-2403) Any disabled datastore breaks WFS GetCapabilities
* [GEOS-2405](https://osgeo-org.atlassian.net/browse/GEOS-2405) NPE when saving catalog
* [GEOS-2406](https://osgeo-org.atlassian.net/browse/GEOS-2406) Any disabled datastore breaks DescribeFeatureType
* [GEOS-2407](https://osgeo-org.atlassian.net/browse/GEOS-2407) Add oracle-ng extension datastore
* [GEOS-2408](https://osgeo-org.atlassian.net/browse/GEOS-2408) Catalog corruption when multiple admins hack the configuration

Improvement:

* [GEOS-1064](https://osgeo-org.atlassian.net/browse/GEOS-1064) KML Extrude (2.5d) support
* [GEOS-1322](https://osgeo-org.atlassian.net/browse/GEOS-1322) Investigate the usage of symbol oriented ttf fonts for making maps
* [GEOS-1601](https://osgeo-org.atlassian.net/browse/GEOS-1601) Cannot make service specific kvp reques readers
* [GEOS-1671](https://osgeo-org.atlassian.net/browse/GEOS-1671) Allow GeoServer to play well in a container that controls logging
* [GEOS-2014](https://osgeo-org.atlassian.net/browse/GEOS-2014) Regionating should work without GWC
* [GEOS-2189](https://osgeo-org.atlassian.net/browse/GEOS-2189) Placemark points are outside of sufficiently concave geometries.
* [GEOS-2217](https://osgeo-org.atlassian.net/browse/GEOS-2217) GeoServer extensions needlessly allocates Integer objects for int comparison
* [GEOS-2219](https://osgeo-org.atlassian.net/browse/GEOS-2219) Retype feature reader builds retyped features inefficiently (limiting scalability)
* [GEOS-2255](https://osgeo-org.atlassian.net/browse/GEOS-2255) KML output does not validate
* [GEOS-2284](https://osgeo-org.atlassian.net/browse/GEOS-2284) Ensure GEoServer does not totally wipe out loggers during logging configuration
* [GEOS-2310](https://osgeo-org.atlassian.net/browse/GEOS-2310) GWC won't cache layer when outside (outdated) boundingbox
* [GEOS-2321](https://osgeo-org.atlassian.net/browse/GEOS-2321) ArcSDE extension installation instructions might be confusing
* [GEOS-2348](https://osgeo-org.atlassian.net/browse/GEOS-2348) Bring fonts & colors into line with Geoserver site
* [GEOS-2369](https://osgeo-org.atlassian.net/browse/GEOS-2369) Disable native acceleration for Mosaic
* [GEOS-2375](https://osgeo-org.atlassian.net/browse/GEOS-2375) Namespace-wide templates
* [GEOS-2393](https://osgeo-org.atlassian.net/browse/GEOS-2393) Rest layer page improvements
* [GEOS-2424](https://osgeo-org.atlassian.net/browse/GEOS-2424) allow outputFormat=kml to engage regular kml output with reflector as opoosed to kmz
* [GEOS-2426](https://osgeo-org.atlassian.net/browse/GEOS-2426) Pimp up the release directory WMS metadata
* [GEOS-2432](https://osgeo-org.atlassian.net/browse/GEOS-2432) Geosearch sitemaps need to link to every tile
* [GEOS-2446](https://osgeo-org.atlassian.net/browse/GEOS-2446) regionator does not handle invalid geometries
* [GEOS-2451](https://osgeo-org.atlassian.net/browse/GEOS-2451) UI should prevent creating multiple namespaces with same URI
* [GEOS-2468](https://osgeo-org.atlassian.net/browse/GEOS-2468) Better names for reflector modes

Bug:

* [GEOS-1284](https://osgeo-org.atlassian.net/browse/GEOS-1284) PutStyle for 'create new SLD' wizard is not working.
* [GEOS-1388](https://osgeo-org.atlassian.net/browse/GEOS-1388) Feature deleted does not seem to contribute to the changeset bbox
* [GEOS-1628](https://osgeo-org.atlassian.net/browse/GEOS-1628) r8033 causes coordinates to be miscalculated on GetVersionedFeature request
* [GEOS-2174](https://osgeo-org.atlassian.net/browse/GEOS-2174) New catalog does not appear to be sending events to listeners
* [GEOS-2177](https://osgeo-org.atlassian.net/browse/GEOS-2177) Stack overflow on GetLog
* [GEOS-2192](https://osgeo-org.atlassian.net/browse/GEOS-2192) StackOverflow on GetDiff between FIRST and LAST
* [GEOS-2207](https://osgeo-org.atlassian.net/browse/GEOS-2207) Shapefile field with just null values does not get listed by Feature Type Editor
* [GEOS-2244](https://osgeo-org.atlassian.net/browse/GEOS-2244) Can trigger infinite loop in StreamingRenderer.processStylers
* [GEOS-2250](https://osgeo-org.atlassian.net/browse/GEOS-2250) Can only add one new coveragestore
* [GEOS-2257](https://osgeo-org.atlassian.net/browse/GEOS-2257) Problems using FID in filter statements with AND or OR for ArcSDE data.
* [GEOS-2267](https://osgeo-org.atlassian.net/browse/GEOS-2267) Problem with ISO-8859-1 Encoding in GeoServer 1.6.3  O
* [GEOS-2272](https://osgeo-org.atlassian.net/browse/GEOS-2272) Make secure object wrapping pluggable
* [GEOS-2274](https://osgeo-org.atlassian.net/browse/GEOS-2274) Quiet down WFSV tests
* [GEOS-2307](https://osgeo-org.atlassian.net/browse/GEOS-2307) WFSV v1.0.0 request returning GML3
* [GEOS-2322](https://osgeo-org.atlassian.net/browse/GEOS-2322) RuntimeException on Rollback
* [GEOS-2328](https://osgeo-org.atlassian.net/browse/GEOS-2328) German, French, Portuguese and Spanish L10N seems to be broken
* [GEOS-2330](https://osgeo-org.atlassian.net/browse/GEOS-2330) Issues with filtering reprojected WMS requests
* [GEOS-2331](https://osgeo-org.atlassian.net/browse/GEOS-2331) Greek labels are shown as questionmarks characters
* [GEOS-2341](https://osgeo-org.atlassian.net/browse/GEOS-2341) GeoServer incorrectly caluates bounding box on PostGIS table
* [GEOS-2345](https://osgeo-org.atlassian.net/browse/GEOS-2345) Tiles rendering off from intended bounds?
* [GEOS-2352](https://osgeo-org.atlassian.net/browse/GEOS-2352) Endless loop in org.geoserver.util.ReaderUtils class "stringToList" function
* [GEOS-2368](https://osgeo-org.atlassian.net/browse/GEOS-2368) data directory backup does not preserve templates and other files
* [GEOS-2376](https://osgeo-org.atlassian.net/browse/GEOS-2376) KML reflector generates links referencing styles by rule name rather than style name
* [GEOS-2377](https://osgeo-org.atlassian.net/browse/GEOS-2377) Dynamic styles mis-encoded in KML output
* [GEOS-2383](https://osgeo-org.atlassian.net/browse/GEOS-2383) NPE looking for templates on newly configured layers
* [GEOS-2384](https://osgeo-org.atlassian.net/browse/GEOS-2384) internal wfs schema is not updated when new layers are added
* [GEOS-2391](https://osgeo-org.atlassian.net/browse/GEOS-2391) KML Superoverlays sometimes omit the actual features.
* [GEOS-2392](https://osgeo-org.atlassian.net/browse/GEOS-2392) KML reflector NPE's on bogus modes
* [GEOS-2394](https://osgeo-org.atlassian.net/browse/GEOS-2394) KML Reflector ignores format KVP
* [GEOS-2396](https://osgeo-org.atlassian.net/browse/GEOS-2396) When i try set the alias name on the layers retrieve an NullPointerException
* [GEOS-2398](https://osgeo-org.atlassian.net/browse/GEOS-2398) kml links in map preview page use old reflector
* [GEOS-2404](https://osgeo-org.atlassian.net/browse/GEOS-2404) Layers failing to show up in Google Earth output
* [GEOS-2427](https://osgeo-org.atlassian.net/browse/GEOS-2427) Cannot edit sample mosaic layer
* [GEOS-2438](https://osgeo-org.atlassian.net/browse/GEOS-2438) KML output doesn't work on Macs
* [GEOS-2439](https://osgeo-org.atlassian.net/browse/GEOS-2439) Dynamic Styles in KML produce bogus KML Styles in the output
* [GEOS-2440](https://osgeo-org.atlassian.net/browse/GEOS-2440) tiles for tiger_roads superoverlay do not load without first zooming out
* [GEOS-2442](https://osgeo-org.atlassian.net/browse/GEOS-2442) KML output into Google Earth yields incorrect feature labels
* [GEOS-2444](https://osgeo-org.atlassian.net/browse/GEOS-2444) Thematic map not showing up properly in Google Earth (no colors)
* [GEOS-2445](https://osgeo-org.atlassian.net/browse/GEOS-2445) saving multiple times breaks the regionator
* [GEOS-2447](https://osgeo-org.atlassian.net/browse/GEOS-2447) kml vector transformer relies on consistent fids
* [GEOS-2449](https://osgeo-org.atlassian.net/browse/GEOS-2449) Excessive logging from GeoSearch or KML
* [GEOS-2453](https://osgeo-org.atlassian.net/browse/GEOS-2453) BBOX filter does not work on ArcSDE
* [GEOS-2459](https://osgeo-org.atlassian.net/browse/GEOS-2459) WFS-T demo does not work anymore (regression)
* [GEOS-2463](https://osgeo-org.atlassian.net/browse/GEOS-2463) GeoServerTemplate loader NPE if the feature type is not inside the local catalog
* [GEOS-2465](https://osgeo-org.atlassian.net/browse/GEOS-2465) KML output fails if no strategy name is specified in request and config has a empty string value
* [GEOS-2470](https://osgeo-org.atlassian.net/browse/GEOS-2470) KMLSuperOverlayTransformer does not pass format_options along when encoding link to next level of hierachy
* [GEOS-2472](https://osgeo-org.atlassian.net/browse/GEOS-2472) superoverlays do not work on raster layers without specifying mode=raster
* [GEOS-2473](https://osgeo-org.atlassian.net/browse/GEOS-2473) Fix up default formats returned by reflector
* [GEOS-2479](https://osgeo-org.atlassian.net/browse/GEOS-2479) MapPreview in IE7 is a blank page
* [GEOS-2483](https://osgeo-org.atlassian.net/browse/GEOS-2483) georss links to indivudual entries uses "fid" to filter by id instead of "featureid"
* [GEOS-2522](https://osgeo-org.atlassian.net/browse/GEOS-2522) Running the service wrapper

Task:

* [GEOS-2184](https://osgeo-org.atlassian.net/browse/GEOS-2184) Restore KML Height feature in 1.7.x branch after .0 release is cut.
* [GEOS-2209](https://osgeo-org.atlassian.net/browse/GEOS-2209) Include transparently styled `<name>` in all KML output
* [GEOS-2282](https://osgeo-org.atlassian.net/browse/GEOS-2282) Delete with spatial filter (other than BBOX) fails with PostGIS
* [GEOS-2285](https://osgeo-org.atlassian.net/browse/GEOS-2285) Mac OSX installer
* [GEOS-2434](https://osgeo-org.atlassian.net/browse/GEOS-2434) update brazillian translation
