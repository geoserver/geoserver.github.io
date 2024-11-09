---
author: Nima Ghasemloo
layout: post
title: Exploring CQL/ECQL Filtering in GeoServer
date: 2024-11-11
categories:   
- Tutorials
---

[GeoSpatial Techno](https://www.youtube.com/@geospatialtechno) is a startup focused on geospatial information that is providing e-learning courses to enhance the knowledge of geospatial information users, students, and other startups. The main approach of this startup is providing quality, valid specialized training in the field of geospatial information.

( [YouTube](https://www.youtube.com/@geospatialtechno)
| [LinkedIn](https://www.linkedin.com/in/geospatialtechno)
| [Facebook](https://www.facebook.com/geospatialtechno)
| [X](https://twitter.com/geospatialtechn)
)

----

### Exploring CQL and ECQL Filtering in GeoServer
In this session, we want to talk about the **Using CQL/ECQL Filters in GeoServer** in detail. If you want to access the complete tutorial, click on the [link](https://www.youtube.com/watch?v=44E2eBiF5Jg&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).

[![](https://img.youtube.com/vi/44E2eBiF5Jg/0.jpg)](https://www.youtube.com/watch?v=44E2eBiF5Jg&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL)

## Introduction
Common Query Language (CQL) is a text-based query language developed by the OGC for the Catalogue Web Services specification. Unlike the XML-based Filter Encoding language, CQL is more readable and easier for manual authoring. However, it has limitations, such as not being able to encode ID filters and requiring the attribute to be on the left side of comparison operators.

To overcome these limitations, GeoServer offers an extended version called ECQL, which closely resembles SQL and provides greater flexibility. ECQL allows users to define filters for querying data in GeoServer using attribute comparisons, logical operators, and spatial predicates. It is compatible with GeoServer's REST API and can be used for WMS and WFS requests to retrieve filtered data.

**Note.** This video was recorded on GeoServer 2.22.4, which is not the most up-to-date version. Currently, versions 2.25.x and 2.26.x are supported. To ensure you have the latest release, please visit this [link](https://geoserver.org/download/) and avoid using older versions of GeoServer.

## Comparison operators
To compare attribute values or other numeric and text values in your CQL / ECQL (Extended Common Query Language) expressions, you can utilize comparison operators.

In the **Layer Preview** section, first click on the **OpenLayers** option for the `topp:states` layer. Next, locate and click on the **Toggle options toolbar** in the top left corner to access the advanced options.

In the CQL filter box within this toolbar, enter the filter expression `STATE_NAME = 'Texas'`, and then press the **Apply** button. This filter will retrieve and display the data for the state of Texas.

By reviewing the following examples using the **Toggle options toolbar** from the **LayerPreview** page, you will learn how to effectively understand and apply comparison operators using CQL/ECQL expressions:

- 'PropertyIsGreaterThanOrEqualTo' filter

This filter shows the states that have more than or equal to 5 million inhabitants.

	PERSONS >= 5000000


- 'PropertyIsLike' filter

This filter shows the states whose names, contain the letters 'ing' like Washington and Wyoming.

	STATE_NAME like '%ing%'


- 'PropertyIsBetween' filter

This filter shows the states with a population of 5 million to 10 million.

	PERSONS between 5000000 and 10000000


## Spatial operators
These operators enable you to perform spatial queries and filter data, based on various relationships between geometries. Here are the explanations for some commonly used spatial operators:

- 'Intersect' filter

This filter allows you to query spatial data in GeoServer based on geometric intersection relationships. This filter returns all features that have any spatial intersection or overlap.

The syntax for the Intersect filter in CQL is as follows:

	Intersects(the_geom,Point(-90 40))


- 'Within' filter

The Within filter checks if a spatial object is completely within another spatial object. This filter retrieves all features that are located within the boundaries of a specified geometric shape, using spatial relationships.

	Within(the_geom,Polygon((-100 30,-100 45,-80 45,-80 30,-100 30)))


- 'Contains' filter

This filter is the inverse of the "Within" filter. It checks if a spatial object completely contains another spatial object and helps you retrieve features that fully enclose the specified geometry.

	CONTAINS(the_geom,LINESTRING(-73.9 43.5,-77.76 42.56))

## Bounding Box operators
The Bounding Box operator is used to filter data based on a specified bounding box. The "bbox" filter in CQL allows you to query spatial data in GeoServer based on a bounding box or a rectangular area.

CQL filters can also be utilized with the GET method. To use the bbox filter using the GET method, enter the following code in the URL address bar of your browser:
	
	http://localhost:8080/geoserver/topp/wms?service=WMS&version=1.1.0&request=GetMap&layers=topp:states&bbox=-124.73142200000001,24.955967,-66.969849,49.371735&width=768&height=330&srs=EPSG:4326&format=application/openlayers&CQL_FILTER=BBOX(the_geom,-110,41,-95,45)

This filter enables you to retrieve all features that intersect, or are contained within the specified bounding box.

----

In this session, we took a brief journey through the "CQL filtering in GeoServer". If you want to access the complete tutorial, click on the  [link](https://www.youtube.com/watch?v=44E2eBiF5Jg&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).