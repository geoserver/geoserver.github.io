---
author: Jody Garnett
date: 2022-01-20
layout: post
title: Log4j1 update or replace activity
categories:
- Behind The Scenes
---

While GeoServer is [not vulnerable to Log4J2 Log4Shell vulnerability]({% post_url 2021-11-22-logj4-rce-statement %}), we would like to thank everyone who has reached out with offers of concern and assistance.

The **Log4J 1.2** library used by GeoServer has a number of smaller vulnerabilities which we would like to address. While the **GeoServer default configuration** is not vulnerable it is time to upgrade or replace this library. If you are at all concerned, locate `WEB-INF/lib/log4j-1.2.17.jar` and replace with our custom [log4j-1.2.17.norce.jar](https://repo.osgeo.org/repository/geotools-releases/log4j/log4j/1.2.17.norce/log4j-1.2.17.norce.jar), and restart GeoServer.

The GeoSever Project Steering Committee invites:

* Proposals for [updating or replacing the Log4J1](https://github.com/geoserver/geoserver/wiki/Update-or-replace-Log4J-1-library) library used by GeoServer.
  
  Successful proposals should consider changes required to GeoTools logging (which bridges from java utility logging to selected logging library), integration with GeoWebCache (uses apache-commons-logging to delegate to selected logging library), and GeoServer (which allows users to select different logging profiles without restarting the application).
  
* [Sponsors](https://github.com/geoserver/geoserver/wiki/Sponsor) interested in funding this activity as a security concern.

  Organizations running GeoServer in a cloud environment are also encouraged to fund this activity. The leading contenders (log4j2,logback,java util logging) provide better integration with cloud logging services than the log4j1 library presently used.

This is a time sensitive activity as we would like to select a good proposal and see the result implemented for the upcoming GeoServer 2.21-RC Release Candidate in March.

Thanks to activity sponsors for your support:

* [opengeogroep.nl](https://opengeogroep.nl/)
* [www.terrestris.de](https://www.terrestris.de/en/)
* [how2map.com](http://how2map.com)
* [Add your name here](https://github.com/geoserver/geoserver/wiki/Sponsor) via OSGeo GitHub Sponsorship (monthly donation), PayPal (one time donation), or OSGeo sponsorship (direct invoice).

For more information visit [updating or replacing the Log4J1](https://github.com/geoserver/geoserver/wiki/Update-or-replace-Log4J-1-library) wiki page.