---
author: Justin Deoliveira
date: 2007-02-19
layout: post
link: http://docs.codehaus.org/display/GEOS/GeoServer+1.6-alpha2
wayback: https://web.archive.org/web/20071222214110/http://docs.codehaus.org:80/display/GEOS/GeoServer+1.6-alpha2
title: "GeoServer 1.6-alpha2 Released"
categories:
- Announcements
---

GeoServer 1.6-alpha2 has been released, check it out below.

----

GeoServer 1.6-alpha2 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6-alpha/):

- [Release Notes](#release-notes)
- [geoserver-1.6-alpha2.exe](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6-alpha/geoserver-1.6-alpha2.exe/download)
- [geoserver-1.6-alpha2-bin.zip](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6-alpha/geoserver-1.6-alpha2-bin.zip/download)
- [geoserver-1.6-alpha2-war.zip](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6-alpha/geoserver-1.6-alpha2-war.zip/download)

Tested with: Jetty, Tomcat

#### DataStore Extensions

- [Extensions download page](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6-alpha2/)
- [GML datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6-alpha2/geoserver-1.6-alpha2-gml-plugin.zip/download)
- [DB2 datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6-alpha2/geoserver-1.6-alpha2-db2-plugin.zip/download)
- [MySQL datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6-alpha2/geoserver-1.6-alpha2-mysql-plugin.zip/download)
- [VPF datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6-alpha2/geoserver-1.6-alpha2-vpf-plugin.zip/download)
- [WFS datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6-alpha2/geoserver-1.6-alpha2-wfs-plugin.zip/download)
- [Oracle datastore](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6-alpha2/geoserver-1.6-alpha2-oracle-plugin.zip/download)

## Release notes

New Feature:

* [GEOS-288](https://osgeo-org.atlassian.net/browse/GEOS-288) Support new SortBy Query element

Improvement:

* [GEOS-739](https://osgeo-org.atlassian.net/browse/GEOS-739) WFS 1.1 GetLock operation
* [GEOS-756](https://osgeo-org.atlassian.net/browse/GEOS-756) KvpParser subclasses should end with Parser, not Reader
* [GEOS-768](https://osgeo-org.atlassian.net/browse/GEOS-768) Run http tests in a profile
* [GEOS-780](https://osgeo-org.atlassian.net/browse/GEOS-780) Dispatcher should try hard not to use temp files at all...
* [GEOS-869](https://osgeo-org.atlassian.net/browse/GEOS-869) Build should not open popup windows
* [GEOS-896](https://osgeo-org.atlassian.net/browse/GEOS-896) Have GeoServerDataDirectory use the GeoServerResourceLoader from the container

Bug:

* [GEOS-659](https://osgeo-org.atlassian.net/browse/GEOS-659) GeoServer throws an exception when a LockFeature request does not include a Filter
* [GEOS-887](https://osgeo-org.atlassian.net/browse/GEOS-887) ows:Exception report references remote schema from schemas.opengis.net, should reference the local server
* [GEOS-891](https://osgeo-org.atlassian.net/browse/GEOS-891) ows dispatcher needs to support output strategies
* [GEOS-892](https://osgeo-org.atlassian.net/browse/GEOS-892) Have dispatcher handles cases where request specified in context
* [GEOS-905](https://osgeo-org.atlassian.net/browse/GEOS-905) schemaLocation in gml3 output missing '&service=WFS' for application schema

Task:

* [GEOS-683](https://osgeo-org.atlassian.net/browse/GEOS-683) Filter 1.1 XML Bindings
* [GEOS-684](https://osgeo-org.atlassian.net/browse/GEOS-684) GML 3.1.1 XML Bindings
* [GEOS-685](https://osgeo-org.atlassian.net/browse/GEOS-685) GetCapabilities Operation
* [GEOS-686](https://osgeo-org.atlassian.net/browse/GEOS-686) DescribeFeatureType Operation
* [GEOS-687](https://osgeo-org.atlassian.net/browse/GEOS-687) GetFeature Operation
* [GEOS-688](https://osgeo-org.atlassian.net/browse/GEOS-688) GetFeatureWithLock Operation
* [GEOS-689](https://osgeo-org.atlassian.net/browse/GEOS-689) Transaction Insert Operation
* [GEOS-690](https://osgeo-org.atlassian.net/browse/GEOS-690) Transaction Update Operation
* [GEOS-691](https://osgeo-org.atlassian.net/browse/GEOS-691) Transaction Delete Operation
* [GEOS-698](https://osgeo-org.atlassian.net/browse/GEOS-698) Capabiltiies Version Negotiation
* [GEOS-890](https://osgeo-org.atlassian.net/browse/GEOS-890) Replicate xml encoding logic from old dispatch system

Sub-task:

* [GEOS-564](https://osgeo-org.atlassian.net/browse/GEOS-564) GML 3.1.1  support in Filter
* [GEOS-696](https://osgeo-org.atlassian.net/browse/GEOS-696) Refactor 1.0.0 DescribeFeatureType code
* [GEOS-697](https://osgeo-org.atlassian.net/browse/GEOS-697) Refactor 1.0.0 GetFeature code
* [GEOS-700](https://osgeo-org.atlassian.net/browse/GEOS-700) GML 3.1.1 Feature Producer
* [GEOS-701](https://osgeo-org.atlassian.net/browse/GEOS-701) Geotools SortBy Support
* [GEOS-702](https://osgeo-org.atlassian.net/browse/GEOS-702) Reprojection Support
* [GEOS-703](https://osgeo-org.atlassian.net/browse/GEOS-703) Hits Results Type
