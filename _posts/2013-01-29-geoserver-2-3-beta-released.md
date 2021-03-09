---
author: geoserver
comments: true
date: 2013-01-29 18:32:02+00:00
layout: post
link: http://blog.geoserver.org/2013/01/29/geoserver-2-3-beta-released/
slug: geoserver-2-3-beta-released
title: GeoServer 2.3-beta released
wordpress_id: 1306
---

We’re happy to announce the release of GeoServer 2.3-beta and encourage you to [download](http://geoserver.org/display/GEOS/GeoServer+2.3-beta) it, try out the great new features, and let us know if there are any bugs. Since this is a beta release, we recommend against deploying it in a production environment without first backing up and undertaking extensive testing.

Please report issues as soon as possible, as we expect the first release candidate as soon as next month. This beta release is the first new major release developed under the time-boxed development model and contains six months worth of improvements, including:


### Pluggable configuration storage subsystem


Thanks to [GSIP 69](http://geoserver.org/display/GEOS/GSIP+69+-+Catalog+scalability+enhancements), the catalog and configuration storage subsystem is now pluggable and better suited to large scale deployments and large quantities of layers. In particular, we've developed a new community module allowing configuration to be stored in a relational database and tests show good performance even with millions of layers stored in it. We invite everybody interested in these capabilities to [download](http://gridlock.opengeo.org/geoserver/master/community-latest/geoserver-2.3-SNAPSHOT-jdbcconfig-plugin.zip) and try out the jdbcconfig module with nightly builds and provide feedback for its development. Thanks to [OpenGeo](http://opengeo.org/) for pushing the envelope in this area.


### GeoWebCache


As a result of  [GSIP 90](http://geoserver.org/display/GEOS/GSIP+90+-+Upgrading+to+GWC+1.4.x), GeoWebCache has been upgraded to the 1.4.x series for significant improvements to our clustering story. In particular, the metastore has been removed, allowing all the meta-information about the tiles to be stored in the file system.
Also, the disk quota subsystem has been overhauled and the dependency for Berkeley DB Java edition has been dropped, allowing the usage of standard relational databases.  An embedded H2 database is used by default but an external database such as PostgreSQL or Oracle can be used as well to enable a cluster of GeoWebCache instances to all share the same disk quota information. Finally, on disk tile management has been improved to allow multiple instances of writing and reading in parallel without conflict. Thanks to the [Norwegian Public Road Authority](http://www.vegvesen.no/en/The+NPRA) for sponsoring the effort of [GeoSolutions](http://www.geo-solutions.it/).
[![](/img/uploads/gwc-nq8-201x300.png)](http://blog.geoserver.org/2013/01/29/geoserver-2-3-beta-released/gwc-nq8/)


### LayerGroup improvements


As part of [GSIP 84](http://geoserver.org/display/GEOS/GSIP+84+-+Control+how+layer+groups+are+exposed+in+the+WMS+capabilities+document) and [GSIP 85](http://geoserver.org/display/GEOS/GSIP+85+-+Nested+layer+groups), LayerGroup functionality has been significantly improved to allow not only grouping of layers but also to expose the inner structure of the group in the capabilites document and also nested layer groups to form a full-fledged tree. A layer can be nested in more than one tree to provide flexibility when presenting the information to WMS clients. It's also now possible to specify a custom title and abstract for a LayerGroup to better describe it in the capabilities document.
Find out more in the [GeoServer documentation](http://docs.geoserver.org/latest/en/user/webadmin/data/layergroups.html). Thanks to [GeoSolutions](http://www.geo-solutions.it/) for performing the work and [DLR](http://www.dlr.de) and [EUMETSAT](http://www.eumetsat.int/Home/index.htm) for sponsoring it.

[![](/img/uploads/layergroups-nq8-300x1211.png)](http://blog.geoserver.org/2013/01/29/geoserver-2-3-beta-released/layergroups-nq8/)


### Security subsystem improvement


The security subsystem has been improved thanks to [GSIP 82](http://geoserver.org/display/GEOS/GSIP+82+-+Reworking+security+filter+chains) and [GSIP 91](http://geoserver.org/display/GEOS/GSIP+91+-+Enhance+authentication+filter+chain+configuration). Both improvements target the security authentication chains, making them more flexible and easier to configure as well as improving the user interface. Administrators can now create custom authentication chains and associated them to the different URLs GeoServer exposes. Authentication chains can enforce SSL connections and send back roles for authenticated principals in an HTTP response header attribute. It is also possible to disable security for a chain. The filter chain matching is extended to optionally check the HTTP method(s) of an incoming request—for example, giving anonymous access for GET and POST but requiring basic authentication for PUT and DELETE.

Both the Central Authentication Service (CAS) subsystem and the [authkey](http://docs.geoserver.org/latest/en/user/community/authkey/index.html) community module have also been made functional again.

Many thanks to Christian Mueller for the continued work on the security subsystem.


### WPS process selection


The WPS configuration panel now allows the administrator to select which processes to expose to clients, making it possible to expose just a selected few and thereby improving the performance and stability of the server. Thanks to [GeoSolutions](http://www.geo-solutions.it/) for developing this new functionality.

[![](/img/uploads/wps-nq8-300x811.png)](http://blog.geoserver.org/2013/01/29/geoserver-2-3-beta-released/wps-nq8/)


### WMS dimension support improvements


While 2.2.x series added support for time and elevation in WMS, the 2.3.x series brings significant improvements in this area. In particular:



	
  * Dimensions can now be associated with a unit symbol and a unit dimension. Thanks for [Michael Romero](https://github.com/geoserver/geoserver/pull/7) for providing this improvement.

	
  * User-defined dimensions are now supported for raster data, allowing dimensions other than time and elevation to be advertised and managed via WMS. Thanks to [Mike Benowitz](https://github.com/geoserver/geoserver/pull/16) for providing this improvement.

	
  * Image mosaic can now gather and manage custom dimensions. Thanks to [GeoSolutions](http://www.geo-solutions.it/) for developing this under [DLR](http://www.dlr.de) and [EUMETSAT](http://www.eumetsat.int/Home/index.htm) sponsorship.




### Monitoring extension


The [monitoring](http://docs.geoserver.org/latest/en/user/extensions/monitoring/index.html) module graduated from community module to extension, and gained new functionality in the process:



	
  * The system can now gather more information about requests, such as HTTP referrer and better support for requested BBOX

	
  * The storage subsystem has been made pluggable, with the Hibernate classic one being the default implementation


Thanks to [OpenGeo](http://opengeo.org/) for pushing the envelope on this one.


### JSON all over


JSON and JSONP support has been added in several places to support JavaScript development:



	
  * WMS GetFeatureInfo output format

	
  * WMS Describelayer

	
  * WFS DescribeFeatureType (as JSON schema)

	
  * WMS exceptions can now be requested in JSON format as well


Thanks to [GeoSolutions](http://www.geo-solutions.it/) for developing these improvements with [FAO](http://www.fao.org/) sponsorship.


### Gather information about what's installed in your GeoServer


The work performed under [GSIP 83](http://geoserver.org/pages/viewpage.action?pageId=55574531) is going to make  it easier to manage several GeoServer installations. This work added a REST API allowing administrators to gather information about all the libraries included in a certain GeoServer installation and answer questions such as:



	
  * What precise version of GeoServer and GeoTools are used in a certain installation?

	
  * What extensions and community modules are included?

	
  * What java libraries are available in the installation, and what version?


Thanks to [GeoSolutions](http://www.geo-solutions.it/) for developing these improvements with [FAO](http://www.fao.org/) sponsorship.


### INSPIRE module improvements


The INSPIRE community module has been enhanced and now provides INSPIRE specific metadata in the WFS 1.1 and 2.0 capabilities modules, bringing GeoServer closer to full WFS compliance under the INSPIRE requirements. Thanks for [camptocamp](http://www.camptocamp.com/) for the development, and to [IGN France](http://www.ign.fr/).


### Raster data management improvements


Raster data management has been significantly improved in GeoServer 2.3-beta. In particular we worked on raster data reprojection, eliminating artifacts occurring at raster borders during reprojection with better NODATA management, and significantly improving reprojection performance by streamlining the set of operations done while reprojecting a raster. We ran the WMS 2010 shootout raster reprojection tests with 2.2.x and 2.3.x and here is the speedup you can expect (the graph compares requests per second vs number of concurrent requests, click to enlarge):

[![](/img/uploads/performance-300x185.png)](http://blog.geoserver.org/2013/01/29/geoserver-2-3-beta-released/performance/)

Thanks to [GeoSolutions](http://www.geo-solutions.it/) and [OpenGeo](http://opengeo.org/) for pushing the envelope in this area.


### Testing subsystem overhaul


Some good news for developers... If you are developing extensions, improvements, or bug fixes against GeoServer 2.2.x the slowness of the test subsystem was probably something you noticed. [Months ago a team of GeoServer developers met in Vienna to improve this](http://blog.geoserver.org/2012/09/30/vienna-code-sprint/), creating a new set of base classes for testing and upgrading the whole system to JUnit 4 in the process. The new test subsystem is significantly faster, making development on the 2.3.x series much nicer.


### OSGeo incubation progress


GeoServer OSGeo incubation is well underway and approaching completion. Special thanks to the team of developers that met in Australia to perform the code and data provenance review, we all know it's tedious but necessary step in the incubation process. Each finding was documented as a JIRA issue, resulting in a large number of them in the 2.3.x changelog.


### Everything else


The [GeoServer 2.3-beta detailed release notes](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=18651) contain a lot more details, as well as other changes that we haven't included in the announcement for brevity's sake. It's also worth having a look into the corresponding [GeoTools 9.0-M1](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10270&version=18643) and [9.0-beta](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10270&version=18966) changelogs, as GeoServer inherits significant improvements made in GeoTools.


### More interesting stuff cooking in community land


While still not ready for prime time, the current development series contains a couple of very interesting new community modules:



	
  * A **CSW service** with pluggable backends and record frontends. The current backends can serve Dublin Core records out of the file system, and ISO records reflecting the current set of layers in the GeoServer configuration, making GeoServer self hosted in terms of layer searchability. Thanks to Niels Charlier, [GeoSolutions](http://www.geo-solutions.it/), and [OpenGeo](http://opengeo.org/) for pushing the envelope in this area.

	
  * A **WCS 2.0 service** with full EO extension is in the works. The module is being developed by [GeoSolutions](http://www.geo-solutions.it/), with sponsorship from [DLR](http://www.dlr.de) and [EUMETSAT](http://www.eumetsat.int/Home/index.htm).

	
  * Several **[scripting modules](http://docs.geoserver.org/latest/en/user/community/scripting/index.html)** supporting languages such as Python, Groovy, Beanshell, Ruby, and Javascript allow one to script WPS processes as well as little applications. Thanks to [OpenGeo](http://opengeo.org/) for this awesome improvement.

	
  * A **[W3DS service](http://osgeo-org.1560.n6.nabble.com/W3DS-Service-as-a-Community-Module-td5026763.html)** has been added recently, allowing GeoServer to serve 3D data and scenes via OGC protocols. Many thanks to Nuno Oliveira for this exciting new development.




### Conclusions


Everyone who uses GeoServer should have at least one or two items in the above list to get excited about. [Download GeoServer 2.3-beta](http://geoserver.org/display/GEOS/GeoServer+2.2-beta1), try it out, and please provide feedback and report any issues on the [GeoServer mailing list](http://geoserver.org/display/GEOS/Mailing+Lists).  As with any beta version, _be sure to backup your data directory before upgrading_.
