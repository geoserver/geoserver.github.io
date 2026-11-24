---
author: bmmpxf
comments: true
date: 2008-04-01 20:58:45+00:00
layout: post
link: http://blog.geoserver.org/2008/04/01/geoserver-170-alpha1/
slug: geoserver-170-alpha1
title: GeoServer 1.7.0-alpha1
wordpress_id: 98
categories:
- Announcements
---

Development pushes ever on here, and I'd like to mention that the very first build of the 1.7.x branch has been released.  1.7.0-alpha1 is very much an alpha release, with the usual applicable caveats.  The major developments are Xlink support for WFS 1.1 and a full implementation of WCS 1.1.1.  This release is based on GeoTools 2.5.x.

GeoTools 2.5.x contains the new feature model, which should be able to handle the full complexity of GML and any other model that architects may throw at us.  There is still a lot of work to fully incorporate it in to GeoServer, but this alpha release does represent the first step forward towards that goal.

You can get 1.7.0-alpha1 on the [Latest](https://web.archive.org/web/20080401/http://geoserver.org/display/GEOS/Latest) download page, while 1.6.2 is still available on the [Stable](https://web.archive.org/web/20080401/http://geoserver.org/display/GEOS/Stable) page.

----

#### GeoServer 1.7.0-alpha1 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/).

SourceForge Release 588476

- [Release Notes](http://sourceforge.net/project/shownotes.php?release_id=588476&group_id=25086)
- [geoserver-1.7.0-alpha1.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/geoserver-1.7.0-alpha1.exe/download) (Win32 self-installing executable)
- [geoserver-1.7.0-alpha1-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/geoserver-1.7.0-alpha1-bin.zip/download) (UNIX binary)
- [geoserver-1.7.0-alpha1-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/geoserver-1.7.0-alpha1-src.zip/download) (Source code)
- [geoserver-1.7.0-alpha1-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/geoserver-1.7.0-alpha1-war.zip/download) (Web archive)
- [geoserver-1.7.0-alpha1-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/geoserver-1.7.0-alpha1-doc.zip/download) (Documentation)
- [geoserver-1.7.0-alpha1-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/geoserver-1.7.0-alpha1-javadoc.zip/download) (Java Documentation)
- [Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/extensions/)

#### DataStore Extensions

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/extensions/geoserver-1.7.0-alpha1-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/extensions/geoserver-1.7.0-alpha1-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/extensions/geoserver-1.7.0-alpha1-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/extensions/geoserver-1.7.0-alpha1-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/extensions/geoserver-1.7.0-alpha1-vpf-plugin.zip/download)
- [WFS](http://downloads.sourceforge.net/geoserver/geoserver-1.7.0-alpha1-wfs-plugin.zip)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/extensions/geoserver-1.7.0-alpha1-oracle-plugin.zip/download)

#### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-alpha1/extensions/geoserver-1.7.0-alpha1-pyramid-plugin.zip/download)

Tested with: Jetty, Tomcat
