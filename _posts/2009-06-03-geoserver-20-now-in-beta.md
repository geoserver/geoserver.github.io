---
author: aaime
comments: true
date: 2009-06-03 16:08:51+00:00
layout: post
link: http://blog.geoserver.org/2009/06/03/geoserver-20-now-in-beta/
slug: geoserver-20-now-in-beta
title: GeoServer 2.0, now in beta
wordpress_id: 214
categories:
- Announcements
- Developer notes
- Features
- Tutorials
- User perspectives
tags:
- beta
- release
- ui
---

The GeoServer Team is happy to announce [GeoServer 2.0-beta1](http://geoserver.org/display/GEOS/GeoServer+2.0-beta1), the first beta release of the 2.0 series.

The primary focus of version 2.0 is the **new user interface**.  This interface addresses many suggestions for usability improvements, including paging and filtering of lists of information, batch removal of layers, and the elimination of the Submit-Apply-Save workflow.

[![filtering styles](/img/uploads/geoserver_2_beta1.png)](/img/uploads/geoserver_2_beta1.png)

Another particularly useful feature added since [alpha2](http://blog.geoserver.org/2009/04/20/see-the-new-ui/) was released is **cascading delete**. This feature allows a user to remove a workspace or a data store and have all the entities contained inside (such as layers) also be removed.  Previously, it was necessary to delete all layers individually before being able to remove a data store.  To prevent unintended deletion, a confirmation page details what will be removed.

As usual a host of other [fixes and improvements](http://jira.codehaus.org/browse/GEOS/fixforversion/15082) (over 100!) have also been incorporated into this release. Please [download](http://geoserver.org/display/GEOS/GeoServer+2.0-beta1), give it a try, and forward your feedback along.  We greatly appreciate reporting issues to the [users mailing list](mailto:geoserver-users@lists.sourceforge.net) and look forward to general feedback on the new user interface.
