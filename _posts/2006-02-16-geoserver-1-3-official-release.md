---
author: Brent Owens
date: 2006-02-16
layout: post
link: http://docs.codehaus.org/display/GEOS/2006/02/16/GeoServer+1.3+Official+Release
wayback: https://web.archive.org/web/20060331060446/http://docs.codehaus.org:80/display/GEOS/2006/02/16/GeoServer+1.3+Official+Release
title: "GeoServer 1.3 Official Release"
categories:
- Announcements
---

The GeoServer Project is pleased to announce the stable release of\
version 1.3. This release brings a number of improvements to make\
GeoServer the easiest way to get a powerful open source standards-based\
web mapping solution up and running quickly. GeoServer has\
traditionally focused on WFS, which allows access to the raw vector\
data, serving as the WFS reference implementation. 1.3 brings fully\
compliant WMS and SLD, which handle the rendering and styling of maps,\
available as JPEG, PNG, GIF, SVG and KML. Official OGC certifications\
are in the works for both WMS and WFS, as all compliance tests have\
been passed.

Continuing the focus on ease of use, GeoServer now includes an\
integrated MapBuilder (<http://mapbuilder.sourceforge.net>) AJAX-based\
client to instantly preview any GeoServer layer. Configuration is\
still a cinch with a web based interface, and all layers are 'standard\
by default', no need to modify each layer just to have data served\
correctly. Sharing GeoServer configurations has been made easier with\
configurable data directories. The documentation has also been greatly\
improved, transitioning to a wiki-based solution, available at\
<https://web.archive.org/web/20060110030803/http://docs.codehaus.org/display/GEOSDOC/Documentation>

Several new data formats are also reaching maturity, adding DB2,\
Cascading WFS, MySQL, VPF and MapInfo to the already established\
PostGIS, Oracle, ArcSDE and Shapefile. The WFS will also now produce\
Shapefiles directly, instead of only GML. Internationalization has\
been greatly improved, including a new Japanese translation of the web\
admin tool.

For more information about GeoServer please see:\
<https://web.archive.org/web/20060101085439/http://docs.codehaus.org/display/GEOS/What+is+Geoserver> The release\
can be downloaded at: <https://web.archive.org/web/20060215061203/http://docs.codehaus.org/display/GEOS/Stable>\
The GeoServer Project is completely open\
source, in license and development process, built by an open community\
of contributors. Please see:\
<https://web.archive.org/web/20060418064835/http://docs.codehaus.org/display/GEOS/Contributors> for a list of\
everyone that makes GeoServer possible. If you are interested in\
helping out, even with just suggestions on how to make it better, don't\
hesitate to show up on our lists at:\
<http://sourceforge.net/mail/?group_id=25086> All fixed issues for 1.3\
can be found at:\
[release notes](#release-notes)

You can download GeoServer here:\
<https://web.archive.org/web/20060215060717/http://docs.codehaus.org/display/GEOS/Latest>

----

The GeoServer 1.3.0 is available for download from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.0/):

#### Docs

