---
author: GeoSpatial Techno
layout: post
title: How to style a layer using GeoServer and QGIS
date: 2024-03-29
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

### Using GeoServer and QGIS to style a layer
In this session, we will explore the "Capabilities of SLD" and "How to create styles" to produce beautiful maps. If you want to access the complete tutorial, simply click on the [link](https://youtu.be/9AUgLFS9CCY)

[![](https://img.youtube.com/vi/9AUgLFS9CCY/0.jpg)](https://www.youtube.com/watch?v=9AUgLFS9CCY)

## Introduction
Geospatial data has no intrinsic visual component and it must be styled to be visually represented on a map. GeoServer uses a markup language called Styled Layer Descriptor (SLD) to define styling rules for displaying data. SLD is an XML-based language that allows users and software to control the visual portrayal of geospatial data. This language ensures that clients and servers can both understand how to render the data visually.

**Note.** In this blog post, we used GeoServer version 2.20.0.

## Add a Style
To add a new style, navigate to the **Data > Styles** page, then click on the **Add a new style** link. You will be redirected to the new style page, which is the same as the Style Editor Data tab.

This tab includes basic style information, the ability to generate a style and legend details. It has some mandatory basic style information, such as:
- Name: It's the name of the style and it must be a unique name.
- Workspace: Styles can be inside workspaces which causes restrictions. In other words, the styles in a workspace can only be assigned to the services of that, and other services outside it, cannot use these styles. Styles also can be "global" or no workspace, so they don't have any restrictions and services can be used for all suitable styles.
- Format: Default options are **SLD** and **ZIP** formats. To use other formats such as **CSS** and **YSLD**, you should download and install extensions. Make sure to match the version of the extension to the version of the GeoServer.

The "Style Content" area provides options for creating, copying, or uploading a style. It has three options:
- Generate a default style: Choose a generic style based on geometry such as Point, Line, Polygon, Raster, or Generic and click the **Generate** link when selected.
- Copy from existing style: Select an existing style from GeoServer and copy its contents to the current style. Note that not all styles may be compatible with all layers. Click the **Copy** link when selected.
- Upload a style file: Press the **Browse** button to locate and select a plain text file from your local system to add as the style. Click on the **Upload** link to add the style file.

The **Legend** area allows you to preview the legend for the style. Click on the **Preview legend** link to generate a legend based on the current settings.

At the bottom of the Style Editor page, you'll find several options: **Validate**, **Apply**, **Save** and **Cancel**. During editing and especially after editing is complete, you can check the validation of the syntax by pressing the **Validate** button at the bottom. If any validation errors are found, a red message is displayed, and if no errors are found, a green message is displayed. To make changes, press the **Apply** button to access all the tabs and finally press the **Save** button.

After having created the style, it's time to apply it to the layer. To do it, follow these steps:
- Navigate to the **Data > Layers** page then click on the **layer's name** link to open the layer's properties form. Switch to the Publishing tab.
- Go to the **Style** section and from the **Default Style list**, select the suitable style, then press the **Save** button.
- Navigate to the **Data > Layer Preview ** page and open up OpenLayers preview for the layer.

## Edit a Style
On the Styles page, click on the style name to open the **Style Editor**. The Style Editor page presents the style definition and contains four tabs with many configuration options: **Data** , **Publishing** , **Layer Preview** and **Layer Attributes**.
- Data tab: The Data tab includes basic style information, the ability to generate a style, and legend details. Moreover, it allows for direct editing of style definitions at the bottom, with support for line numbering, automatic indentation, and real-time syntax highlighting. You can switch between tabs to create and edit styles easily and can adjust the font size of the editor.
- Publishing tab: This tab shows all layers available on the server, along with their default style and any additional styles they may have. You can easily see which layers are linked to the current style by checking a box in the table.
- Layer Preview tab: This tab enables you to preview and edit the current style of any layer without switching pages. You can easily select the desired layer to preview and fine-tune styles to continuously test visualization changes.
- Layer Attributes tab: The Layer Attributes tab shows a list of attributes for the selected layer, making it easy to see and work with the attributes associated with the layer. This can help in deciding which attribute to use for labeling or setting up scale-dependent rules. 

## Creating SLD styles by QGIS
QGIS has a style editor for map rendering with various possibilities, including the export of raster styles to SLD for use in GeoServer. For versions before 3.4.5, a plugin called **SLD4raster** is required for exporting SLD for use in GeoServer.

Here's a simple guide to styling a vector layer in GeoServer:
- Open QGIS (minimum version 3.0) and loading the vector dataset into your project.
- Double click on the layer to open the **Properties** dialog and navigate to the **Symbology** page.
- Select a **Graduated** rendering, choose the `desired` column, and press the **Classify** button.
- Return to the **Properties** dialog and go to the bottom of the Styles page. Select **Style > Save Style**.
- Save the style in SLD format and choose the `desired` location for the file.

- Go in GeoServer, create a new style and use the **Upload a new style dialog** to upload the exported file. Click on the **Upload** link.
- Press the **Validate** button to ensure there are no errors, then press the **Save** button.
- Switch to the **Publishing** tab and choose either **Default** or **Associated checkbox** to apply the new style to the `desired` layer.

Here is a step by step guide to style a raster layer for GeoServer:
- Begin by opening QGIS with a minimum version of 3.4.5.
- Load the raster layer into your project.
- Double click on the layer to access the **Properties** and go to the **Symbology** tab.
- Select **Singleband pseudocolor** as the Render type, choose **Linear method** for Interpolation, and select a desired Color ramp.
- Press the **Classify** button to create a new color classification, then press the **Apply** button to save this classification. At the bottom-left of the page, choose Style and press Save Style button.
- Choose a name and export it in SLD format to your preferred location.
- In GeoServer, navigate to the Style section and click on **Add a new style** to open the editor form.
- Use the **Choose File** button to locate your exported file in the folder and select it.
- Click on the **Upload** link to load the file into the editor form.
- Validate the style by pressing the **Validate** button to ensure there are no errors, then press the **Save** button.
- Navigate to **Data > Layers** page and open the layer's properties form by clicking on the layer's name. Switch to the Publishing tab.
- Set the style as Default Style and press the **Save** button.
- Finally, in the Layer Preview section, open the OpenLayers preview for the raster layer.

## Remove a Style
To remove a style, click on the checkbox next to the style. Multiple styles can be selected at the same time. Press the **Remove selected style(s)** button at the top of the page. You will be asked for confirmation and press the **OK** button to remove the selected style(s).