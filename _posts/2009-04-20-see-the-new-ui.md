---
author: bmmpxf
comments: true
date: 2009-04-20 14:00:58+00:00
layout: post
link: http://blog.geoserver.org/2009/04/20/see-the-new-ui/
slug: see-the-new-ui
title: See the new UI
wordpress_id: 201
categories:
- Announcements
tags:
- UI wicket alpha release
---

I am happy to announce to everyone a sneak peak of the future of GeoServer.  Behold the newest [alpha release of GeoServer 2.0](http://geoserver.org/display/GEOS/GeoServer+2.0-alpha2).

I [first mentioned GeoServer 2.0 last August](http://blog.geoserver.org/2008/08/11/a-new-ui-is-dawning/) when the first alpha was released, but much work has been done since then.  The most obvious and exciting new feature in GeoServer 2.0 is the [new UI](http://geoserver.org/display/GEOS/GSIP+23+-+Wicket+UI), based on the [Wicket](http://wicket.apache.org) framework.  The UI has been totally redesigned and updated to provide a greatly improved user experience.  Take a look at some screenshots:

[![](/img/uploads/front-new-300x231.png)](/img/uploads/front-new1.png)

Front page

[![](/img/uploads/status-new-300x231.png)](/img/uploads/status-new1.png)

Status

[![](/img/uploads/demo-new-300x231.png)](/img/uploads/demo-new1.png)

Layer preview

[![](/img/uploads/styles-new-300x231.png)](/img/uploads/styles-new1.png)

Styles



Another happy announcement is a major workflow change for data configuration.  The **Submit -> Apply -> Save** workflow, often bemoaned by users, has been eliminated, in favor of a simpler **Save changes** workflow, with changes automatically persisting.  To me, that's a 66.6% reduction in button clicks!

**This is an alpha release** (the most recent stable version remains at [1.7.3](http://geoserver.org/display/GEOS/GeoServer+1.7.3))  and so it comes with a few caveats.  It's very new code, and not fully tested, so please don't run it in a production environment.  Features may also be likely to change as the code approaches stability.  Also, running GeoServer 2.0 with an existing data directory will alter it such that it will become incompatible with existing stable versions.  We have instructions on [how to migrate back to 1.7.x](http://geoserver.org/display/GEOSDOC/Migrating+Between+1.7.x+and+2.0.x), but it might be better to use the built-in data directory for now, or at least to back up your existing data directory first.

That said, we want everyone to [download, try it out](http://geoserver.org/display/GEOS/GeoServer+2.0-alpha2), and provide feedback, since it was partly in response to user feedback that the GeoServer Team upgraded the user environment.  I hope you enjoy!
