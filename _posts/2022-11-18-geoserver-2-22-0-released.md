---
author: Martha Nagginda
date: 2022-11-18
layout: post
title: GeoServer 2.22.0 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_222
version: 2.22.0
jira_version: 16867
---

GeoServer [2.22.0](/release/2.22.0/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.0/geoserver-2.22.0-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.0/geoserver-2.22.0-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.0/GeoServer-2.22.0-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.0/geoserver-2.22.0-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.0/extensions/).

This is a stable release of the GeoServer 2.22.x series, made in conjunction with GeoTools 28.0 
and GeoWebCache 1.22.0.

All major new features have been described in the [Release Candidate (RC) Blog post]({% post_url 2022-10-19-geoserver-2-22-RC-released %}).

Thanks to Martha Nagginda (GeoSolutions) and Andrea Aime (GeoSolutions) for making this release.

We would like to thank everyone who helped test the [release candidate]({% post_url 2022-10-19-geoserver-2-22-RC-released %}): Russell Grew, Georg Weickelt, Jukka Rahkonen, David Blasby, Graham Humphries, and everyone too shy to email the public list.


### Natural Earth GeoPackage and workspace

The sample [data directory](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22-RC/geoserver-2.22-RC-data.zip/download) now includes a small geopackage generated from [Natural Earth](https://www.naturalearthdata.com) data. These layers are good examples with multiple styles, and include complete descriptions from the Natural Earth project.

![World map](/img/posts/2.22/world-map-rc.png) <br/>

Thanks to Jody Garnett (GeoCat), David Blasby (GeoCat), and the attendees of the FOSS4G [GeoServer Beginner Workshop](https://docs.google.com/presentation/d/1fbPLN-1Cs95WK-IxDG1PxCEKyHwFbNBGNkkomxmLr0Y/edit?usp=sharing).

### User Manual Getting Started updated

The user manual has been revised. Changes include:

* [Getting started](https://docs.geoserver.org/latest/en/user/gettingstarted/index.html) has been updated and includes with new sections for GeoPackage, image, layer group and style.
  
* [Tutorials](https://docs.geoserver.org/latest/en/user/tutorials/index.html) now provides an index of all tutorials across the user manual 

Thanks to Jody Garnett (GeoCat) and the attendees of the FOSS4G [GeoServer Beginner Workshop](https://docs.google.com/presentation/d/1fbPLN-1Cs95WK-IxDG1PxCEKyHwFbNBGNkkomxmLr0Y/edit?usp=sharing).

### Welcome Page Updates

**Layout**

The welcome page description provides a summary of the workspaces and layers available to the current user.

The header includes a welcome message and a link to the organization providing the service.

Each web service is listed using the service title as a heading, followed by the service abstract as a description. The protocols provided by the service are displayed as blocks linking to the web service URL. These are the URLs used to access the service in a desktop or web application.

![Welcome layout](/img/posts/2.22/welcome-layout-rc.png) <br/>

The services shown are based on the permissions of the current user. As an example when logged in as an Administrator the REST API service is shown with a link to the API endpoint.

![REST API](/img/posts/2.22/welcome-rest.png) <br/>

For more information on the welcome page and an example of how to use service URLs in QGIS visit the user manual [Welcome](https://docs.geoserver.org/latest/en/user/webadmin/welcome.html) reference page.

**Workspace and Layer Selection**

Use the top-right corner of the welcome page to:

* Select workspace to browse workspace web services
* Select layer and layergroup for layer specific web services

You can book mark or share this page (which is great for providing a team or project with its own distinct web services and landing page).

![Welcome workspace](/img/posts/2.22/welcome-workspace-rc.png) <br/>

For more information on this functionality see [workspace web services](https://docs.geoserver.org/latest/en/user/webadmin/welcome.html#workspace-web-services) and [layer web services](https://docs.geoserver.org/latest/en/user/webadmin/welcome.html#layer-web-services) in the user manual.

Using a **workspace virtual web service** is great if you are setting up a GIS project, supporting a web application, or providing GIS services for a team. This is especially true as it is [straight forward](https://docs.geoserver.org/latest/en/user/data/webadmin/workspaces.html#security) to manage security on a workspace basis.

![Welcome layer](/img/posts/2.22/welcome-workspace-header.png) <br/>

Using a **layer virtual web service** is great when registering a layer with a catalogue service such as GeoNetwork. It provides a web service that can only be used to access a single layer.

![Welcome layer](/img/posts/2.22/welcome-layer-header.png) <br/>

For the technical background on this feature see [Virtual web services](https://docs.geoserver.org/latest/en/user/configuration/virtual-services.html) in the user manual. This functionality has been present in GeoServer for a long time; but because it required hand editing URLs many users were not aware of capability.

**Contact Information and Service Metadata**

Contact information now includes a welcome message to be used as introduction on the welcome page for the global services. Editing the contact details for a workspace will override this introduction for visitors viewing the workspace services.

To customize the welcome page header introduction the **welcome** field is used. To append a welcome page header *For more information visit* link both  **organization** and **online resource** are required.

![Contact Information : Organization](/img/posts/2.22/contact-organization.png) <br/>

To customize the welcome page footer *Contact administrator* link contact information for **email address** is required. If this information is not provided the sentence inviting visitors to contact the administrator will not be shown in the footer.

![Contact Information : Primary Contact](/img/posts/2.22/contact-primary.png) <br/>

To customize the service heading and description shown vist a service configuration page. Edit the service **title** and **abstract** and the change will be reflected on the welcome page (and in the GetCapabilities document shared with web clients). Disabled services are not available and not listed.

![WMS : Service Metadata](/img/posts/2.22/wms-service.png) <br/>

Disabling **global services** prevents any services from being accessable or listed on the initial welcome page.

![Disable global services](/img/posts/2.22/global-services.png) <br/>

All these fields, including the email address, make use of GeoServer [internationalization](https://docs.geoserver.org/latest/en/user/configuration/internationalization/index.html) allowing the welcome page to be customized for all your visitors.

For background information visit [GSIP-202](https://github.com/geoserver/geoserver/wiki/GSIP-202). Thanks to Jody Garnett and the GeoCat Live product for these improvements.

### Startup logging messages

GeoServer performs some initial setup when setting up a data directory for the first time:

* The built-in logging profiles are unpacked into ``logs/`` folder
* The ``security/`` folder is setup

In the past this initialization produced some warnings (when checking for files that were not yet created). These warnings were misleading giving the impression that GeoServer was installed incorrectly.

Please note that startup logs now use the ``CONFIG`` log level during startup one level lower thatn ``INFO``. This change allows logging profiles to filter out the startup process while still retaining information messages on service operation and use.

### Logging profile date formatting updates

The built-in logging profiles have been updated as the date was being incorrectly logged:

* If you have hand edited any of the built-in logging profiles you can fix the data format manually. Locate appender ``PatternLayout`` entries and correct the date formatting to ``%date{dd MMM HH:mm:ss}``.

* If you have not modified any of the built-in logging profiles a quick way to update is to remove them from your GEOSERVER_DATA_DIRECTORY ``logs`` folder.
  
  The built-in logging profiles will be restored next time you change profiles or when the application starts up. 

* If you never plan to customize the built-in loggig profiles use the system property ``UPDATE_BUILT_IN_LOGGING_PROFILES=true``. This setting will cause GeoServer to update the files when changing profiles or on application startup.
  
  This setting only affects the built-in logging profiles; any new logging profiles that you have
  made manually are unaffected.

For more information see the user guide on [built-in logging profiles](https://docs.geoserver.org/latest/en/user/configuration/logging.html#built-in-logging-profiles).

### Style format

The styles list provides a **Format** column indicating the format used.

![World map](/img/posts/2.22/styles.png) <br/>

Thanks to Mohammad Mohiuddin Ahmed for this change.

### CSW ISO and Metadata extension

To support the use of the CSW module the [Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/metadata/index.html) provides a tab for editing metadata as part of layer configuration. It also provides a REST API for bulk metadata activities including importing from GeoNetwork.

The [CSW ISO Metadata](https://docs.geoserver.org/latest/en/user/extensions/csw-iso/index.html) profile is now available as an extension.  

![Metadata tab](/img/posts/2.22/metadata.png) <br/>

For background information see [GSIP-211](https://github.com/geoserver/geoserver/wiki/GSIP-211).

Thanks to Niels for for this work.

### Significant improvements in raster rendering performance

Raster rendering performance has increased significantly for two specific use cases:

* GeoTIFF hyperspectral images, with hundreds of bands, and band interleaved structure 
* Mosaicking hundreds of small images

[Hyperspectral sensors](https://en.wikipedia.org/wiki/Hyperspectral_imaging) collect information at a very high spectral resolution, producing images with hundreds of bands. The typical pixel interleaved layout, where all the bands of a single pixel are stored together, is particularly inefficient while rendering a false color image,
where only three of them are used. A band interleaved, where each band is stored in a separate bank, is more efficient. GeoServer previously loaded
band interleaved images in an inefficient way, but that has been handled, improving both memory usage and rendering performance, in proportion to the number of bands found in the GeoTIFF. For the typical hyperspectral image, that implies an improvement of a couple of orders of magnitude.

![Hyperspectral images](/img/posts/2.22/HyperspectralCube.jpg) <br/>

The second use case involves mosaicking hundreds of images, under the notion that each one has a significant number of overviews.
Showing the entire mosaick involves opening all these files, fetching the smallest overview, and mosaicking the result: the process
used to be slow and very memory intensive (going with the square of the output image size). 
The implementation has been improved so that the memory used in now linear with the output image size, and the amount of processing
has been reduced as well, providing again a couple of orders or magnitude speed up when mosaicking several hundreds small images.

![Mosaicking many little images](/img/posts/2.22/African_mosaic_ESA360518.jpg) <br/>

Thanks to Andrea Aime (GeoSolutions) for these improvements.


### Translation updates

Alexandre has successfully experimented with setting up a [Transfex GeoServer GitHub Integration](https://www.transifex.com/GeoServer/geoserver-github-integration/) synchronization.

![translation](/img/posts/2.22/transifex_sync.png) <br/>

Priority has been given to translating the new welcome page functionality, shown here translation into Dutch by Sander.

![welcome nl](/img/posts/2.22/welcome-nl.png) <br/>

Carsten Klein started an effort to make the german translation more consistant, settling on terms like Gruppenlayer when updating the user interface.

![welcome nl](/img/posts/2.22/welcome-de.png) <br/>

Thanks to Alexandre Gacon, Carsten Klein, Marc Jansen, Sander Schaminee, and everyone who helped work on translations for the new functionality.

* [GEOS-10750](https://osgeo-org.atlassian.net/browse/GEOS-10750) German Translation Overhaul Part 1

### YSLD SLD Properties

The YSLD style format is focused on defining a feature type style (generating the sld and named layer wrapper since they are not used when drawing a single layer). This update allows the sld and named layer wrappers to be configured.

```yaml
sld-title: Civic Information
layer-name: poi
title: Point of Interest
rules:
- title: Locations
  symbolizers:
  - point:
      symbols:
      - mark:
          shape: x
          fill-color: '#0099cc'
          stroke-color: 'black'
          stroke-width: 0.5
```

In the above example ``layer-name`` is used by GeoServer's dynamic styling to identify the layer to draw.

Thanks to Steve Ikeoka for this improvement.

* [GEOT-7210](https://osgeo-org.atlassian.net/browse/GEOT-7210) YSLD styles does not parse/encode layer name

### Community modules news

News about community modules improvements, and new community modules you'll find in the 2.22.x series.

A reminder that GeoServer community modules are still being worked on and are not directly available for download. If you are interested in these topics please support their completion directly by compiling the source code and contributing; or financially by sponsoring or contracting the development team working on the activity.

#### COG reader support for Azure

The COG reader community module now supports COGs stored in Azure as well.
The location of the COG can be provided as a HTTP(s) link, while eventual access credentials should be provided as system properties:

System Property | Description
-------------- | -----------
azure.reader.accountName | The Azure account name
azure.reader.accountKey | The Azure account key
azure.reader.container | The Azure container for the blobs
azure.reader.prefix | The optional prefix folder for the blobs

To support this activity contact Daniele (GeoSolutions).

#### STAC datastore and mosaicking

A new community module, [STAC datastore](https://docs.geoserver.org/latest/en/user/community/stac-datastore/index.html, supports connecting
to a STAC catalog implementing the STAC API, and serve collections as vector layers, and items as features in said layers, with full filtering
and time dimension support, if the server implements a CQL2 search.

![STAC store](/img/posts/2.22/stac-store-configuration.png) <br/>

The store can also be used as an index for an image mosaic, if the STAC API assets points to accessible Cloud Optimized GeoTIFFs.

![STAC mosaic](/img/posts/2.22/stac-store-mosaic.png) <br/>

To support this activity contact Andrea (GeoSolutions).

#### Vector mosaicking datastore

The [vector mosaic datastore](https://docs.geoserver.org/main/en/user/community/vector-mosaic/index.html) allows indexing many smaller vector stores (e.g., shapefiles, FlatGeoBuf) and serving them as a single, seamless data source.

An index table is used to organize them, know their location on the file system (or blob storage) and their footprint, along with eventual
variables that can be used for quick filtering (e.g., time, collecting organization, and so on). 

This can have some advantages compared to the typical database storage:
* Cheaper, when dealing with very large amounts of data in the cloud, as blob storage costs a fraction of an equivalent database.
* Faster for specific use cases, e.g, when extracting a single file and rendering it fully is the typical use case (e.g. tractor tracks in a precision farming application). This happens because the file splitting de-facto imposes and efficient data partitioning, and shapefile access excels at returning the whole set of features (as opposed to a subset).

![STAC mosaic](/img/posts/2.22/vector-mosaic-store.png) <br/>

To support this activity contact Andrea (GeoSolutions).

### Improvements and Fixes

#### Improvement

* [GEOS-10717](https://osgeo-org.atlassian.net/browse/GEOS-10717) XStreamServiceLoader performance improvement with XstreamPersister caching

* [GEOS-10718](https://osgeo-org.atlassian.net/browse/GEOS-10718) \[OIDC\] the OIDC plugin does not currently take into account the id\_token\_hint parameter

* [GEOS-10735](https://osgeo-org.atlassian.net/browse/GEOS-10735) Obfuscate secret key in S3 Blob Store, avoiding requiring reentry when editing and HTML source visibility

* [GEOS-10739](https://osgeo-org.atlassian.net/browse/GEOS-10739) Contact information user interface feedback for welcome message

* [GEOS-10740](https://osgeo-org.atlassian.net/browse/GEOS-10740) Service enabled does not respect minimal/custom service names

#### New Feature

* [GEOS-10734](https://osgeo-org.atlassian.net/browse/GEOS-10734) SpatialJSON WFS output format community module

#### Task

* [GEOS-10721](https://osgeo-org.atlassian.net/browse/GEOS-10721) Bump jettison from 1.4.1 to 1.5.1

#### Bug

* [GEOS-4727](https://osgeo-org.atlassian.net/browse/GEOS-4727) Editing SQL views seems to be leaking connections

* [GEOS-10667](https://osgeo-org.atlassian.net/browse/GEOS-10667) WFS: inconsistent srsDimension=4 with topp:tasmania\_roads layer

* [GEOS-10707](https://osgeo-org.atlassian.net/browse/GEOS-10707) GeoFence internal LayerGroup Limit merge inconsistency

* [GEOS-10709](https://osgeo-org.atlassian.net/browse/GEOS-10709) Schemaless Features - Simplified property access might return values for wrong property names

* [GEOS-10710](https://osgeo-org.atlassian.net/browse/GEOS-10710) Features Templating backward mapping with back xpath \('../my/property/name'\) doesn't work

* [GEOS-10714](https://osgeo-org.atlassian.net/browse/GEOS-10714) DefaultGeoServerFacade throws ConcurrentModificationException for workspace settings and services

* [GEOS-10729](https://osgeo-org.atlassian.net/browse/GEOS-10729) Concurrent access on data access rules \(authorization\) can lead to loss of configured catalog mode, and lost rules

* [GEOS-10731](https://osgeo-org.atlassian.net/browse/GEOS-10731) GWC variable Parameterization does not work with geoserver-environment.properties due to the bean initialization order

* [GEOS-10736](https://osgeo-org.atlassian.net/browse/GEOS-10736) OSEO product creation via REST API fails if the product id starts with a valid ISO date

* [GEOS-10737](https://osgeo-org.atlassian.net/browse/GEOS-10737) GeoCSS misses support for labelInFeatureInfo and labelAttributeName vendor options

* [GEOS-10741](https://osgeo-org.atlassian.net/browse/GEOS-10741) Remove deprecated YUI usage

For complete information see [2.22.0 release notes](https://github.com/geoserver/geoserver/releases/tag/2.22.0).

### About GeoServer 2.22

Additional information on GeoServer 2.22 series:

* [Update Instructions](https://docs.geoserver.org/latest/en/user/installation/upgrade.html)
* [Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/metadata/index.html)
* [CSW ISO Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/csw-iso/index.html)
* [State of GeoServer](https://docs.google.com/presentation/d/1mnOFSvYb8npVudvUR5MSjSTFHc6ZQ_bStafZrBV7LZ8/edit?usp=sharing) (FOSS4G Presentation)
* [GeoServer Beginner Workshop](https://docs.google.com/presentation/d/1fbPLN-1Cs95WK-IxDG1PxCEKyHwFbNBGNkkomxmLr0Y/edit?usp=sharing) (FOSS4G Workshop)
* [Welcome page](https://docs.geoserver.org/latest/en/user/webadmin/welcome.html) (User Guide)

Release notes:
( 
  [2.22.0](https://github.com/geoserver/geoserver/releases/tag/2.22.0) |
  [2.22-RC](https://github.com/geoserver/geoserver/releases/tag/2.22-RC)
| [2.22-M0](https://github.com/geoserver/geoserver/releases/tag/2.22-M0)
)
