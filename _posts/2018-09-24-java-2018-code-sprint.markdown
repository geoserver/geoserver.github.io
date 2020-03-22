---
author: jgarnett
comments: false
date: 2018-09-24 19:57:03+00:00
layout: post
link: http://blog.geoserver.org/2018/09/24/java-2018-code-sprint/
slug: java-2018-code-sprint
title: Java 2018 Code Sprint
wordpress_id: 2973
---

**Java 11 is released tomorrow! **GeoServer has a window until January 2019 before Java 8 is no longer officially supported!

To make the transition the GeoServer team is setting up a [Java 2018 Code Sprint](https://wiki.osgeo.org/wiki/Java_2018_Code_Sprint) - and we need your support to help enough participants attend!



 	
  * October 22-26th

 	
  * Groups gathering in North America, Europe and Oceania


With recent policy changes setting the Java platform on a six-month release cycle. We also have significant work ensuring the libraries we use either work with the "jigsaw" module system or are replaced.

Already we have identified changes needed for GeoServer to run at all:

 	
  * Upgrade Spring: The application framework uses the reflection feature of Java to wire GeoServer together - and needs to be updated to work with the additional Java 11 restrictions.

 	
  * Upgrade Log4J: A Java 11 compatible version of Log4J is available and provides tools for visualization and exploring log messages.

 	
  * Repackage the application adding automatic module names


Our goal is to ensure that the next release of GeoServer can run with Java 8 or Java 11.


## How to participate


Please visit the [osgeo wiki page](https://wiki.osgeo.org/wiki/Java_2018_Code_Sprint) and add yourself to the list of participants. We are trying to bring as contributors together as possible and would love it if you could join us!

In addition to GeoServer representatives from GeoTools and GeoNetwork will be taking part.


## How to sponsor


We have three sponsorship levels available, with contributions devoted to helping participants attend:



 	
  * Gold: $7500 USD

 	
  * Silver: $1500 USD

 	
  * Bronze: $750 USD


Sponsor logos are included on the event page and blog posts in addition to being featured in the associated project release announcements. More importantly your financial support goes towards making sure GeoServer remains available on a supported Java platform.

Please see the wiki page for details on [how to sponsor](https://wiki.osgeo.org/wiki/Java_2018_Code_Sprint#How_to_sponsorship).
