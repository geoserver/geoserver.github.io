---
author: Brent Owens
comments: true
date: 2007-01-04 22:54:36+00:00
layout: post
link: http://blog.geoserver.org/2007/01/04/google-earth-and-geoserver/
slug: google-earth-and-geoserver
title: Google Earth and GeoServer
wordpress_id: 17
categories:
- Tutorials
---

As some of you may know, GeoServer can serve up WMS data as KML or KMZ for Google Earth. There is a full video tutorial located [here](http://geoserver.codehaus.org/tutorials/videos/google_earth/google_earth.html) on how to set it up.


One of the tools GeoServer has to make serving up KML/KMZ easier is a reflector script. This exists so people don't have to type in an entire WMS request URL to view the data in Google Earth. Here is an example of its use:




_http://localhost:8080/geoserver/wms/kml_reflect?layers=states_




By using this URL, you can ignore all the other WMS information. Information such as projection, image size, output format etc. You can also specify more than one layer by just separating the layer names with commas: layers=states,roads,lakes




The reflector will take the layer names and fill in the missing information, then return back a full WMS request. Users have asked why a URL is being returned when they use the reflector in their web browser. The reflector is meant to be used within Google Earth in a Network Link. The network link will interpret the returned WMS request and send it off again to GeoServer to get the real KML data back. So at first it makes two requests to get the real data, but after that it updates with just one get map request.




One recent item of discussion has been how to format the description of the features that are returned. In KML you can return an HTML description of the data.








![ge attributes](http://sigma.openplans.org/blog/ge_attributes.jpg)




What we do is take all of the feature information and put it into an HTML table that pops up when you click on the feature. But say if you wanted to hide some of the attribution, or turn some value into hyper links, there is no current way to do this (at least with not hacking the code). A few ideas have been suggested: including the formatting information into the SLD file, have a separate SLD-like file for just the descriptions, and XML transforms with a template document. In order to make a decision on which path to take, we would like some input from the users: use-case scenarios, requirements, etc.




So drop us a line and tell us what you think.
