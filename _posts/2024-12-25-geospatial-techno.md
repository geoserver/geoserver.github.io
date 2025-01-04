---
author: Milad Rafiei
layout: post
title: Using Logical Operators in GeoServer Filters
date: 2024-12-25
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

### Using Logical Operators in GeoServer Filters
In this session, we want to talk about the **Using logical operators to combine multiple filters** in GeoServer. If you want to access the complete tutorial, click on the [link](https://www.youtube.com/watch?v=_9bTXVGqlcA&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).

[![](https://img.youtube.com/vi/_9bTXVGqlcA/0.jpg)](https://www.youtube.com/watch?v=_9bTXVGqlcA&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL)

## Introduction
Logical operators in Web Feature Service (WFS) filtering are essential for combining multiple conditions within GeoServer. These operators enable users to construct complex queries, facilitating data retrieval from the WFS service. The primary logical operators include **AND**, **OR**, and **NOT**.

**Note.** This video was recorded on GeoServer 2.22.4, which is not the most up-to-date version. Currently, versions 2.25.x and 2.26.x are supported. To ensure you have the latest release, please visit this [link](https://geoserver.org/download/) and avoid using older versions of GeoServer.

### AND
This operator combines multiple conditions into a single filter expression. The resulting expression matches only those features that meet all of the specified criteria.

- As an example of using this filter in WFS getFeature request, navigate to the **Demos** page, then select **Demo requests**.
- From the **Request** section, select the **WFS_getFeature1.0.xml** request.

Use the following block codes to replace line 26:

	<ogc:And>
	  <PropertyIsLessThan>
	    <PropertyName>LAND_KM</PropertyName>
	    <Literal>100000</Literal>
	  </PropertyIsLessThan>
	  <PropertyIsGreaterThan>
	    <PropertyName>PERSONS</PropertyName>
	    <Literal>5000000</Literal>
	  </PropertyIsGreaterThan>
	</ogc:And>

**Note.** In all examples in this blog post, we utilize the `topp:states` layer.

In this example, we applied a filter to the layer, where the value of the `LAND_KM` attribute, is less than 100,000 **and** the `PERSONS` is greater than 5 million people.

The results include three states: `Massachusetts`, `New Jersey` and `Indiana`.


To use the CQL filtering to apply the equivalent of this example, first, preview the `top:states` layer in the **Layer Preview** section. Then, add the filter `CQL_FILTER=LAND_KM<100000 And PERSONS>5000000` to the end of the URL.

The complete URL for the layer is as follows:

	http://localhost:8080/geoserver/topp/wms?service=WMS&version=1.1.0&request=GetMap&layers=topp%3Astates&bbox=-124.73142200000001,24.955967,-66.969849,49.371735&width=768&height=330&srs=EPSG%3A4326&styles=&format=application/openlayers&CQL_FILTER=LAND_KM<100000 And PERSONS>5000000


### OR
This operator allows you to combine multiple conditions and retrieve features that satisfy any of the specified conditions. In simpler terms, at least one condition must be true for the filter to be considered a match.

Here's an example of how to use the "OR" operator to filter a WFS layer based on two conditions.

	<ogc:Or>
	  <PropertyIsLessThan>
	    <PropertyName>LAND_KM</PropertyName>
	    <Literal>100000</Literal>
	  </PropertyIsLessThan>
	  <PropertyIsGreaterThan>
	    <PropertyName>PERSONS</PropertyName>
	    <Literal>5000000</Literal>
	  </PropertyIsGreaterThan>
	</ogc:Or>


Press the **Submit** button.

In this example, we filtered the layer to display features that meet either of these conditions: The value of the `LAND_KM` attribute is less than 100,000 **or** the `PERSONS` attribute represents a population greater than 5 million people. The results include `25` states.


To apply the same example using the CQL filtering and observe the results, use the following code in the URL of the layer as mentioned above:

	http://localhost:8080/geoserver/topp/wms?service=WMS&version=1.1.0&request=GetMap&layers=topp%3Astates&bbox=-124.73142200000001,24.955967,-66.969849,49.371735&width=768&height=330&srs=EPSG%3A4326&styles=&format=application/openlayers&CQL_FILTER=LAND_KM<100000 Or PERSONS>5000000


### NOT
In GeoServer, the **NOT** operator, also known as the logical negation operator, is used to invert the meaning of a filter expression. It takes one or more filter expressions and returns features that don't meet the specified conditions.

Here's an example of using the "NOT" operator for filtering a WFS layer by two conditions:

    <ogc:Not>
      <ogc:Or>
        <PropertyIsLessThan>
          <PropertyName>LAND_KM</PropertyName>
          <Literal>100000</Literal>
        </PropertyIsLessThan>
        <PropertyIsGreaterThan>
          <PropertyName>PERSONS</PropertyName>
          <Literal>5000000</Literal>
        </PropertyIsGreaterThan>
      </ogc:Or>
    </ogc:Not>


Press the **Submit** button.

In this example, we filtered the layer to show features that don't meet any of these conditions. That is, neither the value of the `LAND_KM` attribute is less than 100,000 **nor** is the value of the `PERSONS` parameter more than 5 million people. The results include `24` states.

To see how to use the NOT operator in CQL filtering, use the following code at the end of the URL’s layer:

	http://localhost:8080/geoserver/topp/wms?service=WMS&version=1.1.0&request=GetMap&layers=topp%3Astates&bbox=-124.73142200000001,24.955967,-66.969849,49.371735&width=768&height=330&srs=EPSG%3A4326&styles=&format=application/openlayers&CQL_FILTER=NOT(LAND_KM<100000 Or PERSONS>5000000)


## Combine operators
GeoServer provides the capability of combining logical operators with geometric filters, enhancing the flexibility of WFS filtering. This feature enables users to create more specific and reliable filtering criteria.

Here is an example that effectively uses both spatial and comparison filtering:

    <ogc:Filter>
      <ogc:And>
        <ogc:Intersects>
          <ogc:PropertyName>the_geom</ogc:PropertyName>
          <gml:LineString xmlns:gml="http://www.opengis.net/gml" srsName="EPSG:4326">
            <gml:coordinates>-73.9,43.5 -81.1,38.6 -78.57,35.5</gml:coordinates>
          </gml:LineString>          
        </ogc:Intersects>
        <PropertyIsGreaterThanOrEqualTo>
          <PropertyName>PERSONS</PropertyName>
          <Literal>10000000</Literal>
        </PropertyIsGreaterThanOrEqualTo>
      </ogc:And>
    </ogc:Filter>

  
In this example, we filtered out states with populations exceeding 10 million, as well as states intersected by a LineString with given coordinates.

Thus, we identified `New York` and `Pennsylvania` as the two states that satisfy these conditions.


To see how to use CQL filtering for this example, follow the instance shown on the screen:


	CQL_FILTER=INTERSECTS(the_geom,LINESTRING(-73.9 43.5,-81.1 38.6,-78.57 35.5)) AND PERSONS>10000000
	
	
As a final example, we examine a comprehensive scenario that incorporates different operators. This example includes a spatial operator, such as the Within filter. Additionally, it showcases two comparison operators, namely `PropertyIsLike` and `PropertyIsGreaterThan`.

To better understand these concepts, use the following example:
	

    <ogc:Filter>
      <ogc:And>
        <ogc:Within>
          <ogc:PropertyName>the_geom</ogc:PropertyName>
          <gml:Polygon xmlns:gml="http://www.opengis.net/gml" srsName="EPSG:4326">
            <gml:outerBoundaryIs>
              <gml:LinearRing>
                <gml:coordinates>-100,30 -100,45 -80,45 -80,30 -100,30</gml:coordinates>
              </gml:LinearRing>
            </gml:outerBoundaryIs>
          </gml:Polygon>         
        </ogc:Within>
        <ogc:Or>
          <ogc:Filter>
            <ogc:PropertyIsLike wildCard="%" singleChar="_" escape="!">
              <ogc:PropertyName>STATE_NAME</ogc:PropertyName>
              <ogc:Literal>%na%</ogc:Literal>
            </ogc:PropertyIsLike>
          </ogc:Filter>
          <PropertyIsGreaterThan>
            <PropertyName>STATE_FIPS</PropertyName>
            <Literal>30</Literal>
          </PropertyIsGreaterThan>
        </ogc:Or>
      </ogc:And>
    </ogc:Filter>
  
  
In this example, we use WFS filtering to extract the States that are completely enclosed within specific coordinates. Moreover, we retrieve States whose `STATENAME` includes the letters "na" or whose `STATEFIPS` value is greater than 30.

Therefore, we have identified three states that meet the specified criteria: `Tennessee`, `Indiana`, and `Ohio`.


To use the CQL filtering for this example, use the following code:

	CQL_FILTER=Within(the_geom,Polygon((-100 30,-100 45,-80 45,-80 30,-100 30))) AND (STATE_NAME LIKE '%na%' OR STATE_FIPS > 30)
	

----

In this session, we took a brief journey through the **Combining multiple operators for WFS filtering** in GeoServer. If you want to access the complete tutorial, click on the  [link](https://www.youtube.com/watch?v=_9bTXVGqlcA&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).