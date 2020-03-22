---
author: bmmpxf
comments: true
date: 2009-06-12 15:34:26+00:00
layout: post
link: http://blog.geoserver.org/2009/06/12/new-windows-installer/
slug: new-windows-installer
title: New Windows Installer
wordpress_id: 223
categories:
- Announcements
tags:
- installer
- windows
---

_**Update:**  As of [GeoServer 2.0.1](http://geoserver.org/display/GEOS/GeoServer+2.0.1), the legacy installer has been merged into the new installer.  This means that during installation, you now have a choice on whether to install GeoServer as a Windows service or to run it manually._



* * *



GeoServer has provided a Windows installer for the past 4 years (since at least [version 1.2.4](http://geoserver.org/display/GEOS/GeoServer+1.2.4), if not before).  It has always been simple and functional, providing a modest wrapper for the Jetty container found in the [binary distribution](http://geoserver.org/display/GEOS/Stable).

However, there are a number of ways in which GeoServer works in this environment that could be more in the spirit of Windows.  So, with the release of [GeoServer 1.7.5](http://geoserver.org/display/GEOS/GeoServer+1.7.5), we have redesigned the way GeoServer integrates with Windows,  in the form of a [new installer](http://downloads.sourceforge.net/geoserver/geoserver-1.7.5-ng.exe).

This new installer offers a host of new user-friendly features.  First of all, GeoServer now shows up as a **Windows service**, in line with other server software such as [Apache HTTP Server](http://httpd.apache.org/) or [PostgreSQL](http://www.postgresql.org/) .  This alleviates the need to have a command line window persist on the desktop when running GeoServer.  Integration with Windows Services allows administrators the ability to automate the management of GeoServer, although starting and stopping GeoServer is also still possible from the Start Menu as before.

GeoServer now appears on the **Add/Remove Programs list**.  It was always possible to uninstall via the Start Menu, but the uninstall option is now in a place where more users will expect it to be.

The installer itself has been redesigned as well.  It now allows you to **link to an existing data directory** (if you have previously created one).  Also, it allows (and encourages) you to **change the username and password** for the web administration interface, a feature unique to this installer.  (In all other cases, it is necessary to edit the `users.properties` file.)

There are other some other user-friendly features added, such as the requirement (and check) for **administrator rights** to run the installer, to prevent errors during the install process.

Since this installer is very new and has not been tested on all platforms, we have included a link to the [legacy installer](http://downloads.sourceforge.net/geoserver/geoserver-1.7.5.exe) that functions just like previous versions.  But we encourage everyone to try out the [new installer](http://downloads.sourceforge.net/geoserver/geoserver-1.7.5-ng.exe) (and provide feedback on what works and what doesn't) so that we can make the experience better.  All in all, we feel that this is a marked improvement in the GeoServer Windows experience.  Enjoy.
