---
author: GeoSpatial Techno
layout: post
title: GeoServer About & Status - A Practical Guide
date: 2024-01-17
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

### GeoServer About & Status along with practical guides
In this session, we would like to talk around the "About & Status" section of GeoServer. If you want to access the complete tutorial, simply click on the [link](https://youtu.be/F-RlvlwwJgQ)

[![](https://img.youtube.com/vi/F-RlvlwwJgQ/0.jpg)](https://www.youtube.com/watch?v=F-RlvlwwJgQ)

### Introduction
The "About & Status" section of GeoServer provides information about runtime variables and how GeoServer is described to clients that connect to it. In other words, this section provides access to GeoServer diagnostic and configuration tools and can be particularly useful for debugging.
- "Server Status": view server configuration and run-time status.
- "GeoServer Logs": see GeoServer log output for error diagnosis.
- "Contact Information": manage public contact details for WMS server.
- "About GeoServer": access GeoServer docs, homepage, and bug tracker. You do not need to be logged into GeoServer to access this page.

### Server Status
The "Server Status" page, gives you a summarized overview of the main configuration parameters and information about the current state of the GeoServer. It has three tabs:
- The "Status" tab, provides a summary of server configuration parameters and run-time status.
- The "Modules" tab, provides the status of the various modules installed on the server.
- The "System Status" tab, provides extra information about the system environment GeoServer is running in.

#### Status Field Descriptions
This page describes the current status indicators:
- Data directory: It shows the path to the GeoServer data directory. The procedure for setting the location of the GeoServer data directory is dependent on the type of GeoServer installation. When running a GeoServer Web Archive inside a servlet container, the data directory can be specified in several ways. The recommended method is to set a servlet context parameter. To specify the data directory using a servlet context parameter, create the "context-param" element in the "WEB-INF/web.xml" file for the GeoServer application. After you change the path of the data directory, log in to GeoServer again. Now you can see the new path of the data directory.
- Locks: When using Transactional Web Feature Service (WFS-T), clients can edit feature types. To prevent data corruption, GeoServer locks the data during transactions. If the number is greater than one, there are active transactions. Clicking "Free Locks" resets a hung editing session and removes any abandoned locks.
- Connections: This shows you the number of vector data store connections. Vector data stores are repositories configured for the persistence of features.
- Memory Usage: This shows you how much memory GeoServer is using. You can manually run the garbage collector by clicking the Free Memory button, so it cleans up memory marked for deletion.
- JVM Version: This is the version of the "Java Virtual Machine" that the GeoServer is using.
- Java Rendering Engine: It shows the rendering engine used for vector operations.
- Available Fonts: This is a list of the fonts seen by the GeoServer. Fonts are useful to render labels for spatial features. Selecting the link will show the full list. To add custom fonts to the GeoServer, first, you have to download your favorite fonts from the web, then copy them to the "Java installation folder\jre\lib\fonts". After restarting the Apache Tomcat software, the new fonts will be added to the Available Fonts list.

In programming, to improve the speed and performance of the program, each of the various tasks and parts of the application can be assigned to a thread. The Thread Pool template helps conserve resources in a multithread application and also places parallel computations in a specific predefined framework. When using the Thread Pool, we can perform concurrent tasks in parallel form. Here are the titles of GeoServer’s ThreadPoolExecutor parameters: ThreadPoolExecutor Core Pool Size , ThreadPoolExecutor Max Pool Size , ThreadPoolExecutor Keep Alive Time(ms)
- Update Sequence: This option shows you how many times the server configuration has been updated.
- Resource cache: GeoServer does not cache data, but it does cache connection to stores, feature type definitions, external graphics, font definitions, and CRS definitions as well. The "Clear" button forces those caches to empty and makes GeoServer reopen the stores and re-read image and font information, as well as the custom CRS definitions stored in:
${GEOSERVER_DATA_DIR}/user_projections/epsg.properties
- Configuration and catalog: This option is very useful to update the configuration without having to restart the service. If the configuration on the disk becomes outdated due to external changes, you can refresh it by loading the latest data from the disk.

#### Module Field Descriptions
In GeoServer, a module can fall into one of three classes:
- Core, those modules that are visible by default in the Modules tab that GeoServer requires to function and are distributed with the main GeoServer distribution.
- Extension, those modules that add functionality to GeoServer. They are installed as add-ons to the base GeoServer installation. After you download and install these extensions, they are added to the Geoserver modules list. For example WPS extension
- Community, those modules that are generally considered experimental and are often under development. For that reason, Unlike the official extensions, these modules are not released and stored on SourceForge when an official GeoServer release is produced.

Every module added to GeoServer has its origin as a community module. If the module becomes stable enough it will eventually become part of the main GeoServer distribution either as a core module or as an extension.

#### System Status Field Descriptions
System Status adds some extra information about the system in the GeoServer status page in a tab named System Status and makes that info queryable through the GeoServer REST interface. This info should allow an administrator to get a quick understanding of the status of the GeoServer instance. If the System status tab is not present, it means that the plugin was not installed correctly. The System status tab content will be refreshed automatically every second.

### GeoServer Logs
The "GeoServer Logs" page, lets you read the messages, warnings, and errors contained in the log file. According to the current logging settings, you can find more information about the requests clients send to GeoServer and how it processes them. You can only read the last 1,000 lines by default from the console. You can also change this setting, but if you need to access the entire log content, we would strongly suggest accessing it with a text editor.

You can use the "Download the full log file" link placed just under the text console, or access the log file directly from this path: "geoserver_data_dir/logs/geoserver.log"

### Contact Information
The "Contact Information" page, is used in the Capabilities document of the WMS server and is publicly accessible. GeoServer provides an item to describe this information and metadata in different languages. By default, it's disabled and can be enabled from the i18n checkbox. You can complete this form with the relevant information and press the Save button to save your information.

### About GeoServer
The "About GeoServer" section, provides a brief description of geoserver and build information such as GeoServer Version, Git Revision, Build Date, GeoTools Version, and GeoWebCache Version. Also, this section provides links to the GeoServer Documentation, Wiki, and Issue Tracker. Remember that, You do not need to be logged into GeoServer to access this page.