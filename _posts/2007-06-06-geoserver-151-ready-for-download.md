---
author: Chris Holmes
comments: true
date: 2007-06-06 17:54:25+00:00
layout: post
link: http://blog.geoserver.org/2007/06/06/geoserver-151-ready-for-download/
slug: geoserver-151-ready-for-download
title: GeoServer 1.5.1 ready for download
wordpress_id: 51
categories:
- Announcements
---

The GeoServer team is pleased to announce the [latest release](http://docs.codehaus.org/display/GEOS/GeoServer+1.5.1) in the stable 1.5.x series.  It's great to see GeoServer settling to be a really mature project, as most of the [changes](http://jira.codehaus.org/secure/IssueNavigator.jspa?reset=true&pid=10311&fixfor=13320) done for 1.5.1 were actually improvements instead of bug fixes.  The big change is that we're shipping with [OpenLayers](http://openlayers.org) as our default preview and demo application.  And we took a bit of extra time to get GeoServer producing tiles with nice labels by borrowing 'metaTile' ideas from [TileCache](http://labs.metacarta.com/wms-c), creating them on the fly and in memory.  This summer we've got a Google Summer of Code [project](http://code.google.com/soc/osgeo/appinfo.html?csaid=FED722EC29A37BC5) to work on Tile Caching, so soon those tiles will be cached to disk (and distributed about) as well.

The other fun OpenLayers improvement we've got is making it available as an output format.  So instead of


<blockquote>[http://server.org/geoserver/wms?bbox=-13....&Format=image/png](http://localhost:8080/geoserver/wms?bbox=-130,24,-66,50&styles=&request=GetMap&layers=topp:states&width=550&height=250&srs=EPSG:4326&Format=image/png)</blockquote>


You can do


<blockquote>[http://server.org/geoserver/wms?bbox=-13...&Format=application/openlayers](http://localhost:8080/geoserver/wms?bbox=-130,24,-66,50&styles=&request=GetMap&layers=topp:states&width=550&height=250&srs=EPSG:4326&Format=application/openlayers)</blockquote>


and you'll get an interactive OpenLayers map instead of a mere png image.  Just put _**Format=application/openlayers**_ on any WMS request and we'll make an OpenLayers map with it, changing the default parameters as you pass them in.

And if putting in all those WMS values in is too much for you, we've now got a WMS reflector that makes some guesses as to reasonable defaults.  So you can do:


<blockquote>[http://localhost:8080/geoserver/wms/reflect?layers=topp:states  ](http://localhost:8080/geoserver/wms/reflect?layers=topp:states)</blockquote>


The defaults aren't ideal yet, we're hoping to improve them for the next release to be able to derive more defaults, like take in to account the bbox of the dataset.

Past OpenLayers we've got a lot of nice KML improvements.  First up we've got templates, see the [new tutorial](http://docs.codehaus.org/display/GEOSDOC/KML+Placemark+Templates) on this great feature.  We've leveraged the great [FreeMarker](http://freemarker.sourceforge.net/) templating library to give users incredibly powerful control over the output of KML pop-ups.  Soon we'll also make this available to GetFeatureInfo and GeoRSS as well.  Our old pop-ups would just dump attribute information, now users can make use of KML's html features and link in content using the information stored in their geospatial data.

Other KML improvements include [our first crack](http://docs.codehaus.org/display/GEOSDOC/Google+Earth#GoogleEarth-superoverlay) at [SuperOverlays](http://code.google.com/apis/kml/documentation/kml_21tutorial.html#superoverlays), which are easily one of the most powerful features in Google Earth.  We've taken most all the complexity out of them, allowing users to just configure their layers in GeoServer and we'll automatically do the super overlay.  Right now GeoServer generates all data on the fly, but soon we should have a few caching options.  We also have a few other small improvements for KML, like picking up point icons from SLD, a param to [add a Legend](http://docs.codehaus.org/display/GEOSDOC/Google+Earth#GoogleEarth-legend) to Google Earth, and cleaning our output up so it works with Google Maps better.

We've also had some great contributions this release.  Saul Farber of MassGIS has his ArcSDE raster support in pretty good shape, and is looking for users to test it out and give feedback.  If anyone gets it going with Google Earth Superoverlays do let us know.  More details will be on this blog soon. The other nice contributions were translations of the web admin console to Chinese and Portuguese, adding to Spanish, German, Japanese, and French.

Please give us feedback on this release, especially on documentation and the KML improvements.  We're looking to do a big press release  for the next release to highlight the recent work, and hopefully pick up some new users, so want to be sure everything is really tight.
