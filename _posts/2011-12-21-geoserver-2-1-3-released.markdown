---
author: geoserver
comments: true
date: 2011-12-21 22:28:44+00:00
layout: post
link: http://blog.geoserver.org/2011/12/21/geoserver-2-1-3-released/
slug: geoserver-2-1-3-released
title: GeoServer 2.1.3 Released
wordpress_id: 1017
categories:
- Announcements
- Features
---

The GeoServer team is happy to announce the release of GeoServer 2.1.3, now available for [download](http://geoserver.org/display/GEOS/GeoServer+2.1.3).

For the most part this is a maintainance release consisting of bug fixes, but as usual a few new features and improvements have managed to creep in. A total of [59 issues](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=17865) were resolved for this release. Some of the new and noteworthy include:



	
  * basic http authentication with cascaded WMS servers

	
  * WMS 1.3 support in the layer preview

	
  * transparent sorting for all data stores, not only those backed by a database

	
  * embedded OpenLayers upgraded to 2.11

	
  * a number of INSPIRE compliance improvements

	
  * support for asynchronous WPS processes


And more. Check out the [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=17865) for the entire list. A big thank you to everyone who contributed patches for this release. This includes:



	
  * Tony Young for a monitoring patch to include support for the "user-agent" header ([GEOS-4872](http://jira.codehaus.org/browse/GEOS-4872))

	
  * Tony Young again for a restconfig patch to properly calculate grid dimensions for coverages ([GEOS-4753](http://jira.codehaus.org/browse/GEOS-4753))

	
  * Rudi Hochmeister for a documentation patch providing an installation guide for Debian Linux  ([GEOS-4752](http://jira.codehaus.org/browse/GEOS-4752))

	
  * Frank Gasdorf for a completed German translation ([GEOS-4294](http://jira.codehaus.org/browse/GEOS-4294))


Contributions such as these are what keeps GeoServer moving forward. And thanks to all those who helped out by filing bug reports.

[Download 2.1.3](http://geoserver.org/display/GEOS/GeoServer+2.1.3), try it out and help us to continue to improve GeoServer by providing feedback on the [mailing list](https://lists.sourceforge.net/lists/listinfo/geoserver-users) and reporting bugs in the [issue tracker](https://jira.codehaus.org/browse/GEOS).

Thanks for using GeoServer!
