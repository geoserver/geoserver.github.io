---
author: Chris Holmes
comments: true
date: 2007-11-09 17:06:38+00:00
layout: post
link: http://blog.geoserver.org/2007/11/09/geoserver-community-happenings/
slug: geoserver-community-happenings
title: GeoServer community happenings
wordpress_id: 76
categories:
- Developer notes
---

One thing we've wanted to do with this blog is use it as a forum to allow people to follow what's going on in the world of GeoServer without having to dive in to hundreds of messages per month on the lists.  I've been blogging long enough to know that I should never make promises about how often posts will come, but I will say that more of these will come in the future.

The most exciting things to me are a few new contributions that are becoming community modules, with their authors joining the community.  The first one to bubble up has been adding support for GeoServer to create an html image map, there were [several](http://www.nabble.com/GeoServer-HTML-ImageMap-extension--tf4342893.html#a12371765) [discussions](http://www.nabble.com/GeoServer-HTML-ImageMap-extension--tf4635290.html#a13237227) on the lists, with a couple different approaches developed simultaneously.  The result is that Mauro Bartolomeoli is in the process of putting his code in to a community module, there is a [wiki page describing it](http://docs.codehaus.org/display/GEOS/HTMLImageMap+support), and the code is currently attached to [the jira issue](http://jira.codehaus.org/browse/GEOS-1406) tracking it.  We hope to get the code in svn and get a plugin release relatively soon.  This feature enables users to make a map with tooltips and pop-ups and the like, having it directly composed by GeoServer.  Since it is html that is returned this can scale a lot better than returning features and having pure javascript display them.

The other contribution in the works is some great stuff by the [Ominiverde](http://ominiverdi.org/) team, focusing on styling and a RESTful service for SLD.  No wiki page or code yet, but they sent an email to the list [describing the work](http://www.nabble.com/SLD-SERVICE-RESTLET-PROPOSAL%21-tf4777451.html), with a link to a test [live service](http://test.ominiverdi.org:8080/geoserverSld/sldservice/topp:states).   This should be the basis of a nice thematic mapping gui based on openlayers.  The cool thing is it will leverage code from uDig, to enable all the nice work they've done there, but in a web environment.

The other thing I'll mention here, that I think hasn't spread very widely, is that the latest version of [GeoNetwork](http://geonetwork-opensource.org/) includes an embedded GeoServer.  This is being used as a base map on top of which other layers can be added.  The integration is still pretty minimal, GeoServer is basically just providing a nicer base map.  But there is some work coming soon to do a tighter integration, so that users will be able to upload a shapefile or geotiff through GeoNetwork and have it automatically available through GeoServer as WMS and WFS or WCS, picking up all the service metadata properly.  Andrea Aime is currently in Rome, discussing this with developers and users at the GeoNetwork conference this week, where he also gave a workshop on GeoServer.

There's much more happening, on a variety of fronts, but we'll save it for another post.
