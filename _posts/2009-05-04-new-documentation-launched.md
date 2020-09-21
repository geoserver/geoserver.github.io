---
author: bmmpxf
comments: true
date: 2009-05-04 14:45:12+00:00
layout: post
link: http://blog.geoserver.org/2009/05/04/new-documentation-launched/
slug: new-documentation-launched
title: New documentation launched
wordpress_id: 212
categories:
- Announcements
tags:
- docs
- Documentation
- pdf
- Sphinx
- svn
---

I'm excited to tell you about some changes to the GeoServer documentation.  We are transitioning away from our wiki in favor of a new system.  After [much discussion](http://geoserver.org/display/GEOS/GSIP+25+-+New+Documentation+Framework), we are now using the [**Sphinx Documentation Generator**](http://sphinx.pocoo.org/).

Sphinx has many advantages over a wiki.  The biggest advantage is that the content of the documentation is written in **plain text** (using a simple markup language called [reStructuredText](http://docutils.sourceforge.net/rst.html)) and then "compiled" to become the finished product.  With documentation now essentially just another part of the source code, it can be brought under version control.  This means that we can, for the first time, have **version-specific documentation**, as well as the ability to allow for simultaneous editing, conflict management, and all of the other tools associated with version control.

While wikis have many advantages, a clear hierarchy is generally not one of them.  (For example, one doesn't read Wikipedia "from the beginning.")  And while search remains a feature of our documentation, Sphinx is geared towards the creation of text that can be constructed and read like a manual.  Along this line, we can now create documentation in **PDF**, a feature that has been asked about for years.

We have [soft launched](http://docs.geoserver.org) the new documentation with the release of [GeoServer 1.7.4](http://geoserver.org/display/GEOS/GeoServer+1.7.4).  The [old wiki](http://geoserver.org/display/GEOSDOC/Documentation) is still live, and will remain so.  But there is still much to be done, and you can help.  The documentation is still very much a work in progress, and not all of the content from the wiki has been migrated.  We've developed a [guide to documentation](http://docs.geoserver.org/1.7.x/docguide/index.html) that describes the ways that you can contribute.  The most helpful way is to create content for empty or unfinished pages, and either submit a [bug report](http://jira.codehaus.org/browse/GEOS) with the content attached or commit the changes on your own.  (If you are interested in getting commit rights to our documentation, please send an email to the [GeoServer developers mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-devel).)  If you are aware of a page in the wiki that should be migrated to the new site, please let us know as well.

For GeoServer 1.7.4, the [documentation download](http://downloads.sourceforge.net/geoserver/geoserver-1.7.4-doc.zip) contains both HTML and PDF output.  I encourage everyone to download, read, and make suggestions.  For our part, we will continue to work to make GeoServer easy to learn, use, and understand.
