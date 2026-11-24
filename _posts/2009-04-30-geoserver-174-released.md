---
author: bmmpxf
comments: true
date: 2009-04-30 14:35:48+00:00
layout: post
link: http://blog.geoserver.org/2009/04/30/geoserver-174-released/
slug: geoserver-174-released
title: GeoServer 1.7.4 Released
wordpress_id: 211
categories:
- Polls
- Tutorials
tags:
- release
---

The GeoServer Team is happy to announce the the release of GeoServer 1.7.4, the fifth stable version in the 1.7 series.

This release contains some new features, many having to do with improved map rendering options.  We have introduced [WMS decoration](http://docs.geoserver.org/1.7.4/user/advanced/wmsdecoration.html), which provides a framework for adding images such as compasses and legends to WMS requests using absolute, not spatial, positioning.  The GetFeatureInfo request, often used when clicking on an OpenLayers map, now has a parameter that can be adjusted to allow for looser tolerance, eliminating the need to click precisely on the feature.  GetFeatureInfo also now observes the filters in the SLD, so as to prevent displaying information about a hidden feature.  (Thanks to [SATA Hi-Tech Services](http://www.sata-hts.com/), an Italian company specializing in data security solutions, for providing funding for the GetFeatureInfo improvements.)  Those who work with labels on your map will be pleased to note that label conflict resolution (the selective display of labels to prevent visual collisions) can now be turned off if desired.  Finally, we have the ability to generate [custom legends for raster files](https://web.archive.org/web/20090430/http://geoserver.org/display/GEOS/Raster+Legends+Explained) via the GetLegendGraphic request.

And, as usual, a whole host of [bug fixes](#release-notes) (over 50!) have been incorporated into this release.  Give it a try!

Development work on the 1.7 series will begin to wind down in favor of [GeoServer 2.0]({% post_url 2009-04-20-see-the-new-ui %}), but we anticipate the release of 1.7.5 within the next two months.

----

## GeoServer 1.7.4

Released on April 29, 2009

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/geoserver-1.7.4-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/geoserver-1.7.4-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/geoserver-1.7.4.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/geoserver-1.7.4.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/geoserver-1.7.4-src.zip/download)

#### Documentation

(NEW!) [Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/geoserver-1.7.4-doc.zip/download)

- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/geoserver-1.7.4-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Datastore**

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-db2-plugin.zip/download)
- [DB2 (Next Generation)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-db2ng-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-oracle-plugin.zip/download)
- [Oracle (Next Generation)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-oracleng-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-vpf-plugin.zip/download)

**Coveragestore**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-pyramid-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [OGR Output Format](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-ogr-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-wfsv-plugin.zip/download)
- [REST](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-restconfig-plugin.zip/download)
- GeoExt Styler
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-geosearch-plugin.zip/download)
- [Image Map](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/extensions/geoserver-1.7.4-imagemap-plugin.zip/download)

#### [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.4/)

SourceForge Release 679097.

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 14787

## Release notes

New Feature:

