---
author: David Blasby
date: 2004-12-16
layout: post
link: http://docs.codehaus.org/display/GEOS/GeoServer+1.2.4
wayback: https://web.archive.org/web/20050404035249/http://docs.codehaus.org:80/display/GEOS/GeoServer+1.2.4
title: "GeoServer 1.2.4 Released"
categories:
- Announcements
---

GeoServer 1.2.4 has been released, check it out below.

----

Servlet Container Compatabilty:

- [x] Jetty

More GeoServer 1.2.4 links:

- [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.2.4/)

- [Release Notes](#release-notes)

Please add comments to this page for installation tips and tricks. You can edit this page to report back on additional servelt containers that work…

## Release notes

New Feature:

* [GEOS-195](https://osgeo-org.atlassian.net/browse/GEOS-195) Support GML as a return type for GetFeatureInfo

Improvement:

* [GEOS-126](https://osgeo-org.atlassian.net/browse/GEOS-126) GeoServer Documentation improvements
* [GEOS-161](https://osgeo-org.atlassian.net/browse/GEOS-161) Improving build process
* [GEOS-262](https://osgeo-org.atlassian.net/browse/GEOS-262) SLD Min/MaxScaleDenominator

Bug:

* [GEOS-221](https://osgeo-org.atlassian.net/browse/GEOS-221) adding shapefile fetature type problem
* [GEOS-231](https://osgeo-org.atlassian.net/browse/GEOS-231) SRS as XML option does not persist
* [GEOS-232](https://osgeo-org.atlassian.net/browse/GEOS-232) Intersects on Oracle is not working correctly
* [GEOS-253](https://osgeo-org.atlassian.net/browse/GEOS-253) schema.xml present does not return properly, is instead always generated
* [GEOS-254](https://osgeo-org.atlassian.net/browse/GEOS-254) WFS Dispatcher mangles character encoding
* [GEOS-255](https://osgeo-org.atlassian.net/browse/GEOS-255) kvp featureid requests with a decimal in their name fail
* [GEOS-256](https://osgeo-org.atlassian.net/browse/GEOS-256) GetFeatureInfo can return incorrect i18n strings
* [GEOS-291](https://osgeo-org.atlassian.net/browse/GEOS-291) Fails at compiling. org.vfny.geoserver.global.ConfigurationException: there is no namespace defined for datatasore 'biz'

Task:

* [GEOS-91](https://osgeo-org.atlassian.net/browse/GEOS-91) Replace use of XMLEncoder.encode( Filter )
