---
author: tbarsballe
comments: false
date: 2018-02-22 00:45:28+00:00
layout: post
link: http://blog.geoserver.org/2018/02/22/geoserver-2-13-beta-released/
slug: geoserver-2-13-beta-released
title: GeoServer 2.13-beta released
wordpress_id: 2930
---

We are happy to announce the release of [GeoServer 2.13-beta](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13-beta/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13-beta/geoserver-2.13-beta-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13-beta/geoserver-2.13-beta-war.zip/download), and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13-beta/geoserver-2.13-beta.exe/download)) along with docs and extensions.

This is a beta release of GeoServer made in conjunction with GeoTools 19-beta.

We want to encourage people to test the release thoroughly and report back any issue found. With no further delay, let’s see what’s new, that is, what is there to test!


## Isolated Workspaces


The concept of an "Isolated Workspaces" has been added to GeoServer, to allow for reusing a namespace among multiple workspaces. In particular, an isolated workspace allows reuse of a namespace already used by another workspace, but its resources (layers, styles, etc ...) can only be retrieved when using that workspace's virtual services and will only show up in those virtual service capabilities documents.

When reusing a namespace among workspaces, exactly one of those must be non-isolated, and the rest must be isolated; i.e. isolated workspaces have no restrictions in namespaces usage but the existing restrictions still apply for non isolated workspaces.

