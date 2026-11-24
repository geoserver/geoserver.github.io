---
author: David Blasby
date: 2004-04-22
layout: post
link: http://docs.codehaus.org/display/GEOS/GeoServer+1.2.0rc1
wayback: https://web.archive.org/web/20050404034337/http://docs.codehaus.org:80/display/GEOS/GeoServer+1.2.0rc1
title: "GeoServer 1.2.0rc1 Released"
categories:
- Announcements
---

GeoServer 1.2.0rc1 has been released. Its release page collected installation reports from the community, shown below.

----

This page should be used to report successful GeoServer installations.

| GeoServer 1.2.0rc1 | version  | status  | Win98 | Win2K | WinXP | Linux |
|--------------------|----------|---------|-------|-------|-------|-------|
| Tomcat             | 5.5.7    | working |       |       | x     | x     |
| Tomcat             | 5.0.19   | working | x     | x     |       | x     |
| Tomcat             | 4.1.30   | working | x     | \-    | x     | x     |
| Tomcat             | 4.1.12   | broken  |       |       |       |       |
| Jetty              | internal | working |       | x     | x     | x     |
| Resin              | 3.x      | broken  |       | x     | x     |       |
| Resin              | 2.x      | working |       | x     |       |       |

If you can fill any holes in the above table please edit this page, and write you name and environment down. (Jody here I see that a Win98 column has been added - who tested with this/what java version)

##### Jianchun Xu

I tried GeoServer 1.2.0 rc2, rc1, 1.1.1… None of them is compatible with Sun Application Server Platform Edition 8 (bundled with J2EE 1.4 SDK). Am I missing anything? Why the J2EE server by Sun is not supported? Or, does GeoServer completely follow J2EE specifications?

##### Chris Holmes

OS: Win XP, Java version 1.4.1_07 Jetty 4.1.27, Tomcat 4.1.30. Also tested Resin 3.0.6, but I have problems with the Login page looping, never recognizing that you actually logged in, and I've heard reports of it freezing up on the FeatureTypeEditing, which I've never tested myself, since I use Resin rarely. I'm testing with the latest cvs builds.

##### Jody Garnett

OS: Win 2000, Java 1.4.2_04 with JAI 1.1.2 and image_io, Jetty from the cvs, Resin 3.0.6 is broken although Resin 2.x works. Tomcat 5.0.19 and Tomcat 4.1.30

##### Swapan Mazumdar

Tomcat 5.0.19 working,\
And yeah, tomcat4.1.12 had some major problems. I am not sure what specific module was inconsistent.

##### Rafax

does somebody has some experience with solaris and geoserver? i would like to know if geoserver works on solaris???

- I have heard no reports of it, but don't see any reason it would not work as GeoServer is all Java. Please report back if you test it out. - cholmes

##### Patrick Schlaepfer

OS: SuSE Linux 9, Java 1.4.2_04 with JAI 1.1.2, Tomcat 4.1.30 - Made some changements, that it runs in top level - not as /geoserver

##### Daniel O'Neill

OS: Win XP, Java 1.5.0 with JAI 1.1.2, JBoss 4.0.1 - working\
OS: Win XP, Java 1.4.1 with JAI 1.1.2, Websphere 5.0 - geoserver war deploys and starts but admin page returns ServletExceptions in actionator.jsp, locator.jsp, and menuator.jsp. Already tried changing the quotes as mentioned in the comment. Will investigate further and update as appropriate.

##### Ida de Groot

The same problem occurred in Editor.jsp while adding a feature type.

##### Craig E. Oaks

OS: Win XP, Java 1.5.0 with JAI 1.1.2, Tomcat 5.5.7, PostgreSQL 8.0.1 + PostGIS 1.0.0-RC3 - working\
OS: Fedora Core 3, Java 1.5.0 with JAI 1.1.2, Tomcat 5.5.7 - working\
Note on WinXP: these files must be included in Tomcat's "common/endorsed" folder: xercesImpl.jar, xml-apis.jar, xalan.jar (see [GEOS-292](https://osgeo-org.atlassian.net/browse/GEOS-292) for details.)

## Release notes

New Feature:

