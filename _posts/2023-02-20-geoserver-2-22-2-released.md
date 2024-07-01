---
author: Jody Garnett
date: 2023-02-20
layout: post
title: GeoServer 2.22.2 Release
categories:
- Announcements
tags:
- Release
release: release_222
version: 2.22.2
jira_version: 16876
---

GeoServer [2.22.2](/release/2.22.2/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.2/geoserver-2.22.2-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.2/geoserver-2.22.2-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.2/GeoServer-2.22.2-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.2/geoserver-2.22.2-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.2/extensions/).

This is a stable release of the GeoServer 2.22.x series, made in conjunction with GeoTools 28.2 
and GeoWebCache 1.22.1.

This release was scheduled early to address a [security vulnerability]({% post_url 2023-02-20-ogc-filter-injection %}). Thanks to Jody Garnett for making this release on behalf of GeoCat Live.

### Security Considerations

This release addresses a security vulnerability and is considered an essential upgrade for production systems:

* [CVE-2023-25158 OGC Filter SQL Injection Vulnerabilities](https://github.com/geotools/geotools/security/advisories/GHSA-99c3-qc2q-p94m) (GeoTools)
* [CVE-2023-25157 OGC Filter SQL Injection Vulnerabilities](https://github.com/geoserver/geoserver/security/advisories/GHSA-7g5f-wrx8-5ccf) (GeoServer)

For more information see [OGC Filter Injection Vulnerability Statement]({% post_url 2023-02-20-ogc-filter-injection %}). 

* [GEOT-7302 Escape user inputs in SQL queries](https://osgeo-org.atlassian.net/browse/GEOT-7302)
* [GEOS-10842 JDBCConfig: escape user inputs in SQL queries](https://osgeo-org.atlassian.net/browse/GEOS-10842)
* [GEOS-10839 JDBCConfig: add JDBC Configuration parameter to disable SQL comments and pretty-printing](https://osgeo-org.atlassian.net/browse/GEOS-10839)

**2024-06-30 Update:** The following mitigation has been provided:

* [CVE-2024-36401](https://github.com/geoserver/geoserver/security/advisories/GHSA-6jj6-gm7p-fcvv) Remote Code Execution (RCE) vulnerability in evaluating property name expressions (Critical)

  A [patch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.2/geoserver-2.22.2-patches.zip/download) (replacing `gt-app-schema`, `gt-complex` and `gt-xsd-core` jars) has been provided by Andrea (GeoSolutions)

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

### Natural Earth 50m Sample Data

The Natural Earth ``ne`` workspace has been improved with 1:50m sample data offering the following:

* improved detail
* country labels in multiple languages
* disputed regions

![World 50m Update](/img/posts/2.22/ne50_update.png) <br/>

The ``countries.sld`` style includes the following:

```xml
<sld:TextSymbolizer>
  <sld:Label>
    <ogc:Function name="Recode">
      <ogc:Function name="language"/>
      <ogc:Literal/>
      <ogc:PropertyName>NAME</ogc:PropertyName>
      <ogc:Literal>en</ogc:Literal>
      <ogc:PropertyName>NAME</ogc:PropertyName>
      <ogc:Literal>it</ogc:Literal>
      <ogc:PropertyName>NAME_IT</ogc:PropertyName>
      <ogc:Literal>fr</ogc:Literal>
      <ogc:PropertyName>NAME_FR</ogc:PropertyName>
    </ogc:Function>
  </sld:Label>
```

To try this out in French append ``&LANGUAGE=fr`` to any GetMap request, including Layer Preview.

![World 50m French](/img/posts/2.22/ne50_update_fr.png) <br/>

These styles also now validate. Thanks to Jody Garnett (GeoCat) for this work.

* [GEOS-10624](https://osgeo-org.atlassian.net/browse/GEOS-10624) Data directory and documentation update
* [GEOS-10836](https://osgeo-org.atlassian.net/browse/GEOS-10836) The demo styles in "ne" workspace do not validate

### Welcome Page Performance Improvements

The welcome page loading is now limited to a short amount of time to retrieve the list of workspaces and layers to select from. For large catalogues, with lots of security restrictions, that are unable to respond in this time, a simple text field is provided.

![Welcome Dropdown Selection](/img/posts/2.22/welcome_dropdown.png) <br/>

To force the use of a simple text field the property ``GeoServerHomePage.selectionMode=TEXT`` can be used. Use ``DROPDOWN`` to force a selection control to be used, or ``AUTOMATIC`` to determine the behaviour based on catalogue performance as described above.

The default time out ``GeoServerHomePage.selectionTimeout=5000`` for interaction can be adjusted if you would like to provide the catalogue more time to respond. 

By default ``GeoServerHomePage.selectionMaxItems=1000`` workspaces or layers can be loaded. This number may be limited further if you find browser performance is affected.

Thanks to Andrea (GeoSolutions) for these performance improvements, and Jody Garnett for a number of smaller fixes.


* [GEOS-10833](https://osgeo-org.atlassian.net/browse/GEOS-10833) GeoServerHomePage unresponsive against large catalogs

* [GEOS-10759](https://osgeo-org.atlassian.net/browse/GEOS-10759) Welcome page unreachable with large / slow catalogue configuration

* [GEOS-10838](https://osgeo-org.atlassian.net/browse/GEOS-10838) Speed up DefaultResourceAccessManager securityFilter implementation

* [GEOS-10834](https://osgeo-org.atlassian.net/browse/GEOS-10834) Catalog.list might require a lot of time due to security filtering

* [GEOS-10847](https://osgeo-org.atlassian.net/browse/GEOS-10847) Selecting a raster layer in home page shows incorrect services

* [GEOS-10861](https://osgeo-org.atlassian.net/browse/GEOS-10861) Welcome blurb i18n not respecting language switch

### Community Modules

OGC API updates:

* [GEOS-10860](https://osgeo-org.atlassian.net/browse/GEOS-10860) OGC API should return version including minor and patch in HTTP Response Header

* [GEOS-10828](https://osgeo-org.atlassian.net/browse/GEOS-10828) OGC API - Features - Plugin breaks core \`/rest\` API with JSON payloads

The JDBC Config module received several important fixes:

* [GEOS-10814](https://osgeo-org.atlassian.net/browse/GEOS-10814) Update jdbc config to use consistent SQL formatting

* [GEOS-10813](https://osgeo-org.atlassian.net/browse/GEOS-10813) jdbc config cache bug

* [GEOS-10829](https://osgeo-org.atlassian.net/browse/GEOS-10829) JDBC Config missing some nested layer properties

* [GEOS-10842](https://osgeo-org.atlassian.net/browse/GEOS-10842) Escape user inputs in SQL queries


### Release notes

Improvement:

* [GEOS-10851](https://osgeo-org.atlassian.net/browse/GEOS-10851) GWC S3 Blobstore Parameters  Get Converted back to plain text after an application restart

Bug:

* [GEOS-7506](https://osgeo-org.atlassian.net/browse/GEOS-7506) shutdown.bat cannot run without JAVA\_HOME set

* [GEOS-10689](https://osgeo-org.atlassian.net/browse/GEOS-10689) OSHISystemInfoCollector holds non daemon threads, prevents clean shutdown of Tomcat

* [GEOS-10846](https://osgeo-org.atlassian.net/browse/GEOS-10846) Enable auto-escaping for REST HTML templates

Task:

* [GEOS-10683](https://osgeo-org.atlassian.net/browse/GEOS-10683) FileWrapperResourceTheoryTest fails on Windows since Java 11

* [GEOS-10848](https://osgeo-org.atlassian.net/browse/GEOS-10848) Column remarks documentation should be updated to reflect that functionality is supported with JNDI

For complete information see [2.22.2 release 
notes](https://github.com/geoserver/geoserver/releases/tag/2.22.2).

## About GeoServer 2.22

Additional information on GeoServer 2.22 series:

* [Update Instructions](https://docs.geoserver.org/latest/en/user/installation/upgrade.html)
* [Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/metadata/index.html)
* [CSW ISO Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/csw-iso/index.html)
* [State of GeoServer](https://docs.google.com/presentation/d/1mnOFSvYb8npVudvUR5MSjSTFHc6ZQ_bStafZrBV7LZ8/edit?usp=sharing) (FOSS4G Presentation)
* [GeoServer Beginner Workshop](https://docs.google.com/presentation/d/1fbPLN-1Cs95WK-IxDG1PxCEKyHwFbNBGNkkomxmLr0Y/edit?usp=sharing) (FOSS4G Workshop)
* [Welcome page](https://docs.geoserver.org/latest/en/user/webadmin/welcome.html) (User Guide)

Release notes:
( [2.22.2](https://github.com/geoserver/geoserver/releases/tag/2.22.2)
| [2.22.1](https://github.com/geoserver/geoserver/releases/tag/2.22.1)
| [2.22.0](https://github.com/geoserver/geoserver/releases/tag/2.22.0)
| [2.22-RC](https://github.com/geoserver/geoserver/releases/tag/2.22-RC)
| [2.22-M0](https://github.com/geoserver/geoserver/releases/tag/2.22-M0)
)
