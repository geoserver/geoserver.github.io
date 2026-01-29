---
author: Nima Ghasemloo
layout: post
title: Using Value Comparison Operators in GeoServer Filters
date: 2024-09-03
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

### Value Comparison Operators in GeoServer Filters
In this session, we want to talk about the various types of filters, with a particular focus on "Value comparison operators in GeoServer" comprehensively. If you want to access the complete tutorial, click on the [link](https://www.youtube.com/watch?v=Qcmvr9WS8S8&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).

[![](https://img.youtube.com/vi/Qcmvr9WS8S8/0.jpg)](https://www.youtube.com/watch?v=Qcmvr9WS8S8&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL)

## Introduction
Filtering allows the selection of features that satisfy a specific set of conditions. Filters can be used in several contexts in GeoServer:
- In WMS requests, select which features should be displayed on a map
- In WFS requests, specify the features to be returned
- In SLD documents, apply different symbolizations to features on a thematic map

**Note.** This video was recorded on GeoServer 2.22.4, which is not the most up-to-date version. We encourage all users to use the stable series, currently {{site.stable_branch}}. To ensure you have the latest release, please visit this [link](https://geoserver.org/download/) and avoid using older versions of GeoServer.

## Comparison operators
In GeoServer, the Web Feature Service (WFS) filtering utilizes a set of comparison operators to facilitate the querying of geospatial features. These operators allow users to create precise filters based on attribute values, enabling robust spatial queries. The main comparison operators available include: Binary comparison operators and Value comparison operators.

The value comparison operators are:
- PropertyIsLike
- PropertyIsNull
- PropertyIsBetween

### PropertyIsLike
The **PropertyIsLike** operator is used to compare a string property value with a text pattern. It includes the <PropertyName> and <Literal> elements to specify the property name and pattern respectively. The pattern can contain a sequence of regular characters and three special pattern characters.

These characters are defined by the attributes of the <PropertyIsLike> element:
- **WildCard:** It specifies the pattern character that matches any sequence of zero or more string characters
- **SingleChar:** It specifies the pattern character that matches any single string character
- **EscapeChar:** It specifies the escape character which can be used to escape the pattern character

Geoserver supports the PropertyIsLike operator within filter expressions for querying spatial data. Here are some examples of how you can use this filter in an XML request to filter the `States` layer by the `State_Name` attribute:

- Navigate to the **Demos** page, then select **Demo requests**.
- From the Request section, select the **WFS_getFeature1.0.xml** request.
- The address will be filled in automatically, in the URL section.

Use the following block codes to replace line 26:

    <PropertyIsLike wildCard="*" singleChar="_" escapeChar="\">
      <PropertyName>STATE_NAME</PropertyName>
      <Literal>North*</Literal>
    </PropertyIsLike>	
	   
- Now, we will explain some elements:
  -  The first fifteen lines include explanations in the form of comments.
  -  Line 16 describes the XML version and the GetFeature operation of the WFS service being used.
  -  Line 17 specifies the default output format for the WFS service as "gml2." Additionally, GeoServer supports several other commonly used formats such as "gml3, shapefile, geojson, and csv."
  -  Lines 18 to 23 define the start of the XML request and declare the namespaces used in the request.
  -  Line 24 specifies the type name of the feature to be queried. In this case, it requests features of the "topp:states".
  -  Lines 25 to 30 define the filter criteria for the query. On these lines, we use the **PropertyIsLike** filter, to retrieve all states that start with the word `North`.

- Press the **Submit** button to see the implemented changes.

- **Note.** For GeoServer 2.25.2 the Demo Request page has been improved to show response Headers, and provide the option to pretty print XML output.

Now, we are looking for the States with four-letter names, where the letter `o` appears at both the beginning and the end. This requires using a **singleChar** as a different mode of the "LIKE" operator that you see on the screen:

    <ogc:Filter>
      <PropertyIsLike wildCard="*" singleChar="_" escapeChar="\">
        <PropertyName>STATE_NAME</PropertyName>
        <Literal>O__o</Literal>
      </PropertyIsLike>
    </ogc:Filter>

Press the **Submit** button to see the implemented changes. As you can see, a state called `Ohio` was found that meets the conditions in this example.

To show the escapeChar mode, modify the names 'Montana' and 'Minnesota' to `Monta*na` and `Minnesota*` in QGIS. This will allow you to filter out special characters, such as asterisks or underscores, that you have used. Now, use the codes displayed on the screen:

    <ogc:Filter>
      <PropertyIsLike wildCard="*" singleChar="_" escapeChar="\">
        <PropertyName>STATE_NAME</PropertyName>
        <Literal>*ta\**</Literal>
      </PropertyIsLike>
    </ogc:Filter>

Press the **Submit** button to see the implemented changes. Note that, If the **escapeChar** is not used, the correct result may not be visible in the output; because the underscore is a special character.

You have the flexibility to modify the **wildCard**, **singleChar**, and **escapeChar** attributes based on your requirements. This allows for a more proper filtering experience. So, feel free to customize them and make the most of your filtering capabilities! 

### PropertyIsNull
This operator, allows you to query for features where a specific property or attribute, has a null value. In other words, it is used to filter the features based on the absence of a value in a particular property.
In this example, the query is looking for features in the `topp:states` layer, where the STATE_NAME attribute is null.

As an example of using this filter in a WFS getFeature request, use the following block codes to replace lines 26 to 29:

    <PropertyIsNull>
      <PropertyName>STATE_NAME</PropertyName>
    </PropertyIsNull>
	
Press the **Submit** button. As you can see, there is no value returned in the output as a null value.

### PropertyIsBetween
The **PropertyIsBetween** operator is a helpful tool that allows you to determine whether a particular property of a feature, is within a defined range of values. As an example of using this operator, select the **WFS_getFeatureBetween1.1.xml** request from the **Request** section.

Now the filters block code is as follows:

    <ogc:Filter>
      <ogc:PropertyIsBetween>
        <ogc:PropertyName>topp:LAND_KM</ogc:PropertyName>
        <ogc:LowerBoundary><ogc:Literal>100000</ogc:Literal></ogc:LowerBoundary>
        <ogc:UpperBoundary><ogc:Literal>150000</ogc:Literal></ogc:UpperBoundary>
      </ogc:PropertyIsBetween>
    </ogc:Filter>

Press the **Submit** button.

Remember that **PropertyIsBetween** like other operators, is case-sensitive and the property name is specified as the first parameter to the operator. The minimum and maximum values of the range are specified as the second and third parameters, respectively.

----

In this session, we took a brief journey through the various types of filters, with a particular focus on "Value comparison operators in GeoServer". If you want to access the complete tutorial, click on the  [link](https://www.youtube.com/watch?v=Qcmvr9WS8S8&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).