---
author: geoserver
comments: true
date: 2013-04-23 17:15:09+00:00
layout: post
link: http://blog.geoserver.org/2013/04/23/geoserver-2-3-1-released/
slug: geoserver-2-3-1-released
title: GeoServer 2.3.1 released
wordpress_id: 1387
---

The GeoServer team is happy to announce the release of GeoServer 2.3.1, now available for [download](http://geoserver.org/display/GEOS/GeoServer+2.3.1).

This is the first bug-fix release of the 2.3.x stable series, and packs 34 changes between bug fixes and improvements in different departments. Here is an highlight:



	
  * The [XSLT output format generator](http://docs.geoserver.org/stable/en/user/extensions/xslt/index.html) module graduated from community to official extension (work performed GeoSolutions Andrea Aime with sponsorship from the City of Wien)

	
  * A couple of changes in the SQL Server data increase performance, provided you enable the relevant flags. One is the ability to transfer geometries in SQL Server native format, as opposed to using WKB, which avoids the slow WKB generation routines included in SQL Server, the other allows to disable native paging, which can sometimes lead the SQL Server query planner to create bad data access plans ([GEOS-5750](http://jira.codehaus.org/browse/GEOS-5750) and [GEOS-5314](http://jira.codehaus.org/browse/GEOS-5314)). The native geometry serialization was sponsored by Norwegian Directorate for Nature Management and performed by Bouvet, thanks to Stewart Loving-Gibbard for the paging patch.

	
  * A new flag has been added to prevent the resolution of XML external entities (normally enabled by default in XML parsers), which can be used to prevent some kinds of XML attacks ([GEOS-5273](http://jira.codehaus.org/browse/GEOS-5273) and [GEOS-5314](http://jira.codehaus.org/browse/GEOS-5314)). The work was performed by GeoSolution under sponsorship from the City of Wien.

	
  * Some SLD related fixes ([GEOS-4214](http://jira.codehaus.org/browse/GEOS-4214), [GEOS-5767](http://jira.codehaus.org/browse/GEOS-5767)) (thanks to GeoSolutions's Andrea and Carlo for those)

	
  * A bunch of improvements in the monitoring extension ([GEOS-5725](http://jira.codehaus.org/browse/GEOS-5725), [GEOS-5732](http://jira.codehaus.org/browse/GEOS-5732), [GEOS-5758](http://jira.codehaus.org/browse/GEOS-5758) and [GEOS-5766](http://jira.codehaus.org/browse/GEOS-5766)) (thanks to OpenGeo's Justin Deoliveria and Ian Schneider for those, plus one from Andrea)

	
  * Fixed an issue that prevented GeoServer from serving back GetMap requests under Windows when using the JRE ([GEOS-5768](http://jira.codehaus.org/browse/GEOS-5768)) (thanks goes to GeoSolutions' Simone for this one)

	
  * GWC will now respect the layer HTTP caching settings, and a memory leak has been fixed in respect to the WFS-T integration ([GEOS-5686](http://jira.codehaus.org/browse/GEOS-5686), [GEOS-5659](http://jira.codehaus.org/browse/GEOS-5659))  (thanks' to OpenGeo's Ian Schneider for these)

	
  * The German translation maintainers fixed an encoding problem which resulted in weird chars appearing in the GeoServer UI ([GEOS-5641](http://jira.codehaus.org/browse/GEOS-5641)) (thanks goes to Frank Gasdorf and Oskar Fonts for their continuous work on UI internationalization)

	
  * GeoServer UI is completely available in _**Dutch, German **_and _**Korean **_(thanks goes to Wouter van Nifterick, Frank Gasdorf, Stefan Engelhardt, Minpa Lee and others), feel free to review and contribute at [Transifex.com](https://www.transifex.com/projects/p/geoserver_stable)

	
  * Finally, a few fixes and improvements in the security subsystem ([GEOS-5698](http://jira.codehaus.org/browse/GEOS-5698), [GEOS-5751](http://jira.codehaus.org/browse/GEOS-5751), [GEOS-5753](http://jira.codehaus.org/browse/GEOS-5753), [GEOS-5783](http://jira.codehaus.org/browse/GEOS-5783)) (thanks to Christian Mueller for his continuous work on the security subsystem)


And there is more, you can find everything in the GeoServer [release notes.](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=19153) Also, looking at the corresponding [GeoTools 9.1 release notes](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10270&version=19152) we can find some extra goodies:



	
  * Improved support for sparse shapefiles ([GEOT-2791](http://jira.codehaus.org/browse/GEOT-2791)) (thanks to Dieter DePaepe)

	
  * Added support for UUID data type in PostGis data stores ([GEOT-4414](http://jira.codehaus.org/browse/GEOT-4414)) (thanks to Shane StClair)


[Download GeoServer 2.3.1](http://geoserver.org/display/GEOS/GeoServer+2.3.1), try it out, and provide feedback on the [GeoServer mailing list](http://geoserver.org/display/GEOS/Mailing+Lists).

Thanks again for using GeoServer!


