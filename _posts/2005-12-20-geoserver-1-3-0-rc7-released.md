---
author: Brent Owens
date: 2005-12-20
layout: post
link: http://docs.codehaus.org/display/GEOS/2005/12/20/GeoServer+1.3.0-RC7+Released
wayback: https://web.archive.org/web/20060625112101/http://docs.codehaus.org:80/display/GEOS/2005/12/20/GeoServer+1.3.0-RC7+Released
title: "GeoServer 1.3.0-RC7 Released"
categories:
- Announcements
---

GeoServer 1.3.0-RC7 has been released!

The major changes since RC6 have been:

- Reorganization of the data directory structure
- SLD Validation
- Lenient CRS Transforms
- Logging
- Http Unit Testing\
  Based on the geotools 2.1.x branch (tag = geoserver-1.3.0.RC7)

For more information on the data directory system, look at:\
[GeoServer Data Directory](https://web.archive.org/web/20060613091826/http://docs.codehaus.org/display/GEOSDOC/GeoServer+Data+Directory)

----

The release candiate GeoServer 1.3.0-RC7 is available for testing from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC7/):

#### Docs

- [Release Notes](#release-notes)
- [geoserver-1.3.0-RC7-docs.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC7/geoserver-1.3.0-RC7-docs.zip/download)

#### Deployment

- [geoserver-1.3.0-RC7-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC7/geoserver-1.3.0-RC7-war.zip/download)
- [geoserver-1.3.0-RC7-bin.tar.gz](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC7/geoserver-1.3.0-RC7-bin.tar.gz/download)

#### Windows Installer

- [geoserver-1.3.0-RC7.exe](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC7/geoserver-1.3.0-RC7.exe/download)

#### Source Code

- [geoserver-1.3.0-RC7-src.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/1.3-RC7/geoserver-1.3.0-RC7-src.zip/download)

Tested with: Jetty, Tomcat

GeoServer **[License](https://web.archive.org/web/20051220/http://docs.codehaus.org/display/GEOSDOC/License)** agreement

## Release notes

Improvement:

* [GEOS-404](https://osgeo-org.atlassian.net/browse/GEOS-404) DOC - sld examples
* [GEOS-443](https://osgeo-org.atlassian.net/browse/GEOS-443) Include XALAN-J jar for Java 1.5
* [GEOS-485](https://osgeo-org.atlassian.net/browse/GEOS-485) Shapefile output format should be named SHAPE-ZIP, not SHAPE
* [GEOS-507](https://osgeo-org.atlassian.net/browse/GEOS-507) Make CRS transforms lenient

Bug:

* [GEOS-405](https://osgeo-org.atlassian.net/browse/GEOS-405) Directory "Images" no exists for the html documentation
* [GEOS-416](https://osgeo-org.atlassian.net/browse/GEOS-416) LinePlacement for labeling ignored
* [GEOS-419](https://osgeo-org.atlassian.net/browse/GEOS-419) org.geotools.data.DataSourceException: Transaction rollback
* [GEOS-457](https://osgeo-org.atlassian.net/browse/GEOS-457) Bug with points symbols in SVG
* [GEOS-471](https://osgeo-org.atlassian.net/browse/GEOS-471) Automatic SLD validation no longer provides the .xsd file for the user
* [GEOS-474](https://osgeo-org.atlassian.net/browse/GEOS-474) Logging to file removes logging to console
* [GEOS-482](https://osgeo-org.atlassian.net/browse/GEOS-482) Our getCapabilities document should validate against the schema we give it.

Task:

* [GEOS-453](https://osgeo-org.atlassian.net/browse/GEOS-453) Merge boundedBy changes on FeatureTransformer onto trunk
* [GEOS-456](https://osgeo-org.atlassian.net/browse/GEOS-456) Use the exported wiki docs in the docs-download and binary releases
* [GEOS-461](https://osgeo-org.atlassian.net/browse/GEOS-461) Bring GeoServer Data Dir stuff to prominence

Sub-task:

* [GEOS-462](https://osgeo-org.atlassian.net/browse/GEOS-462) Port all relevant GEOS wiki stuff to GEOSDOC, and organize GEOSDOC
* [GEOS-463](https://osgeo-org.atlassian.net/browse/GEOS-463) Create a navigator bar for exported wiki docs
* [GEOS-464](https://osgeo-org.atlassian.net/browse/GEOS-464) Create script to give real urls to relative Space references.
* [GEOS-465](https://osgeo-org.atlassian.net/browse/GEOS-465) Investigate an Ant task to automate the whole wiki export process
* [GEOS-466](https://osgeo-org.atlassian.net/browse/GEOS-466) Investigate 'tagging' or somehow marking the version of the space in JIRA
* [GEOS-467](https://osgeo-org.atlassian.net/browse/GEOS-467) Append the release guide for a howto on documentation
* [GEOS-473](https://osgeo-org.atlassian.net/browse/GEOS-473) Investigate styling the docs with a similar css to geoserver admin (wish)
* [GEOS-476](https://osgeo-org.atlassian.net/browse/GEOS-476) Update startup scripts to make use of GEOSERVER_DATA_DIR environment variables
* [GEOS-477](https://osgeo-org.atlassian.net/browse/GEOS-477) Fix data_dir system properties to ignore the empty string
* [GEOS-478](https://osgeo-org.atlassian.net/browse/GEOS-478) Put up a better wiki page of GEOSERVER_DATA_DIR
* [GEOS-481](https://osgeo-org.atlassian.net/browse/GEOS-481) Move capabilities/ schema information to top level directory
* [GEOS-483](https://osgeo-org.atlassian.net/browse/GEOS-483) Move more static mapbuilder demos and mapbuilder libs out of data_dir
* [GEOS-484](https://osgeo-org.atlassian.net/browse/GEOS-484) document a 'production best practices'
* [GEOS-486](https://osgeo-org.atlassian.net/browse/GEOS-486) Make sure SLD validation gets the right file
* [GEOS-487](https://osgeo-org.atlassian.net/browse/GEOS-487) Get rid of WEB-INF junk from data_dir
* [GEOS-488](https://osgeo-org.atlassian.net/browse/GEOS-488) Update Wiki for final edits, create an 'upgrade tutorial'.
* [GEOS-489](https://osgeo-org.atlassian.net/browse/GEOS-489) Make userBasic as a sample dataDir
* [GEOS-491](https://osgeo-org.atlassian.net/browse/GEOS-491) exe install to use new conf/ data dir
