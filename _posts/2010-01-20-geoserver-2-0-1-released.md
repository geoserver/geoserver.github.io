---
author: geoserver
comments: true
date: 2010-01-20 22:56:18+00:00
layout: post
link: http://blog.geoserver.org/2010/01/20/geoserver-2-0-1-released/
slug: geoserver-2-0-1-released
title: GeoServer 2.0.1 Released
wordpress_id: 420
categories:
- Announcements
- Features
---

With a large number of users upgrading to GeoServer 2.0, it's no wonder we've had so many fixes and improvements make it into GeoServer 2.0.1, now available for download.

Possibly the most significant change since 2.0.0 has been the addition of the [RESTful API](http://docs.geoserver.org/2.0.x/en/user/extensions/rest/index.html?highlight=rest%20api) to the security sub system.  Previously, users were able to connect in a read-only capacity to otherwise secure services through RESTful GET requests.  While this is a good fix for GeoServer, it does mean that users who were previously relying on anonymous read access to secure services must now authenticate before they can access them.  [More details are available](http://docs.geoserver.org/2.0.x/en/user/security/sec_rest.html) for those who are interested.

Other changes include usability changes to the administration UI, an updated Windows installer that now contains service and console installation options, and over 100 other [issues fixed](#release-notes).

We encourage you to download the latest version and take it for a spin and report any issues you encounter to the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users) or [bug tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS).

As always, we owe a debt of gratitude to all those that have contributed bug reports, fixes, patches and features.  A special thanks goes out to [LISAsoft](https://web.archive.org/web/20100120/http://www.lisasoft.com/) for managing this release.

----

## GeoServer 2.0.1

Released on January 20, 2010

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/geoserver-2.0.1-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/geoserver-2.0.1-war.zip/download)
- [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/geoserver-2.0.1-ng.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/GeoServer-2.0.1.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/geoserver-2.0.1-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/geoserver-2.0.1-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/geoserver-2.0.1-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/geoserver-2.0.1-javadoc.zip/download)
- [Release Notes](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/release-notes-2.0.1.txt/download)
- [Change Log](#release-notes)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-pyramid-plugin.zip/download)
- [JPEG2000](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-imagemosaic-jdbc-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-charts-plugin.zip/download)
- [Excel output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-excel-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-geosearch-plugin.zip/download)
- [Image Map output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-imagemap-plugin.zip/download)
- [OGR output format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-ogr-plugin.zip/download)
- [RESTConfig](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-restconfig-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.1/extensions/geoserver-2.0.1-wfsv-plugin.zip/download)

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 15897

## Release notes

New Feature:

* [GEOS-783](https://osgeo-org.atlassian.net/browse/GEOS-783) MsSqlSpatial support
* [GEOS-2720](https://osgeo-org.atlassian.net/browse/GEOS-2720) Security UI: manager users and rights in the web UI
* [GEOS-3187](https://osgeo-org.atlassian.net/browse/GEOS-3187) Installer should allow alternate Port
* [GEOS-3317](https://osgeo-org.atlassian.net/browse/GEOS-3317) Reload geoserver configuration via REST

Improvement:

* [GEOS-1115](https://osgeo-org.atlassian.net/browse/GEOS-1115) factor in map preview functionality into the reflector
* [GEOS-2698](https://osgeo-org.atlassian.net/browse/GEOS-2698) Can you please check for EPSG:3787 and EPSG:3794 implementation
* [GEOS-3019](https://osgeo-org.atlassian.net/browse/GEOS-3019) Make sure entities with editable names dont' collide with existing items on save
* [GEOS-3092](https://osgeo-org.atlassian.net/browse/GEOS-3092) Add a brief mode to xstream persister
* [GEOS-3166](https://osgeo-org.atlassian.net/browse/GEOS-3166) Windows installer for 64-bit systems
* [GEOS-3183](https://osgeo-org.atlassian.net/browse/GEOS-3183) Windows installer ignores JAVA_HOME input
* [GEOS-3221](https://osgeo-org.atlassian.net/browse/GEOS-3221) Geoserver should take care if a image reader is thread safe
* [GEOS-3227](https://osgeo-org.atlassian.net/browse/GEOS-3227) Websphere Deployment and j_acegi_security_check
* [GEOS-3294](https://osgeo-org.atlassian.net/browse/GEOS-3294) Make FeatureTypeinfo attributes a true derived property
* [GEOS-3401](https://osgeo-org.atlassian.net/browse/GEOS-3401) Make use of bookmarkable links for all main catalog resources
* [GEOS-3420](https://osgeo-org.atlassian.net/browse/GEOS-3420) More details on "Internal error"
* [GEOS-3517](https://osgeo-org.atlassian.net/browse/GEOS-3517) Use layer specific icons in the preview
* [GEOS-3537](https://osgeo-org.atlassian.net/browse/GEOS-3537) GeoServer should stop using the deprecated MapContext.setAreaOfInterest(Envelope) method
* [GEOS-3556](https://osgeo-org.atlassian.net/browse/GEOS-3556) Update GeoSilk icons
* [GEOS-3567](https://osgeo-org.atlassian.net/browse/GEOS-3567) Add an extension point for tabs on the layer / resource edit page.
* [GEOS-3599](https://osgeo-org.atlassian.net/browse/GEOS-3599) Expose png compression options via configuration options
* [GEOS-3615](https://osgeo-org.atlassian.net/browse/GEOS-3615) Allow label displacement for point labels as well
* [GEOS-3624](https://osgeo-org.atlassian.net/browse/GEOS-3624) Improve the ability to match random EPSG wkt definitions to an official EPSG code
* [GEOS-3636](https://osgeo-org.atlassian.net/browse/GEOS-3636) Introduce EMF bindings for the management of WCS1.0.0 requests/responses also
* [GEOS-3643](https://osgeo-org.atlassian.net/browse/GEOS-3643) Make EditAreaBehavior syntax scheme configurable, and change default to xml
* [GEOS-3647](https://osgeo-org.atlassian.net/browse/GEOS-3647) Greater abstraction of DefaultRasterMapProducer.java
* [GEOS-3652](https://osgeo-org.atlassian.net/browse/GEOS-3652) New layer page confusing users with warning sign
* [GEOS-3664](https://osgeo-org.atlassian.net/browse/GEOS-3664) Wrong layername produces nullpointer exception
* [GEOS-3666](https://osgeo-org.atlassian.net/browse/GEOS-3666) Add support for Cassini-Soldner projection
* [GEOS-3667](https://osgeo-org.atlassian.net/browse/GEOS-3667) Add support for equidistant conic projection
* [GEOS-3670](https://osgeo-org.atlassian.net/browse/GEOS-3670) Enable one to easily override doc sphinx theme
* [GEOS-3671](https://osgeo-org.atlassian.net/browse/GEOS-3671) Handle dateline wrapping for vector data in common projections
* [GEOS-3678](https://osgeo-org.atlassian.net/browse/GEOS-3678) cache WMS GetMapProducers to void expensive lookup specially under high concurrency
* [GEOS-3691](https://osgeo-org.atlassian.net/browse/GEOS-3691) Allow for extension blacklists

Bug:

* [GEOS-1094](https://osgeo-org.atlassian.net/browse/GEOS-1094) XML Transformer factory is being set by System.setProperty, impacting entire JVM, breaking Weblogic 9.x
* [GEOS-1253](https://osgeo-org.atlassian.net/browse/GEOS-1253) application/atom+xml and application/rss+xml are in capabilities but are not supported
* [GEOS-1818](https://osgeo-org.atlassian.net/browse/GEOS-1818) unable to handle GetMap with standalone SLD referencing layers defined as BASEMAP in service.xml
* [GEOS-1881](https://osgeo-org.atlassian.net/browse/GEOS-1881) WFS_getFeature ServiceException
* [GEOS-2020](https://osgeo-org.atlassian.net/browse/GEOS-2020) Sample GetCoverage request fails with "colorModel == null"
* [GEOS-2549](https://osgeo-org.atlassian.net/browse/GEOS-2549) Feature portrayal requests don't work when the remote server is a recent GeoServer
* [GEOS-2930](https://osgeo-org.atlassian.net/browse/GEOS-2930) Windows Installer Errata
* [GEOS-2939](https://osgeo-org.atlassian.net/browse/GEOS-2939) GeoWebCache logo on demo page tied to online resource
* [GEOS-3095](https://osgeo-org.atlassian.net/browse/GEOS-3095) gml:id aren't encoded for non-feature types
* [GEOS-3134](https://osgeo-org.atlassian.net/browse/GEOS-3134) RSS + Bing (ex virtual earth) demo does not work
* [GEOS-3216](https://osgeo-org.atlassian.net/browse/GEOS-3216) GeoServer/Image mosaic jdbc reader not thread safe (blank images)
* [GEOS-3224](https://osgeo-org.atlassian.net/browse/GEOS-3224) GEOSERVER_DATA_DIR environment variable ignored
* [GEOS-3325](https://osgeo-org.atlassian.net/browse/GEOS-3325) geoserver-1.7.6-ng installer fails if no JAVA_HOME set
* [GEOS-3344](https://osgeo-org.atlassian.net/browse/GEOS-3344) GS not respecting enable/disable service option
* [GEOS-3348](https://osgeo-org.atlassian.net/browse/GEOS-3348) if coverage stores have duplicate names (in separate workspaces) then one store masks the other
* [GEOS-3352](https://osgeo-org.atlassian.net/browse/GEOS-3352) Welcome page should have link to GeoWebCache admin
* [GEOS-3388](https://osgeo-org.atlassian.net/browse/GEOS-3388) DataStoreFileResource returns incomplete zip file when downloading from a shape datastore
* [GEOS-3393](https://osgeo-org.atlassian.net/browse/GEOS-3393) WMS Post GetMap fails due to exception in OWS Dispatcher on a request.input.reset() (mark invalid)
* [GEOS-3395](https://osgeo-org.atlassian.net/browse/GEOS-3395) Uploading a style whose name does not match the source filename results in bad configuration
* [GEOS-3434](https://osgeo-org.atlassian.net/browse/GEOS-3434) Cannot login in the Wicket UI when GS is sitting behind a reverse proxy
* [GEOS-3440](https://osgeo-org.atlassian.net/browse/GEOS-3440) Default data dir does not survive a restart
* [GEOS-3444](https://osgeo-org.atlassian.net/browse/GEOS-3444) java.lang.OutOfMemoryError with restconfig plugin
* [GEOS-3522](https://osgeo-org.atlassian.net/browse/GEOS-3522) Mosaic plugin ignore mosaic name configuration
* [GEOS-3529](https://osgeo-org.atlassian.net/browse/GEOS-3529) GWC fails to create cache.
* [GEOS-3543](https://osgeo-org.atlassian.net/browse/GEOS-3543) A restart is required to make GeoServer notice new tables in an already configured JDBC datastore
* [GEOS-3548](https://osgeo-org.atlassian.net/browse/GEOS-3548) Mosaic index generation fails over a large tile set
* [GEOS-3564](https://osgeo-org.atlassian.net/browse/GEOS-3564) Cannot create anymore a shapefile datastore providing a full path
* [GEOS-3565](https://osgeo-org.atlassian.net/browse/GEOS-3565) User interface used to distinguish among required and optional datastore parameters, the new one does not
* [GEOS-3568](https://osgeo-org.atlassian.net/browse/GEOS-3568) New web UI does not control which workspace is the default workspace
* [GEOS-3569](https://osgeo-org.atlassian.net/browse/GEOS-3569) Patch to let hibernate catalog correctly working with REST
* [GEOS-3571](https://osgeo-org.atlassian.net/browse/GEOS-3571) geoserver.log and *.properties files appear in the wrong place
* [GEOS-3579](https://osgeo-org.atlassian.net/browse/GEOS-3579) Oracle NG does not offer a OCI based factory
* [GEOS-3584](https://osgeo-org.atlassian.net/browse/GEOS-3584) WFS request not extracting the geometry attributes will fail with a geometry filter
* [GEOS-3588](https://osgeo-org.atlassian.net/browse/GEOS-3588) IOUtils.createTempDirectory - Prefix is ignored
* [GEOS-3598](https://osgeo-org.atlassian.net/browse/GEOS-3598) WFS fields larger than 32000 characters corrupt Excel output
* [GEOS-3600](https://osgeo-org.atlassian.net/browse/GEOS-3600) WMS Performance degrades after >20000 requests served
* [GEOS-3601](https://osgeo-org.atlassian.net/browse/GEOS-3601) Uploading coverage fails
* [GEOS-3605](https://osgeo-org.atlassian.net/browse/GEOS-3605) Oracle (NG) plugin may deadlock under high load
* [GEOS-3607](https://osgeo-org.atlassian.net/browse/GEOS-3607) Layer preview breaks if any output format returns an empty set of formats
* [GEOS-3609](https://osgeo-org.atlassian.net/browse/GEOS-3609) Can't renable resources from the user interface.
* [GEOS-3611](https://osgeo-org.atlassian.net/browse/GEOS-3611) REST request to get coverages metadata in json format
* [GEOS-3613](https://osgeo-org.atlassian.net/browse/GEOS-3613) EPSG overrides are not taken into consideration when computing transformations
* [GEOS-3614](https://osgeo-org.atlassian.net/browse/GEOS-3614) WFS getFeatures propertyName is broken in URL for 2.0.0a
* [GEOS-3616](https://osgeo-org.atlassian.net/browse/GEOS-3616) Demo requests page not using edited Body for request
* [GEOS-3619](https://osgeo-org.atlassian.net/browse/GEOS-3619) "Free JAI Memory" button on StatusPage seems to cause no effect
* [GEOS-3623](https://osgeo-org.atlassian.net/browse/GEOS-3623) PostgGIS  requires geometry columns to be registered in geometry_columns, old postgis datastore did not
* [GEOS-3625](https://osgeo-org.atlassian.net/browse/GEOS-3625) When default workspace is removed there is no way to set it back, this causes datastore creation exceptions
* [GEOS-3626](https://osgeo-org.atlassian.net/browse/GEOS-3626) Projection policy completely ignored in GS 2.0
* [GEOS-3627](https://osgeo-org.atlassian.net/browse/GEOS-3627) OGR output format would break if "leave native" projection policy is used
* [GEOS-3637](https://osgeo-org.atlassian.net/browse/GEOS-3637) URI URL worspace definition
* [GEOS-3638](https://osgeo-org.atlassian.net/browse/GEOS-3638) GEOGRAPHY_COLUMNS view showing up as geometry column
* [GEOS-3644](https://osgeo-org.atlassian.net/browse/GEOS-3644) Transaction with inserts and feature listeners fail against NG datastores
* [GEOS-3646](https://osgeo-org.atlassian.net/browse/GEOS-3646) layer group creation fails due to lack of crs
* [GEOS-3648](https://osgeo-org.atlassian.net/browse/GEOS-3648) Problem with visualization of cp1251 shapefiles and WMS-replies
* [GEOS-3659](https://osgeo-org.atlassian.net/browse/GEOS-3659) Security GUI not preserving newly created rules
* [GEOS-3660](https://osgeo-org.atlassian.net/browse/GEOS-3660) Mosaic reprojection appears to be broken
* [GEOS-3663](https://osgeo-org.atlassian.net/browse/GEOS-3663) The web UI fails if security is put in mixed mode and the current user cannot access some layer/workspace/store
* [GEOS-3668](https://osgeo-org.atlassian.net/browse/GEOS-3668) typo messed up getlegendgraphic url
* [GEOS-3669](https://osgeo-org.atlassian.net/browse/GEOS-3669) GeoWebCach problem when Grouped Layer exist
* [GEOS-3672](https://osgeo-org.atlassian.net/browse/GEOS-3672) Antialiasing and hatch error
* [GEOS-3673](https://osgeo-org.atlassian.net/browse/GEOS-3673) Creating a new style via copy causes subsequent style changes to be applied ot both
* [GEOS-3674](https://osgeo-org.atlassian.net/browse/GEOS-3674) WFS getFeature works incorrectly when using combinations of DWithin and maxFeature
* [GEOS-3680](https://osgeo-org.atlassian.net/browse/GEOS-3680) HTMLImageMapMapProducer is not declared as singleton="false" in the Spring context
* [GEOS-3681](https://osgeo-org.atlassian.net/browse/GEOS-3681) Native SRS from PostGIS not recognized
* [GEOS-3688](https://osgeo-org.atlassian.net/browse/GEOS-3688) Labelling might fail in very tortuous looping lines
* [GEOS-3698](https://osgeo-org.atlassian.net/browse/GEOS-3698) Secure all access via restconfig
* [GEOS-3704](https://osgeo-org.atlassian.net/browse/GEOS-3704) WMS + featureid filter + multiple layer -> exception
* [GEOS-3708](https://osgeo-org.atlassian.net/browse/GEOS-3708) Strange URL validation in Shapefile importer
* [GEOS-3713](https://osgeo-org.atlassian.net/browse/GEOS-3713) Reloading a feature type does not cause xml schema cache to be cleared
* [GEOS-3715](https://osgeo-org.atlassian.net/browse/GEOS-3715) GeoServerAbstractTestSupport should reset the referencing subsystem on startup
* [GEOS-3721](https://osgeo-org.atlassian.net/browse/GEOS-3721) PostGIS datastore does not show new layers until it is edited and saved
* [GEOS-3727](https://osgeo-org.atlassian.net/browse/GEOS-3727) Unbounded prepared statement pooling can bring Oracle to its knees
* [GEOS-3729](https://osgeo-org.atlassian.net/browse/GEOS-3729) Styled overwritten on data directory conversion when file ends with .xml
* [GEOS-3737](https://osgeo-org.atlassian.net/browse/GEOS-3737) When only 1 workspace is defined, you cannot add a PostGIS NG store.
* [GEOS-3770](https://osgeo-org.atlassian.net/browse/GEOS-3770) Logging filter will make Wicket file uploads fail

Task:

* [GEOS-2730](https://osgeo-org.atlassian.net/browse/GEOS-2730) Ensure all strings are i18nized
* [GEOS-3084](https://osgeo-org.atlassian.net/browse/GEOS-3084) Document Wicket UI modules
* [GEOS-3147](https://osgeo-org.atlassian.net/browse/GEOS-3147) Features pregeneraized should have a standard documentation entry, more than a tutorial
* [GEOS-3324](https://osgeo-org.atlassian.net/browse/GEOS-3324) Improve wfs schemamapping docs
* [GEOS-3603](https://osgeo-org.atlassian.net/browse/GEOS-3603) Update wiki download template
* [GEOS-3604](https://osgeo-org.atlassian.net/browse/GEOS-3604) Have the web security packaging use the same name naming rules as the other plugins (e.g. end with -plugin.zip)
* [GEOS-3606](https://osgeo-org.atlassian.net/browse/GEOS-3606) Setup nightly builds for GT 2.6.x and GS 2.0.x
* [GEOS-3618](https://osgeo-org.atlassian.net/browse/GEOS-3618) Show JAI available/used memory in user friendly format just like for Heap mem
* [GEOS-3710](https://osgeo-org.atlassian.net/browse/GEOS-3710) Document REST security configuration
