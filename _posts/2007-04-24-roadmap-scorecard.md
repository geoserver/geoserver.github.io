---
author: Chris Holmes
comments: true
date: 2007-04-24 23:21:31+00:00
layout: post
link: http://blog.geoserver.org/2007/04/24/roadmap-scorecard/
slug: roadmap-scorecard
title: Roadmap scorecard
wordpress_id: 35
categories:
- Developer notes
---

So I'm about to update the [GeoServer Roadmap](http://docs.codehaus.org/display/GEOS/Roadmap), since the short term projects currently listed should be done.  And I thought before doing that I'd see how we did against the previous goals.  Of course we don't make any promises about delivery of these, unless of course someone funds a core developer to meet a hard deadline.  But it's worthwhile to see how we measured up, to get a progress report on where everything is at.


### GeoServer 1.5.x


[1.5.0 Released](http://blog.geoserver.org/2007/04/18/geoserver-150-released/)!  Woo hoo!  This took a good bit longer than expected, but I think everyone is quite satisfied.  It's our most stable and scalable release yet, with lots of good bug fixes and improvements for users, in addition to the incredible new raster support.  We're planning for more 1.5.x releases, back porting the fixes and smaller improvements from 1.6.x, including using openlayers for demos and some [very](http://docs.codehaus.org/display/GEOSDOC/KML+Placemark+Templates) [nice](http://jira.codehaus.org/browse/GEOS-1040) [KML](http://jira.codehaus.org/browse/GEOS-1034) [improvements](http://jira.codehaus.org/browse/GEOS-993), and a [contributed Chinese translation](http://jira.codehaus.org/browse/GEOS-1056) of the web admin.


### Further Tiling Infrastructure


So unfortunately [our research](http://docs.codehaus.org/display/GEOS/Rendering+and+tiling+issues+research) on this didn't yield the results we were hoping for, as we wanted a rendering option that worked better with tiling.  But it turns out that doing meta-tiles (rendering an image much bigger than the tiles then splitting them up).  There is great news on this front, though, which is that Google's [Summer of Code](http://code.google.com/soc/) has funded Chris Whitney to make a [JTileCache](http://code.google.com/soc/osgeo/appinfo.html?csaid=FED722EC29A37BC5), a pure java port of [TileCache](http://labs.metacarta.com/wms-c), backed in his initial implementation by [JCS](http://jakarta.apache.org/jcs/index.html), which will let us make distributed caches very easily.  Since it's java we'll be able to ship with GeoServer, and it will function as a stand-alone.


### Speed Improvements to WMS Renderer


Most of the speed improvements of the past few months have actually been made on the WFS side of the fence.  Chris Tweedie has [some information](http://chris.narx.net/2007/04/20/geoserver-testing/) on his blog, the main work done is not so much on speed improvements, but on setting up a framework for [stress tests](http://docs.codehaus.org/display/GEOS/Stress+Testing) so we can measure things much more easily.  But Andrea also found some great improvements that [doubled](http://www.nabble.com/And-as-if-by-magic,-Geoserver-doubled-its-WFS-serving-speed-:-)-t3541274.html) the WFS output in some cases.


### GeoCollaborator (Geowiki) experimental implementation


The server side implementation is close to done, we've got a [working](http://docs.codehaus.org/display/GEOS/Trying+out+the+early+WFS-V+prototype) [interface](http://docs.codehaus.org/display/GEOS/Versioning+WFS+-+Protocol+considerations), which we encourage to try out and write clients against.  We've got it working against existing WFS-T implementations, but we're working to collaborate on a ['version-aware' client](http://docs.codehaus.org/display/GEOS/Versioning+WFS+-+Client+side+thoughts).  The one remaining piece we need to do on the server side is a bit orthogonal, but necessary, and that's a security framework.  Andrea is gathering requirements and evaluating right now, if you have any feedback throw it on the [wiki](http://docs.codehaus.org/display/GEOSDEV/Geoserver+authentication+and+authorization+subsystem).  Our needs are minor at the moment, but we'd like to pick something that can expand for future uses.


### LGPL for the core


I'm still working on this.  We've decided to just push on getting contributor agreements first that will give us the flexibility to re-license by having all the legal pieces in place, and then we'll figure out LGPL for the core at a separate time.  But I hope to have progress on this relatively soon, so that potential users can license GeoServer under non-GPL licenses.


### WFS 1.1 / architecture improvements


Justin finished this up.  It is on trunk and will be one of the main pieces of 1.6.0.  It's currently available in an alpha release, and hopefully a beta release pretty soon.  Other developers have had good feedback on the new dispatching architecture.


### New [Geotools](http://docs.codehaus.org/display/GEOT/Home) Feature Model


Gabriel has made some great progress on this.  Hopefully he'll give us all a full update soon.  We also got some great news on this front, as [TOPP](http://topp.openplans.org) has been [awarded a CAP grant](http://www.fgdc.gov/grants/2007CAP/Category2/07HQAG-NY/) to work on [uDig](http://udig.refractions.net), making it able to accept WFS 1.1 with US Framework Schemas, which will entail getting on to trunk the GeoTools feature model that GeoServer fully depends upon.

So overall I feel we did pretty well.Â  In the next week I'll update the roadmap and talk a bit more about the exciting stuff coming down the pipeline.Â  And hopefully we'll get the developers talking more about what they've been working on, since there's even more than what I've managed to mention here.
