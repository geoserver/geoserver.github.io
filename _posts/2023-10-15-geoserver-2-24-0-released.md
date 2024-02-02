---
author: Peter Smythe
date: 2023-10-15
layout: post
title: GeoServer 2.24.0 Release
categories:
- Announcements
tags:
- Release
- Vulnerability
release: release_224
version: 2.24.0
jira_version: 16902
--- 

GeoServer [2.24.0](/release/2.24.0/) release is now available with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.0/geoserver-2.24.0-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.0/geoserver-2.24.0-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.0/GeoServer-2.24.0-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.0/geoserver-2.24.0-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.0/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 2.24.0 is made in conjunction with GeoTools 30.0, mapfish-print-v2 2.3.0 and GeoWebCache 1.24.0. 

Thanks to Peter Smythe (AfriGIS) and Jody Garnett (GeoCat) for making this release. 

Thanks to everyone who helped test the release candidate: JP Motaung & Nicolas Kemp, Georg Weickelt, Peter Smythe, Tobia Di Pisa, and Giovanni Allegri.

We would like to thank our 2023 sponsors [North River Geographic Systems Inc](https://northrivergeographic.com/)
and [How 2 Map](https://www.how2map.com/) for their financial assistance.

Keeping GeoServer sustainable requires a long term community commitment.
If you were unable to contribute time testing the release candidate,
[sponsorship options](https://geoserver.org/sponsor/) are available via OSGeo.

## Upgrade Notes

GeoServer strives to maintain backwards compatibility allowing for a smooth upgrade experience.

We have one minor change to share in this release:

* URL Checks: The [url check security setting](https://docs.geoserver.org/maintain/en/user/security/urlchecks.html) is now enabled by default.
  
  In GeoServer 2.22.5 and 2.23.2 this setting was available for use, but was turned off by default.
  If you are not yet in a position to upgrade to 2.24.0 you may wish to enable the recommended setting.

## Security Considerations

This release addresses security vulnerabilities and is considered an essential upgrade for production systems.

* [CVE-2023-43795](https://github.com/geoserver/geoserver/security/advisories/GHSA-5pr3-m5hm-9956) WPS Server Side Request Forgery
* [CVE-2023-41339](https://github.com/geoserver/geoserver/security/advisories/GHSA-cqpc-x2c6-2gmf) Unsecured WMS dynamic styling sld=url parameter affords blind unauthenticated SSRF

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## IAU authority support and EPSG assumption removal

The new gs-iau extension module provides support for planetary CRSs, sourced from the International Astronomical Union. This allows users to manage GIS data over the Moon, Mars, or even the Sun, with well known, officially supported codes.

In addition to that, many bug fixes occurred in the management of CRSs and their text representations (plain codes, URL, URIs) so that the EPSG authority is no longer assumed to be the only possibility, in a variety of places, such as, for example, GML output.
The code base has seen this assumption for twenty long years already, and while we made a good effort to eliminate the assumption, it could be still lurking in some places. Please test and let us know.

![Mars CRS in reprojection console](/img/posts/2.24/iau_wkt.png) 

![Mars map, raster and vector data](/img/posts/2.24/mars.png) 

To learn more about this extension please visit the [user-guide documentation](https://docs.geoserver.org/latest/en/user/extensions/iau/index.html). 
Thanks to Andrea Aime (GeoSolutions) for working on this activity.

* [GSIP-219 - Multiple CRS authority support, planetary CRS](https://github.com/geoserver/geoserver/wiki/GSIP-219)
* [GEOS-11075](https://osgeo-org.atlassian.net/browse/GEOS-11075) IAU authority : planetary CRS support
* [GEOS-11001](https://osgeo-org.atlassian.net/browse/GEOS-11001) Support other CRS authorities in WFS
* [GEOS-11002](https://osgeo-org.atlassian.net/browse/GEOS-11002) Support other CRS authorities in WMS
* [GEOS-11056](https://osgeo-org.atlassian.net/browse/GEOS-11056) Support other CRS authorities in WCS
* [GEOS-11064](https://osgeo-org.atlassian.net/browse/GEOS-11064) Support other CRS authorities in WPS
* [GEOS-11066](https://osgeo-org.atlassian.net/browse/GEOS-11066) Support other CRS authorities in importer
* [GEOS-11076](https://osgeo-org.atlassian.net/browse/GEOS-11076) SRSList should show authorities other than EPSG, if available
* [GEOS-10970](https://osgeo-org.atlassian.net/browse/GEOS-10970) CatalogBuilder cannot handle CRS in authorities other than EPSG
* [GEOS-10971](https://osgeo-org.atlassian.net/browse/GEOS-10971) XStreamPersister cannot save CRS references using authorities other than EPSG
* [GEOS-10972](https://osgeo-org.atlassian.net/browse/GEOS-10972) Resource page CRS editors would not work with authorities other than EPSG

## GeoServer Printing Extension Updates

The printing extension has seen big changes - with a host of new functionality developed by GeoSolutions over the years. With this update the printing module can now be used out-of-the-box by [GeoNode](https://geonode.org/) and [MapStore](https://mapstore.geosolutionsgroup.com/mapstore) (no more customization required).

This update covers the release of MapFish Print 2.3.0 (and restores [website](https://mapfish.github.io/mapfish-print-v2/) user-guide).

GeoServer documentation has been updated with [configuration options](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html) covering the new functionality.

* [Max number of columns configuration for multi column legends](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#legends-block)
* [Simple colored box icon in legends](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#simple-colored-box-icons)
* Explicit support of GeoServer CQL_FILTER parameter (also with layers merge support):  [wiki](https://github.com/geosolutions-it/mapfish-print/wiki/Explicit-support-of-Geoserver-CQL_FILTER-parameter)
* [Legend fitting](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#legend-fitting)
* [Don't break legend items](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#don-t-break-legend-items)
* [Reorder legends block in columns](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#reorder-legends-block-in-columns)
* [Images content](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#images-content)
* [Dynamic images page](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#dynamic-images-page)
* [Multipage legends](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#multipage-legends)
* [Custom intervals in ScalebarBlock](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#custom-intervals-in-scalebarblock)
* Clustering Support [wiki](https://github.com/geosolutions-it/mapfish-print/wiki/Clustering-Support)
* [HTML rendering in text blocks](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#html-in-text-blocks)
* [Extra Pages](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#extra-pages)
* [Group Rendering in attribute blocks](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#group-rendering-in-attribute-blocks)
* [Skip rendering of pages](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#skip-rendering-of-pages)
* [Automatic X-Forwarded-For](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#x-forwarded-for)
* [Parsing of Base64 encoded images](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html#base64)

Thanks to GeoSolutions for adding functionality to mapfish-print for the GeoNode project. Shout out to Tobia Di Pisa and Giovanni Allegra for integration testing.
Jody Garnett (GeoCat) was responsible for updating the mapfish print-lib for Java 11 and gathering up the functionality from different branches and forks. And integrating the updated configuration instructions with the GeoServer User Guide.

* [GEOS-11159](https://osgeo-org.atlassian.net/browse/GEOS-11159) Update mapfish-print-lib 2.3.0

## New Security > URL Checks page

The previous 2.23 series added a new Check URL facility under the Security menu, but it was turned off by default, for backwards compatibility reasons. This functionality allows administrators to manage OGC Service use of external resources.

This has been included in GeoServer 2.22.x and 2.23.x series for backwards compatibility. 

**Backwards compatibility note::** This functionality is turned ON by default from GeoServer 2.24.0 onwards.

![URL Checks](/img/posts/2.22/url-check.png) <br/>

For information and examples on how to use the URL Check page, visit [user guide documentation](https://docs.geoserver.org/maintain/en/user/security/urlchecks.html).

* [GSIP 218 - Control remote HTTP requests sent by GeoTools \\ GeoServer](https://github.com/geoserver/geoserver/wiki/GSIP-218)
* [GEOS-10949](https://osgeo-org.atlassian.net/browse/GEOS-10949) Control remote resources accessed by GeoServer
* [GEOS-11048](https://osgeo-org.atlassian.net/browse/GEOS-11048) Improve URL checking

## Project Updates

### Updated Security Policy

This release follows a [revised security policy](https://github.com/geoserver/geoserver/wiki/GSIP-220).
Our existing "responsible disclosure policy" has been renamed, the practice is now called "coordinated vulnerability disclosure."
Last year we enabled GitHub private vulnerability reporting, we will now use these facilities to issue CVE numbers.

> **Coordinated vulnerability disclosure**
> 
> Disclosure policy:
> 
> 1. The reported vulnerability has been verified by working with the geoserver-security list
> 2. GitHub [security advisory](https://github.com/geoserver/geoserver/security) is used to reserve a CVE number
> 3. A fix or documentation clarification is accepted and backported to both the "stable" and "maintenance" branches
> 4. A fix is included for the "stable" and "maintenance" downloads ([released as scheduled](https://github.com/geoserver/geoserver/wiki/Release-Schedule), or issued via emergency update)
> 6. The CVE vulnerability is published with mitigation and patch instructions
> 
> This represents a balance between transparency and participation that does not overwhelm participants. 
> Those seeking greater visibility are encouraged to volunteer with the geoserver-security list;
> or work with one of the [commercial support providers](https://geoserver.org/support/) who participate on behalf of their customers.

This change has already resulted in improved interaction with security researchers.

Thanks to Jody Garnett (GeoCat) for this proposal on behalf of GeoCat Live customers.

* [GSIP 220](https://github.com/geoserver/geoserver/wiki/GSIP-220)
* [SECURITY.md](https://github.com/geoserver/geoserver/blob/main/SECURITY.md)

## Developer updates

### Internal refactor to remove "org.opengis" package usage

The GeoTools project moved away from using the ``org.opengis`` package after complaints from OGC GeoAPI working group representatives, using
the same package name. Interfaces have been moved to the ``org.geotool.api`` package, along with some general clean up.

While this does not affect GeoServer users directly, it's of consequence for those that have installations with custom, home grown plugins
that might have to be migrated as a consequence. For those, the GeoTools project offers a migration guide, along with a refactoring
script that might perform the migration for you, or else, get you close to a working point. GeoServer itself has been migrated
using these scripts, with minimal manual intervention.

For more details, and access to the migration script, please see the [GeoTools 30 upgrade guide](https://docs.geotools.org/stable/userguide/welcome/upgrade.html#geotools-30-x).

Thanks to Jody Garnett (GeoCat), Andrea Aime (GeoSolutions), and Ian Turton (ASTUN Technologies) for all the hard work on this activity.
We would also like to thank the Open Source Geospatial Foundation for setting up a [cross-project activity](https://www.osgeo.org/opengis-harmonization/) and financial support
to address this requested change.

* [GEOS-11070](https://osgeo-org.atlassian.net/browse/GEOS-11070) Upgrading to GeoTools 30.x series, refactor to ``org.geotools.api`` interfaces

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

[FlatGeoBuf](https://flatgeobuf.org/) is a "performant binary encoding for geographic data", a single file
format that also manages to be cloud native and include a spatial index. GeoServer provides access to
this format thought the [WFS FlatGeobuf output format](https://docs.geoserver.org/stable/en/user/community/flatgeobuf/index.html),
which not only can write the format, but also read it as a standard data store.

The [Vector Mosaic datastore](https://docs.geoserver.org/main/en/user/community/vector-mosaic/index.html) supports
creation of mosaics made of single file vector data, useful in situations where the access to data is
targeted to sub-pages of a larger data set (e.g., data for a single time, or a single customer, or a single data collect,
out of a very large uniform set of vectors) and the database storage for it has become either too slow, or too expensive.

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

(Including the changes made in 2.24-RC, the release candidate)

Improvement:

* [GEOS-11114](https://osgeo-org.atlassian.net/browse/GEOS-11114) Improve extensibility in Pre-Authentication scenarios
* [GEOS-11130](https://osgeo-org.atlassian.net/browse/GEOS-11130) Sort parent role dropdown in Add a new role
* [GEOS-11142](https://osgeo-org.atlassian.net/browse/GEOS-11142) Add mime type mapping for yaml files
* [GEOS-11148](https://osgeo-org.atlassian.net/browse/GEOS-11148) Update response headers for the Resources REST API
* [GEOS-11149](https://osgeo-org.atlassian.net/browse/GEOS-11149) Update response headers for the Style Publisher
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

* [GEOS-11138](https://osgeo-org.atlassian.net/browse/GEOS-11138) Jetty unable to start  cvc-elt.1.a / org.xml.sax.SAXParseException
* [GEOS-11140](https://osgeo-org.atlassian.net/browse/GEOS-11140) WPS download can leak image references in the RasterCleaner
* [GEOS-11145](https://osgeo-org.atlassian.net/browse/GEOS-11145) The GUI "wait spinner" is not visible any longer
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

* [GEOS-11134](https://osgeo-org.atlassian.net/browse/GEOS-11134) Feedback on download bundles: README, RUNNING, GPL html files
* [GEOS-11141](https://osgeo-org.atlassian.net/browse/GEOS-11141) production consideration for logging configuration hardening
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

For the complete list see [2.24.0](https://github.com/geoserver/geoserver/releases/tag/2.24.0) release notes. 

# About GeoServer 2.24 Series

Additional information on GeoServer 2.24 series:

* [GeoServer 2.24 User Manual](https://docs.geoserver.org/2.24.x/en/user/)
* [Control remote HTTP requests sent by GeoTools/GeoServer](https://github.com/geoserver/geoserver/wiki/GSIP-218)
* [Multiple CRS authority support, planetary CRS](https://github.com/geoserver/geoserver/wiki/GSIP-219)
* [Extensive GeoServer Printing improvements](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html)
* [Upgraded security policy](https://github.com/geoserver/geoserver/wiki/GSIP-220)

Release notes:
( [2.24.0](https://github.com/geoserver/geoserver/releases/tag/2.24.0)
| [2.24-RC](https://github.com/geoserver/geoserver/releases/tag/2.24-RC)
) 

