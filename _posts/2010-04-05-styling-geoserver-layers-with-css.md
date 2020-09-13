---
author: geoserver
comments: true
date: 2010-04-05 15:09:42+00:00
layout: post
link: http://blog.geoserver.org/2010/04/05/styling-geoserver-layers-with-css/
slug: styling-geoserver-layers-with-css
title: Styling GeoServer Layers with CSS
wordpress_id: 549
categories:
- Announcements
- Features
---

GeoServer users have a lot to wrap their heads around.  We need to optimize our servlet containers, determine projections for all those broken shapefiles, and remember to fill out layer metadata.  One issue in particular that comes up again and again is difficulty with creating [SLD files](http://docs.geoserver.org/stable/en/user/styling/index.html) to style maps.  It is hardly surprising that map designers fail to take advantage of some of the [niftier](http://blog.geoserver.org/2009/06/01/geoserver-chart-extension/) [rendering](http://blog.geoserver.org/2010/03/17/extending-your-map-styling-with-geometry-transformations/) [tricks](http://blog.geoserver.org/2008/12/08/dynamic-symbolizers-part-1/) that Andrea cooks up.  [Styler](http://blog.opengeo.org/2009/05/05/styler/), a graphical SLD editing application that OpenGeo has been developing, is one approach to making SLD creation more palatable.  But just as experienced web designers often feel limited by WYSIWYG environments, advanced users will always have a use for manual, text-based editing.  Unfortunately, the highly structured, verbose nature of XML can make this strenuous.

With this in mind, I've been working on an extension to GeoServer allowing styling of map layers with a CSS-type syntax.  This work follows in the footsteps of tools like [Cartagen](http://cartagen.org/) and [Cascadenik](http://code.google.com/p/mapnik-utils/wiki/Cascadenik) which both apply a CSS framework to map styling.

To see how a CSS map style would look, compare the "simpleRoads" SLD from the data directory that ships with GeoServer:

    
    
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <StyledLayerDescriptor version="1.0.0"
      xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd"
      xmlns="http://www.opengis.net/sld"
      xmlns:ogc="http://www.opengis.net/ogc"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <NamedLayer>
        <Name>Simple Roads</Name>
        <UserStyle>
          <Title>Default Styler for simple road segments</Title>
          <Abstract>Light red line, 2px wide</Abstract>
          <FeatureTypeStyle>
            <Rule>
              <Title>Roads</Title>
              <LineSymbolizer>
                <Stroke>
                  <CssParameter name="stroke">
                    <ogc:Literal>#AA3333</ogc:Literal>
                  </CssParameter>
                  <CssParameter name="stroke-width">
                    <ogc:Literal>2</ogc:Literal>
                  </CssParameter>
                </Stroke>
              </LineSymbolizer>
            </Rule>
          </FeatureTypeStyle>
        </UserStyle>
      </NamedLayer>
    </StyledLayerDescriptor>





with the equivalent CSS style:

    
    
    
    
    /* @title Default styler for simple road segments
     * @abstract Light red line, 2px wide
     */
    * {
      stroke: #AA3333;
      stroke-width: 2px;
    }





CSS styles are fully converted to SLD before GeoServer uses them for rendering, so the resulting SLDs can be migrated directly to other GeoServer instances, even if they don't have the CSS extension installed.   Filter functions, zoom-based styling rules, and geometry transformations are also available.

You can [download the CSS extension](http://gridlock.openplans.org/geoserver/2.0.x/community-latest/) from the nightly build server and add it to your existing GeoServer instance (2.0.0 and later only).  Installation instructions are available in the [CSS tutorial](http://docs.geoserver.org/2.0.x/en/user/community/css/tutorial.html).  All the features of the CSS extension are documented in the [CSS section](http://docs.geoserver.org/2.0.x/en/user/community/css/index.html) of the User Manual.  I encourage everyone to check it out!
