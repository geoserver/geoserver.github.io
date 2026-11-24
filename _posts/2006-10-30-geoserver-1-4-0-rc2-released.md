---
author: Brent Owens
date: 2006-10-30
layout: post
link: http://docs.codehaus.org/display/GEOS/2006/10/30/GeoServer+1.4.0-RC2+Released%21
wayback: https://web.archive.org/web/20070101144112/http://docs.codehaus.org:80/display/GEOS/2006/10/30/GeoServer+1.4.0-RC2+Released%21
title: "GeoServer 1.4.0-RC2 Released!"
categories:
- Announcements
---

The GeoServer team is proud to announce the second release candidate of the 1.4 series. You can download the release below. The big push of 1.4.0 is the transition of GeoServer's architecture to [Spring](http://www.springframework.org/) to be more programmer friendly, allowing modular addition of new plug-in services. There is also a new embedded Jetty server, German translation, and a GML datastore extension.

The full list is in the [release notes](#release-notes) below.

----

The GeoServer 1.4.0-RC2 beta release is available for download from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC2/):

#### Docs

- [Release Notes](#release-notes)
- [geoserver-1.4.0-RC2-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC2/geoserver-1.4.0-RC2-doc.zip/download)
- [geoserver-1.4.0-RC2-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC2/geoserver-1.4.0-RC2-javadoc.zip/download)

#### Deployment

- [geoserver-1.4.0-RC2-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC2/geoserver-1.4.0-RC2-war.zip/download)
- [geoserver-1.4.0-RC2-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC2/geoserver-1.4.0-RC2-bin.zip/download)

#### Windows Installer

- [geoserver-1.4.0-RC2a.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC2/geoserver-1.4.0-RC2a.exe/download)

#### Source Code

- [geoserver-1.4.0-RC2-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC2/geoserver-1.4.0-RC2-src.zip/download)

#### DataStore Extensions

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC2/extensions/)

- [GML datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC2/extensions/geoserver-1.4.0-RC2-gml-plugin.zip/download)
- [DB2 datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC2/extensions/geoserver-1.4.0-RC2-db2-plugin.zip/download)
- [MySQL datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC2/extensions/geoserver-1.4.0-RC2-mysql-plugin.zip/download)
- [VPF datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC2/extensions/geoserver-1.4.0-RC2-vpf-plugin.zip/download)
- [WFS datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC2/extensions/geoserver-1.4.0-RC2-wfs-plugin.zip/download)
- [Oracle datastore](https://sourceforge.net/projects/geoserver/files/GeoServer/1.4.0-RC2/extensions/geoserver-1.4.0-RC2-oracle-plugin.zip/download)

Tested with: JBoss, Jetty, Tomcat, WebLogic

GeoServer **[**License**](https://web.archive.org/web/20061030/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

Improvement:

* [GEOS-628](https://osgeo-org.atlassian.net/browse/GEOS-628) GetFeatureResults.addFeatures() enforces equality of type name between feature and meta
* [GEOS-719](https://osgeo-org.atlassian.net/browse/GEOS-719) New jetty 6 version
* [GEOS-742](https://osgeo-org.atlassian.net/browse/GEOS-742) Include German translation

Bug:

* [GEOS-492](https://osgeo-org.atlassian.net/browse/GEOS-492) GetFeatureInfo does not work with projected display in WMS
* [GEOS-582](https://osgeo-org.atlassian.net/browse/GEOS-582) Spring startup and Xerces
* [GEOS-626](https://osgeo-org.atlassian.net/browse/GEOS-626) FeatureResponse.execute()  miscalculates maxFeatures
* [GEOS-627](https://osgeo-org.atlassian.net/browse/GEOS-627) GeoServerFeatureStore implements FeatureStore not FeatureSource
* [GEOS-711](https://osgeo-org.atlassian.net/browse/GEOS-711) WebLogic 8.1 doesn't show the administration console
* [GEOS-740](https://osgeo-org.atlassian.net/browse/GEOS-740) Update datastore extensions for 1.4 geotools 2.2.1 jars
* [GEOS-758](https://osgeo-org.atlassian.net/browse/GEOS-758) Geoserver release is missing the usual datastore plugins
* [GEOS-764](https://osgeo-org.atlassian.net/browse/GEOS-764) GetMap request using XML fails
* [GEOS-766](https://osgeo-org.atlassian.net/browse/GEOS-766) sld:GraphicStroke shows no Graphic
* [GEOS-769](https://osgeo-org.atlassian.net/browse/GEOS-769) install problems on windows with geoserver-1.4.0-RC1b
* [GEOS-770](https://osgeo-org.atlassian.net/browse/GEOS-770) GetFeatureInfo not returning GML with request parameter  INFO_FORMAT=application/vnd.ogc.gml
* [GEOS-771](https://osgeo-org.atlassian.net/browse/GEOS-771) Don't set empty parameters in datastores
* [GEOS-773](https://osgeo-org.atlassian.net/browse/GEOS-773) KML map producer eats Postgis connections for breakfast
* [GEOS-774](https://osgeo-org.atlassian.net/browse/GEOS-774) JAI jars missing from 1.4
* [GEOS-775](https://osgeo-org.atlassian.net/browse/GEOS-775) cannot build without JAI, no instructions on how to add jai, poor explanation

Task:

* [GEOS-647](https://osgeo-org.atlassian.net/browse/GEOS-647) Documentation: Bundling your PlugIn
* [GEOS-757](https://osgeo-org.atlassian.net/browse/GEOS-757) Javadocs online
* [GEOS-759](https://osgeo-org.atlassian.net/browse/GEOS-759) Make Oracle spatial ship as an extra datastore
* [GEOS-760](https://osgeo-org.atlassian.net/browse/GEOS-760) Make GML datastore ship as an extra datastore
* [GEOS-761](https://osgeo-org.atlassian.net/browse/GEOS-761) move tutorail docs from sigma to dist.codehaus.org
* [GEOS-772](https://osgeo-org.atlassian.net/browse/GEOS-772) Document WMS Path