* [GEOS-1008](https://osgeo-org.atlassian.net/browse/GEOS-1008) GetFeatureInfo should take into consideration filters in the SLD
* [GEOS-1162](https://osgeo-org.atlassian.net/browse/GEOS-1162) Support custom raster legends via GetLegendGraphic
* [GEOS-1434](https://osgeo-org.atlassian.net/browse/GEOS-1434) Making the tolerance of FeatureInfo-Requests configurable
* [GEOS-2625](https://osgeo-org.atlassian.net/browse/GEOS-2625) Allow label conflict resolution to be turned off for selected labels
* [GEOS-2815](https://osgeo-org.atlassian.net/browse/GEOS-2815) WMS Decoration Layout

Improvement:

* [GEOS-948](https://osgeo-org.atlassian.net/browse/GEOS-948) the namespace in front of the layer name in a map request is required
* [GEOS-1520](https://osgeo-org.atlassian.net/browse/GEOS-1520) Improve the cite testing documentation
* [GEOS-1624](https://osgeo-org.atlassian.net/browse/GEOS-1624) GML3-GZIP is not there
* [GEOS-2049](https://osgeo-org.atlassian.net/browse/GEOS-2049) Remove the regionation factories, register the regionation strategies directly instead
* [GEOS-2363](https://osgeo-org.atlassian.net/browse/GEOS-2363) Commit various improvements for RESTConfig
* [GEOS-2372](https://osgeo-org.atlassian.net/browse/GEOS-2372) MIN_GOODNESS_FIT causing labels to be missed off.
* [GEOS-2529](https://osgeo-org.atlassian.net/browse/GEOS-2529) REST CoverageListResource improvement
* [GEOS-2531](https://osgeo-org.atlassian.net/browse/GEOS-2531) REST CoverageResource improvement
* [GEOS-2575](https://osgeo-org.atlassian.net/browse/GEOS-2575) Tone down client stream aborted exceptions in kml/kmz map producers
* [GEOS-2629](https://osgeo-org.atlassian.net/browse/GEOS-2629) Try to provide better error messages when the capabilities document fails due to a misconfigured layer
* [GEOS-2692](https://osgeo-org.atlassian.net/browse/GEOS-2692) Allow for certain invalid characters (such as a period) in the created shapefile name
* [GEOS-2701](https://osgeo-org.atlassian.net/browse/GEOS-2701) Have FeatureBoundsFeatureCollection force in the proper reference system when the wrapped collection does return an envelope without one
* [GEOS-2776](https://osgeo-org.atlassian.net/browse/GEOS-2776) New splash screen for installers
* [GEOS-2786](https://osgeo-org.atlassian.net/browse/GEOS-2786) GetFeatureInfo default template should not uppercase attribute names
* [GEOS-2824](https://osgeo-org.atlassian.net/browse/GEOS-2824) Add number format support in text symbolizer
* [GEOS-2906](https://osgeo-org.atlassian.net/browse/GEOS-2906) Add pom maven-resources-plugin configuration to set encoding to UTF-8

Bug:

* [GEOS-2053](https://osgeo-org.atlassian.net/browse/GEOS-2053) SLD Library with WMS request not working properly
* [GEOS-2070](https://osgeo-org.atlassian.net/browse/GEOS-2070) Oracle data won't show up properly when bbox exceeeds world bounds
* [GEOS-2598](https://osgeo-org.atlassian.net/browse/GEOS-2598) Java exception when doing getFeatureInfo on OpenLayers map with 2 layers
* [GEOS-2628](https://osgeo-org.atlassian.net/browse/GEOS-2628) Request method check in GetMapRequest randomly throws NPE
* [GEOS-2633](https://osgeo-org.atlassian.net/browse/GEOS-2633) Layer group bounds generation fails with postgis layers
* [GEOS-2656](https://osgeo-org.atlassian.net/browse/GEOS-2656) Cannot configure a shapefile whose name is less than 3 chars long
* [GEOS-2670](https://osgeo-org.atlassian.net/browse/GEOS-2670) Dynamic symbolizers not evaluated in KML output
* [GEOS-2690](https://osgeo-org.atlassian.net/browse/GEOS-2690) WFS-T updates including geometry changes fail on Oracle-NG
* [GEOS-2695](https://osgeo-org.atlassian.net/browse/GEOS-2695) WFS requests with PropertyName have error when using 1.0.0 (1.1.0 is OK) on 1.7.2
* [GEOS-2732](https://osgeo-org.atlassian.net/browse/GEOS-2732) SHAPE-ZIP output format fails when the input data source does not have the geometry as the first attribute
* [GEOS-2734](https://osgeo-org.atlassian.net/browse/GEOS-2734) Image Mosaic JDBC extension does not contain a README (or LICENSE) file
* [GEOS-2737](https://osgeo-org.atlassian.net/browse/GEOS-2737) Imagemap extension does not contain a README (or LICENSE) file
* [GEOS-2744](https://osgeo-org.atlassian.net/browse/GEOS-2744) Raster Issue - no-data pixels in full tiles should be 0xFF instead of 0x00
* [GEOS-2745](https://osgeo-org.atlassian.net/browse/GEOS-2745) SDE Raster issue - Error fetching colormap data
* [GEOS-2746](https://osgeo-org.atlassian.net/browse/GEOS-2746) SDE Raster issue - Some layers not drawing properly at different zoom levels
* [GEOS-2752](https://osgeo-org.atlassian.net/browse/GEOS-2752) Loading base maps which have trailing default styles fails
* [GEOS-2769](https://osgeo-org.atlassian.net/browse/GEOS-2769) Error saving the configuration of a new feature type
* [GEOS-2778](https://osgeo-org.atlassian.net/browse/GEOS-2778) new directory datastore creates backup feature types instead of feature types
* [GEOS-2779](https://osgeo-org.atlassian.net/browse/GEOS-2779) SLD filter against Postgresql 8.3.+
* [GEOS-2781](https://osgeo-org.atlassian.net/browse/GEOS-2781) Stack overflow when using SLD with many rules against a JDBC database
* [GEOS-2803](https://osgeo-org.atlassian.net/browse/GEOS-2803) FeatureType: baseschema: gml:AbstractFeatureType
* [GEOS-2807](https://osgeo-org.atlassian.net/browse/GEOS-2807) Rendering issues caused by a poor quality shapefile
* [GEOS-2818](https://osgeo-org.atlassian.net/browse/GEOS-2818) Namespace deletion should check for any store/layer still using the namespace
* [GEOS-2820](https://osgeo-org.atlassian.net/browse/GEOS-2820) GetFeatureInfo does not work with aliased layers
* [GEOS-2821](https://osgeo-org.atlassian.net/browse/GEOS-2821) GeoRSS and GeoJSON throwing exceptions with per layer security
* [GEOS-2823](https://osgeo-org.atlassian.net/browse/GEOS-2823) Shapefile rendering slowdown when using directory data store
* [GEOS-2825](https://osgeo-org.atlassian.net/browse/GEOS-2825) Styles changed using the Styler application (i.e. RESTconfig) are not persisted
* [GEOS-2831](https://osgeo-org.atlassian.net/browse/GEOS-2831) geoserver 1.7.3 hangs while rendering short text
* [GEOS-2832](https://osgeo-org.atlassian.net/browse/GEOS-2832) GetFeatureInfo does not return any rows with text/html format
* [GEOS-2863](https://osgeo-org.atlassian.net/browse/GEOS-2863) GWC Demos don't find OpenLayers.js
* [GEOS-2940](https://osgeo-org.atlassian.net/browse/GEOS-2940) GetFeature fails if no native srs is set in Oracle
* [GEOS-2941](https://osgeo-org.atlassian.net/browse/GEOS-2941) WFS 1.0.0 Cite tests, DescribeFeatureType schema namespace
* [GEOS-2942](https://osgeo-org.atlassian.net/browse/GEOS-2942) best_guess regionating strategy broken

Task:

* [GEOS-2521](https://osgeo-org.atlassian.net/browse/GEOS-2521) GWC needs database for meta information
* [GEOS-2671](https://osgeo-org.atlassian.net/browse/GEOS-2671) Document support for new arcsde raster formats
* [GEOS-2838](https://osgeo-org.atlassian.net/browse/GEOS-2838) Describe new &buffer GetFeatureInfo parameter and the maxBuffer wms setting
