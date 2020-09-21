---
author: geoserver
comments: true
date: 2010-04-19 07:35:25+00:00
layout: post
link: http://blog.geoserver.org/2010/04/19/increasing-geoserver-performance-and-stability-with-flow-control/
slug: increasing-geoserver-performance-and-stability-with-flow-control
title: Increasing GeoServer performance and stability with flow control
wordpress_id: 625
---

Putting a public OGC server in production can be a daunting task.  Dynamic web GIS requests (be they WMS or WFS) consume significantly more resources than a regular web site, making the service quite demanding in terms of memory, CPU, and bandwith consumption. When a service becomes popular, requests start fighting for limited resources and put the hardware under considerable strain, possibly leading to failure due to lack of available memory.

The default GeoServer configuration already provides some help in this regard: it is already possible to limit the resources used by a single request by setting the maximum amount of features returned in a WFS request and by setting the [maximum time and memory](http://docs.geoserver.org/2.0.x/en/user/services/wms/configuration.html#request-limits) allowed for a WMS request. That is not enough, however, as it is still possible for the service to be bogged down by a large number of requests.

The[ control flow](http://docs.geoserver.org/2.0.x/en/user/community/controlflow/index.html) community module was developed to enable an administrator to impose limits on the total amount of work GeoServer may execute in parallel. With control flow, it is possible to limit the number of GetMap requests that will ever be served concurrently or to limit the number of requests that a single user may run in parallel. This simultaneously improves resource consumption, fairness, and performance.

Because it is a community module, you'll only be able to find control flow in [nightly builds](http://gridlock.openplans.org/geoserver/2.0.x/). I recommend everyone running a public GeoServer instance look into the [documentation](http://docs.geoserver.org/2.0.x/en/user/community/controlflow/index.html), install it, and reap the benefits of increased resource control. I've actually been running it for over two months without issue on a relatively busy server (up to 60 thousand requests per day), resulting in greater up-times and fewer failed requests. Let us know how it works for you—if the module becomes popular we plan to turn it into an official extension that will be available in official releases.
