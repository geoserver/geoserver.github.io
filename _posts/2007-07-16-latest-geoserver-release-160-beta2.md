---
author: Chris Holmes
comments: true
date: 2007-07-16 16:04:04+00:00
layout: post
link: http://blog.geoserver.org/2007/07/16/latest-geoserver-release-160-beta2/
slug: latest-geoserver-release-160-beta2
title: 'Latest GeoServer Release: 1.6.0-beta2'
wordpress_id: 60
categories:
- Announcements
---

The GeoServer Team is pleased to announce the latest 1.6.x release: [1.6.0-beta2](http://docs.codehaus.org/display/GEOS/Geoserver+1.6.0-beta2).  We are hoping that our next release in this series will be a release candidate, so please help us out with testing as we work towards complete stability and reliability.  This release should actually be quite solid, but it's also got some major changes so we want another round of testing to be completely sure.

As for improvements, we've been making strides to allow GeoServer to play more nicely with Java Enterprise Edition containers.  The biggest is that we've swapped out our connection pool code to be more Java EE compliant, enabling the use of JNDI configurations (though we still lack a UI for it), and defaulting to [DBCP](http://jakarta.apache.org/commons/dbcp/).  This is a huge improvement over our old code, as it gives much more control over number of connections and can revalidate lost connections.   It also again points to the strength of the Java open source world, as we've gotten a huge improvement by just leveraging an existing library.

This release also includes better logging options, giving users settings for the logging levels and where the output goes.  Reprojection in WFS 1.1 is also working again, so GeoServer can now give you raw data reprojected on the fly.  Other improvements include integrated demos for Google Maps, Yahoo Maps and Virtual Earth, dateTimes are working again, and there are numerous small bug fixes.  The full log is on [our JIRA](http://jira.codehaus.org/secure/IssueNavigator.jspa?reset=true&pid=10311&fixfor=13547).
