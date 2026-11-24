---
author: Justin Deoliveira
date: 2008-06-11
layout: post
link: http://geoserver.org/display/GEOS/GeoServer+1.7.0-beta1
wayback: https://web.archive.org/web/20080921155038/http://geoserver.org:80/display/GEOS/GeoServer+1.7.0-beta1
title: "GeoServer 1.7.0-beta1 Released"
categories:
- Announcements
---

GeoServer 1.7.0-beta1 has been released, check it out below.

----

#### GeoServer 1.7.0-beta1 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/).

SourceForge Release 606024

- [Release Notes](#release-notes)
- [geoserver-1.7.0-beta1.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/geoserver-1.7.0-beta1.exe/download) (Win32 self-installing executable)
- [geoserver-1.7.0-beta1-bin.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/geoserver-1.7.0-beta1-bin.zip/download) (UNIX binary)
- [geoserver-1.7.0-beta1-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/geoserver-1.7.0-beta1-src.zip/download) (Source code)
- [geoserver-1.7.0-beta1-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/geoserver-1.7.0-beta1-war.zip/download) (Web archive)

- [geoserver-1.7.0-beta1-javadoc.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/geoserver-1.7.0-beta1-javadoc.zip/download) (Java Documentation)

#### [Extensions download page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/extensions/)

##### DataStore Extensions

- [GeoWebCache](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/extensions/geoserver-1.7.0-beta1-gwc-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/extensions/geoserver-1.7.0-beta1-arcsde-plugin.zip/download)
- [GML](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/extensions/geoserver-1.7.0-beta1-gml-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/extensions/geoserver-1.7.0-beta1-db2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/extensions/geoserver-1.7.0-beta1-mysql-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/extensions/geoserver-1.7.0-beta1-vpf-plugin.zip/download)
- [WFS](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/extensions/geoserver-1.7.0-beta1-wfsv-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/extensions/geoserver-1.7.0-beta1-oracle-plugin.zip/download)

##### Coverage Extensions

- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/1.7.0-beta1/extensions/geoserver-1.7.0-beta1-pyramid-plugin.zip/download)

## Release notes

New Feature:

