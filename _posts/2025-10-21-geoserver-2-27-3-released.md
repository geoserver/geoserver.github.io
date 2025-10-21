---
author: Jody Garnett
date: 2025-10-21
layout: post
title: GeoServer 2.27.3 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_227
version: 2.27.3
jira_version: 17338
--- 

GeoServer [2.27.3](/release/2.27.3/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.3/geoserver-2.27.3-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.3/geoserver-2.27.3-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.3/GeoServer-2.27.3-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.3/geoserver-2.27.3-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.3/extensions/).

This is a maintenance release of GeoServer providing existing installations with minor updates and bug fixes.
GeoServer 2.27.3 is made in conjunction with GeoTools 33.3, and GeoWebCache 1.27.3. 

Thanks to Jody Garnett (GeoCat) for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is an important upgrade for production systems.

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

## Upgrade instructions

Please take note of the [Upgrade Instructions](https://docs.geoserver.org/2.28.x/en/user/installation/upgrade.html), specifically:

* The global setting Unrestricted XML External Entity Resolution has been replaced with the `ENTITY_RESOLUTION_UNRESTRICTED` application property.
  
  This change primarily affects application schema users that have not yet adopted ``ENTITY_RESOLUTION_ALLOWLIST``. See [update instructions](https://docs.geoserver.org/2.27.x/en/user/installation/upgrade.html#entity-resolution-unrestricted-application-property-geoserver-2-26-4-and-newer) for details.

* Due to a [user interface change](https://docs.geoserver.org/2.27.x/en/user/installation/upgrade.html#keystore-password-link-geoserver-2-26-and-newer),
  it is no longer necessary to generate a masterpw.info when upgrading an older data directory.

  If this file is present from an earlier upgrade, it is still considered a security warning and is noted on the welcome page.

## Attribute Restrictions

Layer **Feature Type Details** has received a major improvement with an **Edit attribute dialog** making it easier
to define the attribute name, description, type, nillability and for the first time **restrictions**.
Attribute restrictions are used limit data values and are included in DescribeFeatureType.

<img src="/img/posts/2.28/add_attribute_options.png" alt="Attribute Restrictions"
 style="display:block; margin-left:auto; margin-right:auto; max-width: 416px; height:auto;"/>

Two types of restrictions are available:

* Options: Used to restrict set of numeric or string values to a provided set.
* Range: Used to restrict numeric values between a minimum inclusive and maximum inclusive limit. 

Thanks to Alessandro Ricchiuti (GeoSolutions) for this powerful improvement.

For more information see [Feature Type Details](https://docs.geoserver.org/2.27.x/en/user/data/webadmin/layers.html#feature-type-details-vector) in the User Manual. 

* [GSIP-234](https://github.com/geoserver/geoserver/wiki/GSIP-234) Advertise and Enforce Attribute Restrictions
* [GEOS-11937](https://osgeo-org.atlassian.net/browse/GEOS-11937) GSIP 234 - Advertise and Enforce Attribute Restrictions

## Legend: Symbology Encoding Functions

This release includes a long-awaited improvement for legend graphic generation - creating a legend graphic when the Symbology Encoding `Recode`, `Interpolate` and `Categorize` functions are used.

``` xml
<Fill>
  <CssParameter name="fill">
    <ogc:Function name="Recode">
      <!-- Value to Transform -->
      <ogc:Function name="strTrim">
        <ogc:PropertyName>SUB_REGION</ogc:PropertyName>
      </ogc:Function>
      <!-- Map of input to output values -->
      <ogc:Literal>N Eng</ogc:Literal>   <ogc:Literal>#6495ED</ogc:Literal>
      <ogc:Literal>Mid Atl</ogc:Literal> <ogc:Literal>#B0C4DE</ogc:Literal>
      <ogc:Literal>S Atl</ogc:Literal>   <ogc:Literal>#00FFFF</oac:Literal>
      <ogc:Literal>E N Cen</ogc:Literal> <ogc:Literal>#9ACD32</ogc:Literal>
      <ogc:Literal>E S Cen</ogc:Literal> <ogc:Literal>#00FA9A</ogc:Literal>
      <ogc:Literal>W N Cen</ogc:Literal> <ogc:Literal>#FFF8DC</ogc:Literal>
      <ogc:Literal>W S Cen</ogc:Literal> <ogc:Literal>#F5DEB3</ogc:Literal>
      <ogc:Literal>Mtn</ogc:Literal>     <ogc:Literal>#F4A460</ogc:Literal>
      <ogc:Literal>Pacific</ogc:Literal> <ogc:Literal>#87CEEB</ogc:Literal>
    </ogc:Function>
  </CssParameter>
</Fill>
```

<img src="/img/posts/2.27/se-fn-legend.png" alt="Symbology Encoding Legend"
 style="display:block; margin-left:auto; margin-right:auto; max-width: 185px; height:auto;"/>
 

Thanks to Andrea Aime (GeoSolutions) for this improvement on behalf of German Aerospace Center (DLR).

* [GEOS-8002](https://osgeo-org.atlassian.net/browse/GEOS-8002) LegendGraphic display using transformation functions (recode, interpolate, categorize)

## Release notes

New Feature:

* [GEOS-11911](https://osgeo-org.atlassian.net/browse/GEOS-11911) Application property ROOT_LOGIN_ENABLED
* [GEOS-11937](https://osgeo-org.atlassian.net/browse/GEOS-11937) GSIP 234 - Advertise and Enforce Attribute Restrictions
* [GEOS-11949](https://osgeo-org.atlassian.net/browse/GEOS-11949) Support MS Excel download from WPS-download
* [GEOS-8002](https://osgeo-org.atlassian.net/browse/GEOS-8002) LegendGraphic display using transformation functions (recode, interpolate, categorize)

Improvement:

* [GEOS-11867](https://osgeo-org.atlassian.net/browse/GEOS-11867) Improve entity resolution
* [GEOS-11892](https://osgeo-org.atlassian.net/browse/GEOS-11892) Column mentioning user that performed last modification for layers and stores list UI
* [GEOS-11914](https://osgeo-org.atlassian.net/browse/GEOS-11914) Using namespaces parameter with virtual services does not work
* [GEOS-11938](https://osgeo-org.atlassian.net/browse/GEOS-11938) Add support for property selection in OGC API Features
* [GEOS-11950](https://osgeo-org.atlassian.net/browse/GEOS-11950) WMS cascade: fully respect ‘restrict to layer bounds’ flag on GetMap requests

Bug:

* [GEOS-4159](https://osgeo-org.atlassian.net/browse/GEOS-4159) Layer from SQL view feature type details not refreshing after editing sql query (and refreshing attributes there)
* [GEOS-11896](https://osgeo-org.atlassian.net/browse/GEOS-11896) WPS map download flips east/west coordinates
* [GEOS-11900](https://osgeo-org.atlassian.net/browse/GEOS-11900) CRS:XY syntax builds isolated CRSs that do not leverage the EPSG database transformation library
* [GEOS-11902](https://osgeo-org.atlassian.net/browse/GEOS-11902) More compact, easier to maintain conformance configuration UI
* [GEOS-11910](https://osgeo-org.atlassian.net/browse/GEOS-11910) JMS Cluster settings Section is not showing properly
* [GEOS-11917](https://osgeo-org.atlassian.net/browse/GEOS-11917) INSPIRE configuration does not get properly saved when OGC API module is included
* [GEOS-11944](https://osgeo-org.atlassian.net/browse/GEOS-11944) GetLegendGraphic Fails When Using RasterSymbolizer With Interval ColorMap And ENV variables
* [GEOS-11946](https://osgeo-org.atlassian.net/browse/GEOS-11946) DirectRasterRenderer may fail on creating AlphaBand from ROI using Lookup

Task:

* [GEOS-11813](https://osgeo-org.atlassian.net/browse/GEOS-11813) Create REST API For Security Providers
* [GEOS-11814](https://osgeo-org.atlassian.net/browse/GEOS-11814) Create a REST API for Filter Chains
* [GEOS-11815](https://osgeo-org.atlassian.net/browse/GEOS-11815) Create authentication filter REST API
* [GEOS-11852](https://osgeo-org.atlassian.net/browse/GEOS-11852) Remove master password info page
* [GEOS-11853](https://osgeo-org.atlassian.net/browse/GEOS-11853) Clarify keystore vs master vs root password
* [GEOS-11854](https://osgeo-org.atlassian.net/browse/GEOS-11854) Generation of security/masterpw.info no longer required
* [GEOS-11869](https://osgeo-org.atlassian.net/browse/GEOS-11869) Replace entity resolution setting with application property
* [GEOS-11881](https://osgeo-org.atlassian.net/browse/GEOS-11881) Update postgis-jdbc
* [GEOS-11898](https://osgeo-org.atlassian.net/browse/GEOS-11898) GeoFence: issues in evaluation of virtual layer services access
* [GEOS-11956](https://osgeo-org.atlassian.net/browse/GEOS-11956) Fix build server WfsCompatibilityTest failure (when testing against "local" GeoServer on port 8080)

For the complete list see [2.27.3](https://github.com/geoserver/geoserver/releases/tag/2.27.3) release notes. 

## Community Updates

Community module development:

* [GEOS-11885](https://osgeo-org.atlassian.net/browse/GEOS-11885) Smart Data Loader does not support postgresql UUID data type
* [GEOS-11887](https://osgeo-org.atlassian.net/browse/GEOS-11887) Features Templating does not returns content type and charset header on OGC-API
* [GEOS-11888](https://osgeo-org.atlassian.net/browse/GEOS-11888) Features Templating does not support CQL2 new syntax
* [GEOS-11961](https://osgeo-org.atlassian.net/browse/GEOS-11961) OSEO layer management: Support creation of image mosaics in CRS other than 4326

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.27 Series

Additional information on GeoServer 2.27 series:

* [GeoServer 2.27 User Manual](https://docs.geoserver.org/2.27.x/en/user/)
* [CITE Certification achieved]({% post_url 2025-07-16-cite-certification %}) 
* [GeoServer 2025 Q2 Developer Update]({% post_url 2025-05-13-developer-update %}) 
* [GeoServer 2025 Roadmap]({% post_url 2025-01-13-roadmap %}) 
* [Content-Security-Policy Headers](https://github.com/geoserver/geoserver/wiki/GSIP-227)
* [OGCAPI Features Extension](https://github.com/geoserver/geoserver/wiki/GSIP-230)
* [File system access isolation](https://github.com/geoserver/geoserver/wiki/GSIP-229)
* [Promote data dir catalog loader to core](https://github.com/geoserver/geoserver/wiki/GSIP-231)
* [Advertise and Enforce Attribute Restrictions](https://github.com/geoserver/geoserver/wiki/GSIP-234)

GeoServer is an [Open Source Geospatial Foundation](https://www.osgeo.org/projects/geoserver/) project supported by a mix of volunteer and [service provider](https://geoserver.org/support/) activity. We reply on [sponsorship](https://geoserver.org/sponsor/) to fund activities beyond the reach of individual contributors.

Release notes:
( [2.27.3](https://github.com/geoserver/geoserver/releases/tag/2.27.3)
| [2.27.2](https://github.com/geoserver/geoserver/releases/tag/2.27.2)
| [2.27.1](https://github.com/geoserver/geoserver/releases/tag/2.27.1)
| [2.27.0](https://github.com/geoserver/geoserver/releases/tag/2.27.0)
) 

