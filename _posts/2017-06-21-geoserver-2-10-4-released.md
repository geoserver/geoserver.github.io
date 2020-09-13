---
author: tbarsballe
comments: false
date: 2017-06-21 23:40:51+00:00
layout: post
link: http://blog.geoserver.org/2017/06/21/geoserver-2-10-4-released/
slug: geoserver-2-10-4-released
title: GeoServer 2.10.4 Released
wordpress_id: 2881
---

We are pleased to announce the release of [GeoServer 2.10.4](http://geoserver.org/release/2.10.4/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10.4/geoserver-2.10.4-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10.4/geoserver-2.10.4-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10.4/geoserver-2.10.4.dmg/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.10.4/geoserver-2.10.4.exe/download)) along with documentation and extensions.

This is a maintenance release of GeoServer suitable for production systems. Maintenance releases are focused on bug fixes and stability, rather than new features. This release is made in conjunction with GeoTools 16.4 and GeoWebCache 1.10.3.

This release is made by Torben Barsballe and Kevin Smith from the Boundless team. Special thanks to Nick Stires from Boundless and the Frank Warmerdam from OSGeo for their help setting up the new [build.geoserver.org](https://build.geoserver.org/view/geoserver/) server used for this release. We would like to thank these volunteers and everyone who contributed features, fixes and time during the release process.


## Security Considerations


The 2.10.3 release addressed three security vulnerabilities. Details of these vulnerabilities were not included in the 2.10.3 blog post to provide time for the fixes to be included in 2.11.1, and have been replicated here:



 	
  * Added a [configurable delay](http://docs.geoserver.org/latest/en/user/security/webadmin/auth.html#brute-force-attack-prevention) during login, to mitigate a brute force attack.

 	
  * Added a [configurable parameter](http://docs.geoserver.org/latest/en/user/production/config.html#x-frame-options-policy) to control clickjacking attacks against the GeoServer UI.

 	
  * Added an additional parameter for locking down password autocomplete in the GeoServer UI


Thanks to Andrea Aime and Devon Tucker for providing fixes to these issues.

If you wish to report a security vulnerability, please visit our website for [instructions on responsible reporting](http://geoserver.org/issues/).


## New Features and Improvements





 	
  * Add rest endpoint for geofence admin rules

 	
  * Add REST endpoint for a user to change their password

 	
  * Allow disabling usage of SLD and SLD_BODY in WMS requests (also for virtual services)




## Bug Fixes





 	
  * Native JAI installation instructions report incorrect information about the installers

 	
  * Downloading zip file using /rest/workspaces/<ws>/datastores/<ds>/file.shp doesn't work after GeoServer reload

 	
  * Virtual services do not play nice with GML 3 encoding

 	
  * Namespace filtering on capabilties returns all layer groups (including the ones in other workspaces)

 	
  * Cascaded WMS does not encrypt configuration password

 	
  * Reloading GeoServer re-enables all disabled WMTS services

 	
  * Slow WFS GetFeature when using a 3D bbox POST request

 	
  * WMS cascading fails with NPE when advanced projection handling gets disabled

 	
  * Style Editor Preview Legend Fails on non-SLD Styles

 	
  * Exception when saving a layer group in GeoServer UI

 	
  * JMS fails to handle styles workspaces changes

 	
  * WFS-T Insert FeatureIds being returned in incorrect order

 	
  * CSW get capabilities ingore virtual services settings and always use the global service ones

 	
  * Integrated GWC does not work with layer and layer group specific services


And more! For more information on this release check the release notes ( [2.10.4](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15100) | [2.10.3](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15201) | [2.10.2](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=14800) | [2.10.1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=14500) | [2.10.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=14401&styleName=&projectId=10000) | [2.10-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=14202) | [2.10-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=13902&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) | [2.10-M0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=13102&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) )


## About GeoServer 2.10


Articles, docs, blog posts and presentations:



 	
  * The YSLD extension added, with extensive [documentation](http://docs.geoserver.org/latest/en/user/styling/ysld/index.html) (user guide)

 	
  * [State of GeoServer 2016](http://www.slideshare.net/jgarnett/state-of-geoserver) (slideshare)

 	
  * The [style editor](http://docs.geoserver.org/latest/en/user/styling/webadmin/index.html#style-editor) has been refreshed with the best ideas from the css extension (user guide)

 	
  * The [styling workshop](http://docs.geoserver.org/latest/en/user/styling/workshop/index.html) has been updated for foss4g 2016 and now includes both CSS and YSLD examples (user guide)

 	
  * [Smart transparency in GeoServer with image/vnd.jpeg-png format](http://www.geo-solutions.it/blog/geoserver-smart-transparency/) (GeoSolutions)

 	
  * [QGIS SLD export improvements](http://www.geo-solutions.it/blog/qgis-sld-export/) (GeoSolutions)


Community modules

 	
  * A new community module to [backup/restore](http://docs.geoserver.org/latest/en/user/community/backuprestore/index.html) and restore GeoServer configuration

 	
  * A resource browser is available allowing remote management of styles, icons and fonts (needs building from sources).

 	
  * A new [WMTS multidimensional domain discovery](http://demo.geo-solutions.it/share/wmts-multidim/wmts_multidim_geosolutions.html) community module for discovering patches of data in scattered data sets


