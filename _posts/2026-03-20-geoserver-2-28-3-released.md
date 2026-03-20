---
author: Andrea Aime
date: 2026-03-20
layout: post
title: GeoServer 2.28.3 Release
categories:
- Announcements
tags:
- Release
release: release_228
version: 2.28.3
jira_version: 17769
--- 

GeoServer [2.28.3](/release/2.28.3/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.3/geoserver-2.28.3-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.3/geoserver-2.28.3-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.3/GeoServer-2.28.3-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.3/geoserver-2.28.3-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.3/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.
GeoServer 2.28.3 is made in conjunction with GeoTools 34.3, and GeoWebCache 1.28.3. 

Thanks to Andrea Aime (GeoSolutions) for making this release. 

## Release notes

Improvement:

* [GEOS-11886](https://osgeo-org.atlassian.net/browse/GEOS-11886) Sort entries in all .properties files alphabetically
* [GEOS-12033](https://osgeo-org.atlassian.net/browse/GEOS-12033) Allow to configure custom CRS authorities and transformations
* [GEOS-12037](https://osgeo-org.atlassian.net/browse/GEOS-12037) Support Metatiling on MapBox Vectortiles

Bug:

* [GEOS-11964](https://osgeo-org.atlassian.net/browse/GEOS-11964) Metadata Bulk Operations: wicket error
* [GEOS-12038](https://osgeo-org.atlassian.net/browse/GEOS-12038) ModificationProxy.replaceCatalogInfo() precludes converting Filters to native query language
* [GEOS-12047](https://osgeo-org.atlassian.net/browse/GEOS-12047) Lock timeout and nested lock support in GeoServer
* [GEOS-12055](https://osgeo-org.atlassian.net/browse/GEOS-12055) GeoServerSecurityManager.reload() not clearing service caches
* [GEOS-12060](https://osgeo-org.atlassian.net/browse/GEOS-12060) REST API with PUT does not allow un un-set a field

Task:

* [GEOS-12027](https://osgeo-org.atlassian.net/browse/GEOS-12027) Removing not needed org.restlet.ext.fileupload dependency
* [GEOS-12028](https://osgeo-org.atlassian.net/browse/GEOS-12028) Update 'com.google.code.gson' dependency version
* [GEOS-12029](https://osgeo-org.atlassian.net/browse/GEOS-12029) Update 'com.google.protobuf' dependency version
* [GEOS-12049](https://osgeo-org.atlassian.net/browse/GEOS-12049) Remove GWC InMemory cache support

For the complete list see [2.28.3](https://github.com/geoserver/geoserver/releases/tag/2.28.3) release notes. 

## Community Updates

Community module development:

* [GEOS-11509](https://osgeo-org.atlassian.net/browse/GEOS-11509) OGC API 3D GeoVolumes community module
* [GEOS-12002](https://osgeo-org.atlassian.net/browse/GEOS-12002) hz-cluster: homepage pop-up fails
* [GEOS-12030](https://osgeo-org.atlassian.net/browse/GEOS-12030) Features templating xstream tags conflict with geofence
* [GEOS-12044](https://osgeo-org.atlassian.net/browse/GEOS-12044) STAC search endpoint should report invalid collection names as invalid parameters instead of internal errors
* [GEOS-12061](https://osgeo-org.atlassian.net/browse/GEOS-12061) New Community Module for PNG-WIND output format for wind datasets

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.28 Series

Additional information on GeoServer 2.28 series:

* [GeoServer 2.28 User Manual](https://docs.geoserver.org/2.28.x/en/user/)
* [GeoServer 2025 Q4 Developer Update]({% post_url 2025-10-14-developer-update %})* [Advertise and Enforce Attribute Restrictions](https://github.com/geoserver/geoserver/wiki/GSIP-234)

Release notes:
( [2.28.3](https://github.com/geoserver/geoserver/releases/tag/2.28.3)
| [2.28.2](https://github.com/geoserver/geoserver/releases/tag/2.28.2)
| [2.28.1](https://github.com/geoserver/geoserver/releases/tag/2.28.1)
| [2.28.0](https://github.com/geoserver/geoserver/releases/tag/2.28.0)
| [2.28-M0](https://github.com/geoserver/geoserver/releases/tag/2.28-M0)
) 

