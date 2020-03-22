---
author: jgarnett
comments: false
date: 2017-10-17 08:55:00+00:00
layout: post
link: http://blog.geoserver.org/2017/10/17/geoserver-2-12-0-released/
slug: geoserver-2-12-0-released
title: GeoServer 2.12.0 Released
wordpress_id: 2908
categories:
- Announcements
---



We are happy to announce the release of [GeoServer 2.12.0](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.0/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.0/geoserver-2.12.0-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.0/geoserver-2.12.0-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.0/geoserver-2.12.0.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.12.0/geoserver-2.12.0.exe/download)) along with docs and extensions.

This is a stable release recommended for production use. This release is made in conjunction with GeoTools 18.0.






## Rest API now using Spring MVC


[In March](http://blog.geoserver.org/2017/04/11/rest-api-code-sprint-results/), we upgraded the framework used by the GeoServer REST API from Restlet to Spring MVC. All the endpoints have remain unchanged and we would like to thank everyone who took part.

We should also thank David Vick who migrated the embedded GeoWebCache REST API, and the entire team who helped him reintegrate the results for this 2.12.0 release.

Thanks again to the code sprint sponsors and in-kind contributors:

![Gaia3d](http://blog.geoserver.org/wp-content/uploads/2017/03/Gaia3d-300x112.png)   ![atol_logo](http://blog.geoserver.org/wp-content/uploads/2017/03/atol_logo-1024x229.png)  [![Boundless_Logo](http://blog.geoserver.org/wp-content/uploads/2017/03/Boundless_Logo.png)](http://blog.geoserver.org/wp-content/uploads/2017/03/Boundless_Logo.png)  ![](https://wiki.osgeo.org/images/thumb/0/0a/Geodan_logo.png/350px-Geodan_logo.png)  [![How2map_logo](http://blog.geoserver.org/wp-content/uploads/2017/03/How2map_logo.png)](http://www.geodan.nl/)   ![](http://blog.geoserver.org/wp-content/uploads/2017/04/astunlogosmall.jpg)  ![fossgis_logo](http://blog.geoserver.org/wp-content/uploads/2017/03/fossgis_logo.png)  ![iag_logo](http://blog.geoserver.org/wp-content/uploads/2017/03/iag_logo-300x300.png)  [![](http://blog.geoserver.org/wp-content/uploads/2017/04/geosolutions_logo.png)](http://www.geo-solutions.it/)

As part of this upgrade, we also have [new REST documentation](http://docs.geoserver.org/latest/en/user/rest/index.html#rest), providing detailed information about each endpoint. The documentation is written in [swagger](http://swagger.io), allowing different presentations to be generated as shown below.

[![](http://blog.geoserver.org/wp-content/uploads/2017/10/rest-api-docs-983x1024.png)](http://blog.geoserver.org/wp-content/uploads/2017/10/rest-api-docs.png)




## WMTS Cascading


Adds the ability to create WMS layers backed by remote WMTS layers, similar to the pre-existing WMS cascading functionality.

See [GSIP-162](https://github.com/geoserver/geoserver/wiki/GSIP-162) for more details.

[![](http://blog.geoserver.org/wp-content/uploads/2017/09/wmtsaddnew.png)](http://blog.geoserver.org/wp-content/uploads/2017/09/wmtsaddnew.png)

[![](http://blog.geoserver.org/wp-content/uploads/2017/09/wmtsconfigure.png)](http://blog.geoserver.org/wp-content/uploads/2017/09/wmtsconfigure.png)


## Style Based Layer Groups


Adds the ability to define a listing of layers and styles using a single SLD file, in accordance with the original vision of the SLD specification. This includes a new entry type in the Layer Group layers list and a new preview mode for the style editor.

[![](http://blog.geoserver.org/wp-content/uploads/2017/10/style-group-preview.png)](http://blog.geoserver.org/wp-content/uploads/2017/10/style-group-preview.png)

GeoServer has long supported this functionality for clients, via an external SLD file. This change allows more people to use the idea of a single file defining their map layers and styling as a configuration option.

See [GSIP-161](https://github.com/geoserver/geoserver/wiki/GSIP-161) for more details.


## [![](http://blog.geoserver.org/wp-content/uploads/2017/09/gsip161-ui.png)](http://blog.geoserver.org/wp-content/uploads/2017/09/gsip161-ui.png)




## Options for KML Placemark placement


New options for KML encoding have been added, to control the placement of placemark icons, mostly for polygons. The syntax of the new options introduces three new top-level format options keys:

`&format_options=kmcentroid_contain:true;kmcentroid_samples:10;kmcentroid_clip:true`

See [GSIP-160](https://github.com/geoserver/geoserver/wiki/GSIP-160) for more details.


## GeoWebCache data security API


Add an extension point to GeoWebCache allowing for a security check based on the layer and extent of the tile. Adds an implementation of this extension point to GeoServer's GWC integration.

This change mostly only affects developers but will lead to improved security for users in the future.

See [GSIP 159](https://github.com/geoserver/geoserver/wiki/GSIP-159) for more details.


## NetCDF output support for variable attributes and extra variables


Adds the following to the NetCDF output extension:



 	
  1. An option to allow all attributes to be copied from the source NetCDF/GRIB variable to the target variable.

 	
  2. Support for manual configuration of variable attributes, much like the current support for setting global attributes.

 	
  3. Support for configuration of extra variables which are copied from the NetCDF/GRIB source to the output; initially only scalar variables will be supported. Extra variables can be expanded to "higher" dimensions, that is, values copied from one scalar per ImageMosaic granule are assembled into a multidimensional variable over, for example, time and elevation.


See [GSIP 158](https://github.com/geoserver/geoserver/wiki/GSIP-158) for more details.

[![](http://blog.geoserver.org/wp-content/uploads/2017/09/netcdf.png)](http://blog.geoserver.org/wp-content/uploads/2017/09/netcdf.png)


## New labelling features and QGIS compatibility


A number of small new features have been added to labelling to match some of QGIS features, in particular:



 	
  * [Kerning](https://en.wikipedia.org/wiki/Kerning) is on by default

 	
  * New vendor option to strikethrough text

 	
  * New vendor options to control char and word spacing


![../../../_images/charSpacing.png](http://blog.geoserver.org/wp-content/uploads/2017/10/charSpacing.png)
![](http://blog.geoserver.org/wp-content/uploads/2017/10/wordSpacing.png)



 	
  * Perpendicular offset now works also for curved labels (previously only supported for straight labels):![](https://user-images.githubusercontent.com/325433/29674782-771613cc-88f3-11e7-8355-ad3ad584454b.png)

 	
  * Labeling the border of polygons as opposed to their centroid when using a LinePlacement (here with repetition and offset):


[![](http://blog.geoserver.org/wp-content/uploads/2017/09/border.png)](http://blog.geoserver.org/wp-content/uploads/2017/09/border.png)

Along with this work some SLD 1.1 text symbolizer fixes were added in order to better support the new QGIS 3.0 label export, here is an example of a map labeling with background image, as shown in QGIS, and then again in GeoServer using the same data and the exported SLD 1.1 style (click to enlarge):

[![](http://blog.geoserver.org/wp-content/uploads/2017/09/qgis_label-300x168.png)   ](http://blog.geoserver.org/wp-content/uploads/2017/09/qgis_label.png)[![](http://blog.geoserver.org/wp-content/uploads/2017/09/geoserver_label-300x172.png)](http://blog.geoserver.org/wp-content/uploads/2017/09/geoserver_label.png)


## CSS improvements


The CSS styling language and editing UI have seen various improvements. The editor now supports some primitive code completion:[![](http://blog.geoserver.org/wp-content/uploads/2017/09/css_completion.png)](http://blog.geoserver.org/wp-content/uploads/2017/09/css_completion.png)

At the language level:



 	
  * Scale dependencies can now also be expressed using the "@sd" variable (scale denominator) and the values can use common suffixes such as k and M to get more readable values, compare for example "[@scale < 1000000]" with "[@sd < 1M]"

 	
  * Color functions have been introduced to match LessCSS functionality, like "Darken", "Lighten, "Saturate" and so on. The same functions have been made available in all other styling languages.

 	
  * Calling a "env" variable has been made easier, from "env('varName')" to "@varName" (or "@varName(defaultValue)" if you want to provide a default value).


As you probably already know, internally CSS is translated to an equivalent SLD for map rendering purposes. This translation process became 50 times faster over large stylesheets (such as OSM roads, a particularly long and complicated style).


## Image mosaic improvements and protocol control


Image mosaic saw several improvements in 2.12.

First, the support for mosaicking images in different coordinate reference systems improved greatly, with several tweaks and correctness fixes. As a noteworthy change, the code can now handle source data crossing the dateline. The following images show the footprints of images before and after the dateline (expressed in two different UTM zones, 60 and 1 respectively) and the result of mosaicking them as rasters (click to get a larger picture of each):

[![](http://blog.geoserver.org/wp-content/uploads/2017/09/before_dateline-300x239.png)](http://blog.geoserver.org/wp-content/uploads/2017/09/before_dateline.png)[![](http://blog.geoserver.org/wp-content/uploads/2017/09/after_dateline-266x300.png)](http://blog.geoserver.org/wp-content/uploads/2017/09/after_dateline.png)

[![](http://blog.geoserver.org/wp-content/uploads/2017/09/mosaic_dateline-1024x512.png)](http://blog.geoserver.org/wp-content/uploads/2017/09/mosaic_dateline.png)

There is more good news for those that handle mosaics with a lot of super-imposing images taken at different times. If you added interesting information into the mosaic index, such as cloud cover, off-nadir, snow cover and the like, you can now filter and sort them, in both WMS (viewing) and WCS (downloading) by adding the **cql_filter** and **sortBy** KVP parameters.

Here is an example of the same mosaic, the first composite favouring smallest cloud cover, the second one favouring recency instead (click to enlarge):

[![](http://blog.geoserver.org/wp-content/uploads/2017/09/cloudcover-300x210.png)    ](http://blog.geoserver.org/wp-content/uploads/2017/09/cloudcover.png)[![](http://blog.geoserver.org/wp-content/uploads/2017/09/recency-300x207.png)](http://blog.geoserver.org/wp-content/uploads/2017/09/recency.png)


## GeoPackage graduation


The GeoPackage store jumped straight from community to core package, in light of its increasing importance.

The WMS/WFS/WPS output formats are still part of community. Currently, GeoPackage vector does not support spatial indexes but stay tuned, it's cooking!


## New community modules


The 2.12 series comes with a few new community modules, in particular:



 	
  * Looking into styling vector tiles and server side using a single language? Look no further than the [MBStyle module](http://docs.geoserver.org/latest/en/user/styling/mbstyle/index.html)

 	
  * For those into Earth Observation, there is a new [OpenSearch for EO module](http://docs.geoserver.org/latest/en/user/community/opensearch-eo/index.html) in the community section

 	
  * Need to store full GeoTiff in Amazon S3? The "[S3 support for GeoTiff](http://docs.geoserver.org/latest/en/user/community/s3-geotiff/index.html)" module might just be what you're looking for

 	
  * A new "status-monitoring" community module has been added, providing basic statistics system resource usage. Check out this [pull request](https://github.com/geoserver/geoserver/pull/2518) to follow its progress and merge.


Mind, community modules are not part of the release, but you can find them in the [nightly builds](http://geoserver.org/release/2.12.x/) instead.





## Other assorted improvements


Highlights of this release featured below, for more information please see the release notes ([2.12.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=16703&styleName=Html&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7Cf148b3772c10d37fb2a345c4d35ca4b24e27e75d%7Clin) | [2.12-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16600) | [2.12-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15700)):



 	
  * Users REST uses default role service name as a user/group service name

 	
  * imageio-ext-gdal-bindings-xxx.jar not available in geoserver-2.x.x-gdal-plugin.zip anymore since 2.10

 	
  * REST GET resource metadata - file extension can override format parameter

 	
  * GeoServer macOS picks up system extensions

 	
  * SLD files not deleted when SLD is deleted in web admin

 	
  * Reproject geometries in WMS GetFeatureInfo responses when info_format is GML

 	
  * Include [Marlin](https://github.com/bourgesl/marlin-renderer) by default in bin/win/osx downloads, add to war instructions

 	
  * Handle placemark placement when centroid of geometry not contained within

 	
  * Enable usage of viewParams in WPS embedded WFS requests

 	
  * Add GeoJson encoder for complex features

 	
  * Allow image mosaic to refer a GeoServer configured store

 	
  * Duplicate GeoPackage formats in layer preview page

 	
  * ExternalGraphicFactory does not have a general way to reset caches

 	
  * Generating a raster SLD style from template produced a functionally invalid style, now fixed

 	
  * Style Editor Can Create Incorrect External Legend URLs

 	
  * Namespace filtering on capabilities returns all layer groups (including the ones in other workspaces)





## About GeoServer 2.12 Series


Additional information on the 2.12.0 series:



 	
  * [State of GeoServer 2.12 ](https://www.slideshare.net/geosolutions/state-of-geoserver-21geoservernodeopts2)(SlideShare)

 	
  * [GeoServer Feature Frenzy](https://www.slideshare.net/jgarnett/geoserver-feature-frenzy-80906586/jgarnett/geoserver-feature-frenzy-80906586) (SlideShare)

 	
  * New [REST API documentation](http://docs.geoserver.org/latest/en/user/rest/index.html#rest)

 	
  * [REST API Code Sprint Results](http://blog.geoserver.org/2017/04/11/rest-api-code-sprint-results/)



