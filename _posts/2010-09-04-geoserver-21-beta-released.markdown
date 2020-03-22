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

Just in time for FOSS4G the GeoServer community is pleased to announce the release of 2.1 beta1. The first beta release of the long awaited 2.1 branch is now available for [download](http://geoserver.org/display/GEOS/GeoServer+2.1-beta1). Anticipation for this release has been growing over the last few months due to the number of notable new features it brings. Let's go down the list.



### WMS Cascading



Something users have asked for since the addition of WMS support itself is cascading, the ability of GeoServer to proxy for another remote WMS server like MapServer or another GeoServer. This feature has many uses such as pulling in a remote base layer and overlaying local vector data onto it or securing a locally unsecured map server. Special thanks to the [University of Perugia](http://www.unipg.it/) for sponsoring this feature.

[Read more](http://geoserver.org/display/GEOS/GSIP+47+-+WMS+cascading) about WMS cascading.



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



And as usual this release comes with a number of bug fixes and minor improvements. Check out the entire [changelog](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=15082). Help us get to 2.1.0 by [downloading](http://geoserver.org/display/GEOS/GeoServer+2.1-beta1) the beta and trying it out. Be sure to report any issues on the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users) or in the [bug tracker](http://jira.codehaus.org/browse/GEOS).

Thanks for using GeoServer!
