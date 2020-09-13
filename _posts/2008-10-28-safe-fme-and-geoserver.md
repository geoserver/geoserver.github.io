---
author: Chris Holmes
comments: true
date: 2008-10-28 23:08:23+00:00
layout: post
link: http://blog.geoserver.org/2008/10/28/safe-fme-and-geoserver/
slug: safe-fme-and-geoserver
title: Safe FME and GeoServer
wordpress_id: 143
categories:
- Behind The Scenes
---

[OpenGeo](http://opengeo.org) and [Safe Software](http://safe.com) have been talking about working together to make life easier for users of [FME](http://www.safe.com/products/overview.php) and [GeoServer](http://geoserver.org).  We've both been hearing more about organizations using FME to solve their data conversion challenges and then making the results available to the world using the [OpenGeo Stack](http://opengeo.org/technology/).

While many people are making things work with the software now, we figure that a few improvements towards tighter integration could be a big win.  Our end goal is to enable [FME Server](http://www.safe.com/products/server/overview.php) and GeoServer to work together seamlessly.  This allows each piece to solve the area they excel at - GeoServer in OGC standards and web output formats, FME at complex data conversions and translations.  With a few key improvements the combined solution should solve the 'Community Schema' problem that Ron Lake recently [brought up](http://www.galdosinc.com/archives/545) better than any software in world.  In time the GeoServer community will definitely build the capability to handle the full community schema transformation natively, but integrating with FME should provide a transitional path, and FME will always be ahead in terms of the most advanced translations.

If you are a user of both FME and GeoServer we'd love to hear from you with input on how we could work together to make your life easier (or you can just give us encouragement ;).  We are still in the early stages, hoping to put together a rough prototype relatively soon, but beta testers in the future will be appreciated. And of course additional funding will enable us to prioritize the work and get it done faster.  If you are interested in helping out please get in touch at the [OpenGeo contact form](http://opengeo.org/contact/ ).
