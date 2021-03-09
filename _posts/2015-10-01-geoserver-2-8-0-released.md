---
author: geoserver
comments: true
date: 2015-10-01 02:14:13+00:00
layout: post
link: http://blog.geoserver.org/2015/09/30/geoserver-2-8-0-released/
slug: geoserver-2-8-0-released
title: GeoServer 2.8.0 released
wordpress_id: 2351
categories:
- Announcements
---

We are happy to announce the release of [GeoServer 2.8.0](http://geoserver.org/release/2.8.0/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8.0/geoserver-2.8.0.exe/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8.0/geoserver-2.8.0-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8.0/geoserver-2.8.0.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.8.0/geoserver-2.8.0.exe/download)) along with docs and extensions.


# What is new


GeoServer 2.8.0 is the culmination of our latest six month development cycle and contains several new features, along with fixes and security updates.

This blog post provides a breakdown by functional area, for more detail see the [2.8.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=10602), [2.8-beta](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=10164) and [2.8-M0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=10163) release notes.


## Data access and configuration




### PostGIS curves and Oracle speedups


GeoServer 2.6.0, released one year ago, added read only support for Oracle curved geometries, along with all the necessary machinery to represent them in memory, draw them and encode them in WMS.

This release adds [read and write support for curves in PostGIS instead](http://docs.geoserver.org/latest/en/user/webadmin/data/layers.html#curves-support-vector), bringing our support for the famous open source spatial database to match and surpass (with write support) the Oracle one. PostGIS curves are supported in all OGC protocols, either via native support (e.g., GML) or on the fly linearization (e.g. shapefile output).

![Sample curve data for PostGIS - Details](http://i2.wp.com/www.geo-solutions.it/wp-content/uploads/2015/06/helsinki2.jpg?resize=300%2C175)

On the Oracle side, we improved the startup times for installation that are serving of Oracle layers by optimizing the table geometry type and metadata access.

Note: Due to license restrictions the oracle extension no longer includes an Oracle JDBC driver, see the [user guide](http://docs.geoserver.org/latest/en/user/data/database/oracle.html#oracle-install) for manual install instructions.


### Filtering layers during configuration


For all those that want to publish only a subset of the original data to the public we are now offering the configuration of a simple CQL filter that will be applied on data access, no matter what protocol is used. Think of it as a mini "sql view" that can be applied at ease against any data source, not just databases.



This is of course not meant to limit feature access for security reasons, for that use case you should really look into [GeoFence](https://github.com/geoserver/geofence).


### Raster NODATA with JAI-Ext Library


You may now optionally use the JAI-Ext image processing operations when working with raster data. These operations directly support raster NODATA and footprints (reducing the amount of processing required when working with these datasets).

[![JAI-Ext Operations](/img/uploads/server_JAIEXT-300x1151.png)](http://blog.geoserver.org/2015/09/30/geoserver-2-8-0-released/server_jaiext/)

This feature is available in GeoServer 2.8 but is off by default - to enable start up with:


<blockquote>-Dorg.geotools.coverage.jaiext.enabled=true</blockquote>




### REST API for Image Moasic Granule Management


Structured coverages have recently been added to GeoServer, you can now use the REST API to [manage and update](http://docs.geoserver.org/stable/en/user/rest/api/coverages.html#structured-coverages) individual granules in an image mosaic.


### Process raster data during import


Vector import has supported limited data processing during import for some time. GeoServer 2.8.0 provides the same functionality (allowing raster files to be processed using GDAL command line tools during import).

To reproject a raster:

    
    {
      "type": "GdalWarpTransform",
    
      "options": [
      "-t_srs", "EPSG:4326”
      ]
    }


To transform the raster into a GeoTIFF:

    
    {
      “type”: “GdalTranslateTransform”,
      “options”: [
        “-co”, “TILED=YES”,
        “-co”, “BLOCKXSIZE=512”,
        “-co”, “BLOCKYSIZE=512”
      ]
    }
    


To introduce GeoTIFF overviews:

    
    {
      "type": "GdalAddoTransform",
      "options": [ "-r", "average"],
      "levels" : [2, 4, 8, 16]
    }




## Mapping improvements


This release is full of big and small map rendering improvements for all. Here is an organized list.


### Z ordering support


This new features extends SLD and CSS with vendor options allowing the style writer to control the painting order of features, either inside a single layer, or across layers: this allows proper map rendering of areas where a number of objects have below/above relationsthips, like this area in Germany, where a lot of roads and rails are crossing each other in a maze of underpasses, overpasses, and bridges:



This is achieved by specifying a "sortBy" vendor option at the FeatureTypeStyle level, with one or more sorting attributes, and in case multiple layers or FeatureTypeStyles are involved, by grouping them into a single "sortByGroup". You can find more information, [along with examples in CSS and SLD, in your user guide](http://docs.geoserver.org/latest/en/user/styling/sld-extensions/z-order/index.html).

We would like to thank [DLR for sponsoring this improvement](http://www.dlr.de).


### Constrast enhancement improved


GeoServer has been supporting contrast enhancement for a while, within the limits of the SLD specification. Version 2.8.0 steps beyond the limits of the standard by [adding vendor parameters to control the normalization sub-algorithm](http://docs.geoserver.org/latest/en/user/styling/sld-reference/rastersymbolizer.html#contrastenhancement) (stretch to min/max, clip to min/max, clip to zero), as well as its parameters. Here is an example of the syntax:

    
    <ContrastEnhancement>
      <Normalize>
       <VendorOption name="algorithm">StretchToMinimumMaximum</VendorOption>
       <VendorOption name="minValue">50</VendorOption>
       <VendorOption name="maxValue">100</VendorOption>
      </Normalize>
    </ContrastEnhancement>


along with a visual example, before and after the contrast enhancement:

[![](/img/uploads/original-300x1361.png)](http://blog.geoserver.org/2015/09/30/geoserver-2-8-0-released/original/)

[![contrast enhancement after](/img/uploads/contrast-enchance-300x1361.png)](http://blog.geoserver.org/2015/09/30/geoserver-2-8-0-released/contrast-enchance/)


### New arrow mark


Lots of map needs arrows... but every time is the same story, yes, the arrow is almost fine, but it should be longer, or thicker, or with a bigger head, and so on. Instead of having to re-invent a new arrow symbol each time, we created one whose proportions can be altered by changing parameters in its name.

Here is the general syntax of this new "well known mark":

    
    <WellKnownName>extshape://arrow?hr=[hrValue]&t=[tValue]&ab=[abValue]</WellKnownName>


and some examples varying its t (thickness) value between 0 and 1:

![arrow1](http://i1.wp.com/www.geo-solutions.it/wp-content/uploads/2015/06/unnamed1.png?resize=300%2C39)

or changing the witdh the height ratio (hr):

![arrow2](http://i1.wp.com/www.geo-solutions.it/wp-content/uploads/2015/06/unnamed2.png?resize=253%2C85)

So next time they ask you for a customized arrow, you can whip up your arrow mark, and give them something like this:

<WellKnownName>extshape://arrow?hr=4&amp;ab=0.8</WellKnownName>

![arrow4](http://i0.wp.com/www.geo-solutions.it/wp-content/uploads/2015/06/unnamed4.png?resize=237%2C125)


### Multi-script maps made easier


GeoServer 2.8.0 improves its support for maps in multiple scripts, which can be a source of headaches. While it's often easy to find support for most scripts in fonts, it's hard to get one that would support, for example, western languages, arabic, corean, indi and simplified chinese in a single package. Especially for scripts like simplified chinese you have to resort to custom fonts.

Now, what happens if you are labelling a map that contains them all, and sometimes, contains more than one of them in a single label? Before GeoServer 2.8.0 we did not have a great answer to that, but now, you can simply specify multiple fonts in a TextSymbolizer, and the most suitable one will be chosen on the fly, eventually using multiple fonts in a single label in case there is no one able to handle the whole of it. Here is an example with mixed script labels:



We would like to thank [DLR for sponsoring this improvement](http://www.dlr.de).


### Improved labeling density


Before GeoServer 2.8.0 labelling dense road networks with lots of diagonal and curved labels might have left the impression that more labels could have fit the map... and that was not just an impression! Indeed, the previous label algorithm was reserving  a busy area for the bounding box containing the label, which as you may see, is a lot more space than the actual label occupancy:

![Letter reservation - conflict](http://i1.wp.com/www.geo-solutions.it/wp-content/uploads/2015/09/Letter-reservation-conflict.png?resize=254%2C118)

The [French National Institute for geographic information](http://www.ign.fr/) provided a patch that makes the single chars of diagonal or curved labels be reserved instead, resulting in maps with quite a bit more labelled items per square inch:




## WMS/WMTS protocol and configuration improvements




### Creating new styles from templates


It's now possible to create new styles starting from the built-in templates, and the style will be encoded in the desired style language (SLD, or CSS, or even something else, if you created your own styling language extension point):








### GeoWebCache filter parameters GUI improved


It's now possible to configure integer parameters in the caching section of a layer configuration.

[![Parameter Filter](/img/uploads/pfilter-changes11.png)](http://blog.geoserver.org/2015/09/30/geoserver-2-8-0-released/pfilter-changes-2/)


### GeoWebCache Storage


GeoWebCache can now store cached tiles on a perlayer basis - including Amazon S3.





[![](/img/uploads/blobstore1.png)](http://blog.geoserver.org/2015/09/30/geoserver-2-8-0-released/blobstore/)


### Request parameter support in Freemaker templates


Freemarker GetFeatureInfo templates can now [access to the request parameter](http://docs.geoserver.org/latest/en/user/tutorials/freemarker.html#common-data-models), as well as the Java process environment variables, in order to customize their response. For example, it's now possible to expand the following variables in the template:


<blockquote>

>     
>     ${request.LAYERS}
>     ${request.ENV.PROPERTY}
>     ${environment.GEOSERVER_DATA_DIR}
>     ${environment.WEB_SITE_URL}
> 
> 
</blockquote>




### Controlling interpolation on a layer by layer basis


You can now control layer interpolation via GetMap, and specify a [different interpolation policy on different layers](http://docs.geoserver.org/latest/en/user/services/wms/vendor.html#interpolations). This is great if you are serving multiple raster maps, and maybe you want to have your classified raster use nearest neighbor, while showing the ozone density layer with bilinear interpolation.


### Inspire configuration improved




## Security




### REST API for access control


Their is now a REST API for configuring security access control - see the [user guide](http://docs.geoserver.org/stable/en/user/rest/api/accesscontrol.html) for details.


# About GeoServer 2.8


Articles, blog posts and presentations:



	
  * [State of GeoServer 2015](http://www.slideshare.net/jgarnett/state-of-geoserver-2015) (FOSS4G)

	
  * [XEE Vunerability](http://blog.geoserver.org/2015/06/27/geoserver-xee-vulnerability/) (GeoServer)

	
  * [Z ordering features within and across feature types and layers](http://docs.geoserver.org/latest/en/user/styling/sld-extensions/z-order/index.html#z-ordering-features-within-and-across-feature-types-and-layers) (User Manual)

	
  * [JAI-Ext, the Open Source replacement for Oracle JAI](http://www.geo-solutions.it/blog/developers-corner-jai-ext-the-open-source-replacement-for-oracle-jai/) (GeoSolutions)

	
  * [Customizable arrow in GeoServer](http://www.geo-solutions.it/blog/customizable-arrow-geoserver/) (GeoSolutions)

	
  * [PostGIS Curve Support](http://www.geo-solutions.it/blog/postgis-curves-in-geoserver/) (GeoSolutions)

	
  * [Improved NetCDF/GRIB support in GeoServer](http://www.geo-solutions.it/blog/netcdf-grib-support-geoserver/) (GeoSolutions)

	
  * [GeoServer 2.8-RC1](http://blog.geoserver.org/2015/09/14/geoserver-2-8-rc1-released/), [GeoServer 2.8-beta](http://blog.geoserver.org/2015/08/31/geoserver-2-8-beta-release/) and [GeoServer 2.8-M0](http://blog.geoserver.org/2015/05/29/geoserver-2-8-m0-released/) announcements


For additional details see the [2.8.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=10602), [2.8-beta](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=10164) and [2.8-M0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=10163) release notes.


## GeoServer Community


GeoServer Community modules provide an area for ideas and experimentation:



	
  * WCS and WPS output formats based on gdal_translate to provide a greater range of output formats

	
  * Gabriel has created a community module for [vector tiles](https://github.com/geoserver/geoserver/tree/master/src/community/vectortiles) experimentation

	
  * Embedded GeoFence server, REST API and GUI is the result of a productive collaboration between GeoSolutions and Boundless offering greater rule-based control of GeoServer security

	
  * [MongoDB DataStore](http://boundlessgeo.com/2015/07/mongodb-collaboration/) enabling GeoServer to publish from this popular JSON based document database (no zip packaging, needs volunteer)


Community modules should be considered a work-in-progress and are subject to quality assurance, documentation IP checks and a maintainer before being considered ready for release.
