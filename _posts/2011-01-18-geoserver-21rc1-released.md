---
author: geoserver
comments: true
date: 2011-01-18 16:04:15+00:00
layout: post
link: http://blog.geoserver.org/2011/01/18/geoserver-21rc1-released/
slug: geoserver-21rc1-released
title: GeoServer 2.1-RC1 Released
wordpress_id: 837
categories:
- Announcements
- Features
---

The GeoServer community is happy to announce that the first release candidate of GeoServer 2.1 is now available for [download](http://geoserver.org/display/GEOS/GeoServer+2.1-RC1). The team has been busy working on some great new improvements and features since 2.1-beta3.

First up is **GeoWebCache integration**, allowing clients to enjoy the benefits of tile caching through the regular GeoServer WMS endpoint. This enables GeoWebCache to transparently proxy for the GeoServer WMS without the need for a separate service endpoint. Taking advantage of the recently added **disk-quota** functionality, GeoWebCache now provides the ability to set limits on the amount of disk space used for storing tiles, allowing users to control and limit the size of the tile cache on disk. Big thanks to Gabriel Roldán for the great GeoWebCache improvements.

This release also brings some improvements to **RESTConfig**, which is now shipped with GeoServer by default so users need no longer install it as a separate plugin. Improvements to the API include the file upload operation that now allows for uploading files into an existing data store. This addition allows users to upload a shapefile and have it converted automatically into a PostGIS database, publishing it as a PostGIS layer rather than as a Shapefile layer. Finally, the API also supports recursive DELETE operations, making it more convenient to remove resources that contain other resources like stores or workspaces. Thanks to David Winslow and Justin Deoliveira of [OpenGeo](http://opengeo.org/) for these improvements.

Thanks to some great work from the folks at [GeoSolutions](http://www.geo-solutions.it/)**, raster reprojection performance** has improved significantly by using linear appoximations of transformation functions. This improvement was initially added in 2.1-beta3 but has continued to be improved for 2.1-RC1. Those interested should checkout this [article](http://geo-solutions.blogspot.com/2011/01/developers-corner-improving.html) that links to a white paper with the full technical details.

Last but certainly not least, thanks to Andrea Aime for the addition of a **Web Coverage Service** [request builder](http://jira.codehaus.org/secure/attachment/52920/requestBuilder10-nq8.png), a handy tool for graphically building WCS requests to test a coverage service. As clients for WCS have always been sparse, this tool goes a long way for making the service more usable.

We are happy to report the contribution of yet another translation of the web admin interface—special thanks to Oscar Fonts for submitting a **Catalan translation** and to [Geodata Sistemas](http://www.geodata.es) for funding the work.

Also worthy of thanks this round is Ivan Grcic who has submitted some excellent patches, including [bug fixes](http://jira.codehaus.org/browse/GEOS-4286) for WMS layer functionality. Thanks Ivan!

As always, a number of other bug fixes and improvements have made it into this release. Check out the [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=16982) for all new and noteworthy changes.

[Download](http://geoserver.org/display/GEOS/GeoServer+2.1-RC1) and try 2.1-RC1 now. You can help us reach the final 2.1 release by reporting any bugs in the [issue tracker](http://jira.codehaus.org/browse/GEOS) and sending feedback to the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users).

Thanks for supporting GeoServer!
