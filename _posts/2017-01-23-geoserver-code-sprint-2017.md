---
author: jgarnett
comments: true
date: 2017-01-23 19:04:01+00:00
layout: post
link: http://blog.geoserver.org/2017/01/23/geoserver-code-sprint-2017/
slug: geoserver-code-sprint-2017
title: GeoServer Code Sprint 2017
wordpress_id: 2780
categories:
- Behind The Scenes
tags:
- Code Sprint
- rest
---

[GeoSolutions](http://www.geo-solutions.it) has offered to host the GeoServer team for a [Java 2017 code sprint](https://wiki.osgeo.org/wiki/Java_2017_Code_Sprint) to look at updating, fixing and documenting the the GeoServer REST API. The GeoServer [REST API](http://docs.geoserver.org/latest/en/user/rest/index.html) is used to remotely manage a GeoServer instance and has proven highly successful for [automation](http://docs.geoserver.org/latest/en/user/rest/examples/curl.html), [integration with other applications](http://blog.geoserver.org/2015/12/23/geoserver-explorer-plugin-for-qgis/), with libraries for [java](https://github.com/geosolutions-it/geoserver-manager) and [python](https://github.com/boundlessgeo/gsconfig) remote management.[
](http://blog.geoserver.org/wp-content/uploads/2017/01/rest-api.png)

[![rest-api](http://blog.geoserver.org/wp-content/uploads/2017/01/rest-api-1.png)](http://blog.geoserver.org/wp-content/uploads/2017/01/rest-api-1.png)

The code sprint is dedicated to:



 	
  * Migrating from the _restlet_ library to _Spring MVC_ library. As an early adopter GeoServer selected the _restlet_ library as best of breed at the time. It has not aged well, and _Spring MVC_ represents a supported annotation based solution that is familiar to more developers.

 	
  * Although popular the REST API has not attracted a lot of investment, leading it to have the highest bug count of any of our GeoServer modules! This sprint would like to directly reduce this bug count, and indirectly reduce this bug count by introducing more developers to this area of the codebase.

 	
  * The REST API also has the greatest number of requests for documentation and examples. This code sprint will update the documentation for each area of the REST API as as it is migrated, and look at some of the solutions for the automated collection of examples requests.

 	
  * We will be sure to test against the [gsconfig](https://github.com/boundlessgeo/gsconfig) python library and [geoserver-manager](https://github.com/geosolutions-it/geoserver-manager) java library.


The GeoServer team has previously planned and executed a [highly successful code sprint](http://blog.geoserver.org/2016/01/25/geoserver-code-sprint-success/). We would like to once again ask for your support and participation in 2017.


## Viareggio, Lucca




The code sprint is planned for a week in March in the glamorous GeoSolutions headquarters of Viareggio, Lucca. Thanks to GeoSolutions for providing a venue, space is limited to 10-15 people so hit the wiki to sign up if you are interested.




[![Viareggio,_passeggiata_a_mare_2](http://blog.geoserver.org/wp-content/uploads/2017/01/Viareggio_passeggiata_a_mare_2-300x225.jpg)](http://blog.geoserver.org/wp-content/uploads/2017/01/Viareggio_passeggiata_a_mare_2.jpg)




A note on the timing: We were unable to join the [Daytona Code Sprint 2017](https://wiki.osgeo.org/wiki/Daytona_Beach_Code_Sprint_2017) as it is scheduled too close to the GeoServer 2.11 code freeze. GeoSolution's offer to host in Europe will reduce travel costs allowing us to run the event with minimal sponsorship.





## Participation and Sponsorship


We have the following sponsorship levels available:



 	
  * Gold: $1000

 	
  * Silver: $500

 	
  * Bronze: $250


We are reaching out to international and local sponsors. Contributions will be put towards travel costs for overseas sprinters who would be otherwise unable to attend. Any surplus at the end of the event will be turned over to OSGeo or used for a future code sprints.

For more details on participation, sponsorship or budget for the event please see the [Java 2017 Code Sprint 2017](https://wiki.osgeo.org/wiki/Java_2017_Code_Sprint#How_to_Sponsor) on the OSGeo wiki.
