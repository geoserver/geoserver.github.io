---
author: jgarnett
comments: false
date: 2019-03-02 10:16:05+00:00
layout: post
link: http://blog.geoserver.org/2019/03/02/geoserver-2-15-0-released/
slug: geoserver-2-15-0-released
title: GeoServer 2.15.0 Released
wordpress_id: 3005
categories:
- Announcements
tags:
- Release
release: release_215
version: 2.15.0
jira_version: 16736
---

The GeoServer team is happy to announce the [GeoServer 2.15.0](http://geoserver.org/release/2.15.0/) release with downloads ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.0/geoserver-2.15.0-bin.zip/download)|[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.0/geoserver-2.15.0-war.zip/download)|[exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.0/geoserver-2.15.0.exe/download)), documentation ([html](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.0/geoserver-2.15.0-htmldoc.zip/download)|[pdf](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.0/geoserver-2.15.0-user-manual.pdf/download)) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.15.0/extensions/).

This release is production ready and is ready to work with your Java 8 or Java 11 operational environment. This release is made in conjunction with GeoWebCache 1.15.0 and GeoTools 21.0.

The ability to work with Java 11 is the result a [dedicated code sprint](http://blog.geoserver.org/2018/09/24/java-2018-code-sprint/). Thanks to organizations participating in the code sprint ([Boundless](http://boundlessgeo.com/), [GeoSolutions](https://www.geo-solutions.it/), [GeoCat](https://www.geocat.net/), [Astun Technology](https://astuntechnology.com/), [CCRi](https://www.ccri.com/)) along with sprint sponsors ([Gaia3D](http://www.gaia3d.com/), [atol](https://www.atolcd.com/), [osgeo:uk](https://uk.osgeo.org/), [Astun Technology](https://astuntechnology.com/)).


### Layer Service Settings


To start things off an often requested capability, the ability to control which services are enabled on a layer-by layer basis.

[![](/img/uploads/per-layer-service.png)](/img/uploads/per-layer-service.png)

To try it our yourself see [Service Settings](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#services-settings) in our user manual.


### GeoFence Internal Server Extension


Originally a standalone service offering fine grain control over GeoServer security this functionality has been packaged up and embedded into a GeoServer extension for easier deployment.



 	
  * GeoFence rules provided greater control over security allowing layer by layer service restrictions

 	
  * GeoFence rules can provide access to data overriding layer details including CQL filter to limit contents returned and default style used for rendering

 	
  * GeoFence rules can limit access to a geographic extent


[![](/img/uploads/geofence_limit.png)](/img/uploads/geofence_limit.png)

For more details see [GeoFence Internal Server](https://docs.geoserver.org/latest/en/user/extensions/geofence-server/index.html) in our user manual.


### Style Editor SLD Auto-Complete


To help make editing easier the Style Editor can provide auto-complete suggestions for SLD 1.0. To try it out yourself use control-space for context aware suggestions.

[![](/img/uploads/sld_autocomplete.png)](/img/uploads/sld_autocomplete.png)


### Generate Classified Thematics maps


[SLDService](https://docs.geoserver.org/latest/en/user/extensions/sldservice/index.html) is now an official extension, with a number of improvements. SLDService can now be used for the



 	
  * classification of raster data too

 	
  * equal area classification

 	
  * standard deviation filtering


The SLD REST Service extension is used to generate thematic styles based on attribute data:

    
    curl -v -u admin:geoserver -XGET
      http://localhost:8080/geoserver/rest/sldservice/states/classify.xml
      ?attribute=PERSONS
      &ramp=CUSTOM
      &method=quantile
      &intervals=3
      &startColor=0xFF0000
      &endColor=0x0000FF
      &open=true


For more information see [SLD Rest Service](https://docs.geoserver.org/latest/en/user/extensions/sldservice/index.html) in our user manual.

[![](/img/uploads/sld-rest-service.jpg)](/img/uploads/sld-rest-service.jpg)


### WPS GetExecutionStatus and Dismiss Operations


WPS "GetExecutions" vendor operation allows each user to get the list of running processes:



 	
  * Users can review all their running processes

 	
  * Administrators can see all processes


The Dismiss vendor operation can be used to cancel the execution of one of the listed processes.

For more information see [Dismiss](https://docs.geoserver.org/latest/en/user/services/wps/operations.html) in our user guide.


### Java 11 Support


The provided binary download works with either Java 8 or Java 11. Tomcat 9 or newer is required for the WAR install. The user guide [compatibility list](https://docs.geoserver.org/latest/en/user/production/java.html#running-on-java-11) will continue to be updated based on your feedback.

The java ecosystem is now being led by the open source OpenJDK project, with [long term suppor](https://medium.com/@javachampions/java-is-still-free-c02aef8c9e04)t available from a range of organizations notably [RedHat OpenJDK](https://developers.redhat.com/products/openjdk/overview/)  and [Adopt OpenJDK](http://adoptopenjdk.net). The GeoTools [user guide](http://docs.geotools.org/latest/userguide/build/install/jdk.html) provides an overview of Java 8 and Java 11 distributions.

The net effect of these changes:



 	
  * If you have been using Oracle JDK please review your options

 	
  * Java 8 will continue to be available

 	
  * The Java ecosystem is now led by the open-source Open JDK project


Java 11 no longer supports the Java 2 extension mechanism used for native JAI and native ImageIO libraries.  We recommend the use of the pure Java JAI-EXT operations which have been made the default (see the next section).


### JAI-EXT operations on by default


The use of the JAI-EXT operations have long been a recommendation, with this release we are making them the default for GeoServer.  The JAI-EXT library offers a pure java implementation enhanced for geospatial functionality supporting NODATA pixels and support for vector footprints.

[![](/img/uploads/jai-ext-operations-1.png)](/img/uploads/jai-ext-operations-1.png)


### GeoServer Codebase


In addition to Java 11 support this release includes:



 	
  * Add JSON as a Legend Output format (GISP 173)

 	
  * Printing plugin upgrade version of JTS

 	
  * Upgrade NetCDF dependencies

 	
  * Improvements for vector tile production, both in terms of output correctness and production performance


Thanks to Andrea Aime for steady work on the codebase quality:

 	
  * [PMD](https://pmd.github.io/) source code analysis, high priority checks, will fail the build in case of issues

 	
  * [Error Prone](https://errorprone.info) byte code analysis, same as above

 	
  * Many small bugs fixed


For more details developers are invited to review [Automated Quality Assurance checks](https://docs.geoserver.org/latest/en/developer/qa-guide/index.html) in our developers manual. Also, work in ongoing on the master (dev) branch to extend the reach of static code checks using SpotBugs and CheckStyle too.


## About GeoServer 2.15 Series


Additional information on the GeoServer 2.15 series:



 	
  * Release Notes ([2.15.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16736)|[2.15-RC](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16740)|[2.15-M0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16746))

 	
  * [Running on Java 11](https://docs.geoserver.org/latest/en/user/production/java.html#running-on-java-11) (User Manual)


