---
author: geoserver
comments: true
date: 2011-04-26 07:05:36+00:00
layout: post
link: http://blog.geoserver.org/2011/04/26/geoserver-2-1-rc5-released/
slug: geoserver-2-1-rc5-released
title: GeoServer 2.1-RC5 released
wordpress_id: 931
categories:
- Announcements
---



The GeoServer team is happy to announce the fifth release candidate for 2.1, now available for [download](http://geoserver.org/display/GEOS/GeoServer+2.1-RC5).

This release brings some bug fixes and addresses a few residual regressions compared to the old 2.0.x series. In no particular order:



	
  * While GeoServer 2.1 uses extended CQL (ECQL) for all the CQL related activities, it now also preserve backwards compatibility with the old CQL language (in particular, new keywords in ECQL might have conflicted with valid CQL statements).

	
  * The compatibility towards Google Earth 6 was improved too, making Google Earth 6 properly display KMZ files with embedded images.

	
  * The [querylayer](http://docs.geoserver.org/2.1.x/en/user/extensions/querylayer/index.html) module, allowing for cross layer filtering, was promoted from community to extension module and is thus available as an official extension in the release.

	
  * Finally, GeoServer 2.1-RC5 avoids HTTP session creation on all OGC service paths, even when using basic authentication, providing better overall scalability.


Check out the [change log](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=17324) for the full list.

Thanks to everyone who tested RC4 and helped us flush out these last few issues. You can continue to help us get to the official 2.1 release by downloading and trying out RC5. Be sure to report any issues in the [bug tracker](http://jira.codehaus.org/browse/GEOS) or on the [mailing list](mailto:geoserver-users@lists.sourceforge.net). Unless new regressions or serious bugs are found RC5 will be re-released as 2.1.0 final.

Thanks for using GeoServer!





