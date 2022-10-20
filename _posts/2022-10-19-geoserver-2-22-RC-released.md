---
author: Jody Garnett
date: 2022-10-19
layout: post
title: GeoServer 2.22-RC Release Candidate
categories:
- Announcements
tags:
- Release
release: release_222
version: 2.22-RC
jira_version: 16854
---

GeoServer [2.22-RC](/release/2.22-RC/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22-RC/geoserver-2.22-RC-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22-RC/geoserver-2.22-RC-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22-RC/GeoServer-2.22-RC-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22-RC/geoserver-2.22-RC-htmldoc.zip/download), [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22-RC/extensions/), and [data directory](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22-RC/geoserver-2.22-RC-data.zip/download). This release is also available as an [Docker image](https://github.com/geoserver/docker).

This is a release candidate intended for public review and feedback.

Thanks to Jody Garnett (GeoCat) for making this release candidate.

### Release candidate public testing and feedback

Testing and providing feedback on releases is part of the open-source social contract. The development team (and their employers and customers) are responsible for sharing this great technology with you.

*The collaborative part of open-source happens now - we ask you to test this release candidate in your environment and with your data. Try out the new features, double check if the documentation makes sense, and most importantly let us know!**

*If you spot something that is incorrect or not working do not assume it is obvious and we will notice. We request and depend on your [email](https://geoserver.org/comm/) and [bug reports](https://geoserver.org/issues/) at this time. If you are working with [commercial support](https://geoserver.org/support/) your provider is expected to participate on your behalf.*

Keeping GeoServer sustainable as a long term community commitment. If you are unable to contribute time, [sponsorship options](https://github.com/geoserver/geoserver/wiki/Sponsor) are available via OSGeo.

### Natural Earth GeoPackage and workspace

The sample [data directory](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22-RC/geoserver-2.22-RC-data.zip/download) now includes a small geopackage generated from [Natural Earth](https://www.naturalearthdata.com) data. These layers are a good example with multiple styles, and complete descriptions from the natural earth project.

![World map](/img/posts/2.22/world-map-rc.png) <br/>

Thanks to Jody Garnett (GeoCat) and for the attendees of the FOSS4G [GeoServer Beginner Workshop](https://docs.google.com/presentation/d/1fbPLN-1Cs95WK-IxDG1PxCEKyHwFbNBGNkkomxmLr0Y/edit?usp=sharing).

### User Manual Getting Started updated

The user manual has been revised with:

* [Getting started](https://docs.geoserver.org/latest/en/user/gettingstarted/index.html) revised with new sections for geopackage, image, layer group and style.
  
* [Tutorials](https://docs.geoserver.org/latest/en/user/tutorials/index.html) now provides an index of all tutorials across the user manual 

Thanks to Jody Garnett (GeoCat) and the attendees of the FOSS4G [GeoServer Beginner Workshop](https://docs.google.com/presentation/d/1fbPLN-1Cs95WK-IxDG1PxCEKyHwFbNBGNkkomxmLr0Y/edit?usp=sharing).

### Welcome Page Updates

**Layout**

The welcome page description provides a summary of the workspaces and layers available to the current user.

The header includes welcome message and a link to the organization providing the service.

Each web services is listed using the service title as a heading, followed by the service abstract as a description. The protocols provided by the service are displayed as blocks linking to web service URL. These are the URLs used to access the service in a desktop or web application.

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

For more information see [workspace web services](https://docs.geoserver.org/latest/en/user/webadmin/welcome.html#workspace-web-services) and [layer web services](https://docs.geoserver.org/latest/en/user/webadmin/welcome.html#layer-web-services) in the user manual.

**Contact Information**

Contact information now include welcome message to be used as introduction on the welcome page for the global services. Editing the contact details for a workspace will override this introduction for visitors viewing the workspace services.

To customize the welcome page header introduction contact information *welcome* is required. To customize the welcome page header *For more information visit* link both  *organization* and *online resource* is required. If this information is not provided the sentence linking to your organization will not be shown in the header.

![Contact Information : Organization](/img/posts/2.22/contact-organization.png) <br/>

To customize the welcome page footer *Contact administrator* link contact information for *email address* is required. If this information is not provided the sentence inviting visitors to contact the administrator will not be shown in the footer.

![Contact Information : Primary Contact](/img/posts/2.22/contact-primary.png) <br/>

These fields, including the email address, make use of GeoServer internationalization facilities allowing the welcome page to be customized for all your visitors.

For background information visit [GSIP-202](https://github.com/geoserver/geoserver/wiki/GSIP-202). Thanks to Jody Garnett and the GeoCat Live product for these improvements.

### Startup logging messages

GeoServer performs some initial setup when setting up a data directory for the first time:

* The built-in logging profiles are unpacked into ``logs/`` folder
* The ``security/`` folder is setup

In the past this initialization produced some warnings (when checking for files that were not yet created). These warnings were misleading giving the impression that GeoServer was installed incorrectly.

Startup logs now use the ``CONFIG`` log level during startup (previously ``INFO`` was used).

### Logging profile date formatting updates

The built-in logging profiles have been updated as the date was being incorrectly logged:

* If you have hand edited any of the built-in logging profiles you can fix the data format manually. Locate appender ``PatternLayout`` entries and correct the date formatting to ``%date{dd MMM HH:mm:ss}``.

* If you have not modified any of the built-in logging profiles a quick way to update is to remove them from your GEOSERVER_DATA_DIRECTORY``logs`` folder.
  
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

[Hyperspectral sensors](https://en.wikipedia.org/wiki/Hyperspectral_imaging) collect information at a very high spectral resolution, producing images with hundreds of bands. The typical pixel interleaved layout, where all the bands of a single pixel are stored toghether, is particuarly inefficient while rendering a false color image,
where only three of them are used. A band interleaved, where each band is stored in a separate bank, is more efficient. GeoServer used to load
band interleaved images in an inefficient way, but that has been handled, improving both memory usage and rendering performance, in proportion to the number of bands found in the GeoTIFF. For the typical hyperspectral image, that implies an improvement of a couple of orders of magnitude.

![Hyperspectral images](/img/posts/2.22/HyperspectralCube.jpg) <br/>

The second use case involves mosaicking hundreds of images, under the notion that each one has a significant number of overviews.
Showing the entire mosaick involves opening all these files, fetching the smallest overview, and mosaicking the result: the process
used to be slow and very memory intensive (going with the square of the output image size). 
The implementation has been improved so that the memory used in now linear with the output image size, and the amount of processing
has been reduced as well, providing again a couple of orders or magnitude speed up when mosaicking several hundreds small images.

![Mosaicking many little images](/img/posts/2.22/African_mosaic_ESA360518.jpg) <br/>

### Community modules news

News about community modules improvements, and new community modules you'll find in the 2.22.x series.

#### COG reader support for Azure

The COG reader community module now supports COGs stored in Azure as well.
The location of the COG can be provided as a HTTP(s) link, while eventual access credentials should be provided as system properties:


System Property | Description
-------------- | -----------
azure.reader.accountName | The Azure account name
azure.reader.accountKey | The Azure account key
azure.reader.container | The Azure container for the blobs
azure.reader.prefix | The optional prefix folder for the blobs

#### STAC datastore and mosaicking

A new community module, [STAC datastore](https://docs.geoserver.org/latest/en/user/community/stac-datastore/index.html, allows connecting
to a STAC catalog implementing the STAC API, and serve collections as vector layers, and items as features in said layers, with full filtering
and time dimension support, if the server implements a CQL2 search.

![STAC store](/img/posts/2.22/stac-store-configuration.png) <br/>

The store can also be used as an index for an image mosaic, if the STAC API assets points to accessible Cloud Optimized GeoTIFFs.

![STAC mosaic](/img/posts/2.22/stac-store-mosaic.png) <br/>


#### Vector mosaicking datastore

The [vector mosaic datastore](https://docs.geoserver.org/main/en/user/community/vector-mosaic/index.html) allows indexing many smaller vector stores (e.g., shapefiles, FlatGeoBuf) and serving them as a single, seamless data source.

An index table is used to organize them, know their location on the file system (or blob storage) and their footprint, along with eventual
variables that can be used for quick filtering (e.g., time, collecting organization, and so on). 

This can have some advantages compared to the typical database storage:
* Cheaper, when dealing with very large amounts of data in the cloud, as blob storage costs a fraction of an equivalent database.
* Faster for specific use cases, e.g, when extracting a single file and rendering it fully is the typical use case (e.g. tractor tracs in a precision farming application). This happens because the file splitting de-facto imposes and efficient data partitioning, and shapefile access excels at returning the whole set of features (as opposed to a subset).

![STAC mosaic](/img/posts/2.22/vector-mosaic-store.png) <br/>

### Improvements and Fixes

New Feature:

* [GEOS-10651](https://osgeo-org.atlassian.net/browse/GEOS-10651) Incorporate Vector Mosaic Datastore

* [GEOS-10629](https://osgeo-org.atlassian.net/browse/GEOS-10629) Features Templating - Allow control over encodign of complex attribute with n cardinality

* [GEOS-10610](https://osgeo-org.atlassian.net/browse/GEOS-10610) Selective cache reset on stores and resources, via REST API

* [GEOS-10587](https://osgeo-org.atlassian.net/browse/GEOS-10587) Allow DataStore to auto disable on connection failure

* [GEOS-10524](https://osgeo-org.atlassian.net/browse/GEOS-10524) promote gs-metadata to extension \(GSIP 212\)\)

* [GEOS-4613](https://osgeo-org.atlassian.net/browse/GEOS-4613) Expose more JVM statistics on the web gui

* [GEOS-10472](https://osgeo-org.atlassian.net/browse/GEOS-10472) promote gs-csw-iso to extension \(GSIP 211\)


Improvement:

* [GEOS-10696](https://osgeo-org.atlassian.net/browse/GEOS-10696) Allow configuration of Output Format types allowed in GetFeature

* [GEOS-10677](https://osgeo-org.atlassian.net/browse/GEOS-10677)  Improve cleanup of multi part form upload to the dispatcher

* [GEOS-10676](https://osgeo-org.atlassian.net/browse/GEOS-10676) Support uploading .bmp and .gif images as SLD Package icons through restconfig

* [GEOS-10644](https://osgeo-org.atlassian.net/browse/GEOS-10644) Keycloak - Improvements to Role Service

* [GEOS-10639](https://osgeo-org.atlassian.net/browse/GEOS-10639) Keycloak Filter - Allow to use a button to reach keycloak login page

* [GEOS-10637](https://osgeo-org.atlassian.net/browse/GEOS-10637) Keycloak filter configurability improvements

* [GEOS-10581](https://osgeo-org.atlassian.net/browse/GEOS-10581) Support native GeoTIFF band selection

* [GEOS-10580](https://osgeo-org.atlassian.net/browse/GEOS-10580) Server status page improvements for status, modules and docs

* [GEOS-10514](https://osgeo-org.atlassian.net/browse/GEOS-10514)   Better capture catalog configuration issues: layergroup with a misconfigured layer

* [GEOS-10505](https://osgeo-org.atlassian.net/browse/GEOS-10505) Display style format as new column in Styles-list, along with Style Name and Workspace

* [GEOS-10501](https://osgeo-org.atlassian.net/browse/GEOS-10501) GetMap: support auth headers forwarding to remote SLD urls

* [GEOS-10495](https://osgeo-org.atlassian.net/browse/GEOS-10495) Request Logger Memory Buffer Limits

* [GEOS-10464](https://osgeo-org.atlassian.net/browse/GEOS-10464) Improve logging and check for NPEs and other issues in Importer Module

For the complete list see [2.22-M0](https://github.com/geoserver/geoserver/releases/tag/2.22-RC) release notes.

## About GeoServer 2.22

Release notes:
( [2.22-RC](https://github.com/geoserver/geoserver/releases/tag/2.22-RC)
| [2.22-M0](https://github.com/geoserver/geoserver/releases/tag/2.22-M0)
)

* [CSW ISO Metadata](https://docs.geoserver.org/latest/en/user/extensions/csw-iso/index.html) extension

* [State of GeoServer](https://docs.google.com/presentation/d/1mnOFSvYb8npVudvUR5MSjSTFHc6ZQ_bStafZrBV7LZ8/edit?usp=sharing) (FOSS4G Presentation)
* [GeoServer Beginner Workshop](https://docs.google.com/presentation/d/1fbPLN-1Cs95WK-IxDG1PxCEKyHwFbNBGNkkomxmLr0Y/edit?usp=sharing) (FOSS4G Workshop)
* [Welcome](https://docs.geoserver.org/latest/en/user/webadmin/welcome.html) (User Guide)
