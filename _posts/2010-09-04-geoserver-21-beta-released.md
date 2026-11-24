---
author: geoserver
comments: true
date: 2010-09-04 14:56:46+00:00
layout: post
link: http://blog.geoserver.org/2010/09/04/geoserver-21-beta-released/
slug: geoserver-21-beta-released
title: GeoServer 2.1 Beta Released!
wordpress_id: 736
categories:
- Announcements
- Features
---

Just in time for FOSS4G the GeoServer community is pleased to announce the release of 2.1 beta1. The first beta release of the long awaited 2.1 branch is now available for download. Anticipation for this release has been growing over the last few months due to the number of notable new features it brings. Let's go down the list.



### WMS Cascading



Something users have asked for since the addition of WMS support itself is cascading, the ability of GeoServer to proxy for another remote WMS server like MapServer or another GeoServer. This feature has many uses such as pulling in a remote base layer and overlaying local vector data onto it or securing a locally unsecured map server. Special thanks to the [University of Perugia](http://www.unipg.it/) for sponsoring this feature.

[Read more](https://web.archive.org/web/20100904/http://geoserver.org/display/GEOS/GSIP+47+-+WMS+cascading) about WMS cascading.



### Virtual Services



Anyone who has published a large number of layers or feature types with GeoServer has probably at some point been annoyed by the fact that every single layer is published by a single global service. WMS has the ability to group and nest layers but WFS and WCS have no such equivalent. Well now with virtual services one can create multiple service endpoints within a single physical geoserver instance.

Special thanks to [Landgate](http://www.landgate.wa.gov.au) for funding this work.

[Read more](http://docs.geoserver.org/latest/en/user/services/virtual-services.html) about virtual services.



### Layers from SQL



GeoServer has always been good at publishing a flat database table. But users often need to do more such as pre filter the data in a table, or join two tables together, or generate column values on the fly with a function. Before this feature the recommendation was to create a view. However views can be a maintenance burden and are at times problematic.

Now one can create a layer directly from an SQL query. And on top of that query definitions can be parameterized which allows one to create dynamic queries on the fly. These parameters can be restricted with regular expressions in order to prevent an SQL injection security hole.

Special thanks to Andrea for spending much of his personal time on this one. And also to [OBIS](http://www.iobis.org/) who provided the funding for the parametric component of the work.

[Read more](http://gridlock.openplans.org/geoserver/trunk/doc/en/user/data/sqlview.html) about SQL layers.



### WPS



With 2.1 and the arrival of WPS we welcome a new OGC service to the family. The [Web Processing Service](http://www.opengeospatial.org/standards/wps) is an OGC service for performing geospatial analysis functions over the web. The specification is extensible in nature and allows for simple processes like buffering a geometry to more complex processes such as image processing.

Historically GeoServer has been focused primarily on data delivery without any tools for performing analysis of spatial data. WPS fills that gap making GeoServer a more compete solution for geospatial web services.

Thanks to [Refractions Research](http://www.refractions.net/) for the initial contribution of the WPS module and to Andrea once again for taking personal time to bring WPS support to its current state.

[Read more](http://geoserver.org/display/GEOSDOC/4.+WPS+-+Web+Processing+Service) about WPS. [Download](http://sourceforge.net/projects/geoserver/files/GeoServer%20Extensions/2.1-beta1/geoserver-2.1-beta1-wps-plugin.zip/download) the WPS extension now to try it out.



### Unit of Measure



Support for units in SLD allows one to specify values in measurements other than pixels such as feet or meters. This adds a very powerful capability to SLD that in many cases alleviates the need for multiple scale dependent rendering rules. This has the upside of greatly simplifying complex SLD documents.

Special thanks to Milton Jonathan who did the initial GeoTools work to make unit of measure support possible and to Andrea for working with Milton to improve the initial patch.  **Note** that this feature has also been backported to the stable 2.0.x branch. Thanks to [SWECO](http://www.swecogroup.com/en/enswecose/) and [Malmö City of Sweden](http://www.malmo.se/) for sponsoring the backport.

[Read more](http://docs.geoserver.org/latest/en/user/styling/sld-extensions/uom.html) about UOM support.



### DPI Scaling



By default GeoServer renders images at a resolution of 90 DPI. While this is acceptable for the standard screen it is not acceptable for print which requires a higher resolution. Now it is possible to supply a format option to a WMS request on the fly that controls the DPI setting.

Special thanks again to [SWECO](http://www.swecogroup.com/en/enswecose/) and to [Malmö City of Sweden](http://www.malmo.se/) for sponsoring this work. **Note** also that this feature has also been backported to the stable 2.0.x branch.

[Read more](http://docs.geoserver.org/latest/en/user/services/wms/vendor.html#format-options) about DPI scaling.



### And More



And as usual this release comes with a number of bug fixes and minor improvements. Check out the entire [changelog](#release-notes). Help us get to 2.1.0 by downloading the beta and trying it out. Be sure to report any issues on the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users) or in the [bug tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS).

Thanks for using GeoServer!

----

## GeoServer 2.1-beta1

Released on 08/03/2010

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/geoserver-2.1-beta1-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/geoserver-2.1-beta1-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/geoserver-2.1-beta1.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/geoserver-2.1-beta1.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/geoserver-2.1-beta1-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/geoserver-2.1-beta1-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/geoserver-2.1-beta1-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/geoserver-2.1-beta1-javadoc.zip/download)
- [Release Notes](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/geoserver-2.1-beta1-notes.txt)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-imagemosaic-jdbc-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-charts-plugin.zip/download)
- [Control flow](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-control-flow-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-ogr-plugin.zip/download)
- [RESTConfig](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-restconfig-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/extensions/geoserver-2.1-beta1-wfsv-plugin.zip/download)

#### [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/2.1-beta1/)

SourceForge Release .

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 16727

## Release notes

New Feature:

* [GEOS-623](https://osgeo-org.atlassian.net/browse/GEOS-623) Cascading WMS: include remote WMS layers as virtual DataStores

Improvement:

* [GEOS-3905](https://osgeo-org.atlassian.net/browse/GEOS-3905) Control CSS -> FeatureTypeStyle conversion with z-index parameter
* [GEOS-3920](https://osgeo-org.atlassian.net/browse/GEOS-3920) Add Labeling VendorOption SLD extensions to CSS module syntax
* [GEOS-3974](https://osgeo-org.atlassian.net/browse/GEOS-3974) Hide the REST API from bots by default
* [GEOS-3981](https://osgeo-org.atlassian.net/browse/GEOS-3981) Add USE_JAI_IMAGEREAD read parameter configuration to CoverageStore
* [GEOS-4017](https://osgeo-org.atlassian.net/browse/GEOS-4017) Simple patch for ColorMapLegendCreator.java
* [GEOS-4104](https://osgeo-org.atlassian.net/browse/GEOS-4104) GWC transaction listener whipes out the full layer cache upon any transaction on a given layer. Make it respect the transaction bounds as much as possible

Bug:

* [GEOS-3899](https://osgeo-org.atlassian.net/browse/GEOS-3899) Various issues converting a CSS style with scale dependencies
* [GEOS-3982](https://osgeo-org.atlassian.net/browse/GEOS-3982) Intermittent build failure in NewUserPageTest
* [GEOS-3995](https://osgeo-org.atlassian.net/browse/GEOS-3995) Build failure caused by unsafe URL-File conversion in KMLMapTransformer
* [GEOS-3998](https://osgeo-org.atlassian.net/browse/GEOS-3998) GeoserverInfoImpl.setClientProperties has no effect:
* [GEOS-4002](https://osgeo-org.atlassian.net/browse/GEOS-4002) Error occurs when click on the Map CSS Demo link
* [GEOS-4004](https://osgeo-org.atlassian.net/browse/GEOS-4004) Build failure on Windows caused by unsafe File path manipulation in KMLMapTransformer
* [GEOS-4053](https://osgeo-org.atlassian.net/browse/GEOS-4053) ResourcePool caches results out of dirty objects
* [GEOS-4073](https://osgeo-org.atlassian.net/browse/GEOS-4073) Improved word wrap on in-image error reports
* [GEOS-4108](https://osgeo-org.atlassian.net/browse/GEOS-4108) Layer group editor does not include the workspace prefix in layer names

Sub-task:

* [GEOS-4008](https://osgeo-org.atlassian.net/browse/GEOS-4008) Missing SLD in release configuration
