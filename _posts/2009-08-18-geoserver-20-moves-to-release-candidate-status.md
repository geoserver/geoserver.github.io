---
author: geoserver
comments: true
date: 2009-08-18 16:18:53+00:00
layout: post
link: http://blog.geoserver.org/2009/08/18/geoserver-20-moves-to-release-candidate-status/
slug: geoserver-20-moves-to-release-candidate-status
title: GeoServer 2.0 moves to Release Candidate status
wordpress_id: 240
categories:
- Announcements
tags:
- rc
- release
- ui
---

The GeoServer Team would like to announce that GeoServer 2.0 is now out of beta and has moved into Release Candidate status.

In case you haven't been following our [previous]({% post_url 2009-06-03-geoserver-20-now-in-beta %}) [posts]({% post_url 2009-07-21-geoserver-20-beta2-released %}), GeoServer 2.0 contains a completely redesigned user interface, using [Wicket](http://wicket.apache.org/).  Based on feedback from our beta testers, the move to RC1 consisted mainly of user interface improvements. One specific new feature to point out is that ArcSDE stores have a [better configuration panel](https://osgeo-org.atlassian.net/browse/GEOS-3310), one that simplifies requests to raster coverages.

With [55 issues fixed](#release-notes), this first Release Candidate is deemed stable by the GeoServer Team.  But we need your help to verify this, so please download this new version and try it out.

**N.B.**  If you wish to connect GeoServer 2.0 to your existing data directory (from 1.7.x), beware that GeoServer 2.0 changes the directory structure a bit, so should you wish to switch back to 1.7.x, you will need to [hand edit some files](https://web.archive.org/web/20090818/http://geoserver.org/display/GEOSDOC/Migrating+Between+1.7.x+and+2.0.x).

Thanks to everyone who helped out with this release!  Keep sending that feedback in.  Assuming no large problems are found, we should have an official release in the next month or two.

----

## GeoServer 2.0-RC1

Released on 2009-08-14

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/geoserver-2.0-RC1-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/geoserver-2.0-RC1-war.zip/download)
- [Windows Service Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/geoserver-2.0-RC1-ng.exe/download)
- [Windows Console Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/geoserver-2.0-RC1.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/GeoServer-2.0-RC1.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/geoserver-2.0-RC1-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/geoserver-2.0-RC1-htmldocs.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/geoserver-2.0-RC1-javadoc.zip/download)
- [Release Notes](http://downloads.sourceforge.net/project/geoserver/GeoServer/2.0-RC1/geoserver-2.0-RC1-releaseNotes.txt)
- [Change Log](#release-notes)

#### Extensions

**Datastore**

- [Application Schema Support](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-app-schema-plugin.zip/download)
- [ArcSDE](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.0-RC1/geoserver-2.0-RC1a-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-mysql-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-feature-pregeneralized-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-oracle-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-vpf-plugin.zip/download)

**Coveragestore**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-pyramid-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-charts-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-geosearch-plugin.zip/download)
- [Image Map](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-imagemap-plugin.zip/download)
- [OGR Output Format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-ogr-plugin.zip/download)
- [REST](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-restconfig-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/extensions/geoserver-2.0-RC1-wfsv-plugin.zip/download)

#### [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC1/)

SourceForge Release .

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 15379

## Release notes

Improvement:

* [GEOS-2858](https://osgeo-org.atlassian.net/browse/GEOS-2858) Allow the user to check if JAI and JAI Image I/O native extensions are properly installed
* [GEOS-2895](https://osgeo-org.atlassian.net/browse/GEOS-2895) Ensure all pages fit/resize nicely into 1024x768
* [GEOS-3110](https://osgeo-org.atlassian.net/browse/GEOS-3110) Add a set of common tasks to the home page when user is authenaticated
* [GEOS-3157](https://osgeo-org.atlassian.net/browse/GEOS-3157) Provide feedback when ajax actions are performed
* [GEOS-3163](https://osgeo-org.atlassian.net/browse/GEOS-3163) NullPointerException on a (bad) WMS request
* [GEOS-3230](https://osgeo-org.atlassian.net/browse/GEOS-3230) Upgrade xml-apis dependency to 1.3.04
* [GEOS-3274](https://osgeo-org.atlassian.net/browse/GEOS-3274) Further speed up i18n resource loading
* [GEOS-3277](https://osgeo-org.atlassian.net/browse/GEOS-3277) Improve error handling for WMS GetMap requests so only a well known set of rendering exceptions are ignored
* [GEOS-3278](https://osgeo-org.atlassian.net/browse/GEOS-3278) Make sure shapefiles generated by SHAPE-ZIP wfs output format do not contain dots in the name
* [GEOS-3308](https://osgeo-org.atlassian.net/browse/GEOS-3308) Make worskpace name editable
* [GEOS-3309](https://osgeo-org.atlassian.net/browse/GEOS-3309) Provide a store edit extension point so specific store types can provide it's own config page
* [GEOS-3310](https://osgeo-org.atlassian.net/browse/GEOS-3310) Implement a custom ArcSDE coverage store configuration panel

Bug:

* [GEOS-2830](https://osgeo-org.atlassian.net/browse/GEOS-2830) Incorrect data store link when retrieving feature type
* [GEOS-2885](https://osgeo-org.atlassian.net/browse/GEOS-2885) If layer fails to add to catalog invalid resource is still created
* [GEOS-2953](https://osgeo-org.atlassian.net/browse/GEOS-2953) imagemosaic-jdbc-plugin generates empty zip
* [GEOS-3093](https://osgeo-org.atlassian.net/browse/GEOS-3093) items in the metadata map do not round trip type
* [GEOS-3170](https://osgeo-org.atlassian.net/browse/GEOS-3170) Setting number of decimals on feature type page does not persist
* [GEOS-3182](https://osgeo-org.atlassian.net/browse/GEOS-3182) GML2 output returns invalid feature bounds when geometry is null
* [GEOS-3196](https://osgeo-org.atlassian.net/browse/GEOS-3196) Layer group style doesn't override layer default style
* [GEOS-3215](https://osgeo-org.atlassian.net/browse/GEOS-3215) error when disabling store
* [GEOS-3234](https://osgeo-org.atlassian.net/browse/GEOS-3234) Rest API throws error when adding featuretype without geometry
* [GEOS-3238](https://osgeo-org.atlassian.net/browse/GEOS-3238) remove styles
* [GEOS-3253](https://osgeo-org.atlassian.net/browse/GEOS-3253) Changing log level is not reflected until server restart
* [GEOS-3257](https://osgeo-org.atlassian.net/browse/GEOS-3257) StyleEditPageTest  and StyleNewPageTest  fail on Windows
* [GEOS-3258](https://osgeo-org.atlassian.net/browse/GEOS-3258) Newly created style yield Java stack trace on deletion
* [GEOS-3259](https://osgeo-org.atlassian.net/browse/GEOS-3259) Default style has errors
* [GEOS-3260](https://osgeo-org.atlassian.net/browse/GEOS-3260) Can't change the name of existing styles
* [GEOS-3262](https://osgeo-org.atlassian.net/browse/GEOS-3262) Friendly redirect page's home icon redirects to wrong URL
* [GEOS-3288](https://osgeo-org.atlassian.net/browse/GEOS-3288) Cite engine compiles only under Mac
* [GEOS-3290](https://osgeo-org.atlassian.net/browse/GEOS-3290) GeoServerFeatureSource does not handle a null targetCRS
* [GEOS-3295](https://osgeo-org.atlassian.net/browse/GEOS-3295) relative file urls become absolute URLs after save/load cycle
* [GEOS-3302](https://osgeo-org.atlassian.net/browse/GEOS-3302) New layer group UI does not allow to just rely on the layer default style
* [GEOS-3303](https://osgeo-org.atlassian.net/browse/GEOS-3303) Update "Implementing a RESTful Service" to reference version 2.0-SNAPSHOT
* [GEOS-3305](https://osgeo-org.atlassian.net/browse/GEOS-3305) GeoServer trunk does not correctly match a shapefile's projection to the correct epsg
* [GEOS-3311](https://osgeo-org.atlassian.net/browse/GEOS-3311) When schema.xml does not contain gml namespace decl, DescribeFeatureType created invali
* [GEOS-3314](https://osgeo-org.atlassian.net/browse/GEOS-3314) Style validation does not understand GeoServer extensions anymore
* [GEOS-3315](https://osgeo-org.atlassian.net/browse/GEOS-3315) "compute lat/lon from native" does not work if the declared srs has been filled by hand
* [GEOS-3316](https://osgeo-org.atlassian.net/browse/GEOS-3316) Add a UI for the limited SRS in WMS caps
* [GEOS-3318](https://osgeo-org.atlassian.net/browse/GEOS-3318) RestConfig test failure
* [GEOS-3322](https://osgeo-org.atlassian.net/browse/GEOS-3322) WFS 1.1 output broken when changing the namespace URI (after restart)
* [GEOS-3323](https://osgeo-org.atlassian.net/browse/GEOS-3323) Catalog's *InfoImpl objects toString() may return null
* [GEOS-3332](https://osgeo-org.atlassian.net/browse/GEOS-3332) WFS 1.0 output ignores numDecimals on a feature type
* [GEOS-3421](https://osgeo-org.atlassian.net/browse/GEOS-3421) GeoWebCache seems not work correctly?

Task:

* [GEOS-2777](https://osgeo-org.atlassian.net/browse/GEOS-2777) include the icu jar in the distribution
* [GEOS-2887](https://osgeo-org.atlassian.net/browse/GEOS-2887) port all extensions from 1.7.x to trunk
* [GEOS-3060](https://osgeo-org.atlassian.net/browse/GEOS-3060) Port restconfig to trunk
* [GEOS-3063](https://osgeo-org.atlassian.net/browse/GEOS-3063) Make sure GeoServer generates valid XHTML
* [GEOS-3079](https://osgeo-org.atlassian.net/browse/GEOS-3079) Update the release module for web2 into core
* [GEOS-3127](https://osgeo-org.atlassian.net/browse/GEOS-3127) Use loadable/detachable model for StoreInfo in coverage/dataaccess edit pages
* [GEOS-3151](https://osgeo-org.atlassian.net/browse/GEOS-3151) Document Sphinx setup on the most common platforms
* [GEOS-3229](https://osgeo-org.atlassian.net/browse/GEOS-3229) Upgrade OpenLayers demos to 2.8 on trunk
* [GEOS-3291](https://osgeo-org.atlassian.net/browse/GEOS-3291) Add ability to clear resource pool caches
* [GEOS-3297](https://osgeo-org.atlassian.net/browse/GEOS-3297) Port geosearch extension to trunk
* [GEOS-3298](https://osgeo-org.atlassian.net/browse/GEOS-3298) Port sql server extension to trunk
* [GEOS-3299](https://osgeo-org.atlassian.net/browse/GEOS-3299) Port feature-pregen plugin to trunk
* [GEOS-3300](https://osgeo-org.atlassian.net/browse/GEOS-3300) Port imagemosaic-jdbc extension to trunk
