---
author: GeoSpatial Techno
layout: post
title: A Comprehensive Guide to Publishing a Shapefile in GeoServer
date: 2024-02-01
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

### A Comprehensive Guide to publishing a Shapefile in GeoServer
In this session, we want to talk about "How to Publish Shapefile in GeoServer" comprehensively. If you want to access the complete tutorial, simply click on the [link](https://youtu.be/1uDbddWqMvI)

[![](https://img.youtube.com/vi/1uDbddWqMvI/0.jpg)](https://www.youtube.com/watch?v=1uDbddWqMvI)

## Introduction
The **Data** section contains configuration options for all the different data-related settings that GeoServer uses to access and publish geospatial information. It also describes how to load, manage, and publish data in the GeoServer web interface. Each section contains the specific pages that provide add, view, edit, and delete capabilities.

**Note.** In this blog post, we used GeoServer version 2.20.0.

## Workspaces
A Workspace serves as a means to group and organize similar layers together. It enables you to associate multiple layers and stores with a single workspace. Each workspace can be managed independently, with its own security policies, data administrator, and web services. Generally, a workspace is created for each project, along with its corresponding stores and layers.

#### Add a workspace
To create a new workspace, navigate to **Data > Workspaces** page. Click on the **Add new workspace**, then you have to enter a `Workspace Name` and `Namespace URI`.
- Workspace Name: It is an identifier describing your project. It must not exceed ten characters or contain spaces (due to use as an XML "prefix" when downloading content).
- Namespace URI: URI stands for Uniform Resource Identifier, is a formal system for uniquely identifying resources, and consists of two types: **URL** and **URN**. A Namespace URI does not need to point to an actual location on the web and only needs to be a unique identifier.
- Default Workspace: This setting is useful when you only have one workspace defined. The setting allows users to communicate with the web service using just the layer name (rather than prefix:layer name required when managing hundreds of workspaces). select the **Default Workspace** checkbox to assign this as your default workspace.
- Sometimes the same feature type needs to be published multiple times with a different mapping and with the same name. This can be done in GeoServer using **Isolated  Workspaces** functionality.

Press the **Submit** button to save your new workspace.

#### Edit a workspace
To view or edit a workspace, click on the **Workspace name**, then a workspace configuration page will be displayed.
- For Settings, select the **Enabled** checkbox to customize the settings and contact details for the workspace level. This allows you to define an introduction to your workspace, and override the global settings for your workspace.
- Use the checkbox located next to each service to override the Global Settings for the associated service. Once enabled, clicking on the **Services** link will open the settings page for the service, allowing default values for the service title, abstract, and other details to be supplied.
- The Security tab allows to set data access rules at the workspace level. To create/edit the workspace's data access rules, check/uncheck checkboxes according to the desired role.

#### Remove a workspace
To remove a workspace, select it by clicking the checkbox next to the workspace. Multiple workspaces can be selected, or all can be selected by clicking the checkbox in the header. Click the **Remove selected workspace(s)** link. Now you will be asked to confirm or cancel the removal. 

Pressing **OK** removes the selected workspace(s).

## Stores
The Stores manage the connection parameters between GeoServer and the data sources where your spatial data reside. They provide a mechanism for GeoServer to connect to various data repositories, including file systems, databases, and cloud storage services. Each store represents a unique data source and has its configuration settings.

#### Add a store
To add a Store, navigate to **Data > Stores** page. Click on **Add new store**, then you will be prompted to choose a data source. GeoServer supports several different data formats, but they are classified into three types: "Vector data", "Raster data", and "Cascaded Services".
- Vector data formats include Shapefile, GeoPackage, PostGIS, and Properties. The most common and widely used option is Shapefile.
- Raster data formats include ArcGrid, GeoPackage, GeoTIFF, ImageMosaic, and WorldImage. The most used and well-known are the GeoTIFF and the WorldImage. GeoTIFF is a spatial extension of the "TIFF" format and tags image files with geographic information. A WorldImage is similar, but georeferencing information is saved in an external text file.
- Cascaded Services include WFS, WMS, and WMTS. GeoServer can proxy a remote Web Map Service and Web Map Tile Service and load it as a store in GeoServer.

Other data sources are supplied as GeoServer extensions. Extensions are downloadable modules that add functionality to GeoServer. Click the appropriate data source to configure the store, because the connection parameters vary depending on data format.

To create a Shapefile data store, follow these steps:
- Select the desired workspace from the drop-down menu.
- Enter the `Data Source Name`. Make sure the "Enabled" checkbox is selected. Otherwise, access to the store along with all the datasets defined, will be disabled for it.
- In the "Shapefile location", click on the **Browse** link to define the location of the shapefile.
- The DBF file format has a field for character encoding, but it doesn't always accurately indicate the actual encoding used. As a result, it is important to specify the DBF character set correctly when decoding strings to ensure accurate interpretation of the data.

When finished, press the **Save** button. Now it will automatically redirect to the **Add New Layer** page, which will be completely described in the Layer section. Next, we will explain how to edit and remove the store.

#### Edit a store
To view or edit a store, click on the **Store name**. A Store configuration page will be displayed. The exact contents of this page depend on the specific format of the Store. After your configuration is modified, press the **Save** button.

#### Remove a store
To remove a Store, click the checkbox next to the store. Multiple stores can be selected, or all can be selected by clicking the checkbox in the header. Click the **Remove selected stores**. You will be asked to confirm the removal of the configuration for the store(s) and all resources defined under them.

Pressing **OK** removes the selected Store(s), and returns to the Stores page.

## Layers
From the administration interface, navigate to the **Data > Layers** page. 
On this page, you can view and edit existing layers, add a new layer, or remove a layer. It also shows you the type of layers in the Type column, with a different icon for vector and raster layers, according to the geometry shape. The Title, Workspace, and Store values of each layer are shown. 

#### Add a layer
Clicking the **Add a new layer**, brings up a New Layer Chooser panel. The menu displays all currently enabled stores. If you want to add a new layer for a published resource, click on **Publish Again**. Note that when republishing the name of the new layer may have to be modified to avoid conflict with an existing layer.

The beginning sections (Basic Resource Info, Keywords, and Metadata link) provide metadata, specifically textual information that makes the layer data easier to understand and work with. The metadata information will appear in the capabilities documents which refer to the layer. These options are:
- Name: The identifier used to reference the layer in WMS requests that are filled automatically. Note that for a new layer for an already-published resource, the name must be changed to avoid conflict.
- Enabled: A layer that is not enabled won’t be available to any kind of request, it will just show up in the configuration and in REST config.
- Advertised: A layer is advertised by default. A non-advertised layer will be available in all data access requests (for example, WMS GetMap, WMS GetFeature) but won't appear in any capabilities document or the layer preview.
- Title: The human-readable description to briefly identify the layer to clients that filled automatically. GeoServer provides an item for the title and abstract and describes how to specify metadata in different languages. By default, it's disabled and can be enabled from the i18n checkbox.
- Abstract: It describes the layer in detail.
- Keywords: List of short words associated with the layer to assist catalog searching. To add a new keyword, enter your keyword, then press the **Add Keyword** button to add it.
- Metadata & Data Links: It allows linking to external documents that describe the data layer. The `Type` input provides a few example types, like FGDC or ISO19115, but allows any other type to be declared. `Format` provides its mime type, while `URL` points to the actual metadata.

A Coordinate Reference System (CRS) defines how georeferenced spatial data relates to real locations on the Earth's surface. GeoServer needs to know the CRS of your data. This information is used for computing the latitude/longitude bounding box and reprojecting the data during both WMS and WFS requests.

- Native SRS: Specifies the coordinate system the layer is stored in. Clicking the projection link displays a description of the SRS.
- Declared SRS: Specifies the coordinate system GeoServer publishes to clients.
- SRS Handling: Determines how GeoServer should handle projection when the two SRSes differ. Possible values are:
  - Force declared: This is the default option and normally the best course of action. Use this option when the source has no native CRS, has a wrong one, or has one matching the EPSG code.
  - Reproject from native: This setting should be used when the native data set has a CRS that does not match any official EPSG. E.g. `Lambert Conformal Conic to WGS84`.
  - Keep native: This is a setting that should be used in very rare cases. Keeping native means using the declared one in the capabilities documents, but then using the native CRS in all other requests.

The **Bounding Box** determines the extent of the data within a layer. It includes two items: "Native Bounding Box" and "Lat/Lon Bounding Box". Generate the bounds for the layer by pressing the **Compute from data** and **Compute from native bounds** button in the Bounding Boxes section.

Vector layers have a list of the "Feature Type Details". These include the `Property` and `Type` of a data source. Remember that, if you want to change your data by ArcGIS or QGIS, like add or remove features or fields, or edit the attribute table contents, there is no need to create a layer again in the GeoServer, just press the **Reload feature type**, so your layer will be updated.

Remember that GeoServer, by default, publishes all the features that are currently available in the layer. However, if you wish to limit the features to a specific subset, you can achieve this by specifying a CQL filter in the configuration. Upon completing the layer configuration, finalize the process by pressing the **Save** button. This action will create the layer based on the specifications you have provided.

#### Edit a layer
To view or edit a layer, click on the **Layer Name** from the **Layer** page. A layer configuration page will be displayed. After your configuration is modified, press the **Save** button.

#### Remove a layer
To remove a layer, select the checkbox next to the layer. Multiple layers can be selected, or all can be selected by clicking the checkbox in the header. By clicking the **Remove selected layers** link, you will be asked to confirm the removal of the configuration for the layer(s) and all resources defined under them.

Press **OK** removes the selected layer(s), and returns to the Layers page.