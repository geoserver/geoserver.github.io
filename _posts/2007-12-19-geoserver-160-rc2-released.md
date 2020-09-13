---
author: Justin Deoliveira
comments: true
date: 2007-12-19 15:02:24+00:00
layout: post
link: http://blog.geoserver.org/2007/12/19/geoserver-160-rc2-released/
slug: geoserver-160-rc2-released
title: GeoServer 1.6.0-RC2 Released!
wordpress_id: 81
categories:
- Announcements
- Features
---

We are happy to announce the second release candidate of GeoServer 1.6.0. You can download the release from [SourceForge](http://sourceforge.net/project/showfiles.php?group_id=25086&package_id=38410&release_id=562389).

As usual this release candidate brings a heap of bug fixes, with a few minor improvements. Output formats such as [KML](http://docs.codehaus.org/display/GEOSDOC/Google+Earth), SVG, and [GeoRSS](http://docs.codehaus.org/display/GEOSDOC/GeoRSS) have been tightened up fixing a few minor bugs. Backend issues such as PostGIS bounds reprojection and Oracle permissions have also been addressed.  For a complete list check out the [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?version=13874&styleName=Html&projectId=10311&Create=Create).

There are also a few notable improvements to mention. The first being a "strict" request parameter which allows clients to turn on [WFS XML validation](http://docs.codehaus.org/display/GEOSDOC/WFS+vendor+parameters#WFSvendorparameters-validation) on a request by request basis. This provides a nice debugging tool for clients to use for validating WFS requests. Also worth mention is the ongoing work and improvements to the experimental [Versioning WFS protocol](http://docs.codehaus.org/display/GEOS/Versioning+WFS).

With any luck this will be the last release candidate before the official 1.6.0 release. You can help us out by downloading it and trying out. Please report any issues encountered in the [bug tracker](http://jira.codehaus.org/browse/GEOS).
