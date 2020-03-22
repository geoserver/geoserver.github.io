---
author: arneke
comments: true
date: 2008-02-20 17:35:46+00:00
layout: post
link: http://blog.geoserver.org/2008/02/20/announcing-geowebcache-060/
slug: announcing-geowebcache-060
title: Announcing GeoWebCache 0.6.0
wordpress_id: 86
categories:
- Announcements
---

GeoWebCache is finally [out in the open](http://geowebcache.org) and announced on [freshmeat.net](http://freshmeat.net) and other pages. This should really have happened a long time ago, and there are many reasons for why it didn't, but I am very excited about the current momentum.

GeoWebCache, is a tile cache, meaning it acts as a proxy between the client and the WMS server (GeoServer) and stores the image. If another client requests the tile it can respond in milliseconds, regardless of the complexity of the tile. It is different from a regular HTTP proxy, such as Squid, in that it interprets the parameters and matches them to the best tile supported by the configuration.

It is currently not as mature as say [Tile Cache](http://tilecache.org), but has the advantage that you do not need a webserver with Python support. It can either be run in Tomcat, alongside GeoServer, or as a standalone server using Jetty (no binaries are available yet, but we will make them soon).

We have not been sitting still since releasing 0.6.0 either. Based on a customer request we have already added native support for Microsoft Virtual Earth's quadkey scheme. This is currently available in the repository, and we'll probably push it out in a new version soon, after looking into whether we can do the same for the Google Maps API.

Looking to [version 0.7.0 and beyond](http://geowebcache.org/trac/roadmap?) we will start  working on integrating GeoWebCache more tightly with GeoServer. Some key features are



	
  * Automatic configuration based on what layers are available . This will obviously have some limitations, since there are important parameters that the user will have to make some decisions on.

	
  * Update events, so that when the data changes on the backend GeoWebCache will automatically purge the affected tiles and (optionally) reseed them.

	
  * A nice RESTful API that we can program an easy to use JavaScript client against.


There are some internal structures that should still be simplified, and now that the basic structure has solidified we'll gradually start adding tests.

Want to see it in action? [http://sigma.openplans.org](http://sigma.openplans.org) has been using GeoWebCache for over two months (and uncovered some bugs in the process). We look forward to upgrading the site with something that is really pretty to look at, probably soon.

Please sign up to the [mailing lists](http://sourceforge.net/mail/?group_id=215120) if you are interested, we'd love to hear back from you so that we can fix bugs, improve the documentation and stake out the general course.
