---
author: Brent Owens
comments: true
date: 2007-03-12 03:14:20+00:00
layout: post
link: http://blog.geoserver.org/2007/03/11/geoserver-150-rc2-released/
slug: geoserver-150-rc2-released
title: GeoServer 1.5.0-RC2 released
wordpress_id: 27
categories:
- Announcements
---

The GeoServer team is proud to announce the second release candidate for the 1.5 series. This release brings us closer to the stable 1.5.0 release of GeoServer that contains the new and exciting coverage support (WCS). To compliment the release we have created more documentation and [tutorials](https://web.archive.org/web/20070312/http://docs.codehaus.org/display/GEOSDOC/Load+NASA+Blue+Marble+Data), along with some [tools](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/Coverage%20Tools%200.2/CoverageTools-0.2.exe/download) to help you process your raster images.

You can download the latest version below.

Changes in this version include:
- Bug fixes
- Kml returns proper PNG files
- Kml strips out illegal characters now
- Improved error messages
- UI improvements
- Inline features are back
- Links to old homepage updated
- Performance optimization

The full changelog for this release can be found [here](#release-notes).

----

The GeoServer 1.5.0-RC2 release is available for download from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC2/):

#### Docs

- [Task Tracker](#release-notes)
- [geoserver-1.5.0-rc2-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC2/geoserver-1.5.0-rc2-doc.zip/download)

#### Deployment

- [geoserver-1.5.0-rc2a-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC2/geoserver-1.5.0-rc2a-war.zip/download)
- [geoserver-1.5.0-rc2-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC2/geoserver-1.5.0-rc2-bin.zip/download)

#### Windows Installer

- [geoserver-1.5.0-rc2.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC2/geoserver-1.5.0-rc2.exe/download)

#### Source Code

- [geoserver-1.5.0-rc2-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC2/geoserver-1.5.0-rc2-src.zip/download)

#### DataStore Extensions

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC2/extensions/)

- [ArcSDE datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC2/extensions/geoserver-1.5.0-rc2-arcsde-plugin.zip/download)
- [GML datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC2/extensions/geoserver-1.5.0-rc2-gml-plugin.zip/download)
- [DB2 datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC2/extensions/geoserver-1.5.0-rc2-db2-plugin.zip/download)
- [MySQL datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC2/extensions/geoserver-1.5.0-rc2-mysql-plugin.zip/download)
- [VPF datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC2/extensions/geoserver-1.5.0-rc2-vpf-plugin.zip/download)
- [WFS datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC2/extensions/geoserver-1.5.0-rc2-wfs-plugin.zip/download)
- [Oracle datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.5.0-RC2/extensions/geoserver-1.5.0-rc2-oracle-plugin.zip/download)

#### Extra Plugins and Tools

- Server-side [Caching](https://web.archive.org/web/20070312/http://docs.codehaus.org/display/GEOSDOC/Caching). Especially useful for tiling clients such as OpenLayers or Google Maps.
- [Windows Service Wrapper](https://web.archive.org/web/20070312/http://docs.codehaus.org/display/GEOSDOC/Windows+Service+Wrapper): Run GeoServer as a service.
- [Coverage Tools v0.2](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/Coverage%20Tools%200.2/CoverageTools-0.2.exe/download)

Tested with: JBoss, Jetty, Tomcat, WebLogic

GeoServer **[License](https://web.archive.org/web/20070312/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

Improvement:

* [GEOS-812](https://osgeo-org.atlassian.net/browse/GEOS-812) WMS GetLegendGraphic should output labels if no Rule is specified
* [GEOS-845](https://osgeo-org.atlassian.net/browse/GEOS-845) style boxes in FeatureType Editor in web admin tool need to be wider to deal with longer style names
* [GEOS-851](https://osgeo-org.atlassian.net/browse/GEOS-851) Hard to understand error messages on coverage creation failure
* [GEOS-884](https://osgeo-org.atlassian.net/browse/GEOS-884) Fix tiger roads sld in release configuration
* [GEOS-900](https://osgeo-org.atlassian.net/browse/GEOS-900) Preview page forces data envelope recomputation

Bug:

* [GEOS-531](https://osgeo-org.atlassian.net/browse/GEOS-531) NullPointerException in GeoserverDataDirectory when data directory is packaged in the WAR
* [GEOS-790](https://osgeo-org.atlassian.net/browse/GEOS-790) Create style error reporting for 'invalid name' is wrong
* [GEOS-813](https://osgeo-org.atlassian.net/browse/GEOS-813) GetLegendGraphic without a Rule specified in the request on a point layer only displays one rule
* [GEOS-814](https://osgeo-org.atlassian.net/browse/GEOS-814) width and height in the GetLegendGraphic request should be interpreted as the width and the height of the keyimage (not of the total image).
* [GEOS-825](https://osgeo-org.atlassian.net/browse/GEOS-825) InlineFeatures in SLD-POST not rendering
* [GEOS-826](https://osgeo-org.atlassian.net/browse/GEOS-826) Multiple filter in getMap do not work properly, not single filter for multiple layers
* [GEOS-847](https://osgeo-org.atlassian.net/browse/GEOS-847) Reprojection does not occur during rendering if shapefiles do not have a .prj file associated
* [GEOS-866](https://osgeo-org.atlassian.net/browse/GEOS-866) Update old links on welcome.do page
* [GEOS-897](https://osgeo-org.atlassian.net/browse/GEOS-897) Have GeoServerDataDirectory support prehistoric external data dir
* [GEOS-899](https://osgeo-org.atlassian.net/browse/GEOS-899) Unable to scale WMS past 20 concurrent users
* [GEOS-904](https://osgeo-org.atlassian.net/browse/GEOS-904) application.properties files have not been maintained
* [GEOS-926](https://osgeo-org.atlassian.net/browse/GEOS-926) When creating a CoverageStore, the default value for the URL field is wrong
* [GEOS-947](https://osgeo-org.atlassian.net/browse/GEOS-947) KMZ PNGs no longer work
* [GEOS-954](https://osgeo-org.atlassian.net/browse/GEOS-954) Fix up mapbuilder code for user projections
* [GEOS-955](https://osgeo-org.atlassian.net/browse/GEOS-955) Capabilities requests compute bbox each time
* [GEOS-958](https://osgeo-org.atlassian.net/browse/GEOS-958) KML returns invalid characters in name tags

Task:

* [GEOS-922](https://osgeo-org.atlassian.net/browse/GEOS-922) Check that KML still works

Sub-task:

* [GEOS-314](https://osgeo-org.atlassian.net/browse/GEOS-314) Implement request handling as a Chain of Responsability
* [GEOS-863](https://osgeo-org.atlassian.net/browse/GEOS-863) Alphabetize feature type and datastore names in their lists
