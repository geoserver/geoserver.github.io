---
author: geoserver
comments: true
date: 2009-10-15 16:44:15+00:00
layout: post
link: http://blog.geoserver.org/2009/10/15/geoserver-2-0-rc2-released/
slug: geoserver-2-0-rc2-released
title: GeoServer 2.0-RC2 Released
wordpress_id: 338
categories:
- Announcements
---

The GeoServer team is pleased to announce the release of (hopefully) the final release candidate of version 2.0: GeoServer 2.0-RC2!

The main focus of this release was getting every little detail in order for 2.0.0.  There were a number of critical issues discovered that have been fixed, and much work was done on the documentation.  But the community did slide in one major new feature, a new plugin called 'Web security GUI', that enables GUI based editing of GeoServer's security configuration.  It hopefully will eventually move to the core, but for now is a great example of the advantages of the new Wicket UI technology - one of the major features of the 2.0 release.  The security GUI plugin can be added without having to change the core files at all, and is an example of how others can build extensions to the core GeoServer services and UI.

The other major feature of 2.0 is the [app-schema](http://docs.geoserver.org/2.0-RC2/user/data/app-schema/index.html) work, and there have been a number of bug fixes for this release candidate.  More importantly, there's now a lot of great documentation by the CSIRO team on how to get set up with [feature chaining](http://docs.geoserver.org/2.0-RC2/user/data/app-schema/feature-chaining.html), and [data access integration](http://docs.geoserver.org/2.0-RC2/user/data/app-schema/data-access-integration.html), as well as a great [tutorial](http://docs.geoserver.org/2.0-RC2/user/data/app-schema/tutorial.html).

This release also marks the branching of 2.0.x to make way for some great new improvements on trunk.  The [GeoSolutions](http://www.geo-solutions.it/) team is working on [bringing Hibernate](http://blog.geoserver.org/2009/08/27/hibernate-and-geoserver-seeking-for-scalability-and-robustness/) in to the GeoServer catalog, so it can be backed by a database for even greater scalability and robustness.  And Justin Deoliveira is [doing work](https://web.archive.org/web/20091015/http://geoserver.org/display/GEOS/GSIP+36+-+Resource+-+Publishing+Split+and+Virtual+Configuration) to have one GeoServer configuration handle a number of different services and security permissions at once.  These will be the highlights of the 2.1.x release, and please get in touch if you can help with funding or development time.  Also being discussed is WFS 2.0, GML 3.2 and WMS 1.3, all of which could move forward with more support.

Thanks to everyone who made the 2.0-RC2 release possible.  And please download it and let us know what you think.  If there are no major problems this release will become 2.0.0.

----

## GeoServer 2.0-RC2

Released on 2009-11-13

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/geoserver-2.0-RC2-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/geoserver-2.0-RC2-war.zip/download)
- [Windows Service Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/geoserver-2.0-RC2-ng.exe/download)
- [Windows Console Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/geoserver-2.0-RC2.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/geoserver-2.0-RC2.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/geoserver-2.0-RC2-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/geoserver-2.0-RC2-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/geoserver-2.0-RC2-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/geoserver-2.0-RC2-javadoc.zip/download)
- [Release Notes](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/release-notes-2.0-RC2.txt/download)

#### Extensions

**Data store**

- [Application Schema](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-mysql-plugin.zip/download)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-oracle-plugin.zip/download)
- [Pregeneralized features](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-feature-pregeneralized-plugin.zip/download)
- [SQL Server](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-sqlserver-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-vpf-plugin.zip/download)

**Coverage store**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-pyramid-plugin.zip/download)
- [JDBC Image Mosaic](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-imagemosaic-jdbc-plugin.zip/download)

**Other**

- [Chart dynamic symbolizer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-charts-plugin.zip/download)
- [GeoSearch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-geosearch-plugin.zip/download)
- [Image Map](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-imagemap-plugin.zip/download)
- [OGR Output Format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-ogr-plugin.zip/download)
- [REST Config](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-restconfig-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-wfsv-plugin.zip/download)
- [Web security GUI](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/extensions/geoserver-2.0-RC2-web-security.zip/download)

#### [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-RC2/)

SourceForge Release .

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 15569

## Release notes

New Feature:

