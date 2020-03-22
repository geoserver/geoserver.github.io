---
author: geoserver
comments: true
date: 2012-07-09 14:00:06+00:00
layout: post
link: http://blog.geoserver.org/2012/07/09/geoserver-has-moved-to-github/
slug: geoserver-has-moved-to-github
title: GeoServer has moved to GitHub
wordpress_id: 1112
categories:
- Announcements
---

GeoServer and [GeoTools](http://geotools.org/) have moved to [Git](http://git-scm.com/) and [GitHub](https://github.com/) for version control and source hosting.  We hope that this change will make work easier for existing GeoServer developers and encourage contributions from new ones.

Git is a relatively new version management software.  Compared with the Subversion software that GeoServer previously used, it offers several features including offline commits and history browsing, cryptographic checksums for commits, and several advanced options for automatic merging.  In addition, Git's distributed nature means that any potential contributor can "fork" the GeoServer code and make changes instead of waiting on a GeoServer committer to grant access.  (Such changes must still be approved by the GeoServer development team in order to be included in an official GeoServer release.)

Along with the shift to Git, we are moving GeoServer's source hosting to GitHub.  GitHub provides free hosting for open-source projects, including [nice tracking of forks](https://github.com/geoserver/geoserver/network), a syntax-highlighting [source browser](https://github.com/geoserver/geoserver/blob/master/src/main/src/main/java/org/geoserver/config/GeoServer.java), and [interesting reports](https://github.com/geoserver/geoserver/graphs) on who is contributing to the project. GeoServer's documentation, bug tracking, mailing lists, and IRC chat, however, are unaffected by the move.

The GeoServer developer manual has been updated with [instructions on working with Git](http://docs.geoserver.org/latest/en/developer/source.html).  If you are a Git guru with some tips to add to the guide, a savvy user with addenda for the manual, or a Java hacker with bugs to fix, please [fork us on GitHub](https://github.com/geoserver/geoserver)!
