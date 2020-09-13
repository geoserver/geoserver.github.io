---
author: Chris Holmes
comments: true
date: 2007-07-31 01:40:53+00:00
layout: post
link: http://blog.geoserver.org/2007/07/30/geoserver-certified-compliant-for-wcs-10-and-will-serve-as-wcs-11-reference-implementation/
slug: geoserver-certified-compliant-for-wcs-10-and-will-serve-as-wcs-11-reference-implementation
title: GeoServer Certified Compliant for WCS 1.0 and will serve as WCS 1.1 Reference
  Implementation
wordpress_id: 63
categories:
- Announcements
---

The GeoServer Project is pleased to announce that we have been certified compliant by the [Open Geospatial Consortium](http://opengeospatial.org) (OGC) for the Web Coverage Service 1.0 specification.  The majority of this great work was contributed by [GeoSolutions](http://geo-solutions.it), and we are pleased that the quality is now completely certified by the OGC, as it passes all [CITE](http://cite.opengeospatial.org/) tests.  This makes GeoServer the most compliant open source server, with certified implementations of WFS 1.0, WFS 1.1, WMS 1.1.1, and now WCS 1.1.  And not only are we compliant, but we remain 'standard by default', with no additional configuration needed to get fully compliant OGC output, for all the major specifications.

In addition to compliance, GeoServer also serves as the reference implementation of the WFS 1.0 and 1.1 specifications.  This means that it is the open source implementation looked to as the main example for how the interface should respond.  The Open Planning Project (TOPP), is also participating in OGC's [OWS-5](http://www.opengeospatial.org/standards/requests/40) testbed, and will improve GeoServer for XLink WFS 1.1, as well as WCS 1.1 with the help of GeoSolutions.  We are especially excited about serving as WCS 1.1 reference implementation, to continue our focus as the best open source implementation to get at raw data.  We are looking to expand the capabilities of WCS to handle the full potential of the specification, allowing users to work with multi-dimensional data such as NetCDF and HDF, requesting specific bands and dimensions through the web.

We are also doing work on [KML](http://code.google.com/apis/kml/documentation/) for the OWS-5 testbed, doing a Feature Portrayal Service capable of transforming a remote WFS and an SLD document to output KML.  TOPP also will be improving OpenLayers to better handle KML, the current version and experimentation with future versions.  The process will also start to flesh out what the next version of KML might look like, but I'll blog about such things in its own post.  We had a face to face meeting this morning, which continues tomorrow, where we made a decent start.