* [GEOS-2294](https://osgeo-org.atlassian.net/browse/GEOS-2294) Building a mosaic should be a transparent operation
* [GEOS-2712](https://osgeo-org.atlassian.net/browse/GEOS-2712) Let people configure simple mosaics transparently from the UI
* [GEOS-3518](https://osgeo-org.atlassian.net/browse/GEOS-3518) Allow easy overriding / customization / addition off css

Improvement:

* [GEOS-1570](https://osgeo-org.atlassian.net/browse/GEOS-1570) Shapefile index building is very memory hungry
* [GEOS-2636](https://osgeo-org.atlassian.net/browse/GEOS-2636) uploaded sld files are not nicely formatted
* [GEOS-3108](https://osgeo-org.atlassian.net/browse/GEOS-3108) Describe Service Operations
* [GEOS-3188](https://osgeo-org.atlassian.net/browse/GEOS-3188) first page in webadmin to be the about page
* [GEOS-3313](https://osgeo-org.atlassian.net/browse/GEOS-3313) Setting protected modificator in catalog beans
* [GEOS-3355](https://osgeo-org.atlassian.net/browse/GEOS-3355) 2.0.x migration page needs to be ported from confluence to new docs.
* [GEOS-3356](https://osgeo-org.atlassian.net/browse/GEOS-3356) Port coordinate reference system handling over from confluence to new docs
* [GEOS-3383](https://osgeo-org.atlassian.net/browse/GEOS-3383) Workspace dropdown contents are not sorted
* [GEOS-3392](https://osgeo-org.atlassian.net/browse/GEOS-3392) Restore copy-ability to links on preview page
* [GEOS-3397](https://osgeo-org.atlassian.net/browse/GEOS-3397) Show GeoServer version more prominently on the doc pages
* [GEOS-3409](https://osgeo-org.atlassian.net/browse/GEOS-3409) Automatically set a title and an abstract for the newly created resources
* [GEOS-3410](https://osgeo-org.atlassian.net/browse/GEOS-3410) GSIP 39: pluggable url manglers
* [GEOS-3412](https://osgeo-org.atlassian.net/browse/GEOS-3412) Provide better error messages when QUERY_LAYER is not a subset of LAYERS in GetFeatureInfo
* [GEOS-3422](https://osgeo-org.atlassian.net/browse/GEOS-3422) Upgrade to Wicket 1.3.7
* [GEOS-3435](https://osgeo-org.atlassian.net/browse/GEOS-3435) perLayerSecurity User Interface
* [GEOS-3437](https://osgeo-org.atlassian.net/browse/GEOS-3437) Setup some default WMS resource consumption limits by default
* [GEOS-3510](https://osgeo-org.atlassian.net/browse/GEOS-3510) Replace layer type icons with geosilk ones
* [GEOS-3533](https://osgeo-org.atlassian.net/browse/GEOS-3533) Avoid cut out symbols in tiled preview
* [GEOS-3536](https://osgeo-org.atlassian.net/browse/GEOS-3536) Have GeoServerLoginPage extend GeoServerBasePage
* [GEOS-3552](https://osgeo-org.atlassian.net/browse/GEOS-3552) custom error pages in Wicket UI
* [GEOS-3558](https://osgeo-org.atlassian.net/browse/GEOS-3558) Allow favicon contribution via HeaderContribution
* [GEOS-3583](https://osgeo-org.atlassian.net/browse/GEOS-3583) WFSInfoImplHb.GML seems not to be mapped correctly

Bug:

* [GEOS-2061](https://osgeo-org.atlassian.net/browse/GEOS-2061) Metatling + JPEG -> broken output
* [GEOS-2519](https://osgeo-org.atlassian.net/browse/GEOS-2519) Port GEOS-2518 to trunk
* [GEOS-2611](https://osgeo-org.atlassian.net/browse/GEOS-2611) Adding shapefile datastore causes java.lang.OutOfMemoryError: Java heap space
* [GEOS-2736](https://osgeo-org.atlassian.net/browse/GEOS-2736) H2 extension does not contain a README (or LICENSE) file
* [GEOS-2839](https://osgeo-org.atlassian.net/browse/GEOS-2839) Unable to generate bounds against latest PostGIS
* [GEOS-2985](https://osgeo-org.atlassian.net/browse/GEOS-2985) Cannot use absolute paths in Mosaic Plugin
* [GEOS-3193](https://osgeo-org.atlassian.net/browse/GEOS-3193) GetLegendGraphic fails on large mosaics
* [GEOS-3254](https://osgeo-org.atlassian.net/browse/GEOS-3254) Importer doesn't like paths with spaces
* [GEOS-3336](https://osgeo-org.atlassian.net/browse/GEOS-3336) Renaming Layer Name
* [GEOS-3340](https://osgeo-org.atlassian.net/browse/GEOS-3340) Double proxied styles break persistence
* [GEOS-3341](https://osgeo-org.atlassian.net/browse/GEOS-3341) GetFeatureInfo automatic search area estimation does not seem to work properly
* [GEOS-3346](https://osgeo-org.atlassian.net/browse/GEOS-3346) Styles in dropdown display as "StyleInfoImpl[point]"
* [GEOS-3347](https://osgeo-org.atlassian.net/browse/GEOS-3347) ArcSDE UI extension jar not included in the extension bundle
* [GEOS-3353](https://osgeo-org.atlassian.net/browse/GEOS-3353) Building instructions for release indicates wrong DconfigDirectory
* [GEOS-3357](https://osgeo-org.atlassian.net/browse/GEOS-3357) Build failure in restconfig in path with spaces
* [GEOS-3358](https://osgeo-org.atlassian.net/browse/GEOS-3358) Workspace URI validation too strict
* [GEOS-3375](https://osgeo-org.atlassian.net/browse/GEOS-3375) WMS SRS list validator does not allow saving an empty srs list
* [GEOS-3376](https://osgeo-org.atlassian.net/browse/GEOS-3376) SpringUnWrapper fails to load in Java5 enviroment
* [GEOS-3377](https://osgeo-org.atlassian.net/browse/GEOS-3377) Save failures result in corrupted data directory and are not reported in the UI
* [GEOS-3378](https://osgeo-org.atlassian.net/browse/GEOS-3378) Native coverage SRS lost after restart
* [GEOS-3379](https://osgeo-org.atlassian.net/browse/GEOS-3379) JVM crashes in a multithreaded load test against an ECW coverage
* [GEOS-3381](https://osgeo-org.atlassian.net/browse/GEOS-3381) Returning XML file as shapefile
* [GEOS-3384](https://osgeo-org.atlassian.net/browse/GEOS-3384) Remove "Properties" option on new vector data source page
* [GEOS-3394](https://osgeo-org.atlassian.net/browse/GEOS-3394) Missing SLD causes NPE in Style Editor
* [GEOS-3398](https://osgeo-org.atlassian.net/browse/GEOS-3398) Workspace validation does not check for existing and valid URI
* [GEOS-3399](https://osgeo-org.atlassian.net/browse/GEOS-3399) WFS shapefile output generates different names at each call when a field exceeds 10 chars
* [GEOS-3400](https://osgeo-org.atlassian.net/browse/GEOS-3400) org.geoserver.platform.ServiceException: No such operation wms 1.1.0 GetCapabilities?SERVICE=WMS
* [GEOS-3402](https://osgeo-org.atlassian.net/browse/GEOS-3402) XML encoder in WFS 1.1 GetFeature leaks connection
* [GEOS-3406](https://osgeo-org.atlassian.net/browse/GEOS-3406) Workspace new and edit panels do not check the URI is not null
* [GEOS-3407](https://osgeo-org.atlassian.net/browse/GEOS-3407) (The!) Memoryleak in RetypingFeatureSource
* [GEOS-3413](https://osgeo-org.atlassian.net/browse/GEOS-3413) ImageMosaic layer configuration always forces to enter transparent colors
* [GEOS-3416](https://osgeo-org.atlassian.net/browse/GEOS-3416) Global handling in ContactPage
* [GEOS-3417](https://osgeo-org.atlassian.net/browse/GEOS-3417) Layer style hrefs are wrong
* [GEOS-3424](https://osgeo-org.atlassian.net/browse/GEOS-3424) geoserver RC1 WMS bug with new raster data
* [GEOS-3427](https://osgeo-org.atlassian.net/browse/GEOS-3427) creating new workspace allows uri to be unset
* [GEOS-3428](https://osgeo-org.atlassian.net/browse/GEOS-3428) Resource name validator too strict, won't accept valid feature type and coverage names
* [GEOS-3429](https://osgeo-org.atlassian.net/browse/GEOS-3429) ReflectiveHTMLFormat eats all parsing exceptions
* [GEOS-3430](https://osgeo-org.atlassian.net/browse/GEOS-3430) Ending a list resource URL with a trailing "/" results in failure to locate its template
* [GEOS-3431](https://osgeo-org.atlassian.net/browse/GEOS-3431) Exception trying to access coverage html representation
* [GEOS-3513](https://osgeo-org.atlassian.net/browse/GEOS-3513) WFS 1.0 GetCapabilities double prefixes SRS codes like in EPSG:EPSG:4326
* [GEOS-3514](https://osgeo-org.atlassian.net/browse/GEOS-3514) Namespace field not updated if there's only one workspace configured
* [GEOS-3516](https://osgeo-org.atlassian.net/browse/GEOS-3516) KML and WMS reflectors do not work anymore
* [GEOS-3519](https://osgeo-org.atlassian.net/browse/GEOS-3519) The UI allows to set the declared CRS of a resource to one that the native CRS can't be projected to
* [GEOS-3520](https://osgeo-org.atlassian.net/browse/GEOS-3520) CatalogImpl does not remove default namespace and workspace
* [GEOS-3521](https://osgeo-org.atlassian.net/browse/GEOS-3521) Regression: mosaic plugin cannot open anymore a read only index file
* [GEOS-3532](https://osgeo-org.atlassian.net/browse/GEOS-3532) Services report and/or disabled, or rather non reachable, resources by checking isEnabled() instead of enabled()
* [GEOS-3544](https://osgeo-org.atlassian.net/browse/GEOS-3544) Labels won't be painted anymore
* [GEOS-3545](https://osgeo-org.atlassian.net/browse/GEOS-3545) The CatalogBuilder does not store Coverage Dimensions
* [GEOS-3555](https://osgeo-org.atlassian.net/browse/GEOS-3555) PropertyLike Fails when
* [GEOS-3560](https://osgeo-org.atlassian.net/browse/GEOS-3560) The Coverage UI does not correctly save the Grid CRS when the Native EPSG code is unknown
* [GEOS-3570](https://osgeo-org.atlassian.net/browse/GEOS-3570) Read only layers + databases + gml3 = connection leak
* [GEOS-3575](https://osgeo-org.atlassian.net/browse/GEOS-3575) GetFeatureInfo on coverages may fail

Task:

* [GEOS-3069](https://osgeo-org.atlassian.net/browse/GEOS-3069) Add unit test to ensure ResourcePool.clear(DataStoreInfo) ends up calling DataAccess.dispose()
* [GEOS-3240](https://osgeo-org.atlassian.net/browse/GEOS-3240) Make sure all forms have basic validators in
* [GEOS-3339](https://osgeo-org.atlassian.net/browse/GEOS-3339) Document mixed geometry handling in SLD
* [GEOS-3362](https://osgeo-org.atlassian.net/browse/GEOS-3362) "Working with Data" docs
* [GEOS-3363](https://osgeo-org.atlassian.net/browse/GEOS-3363) Port old tutorials to new documentation
* [GEOS-3390](https://osgeo-org.atlassian.net/browse/GEOS-3390) Add wicket's IStringResourceLoader extension point for GeoServerApplication

Sub-task:

* [GEOS-3364](https://osgeo-org.atlassian.net/browse/GEOS-3364) Tutorial: Freemarker templates
* [GEOS-3365](https://osgeo-org.atlassian.net/browse/GEOS-3365) Tutorials: GeoRSS
* [GEOS-3366](https://osgeo-org.atlassian.net/browse/GEOS-3366) Tutorial: GetFeatureInfo templates
* [GEOS-3367](https://osgeo-org.atlassian.net/browse/GEOS-3367) Tutorial: KML Placemark templates
* [GEOS-3368](https://osgeo-org.atlassian.net/browse/GEOS-3368) Tutorial: KML Height templates
* [GEOS-3369](https://osgeo-org.atlassian.net/browse/GEOS-3369) Tutorial: Paletted Images
* [GEOS-3370](https://osgeo-org.atlassian.net/browse/GEOS-3370) Tutorial: Time Templates
* [GEOS-3371](https://osgeo-org.atlassian.net/browse/GEOS-3371) Tutorial: Serving static files
* [GEOS-3372](https://osgeo-org.atlassian.net/browse/GEOS-3372) Tutorial: WMS Reflector
* [GEOS-3453](https://osgeo-org.atlassian.net/browse/GEOS-3453) GeoServer Data Directory --> Setting the Data Directory
* [GEOS-3454](https://osgeo-org.atlassian.net/browse/GEOS-3454) GeoServer Data Directory --> Structure of the Data Directory
* [GEOS-3471](https://osgeo-org.atlassian.net/browse/GEOS-3471) Services --> Web Feature Services --> WFS Basics
* [GEOS-3472](https://osgeo-org.atlassian.net/browse/GEOS-3472) Services --> Web Feature Services --> Lockfeature
* [GEOS-3473](https://osgeo-org.atlassian.net/browse/GEOS-3473) Services --> Web Feature Services --> Transaction
* [GEOS-3475](https://osgeo-org.atlassian.net/browse/GEOS-3475) Services --> Web Map Service --> WMS Configuration--> Layer Groups
* [GEOS-3476](https://osgeo-org.atlassian.net/browse/GEOS-3476) Services --> Web Map Service --> WMS Configuration-->Rendering
* [GEOS-3477](https://osgeo-org.atlassian.net/browse/GEOS-3477) Services --> Web Map Service --> WMS reference --> GetCapabilities
* [GEOS-3478](https://osgeo-org.atlassian.net/browse/GEOS-3478) Services --> Web Map Service --> WMS reference --> GetFeatureInfo
* [GEOS-3479](https://osgeo-org.atlassian.net/browse/GEOS-3479) Services --> Web Map Service --> WMS Reference --> GetMap
* [GEOS-3480](https://osgeo-org.atlassian.net/browse/GEOS-3480) Services --> Web Coverage Service --> WCS Output formats
* [GEOS-3481](https://osgeo-org.atlassian.net/browse/GEOS-3481) Services --> Web Coverage Service --> WCS Vendor Parameters
* [GEOS-3482](https://osgeo-org.atlassian.net/browse/GEOS-3482) Services --> Web Coverage Service --> WCS Reference
* [GEOS-3483](https://osgeo-org.atlassian.net/browse/GEOS-3483) Running in a Production Environment --> Data Considerations --> Pick the best performing Coverage Formats
* [GEOS-3484](https://osgeo-org.atlassian.net/browse/GEOS-3484) Running in a Production Environment --> Other Considerations --> Clustering
* [GEOS-3485](https://osgeo-org.atlassian.net/browse/GEOS-3485) Caching with GeoWebCache --> Demo Page
* [GEOS-3487](https://osgeo-org.atlassian.net/browse/GEOS-3487) Google Earth --> Tutorials --> SuperOverlays and GeoWebCache
* [GEOS-3490](https://osgeo-org.atlassian.net/browse/GEOS-3490) Google Earth --> Features --> KML Legends
* [GEOS-3493](https://osgeo-org.atlassian.net/browse/GEOS-3493) Extensions --> GeoSearch
* [GEOS-3494](https://osgeo-org.atlassian.net/browse/GEOS-3494) Extensions --> ImageMap
* [GEOS-3495](https://osgeo-org.atlassian.net/browse/GEOS-3495) Extensions --> REST --> REST Configuration Examples --> PHP
* [GEOS-3496](https://osgeo-org.atlassian.net/browse/GEOS-3496) Extensions --> GeoExt Styler
* [GEOS-3497](https://osgeo-org.atlassian.net/browse/GEOS-3497) Extensions --> WFS Versioning
* [GEOS-3498](https://osgeo-org.atlassian.net/browse/GEOS-3498) Tutorials --> Freemarker Templates
* [GEOS-3502](https://osgeo-org.atlassian.net/browse/GEOS-3502) Tutorials --> GeoRSS
* [GEOS-3503](https://osgeo-org.atlassian.net/browse/GEOS-3503) Tutorials --> GetFeatureInfo
* [GEOS-3504](https://osgeo-org.atlassian.net/browse/GEOS-3504) Tutorials --> Paletted Images
* [GEOS-3505](https://osgeo-org.atlassian.net/browse/GEOS-3505) Tutorials --> Serving Static Files
* [GEOS-3506](https://osgeo-org.atlassian.net/browse/GEOS-3506) Tutorials --> WMS Reflector
* [GEOS-3509](https://osgeo-org.atlassian.net/browse/GEOS-3509) Google Earth --> Tutorials --> Height Template
* [GEOS-3546](https://osgeo-org.atlassian.net/browse/GEOS-3546) Port 'using image mosiac plugin' page to new docs
