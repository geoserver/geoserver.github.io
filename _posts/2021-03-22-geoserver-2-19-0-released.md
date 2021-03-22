---
author: Andrea Amie
date: 2021-03-22
layout: post
title: GeoServer 2.19.0 Released
categories:
- Announcements
tags:
- Release
---

We are happy to announce GeoServer [2.19.0](/release/2.19.0/) release is available for download  ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.0/geoserver-2.19.0-bin.zip/download) and [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.0/geoserver-2.19.0-war.zip/download)) along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.0/geoserver-2.19.0-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.0/extensions/).

This GeoServer 2.19.0 release was produced in conjunction with GeoTools 25.0 and GeoWebCache 1.19.0.

Thanks to everyone who contributed and helped test this release. Developer adding new features are credited in the sections below. Release candidate testing was performed by Andrea Aime, Bart Verbeeck, Christoforos Vradis, Georg Weickelt, Graham Humphries, Ian Turton, Jody Garnett, Peter Rushforth, Richard Duivenvoorde, Russell Grew, and Simone Giannecchini. With all the new extensions being added we appreciated those testing the release candidate packaging.

Thanks to Alessandro Parma (GeoSolutions) and Andrea Aime (GeoSolutions) for making this release.

## MapML extension

In this release, MapML has graduated from community module to extension status. 
Map Markup Language (MapML) is a proposed extension to HTML, for maps. 
The objective of the project is to standardize accessible, performant Web maps 
with native support from Web browsers (maps in HTML). The GeoServer MapML extension 
will closely track the MapML specification as it evolves. Find out more at 
https://maps4html.org/, and if you like our goals, join the community group!

The MapML extension works with GeoServer layers and layer groups, and uses WMS,
WMTS and WFS facilities built into GeoServer to provide simple map previews layers.
The layer previews can be "dragged" from one browser tab onto another map preview to
visualize a mashup of the layers of layer groups using the built in MapML viewer.

![MapML Layer properties panel](/img/posts/2.19-RC/mapml-layers-panel.png)<br/>
*Editing a layer's MapML properties in the Layers panel*

![MapML gridsets in the Layers Tile Caching tab](/img/posts/2.19-RC/mapml-gridsets.png)<br/>
*Editing a layer's MapML gridsets in the Layers panel Tile Caching tab*

![MapML Preview link is added to the Layer Preview page](/img/posts/2.19-RC/mapml-layer-preview-list.png)<br/>
*Preview a layer in the MapML viewer by following the MapML link*

![MapML previews can be mashed up by dragging the URL of one preview onto another](/img/posts/2.19-RC/mapml-preview-mashup.png)<br/>
*Mash up MapML previews by drag and drop*

The Maps for HTML community would like to thank Andrea Aime, Jody Garnett and the 
GeoServer PSC for their support and help in getting this extension published.

