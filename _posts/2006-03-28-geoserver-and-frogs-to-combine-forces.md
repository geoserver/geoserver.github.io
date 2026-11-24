---
author: Chris Holmes
date: 2006-03-28
layout: post
link: http://docs.codehaus.org/display/GEOS/2006/03/28/GeoServer+and+FROGS+to+combine+forces
wayback: https://web.archive.org/web/20061025232311/http://docs.codehaus.org:80/display/GEOS/2006/03/28/
title: "GeoServer and FROGS to combine forces"
categories:
- Announcements
---

Recently we learned of [FROGS](http://frogs.tigris.org), and the [WPSInt](http://wpsint.tigris.org) plug-in. They have built a solid geospatial services framework and a nice [WPS](http://www.opengeospatial.org/specs/?page=requests&request=rfpc28). What they lack is a solid open source community. As GeoServer is looking in a similar direction, for what we are calling [GeoServer 2.0](https://web.archive.org/web/20060328/http://docs.codehaus.org/display/GEOS/GeoServer+2.0+Technology), we've decided to combine forces.

The plan is that we can collaborate on a base framework that supports pluggable services for all our current needs and designed with future ideas in mind. We will be able to work together on the base level and have more time to create new services and improve existing ones instead of replicating work on all the more mundane tasks like supporting different data formats, J2EE integration, data configuration, and eventually user management and security,. Together we hope to become the framework of choice for web based geospatial services. This will likely eventually spin out as its own project, with 'GeoServer', 'WPSInt', and others being 'distributions' of plug-ins on top of the same base framework. We hope to support a diverse ecosystem of communities around web based geospatial projects, just as Eclipse does in general and uDig is starting to do with the GIS desktop.

There are no immediate plans to perform this work, but our developers are starting to get acquainted with one another's code, and we will point newcomers at one another's respective projects. The hope is to find some funding to be able to dig in to the work of combining the projects relatively soon, or to at least build it in to another funding opportunity. But at the very least we will orient the directions toward one another, and if it can't happen immediately we can work there over time. We are all excited about the possibilities.
