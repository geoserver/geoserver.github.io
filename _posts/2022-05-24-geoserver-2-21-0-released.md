---
author: Ian Turton
date: 2022-05-24
layout: post
title: GeoServer 2.21.0 Release
categories:
- Announcements
tags:
- Release
release: release_221
version: 2.21.0
jira_version: 16855
---

GeoServer [2.21.0](/release/2.21.0/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.0/geoserver-2.21.0-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.0/geoserver-2.21.0-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.0/GeoServer-2.21.0-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.0/geoserver-2.21.0-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.21.0/extensions/).

This is a first release of the new stable branch of GeoServer and is made in conjunction with GeoTools 27.0 
and GeoWebCache 1.21.0.

  * This is likely to be the last release that supports Java 8 and we encourage users to start to make the 
    transition to Java 11 during the lifetime of this branch.
  * Thanks to everyone who help tested the release candidate on and off list: Daniel Calliess, Georg Weickelt, 
    Stefan Overkamp,  Nicolas Matzick, Sander Schaminee, Jose Garcia, Rosa Briones, Jody Garnett, Andrea Aime, 
    Ian Turton.

### Feature Type Customization

We are pleased to share a long-requested feature - the ability to rename attributes and change attribute order when publishing a FeatureType. 

![Feature type customization](/img/posts/2.21/feature_type_remap.png) <br/>

It is also possible to change attribute type, and with the use of ECQL expressions generate new attributes on the fly.

The above example works around the limitations of shapefile to use longer names, and creates a new attribute ``capital`` on the fly from an expression, as shown in the following GetFeatureInfo output.

![GetFeatureInfo tasmania_cities](/img/posts/2.21/tasmania_feature_type.png) <br/>

