---
author: Peter Smythe
date: 2024-06-18
layout: post
title: GeoServer 2.24.4 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_224
version: 2.24.4
jira_version: 16920
--- 

GeoServer [2.24.4](/release/2.24.4/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.4/geoserver-2.24.4-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.4/geoserver-2.24.4-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.4/GeoServer-2.24.4-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.4/geoserver-2.24.4-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.24.4/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes. It also includes security vulnerability fixes.

GeoServer 2.24.4 is made in conjunction with GeoTools 30.4, and GeoWebCache 1.24.4. 

Thanks to Peter Smythe (AfriGIS) for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is considered an essential upgrade for production systems.

* [CVE-2024-36401](https://github.com/geoserver/geoserver/security/advisories/GHSA-6jj6-gm7p-fcvv) Remote Code Execution (RCE) vulnerability in evaluating property name expressions (Critical)
* [CVE-2024-34696](https://github.com/geoserver/geoserver/security/advisories/GHSA-j59v-vgcr-hxvf) GeoServer About Status lists sensitive Environmental Variables (Moderate)

The use of the CVE system allows the GeoServer team to reach a wider audience than blog posts.  See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Demo Requests page rewritten

The Demo Request page has been rewritten to use JavaScript to issue POST examples. This provides a much better user experience:

* **Show Result** lists the response headers to be viewed along side the returned result (with an option for XML pretty printing).
* **Show Result in a New Page** is available to allow your browser to display the result.

![](/img/posts/2.25/demo-request.png)

![](/img/posts/2.25/demo-response.png)

The **WCS Request Builder** and **WPS Request Builder** demos now have the option to show their results in Demo Requests page. Combined these changes replace the previous practice of using an iframe popup, and have allowed the **TestWfsPost** servlet to be removed.

For more information please see the [Demo requests](https://docs.geoserver.org/latest/en/user/configuration/demos/index.html#demos-demorequests) in the User Guide.

Thanks to David Blasby (GeoCat) for these improvements, made on behalf of the GeoCat Live project.

* [GEOS-11390](https://osgeo-org.atlassian.net/browse/GEOS-11390) Replace TestWfsPost with Javascript Demo Page

## Release notes

New Feature:

* [GEOS-11390](https://osgeo-org.atlassian.net/browse/GEOS-11390) Replace TestWfsPost with Javascript Demo Page

Improvement:

* [GEOS-11311](https://osgeo-org.atlassian.net/browse/GEOS-11311) Show a full stack trace in the JVM stack dump panel
* [GEOS-11369](https://osgeo-org.atlassian.net/browse/GEOS-11369) Additional authentication options for cascaded WMS|WMTS data stores
* [GEOS-11400](https://osgeo-org.atlassian.net/browse/GEOS-11400) About Page Layout and display of build information
* [GEOS-11401](https://osgeo-org.atlassian.net/browse/GEOS-11401) Introduce environmental variables for Module Status page

Bug:

* [GEOS-7183](https://osgeo-org.atlassian.net/browse/GEOS-7183) Demo request/wcs/wps pages incompatible with HTTPS/PKI
* [GEOS-11202](https://osgeo-org.atlassian.net/browse/GEOS-11202) CAS extension doesn't use global "proxy base URL" setting for service ticket
* [GEOS-11331](https://osgeo-org.atlassian.net/browse/GEOS-11331) OAuth2 can throw a " java.lang.RuntimeException: Never should reach this point"
* [GEOS-11332](https://osgeo-org.atlassian.net/browse/GEOS-11332) Renaming style with uppercase/downcase empty the sld file
* [GEOS-11382](https://osgeo-org.atlassian.net/browse/GEOS-11382) The interceptor "CiteComplianceHack" never gets invoked by the Dispatcher Servlet
* [GEOS-11385](https://osgeo-org.atlassian.net/browse/GEOS-11385) Demo Requests functionality does not honour ENV variable PROXY_BASE_URL
* [GEOS-11416](https://osgeo-org.atlassian.net/browse/GEOS-11416) GeoPackage output contains invalid field types when exporting content from PostGIS
* [GEOS-11430](https://osgeo-org.atlassian.net/browse/GEOS-11430) CiteComplianceHack not correctly parsing the context

Task:

* [GEOS-11318](https://osgeo-org.atlassian.net/browse/GEOS-11318) Upgrade postgresql from 42.6.0 to 42.7.2
* [GEOS-11374](https://osgeo-org.atlassian.net/browse/GEOS-11374) Upgrade Spring version from 5.3.33 to 5.3.34
* [GEOS-11375](https://osgeo-org.atlassian.net/browse/GEOS-11375) GSIP 224 - Individual contributor clarification
* [GEOS-11393](https://osgeo-org.atlassian.net/browse/GEOS-11393) Upgrade commons-io from 2.12.0 to 2.16.1
* [GEOS-11395](https://osgeo-org.atlassian.net/browse/GEOS-11395) Upgrade guava from 32.0.0 to 33.2.0
* [GEOS-11397](https://osgeo-org.atlassian.net/browse/GEOS-11397) App-Schema Includes fix Integration Tests
* [GEOS-11402](https://osgeo-org.atlassian.net/browse/GEOS-11402) Upgrade PostgreSQL driver from 42.7.2 to 42.7.3
* [GEOS-11403](https://osgeo-org.atlassian.net/browse/GEOS-11403) Upgrade commons-text from 1.10.0 to 1.12.0
* [GEOS-11404](https://osgeo-org.atlassian.net/browse/GEOS-11404) Upgrade commons-codec from 1.15 to 1.17.0

For the complete list see [2.24.4](https://github.com/geoserver/geoserver/releases/tag/2.24.4) release notes. 

## Community Updates

Community module development:

* [GEOS-11040](https://osgeo-org.atlassian.net/browse/GEOS-11040) Could not get a ServiceInfo for service Features thus could not check if the service is enabled
* [GEOS-11381](https://osgeo-org.atlassian.net/browse/GEOS-11381) Error in OIDC plugin in combination with RoleService
* [GEOS-11412](https://osgeo-org.atlassian.net/browse/GEOS-11412) Remove reference to JDOM from JMS Cluster (as JDOM is no longer in use)

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.24 Series

Additional information on GeoServer 2.24 series:

* [GeoServer 2.24 User Manual](https://docs.geoserver.org/2.24.x/en/user/)
* [Control remote HTTP requests sent by GeoTools/GeoServer](https://github.com/geoserver/geoserver/wiki/GSIP-218)
* [State of GeoServer 2.24.1](https://docs.google.com/presentation/d/1X7iU1fd47frfh1EsN_CdUll0qtMMgPXkkMjaTbejj3g/edit?usp=sharing) (foss4g-asia presentation)
* [Multiple CRS authority support, planetary CRS](https://github.com/geoserver/geoserver/wiki/GSIP-219)
* [Extensive GeoServer Printing improvements](https://docs.geoserver.org/stable/en/user/extensions/printing/configuration.html)
* [Upgraded security policy](https://github.com/geoserver/geoserver/wiki/GSIP-220)

Release notes:
( [2.24.4](https://github.com/geoserver/geoserver/releases/tag/2.24.4)
| [2.24.3](https://github.com/geoserver/geoserver/releases/tag/2.24.3)
| [2.24.2](https://github.com/geoserver/geoserver/releases/tag/2.24.2)
| [2.24.1](https://github.com/geoserver/geoserver/releases/tag/2.24.1)
| [2.24.0](https://github.com/geoserver/geoserver/releases/tag/2.24.0)
| [2.24-RC](https://github.com/geoserver/geoserver/releases/tag/2.24-RC)
) 

