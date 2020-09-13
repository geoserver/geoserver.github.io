---
author: Chris Holmes
comments: true
date: 2006-12-21 23:27:24+00:00
layout: post
link: http://blog.geoserver.org/2006/12/21/geoserver-roadmap-updated/
slug: geoserver-roadmap-updated
title: GeoServer Roadmap updated
wordpress_id: 16
categories:
- Developer notes
---

So this may be about as close as I'm going to get to '[Developers notes](http://blog.geoserver.org/?cat=3)' for awhile (though I may let myself work on some [GeoJSON](http://icon.stoa.org/trac/pleiades/wiki/GeoJSON) or [GeoRSS](http://georss.org) output over the holidays), but wanted to let everyone know that I updated the [GeoServer Roadmap](http://docs.codehaus.org/display/GEOS/Roadmap) in an attempt to capture the latest directions of the community.  If I've missed anything please don't hesitate to update it (all our docs are wikis).  The roadmap had fallen out of date - the 'short term' projects were set to complete in september - so I'll try to be more vigilant about updating it more regularly.

But I must say it was quite satisfying doing the update, as the GeoServer community had actually managed to hit most of the things we said we would.  The [demo site](http://sigma.openplans.org) is up, [GeoCollaborator](http://docs.codehaus.org/display/GEOS/GeoCollaborator) stuff has moved from [discussions](http://docs.codehaus.org/display/GEOS/Versioning+WFS) to the beginning of an [implementation](http://docs.codehaus.org/display/GEOS/Versioning+WFS+-+Phase+one+implementation+proposal).  [1.4.0](http://docs.codehaus.org/display/GEOS/GeoServer+1.4.0) is out, and the [WCS branch](/http://docs.codehaus.org/display/GEOSDEV/WCS+Branch) not only got up a release, but is a part of the GeoServer main line as [1.5.0-beta1](http://docs.codehaus.org/display/GEOS/GeoServer+1.5.0+beta1).  We've also had some work on tiling/caching with a [tutorial](http://docs.codehaus.org/display/GEOSDOC/Caching) on running OSCache.  The only thing we didn't get to was an improved SLD editor, but I'm hoping we can do it after our web gui overhaul - which made it's way up to 'medium term', as we've been feeling the pain too long.  If people have suggestions of a good web framework let us know, the ones we're likely going to look at are Wicket, WebWork2, and Google Web Toolkit.

Elsewhere on the horizon we've got WFS 1.1 (which includes GML 3.1.1 simple features) from [OWS-4](http://www.opengeospatial.org/projects/initiatives/ows-4) coming home, and Justin's made some nice improvements on that branch.  And 3d and 4d support in WCS will be in the works as the 2D version works towards the stability of 1.5.0.  Also Social Change Online and Axios are likely going to be doing some more work on bring the new Feature Model home, which should be a huge step forward.  On the non-technical side of things we're also going to be working on changing the license of the 'core' of GeoServer (configuration of data and access to GeoTools) to LGPL, which should enable others to build even more interesting services on top.

So stay tuned, there's lots of fun coming from the edges to the mainstream of GeoServer, and there are some other fun things that may be in the works.  It's going to be an exciting year for sure.

Happy Holidays from all of us working on GeoServer!
