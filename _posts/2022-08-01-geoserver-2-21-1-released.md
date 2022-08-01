---
author: Jody Garnett
date: 2022-08-01
layout: post
title: GeoServer 2.21.1 Release
categories:
- Announcements
tags:
- Release
release: release_221
version: 2.21.1
jira_version: 16856 
---

GeoServer [2.21.1](/release/2.21.1/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.1/geoserver-2.21.1-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.1/geoserver-2.21.1-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.1/GeoServer-2.21.1-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.1/geoserver-2.21.1-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.1/extensions/).

This is a stable release of the GeoServer 1.21.x series, made in conjunction with GeoTools 27.1 
and GeoWebCache 1.21.1.

Thanks to Jody Garnett (GeoCat) for making this release.

### Server Status

The server status page has been cleaned up with a few quality of life improvements: 

* Units supplied for numbers, such as "7 threads" or "30,000 ms"
* Number of items held in the resource cache is shown, so there is visual feed back when using **Clear** button.
* Documentation has been updated to cover all the status field descriptions and document the available actions

For more information see [Server Status page](https://docs.geoserver.org/stable/en/user/configuration/status.html#server-status).

![Server status](/img/posts/2.21/server_status.png) <br/>

### JVM Console

A new **JVM Console** tab has been added to the server status page allowing a summary of memory use to be reviewed and downloaded, and a summary of active threads to be reviewed and downloaded.

For more information see [JVM Console](https://docs.geoserver.org/stable/en/user/configuration/status.html#jvm-console).

![JVM Console](/img/posts/2.21/jvm_console.png) <br/>

### Workspace headers for proxy url

A checkbox **Use headers for Proxy URL** has been added to the workspace page.

This setting an individual workspace use headers for proxy URL (even when the default in global settings has been disabled).

### Improvements and Fixes

Improvement:

[GEOS-10580](https://osgeo-org.atlassian.net/browse/GEOS-10580) Server status page improvements for status, modules and docs

[GEOS-10521](https://osgeo-org.atlassian.net/browse/GEOS-10521) Allow GetFeatureInfo over raster layers to identify both original raster and transformed vectors

[GEOS-10514](https://osgeo-org.atlassian.net/browse/GEOS-10514) Better capture catalog configuration issues: layergroup with a misconfigured layer

[GEOS-10501](https://osgeo-org.atlassian.net/browse/GEOS-10501) GetMap: support auth headers forwarding to remote SLD urls

[GEOS-10495](https://osgeo-org.atlassian.net/browse/GEOS-10495) Request Logger Memory Buffer Limits

[GEOS-10489](https://osgeo-org.atlassian.net/browse/GEOS-10489) Add options to LDAP Role Service to configure prefixes and enforce capitalization

[GEOS-10464](https://osgeo-org.atlassian.net/browse/GEOS-10464) Improve logging and check for NPEs and other issues in Importer Module

Bug:

[GEOS-10584](https://osgeo-org.atlassian.net/browse/GEOS-10584) Enabling logging of request body results in stream closed errors in tomcat environment

[GEOS-10570](https://osgeo-org.atlassian.net/browse/GEOS-10570) Deleting a style in a Hazelcast cluster renames the styles directory

[GEOS-10553](https://osgeo-org.atlassian.net/browse/GEOS-10553) Importer replace fails with schema mismatch

[GEOS-10548](https://osgeo-org.atlassian.net/browse/GEOS-10548) GeoFence layer group handling is inconsistent

[GEOS-10546](https://osgeo-org.atlassian.net/browse/GEOS-10546) Invalid time expressions used in WCS 2.0 subset return a code 200 with generic exception

[GEOS-10545](https://osgeo-org.atlassian.net/browse/GEOS-10545) Layer Group cache not initialized

[GEOS-10539](https://osgeo-org.atlassian.net/browse/GEOS-10539) DescribeLayer typeName is no longer workspace qualified

[GEOS-10535](https://osgeo-org.atlassian.net/browse/GEOS-10535) WFS Update request throw NPE on bad namespace

[GEOS-10534](https://osgeo-org.atlassian.net/browse/GEOS-10534) a badly formed delete transaction will get a NPE instead of an informative error message

[GEOS-10533](https://osgeo-org.atlassian.net/browse/GEOS-10533) Review startup logging INFO and WARN updates

[GEOS-10526](https://osgeo-org.atlassian.net/browse/GEOS-10526) Parallel REST API calls failures

[GEOS-10522](https://osgeo-org.atlassian.net/browse/GEOS-10522) REST API Failure in @ExceptionHandler No input String specified

[GEOS-10518](https://osgeo-org.atlassian.net/browse/GEOS-10518) Partial RELINQUISH\_LOG4J\_CONTROL regression with WildFly

[GEOS-10516](https://osgeo-org.atlassian.net/browse/GEOS-10516) WMS GetCapabilities dimension representations ignores the end attribute

[GEOS-10496](https://osgeo-org.atlassian.net/browse/GEOS-10496) Using the REST API to purge NetCDF granules causes a seemingly infinite loop

[GEOS-10487](https://osgeo-org.atlassian.net/browse/GEOS-10487) Custom logging configuration not respecting log location setting

[GEOS-10468](https://osgeo-org.atlassian.net/browse/GEOS-10468) \(virtually\) Impossible to turn off "Enable All Statistics" in  > Server status > System Status

Tasks:

[GEOS-10588](https://osgeo-org.atlassian.net/browse/GEOS-10588) Build structure gs-sec-oauth2-core is duplicated in the reactor

[GEOS-10585](https://osgeo-org.atlassian.net/browse/GEOS-10585) Upgrade to Jetty from 9.4.44 to 9.4.48

[GEOS-10579](https://osgeo-org.atlassian.net/browse/GEOS-10579) Bump oshi-core from 6.2.0 to 6.2.1

[GEOS-10562](https://osgeo-org.atlassian.net/browse/GEOS-10562) Bump oshi-core from 5.8.6 to 6.2.0

[GEOS-10551](https://osgeo-org.atlassian.net/browse/GEOS-10551) Refactor commons-httpclient usage in the WPS module

[GEOS-10532](https://osgeo-org.atlassian.net/browse/GEOS-10532) FreemarkerTemplateManager API changes for easier subclassing

[GEOS-10529](https://osgeo-org.atlassian.net/browse/GEOS-10529) Use Awaitility to replace waits for condition in tests

[GEOS-10525](https://osgeo-org.atlassian.net/browse/GEOS-10525) Centralize and simplify management of common test dependencies

## About GeoServer 2.21

Additional information on GeoServer 2.21 series:

* [Feature Type Customization](https://github.com/geoserver/geoserver/wiki/GSIP-207)
* [Add Styles support to LayerGroup](https://github.com/geoserver/geoserver/wiki/GSIP-205)
* [Log4j1 update or replace activity]({% post_url 2022-01-20-log4j-upgrade %})

Release notes:
( [2.21.1](https://github.com/geoserver/geoserver/releases/tag/2.21.1)
| [2.21.0](https://github.com/geoserver/geoserver/releases/tag/2.21.0)
| [2.21-RC](https://github.com/geoserver/geoserver/releases/tag/2.21-RC)
)
