---
author: Gabriel Roldan
date: 2023-03-14
layout: post
title: GeoServer 2.23-RC1 Release
categories:
- Announcements
tags:
- Release
release: release_223
version: 2.23-RC1
jira_version: 16862
---

GeoServer [2.23-RC1](/release/2.23-RC1/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23-RC1/geoserver-2.23-RC1-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23-RC1/geoserver-2.23-RC1-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23-RC1/GeoServer-2.23-RC1-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23-RC1/geoserver-2.23-RC1-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23-RC1/extensions/).

This is a release candidate intended for public review and feedback, made in conjunction with GeoTools 29-RC1 and GeoWebCache 1.23-RC1.

Thanks to Gabriel Roldan (Camptocamp), Jody Garnett (GeoCat), and Andrea Aime (Geosolutions) for making this release candidate.

### Release candidate public testing and feedback

Testing and providing feedback on releases is part of the open-source social contract. The development team (and their employers and customers) are responsible for sharing this great technology with you.

*The collaborative part of open-source happens now - we ask you to test this release candidate in your environment and with your data. Try out the new features, double check if the documentation makes sense, and most importantly let us know!*

*If you spot something that is incorrect or not working do not assume it is obvious and we will notice. We request and depend on your [email](https://geoserver.org/comm/) and [bug reports](https://geoserver.org/issues/) at this time. If you are working with [commercial support](https://geoserver.org/support/) your provider is expected to participate on your behalf.*

Keeping GeoServer sustainable requires a long term community commitment. If you are unable to contribute time, [sponsorship options](https://github.com/geoserver/geoserver/wiki/Sponsor) are available via OSGeo.

### Java 11 Minimum

With this release GeoServer no longer supports Java 8, and it is time to upgrade to Java 11 at a minimum. Our build system tests GeoServer in with Java 11 and Java 17 which are both long-term-support OpenJDK releases.

![JVM 11 Minimum](/img/posts/2.23/java_11.png) <br/>

For more information please see our User Manual [Installation](https://docs.geoserver.org/latest/en/user/installation/index.html#installation) (User Manual) and [Java Considerations](https://docs.geoserver.org/latest/en/user/production/java.html) (User Manual) pages.

* [GSIP-215 - Drop Java 8 Support](https://github.com/geoserver/geoserver/wiki/GSIP-215) (Proposal)
* [GEOS-10638](https://osgeo-org.atlassian.net/browse/GEOS-10638) Drop Java 8 support

### CSS Cleanup

The first big internal change for this release of GeoServer is a cleanup of the theme used for the GeoServer web administration application. Previously the pages had lots of little styling adjustments to try and get components to line up correctly and appear okay.

With this update all of the handmade styling changes have been removed, and everything is managed by the "geoserver.css" theme.

Thansk to Micheal Gabriel (GeoCat) who started this work at the Bolsena code-sprint as a labour of love (well frustration).

* [GUI CSS Cleanup](https://github.com/geoserver/geoserver/wiki/GSIP-213) (Proposal)
* []GEOS-10556](https://osgeo-org.atlassian.net/browse/GEOS-10556) Cleanup Inconsistent DOM structure and use of hardcoded styles

### Spring Upgrade

The second internal change for this release of GeoServer in an upgrade to Spring Framework used to wire the internals of GeoServer together.

While this should not result in any change to functionality, it has resulted in quite a lot of carefult quality assurance and testing to ensure everything is still connected and works as intended.

Your "it works" feedback during the release-candidate testing cycle is valuable and will make Joseph Miler (GeoSolution) who worked on this activity feel good.

* [GEOS-10779](https://osgeo-org.atlassian.net/browse/GEOS-10779) Upgrade GeoServer Core Spring to 5.3.23 and Spring Security to 5.7.3

### Windows installer Java 11 Update

We are especially interested in feedback on the Java 11 minium transition for those using the Windows Installer (none of our core development team is in position to test so we are depending on you).

Early feedback indicates that the NSIS installer search for an Oracle JVM by default; but it is fine to select any OpenJDK JRE you have installed (we recommend [Adoptium](https://adoptium.net) which provides a nice windows installer).

* [GEOS-10890](https://osgeo-org.atlassian.net/browse/GEOS-10890) Wrong path for the license file in the Windows installer script

## Feature Type Description

A welcome new feature, building on top of the ability to customize FeatureTypes is the ability to provide a description for each attribute. This information is used in WFS DescribeFeatureType to provide a human readable name or description for the attributes being published.

![Attribute Descriptions](/img/posts/2.23/attribute_description.png) <br/>

* [GEOS-10868](https://osgeo-org.atlassian.net/browse/GEOS-10868) Add support for editable description in GeoServer customize feature type table

## Community Updates

The following community module has been retired:

* [GEOS-10778](https://osgeo-org.atlassian.net/browse/GEOS-10778) Retire GeoStyler community module

  The plugin is now maintained outside of the GeoServer repository at https://github.com/geostyler . 

### Security community modules

With the upgrade to Spring Security to 5.7.3 mentioned above, now is a good time for any teams working with community security modules to perform integration testing.

A reminder that these modules are in need of your support to be recognized as an extension (and be included in our automated testing). Contact the apprioriate module maintainer to see how uou can assist.

### OGCAPI community module Updates

The OGCAPI community module remains under active development:

* [GEOS-10758](https://osgeo-org.atlassian.net/browse/GEOS-10758) OGCAPI - Features - Add storageCrs property for Collections
* [GEOS-10888](https://osgeo-org.atlassian.net/browse/GEOS-10888) OGC API styles OpenAPI document points to dangling remote resources 
* [GEOS-10854](https://osgeo-org.atlassian.net/browse/GEOS-10854) Move the OGC API OpenAPI definitions to the "openapi" resource
* [GEOS-10855](https://osgeo-org.atlassian.net/browse/GEOS-10855) Update the new OGC APIs so that the major version number is part of the path
* [GEOS-10881](https://osgeo-org.atlassian.net/browse/GEOS-10881) Add Content-Crs header to OGC API
* [GEOS-10885](https://osgeo-org.atlassian.net/browse/GEOS-10885) Remove Axis Order from OGC API Header

If you are in a position to support this activity with time, money or resources please contact Andrea (GeoSolutions) to assist.


### Improvements and Fixes

# Release notes - GeoServer - 2.23-RC1

### New Feature

* [GEOS-10696](https://osgeo-org.atlassian.net/browse/GEOS-10696) Allow configuration of Output Format types allowed in GetFeature

### Improvement

* [GEOS-10735](https://osgeo-org.atlassian.net/browse/GEOS-10735) Obfuscate secret key in S3 Blob Store, avoiding requiring reentry when editing and HTML source visibility

* [GEOS-10739](https://osgeo-org.atlassian.net/browse/GEOS-10739) Contact information user interface feedback for welcome message

* [GEOS-10740](https://osgeo-org.atlassian.net/browse/GEOS-10740) Service enabled does not respect minimal/custom service names

* [GEOS-10750](https://osgeo-org.atlassian.net/browse/GEOS-10750) German Translation Overhaul Part 1

* [GEOS-10755](https://osgeo-org.atlassian.net/browse/GEOS-10755) WCS 2.0 module should not use string concatenation to build XML

* [GEOS-10762](https://osgeo-org.atlassian.net/browse/GEOS-10762) Allow enabling auto-escaping for WMS GetFeatureInfo HTML templates

* [GEOS-10814](https://osgeo-org.atlassian.net/browse/GEOS-10814) Update jdbc config to use consistent SQL formatting

* [GEOS-10879](https://osgeo-org.atlassian.net/browse/GEOS-10879) Dispatcher should not respond to non standard HTTP methods

### Tasks


* [GEOS-10798](https://osgeo-org.atlassian.net/browse/GEOS-10798) \[Sphinx site url\]\(http://sphinx.pocoo.org/\) is outdate

For the complete list see [2.23-RC1](https://github.com/geoserver/geoserver/releases/tag/2.23-RC1) release notes.

## About GeoServer 2.23 Series

Release notes:
( [2.23-RC1](https://github.com/geoserver/geoserver/releases/tag/2.23-RC1)
)

* [Drop Java 8](https://github.com/geoserver/geoserver/wiki/GSIP-215)
* [GUI CSS Cleanup](https://github.com/geoserver/geoserver/wiki/GSIP-213) (Proposal)
* [Add the possibility to use fixed values in Capabilities for Dimension metadata](https://github.com/geoserver/geoserver/wiki/GSIP-208)
