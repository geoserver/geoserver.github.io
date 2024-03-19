---
author: Peter Smythe
date: 2023-06-19
layout: post
title: GeoServer 2.22.4 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_222
version: 2.22.4
jira_version: 16891
--- 

GeoServer [2.22.4](/release/2.22.4/) release is now available
with downloads (
[bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.4/geoserver-2.22.4-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.4/geoserver-2.22.4-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.4/GeoServer-2.22.4-winsetup.exe/download))
, along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.4/geoserver-2.22.4-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.4/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.

GeoServer 2.22.4 is made in conjunction with GeoTools 28.4. 


Thanks to Peter Smythe (AfriGIS) and Jody Garnett (GeoCat) for making this release. This is Peter's first time making a GeoServer release and we would like to thank him for volunteering.

## Release notes

New Feature:

* [GEOS-10949](https://osgeo-org.atlassian.net/browse/GEOS-10949) Control remote resources accessed by GeoServer

Improvement:

* [GEOS-10973](https://osgeo-org.atlassian.net/browse/GEOS-10973) DWITHIN delegation to mongoDB

Bug:

* [GEOS-8162](https://osgeo-org.atlassian.net/browse/GEOS-8162) CSV Data store does not support relative store paths
* [GEOS-10906](https://osgeo-org.atlassian.net/browse/GEOS-10906) Authentication not sent if connection pooling activated 
* [GEOS-10936](https://osgeo-org.atlassian.net/browse/GEOS-10936) YSLD and OGC API modules are incompatible
* [GEOS-10969](https://osgeo-org.atlassian.net/browse/GEOS-10969) Empty CQL_FILTER-parameter should be ignored
* [GEOS-10975](https://osgeo-org.atlassian.net/browse/GEOS-10975) JMS clustering reports error about ReferencedEnvelope type not being whitelisted in XStream
* [GEOS-10980](https://osgeo-org.atlassian.net/browse/GEOS-10980) CSS extension lacks ASM JARs as of 2.23.0, stops rendering layer when style references a file
* [GEOS-10981](https://osgeo-org.atlassian.net/browse/GEOS-10981) Slow CSW GetRecords requests with JDBC Configuration
* [GEOS-10993](https://osgeo-org.atlassian.net/browse/GEOS-10993) Disabled resources can cause incorrect CSW GetRecords response
* [GEOS-10994](https://osgeo-org.atlassian.net/browse/GEOS-10994) OOM due to too many dimensions when range requested
* [GEOS-10998](https://osgeo-org.atlassian.net/browse/GEOS-10998) LayerGroupContainmentCache is being rebuilt on each ApplicationEvent
* [GEOS-11015](https://osgeo-org.atlassian.net/browse/GEOS-11015) geopackage wfs output builds up tmp files over time
* [GEOS-11024](https://osgeo-org.atlassian.net/browse/GEOS-11024) metadata: add datetime field type to feature catalog

Task:

* [GEOS-10987](https://osgeo-org.atlassian.net/browse/GEOS-10987) Bump xalan:xalan and xalan:serializer from 2.7.2 to 2.7.3
* [GEOS-11008](https://osgeo-org.atlassian.net/browse/GEOS-11008)) Update sqlite-jdbc from 3.34.0 to 3.41.2.2
* [GEOS-11010](https://osgeo-org.atlassian.net/browse/GEOS-11010) Upgrade guava from 30.1 to 32.0.0
* [GEOS-11011](https://osgeo-org.atlassian.net/browse/GEOS-11011) Upgrade postgresql from 42.4.3 to 42.6.0
* [GEOS-11012](https://osgeo-org.atlassian.net/browse/GEOS-11012) Upgrade commons-collections4 from 4.2 to 4.4
* [GEOS-11018](https://osgeo-org.atlassian.net/browse/GEOS-11018) Upgrade commons-lang3 from 3.8.1 to 3.12.0
* [GEOS-11020](https://osgeo-org.atlassian.net/browse/GEOS-11020) Add test scope to mockito-core dependency

Sub-task:

* [GEOS-10989](https://osgeo-org.atlassian.net/browse/GEOS-10989) Update spring.version from 5.2.23.RELEASE to 5.2.24.RELEASE

For the complete list see [2.22.4](https://github.com/geoserver/geoserver/releases/tag/2.22.4) release notes. 

# About GeoServer 2.22 Series

Additional information on GeoServer 2.22 series:

* [GeoServer 2.22 User Manual](https://docs.geoserver.org/2.22.x/en/user/)
* [Update Instructions](https://docs.geoserver.org/latest/en/user/installation/upgrade.html)
* [Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/metadata/index.html)
* [CSW ISO Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/csw-iso/index.html)
* [State of GeoServer](https://docs.google.com/presentation/d/1mnOFSvYb8npVudvUR5MSjSTFHc6ZQ_bStafZrBV7LZ8/edit?usp=sharing) (FOSS4G Presentation)
* [GeoServer Beginner Workshop](https://docs.google.com/presentation/d/1fbPLN-1Cs95WK-IxDG1PxCEKyHwFbNBGNkkomxmLr0Y/edit?usp=sharing) (FOSS4G Workshop)
* [Welcome page](https://docs.geoserver.org/latest/en/user/webadmin/welcome.html) (User Guide)

Release notes:
( [2.22.4](https://github.com/geoserver/geoserver/releases/tag/2.22.4)
| [2.22.3](https://github.com/geoserver/geoserver/releases/tag/2.22.3)
| [2.22.2](https://github.com/geoserver/geoserver/releases/tag/2.22.2)
| [2.22.1](https://github.com/geoserver/geoserver/releases/tag/2.22.1)
| [2.22.0](https://github.com/geoserver/geoserver/releases/tag/2.22.0)
| [2.22-RC](https://github.com/geoserver/geoserver/releases/tag/2.22-RC)
| [2.22-M0](https://github.com/geoserver/geoserver/releases/tag/2.22-M0)
) 

