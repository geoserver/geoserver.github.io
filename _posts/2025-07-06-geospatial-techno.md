---
author: Milad Rafiei
layout: post
title: GeoServer WPS Extension Installation Guide
date: 2025-07-06
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

### GeoServer WPS Extension Installation Guide
This session covers the steps to install the WPS (Web Processing Service) extension in GeoServer, enabling advanced geospatial data processing capabilities through standardized web service operations.

If you want to access the complete tutorial, click on the [link](https://www.youtube.com/watch?v=WkLDwJ-5YOA&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).

[![](https://img.youtube.com/vi/WkLDwJ-5YOA/0.jpg)](https://www.youtube.com/watch?v=WkLDwJ-5YOA&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL)

## Introduction
GeoServer is a powerful open-source server application that enables users to publish geospatial data and interactive maps on the web. It supports a wide range of data formats and protocols, making it a flexible solution for managing and delivering geospatial content. One of its standout capabilities is functioning as a geoprocessing server.

Geoprocessing involves analyzing spatial data to derive insights and perform operations such as Buffer, Clip, Union, Contour, and more.
By default, GeoServer does not include Web Processing Service (WPS) functionality. However, WPS is available as an optional extension that's easy to install. Adding this extension unlocks advanced geospatial analysis and processing features directly within GeoServer. To get started, download the WPS extension ZIP file that matches your GeoServer version.

**Note**: This tutorial uses GeoServer version 2.25.3. Be sure to download the WPS extension that corresponds exactly to your GeoServer version—mismatched versions will result in errors.

## Installing the WPS Extension
Here are the steps to install the WPS extension in GeoServer:
-	Navigate to the [GeoServer](https://geoserver.org/) website and select the **download** link.
- Under the **Archive** tab, choose the version that matches your installed GeoServer.
-	Select the **WPS** option from the **Services** section. After a few seconds, the extension file will begin downloading automatically.

Prepare for Installation:
- It's recommended to stop GeoServer before installing any extensions. This will prevent any potential conflicts or problems during the installation process.
-	Unzip the downloaded WPS extension file.
- Copy all extracted `.jar` files directly into the `WEB-INF/lib` directory of your GeoServer installation. Ensure the extracted files are placed directly in this directory, avoiding subfolders.
-	Once the files are in place, restart GeoServer to ensure that the changes take effect. This activates the newly installed WPS extension.

## Verifying the WPS Extension Installation
Once GeoServer is running again, open the GeoServer web interface. From the **Server Status** section, click on the **Modules** tab to confirm that the WPS extension is in the list of installed modules.

Testing WPS Functionality:
- Navigate to the **Demos** section in the GeoServer interface.
- Select **WPS Request Builder** to access a tool for testing WPS processes.

- The **WPS Request Builder** consists of a drop-down list containing various processes. It supports many types of processes that are categorized based on prefixes. These prefixes are:
  -  **JTS**: Java Topology Suite
  -  **geo**: geometry processes
  -  **ras**: raster processes
  -  **vec**: Vector processes
  -  **gs**: GeoServer-specific processes

- The `geo` and `JTS` processes return text-based analysis results but do not support internal GeoServer layers as input.
- The `gs` and `vec` function groups support both text input and GeoServer layers or WFS layer URLs.
- For raster data analysis, use processes with the `Ras` prefix.

----

In this session, we took a brief look at how to install the WPS extension in GeoServer. To access the full tutorial, click on this [link](https://www.youtube.com/watch?v=WkLDwJ-5YOA&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).