This is a great new addition to GeoServer, please see [Feture Type Details](https://docs.geoserver.org/latest/en/user/data/webadmin/layers.html#feature-type-details-vector) in the user guide for details.

* [GEOS-10356](https://osgeo-org.atlassian.net/browse/GEOS-10356) Allow feature type customization

Thanks to Andrea Aime (GeoSolutions) for proposal [GSIP-207](https://github.com/geoserver/geoserver/wiki/GSIP-207) and implementation.

### Translations and Language Chooser

A big thanks to Alexandre Gacon and everyone who helped improve GeoServer internationalization for during this release cycle.

To support this activity Andrea Aime has contributed a language chooser to the top of the screen (near the login button).

![Language chooser](/img/posts/2.21/language.png)<br/>

For more information see [Choosing the UI language](https://docs.geoserver.org/latest/en/user/webadmin/index.html#choosing-the-ui-language) (User Guide).

* [GEOS-1158](https://osgeo-org.atlassian.net/browse/GEOS-1158) Specify Geoserver UI Language in Configuration

### Add Styles support to LayerGroup

Layer groups can now be configured with additional styles, with each style listing a series of layers along with the style used to render each layer.

![Layer group styles](/img/posts/2.21/layer_group_styles.png) <br/>

This allows a `SINGLE` or `OPAQUE` layer group to list alternate styles in addition to the default one. Each alternate style is defined by a named configuration of layers and styles providing a unique visual representation.

In the above example the layer group Tasmania is setup with an alternate "data" presentation, presenting the content with the geoserver default styles `point`, `line` and `polygon`.

![Layer group style Tasmania](/img/posts/2.21/layer_group_tas.png) <br/>

For more information see [Layer Group Styles](https://docs.geoserver.org/latest/en/user/data/webadmin/layergroups.html#layer-group-styles) (User Guide).

* [GEOS-10252](https://osgeo-org.atlassian.net/browse/GEOS-10252) Add Styles support to LayerGroup
* [GEOS-10274](https://osgeo-org.atlassian.net/browse/GEOS-10274) Geofence follow up LayerGroup Style addition

Thanks to Marco Volpini (GeoSolutions) for [GSIP-205](https://github.com/geoserver/geoserver/wiki/GSIP-205) proposal and implementation.

### GeoPackage WMS and WFS Output

The result of proposal [GSIP-206](https://github.com/geoserver/geoserver/wiki/GSIP-206) is the creation of the gs-geopkg-output extension packaging up the WFS and WMS output formats from the geopackage community module.

```
curl "http://localhost:8080/geoserver/wfs?service=wfs&version=2.0.0&request=GetFeature&typeNames=topp:states&outputFormat=geopkg" -o wfs.gpkg
```

For more information see [Using the GeoPackage Output Extension](https://docs.geoserver.org/latest/en/user/extensions/geopkg-output/usage.html) in the user guide.

* [GEOS-10351](https://osgeo-org.atlassian.net/browse/GEOS-10351) \[GSIP 206\] Promote GeoPackage WFS and WMS output formats to an extension
* [GEOS-8793](https://osgeo-org.atlassian.net/browse/GEOS-8793) WFS 1.1.0/2.0.0 GeoPackage output wrong Coordinate Order

Thanks to David Blasby and Jody Garnett (GeoCat) for packaging up this work as an extension. This work was 
supported in part by Rijkswaterstaat.

### Mark Factory Precedence

When rendering maps with lots of individual graphics, looking up the correct implementation (known as a MarkFactory) can be time consuming.

WMS Settings have new capability to filter out any mark factories not being used, and provide an order to prioritise the ones being used.

![MarkFactory precedence](/img/posts/2.21/markfactory.png)<br/>

For more information see [WMS Web Administration](https://docs.geoserver.org/stable/en/user/services/wms/webadmin.html#mark-factory-precedence) (user guide).

* [GEOS-10230](https://osgeo-org.atlassian.net/browse/GEOS-10230) MarkFactory WMS rendering performance optimization

Thanks to Fernando Mino (GeoSolutions Group) for troubleshooting this performance issue, and proposal [GSIP-204](https://github.com/geoserver/geoserver/wiki/GSIP-204) as an optimization.

### Log4J 2 Upgrade

The assessment of [Log4Shell]({% post_url 2021-12-13-logj4-rce-statement %}) vulnerability highlighted that although GeoSever was not affected, our use of the older Log4j 1.2 was a notable risk. This discussion resulted a [small fundraising effort]({% post_url 2022-01-20-log4j-upgrade %}) and proposal to [upgrade to Log4j 2](https://github.com/geoserver/geoserver/wiki/GSIP-167).

The result is a small change to the user interface, listing logging profiles by name (previously the file extension was also listed).

![Log4j update](/img/posts/2.21/logging.png)<br/>

Internally this release changes from Log4j 1.2 logging profiles (using ``properties`` extension) to Log4j 2 logging profiles (using ``xml`` extension):

* The built-in logging profiles (``DEFAULT_LOGGING``, ``PRODUCTION_LOGGING``, ...) are replaced with new Log4j 2 ``xml`` files.

* Previous custom logging profiles will continue to be available (Log4J 2 has the ability to read the older Log4J 1.2 properties files).

* If you made any customizations to the built-in profiles, you can recover your changes from backup ``bak`` file. You can use this backup as a reference when creating a new ``xml`` logging profile, or restore this under a different name which does not conflict with the built-in logging profiles.

  A customization to ``PRODUCTION_LOGGING.properties`` will be backed up to ``PRODUCTION_LOGGING.properties.bak``. This can be restored by renaming ``PRODUCTION_LOGGING.properties.bak`` to ``CUSTOM_LOGGING.properties``.

In addition to the ``INFO`` status messages, you will notice a new ``CONFIG`` logging level used during application startup:
```
CONFIG [org.geoserver] - GeoServer configuration lock is enabled
CONFIG [org.geoserver] - Loading catalog...
...
```

For more information, and examples of writing a Log4J 2 profile, see [Logging Settings](https://docs.geoserver.org/latest/en/user/configuration/globalsettings.html#logging-settings) and [Advanced log configuration](https://docs.geoserver.org/latest/en/user/configuration/logging.html) in the User Guide. Of note is the introduction of a new ``CONFIG`` logging level used when loading and saving configuration changes.

* [GEOS-10426](https://osgeo-org.atlassian.net/browse/GEOS-10426) GSIP 167: Upgrade Log4j

Thanks to Jody Garnett (GeoCat) for completing this work, and to the following sponsors for supporting this activity.

* [opengeogroep.nl](https://opengeogroep.nl/)
* [www.terrestris.de](https://www.terrestris.de/en/)
* [how2map.com](http://how2map.com)
* [www.geonovation.nl](https://www.geonovation.nl/)

### Logging REST API

For more information please see [Logging settings](https://docs.geoserver.org/latest/en/user/rest/api/logging.html) (User Guide) and [GeoServer Logging](https://docs.geoserver.org/latest/en/api/#1.0.0/logging.yaml) (REST API).

* [GEOS-10368](https://osgeo-org.atlassian.net/browse/GEOS-10368) Logging Controller Addition allows configuration of logging via REST API.

Thanks to Yalın Eren Deliorman for this contribution.

### New WPS settings and KML input/output support

A number of improvements have been made to the WPS service:

* [GEOS-10443](https://osgeo-org.atlassian.net/browse/GEOS-10443) Graduate kml-ppio community module to wps extension
  
  KML can now be used with WPS service for both input and output parameters.
  
* [GEOS-10391](https://osgeo-org.atlassian.net/browse/GEOS-10391) Add external output directory setting to limit where processes can write
  
  See WPS setting for [external output directory](https://docs.geoserver.org/latest/en/user/services/wps/administration.html#execution-and-resource-management-options) in User Guide.
  
* [GEOS-10431](https://osgeo-org.atlassian.net/browse/GEOS-10431) Add WPS setting to disable remote complex inputs.
  
  See [WPS Security and input limits](https://docs.geoserver.org/main/en/user/services/wps/security.html#complex-inputs) in User Guide.

### GDAL 3.x Compatibility

The gdal-output extension is tested against GDAL 3.x series.

Please pay careful attention to the installation instructions, while the extensions includes ``gdal-3.2.0.jar`` you should double check the native binaries (included in your Linux distribution or installed by hand) and download an appropriate [replacement jar online](https://search.maven.org/artifact/org.gdal/gdal).

For more information see [Installing GDAL native libraries](https://docs.geoserver.org/latest/en/user/data/raster/gdal.html#installing-gdal-native-libraries) in the User Guide.

* [GEOS-10402](https://osgeo-org.atlassian.net/browse/GEOS-10402) Upgrade imageio-ext to 1.4.0 \(tested with gdal 3.2\)

Thanks to Andrea Aime (GeoSolutions) for making the ImageIO-EXT release, and Jody Garnett (GeoCat) for GDAL 
3.x upgrade and testing. This work was supported in part by Rijkswaterstaat.

### Improvements and Fixes

New features:

* [GEOS-10228](https://osgeo-org.atlassian.net/browse/GEOS-10228) Add wrap_limit property to wrap the category text values of a legend

Improvements:

* [GEOS-10146](https://osgeo-org.atlassian.net/browse/GEOS-10146) App-schema: support for multiple geometries with different CRS
* [GEOS-10246](https://osgeo-org.atlassian.net/browse/GEOS-10246) jdbcconfig: performance slow-down from unnecessary transactions
* [GEOS-10251](https://osgeo-org.atlassian.net/browse/GEOS-10251) Refactor MapML vocabulary to map- custom elements HTML namespace
* [GEOS-10463](https://osgeo-org.atlassian.net/browse/GEOS-10463) Support WCS default value for Deflate Compression
* [GEOS-10320](https://osgeo-org.atlassian.net/browse/GEOS-10320) Support GetFeatureInfo on raster layers with transformations turning the output into vector
* [GEOS-10405](https://osgeo-org.atlassian.net/browse/GEOS-10405) GetFeatureInfo: Support multiple featureCollections per query layer

Fixes:

* [GEOS-10226](https://osgeo-org.atlassian.net/browse/GEOS-10226) ResourcePool leaves empty files on failure
* [GEOS-10318](https://osgeo-org.atlassian.net/browse/GEOS-10318) CSV output format for complex features doesn't resolve namespace URIs to prefixes on attributes names
* [GEOS-10235](https://osgeo-org.atlassian.net/browse/GEOS-10235) Prevent double-quote to be specified as CSV separator
* [GEOS-10477](https://osgeo-org.atlassian.net/browse/GEOS-10477) SLD - Validation error on Normalize-node
* [GEOS-10448](https://osgeo-org.atlassian.net/browse/GEOS-10448) GetTimeSeries does not limit number of dates when using a time range request \(without period\)
* [GEOS-10429](https://osgeo-org.atlassian.net/browse/GEOS-10429) Style validation error using the VendorOption "graphic-margin"
* [GEOS-10318](https://osgeo-org.atlassian.net/browse/GEOS-10318) CSV output format for complex features doesn't resolve namespace URIs to prefixes on attributes names
* [GEOS-10502](https://osgeo-org.atlassian.net/browse/GEOS-10502) GML3 output is not pretty printed when pretty print is turned on in global settings.

Tasks:

* [GEOS-10458](https://osgeo-org.atlassian.net/browse/GEOS-10458) Update jai-ext to 1.1.22
* [GEOS-10446](https://osgeo-org.atlassian.net/browse/GEOS-10446) Upgrade to commons-codec 1.15 version
* [GEOS-10363](https://osgeo-org.atlassian.net/browse/GEOS-10363) Switch from itextpdf to openpdf for PDF map rendering

## About GeoServer 2.21

Additional information on GeoServer 2.21 series:

* [Feature Type Customization](https://github.com/geoserver/geoserver/wiki/GSIP-207)
* [Add Styles support to LayerGroup](https://github.com/geoserver/geoserver/wiki/GSIP-205)
* [Log4j1 update or replace activity]({% post_url 2022-01-20-log4j-upgrade %})

Release notes: ( [2.21.0](https://github.com/geoserver/geoserver/releases/tag/2.21.0), 
[2.21-RC](https://github.com/geoserver/geoserver/releases/tag/2.21-RC)  )
