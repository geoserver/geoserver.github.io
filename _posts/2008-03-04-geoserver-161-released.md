---
author: bmmpxf
comments: true
date: 2008-03-04 20:22:19+00:00
layout: post
link: http://blog.geoserver.org/2008/03/04/geoserver-161-released/
slug: geoserver-161-released
title: GeoServer 1.6.1 Released!
wordpress_id: 89
categories:
- Announcements
---

The GeoServer team announces the release of GeoServer version 1.6.1!  Here are some of the highlights in this release:

GeoServer now supports FeatureType aliases, which allows for the creating of friendly names for unwieldy FeatureTypes.  Also, support has been added for limiting (per FeatureType) the maximum number of features that can be requested by a client, thus easing server load.  (Thanks to [Landgate](http://www.landgate.wa.gov.au) for funding both of the above!). Cédric Briançon from [Geomatys](http://geomatys.fr) contributed the GetFeatureInfo operation on WMS coverage data, and GeoServer can now output PDFs from raster as well as vector data.  Saul Farber of [MassGIS](http://www.mass.gov/mgis) added support for UpdateSequence, which returns a “revision number” of the capabilities of the service; this gives clients more efficient access to the Capabilities document.  Also, there have been improvements in MySQL integration: The Java connector was updated, performance was improved, and GeoServer is now using the more-efficient Well Known Binary protocol.

In total, this new release contains over 40 patches and improvements since 1.6.0.  (You can view the [changelog](#release-notes)  for details.  You can download this latest version from geoserver.org.  As usual, we thank everyone who has tested out the software and reported issues.  Please continue to submit bug reports using our [bug tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS).

----

GeoServer 1.6.1 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6.1/). SourceForge Release 580717

- [Release Notes](#release-notes)
- [geoserver-1.6.1.exe](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6.1/geoserver-1.6.1.exe/download)
- [geoserver-1.6.1-bin.zip](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6.1/geoserver-1.6.1-bin.zip/download)
- [geoserver-1.6.1-src.zip](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6.1/geoserver-1.6.1-src.zip/download)
- [geoserver-1.6.1-war.zip](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6.1/geoserver-1.6.1-war.zip/download)
- [geoserver-1.6.1-doc.zip](http://downloads.sourceforge.net/geoserver/geoserver-1.6.1-doc.zip)
- [geoserver-1.6.1-javadoc.zip](https://sourceforge.net/projects/geoserver/files/OldFiles/1.6.1/geoserver-1.6.1-javadoc.zip/download)

[Extensions download page](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6.1/)

#### Service Extensions

- [Versioning WFS](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6.1/geoserver-1.6.1-wfsv-plugin.zip/download)

#### DataStore Extensions

- [ArcSDE](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6.1/geoserver-1.6.1-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6.1/geoserver-1.6.1-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6.1/geoserver-1.6.1-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6.1/geoserver-1.6.1-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6.1/geoserver-1.6.1-vpf-plugin.zip/download)
- [WFS](http://downloads.sourceforge.net/geoserver/geoserver-1.6.1-wfs-plugin.zip)
- [Oracle](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6.1/geoserver-1.6.1-oracle-plugin.zip/download)

#### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/OldFiles/extensions/1.6.1/geoserver-1.6.1-pyramid-plugin.zip/download)

Tested with: Jetty, Tomcat

## Release notes

New Feature:

* [GEOS-1422](https://osgeo-org.atlassian.net/browse/GEOS-1422) GetFeatureInfo for raster

Improvement:

* [GEOS-235](https://osgeo-org.atlassian.net/browse/GEOS-235) Add proper support for UPDATESEQUENCE
* [GEOS-779](https://osgeo-org.atlassian.net/browse/GEOS-779) Support feature type aliases
* [GEOS-1461](https://osgeo-org.atlassian.net/browse/GEOS-1461) Workaround black raster generation in PDF
* [GEOS-1644](https://osgeo-org.atlassian.net/browse/GEOS-1644) Disable the clibpngimagereader by default
* [GEOS-1646](https://osgeo-org.atlassian.net/browse/GEOS-1646) Implement into MySql the same perf improvements found in Postgis
* [GEOS-1659](https://osgeo-org.atlassian.net/browse/GEOS-1659) WFS Maxfeatures refinement
* [GEOS-1698](https://osgeo-org.atlassian.net/browse/GEOS-1698) Upgrade of MySQL JDBC Driver
* [GEOS-1724](https://osgeo-org.atlassian.net/browse/GEOS-1724) resultType hits and maxFeatures limit
* [GEOS-1729](https://osgeo-org.atlassian.net/browse/GEOS-1729) Deprecate Mercator1SPGoogle, geotools can do without it now
* [GEOS-1748](https://osgeo-org.atlassian.net/browse/GEOS-1748) Geoserver unit tests should use partial buffering strategy instead of full buffer one
* [GEOS-1758](https://osgeo-org.atlassian.net/browse/GEOS-1758) Install and attach source jars
* [GEOS-1771](https://osgeo-org.atlassian.net/browse/GEOS-1771) Relax WKT generation checks in WMS GetCapabilities generation

Bug:

* [GEOS-1482](https://osgeo-org.atlassian.net/browse/GEOS-1482) Mock testing leaves temp directories behind, they eventually break the build on Windows
* [GEOS-1489](https://osgeo-org.atlassian.net/browse/GEOS-1489) Geoserver returns more than maxFeatures if more than 1 layer is requested in WFS request
* [GEOS-1544](https://osgeo-org.atlassian.net/browse/GEOS-1544) Avoid reporting a missing layer message when in fact the layer is there
* [GEOS-1545](https://osgeo-org.atlassian.net/browse/GEOS-1545) Unit testing must use its own logging configuration
* [GEOS-1680](https://osgeo-org.atlassian.net/browse/GEOS-1680) Six times slowdown in the application of big filters
* [GEOS-1683](https://osgeo-org.atlassian.net/browse/GEOS-1683) OpenLayers output format does not correctly encode string attributes in CQL filters
* [GEOS-1687](https://osgeo-org.atlassian.net/browse/GEOS-1687) KVP parsing can NPE depending on the container if an empty parameter is used
* [GEOS-1690](https://osgeo-org.atlassian.net/browse/GEOS-1690) GeoServerExtensions caching breaks prototype contract of some beans
* [GEOS-1696](https://osgeo-org.atlassian.net/browse/GEOS-1696) wms reflector does not work with pure remote slds
* [GEOS-1725](https://osgeo-org.atlassian.net/browse/GEOS-1725) KML has unclosed Style
* [GEOS-1735](https://osgeo-org.atlassian.net/browse/GEOS-1735) GeoServer should accept coverage store names with leading numerals
* [GEOS-1736](https://osgeo-org.atlassian.net/browse/GEOS-1736) Coverage store naming error should include underscore and hyphen in list of acceptable characters
* [GEOS-1738](https://osgeo-org.atlassian.net/browse/GEOS-1738) Ampersand in format description in catalog.xml causes failure to start geoserver
* [GEOS-1740](https://osgeo-org.atlassian.net/browse/GEOS-1740) WMS Reprojection won't work when the original data does not have an SRS at all
* [GEOS-1745](https://osgeo-org.atlassian.net/browse/GEOS-1745) kvp parser does not handle parantheses when single filter specified
* [GEOS-1747](https://osgeo-org.atlassian.net/browse/GEOS-1747) PartialBufferOutputStream2 flush issues (CVE-2008-7227)
* [GEOS-1752](https://osgeo-org.atlassian.net/browse/GEOS-1752) GetFeatureInfo does not work on layer whose srs was reprojected at the configuration level
* [GEOS-1753](https://osgeo-org.atlassian.net/browse/GEOS-1753) application/openlayers format creates GetFeatureInfo request with both upper and lowercase parameters
* [GEOS-1754](https://osgeo-org.atlassian.net/browse/GEOS-1754) Avoid NPE when GEOSERVER_DATA_DIR points to an empty directory
* [GEOS-1759](https://osgeo-org.atlassian.net/browse/GEOS-1759) Fix gs.version in top-level POM
* [GEOS-1763](https://osgeo-org.atlassian.net/browse/GEOS-1763) kvp tokenization fails with certain delimter strings
* [GEOS-1764](https://osgeo-org.atlassian.net/browse/GEOS-1764) GetMapResponse finalizer might throw an NPE
* [GEOS-1770](https://osgeo-org.atlassian.net/browse/GEOS-1770) More checks before allowing style deletion
* [GEOS-1772](https://osgeo-org.atlassian.net/browse/GEOS-1772) Secondary styles cannot be removed completely
* [GEOS-1776](https://osgeo-org.atlassian.net/browse/GEOS-1776) Handle "...&updateSequence=&..." as if UpdateSequence wasn't provided
* [GEOS-1777](https://osgeo-org.atlassian.net/browse/GEOS-1777) WCS updatesequence support reports exceptions codes in the locator (instead it should be using "code")

Task:

* [GEOS-1778](https://osgeo-org.atlassian.net/browse/GEOS-1778) update user map link on geoserver front page

Sub-task:

* [GEOS-1145](https://osgeo-org.atlassian.net/browse/GEOS-1145) Bring community-schema support as community module on trunk