More information on the GeoServer MapML extension is available in the 
[user guide](https://docs.geoserver.org/latest/en/user/extensions/mapml/index.html)

## WPS JDBC extension

The WPS JDBC extension allows to share the status of asynchronous WPS requests across a GeoServer cluster. The status of 
all requests, past and ongoing, can be stored in a database, for later reference.

The module uses GeoTools JDBC stores to access databases, create the necessary tables, and track status. 
Connection parameters are provided as property files, e.g.:


```
user=postgres
port=5432
password=******
passwd=******
host=localhost
database=gsstore
driver=org.postgresql.Driver
dbtype=postgis
```

For more information, refer to the [module documentation](https://docs.geoserver.org/latest/en/user/extensions/wps-jdbc/index.html).

We'd like to thank Ian Turton for developing the module on behalf of GeoSolutions, Alessio Fabiani (GeoSolutions) for providing
documentation for it, and Andrea Aime (GeoSolutions) for performing the QA and graduation steps.

## WPS Download extension

The WPS download plugin provides support for the download of large amounts of data,
allowing use of asynchronous requests, where using WFS, WCS or WMS for the same task would lead to HTTP timeouts.
Also, download limits can be configured to avoid excessively large requests: size in MB, number of features, number
of animation frames.

In particular, the following processes are available:

*  ``DownloadEstimator``, verifying that a raster/vector download about to be attempted will fit the download limits.
* ``DownloadProcess``, allowing to download either raster or vector data, reproject and clip them
* ``DownloadMapProcess``, allows to download a large map matching what is visible on a client (which may be using tiles and display on a multi-screen), eventually dynamically fetching layers from remote WMS servers as well. It's also possible to decorate the final map using the standard [decoration layouts](https://docs.geoserver.org/latest/en/user/services/wms/decoration.html#wms-decorations).
* ``DownloadAnimationProcess``, allows to build a MP4 movie given a set of layers and times.

GeoNode uses the module to allow download of datasets, eventually clipped and filtered to the current view. The asynchronous download allows
to download large datasets, and retrieve them later, once ready.

![GeoNode download](/img/posts/2.19-RC/geonode_download_1.png)<br/>
*Initiating a download in GeoNode*

![GeoNode download](/img/posts/2.19-RC/geonode_download_2.png)<br/>
*Configuring the download*

![GeoNode download](/img/posts/2.19-RC/geonode_download_3.png)<br/>
*The download package is ready*

![GeoNode download](/img/posts/2.19-RC/geonode_download_4.png)<br/>
*Viewing the clipped download in QGIS*

For more information, refer to the [module documentation](https://docs.geoserver.org/latest/en/user/extensions/wps-download/index.html).

Thanks to Alessio, Andrea, Daniele, from GeoSolutions, for developing the extension, and GeoNode/MapStore for testing it in various production environments.

## WMTS Multidimensional extension

The WMTS multi-dimensional extension is an extension to the WMTS protocol developed during OGC Testbed 12. The extension allows to explore 
the dimensions attached to a dataset, providing ways to explore them, finding relationships between them.

Here are a couple of real world examples of this functionality:

* GeoServer is publishing a set of satellite images. Each image is time stamped. The user is browsing the set of data on a map, and the client software wants to show the list of available times for the current area. The WMS/WMTS dimension support cannot help, but the WMTS extension has a request,  ``GetDomainValues``, which exactly answers this question.
* GeoServer is publishing a set of NetCDFs containing weather forecasts. Each dataset has two times associated, a run time (the time the forecast was run) and a time (the predicted time for the weather data). Forecasts are run for the short term future, so the two times are strictly related. A user wants to compare forecasts for a given predicted time. The ``GetDomainValues``  request can be used to locate the run times that have a prediction for the given forecast time.
* GeoServer is publishing a set of timestamped data. The client wants to display a timeline, providing an idea of which times are available for the current view. In addition to that, the clients wants to display how many datasets are available along the timeline. The ``GetHistogram`` request can be used to retrieve a count of datasets available over time buckets in a given interval.

The [MapStore client](https://mapstore.readthedocs.io/en/latest/) uses the module to power its [timeline extension](https://mapstore.readthedocs.io/en/v2019.02.00/user-guide/timeline/), providing time discovery, navigation, animation, and histogram display.

![MapStore timeline plugin, with animation controls](/img/posts/2.19-RC/timeline-base.jpg "MapStore timeline plugin, with animation controls")<br/>
*MapStore timeline plugin, with animation controls*

![MapStore timeline plugin, histogram view](/img/posts/2.19-RC/timeline-histogram.jpg "MapStore timeline plugin, histogram view")<br/>
*MapStore timeline plugin, histogram view*

The plugin partially replaces the <a href="https://docs.geoserver.org/latest/en/user/tutorials/animreflector.html">WMS animator</a> functionality, which is going to be deprecated (since it's memory bound, and can only be accessed
with a synchronous request).

For more information, refer to the [module documentation](https://docs.geoserver.org/latest/en/user/extensions/wmts-multidimensional/index.html).

Thanks to Nuno Oliveira (GeoSolutions) and Andrea Aime (GeoSolutions) for the initial development, and MapStore for adopting the module, using it in production, and ensuring its long term development

## Params-extractor extension

The parameter extractor module is used to inject vendor parameters in all links that a standard OGC client uses, by either
reflecting them into the Capabilities documents backlinks, or hiding them in an extra component in the URLs paths.

This can be used, for example, to provide a desktop client, such as QGIS, a different view of a given layer based on ``viewparams``, ``cql_filter``
or ``env`` parameters, even if the client would not be able to use the parameters natively.
Each combination of parameters receives a different starting GetCapabilities request.

A simple query parameter echoing can be setup for clients honoring query parameters in capabilities backlinks:

![Parameter echoing](/img/posts/2.19-RC/param_extract_echo.png)<br/>
*Parameter extractor echoing*

For clients ignoring query parameters or even ignoring backlinks, the parameters can be added as a path component instead, and then expanded in a larger templated value:

![Parameter extraction](/img/posts/2.19-RC/param_extract_expand.png)<br/>
*Parameter expansion from path component*

With the above setup, a URL ending with ``H11``:

``
/geoserver/tiger/wms/H11?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap
``

is interpreted as:

``
/geoserver/tiger/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&CQL_FILTER=CFCC%3D%27H11%27
``

For more information, refer to the [module documentation](https://docs.geoserver.org/stable/en/user/extensions/params-extractor/index.html).

Thanks to Nuno Oliveira (GeoSolutions) for developing this module.


## GeoWebCache-S3 extension

The GeoWebCache S3 blobstore allows storage of GeoWebCache tiles in a S3 bucket. It has been also tested with a few other S3 compatible blob 
storage mechanisms, such as [Minio](https://min.io/).

This plugin is particularly useful when deploying GeoServer on AWS, but also when setting up a shared tile storage in Kubernetes.

![Parameter extraction](/img/posts/2.19-RC/gwc_s3.png)<br/>
*Setting up the S3 tile storage*

For more information, refer to the [module documentation](https://docs.geoserver.org/latest/en/user/extensions/gwc-s3/index.html).


## Retire ArcSDE Extensions

The ArcSDE Extension has been retired.
  
In this case we found that the extension is no longer actively used, and lacked sufficient feedback and resources for continued development. The last tested ArcSDE 10.2.2 version is no longer available, making the required jars required for installation unavailable.


## Retire the Script community module

The Script community module has been retired.

The module provided scripting abilities for GeoServer, allowing to add WPS processes and small REST services in scripting languages, 
and storing them in the data directory. 

Unfortunately the module fell un-maintained and would no longer build nor work.

## JTS 1.18.1

GeoServer 2.19.0 includes the latest JTS Topology Suite 1.18.1 release, the headline feature is an optional "Overlay Next Generation" implementation that should provide a performance improvement for operations such as tile generation, vector tiles, and get map requests. 

To try it out use the system property ``-Djts.overlay=ng`` - the effect should be small as we already have several optimizations in place before trying this now faster JTS Overlay.

Thanks to Martin Davis (Crunch Data) and James Hughes (CCRi) for making [JTS 1.18.1](https://github.com/locationtech/jts/releases/tag/jts-1.18.1) available  during our release window.

## Codebase updates and Quality Assurance

GeoServer continues to be build with the latest open source technologies:

* GeoTools 25.0
* GeoWebCache 1.19.0
* JTS 1.18.1
* JAI-EXT 1.1.19
* GeoFence 3.4.7
* Upgrade oshi-core from 5.4.0 to 5.5.0 for new Apple hardware support
* Freemarker 2.3.31
  
We do not get a chance to talk about the code-base that makes up GeoServer often, but recent changes and improvements deserve some praise. The GeoServer team has really embraced automating code checks, starting with simply formatting the code in a consistent fashion, to more advanced techniques checking for common mistakes.

* Switch most of the unit tests from JUnit 3 to JUnit 4
* Remove usage of Vector/Hashtable, replace with ArrayList and HashMap, add PMD rule to enforce it
* Remove un-necessary casts from code, add PMD rule to enforce it
* Replace try/finally with try-with-resources, add a PMD rule to enforce it
* Collapse catch statements with the same body in a multi-catch, add PMD rule to enforce it
* Avoid assertTrue for tests that can be expressed with dedicated assertions. Add PMD rule to enforce it.
* Replace iterator loops with enhanced for loops, add a QA rule to enforce it.
* Run PMD checks on test sources as well.
* Use Collection.isEmpty() when checking for item availability
* Remove explicit types when diamond operator can be used instead. Added a PMD rule to enforce it.
* Remove or suppress unchecked casts, enable the Java compiler lint option for it.

Although all these changes sound small in isolation, the fact that they are performed on the entire codebase, and checked each time a pull-request is proposed, really provides confidence in the technology we publish.

Thanks to Andrea for this valuable work.

## And more!

There are several other new features and improvements, including:

  * Upgrade SQL Server packaging to use open source JDBC driver
  * Setting Entity Expansion limit on WFS XML Readers
  * Tutorial on [running GeoServer in cloud foundry](https://docs.geoserver.org/latest/en/user/tutorials/cloud-foundry/run_cf.html).
  * Updated DB2 [installation instructions](https://docs.geoserver.org/latest/en/user/data/database/db2.html)
  

Find out more in the [release notes](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16814).

## About GeoServer 2.19

Additional information on GeoServer 2.19 series:

  * [Promote WMTS multidim to extension](https://github.com/geoserver/geoserver/wiki/GSIP-196)
  * [Promote WPS-Download to extension](https://github.com/geoserver/geoserver/wiki/GSIP-195)
  * [Promote params-extractor to extension](https://github.com/geoserver/geoserver/wiki/GSIP-194)
  * [Promote GWC-S3 to extension](https://github.com/geoserver/geoserver/wiki/GSIP-193)
  * [Promote WPS-JDBC to extension status](https://github.com/geoserver/geoserver/wiki/GSIP-197)
  * [Promote MapML to extension status](https://github.com/geoserver/geoserver/wiki/GSIP-200)
  * [GeoServer repository transition to main branch](main-branch.html)
  * Release notes ([2.19.0](https://osgeo-org.atlassian.net/jira/secure/ReleaseNote.jspa?projectId=10000&version=16814) &#124; [2.19-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16766) )
