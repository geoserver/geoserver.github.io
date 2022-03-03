---
layout: post
title: GeoServer 2.19.4 Released
date: 2021-12-22
author: Andrea Aime
release: release_219
version: 2.19.4
jira_version: 16832
categories: 
 - Announcements
tags:
 - Release
---

The GeoServer team are happy to announce GeoServer
[2.19.4](/release/2.19.4/) release is available for download
([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.4/geoserver-2.19.4-bin.zip/download)
and
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.4/geoserver-2.19.4-war.zip/download))
along with
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.4/geoserver-2.19.4-htmldoc.zip/download)
and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.4/extensions/).
 
 This GeoServer 2.19.4 release was produced in conjunction with GeoTools 25.4 and GeoWebCache 1.19.2, this is a maintenance release recommended for production systems.
 
 Thanks to everyone who contributed, and to Andrea Aime (GeoSolutions) for making this release.

### Security Considerations

This release includes several security enhancements and is a recommended upgrade for production systems:

* GeoServer uses the earlier log4j1 library and is not subject to the Log4j2 remote code execution vulnerabilities reported worldwide. For a detailed discussion please read [GeoServer Log4J2 zero day vulnerability assessment]({% post_url 2021-11-22-logj4-rce-statement %}).

  The release of GeoServer includes a patched version of log4j1 which does not include any remote loggers or socket communication.

If you wish to report a security vulnerability, please visit our website for [instructions on responsible reporting](http://geoserver.org/issues/).

## Improvements and Fixes

### Bug

* [GEOS-10337](https://osgeo-org.atlassian.net/browse/GEOS-10337) Harden importer against failed imports, make failures more evident

* [GEOS-10322](https://osgeo-org.atlassian.net/browse/GEOS-10322) JDBCConfig community module does not deal with stale connections to the database

* [GEOS-10300](https://osgeo-org.atlassian.net/browse/GEOS-10300) The map preview logs errors when using AUTO codes

* [GEOS-10299](https://osgeo-org.atlassian.net/browse/GEOS-10299) The reprojection console does not work with AUTO codes

* [GEOS-10292](https://osgeo-org.atlassian.net/browse/GEOS-10292) Changing worker pool size in raster access is not actually applied \(silent error\)

* [GEOS-10289](https://osgeo-org.atlassian.net/browse/GEOS-10289) GeoServer busy for 1 hour on reloading a 50000 shapefiles Directory datastore

* [GEOS-10281](https://osgeo-org.atlassian.net/browse/GEOS-10281) GeoServer log level not picked up with Catalog reload

* [GEOS-10249](https://osgeo-org.atlassian.net/browse/GEOS-10249) GWC produce NPE when it comes to race condition

### Improvement

* [GEOS-10328](https://osgeo-org.atlassian.net/browse/GEOS-10328) Expire completed and stale importer contexts

* [GEOS-10321](https://osgeo-org.atlassian.net/browse/GEOS-10321) WCS 2.0 might fail to return coverages whose native BBOX goes slighly outside of the dateline

* [GEOS-10315](https://osgeo-org.atlassian.net/browse/GEOS-10315) Features Templating - Allow injecting JSON-LD output in HTML

* [GEOS-10314](https://osgeo-org.atlassian.net/browse/GEOS-10314) Features Templating - allow specifying root @type in the JSON-LD output and a different  name for features array

[GEOS-9904](https://osgeo-org.atlassian.net/browse/GEOS-9904) GeoFence backend DBMS dependencies

### Task

* [GEOS-10335](https://osgeo-org.atlassian.net/browse/GEOS-10335) Update GeoServer to a log4j version that does not support RCEs

* [GEOS-10269](https://osgeo-org.atlassian.net/browse/GEOS-10269) Overriding JSON Object while Merging Feature Templates

* [GEOS-10268](https://osgeo-org.atlassian.net/browse/GEOS-10268) Null Support in Features Templating


## About GeoServer 2.19
 
 Additional information on GeoServer 2.19 series:
 
 * [Log4J2 zero day vulnerability assessment]({% post_url 2021-11-22-logj4-rce-statement %})
 * [WMS GetFeatureInfo includes labels from ColorMap ](https://docs.geoserver.org/stable/en/user/tutorials/ GetFeatureInfo/raster.html)
 * [Promote WMTS multidim to extension](https://github.com/geoserver/geoserver/wiki/GSIP-196)
 * [Promote WPS-Download to extension](https://github.com/geoserver/geoserver/wiki/GSIP-195)
 * Promote params-extractor to extension](https://github.com/geoserver/geoserver/wiki/GSIP-194)
 * [Promote GWC-S3 to extension](https://github.com/geoserver/geoserver/wiki/GSIP-193)
 * [Promote WPS-JDBC to extension status](https://github.com/geoserver/geoserver/wiki/GSIP-197)
 * [Promote MapML to extension status](https://github.com/geoserver/geoserver/wiki/GSIP-200)
 * [GeoServer repository transition to main branch](main-branch.html)

Release notes ( [2.19.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16824) \| [2.19.2](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16821)\| [2.19.1](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16816) \| [2.19.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16814) \| [2.19-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa? projectId=10000&version=16766) )
