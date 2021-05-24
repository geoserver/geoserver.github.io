---
author: jgarnett
comments: false
date: 2019-06-13 03:10:41+00:00
layout: post
link: http://blog.geoserver.org/2019/06/13/geoserver-2-14-4-released/
slug: geoserver-2-14-4-released
title: GeoServer 2.14.4 Released
wordpress_id: 3025
categories:
- Announcements
tags:
- Release
release: release_214_war
version: 2.14.4
jira_version: 16755
---




We pleased to share the [GeoServer 2.14.4](http://geoserver.org/release/2.14.4/) maintenance release. Downloads are provided ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.4/geoserver-2.14.4-bin.zip/download)|[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.4/geoserver-2.14.4-war.zip/download)) along with docs ([html](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.4/geoserver-2.14.4-htmldoc.zip/download)) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.14.4/extensions/).







This is a maintenance release of the GeoServer 2.14 series and is a recommended update for existing installations.







A large number of individuals contributed to this release, with efforts primarily focused on the setup of a new build box for the team. Thanks to Torben, Tom, Andrea and Jody for their work restoring the build server. Some activities (windows installer, pdf user guide, CITE testing) are still available to work on.







This release is made in conjunction with GeoTools 20.4 and GeoWebCache 1.14.4.  For more information please see GeoServer release notes ([2.14.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16755) |[2.14.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16748) | [2.14.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16744) | [2.14.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16739)|[2.14.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16734)|[2.14-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16718)).





<!-- more -->





### Improvements and Fixes







This release includes a number of new features and improvements:







  * Improvements to security integration with tiles seeding now working against secured layers, and WCS now supporting "challenge" mode
  * A subtle rendering fix when advanced projection handling is used to remove small vertical gaps in polygon output.
  * Improved rendering for followLine and maxAngleDelta support.
  * REST API now supports layer names that including dot character
  * Include coverage metadata in WCS 2.0.1 GetCapabilities and DescribeCoverage output. Similar improvements for for GetFeatureInfo access to coverage metadata.
  * WCS 1.0.0 support for elevation and custom dimensions
  * Default security configuration restricts WFS StoredQuery management operations to administrator access
  * Application schema has improved its support for xpath with the ability to support multiple matches
  * Style validation is better able to handle internationalization in descriptive text such as title and description
  * A small but important fix in how URL connection parameters are stored and transfered 
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


