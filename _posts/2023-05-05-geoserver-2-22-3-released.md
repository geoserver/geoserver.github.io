---
author: Daniele Romagnoli
date: 2023-05-05
layout: post
title: GeoServer 2.22.3 Release
categories:
- Announcements
tags:
- Release
release: release_222
version: 2.22.3
jira_version: 16882
---

GeoServer [2.22.3](/release/2.22.3/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.3/geoserver-2.22.3-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.3/geoserver-2.22.3-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.3/GeoServer-2.22.3-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.3/geoserver-2.22.3-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.3/extensions/).

This is a maintenance release of the GeoServer 2.22.x series, made in conjunction with GeoTools 28.3 
and GeoWebCache 1.22.2.


Thanks to Daniele Romagnoli (GeoSolutions) for making this release.

### Release notes

Sub-task:

* [GEOS-10908](https://osgeo-org.atlassian.net/browse/GEOS-10908) Update spring version from 5.2.22 to 5.2.23

Bug:

* [GEOS-3978](https://osgeo-org.atlassian.net/browse/GEOS-3978) Layer configuration allows admin to enter a zero area bounding box

* [GEOS-6313](https://osgeo-org.atlassian.net/browse/GEOS-6313) Lifecycle handlers not properly called during shutdown

* [GEOS-10006](https://osgeo-org.atlassian.net/browse/GEOS-10006) Seeding GWC doesn't work for layers with a dot in the name

* [GEOS-10500](https://osgeo-org.atlassian.net/browse/GEOS-10500) WFS-T unable to delete more than 30 features in a single transaction when the data source is PostGIS

* [GEOS-10517](https://osgeo-org.atlassian.net/browse/GEOS-10517) jms-cluster classes missing from XStream security configuration

* [GEOS-10593](https://osgeo-org.atlassian.net/browse/GEOS-10593) Regression: Creating SQL View via REST API and explicit attribute list is no-longer possible

* [GEOS-10611](https://osgeo-org.atlassian.net/browse/GEOS-10611) Uploading application/zip to styles endpoint does not clean up temporary files

* [GEOS-10837](https://osgeo-org.atlassian.net/browse/GEOS-10837) geopackage output fails when java.io.tmpdir on network share

* [GEOS-10865](https://osgeo-org.atlassian.net/browse/GEOS-10865) Backwards incompatible change in the XML representation of user roles

* [GEOS-10869](https://osgeo-org.atlassian.net/browse/GEOS-10869) Jayway JSON Path libraries not included anymore on GeoServer packages

* [GEOS-10871](https://osgeo-org.atlassian.net/browse/GEOS-10871) about geoserver page reporting @project.version@ for WAR deploy

* [GEOS-10878](https://osgeo-org.atlassian.net/browse/GEOS-10878) wps-multidimensional and wps-jdbc are not being deployed on maven repo 

* [GEOS-10890](https://osgeo-org.atlassian.net/browse/GEOS-10890) Wrong path for the license file in the Windows installer script

* [GEOS-10896](https://osgeo-org.atlassian.net/browse/GEOS-10896) Missing NULL check in the template backwards mapping

* [GEOS-10899](https://osgeo-org.atlassian.net/browse/GEOS-10899) Features template escapes twice HTML produced outputs

* [GEOS-10912](https://osgeo-org.atlassian.net/browse/GEOS-10912) jms-cluster fails to clone grid coverage layer on other nodes

* [GEOS-10920](https://osgeo-org.atlassian.net/browse/GEOS-10920) Excel output format packaging misses dependencies, cannot produce .xls

* [GEOS-10921](https://osgeo-org.atlassian.net/browse/GEOS-10921) Double escaping of HTML with enabled features-templating

* [GEOS-10922](https://osgeo-org.atlassian.net/browse/GEOS-10922) Features templating exception on text/plain format

* [GEOS-10934](https://osgeo-org.atlassian.net/browse/GEOS-10934) CSW does not show title/abstract on welcome page

* [GEOS-10946](https://osgeo-org.atlassian.net/browse/GEOS-10946) WMS GetLegendGraphic throws FootprintsTransformation cannot be cast to ProcessFunction Exception

* [GEOS-10950](https://osgeo-org.atlassian.net/browse/GEOS-10950) Performance regression in DescribeFeatureType across all feature types

* [GEOS-10957](https://osgeo-org.atlassian.net/browse/GEOS-10957) Support ResourceAccessManager implementations returning custom subclasess of AccessLimits

Improvement:

* [GEOS-10858](https://osgeo-org.atlassian.net/browse/GEOS-10858) jdbc-config turns off isolated workspace support

* [GEOS-10867](https://osgeo-org.atlassian.net/browse/GEOS-10867) Bump commons-fileupload from 1.4 to 1.5

* [GEOS-10870](https://osgeo-org.atlassian.net/browse/GEOS-10870) Allow importer AttributesToPointGeometryTransform to preserve original geometries, and to configure the name of the target geometry

* [GEOS-10873](https://osgeo-org.atlassian.net/browse/GEOS-10873) Upgrade XStream to 1.4.20

* [GEOS-10898](https://osgeo-org.atlassian.net/browse/GEOS-10898) Preserve key order in STAC responses coming from JSONB columns

* [GEOS-10923](https://osgeo-org.atlassian.net/browse/GEOS-10923) Use default writing params on GeoTIFFPPIO

New Feature:

* [GEOS-10868](https://osgeo-org.atlassian.net/browse/GEOS-10868) Add support for editable description in GeoServer customize feature type table

Task:

* [GEOS-10863](https://osgeo-org.atlassian.net/browse/GEOS-10863) Update Oracle JDBC driver to 19.18.0.0

* [GEOS-10894](https://osgeo-org.atlassian.net/browse/GEOS-10894) Random control-flow errors on Mac builds

* [GEOS-10904](https://osgeo-org.atlassian.net/browse/GEOS-10904) Bump jettison from 1.5.3 to 1.5.4

For complete information see [2.22.3 release 
notes](https://github.com/geoserver/geoserver/releases/tag/2.22.3).

## About GeoServer 2.22

Additional information on GeoServer 2.22 series:

* [Update Instructions](https://docs.geoserver.org/latest/en/user/installation/upgrade.html)
* [Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/metadata/index.html)
* [CSW ISO Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/csw-iso/index.html)
* [State of GeoServer](https://docs.google.com/presentation/d/1mnOFSvYb8npVudvUR5MSjSTFHc6ZQ_bStafZrBV7LZ8/edit?usp=sharing) (FOSS4G Presentation)
* [GeoServer Beginner Workshop](https://docs.google.com/presentation/d/1fbPLN-1Cs95WK-IxDG1PxCEKyHwFbNBGNkkomxmLr0Y/edit?usp=sharing) (FOSS4G Workshop)
* [Welcome page](https://docs.geoserver.org/latest/en/user/webadmin/welcome.html) (User Guide)

Release notes:
( [2.22.3](https://github.com/geoserver/geoserver/releases/tag/2.22.3)
| [2.22.2](https://github.com/geoserver/geoserver/releases/tag/2.22.2)
| [2.22.1](https://github.com/geoserver/geoserver/releases/tag/2.22.1)
| [2.22.0](https://github.com/geoserver/geoserver/releases/tag/2.22.0)
| [2.22-RC](https://github.com/geoserver/geoserver/releases/tag/2.22-RC)
| [2.22-M0](https://github.com/geoserver/geoserver/releases/tag/2.22-M0)
)
