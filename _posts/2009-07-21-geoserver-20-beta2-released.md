---
author: geoserver
comments: true
date: 2009-07-21 15:43:29+00:00
layout: post
link: http://blog.geoserver.org/2009/07/21/geoserver-20-beta2-released/
slug: geoserver-20-beta2-released
title: GeoServer 2.0-beta2 Released
wordpress_id: 230
categories:
- Announcements
tags:
- beta
- complex
- Features
- release
---

The GeoServer community is happy to announce the second beta release of GeoServer 2.0, available for download. The developers have been working hard to get the [new user interface]({% post_url 2009-06-03-geoserver-20-now-in-beta %}) up to the quality and functionality of the existing interface. This release of 2.0-beta2 brings us [74 issues](#release-notes) closer to that goal.

The most noteworthy feature for 2.0-beta2 is the official inclusion of the [app-schema extension](http://docs.geoserver.org/trunk/user/tutorials/app-schema/index.html). Most people probably know app-schema better as **complex features**, a feature GeoServer has been striving toward for the past three years. The extension gives GeoServer WFS the ability to support complex feature application schemas such as [GeoSciML](http://en.wikipedia.org/wiki/GeoSciML). Much thanks goes out to Ben Caradoc-Davies, Rini Angreani, and the rest of the [AuScope](http://www.auscope.org.au/)* team for seeing this work through and actually making complex feature support a reality in GeoServer.

For those who missed the previous [post]({% post_url 2009-07-03-geoserver-app-schema-meeting-in-perth-western-australia %}) about it, Ben and the folks from AuScope recently hosted a complex feature workshop in Perth, Australia, in which a number of the GeoServer developers were brought out. Special thanks for AuScope for hosting the event, which was a great success.

A special thanks also goes out to users who have been downloading the 2.0 alpha and beta releases, trying them out and reporting bugs. The more bug reports we get the faster we can get to the official 2.0 release. This should be the final beta release of 2.0 before it moves into release candidate phase, so stay tuned for RC1 coming soon.

* AuScope Ltd is funded under the National Collaborative Research Infrastructure Strategy (NCRIS), an Australian Commonwealth Government Programme.

----

## GeoServer 2.0-beta2

Released on July 13, 2009

#### Download format

- [Binary (OS independent)](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/geoserver-2.0-beta2-bin.zip/download)
- [Web Archive](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/geoserver-2.0-beta2-war.zip/download)

(NEW!) [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/geoserver-2.0-beta2-ng.exe/download)

- [Legacy Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/geoserver-2.0-beta2.exe/download)
- [Mac OS X Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/geoserver-2.0-beta2.dmg/download)
- [Source Code](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/geoserver-2.0-beta2-src.zip/download)

#### Documentation

- [HTML Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/geoserver-2.0-beta2-htmldoc.zip/download)
- [PDF Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/geoserver-2.0-beta2-pdfdoc.zip/download)
- [API Documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/geoserver-2.0-beta2-javadoc.zip/download)
- [Release Notes](#release-notes)

#### Extensions

**Datastore**

- [Application Schema Support](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/extensions/geoserver-2.0-beta2-app-schema-plugin.zip/download)
- [ArcSDE](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/extensions/geoserver-2.0-beta2-arcsde-plugin.zip/download)
- [DB2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/extensions/geoserver-2.0-beta2-db2-plugin.zip/download)
- [H2](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/extensions/geoserver-2.0-beta2-h2-plugin.zip/download)
- [MySQL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/extensions/geoserver-2.0-beta2-mysql-plugin.zip/download)
- [Pregeneralized features](http://downloads.sourceforge.net/geoserver/geoserver-2.0-beta2-features-pregeneralized-plugin.zip)
- [Oracle](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/extensions/geoserver-2.0-beta2-oracle-plugin.zip/download)
- [VPF](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/extensions/geoserver-2.0-beta2-vpf-plugin.zip/download)

**Coveragestore**

- [GDAL](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/extensions/geoserver-2.0-beta2-gdal-plugin.zip/download)
- [Image Pyramid](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/extensions/geoserver-2.0-beta2-pyramid-plugin.zip/download)

**Other**

- [Charting](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/extensions/geoserver-2.0-beta2-charts-plugin.zip/download)
- [Excel Output Format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/extensions/geoserver-2.0-beta2-excel-plugin.zip/download)
- [Image Map](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/extensions/geoserver-2.0-beta2-imagemap-plugin.zip/download)
- [OGR Output Format](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/extensions/geoserver-2.0-beta2-ogr-plugin.zip/download)
- [WFS Versioning](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/extensions/geoserver-2.0-beta2-wfsv-plugin.zip/download)

#### [SourceForge](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0-beta2/)

SourceForge Release 696646.

#### [JIRA](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS)

JIRA Version 15284

## Release notes

New Feature:

* [GEOS-1951](https://osgeo-org.atlassian.net/browse/GEOS-1951) New Configuration System
* [GEOS-3085](https://osgeo-org.atlassian.net/browse/GEOS-3085) Add a memory allocation limit to WMS requests
* [GEOS-3086](https://osgeo-org.atlassian.net/browse/GEOS-3086) Add a response time limit to WMS requests
* [GEOS-3087](https://osgeo-org.atlassian.net/browse/GEOS-3087) Add an error count limit for WMS rendering requests
* [GEOS-3181](https://osgeo-org.atlassian.net/browse/GEOS-3181) Attribution Support for WMS Capabilities

Improvement:

* [GEOS-2733](https://osgeo-org.atlassian.net/browse/GEOS-2733) Various datastore page improvements
* [GEOS-2836](https://osgeo-org.atlassian.net/browse/GEOS-2836) Add "friendly" names to "All formats" dropdown list on preview page
* [GEOS-3048](https://osgeo-org.atlassian.net/browse/GEOS-3048) Allow NewLayerPage to filter on layer names
* [GEOS-3074](https://osgeo-org.atlassian.net/browse/GEOS-3074) FilePublisher should return binary type for all not known mime types
* [GEOS-3082](https://osgeo-org.atlassian.net/browse/GEOS-3082) Make sure datastore have meaningful default values for common fields
* [GEOS-3145](https://osgeo-org.atlassian.net/browse/GEOS-3145) Direct users to a JDK download from the Windows Installer
* [GEOS-3159](https://osgeo-org.atlassian.net/browse/GEOS-3159) Create a class which abstracts file system access to data directory
* [GEOS-3164](https://osgeo-org.atlassian.net/browse/GEOS-3164) Change metadata on catalog and config objects to be a type safe converting map
* [GEOS-3167](https://osgeo-org.atlassian.net/browse/GEOS-3167) CatalogBuilder.buildFeatureType should be made more tolerant and split up
* [GEOS-3171](https://osgeo-org.atlassian.net/browse/GEOS-3171) Simplify GeoserverTablePanel setup
* [GEOS-3185](https://osgeo-org.atlassian.net/browse/GEOS-3185) Switch default KML generation mode to refresh
* [GEOS-3189](https://osgeo-org.atlassian.net/browse/GEOS-3189) collapsible menu
* [GEOS-3212](https://osgeo-org.atlassian.net/browse/GEOS-3212) Provide an explicit login page for people directly accessing secure pages bypassing the home page
* [GEOS-3236](https://osgeo-org.atlassian.net/browse/GEOS-3236) Wicket UI page `<title>` element should reflect actual page title
* [GEOS-3237](https://osgeo-org.atlassian.net/browse/GEOS-3237) Menu links do not use the MenuPageInfo descriptoin key, their title is stuck to "title"

Bug:

* [GEOS-1511](https://osgeo-org.atlassian.net/browse/GEOS-1511) kill GetMapKvpReader, port GetMapXmlReader to GetMapKvpRequestReader
* [GEOS-2871](https://osgeo-org.atlassian.net/browse/GEOS-2871) Capabilities link do not show up on WMS 1.1 data dir
* [GEOS-2884](https://osgeo-org.atlassian.net/browse/GEOS-2884) Unable to add two layers with the same name
* [GEOS-2933](https://osgeo-org.atlassian.net/browse/GEOS-2933) URL field of demo request page is not used for actual query
* [GEOS-2984](https://osgeo-org.atlassian.net/browse/GEOS-2984) GeoServer won't build with Maven 2.1.0
* [GEOS-3024](https://osgeo-org.atlassian.net/browse/GEOS-3024) PostGIS Error when adding data store
* [GEOS-3049](https://osgeo-org.atlassian.net/browse/GEOS-3049) Failure to connect to a data store prevents WFS GetFeature to work on any other layer
* [GEOS-3071](https://osgeo-org.atlassian.net/browse/GEOS-3071) WFS 1.1 - h2 - xlink data directory oudated on trunk
* [GEOS-3072](https://osgeo-org.atlassian.net/browse/GEOS-3072) web2 FileExistsValidatorTest.testAbsoluteRaw() fails on Windows, breaking the build
* [GEOS-3075](https://osgeo-org.atlassian.net/browse/GEOS-3075) GetMap with remote SLD results in ClassCastException
* [GEOS-3076](https://osgeo-org.atlassian.net/browse/GEOS-3076) GetLegendGraphics with width/height results in a ClassCastException
* [GEOS-3077](https://osgeo-org.atlassian.net/browse/GEOS-3077) GetMap with inline SLD throws service exception about missing layers
* [GEOS-3088](https://osgeo-org.atlassian.net/browse/GEOS-3088) A SoreInfo can't be saved if the coverage/data store can't be accessed. Not even to just disable the store
* [GEOS-3091](https://osgeo-org.atlassian.net/browse/GEOS-3091) ResourceConfigurationPage leaves the list of attributes empty
* [GEOS-3094](https://osgeo-org.atlassian.net/browse/GEOS-3094) Deleting styles with shared resources causes runtime exception
* [GEOS-3105](https://osgeo-org.atlassian.net/browse/GEOS-3105) Editing a file based coverage store with a relative URL always fails
* [GEOS-3106](https://osgeo-org.atlassian.net/browse/GEOS-3106) Disabling a Store does not disable it's layers, and they can still be accessed
* [GEOS-3107](https://osgeo-org.atlassian.net/browse/GEOS-3107) Watermarks applied to entire metatile rather than each tile within it
* [GEOS-3113](https://osgeo-org.atlassian.net/browse/GEOS-3113) schema encoder should respect prefix in the schema.xsd and schema.xml files
* [GEOS-3116](https://osgeo-org.atlassian.net/browse/GEOS-3116) Wicket serialization issue on datastore new page
* [GEOS-3119](https://osgeo-org.atlassian.net/browse/GEOS-3119) Data/CoverageStore New/Edit pages do now show errors anymore
* [GEOS-3120](https://osgeo-org.atlassian.net/browse/GEOS-3120) NewLayerPage shows published resources as non published
* [GEOS-3122](https://osgeo-org.atlassian.net/browse/GEOS-3122) ReverseProxy failing to engage in 2.0.x
* [GEOS-3137](https://osgeo-org.atlassian.net/browse/GEOS-3137) GeoServer assembly generates and empty geoserver-`<version>`-doc.zip file
* [GEOS-3140](https://osgeo-org.atlassian.net/browse/GEOS-3140) The feature-pregeneralized plugin does not follow other plugins naming convention
* [GEOS-3142](https://osgeo-org.atlassian.net/browse/GEOS-3142) If a layer fails to be added/saved when a resource/layer combo is saved then the resource becomes stale
* [GEOS-3144](https://osgeo-org.atlassian.net/browse/GEOS-3144) Disable query filter validation for non-simple feature types
* [GEOS-3146](https://osgeo-org.atlassian.net/browse/GEOS-3146) The list of styles can't be sorted, it's a ModificationProxy$list
* [GEOS-3165](https://osgeo-org.atlassian.net/browse/GEOS-3165) Non spatial feature types can't be configured through the Wicket UI
* [GEOS-3169](https://osgeo-org.atlassian.net/browse/GEOS-3169) Adjusting a standard query in the demo requests has no effect. The standard query is what gets fired.
* [GEOS-3178](https://osgeo-org.atlassian.net/browse/GEOS-3178) startup.bat doesn't like pathnames with spaces
* [GEOS-3180](https://osgeo-org.atlassian.net/browse/GEOS-3180) Shapefile download - problem if null geometries
* [GEOS-3191](https://osgeo-org.atlassian.net/browse/GEOS-3191) Unable to prevent geoserver.log from being written to .\logs
* [GEOS-3192](https://osgeo-org.atlassian.net/browse/GEOS-3192) Namespaces omitted for some layers in wms capabilities
* [GEOS-3195](https://osgeo-org.atlassian.net/browse/GEOS-3195) Double Titles
* [GEOS-3204](https://osgeo-org.atlassian.net/browse/GEOS-3204) Compute from native bounds does not work if there is no native SRS
* [GEOS-3207](https://osgeo-org.atlassian.net/browse/GEOS-3207) WKT link blows up if no SRS defition is available
* [GEOS-3210](https://osgeo-org.atlassian.net/browse/GEOS-3210) filtering property names does not work properly with aliased feature type with json output
* [GEOS-3213](https://osgeo-org.atlassian.net/browse/GEOS-3213) CatalogBuilder might build envelopes with zero area
* [GEOS-3220](https://osgeo-org.atlassian.net/browse/GEOS-3220) Native bounding box is not editable in Wicket UI
* [GEOS-3231](https://osgeo-org.atlassian.net/browse/GEOS-3231) Remove CompositeConverterLocator
* [GEOS-3245](https://osgeo-org.atlassian.net/browse/GEOS-3245) Allow Wicket configuration (development/deployment) to be configured the usual GeoServer way
* [GEOS-3247](https://osgeo-org.atlassian.net/browse/GEOS-3247) WFS GetCapabilities publishes FeatureTypes with non prefixed type names

Task:

* [GEOS-552](https://osgeo-org.atlassian.net/browse/GEOS-552) Community Schema Support
* [GEOS-2109](https://osgeo-org.atlassian.net/browse/GEOS-2109) Implement Coverage Config page
* [GEOS-2979](https://osgeo-org.atlassian.net/browse/GEOS-2979) Reflectively set collection properties to NullObjects on CatalogImpl.resolve
* [GEOS-3078](https://osgeo-org.atlassian.net/browse/GEOS-3078) Move web2 into core
* [GEOS-3083](https://osgeo-org.atlassian.net/browse/GEOS-3083) Document usage of JNDI Connection pools in GeoServer
* [GEOS-3090](https://osgeo-org.atlassian.net/browse/GEOS-3090) ResourceConfigurationPage has no cancel button
* [GEOS-3100](https://osgeo-org.atlassian.net/browse/GEOS-3100) port DataAccess New/Edit page to use proper composite wicket model instead of a MapModel for all properties
* [GEOS-3101](https://osgeo-org.atlassian.net/browse/GEOS-3101) Namespace datastore parameter may be confusing with workspace, show ns prefix too to disambiguate
* [GEOS-3118](https://osgeo-org.atlassian.net/browse/GEOS-3118) Port templates to new data directory structure
* [GEOS-3141](https://osgeo-org.atlassian.net/browse/GEOS-3141) If there're two stores with the same name in different workspaces, it's impossible to know which one to pick on NewLayerPage
* [GEOS-3149](https://osgeo-org.atlassian.net/browse/GEOS-3149) Keep DataAccess namespace param in sync with the workspace's datastore until the resource/publish split is complete
* [GEOS-3211](https://osgeo-org.atlassian.net/browse/GEOS-3211) Port CatalogRepsitory from feature-pregeneralized extension to main
* [GEOS-3250](https://osgeo-org.atlassian.net/browse/GEOS-3250) GSIP 39 - Promote app-schema to extension

Sub-task:

* [GEOS-2992](https://osgeo-org.atlassian.net/browse/GEOS-2992) The url is not pre-filled with file://data/featureTypes
