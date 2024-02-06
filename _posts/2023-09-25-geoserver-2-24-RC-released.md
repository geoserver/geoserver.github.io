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

Keeping GeoServer sustainable requires a long term community commitment. If you are unable to contribute time, [sponsorship options](https://geoserver.org/sponsor/) are available via OSGeo.

### IAU authority support and EPSG assumption removal

The new gs-iau extension module provides support for planetary CRSs, sourced from the International Astronomical Union. This allows to manage GIS data over the Moon, Mars, or even the Sun, with well known, officially supported codes.

In addition to that, many bug fixes occurred in the management of CRSs and their text representations (plain codes, URL, URIs) so that the EPSG authority is no longer assumed to be the only possibility, in a variety of places, such as, for example, GML output.
The code base has seen this assumption for twenty years long, and while we made a good effort to eliminate the assumption, it could be still lurking in some places. Please test and let us know.

![Mars CRS in reprojection console](/img/posts/2.24/iau_wkt.png) 

![Mars map, raster and vector data](/img/posts/2.24/mars.png) 

To learn more about this extension please visit the [user-guide documentation](https://docs.geoserver.org/latest/en/user/extensions/iau/index.html). 
Thanks to Andrea Aime (GeoSolutions) for working on this activity.

* [GSIP-219 - Multiple CRS authority support, planetary CRS](https://github.com/geoserver/geoserver/wiki/GSIP-219)
* [GEOS-11075](https://osgeo-org.atlassian.net/browse/GEOS-11075) IAU authority : planetary CRS support
* [GEOS-11001](https://osgeo-org.atlassian.net/browse/GEOS-11001) Support other CRS authories in WFS
* [GEOS-11002](https://osgeo-org.atlassian.net/browse/GEOS-11002) Support other CRS authorities in WMS
* [GEOS-11056](https://osgeo-org.atlassian.net/browse/GEOS-11056) Support other CRS authorities in WCS
* [GEOS-11064](https://osgeo-org.atlassian.net/browse/GEOS-11064) Support other CRS authorities in WPS
* [GEOS-11066](https://osgeo-org.atlassian.net/browse/GEOS-11066) Support other CRS authorities in importer
* [GEOS-11076](https://osgeo-org.atlassian.net/browse/GEOS-11076) SRSList should show authorities other than EPSG, if available
* [GEOS-10970](https://osgeo-org.atlassian.net/browse/GEOS-10970) CatalogBuilder cannot handle CRS in authorities other than EPSG
* [GEOS-10971](https://osgeo-org.atlassian.net/browse/GEOS-10971) XStreamPersister cannot save CRS references using authorities other than EPSG
* [GEOS-10972](https://osgeo-org.atlassian.net/browse/GEOS-10972) Resource page CRS editors would not work with authorities other than EPSG

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

* [GEOS-11132](https://osgeo-org.atlassian.net/browse/GEOS-11132) mapfish-print-v2 2.3-RC 

## New Security > URL Checks page

This release adds a new Check URL facility under the Security menu. This allows administrators to manage OGC Service use of external resources.

![URL Checks](/img/posts/2.22/url-check.png) <br/>

For information and examples on how to use the URL Check page, visit [user guide documentation](https://docs.geoserver.org/maintain/en/user/security/urlchecks.html).

* [GSIP 218 - Control remote HTTP requests sent by GeoTools \\ GeoServer](https://github.com/geoserver/geoserver/wiki/GSIP-218)
* [GEOS-10949](https://osgeo-org.atlassian.net/browse/GEOS-10949) Control remote resources accessed by GeoServer
* [GEOS-11048](https://osgeo-org.atlassian.net/browse/GEOS-11048) Improve URL checking

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

* [GEOS-11070](https://osgeo-org.atlassian.net/browse/GEOS-11070) Upgrading to GeoTools 30.x series, refactor to org.geotools.api interfaces

## Community modules updates 

While not strictly part of this release, it's interesting to know about some community module advances that can be found only in the
the 2.24.x series.

Two extensions are no longer actively supported and are now available as community modules:

* [GEOS-10960](https://osgeo-org.atlassian.net/browse/GEOS-10960) Downgrade imagemap module to community
* [GEOS-10961](https://osgeo-org.atlassian.net/browse/GEOS-10961) Downgrade xslt extension to community

The following community modules have been removed (due to lack of interest):

* [GEOS-10962](https://osgeo-org.atlassian.net/browse/GEOS-10962) Remove wms-eo community module
* [GEOS-10963](https://osgeo-org.atlassian.net/browse/GEOS-10963) Remove SAML community module
* [GEOS-10966](https://osgeo-org.atlassian.net/browse/GEOS-10966) Remove importer-fgdb community module
* [GEOS-10967](https://osgeo-org.atlassian.net/browse/GEOS-10967) Remove teradata community module
* [GEOS-10977](https://osgeo-org.atlassian.net/browse/GEOS-10977) Remove wmts-styles community module
* [GEOS-10978](https://osgeo-org.atlassian.net/browse/GEOS-10978) Remove nsg-wmts community module
* [GEOS-10984](https://osgeo-org.atlassian.net/browse/GEOS-10984) Remove ows-simulate community module

### OGC API community modules continues to improve

The OGC API community module keeps improving. In particular, thanks to the [GeoNovum](https://www.geonovum.nl/) sponsorship, GeoSolutions made the OGC API Features module pass the OGC CITE compliance tests, for the "core" and "CRS by reference" conformance classes.
Along with this work, other significant changes occurred:

* Made the API version number appear in the service path, easing future upgrades
* Support for configurable links, required to get INSPIRE download service compliance. 

In addition to that, the new "search" experimental conformance class allows to POST complex searches against collections, as a JSON document,
in a way similar to the STAC API.

![Editable OGC API links](/img/posts/2.24/api_features_compliance.png) 

![Editable OGC API links](/img/posts/2.24/ogc_api_links.png) 

Those interested in this work are encouraged to contact Andrea Aime (GeoSolutions).

* [GEOS-10924](https://osgeo-org.atlassian.net/browse/GEOS-10924) Support JSON-FG draft encoding in OGC API - Features
* [GEOS-11045](https://osgeo-org.atlassian.net/browse/GEOS-11045) Implement proposal "OGC API - Features - Part n: Query by IDs"
* [GEOS-10882](https://osgeo-org.atlassian.net/browse/GEOS-10882) Add an option to remove trailing slash match in OGC APIs
* [GEOS-10887](https://osgeo-org.atlassian.net/browse/GEOS-10887) Add angle brackets to OGC API CRS Header
* [GEOS-10892](https://osgeo-org.atlassian.net/browse/GEOS-10892) Allow configuring custom links for OGC API "collections" and single collection resources
* [GEOS-10895](https://osgeo-org.atlassian.net/browse/GEOS-10895) Make OGC API CITE compliant even if the trailing slash is disabled: landing page exception
* [GEOS-11058](https://osgeo-org.atlassian.net/browse/GEOS-11058) Support other CRS authorities in OGC APIs
* [GEOS-10909](https://osgeo-org.atlassian.net/browse/GEOS-10909) Don't link from OGC API Features to WFS 2.0 DescribeFeatureType output, if WFS is disabled
* [GEOS-10954](https://osgeo-org.atlassian.net/browse/GEOS-10954) Split ogcapi community module package into single functionality packages

### DataDir Catalogue loader

For folks working with very large catalogues some improvement from [cloud native geoserver](https://github.com/geoserver/geoserver-cloud) are now available to reduce startup time.

Thanks to Gabriel Roldan for folding this improvement into a community module for the rest of the GeoServer community to enjoy.

* [GEOS-11049](https://osgeo-org.atlassian.net/browse/GEOS-11049) Community module "datadir catalog loader"

### GeoServer Access Control List Project

The [GeoServer Access Control List](https://github.com/geoserver/geoserver-acl) project is an independent application service that manages access rules, and a GeoServer plugin that requests authorization limits on a per-request basis.

Gabriel Roldan is the contact point for anyone interested in this work.

* [GSIP 217 - GeoServer ACL project](https://github.com/geoserver/geoserver/wiki/GSIP-217)

### The vector mosaic and FlatGeoBuf modules sport significant performance improvements

[FlatGeoBuf](https://flatgeobuf.org/) is a "A performant binary encoding for geographic data", a single file
format that also manages to be cloud native and include a spatial index. GeoServer provides access to
this format thought the [WFS FlatGeobuf output format](https://docs.geoserver.org/stable/en/user/community/flatgeobuf/index.html),
which not only can write the format, but also read it as a standard data store.

The [Vector Mosaic datastore](https://docs.geoserver.org/main/en/user/community/vector-mosaic/index.html) supports
creation of mosaics made of single file vector data, useful in situations where the access to data is
targeted to sub-pages of a larger data set (e.g., data for a single time, or a single customer, or a single data collect,
out of a very large uniform set of vectors) and the database storage for it is become either too slow, or too expensive.

These two modules make a great combo for those in need to handle very large vector datasets, by storing
the [FlatGeoBuf](https://flatgeobuf.org/) on cheap storage.

In particular, the FlatGeoBuf module saw speed improvements that made it the new "fastest vector format"
for cases where one needs to display a large data set, all at once, on screen (PostGIS remains the king
of the hill for anything that needs sophisticated filtering instead).

For reference, we have timed rendering 4 million tiny polygons out of a precision farming collect, using a 7 classes
quantile based SLDs. Here is a tiny excerpt of the map:

![Small sample out of 4 million polygons](/img/posts/2.24/flatgeobuf.png) 

And here are the timings to render the full set of polygons, putting them all on screen, at the same time, with a single GetMap request:

* PostGIS, 113 seconds
* Shapefile, 41 seconds
* Flatgeobuf, 36 seconds

The tuning is not complete, more optimizations are possible. Interested? Andrea Aime is the contact point for this work.

## Release notes

New Feature:

* [GEOS-10992](https://osgeo-org.atlassian.net/browse/GEOS-10992) Make GWC UI for disk quota expose HSQLDB, remove H2, automatically update existing installations 
* [GEOS-11000](https://osgeo-org.atlassian.net/browse/GEOS-11000) WPS process to provide elevation profile for a linestring

Improvement:

* [GEOS-10926](https://osgeo-org.atlassian.net/browse/GEOS-10926) Community Module Proxy-Base-Ext
* [GEOS-10934](https://osgeo-org.atlassian.net/browse/GEOS-10934) CSW does not show title/abstract on welcome page
* [GEOS-10973](https://osgeo-org.atlassian.net/browse/GEOS-10973) DWITHIN delegation to mongoDB
* [GEOS-10999](https://osgeo-org.atlassian.net/browse/GEOS-10999) Make GeoServer KML module rely on HSQLDB instead of H2
* [GEOS-11005](https://osgeo-org.atlassian.net/browse/GEOS-11005) Make sure H2 dependencies are included in the packages of optional modules that still need it
* [GEOS-11059](https://osgeo-org.atlassian.net/browse/GEOS-11059) Map preview should not assume EPSG authority
* [GEOS-11081](https://osgeo-org.atlassian.net/browse/GEOS-11081) Add option to disable GetFeatureInfo transforming raster layers
* [GEOS-11087](https://osgeo-org.atlassian.net/browse/GEOS-11087) Fix IsolatedCatalogFacade unnecessary performance overhead
* [GEOS-11090](https://osgeo-org.atlassian.net/browse/GEOS-11090) Use Catalog streaming API in WorkspacePage
* [GEOS-11099](https://osgeo-org.atlassian.net/browse/GEOS-11099) ElasticSearch DataStore Documentation Update for RESPONSE_BUFFER_LIMIT
* [GEOS-11100](https://osgeo-org.atlassian.net/browse/GEOS-11100) Add opacity parameter to the layer definitions in WPS-Download download maps
* [GEOS-11102](https://osgeo-org.atlassian.net/browse/GEOS-11102) Allow configuration of the CSV date format
* [GEOS-11116](https://osgeo-org.atlassian.net/browse/GEOS-11116) GetMap/GetFeatureInfo with groups and view params can with mismatched layers/params

Bug:

* [GEOS-8162](https://osgeo-org.atlassian.net/browse/GEOS-8162) CSV Data store does not support relative store paths
* [GEOS-10452](https://osgeo-org.atlassian.net/browse/GEOS-10452) Use of Active Directory authorisation seems broken since 2.15.2 (LDAP still works)
* [GEOS-10874](https://osgeo-org.atlassian.net/browse/GEOS-10874) Log4J: Windows binary zip release file with log4j-1.2.14.jar
* [GEOS-10875](https://osgeo-org.atlassian.net/browse/GEOS-10875) Disk Quota JDBC password shown in plaintext 
* [GEOS-10899](https://osgeo-org.atlassian.net/browse/GEOS-10899) Features template escapes twice HTML produced outputs
* [GEOS-10903](https://osgeo-org.atlassian.net/browse/GEOS-10903) WMS filtering with Filter 2.0 fails
* [GEOS-10921](https://osgeo-org.atlassian.net/browse/GEOS-10921) Double escaping of HTML with enabled features-templating
* [GEOS-10922](https://osgeo-org.atlassian.net/browse/GEOS-10922) Features templating exception on text/plain format
* [GEOS-10928](https://osgeo-org.atlassian.net/browse/GEOS-10928) Draft JSON-FG Implementation for OGC API - Features
* [GEOS-10936](https://osgeo-org.atlassian.net/browse/GEOS-10936) YSLD and OGC API modules are incompatible
* [GEOS-10937](https://osgeo-org.atlassian.net/browse/GEOS-10937) JSON-FG reprojected output should respect authority axis order
* [GEOS-10958](https://osgeo-org.atlassian.net/browse/GEOS-10958) Update Spotbugs to 4.7.3
* [GEOS-10981](https://osgeo-org.atlassian.net/browse/GEOS-10981) Slow CSW GetRecords requests with JDBC Configuration
* [GEOS-10985](https://osgeo-org.atlassian.net/browse/GEOS-10985) Backup Restore of GeoServer catalog is broken with GeoServer 2.23.0 and StAXSource
* [GEOS-10993](https://osgeo-org.atlassian.net/browse/GEOS-10993) Disabled resources can cause incorrect CSW GetRecords response
* [GEOS-11015](https://osgeo-org.atlassian.net/browse/GEOS-11015) geopackage wfs output builds up tmp files over time
* [GEOS-11016](https://osgeo-org.atlassian.net/browse/GEOS-11016) Docker nightly builds use outdated GeoServer war
* [GEOS-11033](https://osgeo-org.atlassian.net/browse/GEOS-11033) WCS DescribeCoverage ReferencedEnvelope with null crs
* [GEOS-11060](https://osgeo-org.atlassian.net/browse/GEOS-11060) charts and mssql extension zips are missing the extension

Task:

* [GEOS-11091](https://osgeo-org.atlassian.net/browse/GEOS-11091) Upgrade spring-security to 5.7.10
* [GEOS-11094](https://osgeo-org.atlassian.net/browse/GEOS-11094) Bump org.hsqldb:hsqldb:2.7.1 to 2.7.2
* [GEOS-11103](https://osgeo-org.atlassian.net/browse/GEOS-11103) Upgrade Hazelcast version to 5.3.x
* [GEOS-10248](https://osgeo-org.atlassian.net/browse/GEOS-10248) WPSInitializer NPE failure during GeoServer reload
* [GEOS-10904](https://osgeo-org.atlassian.net/browse/GEOS-10904) Bump jettison from 1.5.3 to 1.5.4
* [GEOS-10907](https://osgeo-org.atlassian.net/browse/GEOS-10907) Update spring.version from 5.3.25 to 5.3.26
* [GEOS-10941](https://osgeo-org.atlassian.net/browse/GEOS-10941) Update ErrorProne to 2.18
* [GEOS-10987](https://osgeo-org.atlassian.net/browse/GEOS-10987) Bump xalan:xalan and xalan:serializer from 2.7.2 to 2.7.3
* [GEOS-10988](https://osgeo-org.atlassian.net/browse/GEOS-10988) Update spring.version from 5.3.26 to 5.3.27 and spring-integration.version from 5.5.17 to 5.5.18
* [GEOS-11010](https://osgeo-org.atlassian.net/browse/GEOS-11010) Upgrade guava from 30.1 to 32.0.0
* [GEOS-11011](https://osgeo-org.atlassian.net/browse/GEOS-11011) Upgrade postgresql from 42.4.3 to 42.6.0
* [GEOS-11012](https://osgeo-org.atlassian.net/browse/GEOS-11012) Upgrade commons-collections4 from 4.2 to 4.4
* [GEOS-11018](https://osgeo-org.atlassian.net/browse/GEOS-11018) Upgrade commons-lang3 from 3.8.1 to 3.12.0
* [GEOS-11019](https://osgeo-org.atlassian.net/browse/GEOS-11019) Upgrade commons-io from 2.8.0 to 2.12.0
* [GEOS-11020](https://osgeo-org.atlassian.net/browse/GEOS-11020) Add test scope to mockito-core dependency
* [GEOS-11062](https://osgeo-org.atlassian.net/browse/GEOS-11062) Upgrade httpclient from 4.5.13 to 4.5.14
* [GEOS-11063](https://osgeo-org.atlassian.net/browse/GEOS-11063) Upgrade httpcore from 4.4.10 to 4.4.16
* [GEOS-11067](https://osgeo-org.atlassian.net/browse/GEOS-11067) Upgrade wiremock to 2.35.0
* [GEOS-11080](https://osgeo-org.atlassian.net/browse/GEOS-11080) Remove ASCII grid output format from WCS
* [GEOS-11084](https://osgeo-org.atlassian.net/browse/GEOS-11084) Update text field css styling to look visually distinct
* [GEOS-11092](https://osgeo-org.atlassian.net/browse/GEOS-11092) acme-ldap.jar is compiled with Java 8

For the complete list see [2.24-RC](https://github.com/geoserver/geoserver/releases/tag/2.24-RC) release notes. 

## About GeoServer 2.24 Series

Additional information on GeoServer 2.24 series:

* [Control remote HTTP requests sent by GeoTools/GeoServer](https://github.com/geoserver/geoserver/wiki/GSIP-218)
* [Multiple CRS authority support, planetary CRS](https://github.com/geoserver/geoserver/wiki/GSIP-219)

Release notes:
( [2.24-RC](https://github.com/geoserver/geoserver/releases/tag/2.24-RC)
)