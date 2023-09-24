---
author: Andrea Aime
date: 2023-09-25
layout: post
title: GeoServer 2.24-RC Release
categories:
- Announcements
tags:
- Release
release: release_224
version: 2.24-RC
jira_version: 16862
---

GeoServer [2.24-RC](/release/2.24-RC/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24-RC/geoserver-2.24-RC-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24-RC/geoserver-2.24-RC-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24-RC/GeoServer-2.24-RC-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24-RC/geoserver-2.24-RC-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24-RC/extensions/).

This is a release candidate intended for public review and feedback, made in conjunction with GeoTools 30-RC, GeoWebCache 1.24-RC, mapfish-print-v2 2.3-RC and geofence-3.7-RC.

Thanks to Andrea Aime (GeoSolutions) and Jody Garnett (GeoCat) for working on making this release candidate.

### Release candidate public testing and feedback

Testing and providing feedback on releases is part of the open-source social contract. The development team (and their employers and customers) are responsible for sharing this great technology with you.

*The collaborative part of open-source happens now - we ask you to test this release candidate in your environment and with your data. Try out the new features, double check if the documentation makes sense, and most importantly let us know!*

*If you spot something that is incorrect or not working do not assume it is obvious and we will notice. We request and depend on your [email](https://geoserver.org/comm/) and [bug reports](https://geoserver.org/issues/) at this time. If you are working with [commercial support](https://geoserver.org/support/) your provider is expected to participate on your behalf.*

Keeping GeoServer sustainable requires a long term community commitment. If you are unable to contribute time, [sponsorship options](https://github.com/geoserver/geoserver/wiki/Sponsor) are available via OSGeo.

### IAU authority support and EPSG assumption removal

The new gs-iau extension module provides support for planetary CRSs, sourced from the International Astronomical Union. This allows to manage GIS data over the Moon, Mars, or even the Sun, with well known, officially supported codes.

In addition to that, many bug fixes occurred in the management of CRSs and their text representations (plain codes, URL, URIs) so that the EPSG authority is no longer assumed to be the only possibility, in a variety of places, such as, for example, GML output.
The code base has seen this assumption for twenty years long, and while we made a good effort to eliminate the assumption, it could be still lurking in some places. Please test and let us know.

![Mars CRS in reprojection console](/img/posts/2.24/iau_wkt.png) 

![Mars map, raster and vector data](/img/posts/2.24/mars.png) 

To learn more about this extension please visit the [user-guide documentation](https://docs.geoserver.org/latest/en/user/extensions/iau/index.html). 
Thanks to Andrea Aime (GeoSolutions) for working on this activity.

* [GSIP-219 - Multiple CRS authority support, planetary CRS](https://github.com/geoserver/geoserver/wiki/GSIP-219)

## GeoServer Printing Extension Updates

The printing extension has seen big changes - with a host of new functionality developed by GeoSolutions over the years. With this update the printing module can now be used out-of-the-box by GeoNode and MapStore (no more customization required).

* [Max number of columns configuration for multi column legends](https://github.com/geosolutions-it/mapfish-print/wiki/Max-number-of-columns-configuration-for-multi-column-legends)
* [Simple colored box icon in legends](https://github.com/geosolutions-it/mapfish-print/wiki/Simple-colored-box-icons)
* [Explicit support of Geoserver CQL_FILTER parameter (also with layers merge support)](https://github.com/geosolutions-it/mapfish-print/wiki/Explicit-support-of-Geoserver-CQL_FILTER-parameter)
* [Legend fitting](https://github.com/geosolutions-it/mapfish-print/wiki/Legend-fitting)
* [Don't break legend items](https://github.com/geosolutions-it/mapfish-print/wiki/Don't-break-legend-items)
* [Reorder legends block in columns](https://github.com/geosolutions-it/mapfish-print/wiki/Reorder-legends-block-in-columns)
* [Images content](https://github.com/geosolutions-it/mapfish-print/wiki/Images-content)
* [Dynamic images page](https://github.com/geosolutions-it/mapfish-print/wiki/Dynamic-images-page)
* [Multipage legends](https://github.com/geosolutions-it/mapfish-print/wiki/Multipage-legends)
* [Custom intervals in ScalebarBlock](https://github.com/geosolutions-it/mapfish-print/wiki/Custom-intervals-in-ScalebarBlock)
* [Clustering Support](https://github.com/geosolutions-it/mapfish-print/wiki/Clustering-Support)
* [HTML rendering in text blocks](https://github.com/geosolutions-it/mapfish-print/wiki/HTML-In-Text-Blocks)
* [Extra Pages](https://github.com/geosolutions-it/mapfish-print/wiki/Extra-Pages)
* [Group Rendering in attribute blocks](https://github.com/geosolutions-it/mapfish-print/wiki/Group-Rendering-In-Attribute-Blocks)
* [Skip rendering of pages](https://github.com/geosolutions-it/mapfish-print/wiki/Skip-Rendering-Of-Pages)
* [Automatic X-Forwarded-For](https://github.com/geosolutions-it/mapfish-print/wiki/X-Forwarded-For)
* [Parsing of Base64 encoded images](https://github.com/geosolutions-it/mapfish-print/wiki/Base64-encoded-images)

Thanks to GeoSolutions for adding functionality to mapfish-print for the GeoNode project.
Jody Garnett (GeoCat) was responsible for updating the mapfish print-lib for Java 11 and gathering up the functionality from different branches and forks.

## New Security > URL Checks page

This release adds a new Check URL facility under the Security menu. This allows administrators to manage OGC Service use of external resources.

![URL Checks](/img/posts/2.22/url-check.png) <br/>

For information and examples on how to use the URL Check page, visit [user guide documentation](https://docs.geoserver.org/maintain/en/user/security/urlchecks.html).

* [GSIP 218 - Control remote HTTP requests sent by GeoTools \\ GeoServer](https://github.com/geoserver/geoserver/wiki/GSIP-218)

## Developer updates

### Internal refactor to remove "org.opengis" package usage

The GeoTools project moved away from using the "org.opengis" package after complaints from OGC GeoAPI working group representatives, using
the same package name.
Interfaces have been moved to the "org.geotool.api" package, along with some general clean up.

While this does not affect GeoServer users directly, it's of consequence for those that have installation with custom, home grown plugins
that might have to be migrated as a consequence. For those, the GeoTools project offers a migration guide, along with a refactoring
script that might perform the migration for you, or else, get you close to a working point. GeoServer itself has been migrated
using these scripts, with minimal manual intervention.

For more details, and access to the migration script, please see the [GeoTools 30 upgrade guide](https://docs.geotools.org/stable/userguide/welcome/upgrade.html#geotools-30-x).

Thanks to Jody Garnett (GeoCat), Andrea Aime (GeoSolutions), and Ian Turton (ASTUN Technologies) for all the hard work on this activity.
We would also like to thank the Open Source Geospatial Foundation for setting up a [cross-project activity](https://www.osgeo.org/opengis-harmonization/) and financial support
to address this requested change.

## Community modules updates 

While not strictly part of this release, it's interesting to know about some community module advances that can be found only in the
the 2.24.x series.

### datadir catalogue loader

For folks working with very large catalogues and improvement from [cloud native geoserver](https://github.com/geoserver/geoserver-cloud) has been made to reduce startup time.

Thanks to Gabriel Roland for folding this improvement into a community module for the rest of the GeoServer community to enjoy.

### GeoServer Access Control List Project

The [GeoServer Access Control List](https://github.com/geoserver/geoserver-acl) project is an independent application service that manages access rules, and a GeoServer plugin that requests authorization limits on a per-request basis.

Gabriel Roldand is the contact point for anyone interested in this work.

* [GSIP 217 - GeoServer ACL project](https://github.com/geoserver/geoserver/wiki/GSIP-217)

#### OGC API community modules continues to improve

The OGC API community module keeps improving. In particular, thanks to the [GeoNovum](https://www.geonovum.nl/) sponsorship, GeoSolutions made the OGC API Features module pass the OGC CITE compliance tests, for the "core" and "CRS by reference" conformance classes.
Along with this work, other significant changes occurred:

* Made the API version number appear in the service path, easing future upgrades
* Support for configurable links, required to get INSPIRE download service compliance. 

In addition to that, the new "search" experimental conformance class allows to POST complex searches against collections, as a JSON document,
in a way similar to the STAC API.

![Editable OGC API links](/img/posts/2.24/api_features_compliance.png) 

![Editable OGC API links](/img/posts/2.24/ogc_api_links.png) 

#### The vector mosaic and FlatGeoBuf modules sport significant performance improvements

These two modules make a great combo for those in need to handle very large vector datasets, by storing
the FlatGeoBuf on cheap storage, as long as data access patterns are well known and the typical access
tends to access a "page" of data (e.g., data for a single time, or a single customer, or a single data collect,
out of a very large uniform set of vectors).

In particular, the FlatGeoBuf module saw speed improvements that made it the new "fastest vector format"
for cases where one needs to display a large data set, all at once, on screen (PostGIS remains the king
of the hill for anything that needs sophisticated filtering instead).

For more information check out [WFS FlatGeobuf output format](https://docs.geoserver.org/stable/en/user/community/flatgeobuf/index.html) in the user guide.

### And more

For the complete list see [2.24-RC](https://github.com/geoserver/geoserver/releases/tag/2.24-RC) release notes.

## About GeoServer 2.24 Series

Additional information on GeoServer 2.24 series:

* [Control remote HTTP requests sent by GeoTools/GeoServer](https://github.com/geoserver/geoserver/wiki/GSIP-218)
* [Multiple CRS authority support, planetary CRS](https://github.com/geoserver/geoserver/wiki/GSIP-219)

Release notes:
( [2.24-RC](https://github.com/geoserver/geoserver/releases/tag/2.24-RC)
)