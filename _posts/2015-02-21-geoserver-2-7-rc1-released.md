---
author: geoserver
comments: true
date: 2015-02-21 06:47:50+00:00
layout: post
link: http://blog.geoserver.org/2015/02/21/geoserver-2-7-rc1-released/
slug: geoserver-2-7-rc1-released
title: GeoServer 2.7-RC1 Released
wordpress_id: 2133
categories:
- Announcements
- Features
tags:
- release
---

The GeoServer team is pleased to announce the release of GeoServer [2.7-RC1](http://geoserver.org/release/2.7-RC1/) with some great new features. The download page for [2.7-RC1](http://geoserver.org/release/2.7-RC1/) provides links for [zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7-RC1/geoserver-2.7-RC1-bin.zip), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7-RC1/geoserver-2.7-RC1-war.zip), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7-RC1/geoserver-2.7-RC1.dmg), and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.7-RC1/geoserver-2.7-RC1.exe) bundles. As a release candidate, 2.7-RC1 is considered experimental  and is provided for testing purposes. This release is not recommended  for production (even if you are enthusiastic about the new features).




This release is made in conjunction with GeoTools 13-RC1 and GeoWebCache 1.7-RC1. Thanks to [Ben Caradoc-Davies](mailto:ben@transient.nz) ([Transient Software, New Zealand](http://transient.nz/)) for making this release, Kevin Smith ([Boundless](http://boundlessgeo.com/)) for releasing GeoWebCache 1.7-RC1, Jody Garnett ([Boundless](http://boundlessgeo.com/)) for building the dmg and testing, and a big thanks to Andrea Aime ([GeoSolutions](http://www.geo-solutions.it/)) for gathering up the  contents (and pictures) for this blog post, which is based almost entirely on his post announcing the release of 2.7-beta.




A complete [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20940) since 2.7-beta is available from the issue tracker.





### Please Download and Test


The committers have a great release for you to look forward to, we would like to ask you to **download and test**. By trying GeoServer out on a wide range of platforms and datasets we can all help the next release be great.


<blockquote>_Testing is a key part of the open source [social contract](http://www.how2map.com/2013/09/opensource-and-social-contract.html). This is your best chance to identify issues early while we still have time to do something about it. If you make use of [commercial support](http://geoserver.org/support/) ask your vendor about their plans for 2.7-RC1 testing._</blockquote>


When testing Geoserver 2.7-RC1 please let us know on the [user list](http://geoserver.org/comm/) how it works for you. We will be sure to thank you in the final release announcement and product presentations.


## New Features




### Color composition and blending


Color composition and blending are two new extensions to SLD allowing  the web map styler to control how overlapping layers in a map are  merged together. Beyond the simple stacking and translucency control a  wide range of effects are now possible by allowing masking and specific  color operations for blending layers together in new ways.

A common well known example is a polygon thematic map on top of a  DEM, which tends to provide under-par results using only transparency  control, but generates very appealing ones when using the "multiply"  blending mode:

[![](http://geoserver.wpengine.com/wp-content/uploads/2015/02/dem-multiply.jpg)](http://blog.geoserver.org/2015/01/22/geoserver-2-7-beta-released/dem-multiply/)

Alpha masking also allows for neat cartographic tricks, like the one  below, where the polygon fill has been cut at the border of the states  generating a "inner line" effect:

[![](http://geoserver.wpengine.com/wp-content/uploads/2015/02/nurc-NaturalEarthRaster_nurc-states1.jpg)](http://blog.geoserver.org/2015/01/22/geoserver-2-7-beta-released/nurc-naturalearthraster_nurc-states-3/)

Check out the documentation for a [list of supported operations and some examples](http://docs.geoserver.org/latest/en/user/styling/sld-extensions/composite-blend.html). We would like to thank [Cleveland Metroparks](http://www.clevelandmetroparks.com/) for sponsoring this improvement.


### WPS Clustering


[GSIP 119](https://github.com/geoserver/geoserver/wiki/GSIP%20119%20WPS%20clustering%20of%20asynchronous%20requests) added support for asynchronous requests over a cluster of GeoServer  instances. In WPS an asynchronous request starts by returning the client  a URL that can be polled in order to know about the execution progress,  and eventually to retrieve the final results.  Previous to 2.7-beta the  status information was kept in memory, thus only the GeoServer instance  running the process could meaningfully respond to a poll from the  client. With GeoServer 2.7-beta a new extension point allows the  programmer to create a process status repository that can be shared  among the GeoServer instances.

The first default implementation of the shared repository is a [Hazelcast based one](http://docs.geoserver.org/latest/en/user/extensions/wps/hazelcast-clustering.html),  leveraging in-memory, replicated and distributed maps to share the  state information, while the results (which can be pretty large) are  stored in a shared file system. The community is welcome to develop  other variants that could store the information in other places, for  example, a relational database, a nosql one, or in the cloud (e.g., S3  storage).


### WPS Security


[GSIP 121](https://github.com/geoserver/geoserver/wiki/GSIP-121) added the ability to provide fine grained access control to processes  based on our usual role based authentication system: each process or  group of processes can be associated to a list of roles that can access  them, while other users will be disallowed seeing or accessing the same  processes.

![../../_images/security-groups.png](http://docs.geoserver.org/latest/en/user/_images/security-groups.png)


### WPS Limits


Integrating with the security, [GSIP 123](https://github.com/geoserver/geoserver/wiki/GSIP%20123%20WPS%20input%20and%20execution%20limits) added support for process execution limits, bringing WPS up to par with  the other OGC services in terms of limiting the resources used by a  single request. In the main WPS panel one can now configure how much  processing time to give synchronous and asynchronous requests:

![../../_images/execution.png](http://geoserver.wpengine.com/wp-content/uploads/2015/02/execution.png)

Also, in the new process security page one can configure a global  limit for the size of complex inputs (see above), it is also possible to  configure limits on a process by process basis, in order to restrict  the size of inputs, the range of numerical values, and the multiplicity  of repeatable inputs, to constrain the effort of a WPS process call. All  these limits will be dutifully reflected in the DescribeProcess output.

![../../_images/process_limits.png](http://docs.geoserver.org/latest/en/user/_images/process_limits.png)

If you're not satisfied with the above limits and would like to  develop new ones, no worries, the current code is setup on a pluggable  WPSInputValidator extesion point that will allow you to create new types  of input validators.


### WPS Dismiss


The final Finally, [GSIP 122](https://github.com/geoserver/geoserver/wiki/GSIP%20122%20Dismissing%20WPS%201.0%20process%20execution) added the ability to dismiss an ongoing process from the client that  requested the execution, or as an administrator. The new Dismiss  operation comes from the WPS 2.0 specification, which GeoServer does not  support yet, so it has to be seen as a vendor extension to WPS 1.0,  which leverages the executionId parameter returned in the asynch status  links to allow execution cancellation, you can read more about it in the  [user documentation](http://docs.geoserver.org/latest/en/user/extensions/wps/operations.html#dismiss).  The administrator instead gets a new user interface panel showing the  currently running operations, allowing selection and forceful dismissal  of processes that are running:

![../../_images/statuspage.png](http://geoserver.wpengine.com/wp-content/uploads/2015/02/statuspage.png)

[The user guide](http://docs.geoserver.org/latest/en/user/extensions/wps/administration.html#process-status-page) contains more details about its usage. We would like to thank [NATO STO CMRE](http://www.cmre.nato.int/) for sponsoring all the above WPS improvements.


### Refresh of the CSS module


The initial CSS extension (responsible for using CSS to generate SLD  styles) was written in Scala. Although wildly popular, and featured up  until GeoServer 2.6, the module has not been maintained to the level  expected of a GeoServer extension.

Andrea has taken it unto himself to address this gap, rewriting the  functionality in Java and making the result available to the GeoTools  library.

The new CSS engine performs the same function as the Scala original  and has managed to make a few key improvements. In particular the Java  implementation can efficiently handle large CSS files without bogging  down with minutes of translation time.

[![](http://geoserver.wpengine.com/wp-content/uploads/2015/02/css1.png)](http://blog.geoserver.org/2015/01/22/geoserver-2-7-beta-released/css-2/)

The user interface for the CSS editor has also been revamped a bit,  making better usage of available screen space, and sporting syntax  highlighting and formatting thanks to CodeMirror. This change addresses a  common gripes correctly supporting relative images (the generated SLD  preserves the relative path) and polygon with strokes are now translated  to a single polygon symbolizer (to the benefit of GetLegendGraphic  calls). Finally, you'll notice that the download size have been  significantly trimmed, as we don't need anymore the Scala runtime.

The new translator has been tested against a few hundreds CSS styles  already, but of course it's new, so it's of paramount importance that  you test your own styles, and let us know if you notice any regression.

We take the occasion to thank David Window for creating the initial  CSS module, and Andrea Aime for porting it to java and acting as the new  maintainer.


### Relative time support in WMS/WCS


As you probably knows GeoServer supports time based filtering in both  WMS (aka WMS-T) and WCS (as part of WCS-EO). Up until now you had to  specify the desired time either as an absolute value, e.g.  &time=2011-05-02, or as an absolute range of values,  e.g. &time=2011-05-02/2011-05-05.

The work done in [GSIP 124](https://github.com/geoserver/geoserver/wiki/GSIP-124) adds support for a vendor specific extension to the time syntax which  allows the specification of relative times, e.g., the last 36 hours,  "PT36H/PRESENT", or the day after December 25 2012,  "2010-12-25T00:00:00.0Z/P1D".

This allows for more compact requests, but more importantly, it  allows to generate stable, publishable links to instants or intervals  relative to the present server time, e.g., the weather forecast for  tomorrow, two days and three days in the future, or the temperature maps  for the last three days, maybe in a KML document generated with  animations over time.


### Miscellaneous


In addition a wide range of improvements have been made:



	
  * For those making printed maps, we added a new[ vendor parameter](http://docs.geoserver.org/latest/en/user/services/wms/vendor.html#scalemethod) forcing GeoServer to ignore the WMS simple scale computation algorithm,  and run a local and accurate one instead, resulting in better  integration between printing requirements and maps with scale  dependencies.

	
  * The flow-control module now also supports [rate based rules](http://docs.geoserver.org/latest/en/user/extensions/controlflow/index.html#per-user-rate-control), with the ability to slow down, or simply reject, requests that are incoming from a specific client at an excessive rate.

	
  * For those working at the dateline, you'll be pleased to know that  the WCS 2.0 GetCoverage requests can now handle bounding boxes crossing  the dateline, and they will take the two halves of your coverage from  the antipodes, merge them together in a single output file that will be  returned to you (much like the same support for WMS, introduced in  2.6.0).

	
  * For people using configuration in the database, the  JDBCConfig module and core modules have seen a number of changes to  increase scalability and push down into the database as much filtering  as possible in a larger number of commonly used code paths.

	
  * The DDS module, allowing extraction of DEM portions using the WMS  protocol in order to feed Nasa Worldwind, has seen a number of fixes and  now allows the specification of a texture compression format.

	
  * Finally, the map preview has been switched to OpenLayers 3, although  the nostalgic can get back the OL2 based one by adding the  "-DENABLE_OL3=false" parameter to the JVM startup options. Thanks to  Bart for helping add this to GeoServer.


This concludes the most visible changes, if you are missing some please check the [full changelog](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=20940) for details, there is quite a bit more stuff in there.


## Community modules


In addition to the core GeoServer and extensions we have an active  community area for experiments and new volunteers. This release comes  with a number of new community modules that you might find useful.


#### Clustering modules


The community section now holds two clustering modules allowing a  cluster of GeoServer instances to work against a shared vision of the  data directory.

The first one, contributed by GeoSolutions, works using J2EE JMS  messages to share the state against the various nodes, and allows the  usage of the normal file based configuration, either in a shared data  dir mode, or data dir per node mode. This is know as the "JMS  clustering", [see the documentation](http://docs.geoserver.org/latest/en/user/community/jms-cluster/index.html) for more details. The module is ready for testing as it's part of the [nightly builds](http://ares.boundlessgeo.com/geoserver/master/community-latest/).

The second one, contributed by Boundless, works by using Hazelcast  distributed messages, and it's designed to work best against the  JDBConfig module. At this time there are no released artifacts or  documentation, but the adventurous user will find it pretty easy to  figure out.


#### GeoFence


The GeoFence advanced security subsystem has been donated to the  GeoServer project by GeoSolutions earlier this year, this module is the  plugin connecting a GeoServer instance to the GeoFence rule engine.

GeoFence allows to setup complex security rules and leverage the full  power of the underlying GeoServer security subsystem, for example, it's  possible to establish security rules mixing in the same condition data  and service being used, limit attributes available to certain  users/operations, filter data so that certain records are not visible to  the public, force certain default style to given user roles, and so on.  The [GeoFence wiki](https://github.com/geoserver/geofence/wiki) contains documentation on how to use and configure the system.


#### SOLR data store


The SOLR data store allows GeoServer to connect to a SOLR server and  publish its spatial document via the OGC protocols, efficiently making  maps, serving them via the WFS service, and allowing spatial analysis  via WPS. The user interface allows to classify sets of documents as  layers, and map the document variable structure into the fixed structure  of simple feature types served by GeoServer.

![](http://www.geo-solutions.it/wp-content/uploads/2014/09/Selezione_180.png?57c3b5)

You can read an introduction in [this blog post](http://www.geo-solutions.it/blog/solr-power-shining-through-geoserver-ogc-services/), and delve into details in the user [documentation](http://docs.geoserver.org/latest/en/user/community/solr/index.html).


### New WPS output formats


The gs-gpx and gs-kml modules offer two new PPIO to translate feature  collection resulting off WPS processes in the respective formats. The  KML one, in particular, also supports limited input parsing, allowing to  send KML documents as inputs to the WPS services.


#### The WPS download process


The wps-download community module forms the basis of an "advanced  clip and ship" tool that allows a client to ask for data in a specific  area, eventually reprojecting it, estimate the download size, and allow  the preparazion of a zip package with the desired data, all via  asynchronous calls, providing a good replacement for WFS/WCS when the  amount of data to be extracted is too large to be delivered via  synchronous HTTP calls.





## About GeoServer 2.7


Articles and resources for GeoServer 2.7 series:



	
  * **[SOLR power shining through GeoServer OGC services](http://www.geo-solutions.it/blog/solr-power-shining-through-geoserver-ogc-services/)**






