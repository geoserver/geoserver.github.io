---
author: geoserver
comments: true
date: 2009-08-27 13:02:14+00:00
excerpt: 'At GeoSolutions we have decided to tackle scalability and robustness problems
  by implementing a new GeoServer internal catalog that leverages on Hibernate as
  its persistence engine and that would also not bring the whole configuration into
  memory. Our goal is to be able to support at least Postgis and Oracle as the target
  database, but as you know, many more are supported by Hibernate (spatialite wi  ontheradar
  as well).

  The range of features that this work would open up is pretty wide, just think about
  using Hibernate distributed caching, simplified GeoServer replication, etc., etc.'
layout: post
link: http://blog.geoserver.org/2009/08/27/hibernate-and-geoserver-seeking-for-scalability-and-robustness/
slug: hibernate-and-geoserver-seeking-for-scalability-and-robustness
title: 'Hibernate and GeoServer: seeking for scalability and robustness'
wordpress_id: 262
categories:
- Announcements
tags:
- Enterprise
- GeoServer
- GeoSolutions
- Hibernate
- J2EE
- JEE
---

I thought it would have been worth spending a few minutes to let people know about this development that we are performing at [GeoSolutions](http://www.geo-solutions.it).
Being not only GeoServer developers but also GeoServer hungry users, we have been a bit unpleased in the past some the scalability problems that it was showing due to the fact that:



	
  1. **GeoServer was keeping all its configuration into memory**

	
  2. **GeoServer was making use XML files to handle its internal configuration**


Now a lot of work has been lately for the upcoming 2.0 version of GeoServer, to cope with point 2 above, however point 2 has not been touched yet.
If you use GeoServer the way we use it, with thousand of layers and with 10 to 100 new layers added daily (usually remote sensing data), you might agree with us that we need to:

	
  1. **Not load and keep the entire configuration in memory**

	
  2. **Use a database to store the configuration**


In a few words, we need to improve scalability and robustness while tring to not jeopardize performance, we need to be **enterprise-ready**.

At GeoSolutions we have decided to tackle this problems by implementing a new GeoServer internal catalog that leverages on Hibernate as its persistence engine and that would also not bring the whole configuration into memory. Our goal is to be able to support at least Postgis and Oracle as the target database, but as you know, many more are supported by Hibernate (spatialite wi  ontheradar as well).
The range of features that this work would open up is pretty wide, just think about using Hibernate distributed caching, simplified GeoServer replication, etc., etc.

The work is in progress, we have started to describe the details on the GeoServer [wiki ](http://geoserver.org/display/GEOS/Hibernate+based+catalog).
If you are interesting in supporting somehow (funding or human resources) this effort, please, drop me a few lines at simone.giannecchiniATgeo-solutions.it.
