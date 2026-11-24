---
author: bmmpxf
comments: true
date: 2008-08-11 16:27:07+00:00
layout: post
link: http://blog.geoserver.org/2008/08/11/a-new-ui-is-dawning/
slug: a-new-ui-is-dawning
title: A New UI is Dawning
wordpress_id: 117
categories:
- Announcements
---

The GeoServer team has been working on something very exciting over the past few months, that we'd like to share with you now.   We have the beginnings of a brand new user interface on the admin console for GeoServer.<!-- more -->




The admin console isn't the face of GeoServer; the maps one serves with it are.   (And even then, it's really the application, such as [OpenLayers](http://openlayers.org), or whatever front end is used, that is the real face.)  That said, anyone who has spent any time working with GeoServer needs to get very intimate with the admin console.   The current UI is based on [Apache Struts](http://struts.apache.org/), which was historically the de facto Java web framework standard.  However, it does have its limitations, mainly, its difficulty in maintenance and extensibility, and its programmer-centric workflow.  Personally, I always felt that the UI was never built with the end user in mind, and I think most would agree.  This was fine back in the day when the project was in its infancy, but now that GeoServer has become an enterprise-level product, able to compete in the marketplace with any geospatial server, the community has come to think that now was an appropriate time to rethink the UI with the future, and the users, in mind.




The new UI is based on [Apache Wicket](http://wicket.apache.org/).  Those who are curious about the more technical aspects of Wicket vs. Struts, they are welcome to read the Wicket [GeoServer Improvement Proposal](https://web.archive.org/web/20080811/http://geoserver.org/display/GEOS/GSIP+23+-+Wicket+UI) (and Wicket also has a nice page on the rationale behind [yet another framework](http://wicket.apache.org/introduction.html).) Personally, I think one look at the new environment will convince you that the product has turned a corner.




And so I welcome all users and developers to the first alpha release of GeoServer 2.0.  This release is very experimental, and is intended primarily to show off the new user interface.  The entire team is looking for any feedback on the look and feel of the new interface. Please sign up for the [users](http://lists.sourceforge.net/lists/listinfo/geoserver-users) or [developers](https://lists.sourceforge.net/lists/listinfo/geoserver-devel) mailing list if you haven't already, as posting there is the best way to ensure your feedback is noted and recorded by all.




One note on the distribution of 2.0.0-alpha1.  Due to the very experimental nature of the release, it is currently being offered in .WAR (web archive) format only.  This means that you will need a container server such as [Tomcat](http://tomcat.apache.org/) or [JBoss](http://www.jboss.org/) to be able to run the software.  Future releases will contain all of the standard formats.




For more information and technical details about the new UI, please see the following links:






	
  * [Wicket UI in GeoServer](https://web.archive.org/web/20080811/http://geoserver.org/display/GEOS/GSIP+23+-+Wicket+UI)

	
  * [Adding a Configuration Page with the Wicket UI](https://web.archive.org/web/20080811/http://geoserver.org/display/GEOSDOC/Adding+a+Configuration+Page-GS2)




Download GeoServer 2.0.0-alpha1

----

#### GeoServer 2.0.0-alpha1 is available from the [SourceForge Download Page](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.0-alpha1/).

Released on August 11, 2008. SourceForge Release 619085

- [Release Notes](#release-notes)

- [geoserver-2.0.0-alpha1-war.zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.0.0-alpha1/geoserver-2.0.0-alpha1-war.zip/download) (Web archive)

Due to the very experimental nature of this release, only the .WAR is currently being distributed.

## Release notes

Improvement:

* [GEOS-2077](https://osgeo-org.atlassian.net/browse/GEOS-2077) Create a spring reloading handler for wicket
* [GEOS-2080](https://osgeo-org.atlassian.net/browse/GEOS-2080) Set default value for datastore namespace from the "folder" the datastore is being set up into
* [GEOS-2087](https://osgeo-org.atlassian.net/browse/GEOS-2087) Icons for categories and menu links
* [GEOS-2099](https://osgeo-org.atlassian.net/browse/GEOS-2099) Add remember me cookies handling in new UI
* [GEOS-2108](https://osgeo-org.atlassian.net/browse/GEOS-2108) Use the standard markup for datastore editor
* [GEOS-2111](https://osgeo-org.atlassian.net/browse/GEOS-2111) When configuring a new FeatureType, fill out default metadata from the one provided by FeatureSource.getInfo()

Bug:

* [GEOS-2010](https://osgeo-org.atlassian.net/browse/GEOS-2010) DataTree error message on back button with FF3
* [GEOS-2079](https://osgeo-org.atlassian.net/browse/GEOS-2079) Error thrown if enabling a datastore configuration but can't connect to the backend
* [GEOS-2104](https://osgeo-org.atlassian.net/browse/GEOS-2104) ResourcePool.getDataStore and ModificationProxy.invoke mask source exceptions
* [GEOS-2112](https://osgeo-org.atlassian.net/browse/GEOS-2112) MapPreview page shows disabled resources, which then fail to show up

Task:

* [GEOS-2081](https://osgeo-org.atlassian.net/browse/GEOS-2081) Add demo requests page
* [GEOS-2083](https://osgeo-org.atlassian.net/browse/GEOS-2083) Make the menu organization pluggable.
* [GEOS-2086](https://osgeo-org.atlassian.net/browse/GEOS-2086) Hook up save button for Wicket UI
