---
author: geoserver
comments: true
date: 2010-05-25 08:30:20+00:00
layout: post
link: http://blog.geoserver.org/2010/05/25/polymorphism-in-application-schema/
slug: polymorphism-in-application-schema
title: Polymorphism in application-schema
wordpress_id: 660
categories:
- Features
- Tips and Tricks
- Tutorials
---

Support for  polymorphism is included in Geoserver  2.0.2. Why do we need  polymorphism support in  app-schema? Some complex  attributes are  polymorphic by nature,  which means they can have different types for   different features.




Before polymorphism was supported, attribute types had to be specified in the  mapping file, so could not vary across features. With polymorphism support, filter functions can now be used to specify conditions when  determining the encoded type.

For example: 

If MaterialCode is  "rock", er:material should be encoded as gsml:RockMaterial, otherwise it should  be encoded as  gsml:Mineral.

This can be expressed  in the mapping file like this:

    
    <AttributeMapping>
        <targetAttribute>er:material</targetAttribute>
        <sourceExpression>
            <linkElement>
                if_then_else(equalTo(MaterialCode, 'rock'), 'gsml:RockMaterial', 'gsml:Mineral')
            </linkElement>
        </sourceExpression>
    </AttributeMapping>





Another common example is  replacing null values with an xlink:href  to a URI representing missing  values:

    
    <AttributeMapping>
        <targetAttribute>er:startDate</targetAttribute>
        <sourceExpression>
            <linkElement>if_then_else(isNull(START_DATE), toXlinkHref('urn:ogc:def:nil:OGC::missing'),
                             'gml:TimeInstantPropertyType')
            </linkElement>
        </sourceExpression>
    </AttributeMapping>


Read more about  app-schema polymorphism support: [polymorphism](http://docs.geoserver.org/stable/en/user/data/app-schema/polymorphism.html).
