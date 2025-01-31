---
author: Jody Garnett
date: 2025-01-27
layout: post
title: GeoServer 2.26.2 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_226
version: 2.26.2
jira_version: 16940
--- 

GeoServer [2.26.2](/release/2.26.2/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.2/geoserver-2.26.2-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.2/geoserver-2.26.2-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.2/GeoServer-2.26.2-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.2/geoserver-2.26.2-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.2/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 2.26.2 is made in conjunction with GeoTools 32.2, GeoWebCache 1.26.2, and ImageIO-Ext 1.4.14. 

Thanks to Jody Garnett for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is recommended.

* CVE-2024-38524 Moderate <!-- https://github.com/geoserver/geoserver/security/advisories/GHSA-jm79-7xhw-6f6f -->

<!-- update cve list details when disclosed -->

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

## File System Sandbox Isolation

A file system sandbox is used to limit access for GeoServer Administrators and Workspace Administrators to specified file folders.

* A system sandbox is established using ``GEOSERVER_FILESYSTEM_SANDBOX`` application property, and applies to the entire application, limiting GeoServer administrators to the ``<sandbox>`` folder, and individual workspace administrators into isolated ``<sandbox>/<workspace>`` folders.

* A regular sandbox can be configured from the **Security > Data** screen, and is used to limit individual workspace administrators into ``<sandbox>/<workspace>`` folders to avoid accessing each others files.
  
  ![](/img/posts/2.26/filesystem-sandbox.png)

Thanks to Andrea (GeoSolutions) for this important improvement at the bequest of [Munich RE](https://www.munichre.com/en.html).

- [GSIP 229 - File system access isolation](https://github.com/geoserver/geoserver/wiki/GSIP-229)
- [File system sandboxing](https://docs.geoserver.org/2.26.x/en/user/security/sandbox.html) (User Manual)

## Developer Updates

### Palantir formatter

A nice update for GeoServer developers is an updated formatter that is both wider at 120 columns, and plays well with the use of lamda expressions.

```java
List<TemplateBuilder> filtered = children.stream()
        .filter(b -> b instanceof DynamicValueBuilder || b instanceof SourceBuilder)
        .collect(Collectors.toList());
```

Thanks to Andrea for this improvement, and coordinating the change across all active branches.

- [GSIP 228 - 120 columns format with Palantir formatter](https://github.com/geoserver/geoserver/wiki/GSIP-228)

## Release notes


New Features:

* [GEOS-11616](https://osgeo-org.atlassian.net/browse/GEOS-11616) GSIP 229 - File system access isolation
* [GEOS-11644](https://osgeo-org.atlassian.net/browse/GEOS-11644) Introducing the rest/security/acl/catalog/reload rest endpoint

Improvement:

* [GEOS-11612](https://osgeo-org.atlassian.net/browse/GEOS-11612) Add system property support for Proxy base URL -> use headers activation
* [GEOS-11615](https://osgeo-org.atlassian.net/browse/GEOS-11615) Update to Imageio-EXT 1.4.14
* [GEOS-11683](https://osgeo-org.atlassian.net/browse/GEOS-11683) MapML WMS Features Coordinate Precision Should be adjusted based on scale

Bug:

* [GEOS-11636](https://osgeo-org.atlassian.net/browse/GEOS-11636) Store panels won't always show feedback in target panels
* [GEOS-11494](https://osgeo-org.atlassian.net/browse/GEOS-11494) WFS GetFeature request with a propertyname parameter fails when layer attributes are customized (removed or reordered)
* [GEOS-11606](https://osgeo-org.atlassian.net/browse/GEOS-11606) geofence-server imports obsolete asm dep
* [GEOS-11611](https://osgeo-org.atlassian.net/browse/GEOS-11611) When Extracting the WFS Service Name from the HTTP Request A Slash Before the Question Marks Causes Issues
* [GEOS-11630](https://osgeo-org.atlassian.net/browse/GEOS-11630) REST API throws HTTP 500 When Security Metadata Has Null Attributes
* [GEOS-11643](https://osgeo-org.atlassian.net/browse/GEOS-11643) WCS input read limits can be fooled by geotiff reader
* [GEOS-11647](https://osgeo-org.atlassian.net/browse/GEOS-11647) Restore "quiet on not found" configuration for REST in global settings
* [GEOS-11649](https://osgeo-org.atlassian.net/browse/GEOS-11649) welcome page per-layer is not respecting global service enablement
* [GEOS-11672](https://osgeo-org.atlassian.net/browse/GEOS-11672) GWC virtual services available with empty contents
* [GEOS-11681](https://osgeo-org.atlassian.net/browse/GEOS-11681) MapML raster GetFeatureInfo not working

Task:

* [GEOS-11608](https://osgeo-org.atlassian.net/browse/GEOS-11608) Update Bouncy Castle Crypto package from bcprov-jdk15on:1.69 to bcprov-jdk18on:1.79
* [GEOS-11631](https://osgeo-org.atlassian.net/browse/GEOS-11631) Update MySQL driver to 9.1.0
* [GEOS-11650](https://osgeo-org.atlassian.net/browse/GEOS-11650) Update dependencies for monitoring-kafka module
* [GEOS-11659](https://osgeo-org.atlassian.net/browse/GEOS-11659) Apply Palantir Java format on GeoServer
* [GEOS-11671](https://osgeo-org.atlassian.net/browse/GEOS-11671) Upgrade H3 dependency to 3.7.3
* [GEOS-11685](https://osgeo-org.atlassian.net/browse/GEOS-11685) Bump jetty.version from 9.4.56.v20240826 to 9.4.57.v20241219

For the complete list see [2.26.2](https://github.com/geoserver/geoserver/releases/tag/2.26.2) release notes. 

## Community Updates

Community module development:

* [GEOS-11635](https://osgeo-org.atlassian.net/browse/GEOS-11635) Add support for opaque auth tokens in OpenID connect
* [GEOS-11637](https://osgeo-org.atlassian.net/browse/GEOS-11637) DGGS min/max resolution settings stop working after restart
* [GEOS-11680](https://osgeo-org.atlassian.net/browse/GEOS-11680) Azure COG assembly lacks mandatory libraries, won't work
* [GEOS-11686](https://osgeo-org.atlassian.net/browse/GEOS-11686) Clickhouse DGGS stores cannot properly read dates
* [GEOS-11687](https://osgeo-org.atlassian.net/browse/GEOS-11687) OGC API packages contain gs-web-core
* [GEOS-11691](https://osgeo-org.atlassian.net/browse/GEOS-11691) Smart data loader accepts bigint and bigserial but not int8 postgresql type alias

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.26 Series

{% include 2025-sponsors.html %}

Additional information on GeoServer 2.26 series:

* [GeoServer 2.26 User Manual](https://docs.geoserver.org/2.26.x/en/user/)
* [GeoServer 2025 Roadmap]({% post_url 2025-01-13-roadmap %})
* [GeoServer 2024 Q3 Developer Update]({% post_url 2024-07-22-developer-update %})
* [Raster Attribute Table extension](https://github.com/geoserver/geoserver/wiki/GSIP-222)
* [Community module graduation, amending generality rule](https://github.com/geoserver/geoserver/wiki/GSIP-223)
* [Individual contributor clarification](https://github.com/geoserver/geoserver/wiki/GSIP-224)
* [Migrate geoserver-users from SourceForge to discourse](https://github.com/geoserver/geoserver/wiki/GSIP-225)

Release notes:
( [2.26.2](https://github.com/geoserver/geoserver/releases/tag/2.26.2)
| [2.26.1](https://github.com/geoserver/geoserver/releases/tag/2.26.1)
| [2.26.0](https://github.com/geoserver/geoserver/releases/tag/2.26.0)
| [2.26-M0](https://github.com/geoserver/geoserver/releases/tag/2.26-M0)
) 

