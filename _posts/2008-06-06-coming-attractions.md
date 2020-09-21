---
author: bmmpxf
comments: false
date: 2008-06-06 22:05:06+00:00
layout: post
link: http://blog.geoserver.org/2008/06/06/coming-attractions/
slug: coming-attractions
title: Coming Attractions
wordpress_id: 112
categories:
- Behind The Scenes
---

While lots of talk here has been about software releases and work that's already been completed, I thought that it might be nice to mention some of the work that's in progress.  After all, the GeoServer community is just that, a community, not a closed-door office, and while congratulations are often in order, the people have a right to know what's going on as it happens. With that in mind, I put on my press credentials, got out my tape recorder and microphone, and have been interviewing some of the GeoServer developers to see what they've been up to recently.




I first talked with David Winslow, who has been working on what is known as [KML regionating](http://geoserver.org/display/GEOS/GSIP+20+-+Automated+Regionating+in+KML+MapProducer) (via a grant from Google).  When working with large amounts of data, not only can it take a long time to plot all those points/lines, but it is not always necessary or even useful to display all of those them (say, when fully zoomed out).  Filtering data by zoom levels is now accomplished by the use of SLDs (style layer descriptors), a handy but abstruse XML document that can easily become unmanageable. There exists a need for a tool to simplify this, and that's where regionating comes in.  Regionating, despite the possibly questionable name, allows the automatic splitting of features via zoom level.  Features with (say) high values would be displayed at higher zoom levels, while features with lower values wouldn't show up until zoomed in.  Regionating is expected to be able to automatically filter by data type or size of feature (say, large polygons versus smaller ones).  As someone who has generated SLDs that have run to thousands of lines (most of it semi-duplications for each zoom level), this will be a help indeed.  Note that for the time being this work is for KML output only, so it will benefit users of products like Google Maps and Google Earth.




Through the wonders of Skype, I then phoned in on Andrea Aime in Italy who discussed with me plans for [per-layer security](http://geoserver.org/display/GEOS/GSIP+19+-+Per+layer+security).  Currently, [security in GeoServer](http://geoserver.org/display/GEOSDOC/2.5+Security+subsystem) is very rudimentary.  Per-user properties exist, as does a sensible user/role/service relationship, although passwords for the moment are stored in plain text.  However, as one can only lock down via user or service, if a user has access to (say) WMS, the user has access to all data served using WMS.  This isn't always optimal.  Per-layer security will add more granularity to the security subsystem by allowing or disallowing based on namespace or layer, and even specifying read/write access as based on predefined roles.  This system, when implemented, will be backwards compatible with previous versions; that is, security will be open by default, so users who upgrade won't find all of their layers suddenly inaccessible!  The conventions proposed, such as giving priority to more specific rules over generic rules, seems well-thought out, and will be a nice step forward.  The plan as it stands now is to implement this as part of version 1.7.0, but this could easily change.




There has also been lots of talk about the upcoming code sprint in Bolsena, Italy, where, among much else, work will commence on a new user interface for the admin console.  The new UI is an issue close to my heart, being more of a user than a developer, and I'm very much looking forward to their advances.  I've also been starting to hear rumors about a version number that begins with **2**, but my press credentials will only get me so far.




I should remind everyone that these features are not yet released, stable, or in some cases even coded.  And issues may come up that prevent some of these new improvements from ever seeing the light of day.  GeoServer, though a robust product, is still a work in progress, one that is helped enormously by contributors.  I encourage anyone who is interested in seeing these features (or any others) come to life to [get involved](http://geoserver.org/display/GEOSDOC/0.2+How+to+Help), [join the mailing lists](http://geoserver.org/display/GEOSDOC/1+Mailing+lists), [meet us in IRC](http://geoserver.org/display/GEOSDOC/3+IRC), [edit the documentation wiki](http://geoserver.org/display/GEOSDOC/Guide+to+Documenting+GeoServer), or [submit a patch](http://geoserver.org/display/GEOSDOC/2+Issue+Tracker).  The more people involved, the better GeoServer will be.  As for me, I'll just continue to try and get my copy in before the deadline.
