---
author: David Blasby
date: 2005-06-08
layout: post
link: http://docs.codehaus.org/display/GEOS/GeoServer+1.3.0-RC1
wayback: https://web.archive.org/web/20060624094916/http://docs.codehaus.org:80/display/GEOS/GeoServer+1.3.0-RC1
title: "GeoServer 1.3.0-RC1 Released"
categories:
- Announcements
---

GeoServer 1.3.0-RC1 has been released, check it out below.

----

Servlet Container Compatabilty:

- [x] Jetty
- [x] Tomcat
- Others - currently untested

More GeoServer 1.3.0-RC1 links:

- [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC1/)
- [Release Notes](#release-notes)

Please add comments to this page for installation tips and tricks. You can edit this page to report back on additional servelt containers that work...

## Release notes

Improvement:

* [GEOS-250](https://osgeo-org.atlassian.net/browse/GEOS-250) MaxScale and MinScale about layer
* [GEOS-294](https://osgeo-org.atlassian.net/browse/GEOS-294) Validation for .sld file needed.

Bug:

* [GEOS-293](https://osgeo-org.atlassian.net/browse/GEOS-293) A style gets removed after updating it with an invalid .sld file.
* [GEOS-298](https://osgeo-org.atlassian.net/browse/GEOS-298) The sld filter parser is broken
* [GEOS-328](https://osgeo-org.atlassian.net/browse/GEOS-328) Multiple levels of logic operators
* [GEOS-330](https://osgeo-org.atlassian.net/browse/GEOS-330) sld with same file name (uploader)
* [GEOS-332](https://osgeo-org.atlassian.net/browse/GEOS-332) postgis & sld
* [GEOS-334](https://osgeo-org.atlassian.net/browse/GEOS-334) Geoserver does not recognize SVG validated using XMLSpy
* [GEOS-350](https://osgeo-org.atlassian.net/browse/GEOS-350) WMSMapContext leaks memory
* [GEOS-352](https://osgeo-org.atlassian.net/browse/GEOS-352) Filter_Capabilities in WFS GetCapabilties not accurate
* [GEOS-3929](https://osgeo-org.atlassian.net/browse/GEOS-3929) CLONE -postgis & sld

Task:

* [GEOS-339](https://osgeo-org.atlassian.net/browse/GEOS-339) Roll forward document improvements
