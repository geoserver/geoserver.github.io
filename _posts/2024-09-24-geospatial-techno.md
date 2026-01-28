---
author: Milad Rafiei
layout: post
title: Using Spatial Operators in GeoServer Filters
date: 2024-09-24
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

### Spatial Operators in GeoServer Filters
In this session, we want to talk about the **Spatial operators in GeoServer** in detail. If you want to access the complete tutorial, click on the [link](https://www.youtube.com/watch?v=mYD0sCNiczE&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).

[![](https://img.youtube.com/vi/mYD0sCNiczE/0.jpg)](https://www.youtube.com/watch?v=mYD0sCNiczE&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL)

## Introduction
GeoServer supports various spatial operators that filter geospatial data based on their location or spatial relationships with other features. These operators are commonly used with other filter expressions to create complex queries. These queries are useful for extracting specific subsets of data from a larger dataset.

The spatial operators are Topological, Distance, and Bounding Box operators. We'll explain them in more detail below.

**Note.** This video was recorded on GeoServer 2.22.4, which is not the most up-to-date version. We encourage all users to use the stable series, currently {{site.stable_branch}}. To ensure you have the latest release, please visit this [link](https://geoserver.org/download/) and avoid using older versions of GeoServer.

## Topological operators
In GeoServer, topological operators are used for spatial analysis and processing of geographic data. These operators perform geometric operations that preserve the spatial relationship or topology between geometric features. Some common topological operators in GeoServer include: Intersects, Within, Contains, etc.

### Intersects
The **Intersects** filter in GeoServer is used to query spatial data based on the intersection of two geometry objects. For example, you can use this operator to extract all features that intersect with a specified Point, Line, or Polygon.

Here are some examples of how you can use this filter in an XML request to filter the `States` layer by the `State_Name` attribute:

- Navigate to the **Demos** page, then select **Demo requests**.
- From the Request section, select the **WFS_getFeatureIntersects1.0.xml** request.
- The address will be filled in automatically, in the URL section.
- Now, we will explain some elements:
  -  The first thirteen lines include explanations in the form of comments.
  -  Line 14 describes the XML version and the `getFeatureIntersects` operation of the WFS service being used.
  -  Line 15 specifies the default output format for the WFS service as `GML2`. Additionally, GeoServer supports several other commonly used formats such as "gml3, shapefile, geojson, and csv."
  -  Lines 16 to 22 define the start of the XML request and declare the namespaces used in the request.
  -  Line 23 specifies the type name of the feature to be queried. In this case, it requests features of the `topp:states`.
  -  Lines 25 to 30 define the filter criteria for the query. On these lines, we use the **Intersects** filter, to retrieve all states that intersects with a Point defined by latitude and longitude.

- Press the **Submit** button.

**Note.** For GeoServer 2.25.2 the Demo Request page has been improved to show response Headers, and provide the option to pretty print XML output.

### Within
This operator is used to retrieve features that are completely within the specified geometry. For example, you can use this operator to extract all features that are within a polygon.

Here's an example of how you can define a `Within` filter in XML. As an example of using this filter in a WFS getFeature request, use the following block codes to replace lines 24 to 31:

    <Filter>
      <Within>
        <PropertyName>the_geom</PropertyName>
        <gml:Polygon xmlns:gml="http://www.opengis.net/gml" srsName="EPSG:4326">
		  <gml:outerBoundaryIs>
		    <gml:LinearRing>
			  <gml:coordinates>-90.73,29.85 -90.73,35.92 -80.76,35.92 -80.76,29.85 -90.73,29.85</gml:coordinates>
			</gml:LinearRing>
		  </gml:outerBoundaryIs>
        </gml:Polygon>
      </Within>
    </Filter>

Press the **Submit** button. As you can see, the result includes two states named `Alabama` and `Georgia`.

### Contains
This operator is used to filter data that is completely contained within a given geometry. For example, you can use this operator to extract all features that are completely contained within a polygon that represents a state boundary.

Here's an example of how you can define a `Contains` operator in XML:

    <Filter>
      <Contains>
        <PropertyName>the_geom</PropertyName>
        <gml:LineString srsName="EPSG:4326">
           <gml:coordinates>-89.35,31.46 -89.35,32.11 -89.49,32.23 -90.21,32.23</gml:coordinates>
        </gml:LineString>
      </Contains>
    </Filter>

Press the **Submit** button. As you can see, the state that contains the given geometry is `Mississippi`.

You will need to adjust the filter and shape to match your data and SRS. Assuming you have a data source with a geometry column named the_geom that uses the EPSG:4326 coordinate system.

## Distance operators
In GeoServer, Distance operators like "DWithin" and "Beyond" filters, are used to filter and retrieve features based on their spatial relationship and proximity to a given geometry or location. These operators can be used in WFS requests and are useful for performing spatial analysis and finding nearby features.

### DWithin
The 'DWithin' or 'Distance Within' filter, will return records that are located within a specific distance of a defined point, much like a buffer. As well as the point geometry, you must specify the value of the distance from this point and the unit of measure. The units for the DWithin are: Feet, meters, kilometers and miles.

Here's an example of how to use the `DWithin` filter in a GeoServer XML configuration file. To find all the features that are within `10000` meters of a given point in a layer called "sf:archsites", the following WFS request can be used.

	<wfs:GetFeature service="WFS" version="1.0.0"
                outputFormat="application/json" xmlns:wfs="http://www.opengis.net/wfs"
                xmlns:ogc="http://www.opengis.net/ogc"
                xmlns:gml="http://www.opengis.net/gml"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xsi:schemaLocation="http://www.opengis.net/wfs http://schemas.opengis.net/wfs/1.0.0/WFS-basic.xsd">
	  <wfs:Query typeName="sf:archsites">
	    <ogc:Filter>
		  <ogc:DWithin>
			<ogc:PropertyName>the_geom</ogc:PropertyName>
			  <gml:Point srsName="http://www.opengis.net/gml/srs/epsg.xml#26713">
				<gml:coordinates>593250,4923867</gml:coordinates>
			  </gml:Point>
			<ogc:Distance units="meter">10000</ogc:Distance>
		  </ogc:DWithin>
		</ogc:Filter>
	  </wfs:Query>
	</wfs:GetFeature>

This will return all the features in "sf:archsites" layer, that are within 10000 meters of the given point.
Remember that, the EPSG code mentioned in line 11 is very important because it serves as a reference point for importing coordinates and distance values.

Press the **Submit** button.

## Bounding Box operators
The Bounding Box operator is used to filter data based on a specified bounding box. A bounding box is a rectangular region defined by its lower left and upper right coordinates: minx, miny, maxx, and maxy. For example, you can use this operator to extract all features that are located or partially located inside a box of coordinates.

As an example of using this operator, select the **WFS_getFeatureBBOX1.0.xml** from the Request section. Now the filters block code is as follows:

    <Filter>
      <BBOX>
        <PropertyName>the_geom</PropertyName>
        <gml:Box srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">
           <gml:coordinates>-75.102613,40.212597 -72.361859,41.512517</gml:coordinates>
        </gml:Box>
      </BBOX>
    </Filter>

In this case, we just get the `STATE_NAME` and `PERSONS` attribute.
Using the range specified in the code specifies the features that are completely or partially located in this area.
The result includes four states named `New York`, `Pennsylvania`, `Connecticut`, and `New Jersey` as you see on the screen.

----

In this session, we took a brief journey through the "Spatial operators in GeoServer". If you want to access the complete tutorial, click on the  [link](https://www.youtube.com/watch?v=mYD0sCNiczE&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).