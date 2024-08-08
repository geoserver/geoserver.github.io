---
author: Milad Rafiei
layout: post
title: Using Binary Comparison Operators in GeoServer Filters
date: 2024-08-03
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

### Binary Comparison Operators in GeoServer Filters
In this session, we want to talk about the various types of filters, with a particular focus on "Binary comparison operators in GeoServer" comprehensively. If you want to access the complete tutorial, simply click on the [link](https://www.youtube.com/watch?v=3XCwZIJxi7M&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).

[![](https://img.youtube.com/vi/3XCwZIJxi7M/0.jpg)](https://www.youtube.com/watch?v=3XCwZIJxi7M)

## Introduction
Filtering allows the selection of features that satisfy a specific set of conditions. Filters can be used in several contexts in GeoServer:
- In WMS requests, select which features should be displayed on a map
- In WFS requests, specify the features to be returned
- In SLD documents, apply different symbolizations to features on a thematic map

**Note.** This video was recorded on GeoServer 2.22.4, which is not the most up-to-date version. Currently, versions 2.24.x and 2.25.x are supported. To ensure you have the latest release, please visit this [link](https://geoserver.org/download/) and avoid using older versions of GeoServer.

## Supported filter languages
Data filtering in GeoServer follows the OGC Filter Encoding Specification, which provides a standard XML schema for encoding spatial, attribute, and temporal filters in GIS. This allows for customized queries to retrieve specific data from databases and web services while ensuring interoperability among GIS applications. GeoServer supports filters in both Filter Encoding Language and Common Query Language.

### Filter Encoding Language
The Filter Encoding language, defined by OGC standards, utilizes an XML-based syntax to select specific features, similar to the "WHERE" clause in SQL. A filter consists of a condition formed by Predicate elements and Logical operators, employing comparison and spatial operators to evaluate relationships between feature properties. In this session, we will explore various types of binary comparison operators, while the next sessions will cover spatial operators.

### Common Query Language
Common Query Language (CQL) is a language used in GeoServer for constructing filters and queries on geospatial data. It provides flexible and powerful options for filtering and retrieving specific subsets of data from GeoServer layers. In the upcoming sessions, we will dive into a detailed exploration of CQL, covering its various operations and practical usage.

## Comparison operators
These operators are part of Filter Encoding operators and are used in attribute-based queries to filter and retrieve specific features or data, based on their non-spatial attributes. The comparison operators include: binary comparison operators and value comparison operators.

The binary comparison operators are:
- PropertyIsEqualTo
- PropertyIsNotEqualTo
- PropertyIsLessThan
- PropertyIsLessThanOrEqualTo
- PropertyIsGreaterThan
- PropertyIsGreaterThanOrEqualTo

These operators contain two filter expressions to be compared. The first operand is often a `<PropertyName>`, but both operands may be any expression, function or literal value. Binary comparison operator elements may include an optional matchCase attribute, with the true or false value. The default value is true, but the comparisons do not check the case if the attribute has a false value.

**Note.** String comparison operators are case-sensitive.

### PropertyIsEqualTo
PropertyIsNotEqualTo is a common type of filter used in GeoServer, which allows you to retrieve features from a data source based on the values of one or more properties. As an example of using this filter in WFS getFeature request:
- Navigate to the **Demos** page, then select **Demo requests**.
- From the Request section, select the **WFS_getFeature1.0.xml** request.
- The address will be filled in automatically, in the URL section.

Use the following block codes to replace line 26:

    <PropertyIsEqualTo>
      <PropertyName>STATE_NAME</PropertyName>
	  <Literal>Delaware</Literal>
	</PropertyIsEqualTo>	
	   
- Now, we will explain some elements:
  -  The first fifteen lines include explanations in the form of comments.
  -  Line 16 describes the XML version and the GetFeature operation of the WFS service being used.
  -  Line 17 specifies the default output format for the WFS service as "gml2." Additionally, GeoServer supports several other commonly used formats such as "gml3, shapefile, geojson, and csv."
  -  Lines 18 to 23 define the start of the XML request and declare the namespaces used in the request.
  -  Line 24 specifies the type name of the feature to be queried. In this case, it requests features of the "topp:states".
  -  Lines 25 to 30 define the filter criteria for the query. On these lines, we use the **PropertyIsEqualTo** filter, to retrieve all features where the state name attribute is equal to `Delaware`.

- Press the **Submit** button to see the implemented changes.

- **Note.** For GeoServer 2.25.2 the Demo Request page has been improved to show response Headers, and provide the option to pretty print XML output.

### PropertyIsNotEqualTo
PropertyIsNotEqualTo is another common type of filter used in GeoServer, which allows you to retrieve features from a data source based on properties that don't match a specified value. As an example of using this filter in a WFS getFeature request, use the following block codes to replace lines 26 to 29:

    <PropertyIsNotEqualTo matchCase="false">
      <PropertyName>STATE_NAME</PropertyName>
	  <Literal>delAwarE</Literal>
	</PropertyIsNotEqualTo>

**Note.** The matchCase attribute in WFS_getFeature 1.1 and 2.0 versions, can be set to "false" to specify a case-insensitive comparison.
	
Press the **Submit** button.

In this example, we used the `<PropertyIsNotEqualTo>` filter to retrieve all features where the `STATE_NAME` attribute, is not equal to `Delaware`.

### PropertyIsLessThan
The PropertyIsLessThan filter is used to filter features, based on a comparison of a numeric property with a given value. It returns all features where the specified property is less than the specified value.

An example of using this filter in a WFS getFeature request is:

    outputFormat="shape-zip"
    <wfs:Query typeName="topp:states">
        <wfs:PropertyName>topp:STATE_NAME</wfs:PropertyName> 
        <wfs:PropertyName>topp:LAND_KM</wfs:PropertyName>
    <ogc:Filter>
      <PropertyIsLessThan>
        <PropertyName>STATE_FIPS</PropertyName>
        <Literal>18</Literal>
      </PropertyIsLessThan>
    </ogc:Filter>

Press the **Submit** button.

In this example, we used the `<PropertyIsLessThan>` filter to get all features in a shapefile format where the value of the `STATE_FIPS` attribute is less than `18`. The query only retrieves the `STATE_NAME` and `LAND_KM` fields, instead of all the attributes.

----

In this session, we took a brief journey through the various types of filters, with a particular focus on "Binary comparison operators in GeoServer". If you want to access the complete tutorial, simply click on the [link](https://www.youtube.com/watch?v=3XCwZIJxi7M&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).

[![](https://img.youtube.com/vi/3XCwZIJxi7M/0.jpg)](https://www.youtube.com/watch?v=3XCwZIJxi7M)