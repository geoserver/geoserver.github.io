---
author: Peter Smythe
date: 2023-08-30
layout: post
title: GeoServer 2.22.5 Release
categories:
- Announcements
tags:
- Release
release: release_222
version: 2.22.5
jira_version: 16895
--- 

GeoServer [2.22.5](/release/2.22.5/) release is now available
with downloads (
[bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.5/geoserver-2.22.5-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.5/geoserver-2.22.5-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.5/GeoServer-2.22.5-winsetup.exe/download))
, along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.5/geoserver-2.22.5-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.5/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.
GeoServer 2.22.5 is made in conjunction with GeoTools 28.5, and GeoWebCache 1.22.5. 

Thanks to Peter Smythe (AfriGIS) for making this release.

**2023-09-05 update:** GeoServer 2.22.5 has been recompiled and uploaded to SourceForge. The initial upload was accidentally compiled with Java 11 and would not function in a Java 8 environment. 

Thanks to Jody Garnett (GeoCat) for this update, and Steve Ikeoka for testing in a Java 8 environment.

## Java 8 End-of-life

This GeoServer 2.22.5 maintenance release is final scheduled release of GeoServer 2.22.x series, and thus the last providing Java 8 support.

All future releases will require a minimum of Java 11.

## Release notes

Improvement:

* [GEOS-10856](https://osgeo-org.atlassian.net//browse/GEOS-10856) geoserver monitor plugin - scaling troubles
* [GEOS-11048](https://osgeo-org.atlassian.net//browse/GEOS-11048) Improve URL checking
* [GEOS-11081](https://osgeo-org.atlassian.net//browse/GEOS-11081) Add option to disable GetFeatureInfo transforming raster layers
* [GEOS-11099](https://osgeo-org.atlassian.net//browse/GEOS-11099) ElasticSearch DataStore Documentation Update for RESPONSE_BUFFER_LIMIT
* [GEOS-11100](https://osgeo-org.atlassian.net//browse/GEOS-11100) Add opacity parameter to the layer definitions in WPS-Download download maps

Bug:

* [GEOS-10874](https://osgeo-org.atlassian.net//browse/GEOS-10874) Log4J: Windows binary zip release file with log4j-1.2.14.jar
* [GEOS-10875](https://osgeo-org.atlassian.net//browse/GEOS-10875) Disk Quota JDBC password shown in plaintext 
* [GEOS-10901](https://osgeo-org.atlassian.net//browse/GEOS-10901) GetCapabilities lists the same style multiple times when used as both a default and alternate style
* [GEOS-10903](https://osgeo-org.atlassian.net//browse/GEOS-10903) WMS filtering with Filter 2.0 fails
* [GEOS-10932](https://osgeo-org.atlassian.net//browse/GEOS-10932) csw-iso: should only add 'xsi:nil = false' attribute
* [GEOS-11025](https://osgeo-org.atlassian.net//browse/GEOS-11025) projection parameter takes no effect on MongoDB Schemaless features WFS requests
* [GEOS-11035](https://osgeo-org.atlassian.net//browse/GEOS-11035) Enabling OSEO from Workspace Edit Page Results in an NPE
* [GEOS-11054](https://osgeo-org.atlassian.net//browse/GEOS-11054) NullPointerException creating layer with REST, along with attribute list
* [GEOS-11055](https://osgeo-org.atlassian.net//browse/GEOS-11055) Multiple layers against the same ES document type conflict with each other
* [GEOS-11069](https://osgeo-org.atlassian.net//browse/GEOS-11069) Layer configuration page doesn't work for broken SQL views

Task:

* [GEOS-11062](https://osgeo-org.atlassian.net//browse/GEOS-11062)  Upgrade httpclient from 4.5.13 to 4.5.14
* [GEOS-11063](https://osgeo-org.atlassian.net//browse/GEOS-11063) Upgrade httpcore from 4.4.10 to 4.4.16
* [GEOS-11067](https://osgeo-org.atlassian.net//browse/GEOS-11067) Upgrade wiremock to 2.35.0
* [GEOS-11092](https://osgeo-org.atlassian.net//browse/GEOS-11092) acme-ldap.jar is compiled with Java 8

For the complete list see [2.22.5](https://github.com/geoserver/geoserver/releases/tag/2.22.5) release notes. 

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
( [2.22.5](https://github.com/geoserver/geoserver/releases/tag/2.22.5)
| [2.22.4](https://github.com/geoserver/geoserver/releases/tag/2.22.4)
| [2.22.3](https://github.com/geoserver/geoserver/releases/tag/2.22.3)
| [2.22.2](https://github.com/geoserver/geoserver/releases/tag/2.22.2)
| [2.22.1](https://github.com/geoserver/geoserver/releases/tag/2.22.1)
| [2.22.0](https://github.com/geoserver/geoserver/releases/tag/2.22.0)
| [2.22-RC](https://github.com/geoserver/geoserver/releases/tag/2.22-RC)
| [2.22-M0](https://github.com/geoserver/geoserver/releases/tag/2.22-M0)
) 

