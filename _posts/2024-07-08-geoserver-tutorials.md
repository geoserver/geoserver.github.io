---
author: Nima Ghasemloo
layout: post
title: Utilizing the Demo Section in Geoserver
date: 2024-07-08
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

### Utilizing the Demo Section in Geoserver
In this session we aim to provide content on how to use the **Demo menu and its modules in GeoServer** and teach the process of making different requests and getting responses from the server. If you want to access the complete tutorial, simply click on the [link](https://youtu.be/3xKKI8irlQk).

[![](https://img.youtube.com/vi/3xKKI8irlQk/0.jpg)](https://www.youtube.com/watch?v=3xKKI8irlQk)

## Introduction
The Demo page provides valuable tool to help you practice with requests and understand how GeoServer works. The **Demo Requests** is used to create and test requests to GeoServer. The user can see the response to successful requests, or troubleshoot problems. To become familiar with the demo page, navigate to **Demos** to open the **GeoServer Demos** page. This page contains these options:
- Demo Requests
- SRS List
- Reprojection Console
- WCS Request Builder.

If you have installed the WPS extension, you will see an additional option called WPS Request Builder. 

**Note.** These tools are for the public like **Layer Preview**, you do not need to be logged into GeoServer to access this page.

**Note.** This video was recorded on GeoServer 2.22.4, which is not the most up-to-date version. Currently, versions 2.24.x and 2.25.x are supported. To ensure you have the latest release, please visit this [link](https://geoserver.org). and avoid using older versions of GeoServer.

## Demo Request
This page has examples of WMS, WCS, and WFS requests for GeoServer that you can use to examine and change. To learn about WMS, WFS, and WCS standards, simply click on the [link](https://youtu.be/SYamRAKEj5E).

Now let's explore some basic operations:
- From the drop-down list, you can select a set of prepared requests. They are listed with a syntax declaring the standard as a prefix and the standard's version as a suffix. Choose WFS_getCapabilities-1.1.xml.
- Press the Submit button. A new panel is shown, and, after a while, it lists the XML response from GeoServer.
- Another basic WFS operation is getFeature, which will retrieve a feature for you. Select WFS_getFeature-1.0.xml. If you look at the XML code, you can see a clear reference to the topp:states layer, which is included in the sample set.
- Press the Submit button. A new panel is shown, and, after a while, it lists the XML response from GeoServer. The code is a GML representation of the features with `fid = 3`, as requested in the filter.

The Demo requests interface lets you select sample requests and modify them to perform testing on GeoServer. When in doubt about a specific operation, this application should be the first point where you go to debug. From here, you can concentrate on the request's syntax, avoiding network issues or other problems that you may have experienced with an external client.

**New Feature:** For GeoServer 2.25.2 the Demo Request page has been improved to show response Headers, and provide the option to pretty print XML output.

### SRS List
GeoServer natively supports almost 4000 Spatial Referencing Systems (SRS), also known as projections, and more can be added. A spatial reference system defines an ellipsoid, a datum using that ellipsoid, and either a geocentric, geographic or projection coordinate system. This page lists all SRS info known to GeoServer.

The Code column refers to the unique integer identifier of that spatial reference system. Each code is linked to a more detailed description page, accessed by clicking on that code. Now let's filter the projection list:
- In the Search textbox, type in the project code for the basic projection, 4326 or WGS 84; then press Enter.
- Click on the projection code to show the projection details that include: 
  -  A short text description of the SRS
  -  An EPSG or Internal description of the SRS, provides an overview of how each projection is defined. It includes several parameters formatted in the WKT format.
  -  And a map showing you the area of validity or bounding box for the SRS. For `4326`, it is the planet's surface.
- Repeat these steps to review another code `32633` which is the WGS 84, UTM zone 33N. Please consider the area of validity and the countries eligible to use this SRS.

### Reprojection console
The reprojection console allows you to calculate and quickly test coordinate transformation. You can use it to convert a single coordinate or WKT geometry and transform it from one CRS to another.
In this recipe, you'll discover a simple, yet very useful tool that ships with GeoServer. It lets you have a look at how coordinates change when you move data from one CRS to another.
- From the list, select the Reprojection console.
- Insert `EPSG:4326` in the Source CRS field and `EPSG:32632` in the Target CRS field. Then, enter the coordinates of the POINT in the Geometry of Source CRS field, similar to what you see on the video. In this example, we used the coordinates of the San Siro stadium in Milan.
- Click on the Forward Transformation link; GeoServer calculates the new coordinates for you and fills the Geometry of Target CRS textbox.
Use Forward transformation to convert from source CRS to target CRS, and Backward transformation to convert from target CRS to source CRS. You can also view the underlying calculation GeoServer is using to perform the transformation.

### WCS Request Builder
The WCS Request Builder is a tool for generating and executing WCS requests. Since WCS requests can be cumbersome to the author, this tool can make working with WCS much easier. To access the WCS Request Builder, Select WCS Request Builder from the list of demos. The WCS Request Builder consists of a form that can be used to generate several different types of requests. When first opened, the form is short, only including these options:
- WCS Version—Version of WCS to use when crafting the request.
- Coverage name—Coverage to use in the request.

**Note.** All other options displayed will be non-functional until Coverage name is selected. Once selected, the remainder of the form will be displayed. Watch the video for a full explanation of these options: 
- Spatial subset
- Coordinate reference system
- Specify source grid manually (1.0.0 only)
- Target coverage layout (1.1.1 only)
- Target CRS
- Output format

There is also a link for Describe coverage next to the Coverage name which will execute a WCS DescribeCoverage request for the particular layer. At the bottom of the form are two buttons for form submission:
- Get Coverage: It executes a GetCoverage request using the parameters in the form.
- Generate GetCoverage XML: Clicking this button generates the GetCoverage request based on the form parameters.

By using this generated XML code, you can easily construct and customize your GetCoverage requests with various parameters, making it easier to retrieve the desired coverage data from GeoServer. 

**New Feature:** For GeoServer 2.25.2 the WCS Request Builder has new option to open the generated request in the **Demo Request Builder**. This is very helpful allowing the response to be shown on the page, rather than downloaded in the browser.

## WPS Request Builder
GeoServer with the WPS extension installed includes a request builder for generating and executing WPS processes. Using this tool can greatly simplify the process of authoring WPS requests and making your work with WPS much more convenient and efficient. It's always nice to have assistance in tasks that can be complex or time-consuming. This tool can be a valuable asset in your WPS workflow.

In future sessions, we'll dive deep into the Web Processing Service or WPS and explore its functionalities and how to use different functions in detail. So get ready to expand your knowledge and learn how to leverage the power of WPS for your geospatial analysis needs!

**New Feature:** For GeoServer 2.25.2 the WPS Request Builder has the new option to open the generated request in the **Demo Request Builder**.

----

In this session, we took a brief journey through GeoServer Demo section. we have explored the Demo menu and its modules in GeoServer. If you want to access the complete tutorial, simply click on the [link](https://youtu.be/3xKKI8irlQk).

[![](https://img.youtube.com/vi/3xKKI8irlQk/0.jpg)](https://www.youtube.com/watch?v=3xKKI8irlQk)