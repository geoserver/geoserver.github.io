---
author: geoserver
comments: true
date: 2013-08-19 17:37:26+00:00
layout: post
link: http://blog.geoserver.org/2013/08/19/geoserver-2-4-rc1-released/
slug: geoserver-2-4-rc1-released
title: GeoServer 2.4-RC1 released
wordpress_id: 1533
---

GeoServer team is pleased to announce the release of [GeoServer 2.4-RC1](http://geoserver.org/display/GEOS/GeoServer+2.4-RC1). This release contains a set of bug fixes and minor improvements compared to 2.4-beta, including:



	
  * Some love to the layer group edit page, fixing style editing

	
  * Improvements in the CSS extension editor

	
  * A number of fixes in the CSW community module (scheduled to graduate to extension real soon now)

	
  * Making GML3 GetFeatureInfo output work against rasters too

	
  * A bunch of minor fixes to the new KML module


See the [GeoServer 2.4-RC1 release notes](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=19446) for more details.

The next release candidate is scheduled in two weeks. If we don't hear about major bugs reported against 2.4-RC1, we'll release it as 2.4.0:  user community, your turn, **please test RC1 now and let us know if anything major does not work as you expected**. If you discover any issue, report it in our [bug tracker](http://jira.codehaus.org) and if you still do not have a login, you can create one at [Codehaus](http://xircles.codehaus.org) (valid for all Codehaus services, including the GeoServer bug tracker they are graciously hosting for us).


### About the GeoServer 2.4 series


GeoServer 2.4 continues our 6-month release cycle.

Volunteer opportunities:



	
  * We strongly encourage all interested parties to take part in testing GeoServer 2.4-RC1


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



