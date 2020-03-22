---
author: geoserver
comments: true
date: 2014-01-07 09:01:27+00:00
layout: post
link: http://blog.geoserver.org/2014/01/07/using-geoserver-at-ign-the-french-national-mapping-agency-to-create-new-digital-maps/
slug: using-geoserver-at-ign-the-french-national-mapping-agency-to-create-new-digital-maps
title: Using GeoServer at IGN (the French National Mapping Agency) to create new digital
  maps
wordpress_id: 1741
---

We start the new year with a report of how IGN uses GeoServer to deliver high quality maps. We'd like to thank in advance the IGN team for the very nice showcase, and we leave you to their report.




Thanks to GeoServer and other technologies, IGN France is now able to provide new digital maps to professional users. These maps, named "SCAN Express", cover the French territory, and are fully updated every six months. Two kinds of map with two different color charts are available through the French Géoportail WMS and WMTS services ([http://api.ign.fr](http://api.ign.fr/) ), offering an advanced cartographic map rendering of IGN’s topographic databases.




Here are some screenshots, with different zoom levels:





[![](http://geoserver.wpengine.com/wp-content/uploads/2014/01/sample1.png)](http://blog.geoserver.org/2014/01/07/using-geoserver-at-ign-the-french-national-mapping-agency-to-create-new-digital-maps/sample1/)



[![](http://geoserver.wpengine.com/wp-content/uploads/2014/01/sample2.png)](http://blog.geoserver.org/2014/01/07/using-geoserver-at-ign-the-french-national-mapping-agency-to-create-new-digital-maps/sample2/)



[![](http://geoserver.wpengine.com/wp-content/uploads/2014/01/sample3.png)](http://blog.geoserver.org/2014/01/07/using-geoserver-at-ign-the-french-national-mapping-agency-to-create-new-digital-maps/sample3/)

[![](http://geoserver.wpengine.com/wp-content/uploads/2014/01/sample4.png)](http://blog.geoserver.org/2014/01/07/using-geoserver-at-ign-the-french-national-mapping-agency-to-create-new-digital-maps/sample4/)



[![](http://geoserver.wpengine.com/wp-content/uploads/2014/01/sample6.png)](http://blog.geoserver.org/2014/01/07/using-geoserver-at-ign-the-french-national-mapping-agency-to-create-new-digital-maps/sample6/)

[![](http://geoserver.wpengine.com/wp-content/uploads/2014/01/sample7.png)](http://blog.geoserver.org/2014/01/07/using-geoserver-at-ign-the-french-national-mapping-agency-to-create-new-digital-maps/sample7/)




One color chart (the “standard legend”) offers pastel colors, so that user data can be added to the map, and keep it readable. The other one (the “classical legend”) is similar to well-established legends of IGN’s paper maps.







[caption id="attachment_1748" align="aligncenter" width="576" caption="Standard and classical legend"][![](http://geoserver.wpengine.com/wp-content/uploads/2014/01/sample8.png)](http://blog.geoserver.org/2014/01/07/using-geoserver-at-ign-the-french-national-mapping-agency-to-create-new-digital-maps/sample8/)[/caption]




First, data are processed using different softwares and libraries depending on scale (open-source, proprietary or home-made) performing automatic tasks such as generalization or high-level cartographic label placement. Thus, 1Spatial software or JTS library are used. Then, cartographers perform controls using desktop GIS such as OpenJump or GeoConcept. Data are stored in PostgreSQL/PostGIS databases.




Rendering is fully based on GeoServer capabilities.  More than 300 SLD files defining almost 2000 feature styles have been written to manage rendering with smooth transitions at 12 different zoom levels. In order to allow map legend customization, the “variable substitution in SLD" mechanism is used to compute easily different kind of color charts according to needs (about 50 variables allowing a wide range of customization possibilities).This could open the way to new web services that will allow dynamic customization of this cartographic background.




Raster tiles are produced by sending GeoServer WMS requests, whose resolution depends on the map scale, from 0.5 to 2048 meters per pixel. Requests are load-balanced on several GeoServe instances, to produce more than 500 Gb of data per color chart.


GeoServer is well suited to IGN’s need and its efficiency is much appreciated. IGN’s team focusing on these topics wishes to point out that the cartographic rendering capabilities of GeoServer are very rich and can be exploited in an industrial context.







