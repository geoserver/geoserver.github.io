---
author: Chris Holmes
comments: true
date: 2007-05-16 18:10:47+00:00
layout: post
link: http://blog.geoserver.org/2007/05/16/web-processing-service-wps-demos-with-geoserver/
slug: web-processing-service-wps-demos-with-geoserver
title: Web Processing Service (WPS) demos with GeoServer
wordpress_id: 41
categories:
- User perspectives
---

Theodor Foerster, of [52North](http://52north.org) and [ITC](http://www.itc.nl/), has been leveraging GeoServer in his work on generalization of geospatial data using the new Web Processing Service specification.  He recently posted some nice new work, including updates to the [Web Processing Service web app](http://incubator.52north.org/twiki/bin/view/Processing/52nWebProcessingService), as well as a new [WPS client](http://incubator.52north.org/twiki/bin/view/Processing/52nUdigWPSClient) written as a plug-in to [uDig](http://udig.refractions.net).   Awhile ago he also did some [prototypes](https://incubator.52north.org/twiki/bin/view/Processing/52nWebProcessingServiceInGeoserver) of integrating the WPS with GeoServer, making the WPS a datastore that could be served out as WMS and WFS.   It's great to see new open source tools being built that can use and leverage the work we've done with GeoServer.  You can see his work in action, with GeoServer, in the [screencast](http://52north.org/index.php?option=com_projects&task=showProject&id=21&Itemid=127#demos) that he's also posted.

Eventually we're hoping to be able to offer some integration between GeoServer and his WPS work, possibly as a plug-in to GeoServer that makes it really easy to install both, and to do common data configuration through our web gui.  In the past we've also talked to the [FROGS](http://frogs.tigris.org/) WPS community about possible integrations as well.  Since we're evolving GeoServer to be a platform it makes a lot of natural sense to be able to bring WPS in to the mix, in some form.  It looks like the FROGS people are also leveraging [Spring](http://springframework.org), which may help compatibility as well (we haven't talked to them for awhile so I suppose we can just cross our fingers that they're looking at what we've done).  So if anyone has the time or the money to get a WPS integrated with GeoServer, let us know, as we've got some great pieces to work with.
