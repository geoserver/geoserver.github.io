---
author: Chris Holmes
comments: true
date: 2007-07-09 21:33:19+00:00
layout: post
link: http://blog.geoserver.org/2007/07/09/geojson-output-for-geoserver/
slug: geojson-output-for-geoserver
title: GeoJSON output for GeoServer
wordpress_id: 57
categories:
- Announcements
- Developer notes
---

I've just uploaded a new [GeoJSON](http://geojson.org) plug-in for GeoServer, enabling [JSON](http://json.org) output for any WFS request.  The plug-in is definitely compatible with all versions of GeoServer 1.5.x, and will likely work with 1.4.x as well.  This was a breeze to write, which is a testament to the nice design of GeoServer and to the strength of the Java open source world.  I made use of [json-lib](http://json-lib.sourceforge.net), and extended the JSONBuilder to handle geometries.  Then hooked that up as an output format plugin for WFS, and we can now plug it in to existing GeoServer installations.  Please give us feedback on how it's working, and if we get a positive response we'll likely include it in the default release.

The plug-in can be downloaded from [sourceforge](http://sourceforge.net/project/showfiles.php?group_id=25086&package_id=129885&release_id=522015), and there's a bit of a [write-up](http://docs.codehaus.org/display/GEOSDOC/GeoJSON+Output+Format) in the GeoServer documentation.  For more information on GeoJSON, see [http://geojson.org](http://geojson.org).  The spec is not yet finalized as 1.0, but is a first release candidate.  So hopefully it will hold up, but if not we'll definitely stay up to date with the latest versions.
