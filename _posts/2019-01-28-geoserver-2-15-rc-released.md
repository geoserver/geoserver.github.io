---
author: iant
comments: false
date: 2019-01-28 09:54:05+00:00
layout: post
link: http://blog.geoserver.org/2019/01/28/geoserver-2-15-rc-released/
slug: geoserver-2-15-rc-released
title: GeoServer 2.15-RC Released
wordpress_id: 3000
categories:
- Announcements
tags:
- Release Candidate
release: release_215
version: 2.15-RC
jira_version: 16740
---

We are happy to share a [GeoServer 2.15-RC](http://geoserver.org/release/2.15-RC/) milestone release with downloads ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15-RC/geoserver-2.15-RC-bin.zip/download)|[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15-RC/geoserver-2.15-RC-war.zip/download)|[exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15-RC/geoserver-2.15-RC.exe/download)), documentation ([html](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15-RC/geoserver-2.15-RC-htmldoc.zip/download)|[pdf](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15-EC/geoserver-2.15-RC-user-manual.pdf/download)) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15-RC/extensions/).

This release candidate is provided for everyone considering a Java 11 operational environment in 2019.  A release candidate provides a final to support the development team with early feedback:  _your assistance and participation is requested!_

This release is a result of [participation](http://blog.geoserver.org/2018/09/24/java-2018-code-sprint/) in the OSGeo [Java 2018 Code Sprint](https://wiki.osgeo.org/wiki/Java_2018_Code_Sprint) and is made in conjunction with GeoTools 21-RC and GeoWebCache 1.15-RC. We would like to thank organizations participating in the code sprint ([Boundless](http://boundlessgeo.com/), [GeoSolutions](https://www.geo-solutions.it/), [GeoCat](https://www.geocat.net/), [Astun Technology](https://astuntechnology.com/), [CCRi](https://www.ccri.com/)) along with sprint sponsors ([Gaia3D](http://www.gaia3d.com/), [atol](https://www.atolcd.com/), [osgeo:uk](https://uk.osgeo.org/), [Astun Technology](https://astuntechnology.com/)). Our gratitude goes out to the individuals who worked so hard to bring everything together.


### Highlights


In addition to Java 11 support this release includes:



 	
  * JAI-EXT enabled by default, in other words, support for NODATA pixels on by default

 	
  * Add JSON as a Legend Output format (GISP 173)

 	
  * Printing plugin upgrade version of JTS

 	
  * SLDService become an official extension, with a number of improvements in it SLDService (classification of raster data too, equal area classification, standard deviation filtering)

 	
  * Allow configuring services on a per layer basis

 	
  * GeoFence upgraded from community module to official extension

 	
  * WPS "GetExecutions" vendor operation allows each user to get the list of running processes (limited to his account for normal users, showing all processes if the request is made by an admin)

 	
  * Autocomplete support for SLD 1.0 in style editor

 	
  * Improvements for vector tile production, both in terms of output correctness and production performance

 	
  * Upgrade NetCDF dependencies

 	
  * QA work adding PMD and ErrorProne checks in the build

 	
  * and a large number of bug fixes.




### Java 11 Support


The provided binary download works with either Java 8 or Java 11. Tomcat 9 or newer is required for the WAR install.

We will the update the user guide [compatibility list](https://docs.geoserver.org/latest/en/user/production/java.html#running-on-java-11) based on your feedback and testing of this 2.15-RC milestone release. Please note that Java 11 no longer supports the Java 2 extension mechanism used for native JAI and native ImageIO.

This is a good opportunity to review your operational environment and help test GeoServer with the environment you intend to use in 2019.


### Java Roadmap Considerations


Our initial concerns with respect to continued availability of the Java 8 platform have been alleviated by industry action and commitment. Extensive [Java 8 support options are now](https://medium.com/@javachampions/java-is-still-free-c02aef8c9e04) available, with RedHat making a public commitment to contribute fixes to the OpenJDK 8 codebase, and a range of organizations committed to making OpenJDK 8 builds available on a range of platforms.

Oracle has changed to a six month release schedule, donating additional components to OpenJDK to make it lead platform. Long term support (beyond six months) is being offered from a range of organizations notably [RedHat OpenJDK](https://developers.redhat.com/products/openjdk/overview/)  and [Adopt OpenJDK](http://adoptopenjdk.net).

The net effect of these changes:



 	
  * If you have been using Oracle JDK up until now it is time to review your options

 	
  * Java 8 will continue to be available

 	
  * The Java ecosystem is now led by the open-source Open JDK project


See the GeoTools [user guide](http://docs.geotools.org/latest/userguide/build/install/jdk.html) for a table outlining the Java 8 and Java 11 alternatives to consider in the year ahead.


## About GeoServer 2.15 Series


Additional information on the GeoServer 2.15 series:



 	
  * Release Notes ([2.15-RC](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16740))

 	
  * Release Notes ([2.15-M0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16746))

 	
  * [Running on Java 11](https://docs.geoserver.org/latest/en/user/production/java.html#running-on-java-11) (User Manual)


