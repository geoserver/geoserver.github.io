---
author: GeoSpatial Techno
layout: post
title: How to Publish a GeoTIFF file in GeoServer
date: 2024-03-08
categories:   
- Tutorials
---

[GeoSpatial Techno](https://www.youtube.com/@geospatialtechno) is a startup focused on geospatial information that is providing e-learning courses to enhance the knowledge of geospatial information users, students, and other startups. The main approach of this startup is providing quality, valid specialized training in the field of geospatial information.

( [YouTube](https://www.youtube.com/@geospatialtechno)
| [LinkedIn](https://www.linkedin.com/in/geospatialtechno)
| [Facebook](https://www.facebook.com/geospatialtechno)
| [Reddit](https://www.reddit.com/user/geospatialtechno)
| [X](https://twitter.com/geospatialtechn)
)

----

### Publishing a GeoTIFF file in GeoServer
In this session, we want to talk about "How to Publish a GeoTIFF file in GeoServer" comprehensively. If you want to access the complete tutorial, simply click on the [link](https://youtu.be/X2W7kFSaHl4).

[![](https://img.youtube.com/vi/X2W7kFSaHl4/0.jpg)](https://www.youtube.com/watch?v=X2W7kFSaHl4)

## Introduction
The GeoTIFF is a widely used geospatial raster data format, it is composed of a single file containing both the data and the georeferencing information. By default, GeoTIFF will be an option in the Raster Data Sources list when creating a new data store.

**Note.** In this blog post, we used GeoServer version 2.20.0.

## Add a GeoTIFF data
To add a GeoTIFF data in GeoServer, follow these steps:
- Navigate to **Data > Stores** page, then click on the **Add new Store** link.
- Select the desired workspace from the drop-down menu.
- Enter the Data Source Name, make sure the Enabled option is checked. If checked, it enables the store. If unchecked (disabled), no data in the GeoTIFF will be served from GeoServer. 
- In the URL under the Connection Parameters, browse to the location of the GeoTIFF file then press the **Save** button.
- Now you will be redirected to the New Layer page automatically and to add a layer for an available resource click on the **Publish** link.
- Check the Name, Coordinate Reference Systems and the Bounding Boxes fields are properly set and press the **Save** button.

## Layer Groups
In Geoserver, a layer group serves as a convenient container for organizing layers and other layer groups in a structured hierarchy. By assigning a single layer to a layer group in WMS requests, the process of making requests is simplified as instead of specifying multiple individual layers, only one layer needs to be indicated. Furthermore, a layer group establishes a set order for the layers within it and enables the specification of alternative styles for the layers, distinct from their default settings.

## Add a Layer Group
- To create a Layer Groups, navigate to **Data > Stores** page. Click on **Add a new layer group** link. The initial fields allow you to configure the name, title, abstract and workspace of the layer group. Enter the `Data Source Name` and `Title`.

- The **Enabled** checkbox, if disabled, will cause the layer group to just show up at configuration time, while the **Advertised** checkbox, if unchecked, will make it to not be available in GetCapabilities request and in the layer preview. The behaviour of layer group regarding both checkboxes will not affect the behaviour of any of the layers being grouped, which will follow respectively that specified in the corresponding edit page.

  **Note.** In the layer group section, Workspace selection is optional.

- The **Bound** section contain the data BoundingBox of this layer group in the native coordinate reference system. The input can be done manually or automatically with the help of Generate Bounds.

  **Note.** By default, a layer group is queryable when at least a child layer is queryable. Uncheck **Queryable** box if you want to explicitly indicate that it is not queryable independently of how the child layers are configured.

- To add more layers to the Layer Group list, you can press the **Add Layer…** button at the top of the table. From the popup window, select the layer to be added by clicking the layer name. 

- A layer group can be added by pressing the **Add Layer Group…** button at the top of the table. From the list of layer groups, select the appropriate layer group's name.

- A style group is a style that has one or more Named Layers which reference layers that exist in the catalog. Style groups can be added to Layer Groups as an alternative way of defining a collection of styled layers. To add it, press the **Add Style Group…** button at the top of the table and from the popup window, select the style group to be added by clicking its name.

- Press the **generate bounds** button to have geoserver compute the group bounds from the layers inside of it.

  **Note**. A layer group can contain layers with dissimilar bounds and projections. GeoServer automatically reprojects all layers to the projection of the layer group.

- When a layer group is processed, the layers are rendered in the order provided, so the publishable elements at the bottom of list will be rendered last and will show on top of the others. A publishable element can be positioned higher or lower on this list by pressing the green up or down arrows, respectively, or can be simply dragged in the target position.

- Metadata links allows linking to external documents that describe the data of layer group. **Keywords** make possible to associate a layer group with some keywords that will be used to assist catalog searching.

- Press **Save**  button to create the new layer group.

## Preview a Layer Group
So in order to preview the created layer, navigate to the **Data > Layer Preview** page  and enter the name of your layer group in the search box, then press **Enter** button. Click on the **OpenLayers** link for a given layer and the view will display. An OpenLayers map loads in a new page and displays the group layer with the default styles. You can use the Preview Map to zoom and pan around the dataset, as well as display the attributes of features by click on each feature.

## Using WMS layers in QGIS
To display a WMS layer in QGIS software, follow these steps:
- Open GQIS and navigate to **Layer > Add Layer > Add WMS/WMTS Layer**.
- To create a new service connection, from the Layers tab, press **New** button.
- Name your connection from the Connection Details. Next, from the `URL` textbox, you need to access a WMS layer as HTTP address of Web Map Server. In this case, name the connection as `My Project` and the URL as  `http://localhost:8080/geoserver/project/wms` and press **OK**. Note that the "project" refers to the workspace defined in Geoserver.
- Press the **Connect** button to fetch the list of layers available, then press **Add** button and **Close**.
- Now, you will see the layer loaded in the QGIS canvas. You can zoom/pan around just like any other layer. The way WMS service works is that every time you zoom/pan, it sends your viewport coordinates to the server and the server creates an image for that viewport and return it to the client. So there will be some delay before you see the image for the area after you have zoomed in. Also, since the data you see is an image, there is no way to query for attributes like in a regular vector/imagery layer.