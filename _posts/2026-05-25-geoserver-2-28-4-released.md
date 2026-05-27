---
author: Peter Smythe
date: 2026-05-25
layout: post
title: GeoServer 2.28.4 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_228
version: 2.28.4
jira_version: 17868
--- 

GeoServer [2.28.4](/release/2.28.4/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.4/geoserver-2.28.4-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.4/geoserver-2.28.4-war.zip/download),
~~[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.4/GeoServer-2.28.4-winsetup.exe/download)~~), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.4/geoserver-2.28.4-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.4/extensions/).

Please note, this is an **extended stable** release of GeoServer providing existing installations with minor updates and bug fixes, provided shortly before the GeoServer 3.0 release.  
GeoServer 2.28.4 is made in conjunction with GeoTools 34.4, and GeoWebCache 1.28.4. 

Also note that for the last few months we have been unable to provide a [Windows Installer](https://sourceforge.net/projects/geoserver/files/GeoServer/2.28.4/GeoServer-2.28.4-winsetup.exe/download) due to an expired certificate to sign Windows builds, but we are working on a resolution.  Please bear with us, or offer to help, if it is important to you.

Thanks to Peter Smythe (AfriGIS) for making this release. 

## Security Considerations

This release addresses security vulnerabilities and is an important upgrade for production systems.

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.


## Release notes

Improvement:

* [GEOS-12045](https://osgeo-org.atlassian.net/browse/GEOS-12045) Allow disabling specific OGC service versions
* [GEOS-12105](https://osgeo-org.atlassian.net/browse/GEOS-12105) DiskQuotaConfigPanel: expose JDBCConfiguration.schema in the UI
* [GEOS-12111](https://osgeo-org.atlassian.net/browse/GEOS-12111) LDAP TLS pooled hostname

Bug:

* [GEOS-12092](https://osgeo-org.atlassian.net/browse/GEOS-12092) DescribeFeatureType fails to render a single option restriction in JSON format
* [GEOS-12116](https://osgeo-org.atlassian.net/browse/GEOS-12116) Workspace admin pager shows incorrect total count for security-filtered workspaces


For the complete list see [2.28.4](https://github.com/geoserver/geoserver/releases/tag/2.28.4) release notes. 

## Community Updates

Community module development:

* [GEOS-12098](https://osgeo-org.atlassian.net/browse/GEOS-12098) Rename JWT Header assembly so it is collected for nightly downloads
* [GEOS-12101](https://osgeo-org.atlassian.net/browse/GEOS-12101) Workspace styles not persisted to disk after restore

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.28 Series

Additional information on GeoServer 2.28 series:

* [GeoServer 2.28 User Manual](https://docs.geoserver.org/2.28.x/en/user/)
* [GeoServer 2025 Q4 Developer Update]({% post_url 2025-10-14-developer-update %})* [Advertise and Enforce Attribute Restrictions](https://github.com/geoserver/geoserver/wiki/GSIP-234)

Release notes:
( [2.28.4](https://github.com/geoserver/geoserver/releases/tag/2.28.4)
| [2.28.3](https://github.com/geoserver/geoserver/releases/tag/2.28.3)
| [2.28.2](https://github.com/geoserver/geoserver/releases/tag/2.28.2)
| [2.28.1](https://github.com/geoserver/geoserver/releases/tag/2.28.1)
| [2.28.0](https://github.com/geoserver/geoserver/releases/tag/2.28.0)
| [2.28-M0](https://github.com/geoserver/geoserver/releases/tag/2.28-M0)
) 

