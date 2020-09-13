---
author: geoserver
comments: true
date: 2009-07-03 06:08:20+00:00
layout: post
link: http://blog.geoserver.org/2009/07/03/geoserver-app-schema-meeting-in-perth-western-australia/
slug: geoserver-app-schema-meeting-in-perth-western-australia
title: GeoServer app-schema meeting in Perth, Western Australia
wordpress_id: 226
categories:
- Behind The Scenes
---

Last week AuScope hosted a GeoServer app-schema meeting in Perth,  Western Australia, to bring together developers, information modellers,  and users:

[https://twiki.auscope.org/twiki/bin/view/Grid/AuScopeSissGeoserverMeeting2009](https://twiki.auscope.org/twiki/bin/view/Grid/AuScopeSissGeoserverMeeting2009)

The meeting was attended by Jody Garnett, GeoServer developers Justin  Deoliveira and Gabriel Roldán from OpenGeo, AuScope Spatial Information  Services Stack developers, GeoSciML gurus, and AuScope participants  including GeoScience Victoria, Geoscience Australia, and Landgate.  Discussions included the history of GeoServer app-schema, background on  AuScope, user perspectives, and future development priorities.

Future development options that received support included:



	
  * Graphical configuration for app-schema (Wicket UI)

	
  * Support for polymorphism in encoded app-schema XML

	
  * 3D geometry support

	
  * GML 3.2

	
  * WFS 2.0


and more. See the minutes for details:

[https://twiki.auscope.org/twiki/bin/view/Grid/AppSchemaMeetingMinutes](https://twiki.auscope.org/twiki/bin/view/Grid/AppSchemaMeetingMinutes)

The developers stayed on for a code sprint and:



	
  * Implemented vocabulary operations in CQL

	
  * Got GeoServer app-schema working with an ArcSDE backend

	
  * Got GeoServer WMS working with a simple feature WFS backend

	
  * Demonstrated encoding failure of ISO 19107 geometries (3D support)

	
  * Debated polymorphism implementation approaches

	
  * Wrapped Justin in org.geotools.xml.Encoder

	
    * [http://svn.osgeo.org/geotools/trunk/modules/extension/xsd/xsd-core/src/main/java/org/geotools/xml/Encoder.java](http://svn.osgeo.org/geotools/trunk/modules/extension/xsd/xsd-core/src/main/java/org/geotools/xml/Encoder.java)

	
    * To be fair, Justin is only the most recent maintainer

	
    * The source is 3.5 metres long when printed in 6 point DejaVu Sans Mono

	
    * One method alone is 1.2 metres long





AuScope thanks all the participants, especially Jody who helped organise  the meeting, and the international visitors Justin and Gabriel who  travelled from North and South America respectively. We hope you enjoyed  it as much as we did.
