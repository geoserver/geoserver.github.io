---
author: geoserver
comments: true
date: 2009-11-18 19:33:46+00:00
layout: post
link: http://blog.geoserver.org/2009/11/18/proposal-for-improving-imagepyramid-support-and-other-small-developments/
slug: proposal-for-improving-imagepyramid-support-and-other-small-developments
title: Proposal for improving ImagePyramid support (and other small developments)
wordpress_id: 378
categories:
- Behind The Scenes
- Polls
tags:
- FOSSG
- funding
- GeoServer
- GeoSolutions
---

Ciao a tutti,

Supporting a project such as GeoServer requires a great investment of time and resources.  [Organizations](http://geoserver.org/display/GEOS/Commercial+Support) that support it are faced with the problem of finding funding. As founder of my own [company](http://www.geo-solutions.it/), I often find myself in the position to seek funding for supporting GeoServer and I obviously tend to prefer large contracts to small ones.  This seems perfectly reasonable, however I do recognize that in the long run this approach may cause some missed opportunities.  Large funding usually focuses on large developments, but they leave aside common glitches and bugs, i.e. isolated features that are not working properly or could be improved relatively easily.  To counter this, supporting organizations must invest surplus money and resources from other contracts into tackling these problems, since it is difficult or inefficient to chase money to address each small issue separately.

As a specific example, I have lately seen people struggling to get the [ImagePyramid](http://docs.geoserver.org/2.0.x/en/user/data/imagepyramid.html) extension working, and I know it would be relatively easy to improve things (in that it would not need a lot of funding) but none of our current clients needs this functionality, so the work never gets done.

With this in mind, I have come up with the following idea: once someone, be it a user or a support organization, recognizes an issue/missing feature that no one else wants or has funding to fix, we should try to describe the problem/feature somewhere (such as on this blog), provide a Point of Contact (POC) for the work and then ask the community for an Expression of Interest (EOI) to check whether there is enough momentum/desire to fix/implement. Perhaps the POC should write the proposal having already scoped out the work or maybe the scope should wait until we know that there is enough interest.  Another topic where I would see some interest is in whether the process should be completely transparent or not regarding who gives the funding as well as who spends the funding gathered.  I would be interested in feedback on all of these suggestions.

To test his idea, I would like to invite anyone who might be interested in providing a bit of funding to improve the support for the ImagePyramid extension in GeoServer to express your interest to me. Specifically, I am talking about automagic [import from GDAL retile](http://jira.codehaus.org/browse/GEOT-2712), improved stability and performance, and/or automagic pyramiding as a GeoServer/GeoTools utility.

If you are interested you can drop me an email at simone.giannecchiniATgeo-solutions.it.

Ciao, Simone.
