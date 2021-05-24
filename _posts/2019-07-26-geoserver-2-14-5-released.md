---
author: iant
comments: false
date: 2019-07-26 14:17:43+00:00
layout: post
link: http://blog.geoserver.org/2019/07/26/geoserver-2-14-5-released/
slug: geoserver-2-14-5-released
title: GeoServer-2.14.5 released
wordpress_id: 3031
categories:
- Announcements
tags:
- Release
release: release_214_war
version: 2.14.5
jira_version: 16759
---




We pleased to share the [GeoServer 2.14.5](http://geoserver.org/release/2.14.5/) maintenance release. Downloads are provided ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.5/geoserver-2.14.5-bin.zip/download)|[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.5/geoserver-2.14.5-war.zip/download)) along with docs ([html](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.5/geoserver-2.14.5-htmldoc.zip/download)|[pdf](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.5/geoserver-2.14.5-user-manual.pdf/download)) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.4/extensions/).







This is a maintenance release of the GeoServer 2.14 series and is a recommended update for existing installations.







A large number of individuals contributed to this release, with efforts primarily focused on the setup of a new build box for the team. Thanks to Torben, Tom, Andrea and Jody for their work restoring the build server. Some activities (windows installer, CITE testing) are still available to work on.







This release is made in conjunction with GeoTools 20.5 and GeoWebCache 1.14.5.  For more information please see GeoServer release notes ([2.14.5](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16759) |[2.14.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16755)|[2.14.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16748) | [2.14.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16744) | [2.14.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16739)|[2.14.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16734)|[2.14-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16718)).





<!-- more -->





### Improvements and Fixes







This release a few improvements and several bug fixes:







* Upgrade Jetty to 9.4.18.v20190429
* That GeoTIFF sources configured with earlier versions of GeoServer 2.14.x might not work in 2.15.x is now fixed in this version.





* Many dependencies have been updated, along with small bug fixes as described in the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16755).






### About GeoServer 2.14 series

Additional information on the GeoServer 2.14 series:

* New [MongoDB extension](https://docs.geoserver.org/latest/en/user/extensions/mongodb/index.html) added
* Style editor improvements including [side by side editing](https://docs.geoserver.org/latest/en/user/styling/webadmin/index.html#style-editor-full-screen-side-by-side-mode)
* Nearest match support for [WMS dimension handling](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#edit-layer-dimensions)
* Upgrade notes documenting [REST API feature type definition change](https://docs.geoserver.org/stable/en/user/installation/upgrade.html#jts-type-bindings-geoserver-2-14-and-newer)  

* [State of GeoServer 2.14](https://www.slideshare.net/jgarnett/state-of-geoserver-214) (SlideShare)  

* [GeoServer Ecosystem](https://www.slideshare.net/jgarnett/geoserver-ecosystem-2018) (SlideShare)  

* [GeoServer Developers Workshop](https://www.slideshare.net/jgarnett/geoserver-developers-workshop) (SlideShare)


