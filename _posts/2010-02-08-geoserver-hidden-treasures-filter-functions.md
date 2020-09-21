---
author: geoserver
comments: true
date: 2010-02-08 16:11:42+00:00
layout: post
link: http://blog.geoserver.org/2010/02/08/geoserver-hidden-treasures-filter-functions/
slug: geoserver-hidden-treasures-filter-functions
title: 'GeoServer hidden treasures: filter functions'
wordpress_id: 470
categories:
- Behind The Scenes
- Tips and Tricks
---

Ever had the need to format some text in SLD, or to perform complex filter in WFS, and noticed that the basic elements of the OGC Filter specification left you wanting for more?

If so, welcome to the club. One thing few people know is that both SLD and WFS filtering capabilities can be extended by using **filter functions**. A filter function is just like a programming language function, it's something that takes arguments and returns some result. For example, "sin(toRadians(45))" will compute the mathematical sin of 45 degrees, and "strSubstring("hippopotamus", 0,  5)" will return "hippo".

The concept of filter function is standardized, but functions themselves are not, so once you start using them you're tied to a specific server. However they often provide the level of flexibility that you just need in order to get some work done. The good news is that GeoServer already contains tens of them, from number and date formatting, to geometry manipulation, math, string wrangling. So far we just never found the time to document them, but things have changed and we have now quite a [complete reference along with some examples](http://docs.geoserver.org/2.0.x/en/user/filter/index.html).

Let me show you a simple example of using functions. Say we have a contour map, each isoline has an elevation, and we want to show it on the map. Unfortunately the elevation is stored as a floating point, resulting in a less than pleasing output of "150.0" or sometimes "149.999999" when we know the elevation accuracy does not go beyond the meter. To get nice labelling we can use the "numberFormat" filter function to force an integer representation instead (along with some VendorOptions):

    
    <TextSymbolizer>
      <Label>
        <ogc:Function name="numberFormat">
           <ogc:Literal>#</ogc:Literal>
           <ogc:PropertyName>ELEVATION</ogc:PropertyName>
        </ogc:Function>
       </Label>



    
      ....



    
       <VendorOption name="followLine">true</VendorOption>
       <VendorOption name="repeat">250</VendorOption>
       <VendorOption name="maxDisplacement">150</VendorOption>
       <VendorOption name="maxAngleDelta">30</VendorOption>
    </TextSymbolizer>


Notice how the the ELEVATION field is formatted as an integer number following the simple formatting pattern provided (for a full reference see the the [Java DecimalFormat](http://java.sun.com/javase/6/docs/api/java/text/DecimalFormat.html) documentation):

![contours](http://geoserver.wpengine.com/wp-content/uploads/2010/02/contours1.png)

I hope you'll find interesting and clever uses of the existing filter functions to improve the way you work with GeoServer. Next time I'll show you my favourite one, which is also a new feature in GeoServer 2.0.1, called "geometry transformations". Stay tuned to learn more about it.
