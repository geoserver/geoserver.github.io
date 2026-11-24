---
author: Chris Holmes
date: 2006-07-05
layout: post
link: http://docs.codehaus.org/display/GEOS/2006/07/05/GeoServer+1.3.2+Released
wayback: https://web.archive.org/web/20060708090138/http://docs.codehaus.org:80/display/GEOS/2006/07/05/GeoServer+1.3.2+Released
title: "GeoServer 1.3.2 Released"
categories:
- Announcements
---

The GeoServer Project is pleased to announce the release of version 1.3.2. We know it's not a very glamorous number - if the our project members were focused on marketing instead of building great software we'd probably call it GeoServer XT, or perhaps GeoServer, [Google Earth](http://earth.google.com/) edition, to more accurately reflect what we've been up to. But we think it's a pretty great release.

Improvements for this release include an upgrade to [GeoTools](https://web.archive.org/web/20060705/http://docs.codehaus.org/display/GEOTOOLS/Home) 2.2.x, and some performance tuning on the toolkit, with users reporting at least a 60-70% speed increase against PostGIS. There are also great user contributed fixes to create PDF maps from WMS and to adjust headers to allow caching, which can optimize GeoServer for tiling web mapping clients like [Google Maps](https://web.archive.org/web/20060718160021/http://docs.codehaus.org/display/GEOSDOC/Google+Maps) or [OpenLayers](http://openlayers.org). The other big set of improvements were supported by Google, in order to leverage GeoServer's data reading and map producing capabilities to allow anyone to make their existing data available on Google Earth. The bulk of the work was to create [KML/KMZ output](https://web.archive.org/web/20060707185334/http://docs.codehaus.org/display/GEOSDOC/Google+Earth) from the open WMS standard, which is compatible with Google's network link. Also funded was a basic SLD creation wizard, so that basic map styles can be created through the web administration GUI. There is also a built in KML reflector, making it very easy to connect GeoServer to Google Earth.

With the latest additions GeoServer becomes an ideal server for Google Earth, especially for connecting with existing spatial databases. GeoServer supports PostGIS, ArcSDE, Oracle Spatial, DB2, and Shapefiles and recent improvements with GeoTools 2.2.x pass the majority of the spatial processing back to the database. There is also a KMScore optimization, which has GeoServer render the features as a raster to be used as a Ground Overlay, for situations when there are too many features for Google Earth to efficiently portray. GeoServer will easily handle millions of rows in a geospatial database, and will perform quite nicely as long as the map is styled efficiently with the Styled Layer Descriptors (SLD) specification from the OGC. GeoServer remains 'standard by default', so all layers configured for Google Earth will also be available as standard WMS and WFS. GeoServer's transactional capabilities also allow a community of users to update spatial data, and have it available in a variety of formats.

----

The GeoServer 1.3.2 release is available for download from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.2/):

#### Docs

- [Release Notes](#release-notes)
- [geoserver-1.3.2-docs.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.2/geoserver-1.3.2-docs.zip/download)

#### Deployment

- [geoserver-1.3.2-war.zip](https://sourceforge.net/projects/geoserver/files/OldFiles/1.3.2/geoserver-1.3.2-war.zip/download)
- [geoserver-1.3.2-bin.tar.gz](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.2/geoserver-1.3.2-bin.tar.gz/download)

#### Windows Installer

- [geoserver-1.3.2.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.2/geoserver-1.3.2.exe/download)

#### Source Code

- [geoserver-1.3.2-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.2/geoserver-1.3.2-src.zip/download)

#### DataStore Extensions

[Extensions download page](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/)

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-arcsde-ext1.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-db2-ext.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-mysql-ext.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-vpf-ext.zip/download)
- [WFS datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/DataStore%20Extras%201.3.x%2B/geoserver-1.3.x-wfs-ext.zip/download)

Tested with: JBoss, Jetty, Tomcat, Resin

GeoServer **[License](https://web.archive.org/web/20060705/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

New Feature:

* [GEOS-454](https://osgeo-org.atlassian.net/browse/GEOS-454) Cache-Control based WMS map caching
* [GEOS-573](https://osgeo-org.atlassian.net/browse/GEOS-573) PDF support as an output format
* [GEOS-625](https://osgeo-org.atlassian.net/browse/GEOS-625) Add support for more Math functions in Filters

Improvement:

* [GEOS-534](https://osgeo-org.atlassian.net/browse/GEOS-534) sort featuretypes on featuretype select page
* [GEOS-549](https://osgeo-org.atlassian.net/browse/GEOS-549) Tiger roads demo -- roads disappear when you zoom out.
* [GEOS-598](https://osgeo-org.atlassian.net/browse/GEOS-598) Enable GeoServer to function behind a reverse proxy.
* [GEOS-604](https://osgeo-org.atlassian.net/browse/GEOS-604) Allow more choices in SLD style names
* [GEOS-613](https://osgeo-org.atlassian.net/browse/GEOS-613) Use Geotools 2.2.x

Bug:

* [GEOS-264](https://osgeo-org.atlassian.net/browse/GEOS-264) sld, besides class=... entry, is completely ignored in format image/svg+xml
* [GEOS-355](https://osgeo-org.atlassian.net/browse/GEOS-355) Web-admin can't save WFS datastore
* [GEOS-372](https://osgeo-org.atlassian.net/browse/GEOS-372) Geoserver War file in Tomcat  1.3.0-RC1 War File - Many Problems Needed JAI (Range)
* [GEOS-418](https://osgeo-org.atlassian.net/browse/GEOS-418) Character set encoding for wfs: html content-type differe
* [GEOS-518](https://osgeo-org.atlassian.net/browse/GEOS-518) Cancel button missing on installation dialogue for win32
* [GEOS-540](https://osgeo-org.atlassian.net/browse/GEOS-540) Close tag for tasmania roads datastore
* [GEOS-546](https://osgeo-org.atlassian.net/browse/GEOS-546) SLD Validator uses apache xerces classes
* [GEOS-566](https://osgeo-org.atlassian.net/browse/GEOS-566) Duplicate keys in the translation bundle
* [GEOS-579](https://osgeo-org.atlassian.net/browse/GEOS-579) src distribution is incomplete
* [GEOS-583](https://osgeo-org.atlassian.net/browse/GEOS-583) cuncurrent WFS-requests are causing wrong responses
* [GEOS-602](https://osgeo-org.atlassian.net/browse/GEOS-602) SLD: <PerpendicularOffset> not being applied
* [GEOS-603](https://osgeo-org.atlassian.net/browse/GEOS-603) exception with wfs insert (SetCharacterEncodingFilter)
* [GEOS-624](https://osgeo-org.atlassian.net/browse/GEOS-624) IP Issues
* [GEOS-629](https://osgeo-org.atlassian.net/browse/GEOS-629) Binary download of WFS DataStore should be updated
* [GEOS-631](https://osgeo-org.atlassian.net/browse/GEOS-631) Connections are not closed in WMS
* [GEOS-639](https://osgeo-org.atlassian.net/browse/GEOS-639) Bad SRIDs when inserting Oracle spatial with WFS-T

Task:

* [GEOS-541](https://osgeo-org.atlassian.net/browse/GEOS-541) give the tasmania wfs-t demo a link from the demo page
* [GEOS-542](https://osgeo-org.atlassian.net/browse/GEOS-542) Remove outdated pdfs from docs
* [GEOS-543](https://osgeo-org.atlassian.net/browse/GEOS-543) Make GeoServer war release build from data_dirs/userBasic

Sub-task:

* [GEOS-468](https://osgeo-org.atlassian.net/browse/GEOS-468) Remove old doc stuff from SVN
* [GEOS-545](https://osgeo-org.atlassian.net/browse/GEOS-545) Update to a new version of MapBuilder
* [GEOS-550](https://osgeo-org.atlassian.net/browse/GEOS-550) Datastore delete on empty DS causes StackOverflow error
* [GEOS-551](https://osgeo-org.atlassian.net/browse/GEOS-551) Null pointer if edit, default, or delete on empty namespace
* [GEOS-568](https://osgeo-org.atlassian.net/browse/GEOS-568) Applying a WFS datastore causes NullPointerException
* [GEOS-619](https://osgeo-org.atlassian.net/browse/GEOS-619) mplement editing controls
