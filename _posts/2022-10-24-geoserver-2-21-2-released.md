---
author: Jody Garnett
date: 2022-10-24
layout: post
title: GeoServer 2.21.2 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_2211
version: 2.21.2
jira_version: 16860 
---

GeoServer [2.21.2](/release/2.21.2/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.2/geoserver-2.21.2-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.2/geoserver-2.21.2-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.2/GeoServer-2.21.2-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.2/geoserver-2.21.2-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.2/extensions/).

This is a stable release of the GeoServer 2.21.x series, made in conjunction with GeoTools 27.2 
and GeoWebCache 1.21.2.

Thanks to Jody Garnett (GeoCat) for making this release.

### Security Considerations

This release includes a security enhancement and is a recommended upgrade for production systems.

* [GEOS-10458](https://osgeo-org.atlassian.net/browse/GEOS-10598) XSS vulnerability in the email address field
  
### REST API Cache Reset

For everyone who enjoys automating GeoServer a really useful feature. For the longest time GeoServer has had a REST API endpoint for reseting and reloading the Catalogue. 

This change allows a reset of the information cached for:

* ``[POST] /workspaces/<ws>/datastores/<cs>/reset``
* ``[POST] /workspaces/<ws>/datastores/<ds>/featuretypes/<ft>/reset``

  Resetting a featuretype will not overwrite any attribute selection / renaming / type conversion as this has been supplied by hand and not generated (That kind of information can be updated via REST API explicit PUT on the feature type resource.)

* ``[POST] /workspaces/<ws>/coveragestores/<cs>/reset``
* ``[POST] /workspaces/<ws>/coveragestores/<cs>/coverages/<c>/reset``

To use consult REST API reference for [coveragestores](http://docs.geoserver.org/latest/en/api/#1.0.0/coveragestores.yaml) / [coverages](http://docs.geoserver.org/latest/en/api/#1.0.0/coverages.yaml]), and  [datastores](http://docs.geoserver.org/latest/en/api/#1.0.0/datastores.yaml) / [featuretypes](http://docs.geoserver.org/latest/en/api/#1.0.0/featuretypes.yaml).

Thanks to Andrea (GeoSolutions) for proposing and implementing this improvement. See proposal [GSIP-214 - Selective reset of ResourcePool caches](https://github.com/geoserver/geoserver/wiki/GSIP-214) for background information.

* [GEOS-10610](https://osgeo-org.atlassian.net/browse/GEOS-10610) Selective cache reset on stores and resources, via REST API

### Logging profile date formatting updates

The built-in logging profiles have been updated as the date was being incorrectly logged:

* If you have hand edited any of the built-in logging profiles you can fix the data format manually. Locate appender ``PatternLayout`` entries and correct the date formatting to ``%date{dd MMM HH:mm:ss}``.

* If you have not modified any of the built-in logging profiles a quick way to update is to remove them from your GEOSERVER_DATA_DIRECTORY ``logs`` folder.
  
  The built-in logging profiles will be restored next time you change profiles or when the application starts up. 

* If you never plan to customize the built-in loggig profiles use the system property ``UPDATE_BUILT_IN_LOGGING_PROFILES=true``. This setting will cause GeoServer to update the files when changing profiles or on application startup.
  
  This setting only affects the built-in logging profiles; any new logging profiles that you have
  made manually are unaffected.

For more information see the user guide on [built-in logging profiles](https://docs.geoserver.org/stable/en/user/configuration/logging.html#built-in-logging-profiles).

* [GEOS-10701](https://osgeo-org.atlassian.net/browse/GEOS-10701) Logging profiles timestamp reports minutes where it should report months

* [GEOS-10700](https://osgeo-org.atlassian.net/browse/GEOS-10700) Impossible to customize built-in logging profiles: GeoServer will rewrite them on startup


### Improvements and Fixes

Improvements:

* [GEOS-10677](https://osgeo-org.atlassian.net/browse/GEOS-10677)  Improve cleanup of multi part form upload to the dispatcher

* [GEOS-10676](https://osgeo-org.atlassian.net/browse/GEOS-10676) Support uploading .bmp and .gif images as SLD Package icons through restconfig

* [GEOS-10644](https://osgeo-org.atlassian.net/browse/GEOS-10644) Keycloak - Improvements to Role Service

* [GEOS-10639](https://osgeo-org.atlassian.net/browse/GEOS-10639) Keycloak Filter - Allow to use a button to reach keycloak login page

* [GEOS-10637](https://osgeo-org.atlassian.net/browse/GEOS-10637) Keycloak filter  configurability improvements

* [GEOS-10625](https://osgeo-org.atlassian.net/browse/GEOS-10625) GeoFence: improve filtering by role

* [GEOS-10620](https://osgeo-org.atlassian.net/browse/GEOS-10620) Update oshi to 6.2.2 to support Apple M2 CPU

* [GEOS-10606](https://osgeo-org.atlassian.net/browse/GEOS-10606) Generate html notice and license information for release assemblies

Fixes:

* [GEOS-10711](https://osgeo-org.atlassian.net/browse/GEOS-10711) ConcurrentModificationException can happen while modifying data access rules with concurrent WMS traffic

* [GEOS-10699](https://osgeo-org.atlassian.net/browse/GEOS-10699) WCS 2.0 latitude subsetting may fail if the source data has longitudes spanning both datelines

* [GEOS-10671](https://osgeo-org.atlassian.net/browse/GEOS-10671) Parallel REST API calls failures \(users\)

* [GEOS-10649](https://osgeo-org.atlassian.net/browse/GEOS-10649) Concurrent modification to GWC style parameter filter can lead to OOM

* [GEOS-10636](https://osgeo-org.atlassian.net/browse/GEOS-10636) Proxied Login is broken after upgrade to 2.22-M0 and 2.21.1

* [GEOS-10635](https://osgeo-org.atlassian.net/browse/GEOS-10635) GeoFence: area reprojection tests are failing

* [GEOS-10631](https://osgeo-org.atlassian.net/browse/GEOS-10631) AccessManager will not be looked up if multiple beans are of type DefaultResourceAccessManager

* [GEOS-10628](https://osgeo-org.atlassian.net/browse/GEOS-10628) GWC Environment parameterization does not work on geoserver startup

* [GEOS-10607](https://osgeo-org.atlassian.net/browse/GEOS-10607) Links disappearing for the Admin user

* [GEOS-10547](https://osgeo-org.atlassian.net/browse/GEOS-10547) Integrated WMS caching without the tiled parameter might result in deep recursion

* [GEOS-10507](https://osgeo-org.atlassian.net/browse/GEOS-10507) GeoFence Internal - Support Batch operations for Rules and AdminRules

For complete information see [2.21.2 release notes](https://github.com/geoserver/geoserver/releases/tag/2.21.2).

## About GeoServer 2.21

Additional information on GeoServer 2.21 series:

* [Feature Type Customization](https://github.com/geoserver/geoserver/wiki/GSIP-207)
* [Add Styles support to LayerGroup](https://github.com/geoserver/geoserver/wiki/GSIP-205)
* [Log4j1 update or replace activity]({% post_url 2022-01-20-log4j-upgrade %})

Release notes:
( [2.21.2](https://github.com/geoserver/geoserver/releases/tag/2.21.2)
| [2.21.1](https://github.com/geoserver/geoserver/releases/tag/2.21.1)
| [2.21.0](https://github.com/geoserver/geoserver/releases/tag/2.21.0)
| [2.21-RC](https://github.com/geoserver/geoserver/releases/tag/2.21-RC)
)
