---
author: Jody Garnett
date: 2024-06-18
layout: post
title: GeoServer 2.25.2 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_225
version: 2.25.2
jira_version: 16923
--- 

GeoServer [2.25.2](/release/2.25.2/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.2/geoserver-2.25.2-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.2/geoserver-2.25.2-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.2/GeoServer-2.25.2-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.2/geoserver-2.25.2-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.25.2/extensions/).

This is a stable release of GeoServer recommended for production use. This release is made ahead of schedule to address an urgent bug or security vulnerability.
GeoServer 2.25.2 is made in conjunction with GeoTools 31.2, and GeoWebCache 1.25.2. 

Thanks to Jody Garnett (GeoCat) for making this release on behalf of GeoCat customers. If you are not in a position to upgrade at this time please consulting the security considerations below for available mitigation measures.

## Security Considerations

This release addresses security vulnerabilities and is considered an essential upgrade for production systems.

* [CVE-2024-36401](https://github.com/geoserver/geoserver/security/advisories/GHSA-6jj6-gm7p-fcvv)

The details of this vulnerability are locked now and will be made available at the end of the month providing an opportunity to update.

The use of the CVE system allows the GeoServer team to reach a wider audience than blog posts. See the project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Demo Requests page rewritten

The Demo Request page has been rewritten use use JavaScript to issue POST examples. This provides a much better user experience:

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

* [GEOS-11351](https://osgeo-org.atlassian.net/browse/GEOS-11351) Exact term search in the pages' filters

Bug:

* [GEOS-7183](https://osgeo-org.atlassian.net/browse/GEOS-7183) Demo request/wcs/wps pages incompatible with HTTPS/PKI
* [GEOS-11416](https://osgeo-org.atlassian.net/browse/GEOS-11416) GeoPackage output contains invalid field types when exporting content from PostGIS
* [GEOS-11430](https://osgeo-org.atlassian.net/browse/GEOS-11430) CiteComplianceHack not correctly parsing the context

Task:

* [GEOS-11411](https://osgeo-org.atlassian.net/browse/GEOS-11411) Upgrade to ImageIO-EXT 1.4.11
* [GEOS-11426](https://osgeo-org.atlassian.net/browse/GEOS-11426) Rework community dependency packaging to use module's dependencies
* [GEOS-11429](https://osgeo-org.atlassian.net/browse/GEOS-11429) Split COG community module packaging based on target cloud provider
* [GEOS-11432](https://osgeo-org.atlassian.net/browse/GEOS-11432) Upgrade to ImageIO-EXT 1.4.12

For the complete list see [2.25.2](https://github.com/geoserver/geoserver/releases/tag/2.25.2) release notes. 

## Community Updates

Community module development:

* [GEOS-11412](https://osgeo-org.atlassian.net/browse/GEOS-11412) Remove reference to JDOM from JMS Cluster (as JDOM is no longer in use)
* [GEOS-11413](https://osgeo-org.atlassian.net/browse/GEOS-11413) STAC uses inefficient dabase queries when asking for collections in JSON format

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.25 Series

Additional information on GeoServer 2.25 series:

* [GeoServer 2.25 User Manual](https://docs.geoserver.org/2.25.x/en/user/)
* [GeoServer 2024 Roadmap Plannings]({% post_url 2024-01-03-roadmap %}) 
* [Raster Attribute Table extension](https://github.com/geoserver/geoserver/wiki/GSIP-222)
* [Individual contributor clarification](https://github.com/geoserver/geoserver/wiki/GSIP-224)

Release notes:
( [2.25.2](https://github.com/geoserver/geoserver/releases/tag/2.25.2)
| [2.25.1](https://github.com/geoserver/geoserver/releases/tag/2.25.1)
| [2.25.0](https://github.com/geoserver/geoserver/releases/tag/2.25.0)
| [2.25-RC](https://github.com/geoserver/geoserver/releases/tag/2.25-RC)
) 

