---
layout: post
author: Ian Turton
title: GeoServer 2.19.5 Released
date: 2022-03-08
release: release_219
version: 2.19.5
jira_version: 16839
categories: 
 - Announcements
 - Vulnerability
tags:
 - Release
---

The GeoServer team are happy to announce GeoServer
[2.19.5](/release/2.19.5/) release is available for download
([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.5/geoserver-2.19.4-bin.zip/download)
and
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.5/geoserver-2.19.4-war.zip/download))
along with
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.5/geoserver-2.19.4-htmldoc.zip/download)
and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.5/extensions/).
 
 This GeoServer 2.19.5 release was produced in conjunction with GeoTools 25.5 and GeoWebCache 1.19.2, this is a maintenance release recommended for production systems.
 
 Thanks to everyone who contributed, and to Ian Turton (Astun Technology) for making this release.

### Security Considerations

This release includes several security enhancements and is a recommended update for production systems.

This release includes two improvements limiting Server-side request forgery (SSRF) opportunities:

* [GEOS-10389](https://osgeo-org.atlassian.net/browse/GEOS-10389) Introduce ``ENTITY_RESOLUTION_ALLOWLIST`` parameter to further restrict external entity resolution.

  See the user guide on [external entities resolution](https://docs.geoserver.org/latest/en/user/production/config.html#production-config-external-entities) for instructions on use. Keep in mind that the application schema plugin requires external entity resolution to local files be available. The global setting required by application schema has been renamed to [Unrestricted XML External Entity Resolution](https://docs.geoserver.org/latest/en/user/configuration/globalsettings.html#config-globalsettings-external-entities).
  
* [GEOS-10384](https://osgeo-org.atlassian.net/browse/GEOS-10384) Change GetMap to URIKvpParser.
  
  This improvement is used in conjunction with WMS dynamic styling setting [disabling of SLD and SLD_BODY parameters](https://docs.geoserver.org/latest/en/user/services/wms/webadmin.html#disabling-usage-of-dynamic-styling-in-getmap-and-getfeatureinfo-requests). By handling SLD and SLD_BODY as URI values we can avoid a [well-known java side-effect](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=4434494) when comparing URL values.

We would like to thank GeoCat for addressing these two issues on behalf of Fisheries and Oceans Canada. If you wish to report a security vulnerability, please visit our website for [instructions on responsible reporting](http://geoserver.org/issues/).

## Improvements and Fixes

Fixes:

* [GEOS-9785](https://osgeo-org.atlassian.net/browse/GEOS-9785) Invalid argument type=null when trying to use gs:Download WPS identifier
* [GEOS-9770](https://osgeo-org.atlassian.net/browse/GEOS-9770) Cascading WMS server sets invalid I and J when using EPSG:3006 on GetFeatureInfo calls

## About GeoServer 2.19
 
 Additional information on GeoServer 2.19 series:
 
 * [Log4J2 zero day vulnerability assessment]({% post_url 2021-12-13-logj4-rce-statement %})
 * [WMS GetFeatureInfo includes labels from ColorMap ](https://docs.geoserver.org/stable/en/user/tutorials/ GetFeatureInfo/raster.html)
 * [Promote WMTS multidim to extension](https://github.com/geoserver/geoserver/wiki/GSIP-196)
 * [Promote WPS-Download to extension](https://github.com/geoserver/geoserver/wiki/GSIP-195)
 * [Promote params-extractor to extension](https://github.com/geoserver/geoserver/wiki/GSIP-194)
 * [Promote GWC-S3 to extension](https://github.com/geoserver/geoserver/wiki/GSIP-193)
 * [Promote WPS-JDBC to extension status](https://github.com/geoserver/geoserver/wiki/GSIP-197)
 * [Promote MapML to extension status](https://github.com/geoserver/geoserver/wiki/GSIP-200)
 * [GeoServer repository transition to main branch](main-branch.html)

Release notes ( [2.19.5](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16839) \| [2.19.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16832) \| [2.19.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16824) \| [2.19.2](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16821)\| [2.19.1](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16816) \| [2.19.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16814) \| [2.19-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa? projectId=10000&version=16766) )
