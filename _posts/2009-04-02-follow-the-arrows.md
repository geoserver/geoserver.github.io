---
author: bmmpxf
comments: true
date: 2009-04-02 15:47:09+00:00
layout: post
link: http://blog.geoserver.org/2009/04/02/follow-the-arrows/
slug: follow-the-arrows
title: Follow the arrows
wordpress_id: 191
categories:
- Tips and Tricks
- User perspectives
tags:
- street labels arrows SLD
---

Here's a neat trick for those working with road maps that want to indicate traffic direction by way of appropriately pointed arrows.  With [text symbolizers using font characters](http://blog.geoserver.org/2008/12/16/dynamic-symbolizers-part-2/), this is actually a snap, provided your data includes information about direction.

The [New York City streets](http://www.nyc.gov/html/dcp/html/bytes/dwnlion.shtml) data set has an attribute field called `trafdir` which specifies the flow of traffic on one-way streets:



<blockquote>**W** - ("with") One-way in the direction of ascending street numbers
**A** - ("against") One-way in the opposite direction of ascending street numbers</blockquote>




With this in mind, all that is needed is an SLD with two rules, each rule drawing an arrow pointing in appropriate direction specified by the `trafdir` attribute.  Since arrows are included in most fonts, this can be accomplished using text symbolizers.  And since the text label is oriented relative to the lines themselves (due to [labels that can follow curves](http://blog.geoserver.org/2009/01/08/throw-geoserver-a-curve/)) the arrows will automatically be properly aligned with the road.

Here is one of the SLD rules.  The other rule is identical, except for the attribute value and the specific character used.


    
    
    <Rule>
      <ogc:Filter>
        <ogc:PropertyIsEqualTo>
          <ogc:PropertyName>trafdir</ogc:PropertyName>
          <ogc:Literal>W</ogc:Literal>
        </ogc:PropertyIsEqualTo>
      </ogc:Filter>
      <TextSymbolizer>
        <Label>
          <ogc:Literal>&#x2192;</ogc:Literal>
        </Label>
        <Font>
          <CssParameter name="font-family">Lucida Sans</CssParameter>
          <CssParameter name="font-size">18</CssParameter>
        </Font>
        <Fill>
          <CssParameter name="fill">#a4bdc5</CssParameter>
        </Fill>
      </TextSymbolizer>
    </Rule>
    






This trick was figured out by Jordan Anderson, author of [Ride The City](http://www.ridethecity.com/), who goes on to say:



<blockquote>_"Probably the most challenging thing was getting the correct balance between street name labels and arrow labels (which are on two different layers). I became intimately familiar with all the new labeling options and made use of spaceAround, maxDisplacement, and Repeat to get something close to the right balance."_</blockquote>



[![](http://geoserver.wpengine.com/wp-content/uploads/2009/04/oneway_arrows-300x2821.png)](http://geoserver.wpengine.com/wp-content/uploads/2009/04/oneway_arrows1.png)

Looks pretty good to me.  Thanks Jordan!
