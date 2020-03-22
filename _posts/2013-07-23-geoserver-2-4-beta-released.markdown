---
author: geoserver
comments: true
date: 2013-07-23 01:23:59+00:00
layout: post
link: http://blog.geoserver.org/2013/07/22/geoserver-2-4-beta-released/
slug: geoserver-2-4-beta-released
title: GeoServer 2.4-beta Released
wordpress_id: 1471
categories:
- Announcements
---

GeoServer team is pleased to announce the release of [GeoServer 2.4-beta](http://geoserver.org/display/GEOS/GeoServer+2.4-beta).



	
  * The headline feature is a new implementation of the KML module.  This implementation introduces a new WFS KML output format leveraging the extended data with schema KML construct. Faster KML generation (similar speeds to GML2 output) and schema compliant KML output.
It is great to have a clean implementation to start any future enhancements against, however we do encourage all organisations that depend on GeoServer for KML output to take part in testing this beta.
Thanks to the NSW Geological Survey for sponsoring this work.

	
  * A lot of under-the-hood changes have been taking place for raster support. Many of the improvements will be realised in the community modules for the NetCDF and Image Mosaic formats. One visible change of all this hard work is the configuration of band information.

	
  * Application Schema users should note that joining behaviour is now on by default.

	
  * New community module for libjpeg-turbo

	
  * New community module for WMS Earth Observation profile, this required some API changes to GeoServer core (see GSIP 92 below).

	
  * The much loved CSS module has been promoted to an extension. This is significant as it represents our first non-Java module obtaining extension status.
The CSS module is written in Scala in part to take advantage of the excellent functional programming facilities for for calculating derived styles.

	
  * WPS processes can now operate against secured data (see GSIP 96 below)

	
  * This release is made in conjunction with [GeoTools 10-beta](http://geotoolsnews.blogspot.com.au/2013/07/geotools-10-beta-released.html)

	
  * This release is made in conjunction with GeoWebCache 1.5.0 - thanks to Kevin for publishing on such short notice.


See the [GeoServer 2.4-beta release notes](http://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=19083) for more details.


### About GeoServer 2.4


GeoServer 2.4 continues our 6-month release cycle (with this beta release marking feature-complete for FOSS4G).

Volunteer opportunities:



	
  * We strongly encourage all interested parties to take part in testing GeoServer 2.4-beta

	
  * We would like to thank Frank Gasdorf and related volunteers for the excellent work translating GeoServer into additional languages
(English, Dutch, German and Korean are at 100%). If you would like to take part, or just check how far translation is going, please visit [GeoServer Localization](https://www.transifex.com/projects/p/geoserver_stable/))


The following change control requests were completed during the development of GeoServer 2.4:

	
  * [Replace old KML module with new one ](http://geoserver.org/display/GEOS/GSIP+98+-+replace+old+KML+module+with+new+one)(GSIP 98)

	
  * [Allow plugins to modify WMS MapContent before map rendering](http://geoserver.org/display/GEOS/GSIP+92+-+Allow+plugins+to+modify+WMS+MapContent+before+map+rendering) (GSIP 92)

	
  * [Machinery to pass thread locals down in thread pools](http://geoserver.org/display/GEOS/GSIP+96+-+Machinery+to+pass+thread+locals+down+in+thread+pools) (GSIP 96) - also available in 2.3.4

	
  * [Promote CSS Styling module from Community to Extension](http://geoserver.org/display/GEOS/GSIP+97+-+Promote+CSS+Styling+module+from+Community+to+Extension) (GSIP 97) - also available in 2.3.2

	
  * [Graduate the INSPIRE module to extension status](http://geoserver.org/display/GEOS/GSIP+94+-+Graduate+the+INSPIRE+module+to+extension+status) (GSIP 94) - also available in 2.3.2

	
  * [Promote XSLT community module to extension](http://geoserver.org/display/GEOS/GSIP+93+promote+XSLT+community+module+to+extension) (GSIP 93) - also available in 2.3.1


Articles and blogs during GeoServer 2.4 development:

	
  * GeoServer in a clustered configuration ([Part 1](http://blog.opengeo.org/2013/04/18/geoserver-in-a-clustered-configuration-part-1/), [Part 2](http://blog.opengeo.org/2013/04/30/geoserver-in-a-clustered-configuration-part-2/))

	
  * [New GeoServer community on Google+](http://blog.geoserver.org/2013/05/13/new-geoserver-community-on-google/)

	
  * [How to publish GDAL/MrSID image formats on a production GeoServer](http://blog.opengeo.org/2013/03/13/how-to-publish-gdalmrsid-image-formats-on-a-production-geoserver-on-windows/)

	
  * GeoServer crunch time ([Part I](http://www.lisasoft.com/blog/geoserver-crunch-time), [Part II](http://www.lisasoft.com/blog/geoserver-crunch-time-ii) and [Part III](http://www.lisasoft.com/blog/geoserver-crunch-time-iii))

	
  * FOSS4G-NA slides ([GeoServer In Production](http://blog.opengeo.org/wp-content/uploads/2013/05/GeoServerProduction.pdf), [GeoServer CSS Module](http://blog.opengeo.org/wp-content/uploads/2013/05/foss4gna2013-geoserver-css.pdf), [Scripting GeoServer with GeoScript](http://blog.opengeo.org/wp-content/uploads/2013/05/Scripting-GeoServer-with-GeoScript.pdf), [The State of GeoServer 2013](http://blog.opengeo.org/wp-content/uploads/2013/05/State-of-GeoServer-2013.pdf))

	
  * INSPIRE Conference 2013 slides ([Analysing GeoServer compatibility with INSPIRE requirements](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime?from_search=2))

	
  * FOSSGIS 2013 slides ([Introduction to GeoServer](http://www.slideshare.net/geosolutions/fossgis2013-2013geoserveraime))


