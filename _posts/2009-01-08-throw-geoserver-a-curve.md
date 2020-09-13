---
author: bmmpxf
comments: true
date: 2009-01-08 20:49:42+00:00
layout: post
link: http://blog.geoserver.org/2009/01/08/throw-geoserver-a-curve/
slug: throw-geoserver-a-curve
title: Throw GeoServer a curve (and it will be labeled)
wordpress_id: 166
categories:
- Features
- Tips and Tricks
---

Improvements to GeoServer are being made all the time, but to the average user, not all improvements are immediately discernible.  However, recently a new feature has been added to GeoServer's rendering algorithms, and all I can say is “wow.”  I am referring to **curved line labeling**.

Labels on lines have rendering challenges that points and polygons do not.  This is because lines can curve.  Not officially, of course, but lines can be a collection of line segments, which meet at their edges but can be rotated with respect to each other.  The default behavior for a label is to appear parallel to the orientation of a line.  However, this can cause problems when the label resides along a curve, as the label will not follow it.  In some extreme cases, the label can appear only marginally connected to the line, which minimizes the effectiveness of the label!  Clearly, there was room for improvement.

This improvement was sponsored by [TriMet](http://trimet.org), the Portland, Oregon area transportation agency that uses GeoServer in their [Trip Planner](http://maps.trimet.org).  Lead GeoServer developer Andrea Aime tackled this task with his usual aplomb, and GeoServer now renders labels that follow curves.  Below is worth two thousand words:

[gallery]
  


This new road labeling is only in versions 1.7.1 and later.  Currently this functionality is not turned on by default, but is instead must be enabled in GeoServer.  One way of doing this is to edit your `web.xml` file inside the `WEB-INF` directory.  Stop your GeoServer instance, and insert the following code block:


<blockquote>`<context-param>
<param-name>USE_NG_LABELLER</param-name>
<param-value>true</param-value>
</context-param> `</blockquote>


In addition, you also need to edit your SLD to include a `VendorOption` inside your `TextSymbolizer`.  Add the following line:


<blockquote>`<VendorOption name="followLine">true</VendorOption>`</blockquote>


Restart your GeoServer, and you're all set!

For me, the ability for GeoServer to output curved line labels is a huge step forward.  There's something about these labels that make the map seem so much more professional.  Special thanks to TriMet for sponsoring this awesome new feature.  [Have you tried it out yet?](http://geoserver.org/display/GEOS/Stable)