This is particularly useful for those publishing complex schemas for INSPIRE compliance. For more details, refer to the [original proposal](https://github.com/geoserver/geoserver/wiki/GSIP-165---Add-isolated-workspaces-concept-to-GeoServer).


## GeoWebCache REST API


Two new endpoints have been added to the GeoWebCache REST API:



 	
  * /gwc/rest/blobstores:

 	
    * GET /gwc/rest/blobstores for a list of the blobstores

 	
    * GET /gwc/rest/blobstores/{blobStoreName} for details about a single blobstore

 	
    * PUT /gwc/rest/blobstores/{blobStoreName} to create or update a blobstore

 	
    * DELETE /gwc/rest/blobstores/{blobStoreName} to remove a blobstore




 	
  * /gwc/rest/gridsets:

 	
    * GET /gwc/rest/gridsets for a list of the gridsets

 	
    * GET /gwc/rest/gridsets/{gridSetName} for details about a single gridset

 	
    * PUT /gwc/rest/gridsets/{gridSetName} to create or update a gridset

 	
    * DELETE /gwc/rest/gridsets/{gridSetName} to remove a gridset





API docs for these endpoints will be added to the GeoServer documentation shortly. Until then, the request body syntax for PUT requests closely matched the equivalent structures in geowebcache.xml: [BlobStores](http://geowebcache.org/docs/latest/configuration/storage.html#blobstore-configuration) and [GridSets](http://geowebcache.org/docs/latest/concepts/gridsets.html#corresponding-xml).

The ArcGISCache backed layers are now also configurable via the REST API.

This release sees a major reworking of the configuration system in GeoWebCache that will allow for plugging in alternate configuration persistence mechanisms in future. While these changes should be largely invisible to users, it is a huge update that impacts all of GeoWebCache. However, due to these changes, we ask that you **please test the embedded GeoWebCache**.


## UI Improvements


Entering in URLs for data files has been improved with autocomplete - now GeoServer will scan the path that has already been typed, and suggest existing files within that path.[![](http://blog.geoserver.org/wp-content/uploads/2018/02/34523743-0b6ba4b2-f099-11e7-99bd-1af27da0ddea.png)](http://blog.geoserver.org/wp-content/uploads/2018/02/34523743-0b6ba4b2-f099-11e7-99bd-1af27da0ddea.png)

In addition, autocomplete support has been added to a number of dropdowns which contain a long list of values, such as stores or layers. You can now start typing the name of an option, and the visible options will be filtered to match.[![](http://blog.geoserver.org/wp-content/uploads/2018/02/store_chooser.png)](http://blog.geoserver.org/wp-content/uploads/2018/02/store_chooser.png)

Editing raster layer parameters made easier, from a wall a text input fields, to appropriate controls being used depending on the parameter type. Here is a "before and after" comparison:

[![](http://blog.geoserver.org/wp-content/uploads/2018/02/coverageParams.png)](http://blog.geoserver.org/wp-content/uploads/2018/02/coverageParams.png)

Finally, error messages are now displayed both at top (as usual) and bottom (new!) in all configuration pages. This should make it easier to locate error messages, especially while editing styles:

[![](http://blog.geoserver.org/wp-content/uploads/2018/02/Selezione_100.png)](http://blog.geoserver.org/wp-content/uploads/2018/02/Selezione_100.png)




## GeoPackage performance improvements


GeoPackage reading and rendering performance improved significantly, up to two times faster on large datasets full extractions and 50% faster on small bounding box searches, bringing GeoPackage on par with PostGIS. We also have a [Google spreadsheet with more details.](https://docs.google.com/spreadsheets/d/1tDEo9M_Vgld1nEDuzGGq7qw8HjaNEd9NTY2Pz5iFyQ4/edit#gid=767941389)

Shapefile remains king of full dataset extractions and the fastest data source for pure spatial driven queries.


## WFS 2.0 and WMTS 1.0 OGC compliance work


During the past few months we have been involved in OGC Testbed 14 and significantly improved GeoServer compliance with WFS 2.0 and WMTS 1.0. The work involved numerous fixes in GeoServer/GeoWebCache, along with variuos fixes in the CITE tests themselves. The changes were too numerous to backport to the 2.12.x series, so if compliance with these protocols is important it's time to consider an upgrade to the 2.13.x series. For details see these lists:



 	
  * [Full list of WFS 2.0 OGC compliances related changes](https://osgeo-org.atlassian.net/issues/?filter=12102)

 	
  * List of changes for WMTS 1.0 are split among [GeoWebCache](https://github.com/GeoWebCache/geowebcache/issues?q=label%3Acitewmts10+is%3Aclosed) and [GeoServer](https://osgeo-org.atlassian.net/issues/?filter=12107) ones


Work is still ongoing and a small number of issues are yet to be fixed, we'll keep you updated.


## **Support for more PostGIS data types**


The PostGIS data store now has simple support for HStore and JSON columns. HStore is returned as a Map and will render as a JSON formatted string field in common WFS output formats, while JSON is read as a string and rendered as-is. In both cases no special query support has been added for those types (but we'd be very happy if someone would work, or sponsor, that functionality too).


## **Better label position control in map rendering**


When setting maxDisplacement on point/polygons the renderer used to search in a circular area around the designated label point.
The new displacementMode vendor option allows to control the positioning by specifying the preferred cardinal positions, as a comma separated list.

![](http://blog.geoserver.org/wp-content/uploads/2018/02/displacementMode.png)


## Coverage views from heterogeneous bands


Satellite data often comes as a set of heterogeenous resolution bands, due to multiple sensors having different native resolutions. It is yet useful to have all bands packaged on the same coverage, for ease of display (false color setups) and information (GetFeatureInfo). Coverage views now allow to mix those bands, coming from separate files and organized in a image mosaic, in a single multiband coverage view, resampling on the fly with configurable target resolution policies.

[![](http://blog.geoserver.org/wp-content/uploads/2018/02/Selezione_098.png)](http://blog.geoserver.org/wp-content/uploads/2018/02/Selezione_098.png)


## Removed OS X installers


Due to lack of resources and interest, the OS X dmg installers are no longer being built. OS X users can still [use](http://docs.geoserver.org/stable/en/user/installation/linux.html#installation) the [system-independent binary](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13-beta/geoserver-2.13-beta-bin.zip/download).


## New community modules and improvements


The 2.13 series comes with a few new community modules, in particular:



 	
  * Do you want to generate GHRSST compliant outputs from GHRSST inputs? Try out the new GHRSST NetCDF output community module.

 	
  * There is also a new [community module](http://docs.geoserver.org/latest/en/user/community/nsg-profile/index.html) introducing NSG profiles for the WFS and WMTS services.


Existing community modules also got some love, in particular:

 	
  * The WPS download module now allows to download large maps, and also build animations, generating MP4 courtesy of jcodec library. Both processes can (and should!) be invoked asynchronously to better handle long generation times. Here is an example of animation output:


[video width="768" height="768" mp4="http://blog.geoserver.org/wp-content/uploads/2018/02/response.mp4"][/video]

 	
  * The WPS download process now also allows control of GeoTiff output structure (tiling, compression) in raw raster downloads

 	
  * Various JDBCConfig and JDBCStore performance improvements, reducing the number of configuration database queries performed for each OGC request. Configuration queries are also consistently logged for further analysis


Note that community modules are not part of the release; instead you can find them in the [nightly builds](https://build.geoserver.org/geoserver/2.13.x/).





## Other assorted improvements


There are many bug fixes and improvements to look at in the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16702), cherry picking a few here:



 	
  * Upgrade JDom library

 	
  * REST API CORS support

 	
  * REST improvements to list all layers in a workspace, and include the workspace prefix in layer listings

 	
  * Style POST does not support non-SLD styles

 	
  * Add WMTS RESTful API

 	
  * Installing the XSLT plugin may cause random REST endpoints to report lists with transforms/transform

 	
  * WCS 1.0.0 does not handle FORMAT parameter properly

 	
  * Cache small amount of features in memory to avoid repeated data scans in GetFeature requests

 	
  * Allow requesting both OL3 and OL2 from the client side

 	
  * Simple feature GML 3.2.1 output schema-invalid as geometries lack mandatory gml:id

 	
  * GeoPackage generated via WPS has y coordinates starting from bottom left

 	
  * Numerous WFS 2.0 bugfixes (WFS 2.0 CITE compliance related)

 	
  * WMTS bugfixes, improving CITE compliance

 	
  * Submitting a seed/truncate request for a tile layer results in a "406, not acceptable"

 	
  * GWC Seed Form returns "Chunk [] is not a valid entry" message error when seeding a layer.

 	
  * Demo Page does not send password

 	
  * Importer can now add computed fields (with CQL expressions) during imports

 	
  * NetCDF output format has a new option to copy global attributes from the source NetCDF file




## Test, test, test!


Now that you know about all the goodies, please go, [download and test](http://sourceforge.net/projects/geoserver/files/GeoServer/2.13-beta/) your favourite ones. Let us know how it went!


## About GeoServer 2.13


GeoServer 2.13 is scheduled for March 2018 release.


