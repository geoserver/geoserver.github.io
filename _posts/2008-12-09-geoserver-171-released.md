---
author: Justin Deoliveira
comments: true
date: 2008-12-09 16:55:52+00:00
layout: post
link: http://blog.geoserver.org/2008/12/09/geoserver-171-released/
slug: geoserver-171-released
title: GeoServer 1.7.1 Released
wordpress_id: 158
categories:
- Announcements
- Features
- Tips and Tricks
---

The GeoServer team is happy to announce the release of [GeoServer 1.7.1](http://geoserver.org/display/GEOS/GeoServer+1.7.1)!

The biggest improvement in this release is better **Google Earth support**.   Using revamped KML output (known as the [KML "reflector"](http://geoserver.org/display/GEOSDOC/01-KML+Reflector)) GeoServer can now output [vector super-overlays](http://geoserver.org/display/GEOSDOC/07-KML+Super-Overlays).  Prior to this version, data served by GeoServer when viewed in Google Earth would only update when the the camera stopped.  With super-overlays, however, views are updated dynamically.  Data is also broken up into [regions](http://geoserver.org/display/GEOSDOC/08-KML+Regionation) which are used to sort features into a hierarchy so that more prominent features are visible at higher zoom levels and less prominent features become visible at lower zoom levels. Super-overlays also work on raster datasets, providing lower resolutions versions of imagery (overviews) at higher zoom levels and higher resolutions at lower zoom levels.

All of this is is a huge step for GeoServer, as it is now the first major GIS server to return placemarks, lines, and polygons with the super-overlay mechanism.  This means that serving data through Google Earth is a more seamless experience; your data will look like it is naturally part of Google Earth.  And with super-overlays, you can serve large amounts of data with minimal performance issues.

In addition to super-overlays, GeoServer now has support for adding a [height attribute](http://geoserver.org/display/GEOSDOC/04-KML+Height+and+Time) to features (also known as "extrudes"), which allows Google Earth to [render data in 3-D](http://geoserver.org/display/GEOSDOC/04-Height+Templates). Height information is specified via a template, similar to how one specifies [time attributes](http://geoserver.org/display/GEOSDOC/02-Time+Templates) to create animations.  We have a nice tutorial on how to use the [height feature with super-overlays](http://geoserver.org/display/GEOSDOC/05-Super+Overlays+and+Extrudes+with+Building+Data), to see this in action, but here's a quick screenshot.

[
![](http://geoserver.org/download/attachments/13565962/google_earth2.png)
](http://geoserver.org/download/attachments/13565962/google_earth2.png)

Although the default mode of output using the improved [KML reflector](http://geoserver.org/display/GEOSDOC/01-KML+Reflector) is now the super-overlay mode, the previous default, [refresh](http://geoserver.org/display/GEOSDOC/01-KML+Reflector-modes) mode, is still available. Also available is a [download](http://geoserver.org/display/GEOSDOC/01-KML+Reflector-modes) mode which outputs a self-contained KML file, useful for situations where server access is not necessary or possible.

Special thanks go out to David Winslow for all the great work implementing all the new KML functionality.

This version has more than just improved Google Earth support.  GeoServer now has an official [SQL Server extension](http://downloads.sourceforge.net/geoserver/geoserver-1.7.1-sqlserver-plugin.zip) (described [previously](http://blog.geoserver.org/2008/11/10/146/)). In addition, there is a new and improved [Oracle extension](http://downloads.sourceforge.net/geoserver/geoserver-1.7.1-oracleng-plugin.zip) which provides better performance and security from the previous version.

Further improving the visualization experience is [GeoWebCache](http://geowebcache.org), a WMS tile-caching program.  Previously available as an extension (and still available as a [standalone product](http://geowebcache.org)), GeoWebCache is now built-in to GeoServer and can vastly accelerate map rendering.  We will be talking more about GeoWebCache in a future post.

Finally, this version includes a new [drag and drop installer](http://downloads.sourceforge.net/geoserver/geoserver-1.7.1.dmg) for Mac OS X users.

As always with any GeoServer release a heap of other improvements and bug fixes are included. A total of [98 issues](http://jira.codehaus.org/browse/GEOS/fixforversion/14502) were handled for this release.

We're very excited about this release, and we encourage you to [download](http://geoserver.org/display/GEOS/GeoServer+1.7.1), try it out, and let us know what you think. Comments and feedback are always welcome on the [mailing list](mailto:geoserver-users@lists.sourceforge.net), as the community is always interested to hear how people are using GeoServer. Stay tuned for the 1.7.2 release, slated for release in the next month or so, which will include new breakthroughs in support for [GeoSearch](http://blog.geoserver.org/2008/05/13/geoserver-and-googles-geo-search/).
