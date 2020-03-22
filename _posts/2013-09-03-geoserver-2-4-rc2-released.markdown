---
author: geoserver
comments: true
date: 2013-09-03 21:05:19+00:00
layout: post
link: http://blog.geoserver.org/2013/09/03/geoserver-2-4-rc2-released/
slug: geoserver-2-4-rc2-released
title: GeoServer 2.4-RC2 released
wordpress_id: 1593
categories:
- Announcements
---

GeoServer team is pleased to announce the release of [GeoServer 2.4-RC2](http://geoserver.org/display/GEOS/GeoServer+2.4-RC2) with a few last minute additions:



	
  * Catalog Service Web has graduated to a formal Extension, including new admin page and many fixes

	
  * A fix for those using Tomcat Apache Portable Runtime

	
  * Removal of the VPF Extension

	
  * See the [GeoServer 2.4-RC2 release notes](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=19547) for more details


This is our last shot before [FOSS4G](http://2013.foss4g.org) so we really need to call out to our great community and ask for your assistance with testing. There are two aspects where your your help is vital:



	
  * Our developers are not in position to test on every platform, so if we need to ask for assistance **testing in strange environments** (like [Windows](http://windows.microsoft.com) or [WildFly](http://www.wildfly.org))

	
  * In a similar fashion the developers tend to play with a few specific sample datasets which have been donated to the project for this purpose. If you can **test with your own data** and confirm everything works as expected it will save us both any surprises


To quickly report back success, drop a message on twitter with the [#GeoServer](https://twitter.com/search?q=%23GeoServer) tag!

If you discover any issue, please let us know using the [bug tracker](http://jira.codehaus.org) (Use [xircles](http://xircles.codehaus.org) to set up a CodeHaus login).


### About the GeoServer 2.4 series


The following change control requests were completed during the development of GeoServer 2.4:



	
  * [Replace old KML module with new one ](http://geoserver.org/display/GEOS/GSIP+98+-+replace+old+KML+module+with+new+one)(GSIP 98)

	
  * [Allow plugins to modify WMS MapContent before map rendering](http://geoserver.org/display/GEOS/GSIP+92+-+Allow+plugins+to+modify+WMS+MapContent+before+map+rendering) (GSIP 92)

	
  * [Machinery to pass thread locals down in thread pools](http://geoserver.org/display/GEOS/GSIP+96+-+Machinery+to+pass+thread+locals+down+in+thread+pools) (GSIP 96, fixes WPS asych requests security issues) - also available in 2.3.4

	
  * [Promote CSS Styling module from Community to Extension](http://geoserver.org/display/GEOS/GSIP+97+-+Promote+CSS+Styling+module+from+Community+to+Extension) (GSIP 97) - also available in 2.3.2

	
  * [Graduate the INSPIRE module to extension status](http://geoserver.org/display/GEOS/GSIP+94+-+Graduate+the+INSPIRE+module+to+extension+status) (GSIP 94) - also available in 2.3.2

	
  * [Promote XSLT community module to extension](http://geoserver.org/display/GEOS/GSIP+93+promote+XSLT+community+module+to+extension) (GSIP 93) - also available in 2.3.1

	
  * The shapefile datastore was completely rewritten (mostly as a code cleanup)


Articles and blogs during GeoServer 2.4 development:

	
  * GeoServer in a clustered configuration ([Part 1](http://blog.opengeo.org/2013/04/18/geoserver-in-a-clustered-configuration-part-1/), [Part 2](http://blog.opengeo.org/2013/04/30/geoserver-in-a-clustered-configuration-part-2/))

	
  * [New GeoServer community on Google+](http://blog.geoserver.org/2013/05/13/new-geoserver-community-on-google/)

	
  * [How to publish GDAL/MrSID image formats on a production GeoServer](http://blog.opengeo.org/2013/03/13/how-to-publish-gdalmrsid-image-formats-on-a-production-geoserver-on-windows/)

	
  * GeoServer crunch time ([Part I](http://www.lisasoft.com/blog/geoserver-crunch-time), [Part II](http://www.lisasoft.com/blog/geoserver-crunch-time-ii) and [Part III](http://www.lisasoft.com/blog/geoserver-crunch-time-iii))

	
  * FOSS4G-NA slides ([GeoServer In Production](http://blog.opengeo.org/wp-content/uploads/2013/05/GeoServerProduction.pdf), [GeoServer CSS Module](http://blog.opengeo.org/wp-content/uploads/2013/05/foss4gna2013-geoserver-css.pdf), [Scripting GeoServer with GeoScript](http://blog.opengeo.org/wp-content/uploads/2013/05/Scripting-GeoServer-with-GeoScript.pdf), [The State of GeoServer 2013](http://blog.opengeo.org/wp-content/uploads/2013/05/State-of-GeoServer-2013.pdf))

	
  * INSPIRE Conference 2013 slides ([Analysing GeoServer compatibility with INSPIRE requirements](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime?from_search=2))

	
  * FOSSGIS 2013 slides ([Introduction to GeoServer](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime))