* [GEOS-86](https://osgeo-org.atlassian.net/browse/GEOS-86) Provide Feature Lock Control
* [GEOS-151](https://osgeo-org.atlassian.net/browse/GEOS-151) User Interface page for login.

Improvement:

* [GEOS-8](https://osgeo-org.atlassian.net/browse/GEOS-8) Redo gzipping of response's content if user agent supports it
* [GEOS-23](https://osgeo-org.atlassian.net/browse/GEOS-23) Test and get working with Resin and other servlet containers.
* [GEOS-84](https://osgeo-org.atlassian.net/browse/GEOS-84) Separate Page for New Actions
* [GEOS-119](https://osgeo-org.atlassian.net/browse/GEOS-119) Update date in Web Map Server Contents
* [GEOS-121](https://osgeo-org.atlassian.net/browse/GEOS-121) Build process
* [GEOS-122](https://osgeo-org.atlassian.net/browse/GEOS-122) Use default values provided by DataStore params when creating new datastores
* [GEOS-125](https://osgeo-org.atlassian.net/browse/GEOS-125) Cancel buttons in Editor windows
* [GEOS-141](https://osgeo-org.atlassian.net/browse/GEOS-141) GMLPrefix option in web admin tool?

Bug:

* [GEOS-16](https://osgeo-org.atlassian.net/browse/GEOS-16) Lost support for international character sets.
* [GEOS-40](https://osgeo-org.atlassian.net/browse/GEOS-40) Strings handled as numbers on inserts
* [GEOS-56](https://osgeo-org.atlassian.net/browse/GEOS-56) The embedded Tomcat no longer works.
* [GEOS-59](https://osgeo-org.atlassian.net/browse/GEOS-59) Most of the cite tests are working, here is a list of the broken tests.
* [GEOS-65](https://osgeo-org.atlassian.net/browse/GEOS-65) Oracle cannot add FeatureTypes
* [GEOS-94](https://osgeo-org.atlassian.net/browse/GEOS-94) Style Edit error
* [GEOS-104](https://osgeo-org.atlassian.net/browse/GEOS-104) GetFeature namespaces and schemas location
* [GEOS-113](https://osgeo-org.atlassian.net/browse/GEOS-113) getCapabilities returns an invalid xml
* [GEOS-118](https://osgeo-org.atlassian.net/browse/GEOS-118) maven test fails for gmldatasource preventing full build
* [GEOS-123](https://osgeo-org.atlassian.net/browse/GEOS-123) quickstart problems
* [GEOS-124](https://osgeo-org.atlassian.net/browse/GEOS-124) FeatureTypeEditor: SRS and Bounding box
* [GEOS-134](https://osgeo-org.atlassian.net/browse/GEOS-134) Validation test sutie delete - does not remove xml files
* [GEOS-135](https://osgeo-org.atlassian.net/browse/GEOS-135) /geoserver/data and wfs schemas no longer show up online
* [GEOS-136](https://osgeo-org.atlassian.net/browse/GEOS-136) Styles with filters fail
* [GEOS-137](https://osgeo-org.atlassian.net/browse/GEOS-137) Transactions do not work with Postgres 7.4
* [GEOS-138](https://osgeo-org.atlassian.net/browse/GEOS-138) Gep Map request fails for bc_roads
* [GEOS-139](https://osgeo-org.atlassian.net/browse/GEOS-139) Admin interface fails at startup
* [GEOS-148](https://osgeo-org.atlassian.net/browse/GEOS-148) Test linux with resin (2.x and 3.x)
* [GEOS-150](https://osgeo-org.atlassian.net/browse/GEOS-150) Bounding Box for tables that have no geometries does not let you pass go.
* [GEOS-152](https://osgeo-org.atlassian.net/browse/GEOS-152) Start error after altering the configuration applied by web interface (and more)
* [GEOS-154](https://osgeo-org.atlassian.net/browse/GEOS-154) Test web interface with Oracle and user defined schemas, and update the user docs.
* [GEOS-157](https://osgeo-org.atlassian.net/browse/GEOS-157) Tomcat 4x action servlet failure

Task:

* [GEOS-39](https://osgeo-org.atlassian.net/browse/GEOS-39) Test and document the restriction filter.

Wish:

* [GEOS-30](https://osgeo-org.atlassian.net/browse/GEOS-30) For Caps requests that come through the dispatcher report all with the dispatcher's base
