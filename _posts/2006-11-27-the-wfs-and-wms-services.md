---
author: Brent Owens
comments: true
date: 2006-11-27 21:51:55+00:00
layout: post
link: http://blog.geoserver.org/2006/11/27/the-wfs-and-wms-services/
slug: the-wfs-and-wms-services
title: The WFS and WMS Services
wordpress_id: 13
---

### OGC Web Services for accessing Geographic Data


The [Open Geospatial Consortium](http://www.opengeospatial.org/) has defined several Open Web Services for accessing (usually geographic) data. There are two basic service sets - the Web Feature Services (WFS) and the Web Map Services (WMS). The WFS is concerned with direct access to your data - reading, writing, and updating your [features](http://udig.refractions.net/confluence/pages/viewpage.action?pageId=5151).  The WMS is concerned with transforming your data into a map (image).


_Diagram from the uDig wiki, no longer available._


> **(i) What is a Feature?**
>
> A feature is an Object that is an abstraction of a real world phenomenon. This object has a set of properties associated with each having a name, a type, and a value. An example of a feature might be Road with a Name, Location (line geometry), Width, Speed Limit, and Jurisdiction.
>
> Typically these features are stored in a [spatial database](http://udig.refractions.net/confluence/pages/viewpage.action?pageId=5223), shapefile, or other format.


> **✓ OGC Open Web Services**
>
> The OGC Web Services provide access to the features - either directly or as images (maps) - in a standardized way independent of the company who created the server or the actual format the data is stored in.


### What to use a the WFS services for


A WFS allows uniform direct access to the features stored on a server. Use a WFS when they want to perform actions such as:


	
  * query a dataset and retrieve the features

	
  * find the feature definition (feature's property names and types)

	
  * add features to dataset

	
  * delete feature from a dataset

	
  * update feature in a dataset

	
  * lock features to prevent modification


### A WMS allows for uniform rendering access to features stored on a server.  Use a WMS when you want to perform actions such as:


	
  * Producing Maps

	
  * Very simple Querying of data


