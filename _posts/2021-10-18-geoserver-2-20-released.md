---
author: Andrea Aime
date: 2021-10-18
layout: post
title: GeoServer 2.20.0 Released
categories:
- Announcements
tags:
- Release
release: release_220
version: 2.20.0
jira_version: 16828
---

We are happy to announce GeoServer [2.20](/release/2.20.0/) release candidate is available for testing. Downloads are available ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.0/geoserver-2.20.0-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.0/geoserver-2.20.0-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.0/GeoServer-2.20.0-winsetup.exe/download)) along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.0/geoserver-2.20.0-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.0/extensions/).

This is the first stable release of the 2.20.x series, made in conjunction with GeoTools 26.0 and GeoWebCache 1.20.

## Internationalization

The leading feature for this release is the internationalization of Title, Abstract and Contact details for:

* WMS 1.1 and 1.3
* WFS 2.0
* WCS 2.0

See documentation for [internationalization support](https://docs.geoserver.org/latest/en/user/services/internationalization/index.html) and [GSIP-203 proposal](https://github.com/geoserver/geoserver/wiki/GSIP-203) for details.

New feature:

* [GEOS-10123](https://osgeo-org.atlassian.net/browse/GEOS-10123) Internationalization for title and abstract
* [GEOS-10207](https://osgeo-org.atlassian.net/browse/GEOS-10207) Allow creation of internationalized raster legends
* [GEOS-10190](https://osgeo-org.atlassian.net/browse/GEOS-10190) i18n support for Contact Information
* [GEOS-10185](https://osgeo-org.atlassian.net/browse/GEOS-10185) LayerGroup legend internationalization styles returns multiple values
* [GEOS-10177](https://osgeo-org.atlassian.net/browse/GEOS-10177) Allow Default Translation
* [GEOS-10129](https://osgeo-org.atlassian.net/browse/GEOS-10129) Add language function for multilingual support in sld

Improvements and fixes:

* [GEOS-10205](https://osgeo-org.atlassian.net/browse/GEOS-10205) Layer with i18n title might appear twice in the capabilities, while being contained in a named tree
* [GEOS-10204](https://osgeo-org.atlassian.net/browse/GEOS-10204) Default locale is not being used while producing internationalized outputs in Capabilities document
* [GEOS-10160](https://osgeo-org.atlassian.net/browse/GEOS-10160) Requested Language in GetCapabilities


![Configuring multiple languages for title and abstract](/img/posts/2.20/i18n.png)<br/>

## Modules Status Information for Extensions

Thanks to Ian for completing a [long outstanding request][https://osgeo-org.atlassian.net/browse/GEOS-10067] to provide listing everything you have installed:

* The Server Status page now provides a complete list of the loaded modules and extensions
* This extension list can also be checked via REST API (allowing scripts to check if the functionality they require has been installed)

New Feature:

* [GEOS-10067](https://osgeo-org.atlassian.net/browse/GEOS-10067) Implement module status in extensions ([GISP-143](https://github.com/bencaradocdavies/geoserver/wiki/GSIP-143))

Improvements and fixes:

* [GEOS-9967](https://osgeo-org.atlassian.net/browse/GEOS-9967) Add Module Status implementation for CSW Extension


![Module listing in the status page](/img/posts/2.20/modules.png)<br/>

## Updates and quality assurance

GeoServer continues to be build with the latest open source technologies:

* GeoTools 26-RC
* GeoWebCache 1.20-RC
* JAI-EXT 1.1.20
* ImageIO-EXT 1.3.10
* JTS 1.18.2
* GeoFence 3.5.0
* Flatgeobuf to 3.10.1

The team continues to work with automated code checks, gradually improving the codebase and introducing checks to ensure issues are not re-introduced over time:

* Check system.out.println and printStackTrace statements are not accidentally committed, which can add to logs
* Cognitive complexity checks, start cleaning up methods that are too complex
* Use StandardCharsets when possible, rather than String
* Avoid unnecessary object wrapper creation
* Use short arrays initializers
* Work towards consistent style with checks to avoid C style array declarations, add missing @Override annotations, and check java generics are used

This dedication helps provide confidence in the technology we publish.

### WMS

Fixes and improvements:

* [GEOS-4939](https://osgeo-org.atlassian.net/browse/GEOS-4939) Coordinate system ISSUE - S-JTSK Krovak East North (`EPSG: 5514`) - cannot be set up
* [GEOS-10032](https://osgeo-org.atlassian.net/browse/GEOS-10032) Group Layer in Catalog Mode Hide not in capabilities when unauthenticated
* [GEOS-10013](https://osgeo-org.atlassian.net/browse/GEOS-10013) Mark invalid error while validating or saving a Style
* [GEOS-9907](https://osgeo-org.atlassian.net/browse/GEOS-9907) Enable usage of labelPoint function in GetFeatureInfo requests
* [GEOS-9759](https://osgeo-org.atlassian.net/browse/GEOS-9759) Set Response Cache Headers in LayerGroups

The following functionality has been removed:

* [GEOS-10001](https://osgeo-org.atlassian.net/browse/GEOS-10001) Remove animator and animated GIF support from WMS
  
  Use of WPS Animation process is provided as an alternative

## WFS

Fixes and improvements:

* [GEOS-10222](https://osgeo-org.atlassian.net/browse/GEOS-10222) WFS CSV OutputFormat delimiter

## WPS

Fixes and improvements:

* [GEOS-9990](https://osgeo-org.atlassian.net/browse/GEOS-9990) Add GUI and REST API to configure the wps-download module
* [GEOS-10073](https://osgeo-org.atlassian.net/browse/GEOS-10073) WPS animation download process should report about eventual time mis-matches

## WMTS

Improvements and fixes:

* [GEOS-10008](https://osgeo-org.atlassian.net/browse/GEOS-10008) Have GeoServerTileLayer implementing TileJSONProvider
* [GEOS-9971](https://osgeo-org.atlassian.net/browse/GEOS-9971) GeoWebCache S3 plugin require AWS creds


## INSPIRE Extension

New feature:

* [GEOS-10124](https://osgeo-org.atlassian.net/browse/GEOS-10124) Add Language support to INSPIRE extension

Improvements and fixes:

* [GEOS-10211](https://osgeo-org.atlassian.net/browse/GEOS-10211) Unable to pass INSPIRE validation: Version is mandatory \(WMS\)
* [GEOS-10192](https://osgeo-org.atlassian.net/browse/GEOS-10192) Inspire extension consistent outputResponse element
* [GEOS-10141](https://osgeo-org.atlassian.net/browse/GEOS-10141) Inspire extension better error message on language not found
* [GEOS-10163](https://osgeo-org.atlassian.net/browse/GEOS-10163) Incorrect INSPIRE namespace URI

## And more!

Fixes and Improvements:

* [GEOS-10092](https://osgeo-org.atlassian.net/browse/GEOS-10092) Fix the page description of remote WMS/WMTS connection
* [GEOS-10189](https://osgeo-org.atlassian.net/browse/GEOS-10189) I18n improvement using the UTF-8 charset for Chinese translations
* [GEOS-10033](https://osgeo-org.atlassian.net/browse/GEOS-10033) Geoserver startup and shutdown shell scripts don't handle path with spaces
* [GEOS-9381](https://osgeo-org.atlassian.net/browse/GEOS-9381) Conversion from boolean true/false in geoserver to SQL Server bit 0/1, is broken
* [GEOS-9970](https://osgeo-org.atlassian.net/browse/GEOS-9970) MapML GetFeature bug fix for CRS authority
* [GEOS-10201](https://osgeo-org.atlassian.net/browse/GEOS-10201) Geoserver fails to start on Windows 11 beta
* [GEOS-10264](https://osgeo-org.atlassian.net/browse/GEOS-10264) Address startup warning File option not set for appender \[geoserverlogfile\]
* [GEOS-9950](https://osgeo-org.atlassian.net/browse/GEOS-9950) MapPreviewPage logs unable to find property: format.wfs.text/csv continuously
* [GEOS-10265](https://osgeo-org.atlassian.net/browse/GEOS-10265) WFS-T Bulk Transaction optimization


## About GeoServer 2.20

Additional information on GeoServer 2.20 series:

  * [Internationalization of title and abstract](https://docs.geoserver.org/latest/en/user/services/internationalization/index.html)
  * [State of GeoServer 2.20 edition](https://docs.google.com/presentation/d/19Cmld0_VFePh1g4qUSfqNWWB0t-teClFpT3eUqpYGos/edit?usp=sharing)

