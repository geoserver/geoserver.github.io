---
author: Nima Ghasemloo
layout: post
title: GeoServer Installation and Upgrade Guide on Windows
date: 2025-05-21
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

### GeoServer Installation and Upgrade Guide
In this session, we will install GeoServer on Windows using the Web Archive installation method and upgrade to a new version, while retaining existing data.

If you want to access the complete tutorial, click on the [link](https://www.youtube.com/watch?v=SpTdPIRxjU0&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).

[![](https://img.youtube.com/vi/SpTdPIRxjU0/0.jpg)](https://www.youtube.com/watch?v=SpTdPIRxjU0&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL)

## Introduction
GeoServer is a versatile, Java-based application compatible with various operating systems, provided a suitable Java Virtual Machine (JVM) is available. The latest versions of GeoServer have been tested with both Oracle JRE and OpenJDK.

The GeoServer WAR file is a platform-independent web archive designed for deployment on application servers. Apache Tomcat is the recommended servlet container due to its robust integration capabilities and comprehensive documentation. This setup allows multiple web applications to run concurrently, enabling GeoServer to operate alongside other Java-based services, enhancing server versatility.

**Note.** This guide outlines the installation of GeoServer 2.25.x using Java 17 and Apache Tomcat 9, followed by upgrade instructions. To ensure you have the latest release, please visit this [link](https://geoserver.org/download/) and avoid using older versions of GeoServer.

## Preparing for Installation
Before proceeding, follow the steps below:
- Backup the existing GeoServer folder (if upgrading).
   
  The folder ``webapps/geoserver/data`` is the data directory containing your configuration settings you wish to preserve. 
  
  The folder ``webapps/geoserver/WEB-INF/lib`` contains the deployed GeoServer web application, along with an extensions you have manually installed.
 
The folder ``webapps/geoserver/data`` is the data directory containing your configuration settings you wish to preserve. 
  
The folder ``webapps/geoserver/WEB-INF/lib`` contains the deployed GeoServer web application, along with an extensions you have manually installed.

- Check the **Modules** tab under the **Server Status** page to see all installed extensions.
- Uninstall previous versions of Java and Apache Tomcat.

### Installing Java Development Kit (JDK)
To download JDK 17, navigate to [adoptium.net](https://adoptium.net) and select:  
   - **Operating System:** Windows  
   - **Architecture:** x64  
   - **Package Type:** JDK  
   - **Version:** 17-LTS  

Download the `.msi` file and run it as an administrator. During installation, accept default settings and complete the setup.

## Installing Apache Tomcat
To download and install Apache Tomcat software, navigate to [tomcat.apache.org](https://tomcat.apache.org) and select **Tomcat 9** from the **Download** section.

Choose the **32-bit/64-bit Windows Service Installer** and run it as an administrator.

During setup:  
   - Configure the **ports** (default recommended).  
   - Set a **secure** username and password for administration (avoiding common defaults like `admin` or `tomcat`).  
   - The installer should auto-detect the installed JDK; if not, the user manually selects the Java installation path.   

To configure JVM memory allocation, navigate to `C:\Program Files\Apache Software Foundation\Tomcat 9.0\bin` and run **Tomcat9w.exe** as an administrator.

In the **Java** tab, the user sets:  
   - **Initial Memory Pool:** 512 MB
   - **Maximum Memory Pool:** 1024 MB
   - **Java Options**: As required for [running on Java 17](https://docs.geoserver.org/latest/en/user/production/java.html#running-on-java-17)
     
     ```
     --add-exports=java.desktop/sun.awt.image=ALL-UNNAMED
     --add-opens=java.base/java.lang=ALL-UNNAMED
     --add-opens=java.base/java.util=ALL-UNNAMED
     --add-opens=java.base/java.lang.reflect=ALL-UNNAMED
     --add-opens=java.base/java.text=ALL-UNNAMED
     --add-opens=java.desktop/java.awt.font=ALL-UNNAMED
     --add-opens=java.desktop/sun.awt.image=ALL-UNNAMED
     --add-opens=java.naming/com.sun.jndi.ldap=ALL-UNNAMED
     --add-opens=java.desktop/sun.java2d.pipe=ALL-UNNAMED
     ```
   - **Java Options**: As required for [running on Java 17](https://docs.geoserver.org/latest/en/user/production/java.html#running-on-java-17).
     
```
     --add-exports=java.desktop/sun.awt.image=ALL-UNNAMED
     --add-opens=java.base/java.lang=ALL-UNNAMED
     --add-opens=java.base/java.util=ALL-UNNAMED
     --add-opens=java.base/java.lang.reflect=ALL-UNNAMED
     --add-opens=java.base/java.text=ALL-UNNAMED
     --add-opens=java.desktop/java.awt.font=ALL-UNNAMED
     --add-opens=java.desktop/sun.awt.image=ALL-UNNAMED
     --add-opens=java.naming/com.sun.jndi.ldap=ALL-UNNAMED
     --add-opens=java.desktop/sun.java2d.pipe=ALL-UNNAMED
```
   
Switch to the **General** tab, and set **Startup Type** to **Automatic**, and start the Tomcat service.

## Deploying GeoServer
Download the latest **GeoServer WAR** file from [geoserver.org](https://geoserver.org).  

Extract the `.war` file and copy it to `C:\Program Files\Apache Software Foundation\Tomcat 9.0\webapps`.
  
To start GeoServer:  
   - Navigate `http://localhost:8080/manager`.  
   - Login with the Tomcat credentials.  
   - Click **Start** next to the GeoServer application.
   
The user accesses GeoServer at `http://localhost:8080/geoserver` and logs in using the default credentials:  
   - **Username:** admin  
   - **Password:** geoserver  

## Upgrading GeoServer
Stop GeoServer via the **Tomcat Manager App**, then replace the existing `webapps/geoserver/data` directory with the one from your backup.

Reinstall any **compatible extensions** for the new version, and restart GeoServer and verifies functionality.  

----

In this session, we took a brief journey to installation of GeoServer using the Web Archive method. If you want to access the complete tutorial, click on the  [link](https://www.youtube.com/watch?v=SpTdPIRxjU0&list=PL_ITaxp1Ob4sjk24Stboa5XbO0LGdEKbL).