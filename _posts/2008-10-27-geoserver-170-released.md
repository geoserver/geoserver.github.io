---
author: Justin Deoliveira
comments: true
date: 2008-10-27 05:12:30+00:00
layout: post
link: http://blog.geoserver.org/2008/10/27/geoserver-170-released/
slug: geoserver-170-released
title: GeoServer 1.7.0 Released
wordpress_id: 142
categories:
- Announcements
- Features
---

The GeoServer team is proud to announce the release of GeoServer 1.7.0, available [here](http://geoserver.org/display/GEOS/GeoServer+1.7.0) for download. This is a very big release for GeoServer as the 1.7.x series brings some exciting new features and improvements.

Security in 1.7 has been improved by allowing access control at the [layer/feature type level](http://geoserver.org/display/GEOS/GSIP+19+-+Per+layer+security), in addition to the [service level](http://geoserver.org/display/GEOSDOC/2.6+Security+subsystem). This allows users to secure data in a much more granular way. There has also been much work done to better performance for GeoServer 1.7. The short of which is faster rendering with WMS, as well as faster data access with Shapefile, PostGIS, and ArcSDE. For those interested in the specifics check out the [presentation](http://presentations.opengeo.org/2008_FOSS4G/WebMapServerPerformance-FOSS4G2008.pdf) given by Andrea Aime at FOSS4G this year in South Africa. Also of note for this release is a retrofit of the built in [OpenLayers](http://openlayers.org) map preview. The preview interface now allows for filtering and controlling various rendering aspects such as anti-aliasing and image format.

The folks from [GeoSolutions](http://www.geo-solutions.it/) have also been quite busy as usual and have once again made some great improvements on the raster/coverage side of things. GeoServer now supports [additional raster formats](http://geoserver.org/display/GEOSDOC/ImageIO-ext+GDAL+extensions) such as ECW, MrSID, and JPEG 2000. This has been achieved by leveraging the [GDAL](http://www.gdal.org/) library. As well as additional formats GeoSolutions has also provided the ability to perform much more powerful coverage portrayal via the SLD [RasterSymbolizer](http://docs.codehaus.org/display/GEOTOOLS/Raster+Symbolizer+support) construct. With support for RasterSymbolizer users can now do channel selection, define color maps, perform contrast enhancement, and more. Special thanks to GeoSolutions.

As the GeoServer community expands, so does the number of translations to support other languages. 1.7 brings a Dutch and a Russian translation. Thanks to Leon Vanberio and Maxim Dubinin for their great contributions. And special thanks to all users who helped us test the 1.7 release candidates and filed bugs in the tracker.

Not only is GeoServer 1.7.0 a big release for users, it's also a notable one for developers. Some major improvements have been done to the GeoServer core which will act as building blocks for features in future releases. This involves a change to the internal feature model which now allows the modeling of complex feature relationships; something that gets us closer to achieving full community schema support. There have also been changes to the back-end configuration subsystem which now has a much cleaner API for developers writing plug-ins and user interface components. It will also serve as the base for supporting additional persistence mechanisms such as hibernate and other O/R mappers.

And as usual a heap of bugs were fixed for this release. Over [200 issues](http://jira.codehaus.org/secure/IssueNavigator.jspa?reset=true&&fixfor=14627&fixfor=14538&fixfor=13880&fixfor=14500&fixfor=14475&fixfor=14377&fixfor=13881&pid=10311&sorter/field=issuekey&sorter/order=DESC) were handled for 1.7.0.

[Download](http://geoserver.org/display/GEOS/GeoServer+1.7.0), try it out, and let us know what you think. Comments and feedback are always welcome on the [mailing list](mailto:geoserver-users@lists.sourceforge.net). The community is always interested to hear how people are using GeoServer. Also stay tuned for the 1.7.1 release, due out in a month or so, which will include some exciting new improvements to Google Earth and KML support.
