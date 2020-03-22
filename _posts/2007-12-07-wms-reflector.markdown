---
author: sbenthall
comments: true
date: 2007-12-07 22:00:37+00:00
layout: post
link: http://blog.geoserver.org/2007/12/07/wms-reflector/
slug: wms-reflector
title: WMS Reflector
wordpress_id: 80
categories:
- Features
---

Check out the two Geoserver-provided images below:
<table cellpadding="1" cellspacing="1" align="center" border="1" >
<tr >

<td align="center" >**Exhibit A**
</td>
</tr>
<tr >

<td align="center" >![](http://geo.openplans.org:8080/geoserver/wms?service=WMS&request=GetMap&version=1.1.1&format=image/png&width=256&height=108&srs=EPSG:4326&layers=topp:states&styles=population&bbox=-138.4239531951185,19.168145657378737,-53.27731780488149,55.15955634262126)
</td>
</tr>
<tr >

<td align="center" >**Exhibit B**
</td>
</tr>
<tr >

<td align="center" >![](http://geo.openplans.org:8080/geoserver/wms/reflect?layers=topp:states&width=256)
</td>
</tr>
</table>
­
They may look very similar, but they have two important differences. First, the scaling of the second map is better for conveying the data.  The second and more important difference you won't be able to see unless you view this page's source.  The markup that produced Exhibit A involved the burdensome URLs you may be used to:

`<img src="http://geo.openplans.org:8080/geoserver/wms?service=WMS &request=GetMap &version=1.1.1 &format=image/png &width=256 &height=108 &srs=EPSG:4326 &layers=topp:states &styles=population &bbox=-138.4239531951185,19.168145657378737,-53.27731780488149,55.15955634262126" />`

Exhibit B, on the other hand, uses a far more concise URL for the image source:

`<img src="http://geo.openplans.org:8080/geoserver/wms/reflect? layers=topp:states&width=256" />`

How is this possible?  Exhibit B uses the new **WMS Reflector**, written by Justin DeOliveira and augmented by Arne Krepp for 1.6.0 for RC1.  The URL asks the reflector (`wms/reflect`) to display the feature "topp:states" (`layers=topp:states`) and that the width should be 256 pixels (`width=256`).  The rest of the parameters are filled in either by sensible but overridable defaults--such as `format=image/png`--or with values calculated on the fly. The bounding box, for example, was inferred from the bounds of the content instead of being explicitly defined.

­


### Less Pain­­


The WMS Reflector is designed to make it easier to play around with Geoserver without having to waste time tweaking cumbersome URLs.  Before, writing a WMS request by hand was almost impossible, since you had to manually make sure that the ratio between the width and height parameters was the same as the ratio for the bounding box.  You also had to know what a spatial reference system is, what version of WMS you wanted to use, and so on.

None of this should be weighing on the user who just wants to get Geoserver to show them a map.  The WMS Reflector frees them from this kind of micromanagement.  As seen in Exhibit B above, all you need to do is supply either a heig­ht or a width attribute and the rest--the bounding box, the other dimension--are automagically tailored to the data.


### Overriding the Defaults


With the WMS Reflector handling the sizing and bounding box issues, it's easier to play with Geoserver's different [output formats](http://docs.codehaus.org/display/GEOSDOC/Output+Formats).  The default request returns a PNG image of a map.  But the following URL gets you a PDF

[­`http://geo.openplans.org:8080/geoserver/wms/reflect?format=application/pdf&layers=topp:states`](http://geo.openplans.org:8080/geoserver/wms/reflect?format=application/pdf&layers=topp:states)

Once again, with the Reflector, the URL contains just what needs to be said, and no more.  You can even use the Reflector to quickly make navigable OpenLayers maps using the `format=application/openlayers`­ option.

[­`http://geo.openplans.org:8080/geoserver/wms/reflect?format=application/openlayers &layers=topp:states&height=300`](http://geo.openplans.org:8080/geoserver/wms/reflect?format=application/openlayers&layers=topp:states&height=300)

If you are interested in learning more about the WFS Reflector and the parameters it supplies and derives, take a look at Arne's [documentation](http://docs.codehaus.org/display/GEOSDOC/WMS+Reflector+-+Include+maps+on+your+webpages,+the+easy+way), which provides more details and examples.

­

­
