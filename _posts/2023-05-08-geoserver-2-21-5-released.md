---
author: Daniele Romagnoli
date: 2023-05-08
layout: post
title: GeoServer 2.21.5 Release
categories:
- Announcements
tags:
- Release
release: release_2211
version: 2.21.5
jira_version: 16881 
---

GeoServer [2.21.5](/release/2.21.5/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.5/geoserver-2.21.5-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.5/geoserver-2.21.5-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.5/GeoServer-2.21.5-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.5/geoserver-2.21.5-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.5/extensions/).

This is a maintenance release of the GeoServer 2.21.x series, made in conjunction with GeoTools 27.5 
and GeoWebCache 1.21.5.

Thanks to Daniele Romagnoli (GeoSolutions) for making this release.

### Security Considerations

**2024-06-30 Update:** The following mitigation has been provided:

* [CVE-2024-36401](https://github.com/geoserver/geoserver/security/advisories/GHSA-6jj6-gm7p-fcvv) Remote Code Execution (RCE) vulnerability in evaluating property name expressions (Critical)

  [geoserver-2.21.5-patches.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.5/geoserver-2.21.5-patches.zip/download) (replacing `gt-app-schema`, `gt-complex` and `gt-xsd-core` jars) has been provided by Andrea (GeoSolutions)

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

### Release notes

Bug

* [GEOS-3978](https://osgeo-org.atlassian.net/browse/GEOS-3978) Layer configuration allows admin to enter a zero area bounding box

* [GEOS-6313](https://osgeo-org.atlassian.net/browse/GEOS-6313) Lifecycle handlers not properly called during shutdown

* [GEOS-10006](https://osgeo-org.atlassian.net/browse/GEOS-10006) Seeding GWC doesn't work for layers with a dot in the name

* [GEOS-10500](https://osgeo-org.atlassian.net/browse/GEOS-10500) WFS-T unable to delete more than 30 features in a single transaction when the data source is PostGIS

* [GEOS-10517](https://osgeo-org.atlassian.net/browse/GEOS-10517) jms-cluster classes missing from XStream security configuration

* [GEOS-10593](https://osgeo-org.atlassian.net/browse/GEOS-10593) Regression: Creating SQL View via REST API and explicit attribute list is no-longer possible

* [GEOS-10611](https://osgeo-org.atlassian.net/browse/GEOS-10611) Uploading application/zip to styles endpoint does not clean up temporary files

* [GEOS-10828](https://osgeo-org.atlassian.net/browse/GEOS-10828) OGC API - Features - Plugin breaks core \`/rest\` API with JSON payloads

* [GEOS-10837](https://osgeo-org.atlassian.net/browse/GEOS-10837) geopackage output fails when java.io.tmpdir on network share

* [GEOS-10869](https://osgeo-org.atlassian.net/browse/GEOS-10869) Jayway JSON Path libraries not included anymore on GeoServer packages

* [GEOS-10878](https://osgeo-org.atlassian.net/browse/GEOS-10878) wps-multidimensional and wps-jdbc are not being deployed on maven repo 

* [GEOS-10896](https://osgeo-org.atlassian.net/browse/GEOS-10896) Missing NULL check in the template backwards mapping

* [GEOS-10899](https://osgeo-org.atlassian.net/browse/GEOS-10899) Features template escapes twice HTML produced outputs

* [GEOS-10912](https://osgeo-org.atlassian.net/browse/GEOS-10912) jms-cluster fails to clone grid coverage layer on other nodes

* [GEOS-10920](https://osgeo-org.atlassian.net/browse/GEOS-10920) Excel output format packaging misses dependencies, cannot produce .xls

* [GEOS-10921](https://osgeo-org.atlassian.net/browse/GEOS-10921) Double escaping of HTML with enabled features-templating

* [GEOS-10932](https://osgeo-org.atlassian.net/browse/GEOS-10932) csw-iso: should only add 'xsi:nil = false' attribute

* [GEOS-10946](https://osgeo-org.atlassian.net/browse/GEOS-10946) WMS GetLegendGraphic throws FootprintsTransformation cannot be cast to ProcessFunction Exception

* [GEOS-10950](https://osgeo-org.atlassian.net/browse/GEOS-10950) Performance regression in DescribeFeatureType across all feature types

* [GEOS-10957](https://osgeo-org.atlassian.net/browse/GEOS-10957) Support ResourceAccessManager implementations returning custom subclasess of AccessLimits

Improvement

* [GEOS-10870](https://osgeo-org.atlassian.net/browse/GEOS-10870) Allow importer AttributesToPointGeometryTransform to preserve original geometries, and to configure the name of the target geometry

* [GEOS-10940](https://osgeo-org.atlassian.net/browse/GEOS-10940) Update MapML viewer to release 0.11.0

Task

* [GEOS-10867](https://osgeo-org.atlassian.net/browse/GEOS-10867) Bump commons-fileupload from 1.4 to 1.5

* [GEOS-10873](https://osgeo-org.atlassian.net/browse/GEOS-10873) Upgrade XStream to 1.4.20

* [GEOS-10908](https://osgeo-org.atlassian.net/browse/GEOS-10908) Update spring version from 5.2.22 to 5.2.23

* [GEOS-10863](https://osgeo-org.atlassian.net/browse/GEOS-10863) Update Oracle JDBC driver to 19.18.0.0

* [GEOS-10904](https://osgeo-org.atlassian.net/browse/GEOS-10904) Bump jettison from 1.5.3 to 1.5.4

For complete information see [2.22.5 release 
notes](https://github.com/geoserver/geoserver/releases/tag/2.21.5).

## About GeoServer 2.21

Additional information on GeoServer 2.21 series:

- [Feature Type Customization](https://github.com/geoserver/geoserver/wiki/GSIP-207)
- [Add Styles support to LayerGroup](https://github.com/geoserver/geoserver/wiki/GSIP-205)
- [Log4j1 update or replace activity]({% post_url 2022-01-20-log4j-upgrade %})

Release notes:
( [2.21.5](https://github.com/geoserver/geoserver/releases/tag/2.21.5)
| [2.21.4](https://github.com/geoserver/geoserver/releases/tag/2.21.4)
| [2.21.3](https://github.com/geoserver/geoserver/releases/tag/2.21.3)
| [2.21.2](https://github.com/geoserver/geoserver/releases/tag/2.21.2)
| [2.21.1](https://github.com/geoserver/geoserver/releases/tag/2.21.1)
| [2.21.0](https://github.com/geoserver/geoserver/releases/tag/2.21.0)
| [2.21-RC](https://github.com/geoserver/geoserver/releases/tag/2.21-RC)
)
