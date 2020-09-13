---
author: bmmpxf
comments: true
date: 2009-03-25 14:38:31+00:00
layout: post
link: http://blog.geoserver.org/2009/03/25/coming-soon-complex-features/
slug: coming-soon-complex-features
title: 'Coming Soon: Complex features'
wordpress_id: 193
categories:
- Behind The Scenes
tags:
- complex features schema GSIP
---

Here's a guest post by Ben Caradoc-Davies and Robert Woodcock of the Australian [Commonwealth Scientific and Industrial Research Organisation](http://www.csiro.au).



<blockquote>
As a part of the Auscope Spatial Information Services Stack, GeoServer **complex feature** support is nearing completion.

[Auscope](http://www.auscope.org.au) is using GeoServer to support its vision of developing a collaborative national geoscience spatial data infrastructure (SDI) that improves information exchange across industry and government in the earth sciences. The earth science community is challenged with increasingly complex problems in environmental sustainability, climate change, minerals discovery, and others. In investigating these challenges scientists and policy makers are increasingly combining spatial information from multiple organizations and disciplines.

Scientists need to be certain of the meaning being conveyed and the assertions they can make regarding the data. It isn't sufficient to label a value as "temperature" or "sky".  GeoServer, with OGC standards support, provides a basis for the exchange of geospatial information. With the addition of the **application schema** (or "app-schema", the GeoTools module that implements complex feature support) GeoServer can provide for the expression of community-agreed features and vocabularies, like those of [GeoSciML](https://www.seegrid.csiro.au/twiki/bin/view/CGIModel/GeoSciML), a GML application schema and international standard for earth science information exchange.  This is important for the type of scientific and policy dialogue Auscope's community is seeking.

Auscope is working with Australian government agencies and research organizations to ensure the GeoServer app-schema support is robust enough for full deployment. Auscope is also working with the [One Geology](http://www.onegeology.org) on a "cook book" for geological surveys who wish to deploy GeoServer and use GeoSciML as part of the international exchange of earth science information.

AuScope Ltd is funded under the [National Collaborative Research Infrastructure Strategy](http://ncris.innovation.gov.au) (NCRIS), an Australian Commonwealth Government Programme.
</blockquote>



For those who are on the fence about deploying GeoServer because of complex feature support, your wait will soon be over.  An alpha release of GeoServer with complex feature support in WFS is expected **by the end of April**.  For more information about this ongoing work, please see the [GeoServer Improvement Proposal](http://geoserver.org/display/GEOS/GSIP+31+-+Use+DataAccess+API).
