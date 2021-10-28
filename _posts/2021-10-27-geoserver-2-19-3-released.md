---
layout: post
title: GeoServer 2.19.3 Released
date: 2021-10-27
release: release_219
version: 2.19.3
jira_version: 16824
categories: 
 - Announcements
tags:
 - Release
---
# GeoServer 2.19.3 Released

The GeoServer team are happy to announce GeoServer
[2.19.3](/release/2.19.3/) release is available for download
([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.3/geoserver-2.19.3-bin.zip/download)
and
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.3/geoserver-2.19.3-war.zip/download))
along with
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.3/geoserver-2.19.3-htmldoc.zip/download)
and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.3/extensions/).
 
 This GeoServer 2.19.3 release was produced in conjunction with GeoTools 25.3, this is a maintenance release recommended for production systems.
 
 Thanks to everyone who contributed, and to Ian Turton (Astun Technology) for making this release.
 
## Improvements and Fixes

### Bug

+ [[GEOS-9937](https://osgeo-org.atlassian.net/browse/GEOS-9937)] - Name of styles with colons are incorrect in REST API
+ [[GEOS-10072](https://osgeo-org.atlassian.net/browse/GEOS-10072)] - WMS dimension default values and nearest match can pollute caches (in GWC and beyond)
+ [[GEOS-10132](https://osgeo-org.atlassian.net/browse/GEOS-10132)] - Deadlock at org.geotools.xsd.XSD.getSchema
+ [[GEOS-10133](https://osgeo-org.atlassian.net/browse/GEOS-10133)] - Connecting to WMS Service via Http Proxy
+ [[GEOS-10158](https://osgeo-org.atlassian.net/browse/GEOS-10158)] - POST request -> j_spring_security_check is in http plain even if proxy base url is in https
+ [[GEOS-10161](https://osgeo-org.atlassian.net/browse/GEOS-10161)] - Smart data loader missing PostgreSQL type in DomainModelBuilder
+ [[GEOS-10162](https://osgeo-org.atlassian.net/browse/GEOS-10162)] - GeoServerOAuthAuthenticationFilter creates Anonymous authentication when preAuthenticated principal is not present
+ [[GEOS-10173](https://osgeo-org.atlassian.net/browse/GEOS-10173)] - CoverageViewReader's format not being secured with Geofence-Geoserver
+ [[GEOS-10188](https://osgeo-org.atlassian.net/browse/GEOS-10188)] - Features templating when deleting a templateInfo all the template contents will be deleted
+ [[GEOS-10193](https://osgeo-org.atlassian.net/browse/GEOS-10193)] - Indirect imports will drop the target table if there is any failure during the import process
+ [[GEOS-10198](https://osgeo-org.atlassian.net/browse/GEOS-10198)] - Features Templating - TemplateRuleService save rule bug
+ [[GEOS-10200](https://osgeo-org.atlassian.net/browse/GEOS-10200)] - GetLegendGraphic can fail if SCALE removes all rules
+ [[GEOS-10208](https://osgeo-org.atlassian.net/browse/GEOS-10208)] - Broken link in DDS/BIL community plugin documentation
+ [[GEOS-10213](https://osgeo-org.atlassian.net/browse/GEOS-10213)] - WMS requests fail on LayerGroup default style names, when used in GetMap/GetFeatureInfo/GetLegendGraphics
+ [[GEOS-10215](https://osgeo-org.atlassian.net/browse/GEOS-10215)] - Layers nested inside a group maintain their prefix even in workspace specific services
+ [[GEOS-10227](https://osgeo-org.atlassian.net/browse/GEOS-10227)] - Features Templating - Included templates are not reloaded on file modifications
+ [[GEOS-10266](https://osgeo-org.atlassian.net/browse/GEOS-10266)] - Features Templating makes getfeatureinfo fail for raster data
+ [[GEOS-10273](https://osgeo-org.atlassian.net/browse/GEOS-10273)] - GeofenceAccesManager throws index out of bound when requesting nested layerGroups

### New Feature

+ [[GEOS-10063](https://osgeo-org.atlassian.net/browse/GEOS-10063)] - Add XML templating support to features-templating community plug-in
+ [[GEOS-10118](https://osgeo-org.atlassian.net/browse/GEOS-10118)] - Features templating add include directive in xml templates
+ [[GEOS-10153](https://osgeo-org.atlassian.net/browse/GEOS-10153)] - Features templating UI
+ [[GEOS-10154](https://osgeo-org.atlassian.net/browse/GEOS-10154)] - Feature templating - Add HTML template support
+ [[GEOS-10165](https://osgeo-org.atlassian.net/browse/GEOS-10165)] - Features templating add Rest API
+ [[GEOS-10166](https://osgeo-org.atlassian.net/browse/GEOS-10166)] - Features templating - Add CQL profile field in template rule UI
+ [[GEOS-10217](https://osgeo-org.atlassian.net/browse/GEOS-10217)] - Features templating add GetFeatureInfo support

### Improvement

+ [[GEOS-10080](https://osgeo-org.atlassian.net/browse/GEOS-10080)] - Features-templating allows the possibility to reference domain attribute in templates
+ [[GEOS-10081](https://osgeo-org.atlassian.net/browse/GEOS-10081)] - Features-templating allow the encoding of xml attribute in nodes encoded from a Static or Dynamic builder
+ [[GEOS-10119](https://osgeo-org.atlassian.net/browse/GEOS-10119)] - Features templating add managed support and allow simplified templates structure
+ [[GEOS-10172](https://osgeo-org.atlassian.net/browse/GEOS-10172)] - Add support for GeoPackage output in WPS download
+ [[GEOS-10194](https://osgeo-org.atlassian.net/browse/GEOS-10194)] - Improve importer LOGGING
+ [[GEOS-10265](https://osgeo-org.atlassian.net/browse/GEOS-10265)] - WFS-T Bulk Transaction optimization


For details check the [2.19.3](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16824) release notes.
 
## About GeoServer 2.19
 
 Additional information on GeoServer 2.19 series:
 
 • [WMS GetFeatureInfo includes labels from ColorMap ](https://docs.geoserver.org/stable/en/user/tutorials/ GetFeatureInfo/raster.html)
 
 • [Promote WMTS multidim to extension](https://github.com/geoserver/geoserver/wiki/GSIP-196)
 
 • [Promote WPS-Download to extension](https://github.com/geoserver/geoserver/wiki/GSIP-195)
 
 • [Promote params-extractor to extension](https://github.com/geoserver/geoserver/wiki/GSIP-194)
 
 • [Promote GWC-S3 to extension](https://github.com/geoserver/geoserver/wiki/GSIP-193)
 
 • [Promote WPS-JDBC to extension status](https://github.com/geoserver/geoserver/wiki/GSIP-197)
 
 • [Promote MapML to extension status](https://github.com/geoserver/geoserver/wiki/GSIP-200)
 
 • [GeoServer repository transition to main branch](main-branch.html)
 
 Release notes ( [2.19.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16824)\| [2.19.2](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16821)\| [2.19.1](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16816) \| [2.19.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa? projectId=10000&version=16814) \| [2.19-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa? projectId=10000&version=16766) )
