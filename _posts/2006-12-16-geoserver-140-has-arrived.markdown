---
author: Brent Owens
comments: true
date: 2006-12-16 00:15:43+00:00
layout: post
link: http://blog.geoserver.org/2006/12/15/geoserver-140-has-arrived/
slug: geoserver-140-has-arrived
title: GeoServer 1.4.0 has arrived!
wordpress_id: 15
categories:
- Announcements
---

It's finally here! Version 1.4.0 is out the door and kicking. This is quite an exciting release for us because it is taking GeoServer in a new, more developer friendly, direction with the [Spring](http://www.springframework.org/) framework it is built on. What we gain from this new framework is the ability to modularize GeoServer into separate components and allow for outside developers to create plug-ins easily. It used to be a lot more difficult to add extensions, comparatively to what we have now, and this means that we can look forward to new and interesting additions from the many users out there.




That said, I will point you at the documentation that describes just how to write your own plug-in: [http://docs.codehaus.org/display/GEOSDOC/4+Programmers+Guide](http://docs.codehaus.org/display/GEOSDOC/4+Programmers+Guide)




Of course there are many bug fixes and improvements in this release. We have also worked on stability a fair amount and are currently testing version 1.4.0 on our demo server: [Sigma](http://sigma.openplans.org) . So if you have a WMS up and running, feel free to point it at our layers and use our data. The more we can hit the server the easier it will be to find problems.




Hot on the heels of this release is GeoServer 1.5 with Web Coverage Service support. We hope to see the first release candidate in January. So stay tuned!




You can grab the 1.4.0 release [here](http://docs.codehaus.org/display/GEOS/GeoServer+1.4.0).