- [Release Notes](#release-notes)
- [geoserver-1.3.0a-docs.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.0/geoserver-1.3.0a-docs.zip/download)

#### Deployment

- [geoserver-1.3.0a-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.0/geoserver-1.3.0a-war.zip/download)
- [geoserver-1.3.0a-bin.tar.gz](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.0/geoserver-1.3.0a-bin.tar.gz/download)

#### Windows Installer

- [geoserver-1.3.0a.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.0/geoserver-1.3.0a.exe/download)

#### Source Code

- [geoserver-1.3.0a-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3.0/geoserver-1.3.0a-src.zip/download)

#### DataStore Extensions

- [DB2](http://prdownloads.sourceforge.net/geoserver/geoserver-1.3.0-db2-ext.zip?download)
- [MySQL](http://prdownloads.sourceforge.net/geoserver/geoserver-1.3.0-mysql-ext.zip?download)
- [VPF](http://prdownloads.sourceforge.net/geoserver/geoserver-1.3.0-vpf-ext.zip?download)
- [WFS](http://prdownloads.sourceforge.net/geoserver/geoserver-1.3.0-wfs-ext.zip?download)

Tested with: JBoss, Jetty, Tomcat, Resin

GeoServer **[License](https://web.archive.org/web/20060216/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

New Feature:

* [GEOS-199](https://osgeo-org.atlassian.net/browse/GEOS-199) Support gif as an output format for the WMS
* [GEOS-438](https://osgeo-org.atlassian.net/browse/GEOS-438) Boundingbox per feature

Improvement:

* [GEOS-1](https://osgeo-org.atlassian.net/browse/GEOS-1) Generate LatLongBoundingBox dynamically
* [GEOS-263](https://osgeo-org.atlassian.net/browse/GEOS-263) Performance improvement in PointSybolizer
* [GEOS-277](https://osgeo-org.atlassian.net/browse/GEOS-277) Better error messages for file system accesses
* [GEOS-379](https://osgeo-org.atlassian.net/browse/GEOS-379) move or copy mapbuilder demo to demo page
* [GEOS-521](https://osgeo-org.atlassian.net/browse/GEOS-521) Change Welcome page on windows installer
* [GEOS-522](https://osgeo-org.atlassian.net/browse/GEOS-522) Changing wording of data_dir windows installer page
* [GEOS-523](https://osgeo-org.atlassian.net/browse/GEOS-523) Link to documentation from Windows menu is broken
* [GEOS-525](https://osgeo-org.atlassian.net/browse/GEOS-525) welcome.do improvements
* [GEOS-536](https://osgeo-org.atlassian.net/browse/GEOS-536) GetCapabilities URL needed for Connection information

Bug:

* [GEOS-193](https://osgeo-org.atlassian.net/browse/GEOS-193) SVG output lacking xlink:href tag
* [GEOS-270](https://osgeo-org.atlassian.net/browse/GEOS-270) ACE-GIS test 7, task 1: GetMap SRS Parameter checking
* [GEOS-272](https://osgeo-org.atlassian.net/browse/GEOS-272) ACE_GIS Test 10, Task 1 - TRANSPARENT, BGCOLOR Parameter
* [GEOS-285](https://osgeo-org.atlassian.net/browse/GEOS-285) GetMap with Oracle does not take point rotations into account
* [GEOS-295](https://osgeo-org.atlassian.net/browse/GEOS-295) Invalid datastore connection blocks update/delete for other connections
* [GEOS-318](https://osgeo-org.atlassian.net/browse/GEOS-318) deleting all featuretypes and datastores
* [GEOS-319](https://osgeo-org.atlassian.net/browse/GEOS-319) PostGIS 1.0 WKB changed
* [GEOS-320](https://osgeo-org.atlassian.net/browse/GEOS-320) Postgis filter encoder - disjoint
* [GEOS-349](https://osgeo-org.atlassian.net/browse/GEOS-349) capabilities directory required for validation
* [GEOS-364](https://osgeo-org.atlassian.net/browse/GEOS-364) Unable to set a default data namespace in French configuration page
* [GEOS-369](https://osgeo-org.atlassian.net/browse/GEOS-369) Filter Functions don't work, ExpressionSAXParser misses implementation
* [GEOS-395](https://osgeo-org.atlassian.net/browse/GEOS-395) documentation change
* [GEOS-401](https://osgeo-org.atlassian.net/browse/GEOS-401) Problem with labels (texts disappear)
* [GEOS-442](https://osgeo-org.atlassian.net/browse/GEOS-442) URL Encoding issue
* [GEOS-460](https://osgeo-org.atlassian.net/browse/GEOS-460) MySQL doesn't work with MapPreview
* [GEOS-500](https://osgeo-org.atlassian.net/browse/GEOS-500) demos - check validity of xml
* [GEOS-526](https://osgeo-org.atlassian.net/browse/GEOS-526) SLD namespace aware bug with remote SLD documents
* [GEOS-527](https://osgeo-org.atlassian.net/browse/GEOS-527) Shapefile output format fails on linux

Task:

* [GEOS-301](https://osgeo-org.atlassian.net/browse/GEOS-301) Improve the contributors page
* [GEOS-514](https://osgeo-org.atlassian.net/browse/GEOS-514) Create a tutorial for how to do documentation
