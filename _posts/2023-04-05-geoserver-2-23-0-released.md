---
author: Jody Garnett
date: 2023-04-05
layout: post
title: GeoServer 2.23.0 Release
categories:
- Announcements
tags:
- Release
release: release_223
version: 2.23.0
jira_version: 16885
---

GeoServer [2.23.0](/release/2.23.0/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.0/geoserver-2.23.0-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.0/geoserver-2.23.0-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.0/GeoServer-2.23.0-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.0/geoserver-2.23.0-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.23.0/extensions/).

This is a stable release of GeoServer suitable for production systems, made in conjunction with GeoTools 29.0 and GeoWebCache 1.23.0.

Thanks to Jody Garnett (GeoCat) for making this release. Additional thanks to those volunteering to test the release candidate, your assistance is seen and appreciated: Peter Rushforth, Mark Prins, Gabriel Roldan, and Juan Luis.

Keeping GeoServer sustainable requires community commitment. If you are unable to contribute time, [sponsorship options](https://github.com/geoserver/geoserver/wiki/Sponsor) are available via the Open Source Geospatial Foundation.

### Security Considerations

This release addresses a security vulnerability and is considered an essential upgrade for production systems.

* [CVE-2023-25158 OGC Filter SQL Injection Vulnerabilities](https://github.com/geotools/geotools/security/advisories/GHSA-99c3-qc2q-p94m) (GeoTools)
* [CVE-2023-25157 OGC Filter SQL Injection Vulnerabilities](https://github.com/geoserver/geoserver/security/advisories/GHSA-7g5f-wrx8-5ccf) (GeoServer)

For more information see [OGC Filter Injection Vulnerability Statement]({% post_url 2023-02-20-ogc-filter-injection %}).

If you have already updated to a patched release that is excellent. We still advise updating to benefit from the considerable work done updating dependencies for GeoServer 2.23.0.

### Java 11 Minimum

With this release GeoServer no longer supports Java 8, and it is time to upgrade to Java 11 at a minimum. Our build system tests GeoServer in with Java 11 and Java 17 which are both long-term-support OpenJDK releases.

![JVM 11 Minimum](/img/posts/2.23/java_11.png) <br/>

If you try starting this version of GeoServer with Java 8 it will produce the following failure:

```
java.lang.UnsupportedClassVersionError: org/geoserver/GeoserverInitStartupListener
has been compiled by a more recent version of the Java Runtime (class file version 55.0),
this version of the Java Runtime only recognizes class file versions up to 52.0
```

For more information please see our User Manual [Installation](https://docs.geoserver.org/latest/en/user/installation/index.html#installation) (User Manual) and [Java Considerations](https://docs.geoserver.org/latest/en/user/production/java.html) (User Manual) pages.

* [GSIP-215 - Drop Java 8 Support](https://github.com/geoserver/geoserver/wiki/GSIP-215)
* [GEOS-10638](https://osgeo-org.atlassian.net/browse/GEOS-10638) Drop Java 8 support

### CSS Cleanup

The first big internal change for this release of GeoServer is a cleanup of the theme used for the GeoServer web administration application. Previously the pages had lots of little styling adjustments to try and get components to line up correctly and appear okay.

With this update all of the handmade styling changes have been removed, and everything is managed by the "geoserver.css" theme.

Thanks to Michel Gabriël (GeoCat) who started this work at the Bolsena code-sprint as a labour of love (well frustration).

* [GSIP 213 - GUI CSS Cleanup](https://github.com/geoserver/geoserver/wiki/GSIP-213)
* [GEOS-10556](https://osgeo-org.atlassian.net/browse/GEOS-10556) Cleanup Inconsistent DOM structure and use of hardcoded styles

### Spring Upgrade

The second internal change for this release of GeoServer is an upgrade to the Spring Framework used to wire the internals of GeoServer together.

While this should not result in any change to functionality, it has resulted in quite a lot of careful quality assurance and testing to ensure everything is still connected and works as intended.

Thanks to Joseph Miler (GeoSolution) who worked on this activity.

* [GEOS-10779](https://osgeo-org.atlassian.net/browse/GEOS-10779) Upgrade GeoServer Core Spring to 5.3.23 and Spring Security to 5.7.3

* [GEOS-10907](https://osgeo-org.atlassian.net/browse/GEOS-10907) Update spring.version from 5.3.25 to 5.3.26

### Windows installer Java 11 Update

Windows users are advised to keep the Java 11 minimum requirement in mind when upgrading existing systems.

The installer will correctly detect the [Adoptium](https://adoptium.net) Java 17 and Java 11:

![Adoptium JDK 17 Manual](/img/posts/2.23/windows_jdk17.png) <br/>

The windows installer does not detect Oracle JDK 17; but you can use Browse to manually select this JDK:

![Oracle JDK 17 Manual](/img/posts/2.23/windows_jdk17_oracle_manual.png) <br/>

* [GEOS-10890](https://osgeo-org.atlassian.net/browse/GEOS-10890) Wrong path for the license file in the Windows installer script

Thanks to Juan Luis (GeoCat) for troubleshooting the windows installer for this release.

### Feature Type Description

A welcome new feature, building on top of the ability to customize FeatureTypes is the ability to provide a description for each attribute. This information is used in WFS DescribeFeatureType to provide a human readable name or description for the attributes being published.

![Attribute Descriptions](/img/posts/2.23/attribute_description.png) <br/>

* [GEOS-10868](https://osgeo-org.atlassian.net/browse/GEOS-10868) Add support for editable description in GeoServer customize feature type table

### OGC CITE Fixes

The traditional OGC Open Web Services have not had automated CITE tests run for a while, but a few fixes have been made to restore CITE compliance:

* [GEOS-10787](https://osgeo-org.atlassian.net/browse/GEOS-10787) CITE WCS 1.1.1 - Throw exception on bad 'store' parameter

* [GEOS-10788](https://osgeo-org.atlassian.net/browse/GEOS-10788) CITE WCS 1.1.1 - Empty InterpolationMethod should throw exception

* [GEOS-10757](https://osgeo-org.atlassian.net/browse/GEOS-10757) CITE: WMS &lt;Style&gt; has elements in wrong order (DTD validation)

* [GEOS-10782](https://osgeo-org.atlassian.net/browse/GEOS-10782) CITE WFS 1.1 - HITS mimetype is incorrect

* [GEOS-10783](https://osgeo-org.atlassian.net/browse/GEOS-10783) CITE WFS 1.1 - Check customized feature type to determine if transform wrapper needed

* [GEOS-10784](https://osgeo-org.atlassian.net/browse/GEOS-10784) CITE WFS 1.1 - don't do illegal geometry conversions

* [GEOS-10785](https://osgeo-org.atlassian.net/browse/GEOS-10785) CITE WFS 1.1 - Data Dir - allow anonymous users to modify data

Thanks to David Blasby (GeoCat) for this work on behalf of the GeoCat Live Project. David addressed several errors in the CITE testing for these services while addressing the above issues for the GeoServer community.

A number of CITE conformance issues remain open, notably the handling of acceptsVersions with a mix of older protocols (such as WFS 2.0, WFS 1.1 and WFS 1.0). If you are interested in funding or sponsoring this activity please visit our [sponsorship](https://github.com/geoserver/geoserver/wiki/Sponsor) page.

### Configuration Saving and Loading

A special call out to Dieter Stuken for working on the kind of fixes that just cause frustration - trouble shooting the internal *Resource Store* component that allows GeoServer configuration to be saved in a disk or database.

These fixes help the GeoServer Admin Console provide better error messages when a file is unavailable. And prevent the accidental creation of "missing" files when attempting to read from them.

* [GEOS-10724](https://osgeo-org.atlassian.net/browse/GEOS-10724) SpringResourceAdaptor should throw a FileNotFoundException instead of creating any missing file

* [GEOS-10743](https://osgeo-org.atlassian.net/browse/GEOS-10743) ResourcePool.readStyle created empty files

* [GEOS-10723](https://osgeo-org.atlassian.net/browse/GEOS-10723) clean up params-extractor plugin to use Resource

## Community Updates

The following community module has been retired:

* [GEOS-10778](https://osgeo-org.atlassian.net/browse/GEOS-10778) Retire GeoStyler community module

  The plugin is now maintained outside of the GeoServer repository at https://github.com/geostyler . 

### Security community modules

With the upgrade to Spring Security to 5.7.3 mentioned above, the community security modules have affected.

A reminder that these modules are in need of your support to be recognized as an extension (and be included in our automated testing). Contact the appropriate module maintainer (Alessio or David) to see how you can assist.

### OGCAPI community module Updates

The OGCAPI community module remains under active development:

* [GEOS-10889](https://osgeo-org.atlassian.net/browse/GEOS-10889) OGC API info section should report the spec version, not the server version

* [GEOS-10758](https://osgeo-org.atlassian.net/browse/GEOS-10758) OGCAPI - Features - Add storageCrs property for Collections

* [GEOS-10888](https://osgeo-org.atlassian.net/browse/GEOS-10888) OGC API styles OpenAPI document points to dangling remote resources 

* [GEOS-10854](https://osgeo-org.atlassian.net/browse/GEOS-10854) Move the OGC API OpenAPI definitions to the "openapi" resource

* [GEOS-10855](https://osgeo-org.atlassian.net/browse/GEOS-10855) Update the new OGC APIs so that the major version number is part of the path

* [GEOS-10881](https://osgeo-org.atlassian.net/browse/GEOS-10881) Add Content-Crs header to OGC API

* [GEOS-10885](https://osgeo-org.atlassian.net/browse/GEOS-10885) Remove Axis Order from OGC API Header

Andrea (GeoSolutions) has been working towards CITE compliance on behalf of Geonovum.

![OGC API Features](/img/posts/2.23/cite-core.png) <br/>

![OGC API Features](/img/posts/2.23/cite-crs.png) <br/>

As a community module GeoServer OGC API is made available to developers for collaboration, and can also be accessed as a nightly build for feedback. If you are in a position to support this activity with time, money or resources please contact Andrea.

![OGC API Features](/img/posts/2.23/ogc-api-features.png) <br/>

### Improvements and Fixes

The following improvements and fixes are provided for the 2.23.0 and 2.23-RC. 

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

### Fixes

* [GEOS-10006](https://osgeo-org.atlassian.net/browse/GEOS-10006) Seeding GWC doesn't work for layers with a dot in the name

* [GEOS-10865](https://osgeo-org.atlassian.net/browse/GEOS-10865) Backwards incompatible change in the XML representation of user roles

* [GEOS-10905](https://osgeo-org.atlassian.net/browse/GEOS-10905) Default CSW properties do not allow sorting by identifiers

### Tasks

* [GEOS-10798](https://osgeo-org.atlassian.net/browse/GEOS-10798) Sphinx site http://sphinx.pocoo.org/ is outdate

* [GEOS-10904](https://osgeo-org.atlassian.net/browse/GEOS-10904) Bump jettison from 1.5.3 to 1.5.4

* [GEOS-10894](https://osgeo-org.atlassian.net/browse/GEOS-10894) Random control-flow errors on Mac builds

* [GEOS-10863](https://osgeo-org.atlassian.net/browse/GEOS-10863) Update Oracle JDBC driver to 19.18.0.0

* [GEOS-10775](https://osgeo-org.atlassian.net/browse/GEOS-10775) Update xmlunit to 1.6

For the complete list see [2.23.0](https://github.com/geoserver/geoserver/releases/tag/2.23.0) release notes.

## About GeoServer 2.23 Series

Release notes:
( [2.23.0](https://github.com/geoserver/geoserver/releases/tag/2.23.0)
| [2.23-RC1](https://github.com/geoserver/geoserver/releases/tag/2.23-RC1)
)

* [Drop Java 8](https://github.com/geoserver/geoserver/wiki/GSIP-215)
* [GUI CSS Cleanup](https://github.com/geoserver/geoserver/wiki/GSIP-213)
* [Add the possibility to use fixed values in Capabilities for Dimension metadata](https://github.com/geoserver/geoserver/wiki/GSIP-208)
