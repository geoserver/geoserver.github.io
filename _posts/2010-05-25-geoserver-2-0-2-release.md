---
author: geoserver
comments: true
date: 2010-05-25 16:00:06+00:00
layout: post
link: http://blog.geoserver.org/2010/05/25/geoserver-2-0-2-release/
slug: geoserver-2-0-2-release
title: GeoServer 2.0.2 release
wordpress_id: 687
categories:
- Announcements
tags:
- Features
- GeoServer
- release
---

To meet the growing demand for a geospatial server that meets the open standards set by the Open Geospatial Consortium, the GeoServer community has worked hard to release the new [GeoServer 2.0.2](http://geoserver.org/display/GEOS/GeoServer+2.0.2).  This release includes [almost 100 bugfixes and new features](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=16040).

As [previously mentioned](http://blog.geoserver.org/2010/05/17/oracle-georaster-custom-jdbc-access), GeoServer now provides support for Oracle Georaster, custom database layouts for image data and [polymorphism](http://blog.geoserver.org/2010/05/25/polymorphism-in-application-schema/).

Have you ever wondered what geographical area an EPSG code covers? A new feature has been added to showcase the different projections visually, by showing a map of the projection's area of validity in the same CRS.  Here are three examples of this: [EPSG:2964](http://demo.opengeo.org/geoserver/web/?wicket:bookmarkablePage=:org.geoserver.web.demo.SRSDescriptionPage&code=EPSG:2964), [EPSG:3032](http://demo.opengeo.org/geoserver/web/?wicket:bookmarkablePage=:org.geoserver.web.demo.SRSDescriptionPage&code=EPSG:3032), [EPSG:22184](http://demo.opengeo.org/geoserver/web/?wicket:bookmarkablePage=:org.geoserver.web.demo.SRSDescriptionPage&code=EPSG:22184).

To add to this, we have also added a default style preview in the layer publishing configuration.

The rendering subsystem has been improved to include [parameter substitution](http://docs.geoserver.org/stable/en/user/styling/sld-extensions/substitution.html), meaning you can pass parameters down from a GetMap request into your SLD for dynamic styling purposes.

The ability to do geometry transformations, included in GeoServer 2.0.1 without much fanfare, now has been [completely documented](http://docs.geoserver.org/stable/en/user/styling/sld-extensions/geometry-transformations.html).

Building image pyramids just got easier: gone are the times where you had to manually build each level mosaic and configure the main property file by hand.  The current pyramid extension can do this for you provided it is given a suitably configured directory set. See the [pyramid tutorial](http://docs.geoserver.org/stable/en/user/tutorials/imagepyramid/imagepyramid.html) for more details.

Finally, this release of GeoServer implements the GetStyles optional WMS method allowing a user to retrieve the definition of all styles attached to a specific WMS layer, see the following link for an example:
[http://demo.opengeo.org/geoserver/wms?request=GetStyles&layers=topp:states&service=wms&version=1.1.0](http://demo.opengeo.org/geoserver/wms?request=GetStyles&layers=topp:states&service=wms&version=1.1.0)

Thanks to everyone who have worked hard over the past few months adding features and fixing bugs, in order to make this release happen.  As usual, we encourage you to [download](http://geoserver.org/display/GEOS/GeoServer 2.0.2), try it out, and provide feedback on the [users mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users).
