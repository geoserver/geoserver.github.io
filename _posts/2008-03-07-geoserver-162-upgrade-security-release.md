---
author: Chris Holmes
comments: true
date: 2008-03-07 20:16:24+00:00
layout: post
link: http://blog.geoserver.org/2008/03/07/geoserver-162-upgrade-security-release/
slug: geoserver-162-upgrade-security-release
title: 'GeoServer 1.6.2 upgrade: security release'
wordpress_id: 90
categories:
- Announcements
---

GeoServer 1.6.2 is now available for download here. This is a **Security Release**, which means it contains [fixes](#release-notes) for two Security Vulnerabilities.   We highly recommend that you upgrade to this version.  We found out about both these vulnerabilities in the past couple days, and made an effort to fix them and get this release out as quickly as possible.  One of the issues also affects older versions of GeoServer.  We are not doing a security release for it at this time for all the older versions, but have [clear instructions](https://web.archive.org/web/20080307/http://geoserver.org/display/GEOS/Security+issue+-+Disable+demoRequest) on how to update one file to disable the page where the exploit is possible.  We highly recommend that any production instances of GeoServer follow this, it should be easier to do than a full upgrade.

----

GeoServer 1.6.2 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.2/)

\* [Release Notes](#release-notes)\
\* [Change Log](#release-notes)\
\* [geoserver-1.6.2a.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.2/geoserver-1.6.2a.exe/download) (Win32 self-installing executable)\
\* [geoserver-1.6.2a-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.2/geoserver-1.6.2a-bin.zip/download) (UNIX binary)\
\* [geoserver-1.6.2a-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.2/geoserver-1.6.2a-src.zip/download) (Source code)\
\* [geoserver-1.6.2a-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.2/geoserver-1.6.2a-war.zip/download) (Web archive)\
\* [geoserver-1.6.2-doc.zip](http://downloads.sourceforge.net/geoserver/geoserver-1.6.1-doc.zip) (Documentation)\
\* [geoserver-1.6.2a-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.2/geoserver-1.6.2a-javadoc.zip/download) (Java Documentation)

[Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.2/extensions/)

#### Service Extensions

\* [Versioning WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.2/extensions/geoserver-1.6.2-wfsv-plugin.zip/download)

#### DataStore Extensions (described in [DataStore Config](http://docs.codehaus.org/display/GEOSDOC/2+DataStore+Config))

#### 

\* [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.2/extensions/geoserver-1.6.2-arcsde-plugin.zip/download)\
\* [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.2/extensions/geoserver-1.6.2-gml-plugin.zip/download)\
\* [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.2/extensions/geoserver-1.6.2-db2-plugin.zip/download)\
\* [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.2/extensions/geoserver-1.6.2-mysql-plugin.zip/download)\
\* [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.2/extensions/geoserver-1.6.2-vpf-plugin.zip/download)\
\* [WFS](http://downloads.sourceforge.net/geoserver/geoserver-1.6.2-wfs-plugin.zip)\
\* [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.6.2/extensions/geoserver-1.6.2-oracle-plugin.zip/download)

#### Coverage Extensions (described in [Image Pyramid](http://docs.codehaus.org/display/GEOSDOC/Image+Pyramid))

#### 

\* [Image Pyramid](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6.2/geoserver-1.6.2-pyramid-plugin.zip/download)

\|\| Jetty \|\| Tomcat \|\|\
\|\| ✓ \|\| ✓ \|\|

## Release notes

Bug:

* [GEOS-1785](https://osgeo-org.atlassian.net/browse/GEOS-1785) Data dir included in the .war distribution is wide open for the world to see...
* [GEOS-1792](https://osgeo-org.atlassian.net/browse/GEOS-1792) Security issue demoRequest (web interface)
* [GEOS-1806](https://osgeo-org.atlassian.net/browse/GEOS-1806) Image Pyramid extension archive contains no .jar files
