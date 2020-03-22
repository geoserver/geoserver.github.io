---
author: bmmpxf
comments: true
date: 2008-03-04 20:22:19+00:00
layout: post
link: http://blog.geoserver.org/2008/03/04/geoserver-161-released/
slug: geoserver-161-released
title: GeoServer 1.6.1 Released!
wordpress_id: 89
categories:
- Announcements
---

The GeoServer team announces the release of [GeoServer version 1.6.1](http://geoserver.org/display/GEOS/GeoServer+1.6.1)!  Here are some of the highlights in this release:

GeoServer now supports FeatureType aliases, which allows for the creating of friendly names for unwieldy FeatureTypes.  Also, support has been added for limiting (per FeatureType) the maximum number of features that can be requested by a client, thus easing server load.  (Thanks to [Landgate](http://www.landgate.wa.gov.au) for funding both of the above!). Cédric Briançon from [Geomatys](http://geomatys.fr) contributed the GetFeatureInfo operation on WMS coverage data, and GeoServer can now output PDFs from raster as well as vector data.  Saul Farber of [MassGIS](http://www.mass.gov/mgis) added support for UpdateSequence, which returns a “revision number” of the capabilities of the service; this gives clients more efficient access to the Capabilities document.  Also, there have been improvements in MySQL integration: The Java connector was updated, performance was improved, and GeoServer is now using the more-efficient Well Known Binary protocol.

In total, this new release contains over 40 patches and improvements since 1.6.0.  (You can view the [changelog](http://jira.codehaus.org/secure/IssueNavigator.jspa?reset=true&&fixfor=14070&pid=10311&sorter/field=issuekey&sorter/order=DESC)  for details.  You can download this latest version from [geoserver.org](http://geoserver.org/display/GEOS/GeoServer+1.6.1).  As usual, we thank everyone who has tested out the software and reported issues.  Please continue to submit bug reports using our [bug tracker](http://jira.codehaus.org/browse/GEOS).
