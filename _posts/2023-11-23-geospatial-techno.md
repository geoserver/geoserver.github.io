---
author: GeoSpatial Techno
layout: post
title: GeoServer installation methods on Windows
date: 2023-11-30
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

### GeoServer installation methods: “Windows Installer” and “Web Archive”
GeoServer installation methods: “Windows Installer” and “Web Archive”
In this session, we will talk about how to install GeoServer software by two common methods in Windows. If you want to access the complete tutorial, simply click on the [link](https://youtu.be/G47vV2od4yc).

[![](https://img.youtube.com/vi/G47vV2od4yc/0.jpg)](https://www.youtube.com/watch?v=G47vV2od4yc)

### Introduction
GeoServer can be installed on different operating systems, since it's a Java based application. You can run it on any kind of operating system for which exists a Java virtual machine. GeoServer’s speed depends a lot on the chosen Java Runtime Environment (JRE). The latest versions of GeoServer are tested with both OracleJRE and OpenJDK. These versions are:
- Java 17 for GeoServer 2.23 and above
- Java 11 for GeoServer 2.15 and above
- Java 8 for GeoServer 2.9 to GeoServer 2.22
- Java 7 for GeoServer 2.6 to GeoServer 2.8
- Java 6 for GeoServer 2.3 to GeoServer 2.5
- Java 5 for GeoServer 2.2 and earlier

But remember that the older versions are unsupported and won't receive fixes nor security updates, and contain well-known security vulnerabilities that have not been patched, so use at own risk. That is true for both GeoServer and Java itself.

There are many ways to install GeoServer on your system. This tutorial will cover the two most commonly used installation methods on Windows.
- Windows Installer
- Web Archive

### Windows installer
The Windows installer provides an easy way to set up GeoServer on your system, as it requires no configuration files to be edited or command line settings.

#### Installation
- GeoServer requires a Java environment (JRE) to be installed on your system, available from [Adoptium](https://adoptium.net) for Windows Installer, or provided by your OS distribution. For more information, please refer to this link: https://docs.geoserver.org/latest/en/user/installation/index.html#installation

Consider the operating system architecture and memory requirements when selecting a JRE installer. 32-bit Java version is restricted to 2 GB memory, while the 64-bit version is recommended for optimal server memory. Utilizing JAI with the 32-bit JRE can enhance performance for WMS output generation and raster operations.
- Install JRE by following the default settings and successfully complete the installation.
- Navigate to the GeoServer.org and download the desired version of GeoServer.
- Launch the GeoServer installer and agree to the license.
- Enter the path to the JRE installation and proceed with the installation. The installer will attempt to automatically populate this box with a JRE if it is found, but otherwise you will have to enter this path manually.
- Provide necessary details like the GeoServer data directory, administration credentials, and port configuration.
- Review the selections, install GeoServer, and start it either manually or as a service.
- Finally, navigate to localhost:8080/geoserver (or wherever you installed GeoServer) to access the GeoServer Web administration interface.

#### Uninstallation
GeoServer can be uninstalled in two ways:
- By running the uninstall.exe file in the directory where GeoServer was installed
- By standard Windows program removal

### Web Archive
GeoServer is packaged as a web-archive (WAR) for use with an application server such as Apache Tomcat or Jetty. It has been mostly tested using Tomcat, and so is the recommended application server. There are reasons for installing it such as it is widely used, well-documented, and relatively simple to configure. GeoServer requires a newer version of Tomcat (7.0.65 or later) that implements Servlet 3 and annotation processing. Other application servers have been known to work, but are not guaranteed.

#### Installation
- Make sure you have a JRE installed on your system, then download Apache Tomcat from its website(https://tomcat.apache.org). For the Windows installation package, scroll down and choose the 32bit/64bit Windows Service Installer option.
- Configure Tomcat by selecting components, setting up a username and password, and specifying memory settings. So, before start the Tomcat service, you have to configure the memory settings that will use for Java VM. To do it, open the Tomcat9w from the bin folder, then click on the Java tab. This tab allows for configuration of memory settings, including initial and maximum memory pool sizes. Recommended values are 512MB for the initial memory pool and 1024MB for the maximum memory pool.
- Start Tomcat service and verify its functionality, then navigate to localhost:8080, and get the Tomcat9 web page.
- Navigate to the GeoServer.org and Download page. Select Web Archive on the download page from the version of GeoServer that you wish to download.
- Deploy the GeoServer web archive as you would normally. Often, all that is necessary is to copy the GeoServer.war file to the Tomcat’s webapps directory, then the application will be deployed automatically.
- Now to access the Web administration interface, open a browser and navigate to localhost:8080 and press Manager App button. Enter the username and password of apache tomcat. Click on the start button for the GeoServer. Once it has started, click the GeoServer link. This will take you to the GeoServer web page.

#### Uninstallation
Stop the container application. Remove the GeoServer webapp from the container application’s webapps directory. This will usually include the GeoServer.war file as well as a GeoServer directory.

### Difference between GEOSERVER.war and GEOSERVER.exe?
- The 'GeoServer.exe' NSIS installer registers GeoServer as a Windows Service, which uses the Jetty application server to run GeoServer. The 'GeoServer.war' is a platform independent web-archive package to be deployed in your own application server (we recommend Apache Tomcat.)

Using the 'GeoServer.exe' installer is a reliable way to setup GeoServer as a windows background service. The downside is the included Jetty application server is managed using text files (jetty.ini) once installed.
- Use of 'GeoServer.war' web-archive is provided to install into your own application server (we recommend Apache Tomcat as the market leader, with excellent documentation and integration options). A single application server may support several web application allowing GeoServer to be run alongside your own java web application.