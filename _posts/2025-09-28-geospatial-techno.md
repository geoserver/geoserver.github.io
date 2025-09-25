---
author: Milad Rafiei
layout: post
title: Unlock GeoServer WPS - Key Input Categories You Need
date: 2025-09-28
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
### Unlock GeoServer WPS - Key Input Categories You Need to Know
This session provides a detailed overview of the various inputs and categories in the WPS Request Builder. If you want to access the complete tutorial, click on the [link](https://www.youtube.com/watch?v=zfNJ9virFoQ&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).

[![](https://img.youtube.com/vi/zfNJ9virFoQ/0.jpg)](https://www.youtube.com/watch?v=zfNJ9virFoQ&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL)

## Introduction
In GeoServer, the WPS request builder enables users to perform various geospatial processing operations with different functionality to analyze and manipulate geospatial data. Each category provides a set of specific operations tailored to a range of geospatial tasks.

**Note**: This tutorial uses GeoServer version 2.25.3. Be sure to download the WPS extension that corresponds exactly to your GeoServer version—mismatched versions will result in errors.

Some categories available in the WPS request builder are **JTS**, **Geo**, **GS**, and **Vec**.
-	**JTS:** The JTS category uses the Java Topology Suite library to perform various geometry manipulation and analysis operations such as Buffer, Intersection, Union, Simplify, etc.
-	**Geo:** This category includes geospatial operations that may involve coordinate transformations and spatial analysis. Some common functions include Reproject, Centroid, Convex Hull, etc.
-	**GS:** The GS or 'GeoServer Specific' category uses the GeoTools library and provides a set of geospatial processing operations specifically designed for use in the GeoServer environment. Some common functions include Feature Count, Centroid, BufferFeatureCollection, etc.
-	**Vec:** This category contains operations specifically designed for working with vector data, such as merge, dissolve, aggregate, etc.

Unlike the **GS** and **Vec** categories, the **JTS** and **Geo** do not have direct access to the layers provided by GeoServer. Instead, these processes depend on external libraries rather than utilizing the built-in features of GeoServer. First, we will introduce the inputs of the **JTS** and **Geo** categories, and then we will delve into the **GS** and **Vec** categories.

## JTS and Geo categories
The **JTS** and **Geo** categories refer to different sets of processing functions that are specifically dedicated to handling geometries and performing geospatial operations.

From the Demo menu, navigate to the WPS Request Builder. This section contains several types of processes, which you can view in the Choose Process section. They accept three inputs for execution: **Text**, **Reference**, and **Subprocess**.

### TEXT
In Text mode, you can enter the data geometry information in one of the standard formats supported by WPS. These standard formats are:
-	text/xml; subtype=gml
-	application/wkt
-	application/gml
-	application/json

The main differences between these MIME types are:
- **text/xml; subtype=gml** is more suitable for human readability and debugging, while **application/gml** is intended for machine-to-machine interactions, APIs, and programmatic consumption.
- Use **text/xml; subtype=gml** for scenarios that require easy readability or manual processing, and **application/gml** for cases where data is consumed directly by applications without being rendered as text.

Overall, the choice between the two should depend on the intended use case: for human interaction, use **text/xml; subtype=gml**; for application-oriented needs, choose **application/gml**.

#### application/wkt
The application/wkt is a MIME type that represents data encoded in the Well-Known Text (WKT) format. WKT is a text-based format for representing and exchanging geospatial data, particularly geometric shapes and objects. It supports various geometric types, including: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon.

The **application/wkt** and **application/ewkt** formats in GeoServer WPS represent geometry; WKT defines shapes without CRS, suitable for basic 2D/3D geometry. EWKT adds an SRID, embedding CRS info in the geometry string for essential context.

Here is an example of the **application/wkt** format:

```text
- POINT(48.23 11.56)
- LINESTRING(45.67 9.12, 50.45 12.34, 55.89 10.67)
- POLYGON((45.67 9.12, 50.45 12.34, 55.89 10.67, 45.67 9.12))
- MULTIPOINT((45.67 9.12), (50.45 12.34), (55.89 10.67))
- MULTILINESTRING((45.67 9.12, 50.45 12.34), (55.89 10.67, 45.67 9.12))
- MULTIPOLYGON(((45.67 9.12, 50.45 12.34, 55.89 10.67, 45.67 9.12)), ((60.12 8.34, 62.45 11.67, 65.89 10.01, 60.12 8.34)))
```

#### application/json
The application/json is a MIME type used to represent data encoded in GeoJSON format for encoding geographic data structures. It is based on the JSON format and allows the representation of simple geographic features along with their associated non-spatial attributes stored in the Properties object.

This MIME type is commonly used in Web mapping applications, GIS, and various other geospatial applications because it provides a standardized way to represent and exchange geographic data.

Here is an example of the **application/json** document:

```json  
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-122.41, 37.78]
      },
      "properties": {
        "name": "San Francisco",
        "population": 883306,
        "elevation": 16
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [[
          [-122.4194, 37.7749],
          [-122.4244, 37.7749],
          [-122.4244, 37.7799],
          [-122.4194, 37.7799],
          [-122.4194, 37.7749]
        ]]
      },
      "properties": {
        "name": "San Francisco City Hall",
        "type": "government"
      }
    }
  ]
}  
```

### REFERENCE
The **Reference** mode for specifying input geometry involves linking to an external resource containing the necessary geometry data for processing. This mode is beneficial when the geometry data is stored in a separate file or service, allowing you to provide a reference instead of including the data directly in the WPS request.

To use this option, you can choose between the GET or POST method. The choice depends on the size and nature of the referenced data, as well as any security considerations.
-	GET: This method includes the reference to an external resource, such as a URL pointing to a file or service endpoint, directly in the request URL. It's ideal for retrieving small to moderate-sized data, as the data is transmitted via URL query parameters.
- POST: This method includes the reference to the external resource in the body of the HTTP request, rather than in the URL. The POST method preferred for larger datasets or confidential data, because it's more secure and allow larger amounts of data to be transferred without URL length limitations.

### SUBPROCESS
Using the **Subprocess** mode for input geometry in a WPS request, allows for seamless chaining of multiple processes. It enables you to reference data from another process without writing intermediate results to disk, significantly enhancing workflow efficiency.

This approach is particularly beneficial when managing large datasets or executing multiple processing tasks rapidly, as it eliminates unnecessary handling steps and facilitates direct data transfer between interconnected processes.

Select **Subprocess** from the **Process Inputs** dropdown menu in the WPS Request Builder section. Then, click the **Define/Edit** link to open a new page where you can choose an additional process for chaining.

### OUTPUT
The **result** output refers to a spatial data layer, typically represented in a vector format such as **GML**, **GeoJSON**, or **WKT**. This output can be processed further, visualized, or utilized in various spatial analyses. When generating the WPS result geometry, you can choose from several standard spatial data formats, each described in detail.

These formats are:
-	text/xml; subtype=gml
-	application/wkt
-	application/gml
-	application/json

Selecting the appropriate format allows you to tailor the output to suit your specific use case or workflow.

## GS and Vec categories
These categories are specifically designed to integrate seamlessly with GeoServer layers, thereby enhancing the utilization of geospatial data. The **GS** category includes various GeoServer-specific operations for interacting with and managing GeoServer resources, while the **Vec** category specializes in vector data processing, offering tools for analyzing and transforming vector geometries.

They accept four inputs for execution: **Text**, **Reference**, **Subprocess**, and **Vector layers**.

### TEXT
In this mode, you can use various standard formats supported by WPS. These formats are:
-	text/xml;subtype=wfs-collection
-	application/wfs-collection
-	application/zip
-	text/csv
-	application/json
-	application/vnd.google-earth.kml+xml

#### text/xml;subtype=wfs-collection
Using this format allows you to submit a collection of geometries directly from a WFS request to a WPS process in GeoServer. When you use a WFS-Collection as input, you reference a set of geometries that the WPS operation can manipulate directly.

Here's an example of how to use a **WFS collection 1.1** in a WPS request:

  ```xml
<wfs:FeatureCollection xmlns:wfs="http://www.opengis.net/wfs" xmlns:feature="http://www.openplans.org/topp" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" xmlns:ows="http://www.opengis.net/ows" xmlns:xlink="http://www.w3.org/1999/xlink">
  <gml:boundedBy>
    <gml:Envelope srsDimension="2" srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">
      <gml:lowerCorner>147.291 -42.851002</gml:lowerCorner>
      <gml:upperCorner>147.291 -42.851002</gml:upperCorner>
    </gml:Envelope>
  </gml:boundedBy>
  <gml:featureMember>
    <feature:tasmania_cities gml:id="tasmania_cities.1">
      <gml:boundedBy>
        <gml:Envelope srsDimension="2" srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">
          <gml:lowerCorner>147.291 -42.851002</gml:lowerCorner>
          <gml:upperCorner>147.291 -42.851002</gml:upperCorner>
        </gml:Envelope>
      </gml:boundedBy>
      <feature:the_geom>
        <gml:Point srsDimension="2" srsName="http://www.opengis.net/gml/srs/epsg.xml#4326">
          <gml:pos>147.291 -42.851002</gml:pos>
        </gml:Point>
      </feature:the_geom>
      <feature:CITY_NAME>Hobart</feature:CITY_NAME>
      <feature:ADMIN_NAME>Tasmania</feature:ADMIN_NAME>
      <feature:CNTRY_NAME>Australia</feature:CNTRY_NAME>
      <feature:STATUS>Provincial capital</feature:STATUS>
      <feature:POP_CLASS>100,000 to 250,000</feature:POP_CLASS>
    </feature:tasmania_cities>
  </gml:featureMember>
</wfs:FeatureCollection>
  ```

#### application/vnd.google-earth.kml+xml
It is a MIME type used for representing geospatial data in the Keyhole Markup Language (KML) format which primarily associated with Google Earth and various mapping applications. KML enables the encoding of diverse geographic features, such as points, lines, and polygons, along with their associated attributes.

Here's an example of how to use an **application/vnd.google-earth.kml+xml** mime type in a WPS request:

  ```xml
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:ns2="http://www.google.com/kml/ext/2.2" xmlns:ns3="http://www.w3.org/2005/Atom" xmlns:ns4="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0">
      <Document>
          <Schema name="poi" id="poi">
              <SimpleField type="string" name="NAME"/>
          </Schema>
          <Folder>
              <name>poi</name>
              <Placemark id="poi.1">
                  <ExtendedData>
                      <SchemaData schemaUrl="#poi">
                          <SimpleData name="NAME">museam</SimpleData>
                      </SchemaData>
                  </ExtendedData>
                  <Point>
                      <coordinates>-74.01046109936333,40.707587626256554</coordinates>
                  </Point>
              </Placemark>
              <Placemark id="poi.2">
                  <ExtendedData>
                      <SchemaData schemaUrl="#poi">
                          <SimpleData name="NAME">stock</SimpleData>
                      </SchemaData>
                  </ExtendedData>
                  <Point>
                      <coordinates>-74.0108375113659,40.70754683896324</coordinates>
                  </Point>
              </Placemark>
              <Placemark id="poi.3">
                  <ExtendedData>
                      <SchemaData schemaUrl="#poi">
                          <SimpleData name="NAME">art</SimpleData>
                      </SchemaData>
                  </ExtendedData>
                  <Point>
                      <coordinates>-74.01053023879955,40.70938711687079</coordinates>
                  </Point>
              </Placemark>            
          </Folder>
      </Document>
  </kml>
  ```

### Vector Layer
This mode in GeoServer allows users to utilize predefined geographical data for advanced spatial analyses, including overlay analysis, buffering, and spatial querying. This access to well-organized data, such as points, lines, and polygons, significantly enhances analytical capabilities compared to relying solely on **JTS** or **Geo** categories.

By integrating vector layers into the WPS request builder, users can perform sophisticated geospatial analyses, enabling deeper insights from their datasets and making GeoServer a preferred choice for complex spatial processing tasks.

### OUTPUT
The **result** output typically provides a spatial data layer in various vector formats, including **GML**, **GeoJSON**, **CSV**, and **Shapefile**. This output can be further processed, visualized, or used in other spatial analyses, making it highly versatile for different applications.

When generating geometry, you can choose the result in a variety of standard data formats, including: 
-	text/xml;subtype=wfs-collection
-	application/wfs-collection
-	application/zip
-	text/csv
-	application/json
-	application/vnd.google-earth.kml+xml

This flexibility allows you to choose the most appropriate format for your specific use case or workflow, ensuring compatibility with your analysis tools and visualization platforms. By offering these multiple output formats, GeoServer effectively supports a wide range of geoprocessing needs, facilitating seamless integration and analysis of spatial data.

----

In this session, we discussed the types of different categories and various inputs in the WPS Request Builder. To access the full tutorial, click on this [link](https://www.youtube.com/watch?v=zfNJ9virFoQ&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).