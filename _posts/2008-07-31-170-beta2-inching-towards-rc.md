---
author: bmmpxf
comments: true
date: 2008-07-31 15:11:26+00:00
layout: post
link: http://blog.geoserver.org/2008/07/31/170-beta2-inching-towards-rc/
slug: 170-beta2-inching-towards-rc
title: '1.7.0-beta2: Inching Towards RC'
wordpress_id: 116
categories:
- Announcements
---

The GeoServer team has been working full steam ahead on the new branch (1.7.x) of GeoServer.  With 1.7.0-beta2 released, [KML regionating](https://web.archive.org/web/20080731/http://geoserver.org/display/GEOS/GSIP+20+-+Automated+Regionating+in+KML+MapProducer) has been optimized.  Regionating is the process of automatically filtering what data is shown based on an attribute of that data (say, only showing large features when zoomed out).  Currently regionating is only functional for KML output, but this may eventually change.  Also, [per-layer security](https://web.archive.org/web/20080731/http://geoserver.org/display/GEOS/GSIP+19+-+Per+layer+security) has been added and enhanced, which people have been asking about on the mailing list for some time.  Per-layer security* will allow for layers to be viewable based on certain security credentials.  _*The development team is looking for a better, more succinct name than "per-layer security."  If you have an awesome name suggestion, [meet us in IRC](https://web.archive.org/web/20080731/http://geoserver.org/display/GEOSDOC/3+IRC) and tell us!

_This is still a beta, so bugs will occur.  Nevertheless, if you find one, [please let us know](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS).  Also, we still haven't abandoned the 1.6.x branch (the most recent stable version remains at [1.6.4](https://web.archive.org/web/20080731/http://geoserver.org/display/GEOS/GeoServer+1.6.4)), so if you're not looking for cutting edge (or if you're looking to run [GeoServer in a production environment](https://web.archive.org/web/20080731/http://geoserver.org/display/GEOSDOC/2.6+GeoServer+in+Production+Environment)), [1.6.4](https://web.archive.org/web/20080731/http://geoserver.org/display/GEOS/GeoServer+1.6.4) is the version you want.

We'll be unveiling some exciting news about the future of GeoServer fairly soon, so stay tuned!

----

#### GeoServer 1.7.0-beta2 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/).

Released on July 30, 2008.  SourceForge Release 616737.

- [Release Notes](#release-notes)
- [geoserver-1.7.0-beta2.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/geoserver-1.7.0-beta2.exe/download) (Win32 self-installing executable)
- [geoserver-1.7.0-beta2-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/geoserver-1.7.0-beta2-bin.zip/download) (UNIX binary)
- [geoserver-1.7.0-beta2-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/geoserver-1.7.0-beta2-src.zip/download) (Source code)
- [geoserver-1.7.0-beta2-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/geoserver-1.7.0-beta2-war.zip/download) (Web archive)
- [geoserver-1.7.0-beta2-doc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/geoserver-1.7.0-beta2-doc.zip/download) (Documentation export from geoserver.org)
- [geoserver-1.7.0-beta2-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/geoserver-1.7.0-beta2-javadoc.zip/download) (Java Documentation)

#### [Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/extensions/)

**DataStore Extensions**

- [GeoWebCache](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/extensions/geoserver-1.7.0-beta2-gwc-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/extensions/geoserver-1.7.0-beta2-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/extensions/geoserver-1.7.0-beta2-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/extensions/geoserver-1.7.0-beta2-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/extensions/geoserver-1.7.0-beta2-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/extensions/geoserver-1.7.0-beta2-vpf-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/extensions/geoserver-1.7.0-beta2-wfsv-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/extensions/geoserver-1.7.0-beta2-oracle-plugin.zip/download)

**Coverage Extensions**

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta2/extensions/geoserver-1.7.0-beta2-pyramid-plugin.zip/download)

## Release notes

Improvement:

* [GEOS-1582](https://osgeo-org.atlassian.net/browse/GEOS-1582) Implement VersionedFeatureCollection
* [GEOS-1610](https://osgeo-org.atlassian.net/browse/GEOS-1610) VersionedGML3OutputFormat not working on trunk
* [GEOS-1625](https://osgeo-org.atlassian.net/browse/GEOS-1625) Expose and test GeoRSS simple/gml output formats as well
* [GEOS-1969](https://osgeo-org.atlassian.net/browse/GEOS-1969) Implement GSIP 19, per layer security subsystem
* [GEOS-2033](https://osgeo-org.atlassian.net/browse/GEOS-2033) Map preview should protect itself from layer errors

Bug:

* [GEOS-1551](https://osgeo-org.atlassian.net/browse/GEOS-1551) GeoServerFactoryIteratorProvider causes NPE during coverage loading
* [GEOS-1660](https://osgeo-org.atlassian.net/browse/GEOS-1660) Feature bounds generation broken on trunk when geometry property is not included
* [GEOS-1695](https://osgeo-org.atlassian.net/browse/GEOS-1695) WCS 1.0 GetCoverage does not properly sets the content type
* [GEOS-1719](https://osgeo-org.atlassian.net/browse/GEOS-1719) Multiple KVP parsers for the same key will step on each other toes
* [GEOS-1821](https://osgeo-org.atlassian.net/browse/GEOS-1821) SLD filters broken
* [GEOS-1831](https://osgeo-org.atlassian.net/browse/GEOS-1831) make geoserver runnable in spring 2
* [GEOS-1893](https://osgeo-org.atlassian.net/browse/GEOS-1893) Required param missing in GetFeature, funny error back
* [GEOS-1936](https://osgeo-org.atlassian.net/browse/GEOS-1936) EXCEPTIONS=application/Fvnd.ogc.se_inimage is not respected
* [GEOS-1942](https://osgeo-org.atlassian.net/browse/GEOS-1942) WMS renders point layer incorrectly
* [GEOS-1948](https://osgeo-org.atlassian.net/browse/GEOS-1948) When an sld refers an external graphic that's not there, generated KML is invalid (unclosed elements)
* [GEOS-1955](https://osgeo-org.atlassian.net/browse/GEOS-1955) WFS-T demo broken in FF3 RC1 and IE 7
* [GEOS-1988](https://osgeo-org.atlassian.net/browse/GEOS-1988) RESTConfig does not compile with new configuration API
* [GEOS-1992](https://osgeo-org.atlassian.net/browse/GEOS-1992) rest/styles throws Exception on 1.6.x
* [GEOS-2002](https://osgeo-org.atlassian.net/browse/GEOS-2002) WCS 1.1 module cannot be built with tests disabled
* [GEOS-2005](https://osgeo-org.atlassian.net/browse/GEOS-2005) Dispatcher breaks on kvp parse when strict=true is used
* [GEOS-2007](https://osgeo-org.atlassian.net/browse/GEOS-2007) Specifying Inline Features in an SLD throws an exception
* [GEOS-2023](https://osgeo-org.atlassian.net/browse/GEOS-2023) KML regionating options are splitting into two the caching options
* [GEOS-2024](https://osgeo-org.atlassian.net/browse/GEOS-2024) Caching headers issues
* [GEOS-2026](https://osgeo-org.atlassian.net/browse/GEOS-2026) Locking code can still leak connections
* [GEOS-2031](https://osgeo-org.atlassian.net/browse/GEOS-2031) WMS capabilities report an inexistent style for layer groups
* [GEOS-2040](https://osgeo-org.atlassian.net/browse/GEOS-2040) AbstractFeatureInfoResponse: WmsException may occurs if Bulsa Parameters are missing when evaluating a coverage providing a point in different CRS (with respect to the one of the coverage itself).
* [GEOS-2042](https://osgeo-org.atlassian.net/browse/GEOS-2042) Labels are always centered, the label point does not take into account the visible part of the polygon
* [GEOS-2043](https://osgeo-org.atlassian.net/browse/GEOS-2043) LegacyCatalogImporter NPE's when presented with a missing FeatureTypes directory
* [GEOS-2046](https://osgeo-org.atlassian.net/browse/GEOS-2046) SLD filters aren't applied on KML output when reprojection is needed
* [GEOS-2052](https://osgeo-org.atlassian.net/browse/GEOS-2052) Can't disable caching and remove the caching time (in feature type configuration)
* [GEOS-2057](https://osgeo-org.atlassian.net/browse/GEOS-2057) WMS raster interpolation settings are ignored
* [GEOS-2058](https://osgeo-org.atlassian.net/browse/GEOS-2058) Coverages do disappear from the catalog after "apply" is pressed
* [GEOS-2060](https://osgeo-org.atlassian.net/browse/GEOS-2060) WMS rendering options are not honored on apply, only on save

Sub-task:

* [GEOS-1665](https://osgeo-org.atlassian.net/browse/GEOS-1665) Move kvp parsers into a different package so that they won't conflict with the wcs 1.0 ones (and then use the same naming convetions)
* [GEOS-1692](https://osgeo-org.atlassian.net/browse/GEOS-1692) Add support for store=true
