---
author: geoserver
comments: true
date: 2012-06-12 15:00:19+00:00
layout: post
link: http://blog.geoserver.org/2012/06/12/geoserver-to-the-rescue-with-cascading-services/
slug: geoserver-to-the-rescue-with-cascading-services
title: GeoServer to the rescue with cascading services
wordpress_id: 1077
categories:
- User perspectives
tags:
- cascaded wms
- GeoServer
- msrmaps
- oklahoma
- stories
- terraserver
- user
- usgs
- wms
---

The [GeoServer Users](https://lists.sourceforge.net/lists/listinfo/geoserver-users) mailing list is often replete with stories about how folks are using GeoServer to solve problems and be successful.  For more casual watchers of GeoServer who are not on this list, you may not get to hear about these success stories.  So, to switch things up on this blog, we thought we'd report on success story from longtime GeoServer community member Roger Bedell.  Here, he talks about using GeoServer as a replacement for [MSRMAPS](http://msrmaps.com/).


<blockquote>Another awe-inspiring moment provided by GeoServer.

Recently, MSRMAPS (Microsoft Research Maps, originally known as **TerraServer**), a WMS server for digital raster graphics (DRGs) and digital orthophoto quarter quadrangles (DOQQs) was shut down. Nobody really cared about the DOQQs, but this was just about the only DRG WMS server out there.

Looking around, I found that the [USGS](http://usgs.gov) has a DRG server:

> 
> <blockquote>[ http://raster.nationalmap.gov/ArcGIS/services/DRG/TNM_Digital_Raster_Graphics/MapServer/WMSServer?request=GetCapabilities&service=WMS]( http://raster.nationalmap.gov/ArcGIS/services/DRG/TNM_Digital_Raster_Graphics/MapServer/WMSServer?request=GetCapabilities&service=WMS)</blockquote>
> 
> 
However it is split into UTM zones and different resolutions. I just wanted 4326 for the entire US, like Terraserver provided.

So, I created a GeoServer [Amazon EC2 Micro](http://aws.amazon.com/free/) instance (which is free for a year) using the basic Amazon Linux AMI (AMI ID: ami-e565ba8c), and installed just [Tomcat](http://tomcat.apache.org) and and [GeoServer 2.2 beta 2](http://geoserver.org/display/GEOS/GeoServer+2.2-beta2):
`
sudo yum update
sudo yum install httpd httpd-devel tomcat7
wget http://sourceforge.net/projects/geoserver/files/GeoServer/2.2-beta2/geoserver-2.2-beta2-war.zip/download
unzip geoserver-2.2-beta2-war.zip
sudo chown tomcat:tomcat geoserver.war
sudo mv geoserver.war /var/lib/tomcat7/webapps/
sudo /sbin/service httpd start
sudo /sbin/service tomcat7 start
`

I then added a [cascaded WMS store](http://docs.geoserver.org/latest/en/user/data/cascaded/wms.html) and used the GetCapabilities URL above. This automatically added and published all of the layers.

Then I put together a [layer group](http://docs.geoserver.org/latest/en/user/webadmin/data/layergroups.html) with all the layers.  The only change I made was to check the "Default Style" box, otherwise I would get a WMS error.

I set the coordinate system for the layer group to EPSG:4326, and it worked.

Thank you GeoServer team!</blockquote>


For those who are interested in using this composite layer, here is the capabilities document to a hosted GeoServer:


<blockquote>[http://ogi.state.ok.us/geoserver/USGSNationalMap/wms?service=WMS&version=1.1.0&request=GetCapabilities](http://ogi.state.ok.us/geoserver/USGSNationalMap/wms?service=WMS&version=1.1.0&request=GetCapabilities)</blockquote>


The layer in question is called **DRGComposite**.  And if you'd like you see a preview of this layer without creating a new store in your GeoServer:


<blockquote>[http://ogi.state.ok.us/geoserver/USGSNationalMap/wms/reflect?layers=DRGComposite&format=openlayers](http://ogi.state.ok.us/geoserver/USGSNationalMap/wms/reflect?layers=DRGComposite&format=openlayers)</blockquote>


Thank you, Roger, for sharing your story!

If you have other GeoServer success stories and would like to share them here, please comment on this post and let the rest of us know!
