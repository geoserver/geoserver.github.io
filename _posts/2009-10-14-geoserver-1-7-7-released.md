---
author: geoserver
comments: true
date: 2009-10-14 15:32:08+00:00
layout: post
link: http://blog.geoserver.org/2009/10/14/geoserver-1-7-7-released/
slug: geoserver-1-7-7-released
title: GeoServer 1.7.7 Released
wordpress_id: 316
categories:
- Announcements
tags:
- lisasoft
- release
- stable
---

With the rush for [FOSS4G](http://2009.foss4g.org) in full swing and most efforts pushing towards a final release of 2.0, we're happy to announce that the GeoServer stable series (1.7.x) is still receiving the love it deserves.  Today we see the release of GeoServer 1.7.7 into the wild.  Though there is a [relatively short list](#release-notes) of bug fixes, a few of the [rare](https://osgeo-org.atlassian.net/browse/GEOS-2061) [but](https://osgeo-org.atlassian.net/browse/GEOS-3379) [critical](https://osgeo-org.atlassian.net/browse/GEOS-3407) leaks have been plugged, and various improvements have been made to the REST configuration API, imagemosaic plugins, and the shapefile output format.

We encourage you to point your browser to the download site and give it a try, and as always, we are keen to [hear any feedback](mailto:geoserver-users@lists.sourceforge.net) you my have.

[GEOS-2061](https://osgeo-org.atlassian.net/browse/GEOS-2061)
[GEOS-3379](https://osgeo-org.atlassian.net/browse/GEOS-3379)
[GEOS-3407](https://osgeo-org.atlassian.net/browse/GEOS-3407)

----

## GeoServer 1.7.7

Released on October 14, 2009

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/geoserver-1.7.7-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/geoserver-1.7.7-war.zip/download)
- [Windows Service Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/geoserver-1.7.7-ng.exe/download)
- [Windows Console Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/geoserver-1.7.7.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/geoserver-1.7.7.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/geoserver-1.7.7-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/geoserver-1.7.7-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/geoserver-1.7.7-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/geoserver-1.7.7-javadoc.zip/download)
- [Release Notes](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/geoserver-1.7.7-releaseNotes.txt/download)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-db2-plugin.zip/download)
- [DB2 (Next Generation)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-db2ng-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-gml-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-oracle-plugin.zip/download)
- [Oracle (Next Generation)](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-oracleng-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-pyramid-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-charts-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-geosearch-plugin.zip/download)
- [Image Map](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-imagemap-plugin.zip/download)
- [OGR Output Format](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-ogr-plugin.zip/download)
- [REST Config](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-restconfig-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/extensions/geoserver-1.7.7-wfsv-plugin.zip/download)

#### [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.7/)

SourceForge Release .

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 15542

## Release notes

New Feature:

* [GEOS-2294](https://osgeo-org.atlassian.net/browse/GEOS-2294) Building a mosaic should be a transparent operation
* [GEOS-2712](https://osgeo-org.atlassian.net/browse/GEOS-2712) Let people configure simple mosaics transparently from the UI
* [GEOS-3317](https://osgeo-org.atlassian.net/browse/GEOS-3317) Reload geoserver configuration via REST

Improvement:

* [GEOS-2195](https://osgeo-org.atlassian.net/browse/GEOS-2195) New FeatureTypes unecessarily append "_Type" to Title
* [GEOS-2636](https://osgeo-org.atlassian.net/browse/GEOS-2636) uploaded sld files are not nicely formatted
* [GEOS-2965](https://osgeo-org.atlassian.net/browse/GEOS-2965) Allow RADIUS to be used as an alias for BUFFER in GetFeatureInfo
* [GEOS-3046](https://osgeo-org.atlassian.net/browse/GEOS-3046) coveragestoryes typed as coveargestores when accessing a coveragestore
* [GEOS-3209](https://osgeo-org.atlassian.net/browse/GEOS-3209) Report back a proper error exception when GetFeatureInfo QUERY_LAYERS is not a subset of LAYERS
* [GEOS-3345](https://osgeo-org.atlassian.net/browse/GEOS-3345) Update EPSG database
* [GEOS-3397](https://osgeo-org.atlassian.net/browse/GEOS-3397) Show GeoServer version more prominently on the doc pages
* [GEOS-3412](https://osgeo-org.atlassian.net/browse/GEOS-3412) Provide better error messages when QUERY_LAYER is not a subset of LAYERS in GetFeatureInfo

Bug:

* [GEOS-2061](https://osgeo-org.atlassian.net/browse/GEOS-2061) Metatling + JPEG -> broken output
* [GEOS-2528](https://osgeo-org.atlassian.net/browse/GEOS-2528) validation tests fail
* [GEOS-2738](https://osgeo-org.atlassian.net/browse/GEOS-2738) OGR extension does not contain a README (or LICENSE) file
* [GEOS-2830](https://osgeo-org.atlassian.net/browse/GEOS-2830) Incorrect data store link when retrieving feature type
* [GEOS-2937](https://osgeo-org.atlassian.net/browse/GEOS-2937) Ensure xmlns mapping for gml exists in schema.xsd or schema.xml
* [GEOS-2985](https://osgeo-org.atlassian.net/browse/GEOS-2985) Cannot use absolute paths in Mosaic Plugin
* [GEOS-3135](https://osgeo-org.atlassian.net/browse/GEOS-3135) The RSS demo popups refer to a TOPP image that does not exist anymore
* [GEOS-3234](https://osgeo-org.atlassian.net/browse/GEOS-3234) Rest API throws error when adding featuretype without geometry
* [GEOS-3271](https://osgeo-org.atlassian.net/browse/GEOS-3271) grouplayer can not be added by REST API when using namespaces
* [GEOS-3285](https://osgeo-org.atlassian.net/browse/GEOS-3285) While trying to save a feature-type from a PostGIS datastore, GeoServer throws a nasty error.
* [GEOS-3304](https://osgeo-org.atlassian.net/browse/GEOS-3304) Directory datastores can be created, but not edited anymore
* [GEOS-3330](https://osgeo-org.atlassian.net/browse/GEOS-3330) Generic WFS DescribeFeatureType responds with 1.1.0 response to a 1.0.0 request
* [GEOS-3379](https://osgeo-org.atlassian.net/browse/GEOS-3379) JVM crashes in a multithreaded load test against an ECW coverage
* [GEOS-3381](https://osgeo-org.atlassian.net/browse/GEOS-3381) Returning XML file as shapefile
* [GEOS-3399](https://osgeo-org.atlassian.net/browse/GEOS-3399) WFS shapefile output generates different names at each call when a field exceeds 10 chars
* [GEOS-3402](https://osgeo-org.atlassian.net/browse/GEOS-3402) XML encoder in WFS 1.1 GetFeature leaks connection
* [GEOS-3407](https://osgeo-org.atlassian.net/browse/GEOS-3407) (The!) Memoryleak in RetypingFeatureSource
* [GEOS-3429](https://osgeo-org.atlassian.net/browse/GEOS-3429) ReflectiveHTMLFormat eats all parsing exceptions
* [GEOS-3430](https://osgeo-org.atlassian.net/browse/GEOS-3430) Ending a list resource URL with a trailing "/" results in failure to locate its template
* [GEOS-3511](https://osgeo-org.atlassian.net/browse/GEOS-3511) Labeling Again
* [GEOS-3541](https://osgeo-org.atlassian.net/browse/GEOS-3541) H2 database in GWC prevents proper servlet shutdown in Tomcat

Task:

* [GEOS-3151](https://osgeo-org.atlassian.net/browse/GEOS-3151) Document Sphinx setup on the most common platforms
* [GEOS-3339](https://osgeo-org.atlassian.net/browse/GEOS-3339) Document mixed geometry handling in SLD
* [GEOS-3386](https://osgeo-org.atlassian.net/browse/GEOS-3386) Oracle + JNDI will fail if the Oracle drivers are left among the GeoServer libs. Document why.
* [GEOS-3403](https://osgeo-org.atlassian.net/browse/GEOS-3403) port fix for GEOS-3277 to 1.7.x
