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

This is a release candidate intended for public review and feedback, made in conjunction with GeoTools 30-RC and GeoWebCache 1.24-RC.

Thanks to Andrea Aime (GeoSolutions) and Jody Garnett (GeoCat) for working on making this release candidate train.

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

### Internal refactor to remove "org.opengis" package usage

TBD

### OGC API community modules continues to improve

The OGC API community module keeps improving. In particular, thanks to the [GeoNovum](https://www.geonovum.nl/) sponsorship, GeoSolutions made the OGC API Features module pass the OGC CITE compliance tests, for the "core" and "CRS by reference" conformance classes.
Along with this work, other significant changes occurred:

* Made the API version number appear in the service path, easing future upgrades
* Support for configurable links, required to get INSPIRE download service compliance. 

In addition to that, the new "search" experimental conformance class allows to POST complex searches against collections, as a JSON document,
in a way similar to the STAC API.

![Editable OGC API links](/img/posts/2.24/api_features_compliance.png) 

![Editable OGC API links](/img/posts/2.24/ogc_api_links.png) 



### And more

For the complete list see [2.24-RC](https://github.com/geoserver/geoserver/releases/tag/2.24-RC) release notes.

## About GeoServer 2.24 Series

Additional information on GeoServer 2.24 series:

* [Control remote HTTP requests sent by GeoTools/GeoServer](https://github.com/geoserver/geoserver/wiki/GSIP-218)

Release notes:
( [2.24-RC](https://github.com/geoserver/geoserver/releases/tag/2.24-RC)
)