* [GEOS-1897](https://osgeo-org.atlassian.net/browse/GEOS-1897) Add paging support in WMS through the custom startIndex and maxFeatures GetMap request parameters

Improvement:

* [GEOS-235](https://osgeo-org.atlassian.net/browse/GEOS-235) Add proper support for UPDATESEQUENCE
* [GEOS-1366](https://osgeo-org.atlassian.net/browse/GEOS-1366) Allow renaming of featureTypes
* [GEOS-1382](https://osgeo-org.atlassian.net/browse/GEOS-1382) Improve the OL preview
* [GEOS-1572](https://osgeo-org.atlassian.net/browse/GEOS-1572) OL preview should default to jpeg tiles for raster data
* [GEOS-1629](https://osgeo-org.atlassian.net/browse/GEOS-1629) Allow unit testing to use real data directories and real data stores
* [GEOS-1659](https://osgeo-org.atlassian.net/browse/GEOS-1659) WFS Maxfeatures refinement
* [GEOS-1663](https://osgeo-org.atlassian.net/browse/GEOS-1663) Try harder not to report "client closed socket" stack traces
* [GEOS-1718](https://osgeo-org.atlassian.net/browse/GEOS-1718) Transaction failing to locate feature type message could be improved
* [GEOS-1728](https://osgeo-org.atlassian.net/browse/GEOS-1728) Make sure axis ordering, logging, jai checks are performed before anything else starts up
* [GEOS-1748](https://osgeo-org.atlassian.net/browse/GEOS-1748) Geoserver unit tests should use partial buffering strategy instead of full buffer one
* [GEOS-1795](https://osgeo-org.atlassian.net/browse/GEOS-1795) GeoServer is not cleaning testing data dirs using coverages on windows
* [GEOS-1820](https://osgeo-org.atlassian.net/browse/GEOS-1820) Add explanation of the different downloadables
* [GEOS-1858](https://osgeo-org.atlassian.net/browse/GEOS-1858) Better default formatting for KML
* [GEOS-1874](https://osgeo-org.atlassian.net/browse/GEOS-1874) Switch all read only tests to a "one time setup" architecture
* [GEOS-1918](https://osgeo-org.atlassian.net/browse/GEOS-1918) Add a servlet filter that does the reverse proxy work in translating html and javascript urls to the proxy based ones
* [GEOS-1925](https://osgeo-org.atlassian.net/browse/GEOS-1925) PointSymbolizer on polygon features results in an icon at the edge of the polygon (should be inside)
* [GEOS-1957](https://osgeo-org.atlassian.net/browse/GEOS-1957) Have a WFSV 1.0 configuration
* [GEOS-1967](https://osgeo-org.atlassian.net/browse/GEOS-1967) Make IdentifierKvpParser generic
* [GEOS-1981](https://osgeo-org.atlassian.net/browse/GEOS-1981) Porting old configuration to new configuration

Bug:

* [GEOS-1486](https://osgeo-org.atlassian.net/browse/GEOS-1486) Cannot create new SLD for ArcSDE FeatureType
* [GEOS-1546](https://osgeo-org.atlassian.net/browse/GEOS-1546) Catalog is loaded twice for each unit test
* [GEOS-1581](https://osgeo-org.atlassian.net/browse/GEOS-1581) WCS Describe Coverage does not work properly with rotated coverages
* [GEOS-1656](https://osgeo-org.atlassian.net/browse/GEOS-1656) NPE thrown when pointing shapefile datastore configuration to a non existing path
* [GEOS-1657](https://osgeo-org.atlassian.net/browse/GEOS-1657) NPE thrown when configuring a shapefile with no .prj information
* [GEOS-1667](https://osgeo-org.atlassian.net/browse/GEOS-1667) All geometric filter return a blank image on wms + shapefiles + geoserver 1.6.x
* [GEOS-1669](https://osgeo-org.atlassian.net/browse/GEOS-1669) Exception reports by mistake n times the same message instead of using the messages got from the stack trace
* [GEOS-1678](https://osgeo-org.atlassian.net/browse/GEOS-1678) admin page contains freudian slip: GeoSever
* [GEOS-1686](https://osgeo-org.atlassian.net/browse/GEOS-1686) WFSV extension datastore is missing the net.opengis.wfsv jar
* [GEOS-1688](https://osgeo-org.atlassian.net/browse/GEOS-1688) null pointer exception in DefaultFilterVisitor
* [GEOS-1699](https://osgeo-org.atlassian.net/browse/GEOS-1699) GetCoverage band selection does not work for all bands but the first one
* [GEOS-1705](https://osgeo-org.atlassian.net/browse/GEOS-1705) Some XML writters set the xml charset to its human readable form instead of its canonical form
* [GEOS-1722](https://osgeo-org.atlassian.net/browse/GEOS-1722) When deploying two geoservers in the same VM, the second won't be able to use the custom epsg codes (Google projection included)
* [GEOS-1723](https://osgeo-org.atlassian.net/browse/GEOS-1723) srsList fails with "java.lang.NumberFormatException: For input string: "WGS84(DD)"
* [GEOS-1727](https://osgeo-org.atlassian.net/browse/GEOS-1727) Error when inserting polygons into a postgis table via geoserver with wfs gml.
* [GEOS-1747](https://osgeo-org.atlassian.net/browse/GEOS-1747) PartialBufferOutputStream2 flush issues (CVE-2008-7227)
* [GEOS-1749](https://osgeo-org.atlassian.net/browse/GEOS-1749) comma in PostGIS money datatype causes GetFeatureInfo request to fail
* [GEOS-1754](https://osgeo-org.atlassian.net/browse/GEOS-1754) Avoid NPE when GEOSERVER_DATA_DIR points to an empty directory
* [GEOS-1766](https://osgeo-org.atlassian.net/browse/GEOS-1766) Freemarker is eating exception causes if an error occurrs scrolling over a feature collection
* [GEOS-1801](https://osgeo-org.atlassian.net/browse/GEOS-1801) geojson output format does not handle queries for multiple feature types
* [GEOS-1815](https://osgeo-org.atlassian.net/browse/GEOS-1815) ensure all xml output explicity sets charset from GeoServer.getCharSet()
* [GEOS-1833](https://osgeo-org.atlassian.net/browse/GEOS-1833) CoverageInfos bounding boxes are not aggregated for the main WMS Layer in GetCapabilities
* [GEOS-1850](https://osgeo-org.atlassian.net/browse/GEOS-1850) Rotated images are not displayed correctly anymore (regression)
* [GEOS-1856](https://osgeo-org.atlassian.net/browse/GEOS-1856) ConcurrentModificationException under heavy load in xml module configuration
* [GEOS-1863](https://osgeo-org.atlassian.net/browse/GEOS-1863) Multiple bbox computation issues in projected layers (both feature type info panel and preview)
* [GEOS-1864](https://osgeo-org.atlassian.net/browse/GEOS-1864) GetMapKvpRequestReader eats CRS decoding exceptions
* [GEOS-1868](https://osgeo-org.atlassian.net/browse/GEOS-1868) org.vfny.geoserver.config.CoverageConfig causes memory overflow
* [GEOS-1873](https://osgeo-org.atlassian.net/browse/GEOS-1873) Problem adding new features using WFS-T
* [GEOS-1878](https://osgeo-org.atlassian.net/browse/GEOS-1878) Attributes containing apostrophes fail on insert/update using WFS-T
* [GEOS-1901](https://osgeo-org.atlassian.net/browse/GEOS-1901) Text only antialias is not working properly
* [GEOS-1909](https://osgeo-org.atlassian.net/browse/GEOS-1909) CITE WFS 1.1 failure after prepared statement usage in postgis data store
* [GEOS-1916](https://osgeo-org.atlassian.net/browse/GEOS-1916) GetFeatureInfo does not properly handle multi layer filters
* [GEOS-1935](https://osgeo-org.atlassian.net/browse/GEOS-1935) Regression: GetFeatureInfo NPE's
* [GEOS-1937](https://osgeo-org.atlassian.net/browse/GEOS-1937) Trying to clean up the cache results in a NPE
* [GEOS-1939](https://osgeo-org.atlassian.net/browse/GEOS-1939) Sorting WFS 1.1.0 cite tests broken
* [GEOS-1944](https://osgeo-org.atlassian.net/browse/GEOS-1944) Parsing NullPointerException for GetVersionedFeature request
* [GEOS-1953](https://osgeo-org.atlassian.net/browse/GEOS-1953) GeoServer extensions do not contain geotools jars, trunk nightlies extensions are useless
* [GEOS-1958](https://osgeo-org.atlassian.net/browse/GEOS-1958) Transaction binding in WFS 1.0 is not able to read native elements properly
* [GEOS-1970](https://osgeo-org.atlassian.net/browse/GEOS-1970) Acegi filter integration is not covering the /ows path
* [GEOS-1973](https://osgeo-org.atlassian.net/browse/GEOS-1973) Data directory relative path are not preserved anymore on trunk
* [GEOS-1976](https://osgeo-org.atlassian.net/browse/GEOS-1976) Regression, cannot configure layer groups without explicit styles anymore

Task:

* [GEOS-1574](https://osgeo-org.atlassian.net/browse/GEOS-1574) wfs:GetFeature.XLink-POST-XML-3
* [GEOS-1575](https://osgeo-org.atlassian.net/browse/GEOS-1575) wfs:GetFeature.XLink-POST-XML-4
* [GEOS-1576](https://osgeo-org.atlassian.net/browse/GEOS-1576) WFS 1.1 Xlink Cite Tests
* [GEOS-1587](https://osgeo-org.atlassian.net/browse/GEOS-1587) wfs:GetFeature.XLink-POST-XML-5
* [GEOS-1588](https://osgeo-org.atlassian.net/browse/GEOS-1588) wfs:GetFeature.XLink-POST-XML-6
* [GEOS-1627](https://osgeo-org.atlassian.net/browse/GEOS-1627) CCE from saxon in wms:basic_elements-version-negotiation-4 + wms:wmsops-getcapabilities-params-version-3
* [GEOS-1630](https://osgeo-org.atlassian.net/browse/GEOS-1630) wcs tests mishandle sequences of gml:pos
* [GEOS-1631](https://osgeo-org.atlassian.net/browse/GEOS-1631) wcs tests syntax issues
* [GEOS-1757](https://osgeo-org.atlassian.net/browse/GEOS-1757) Update the geoserver usage of GeoTools data api to use generics

Sub-task:

* [GEOS-1691](https://osgeo-org.atlassian.net/browse/GEOS-1691) Make sure GetCoverage output formats do use mime type compliant names
* [GEOS-1870](https://osgeo-org.atlassian.net/browse/GEOS-1870) Update GeoJSON output format to use CoordinateSequence instead of Coordinate[]
* [GEOS-1871](https://osgeo-org.atlassian.net/browse/GEOS-1871) Update ShapeZipOutputFormat to use CoordinateSequence instead of Coordinate[]
