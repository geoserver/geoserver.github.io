---
author: jgarnett
comments: false
date: 2019-01-03 01:23:08+00:00
layout: post
link: http://blog.geoserver.org/2019/01/03/java-2018-code-sprint-results/
slug: java-2018-code-sprint-results
title: Java 2018 Code Sprint Results
wordpress_id: 2984
---

The [Java 2018 code sprint](https://wiki.osgeo.org/wiki/Java_2018_Code_Sprint) was an ambitious event gathering up OSGeo Java projects to look at Java 11 compatibility. With a great response from the GeoServer community we are pleased to announce the GeoServer can now run in Java 11!

[![](/img/uploads/Screen-Shot-2019-01-02-at-4.50.39-PM-1024x366.png)](/img/uploads/Screen-Shot-2019-01-02-at-4.50.39-PM.png)

This sprint was an important response by our community to changes in the Java roadmap. The immediate motivation is to give our users the option of using Java 11 in the coming year now that OpenJDK is taking over as lead project. We are also pleased to report that Java 8 will continue to be supported (thanks to the commitment of [RedHat](https://developers.redhat.com/products/openjdk/overview/) and [Adopt OpenJDK](http://adoptopenjdk.net)) giving everyone a chance to migrate when ready.

We had 11 participants for the sprint - thanks to everyone who attended!



 	
  * David Vick (Boundless), Devon Tucker (Boundless), Jim Hughes (CCRi), Jody Garnett (Boundless) Kevin Smith (Boundless), and Torben Barsballe (Boundless) gathered at the Boundless office in Victoria, Canada.

 	
  * Andrea Aime (GeoSolutions) and Antonello Andrea (Hydrologis) participated from Andrea's home office in Italy.

 	
  * María Arias de Reyna (GeoCat), Ian Turton (Astun), Landon Blake (BKF Engineers), and Brad Hards participated remotely.


With support from OSGeo and event sponsors many individuals were able to meet up in person, with those hosed at the Boundless Victoria office enjoying the occasional break outside.

[![](/img/uploads/DSC0084-1024x755.jpg)](/img/uploads/DSC0084.jpg)


## How to try it out:


To get started:



 	
  1. Download and install Java 11 from [jdk.java.net/11](http://jdk.java.net/11/)

 	
  2. Download the [GeoServer 2.15-M0 milestone release](http://blog.geoserver.org/2019/01/01/geoserver-2-15-m0-release/) of GeoServer

 	
    * The GeoServer 2.15-M0 will run under Java 11 with no additional configuration on **Tomcat 9** or newer and **Jetty 9.4.12** or newer.

 	
    * The binary distribution includes a compatible version of Jetty.









We need your help:



 	
  * pulling [together running on java 11](https://docs.geoserver.org/latest/en/user/production/java.html#running-on-java-11) instructions for additional application servers, please download the WAR bundle to help out

 	
  * testing the windows installer







## Sponsors


Thanks to Gaia3D for leading with a silver sponsorship, and ASTUN Technology, OSGeo:UK, and ATOL for their bronze sponsorships.

[![Gaia3d](https://wiki.osgeo.org/images/thumb/3/34/Gaia3d.png/350px-Gaia3d.png)](http://www.gaia3d.com/)

[![AstunLogo.png](https://wiki.osgeo.org/images/e/e8/AstunLogo.png)](http://astuntechnology.com/)

[![uk.osgeo.org](https://wiki.osgeo.org/images/thumb/c/cd/Osgeo-uk.png/300px-Osgeo-uk.png)](https://wiki.osgeo.org/wiki/File:Osgeo-uk.png) [![Atol](https://wiki.osgeo.org/images/thumb/f/f9/Atol_logo.png/300px-Atol_logo.png)](https://www.atolcd.com/)

These sprints also require people to function, and we appreciate Boundless, GeoCat, ASTUN Technology, GeoSolutions and CCRi for their in-kind participation.

[![Boundless](https://wiki.osgeo.org/images/thumb/6/66/Boundless_Logo.png/300px-Boundless_Logo.png)](http://boundlessgeo.com/)

[![Astun.png](https://wiki.osgeo.org/images/5/5a/Astun.png)](https://astuntechnology.com/)   [![Ccri.](https://wiki.osgeo.org/images/thumb/b/bf/Ccri.png/150px-Ccri.png)](https://www.ccri.com/)

[![Geosolutions](https://wiki.osgeo.org/images/thumb/e/e0/Geosolutions.png/150px-Geosolutions.png)](https://www.geo-solutions.it/) [![GeoCat](https://wiki.osgeo.org/images/thumb/0/03/GeoCat.png/300px-GeoCat.png)](https://www.geocat.net/)


## Key accomplishments:





 	
  * GeoServer was upgraded to Spring 5. Thanks to David Vick and everyone for this (especially the Spring Security upgrade with James).

 	
  * Kevin went through the same steps for GeoWebCache for a difficult couple of days.

 	
  * The EMF models that drive much of our parsing technology were upgraded. Thanks to Ian who worked through this, putting us in a much better spot to make changes to our codebase.

 	
  * Torben helped remove countless references to internal "com.sun" classes.

 	
  * A big thanks to Andrea for stepping up where needed (i.e. everywhere) and encouraging everyone through out the week

 	
  * Thanks to Andrea and Brad for preliminary work that made this sprint possible.

 	
  * Thanks to Jody for doing the milestone release.


[![](/img/uploads/sprint-1024x485.jpeg)](/img/uploads/sprint.jpeg)


## Outstanding issues:


Certain components and dependencies could not be upgraded as no Java 11-compatible versions have been released. These have been removed or replaced by different libraries where possible, but some incompatible libraries remain.

The remaining issues are primarily either Internal API usage or Illegal access. These will only cause problems when running on Java 11:


#### Internal API usage


Some components and dependencies reference internal Java API. Depending on the nature of this API, calling this code may cause a runtime error or a warning when running on Java 11. If you run into any unusual failures when running under Java 11, please [report them](https://osgeo-org.atlassian.net/projects/GEOS).

Examples of libraries producing these warnings:



 	
  * freemarker template library (used for GetFeatureInfo responses)

 	
  * ehcache library used for image mosaic performance

 	
  * Java Advanced Imaging used for image processing




#### Illegal Access


Java 11 introduces stricter access constraints on reflective operations. For now, such issues will only cause a warning in the logs, of the form:





<blockquote>WARNING: Illegal reflective access by ...</blockquote>





In future versions of Java, this will instead cause a runtime error.

Known warnings you can expect when running in Java 11:



 	
  * org.hsqldb.persist.RAFileNIO

 	
  * org.parboiled.transform.AsmUtils

 	
  * org.fest.reflect.util.Accessibles

 	
  * com.google.protobuf.UnsafeUtil

 	
  * net.sf.cglib.core.ReflecUtils


If you run into a reflective access warning about a package not in this list, please [report it](https://osgeo-org.atlassian.net/projects/GEOS).


#### Community Modules


The following community modules do not yet support Java 11:



 	
  * printing

 	
  * script

 	
  * spatiallite

 	
  * monitor-hibernate




## Further reading:





 	
  * [GSIP-171 Java 18.9 Compatibility](https://github.com/geoserver/geoserver/wiki/GSIP-171)

 	
  * [Java 2018 Code Sprint](https://wiki.osgeo.org/wiki/Java_2018_Code_Sprint)

 	
  * [GeoServer 2.15-M0 Release](http://blog.geoserver.org/2019/01/01/geoserver-2-15-m0-release/)


