---
author: jgarnett
comments: true
date: 2016-03-01 23:36:55+00:00
layout: post
link: http://blog.geoserver.org/2016/03/01/geoserver-2-9-beta-released/
slug: geoserver-2-9-beta-released
title: GeoServer 2.9-beta released
wordpress_id: 2626
categories:
- Announcements
tags:
- beta
- release
---

The GeoServer team is pleased to announce the release of [GeoServer 2.9-beta](http://geoserver.org/release/2.9-beta/). This is a beta release, focused on making our wicket update available for testing, and trying out our release process to ensure we have not broken anything.

Beta releases are intended for public feedback and are not recommended for production use.

Download [bundles](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9-beta/) are available ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9-beta/geoserver-2.9-beta-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9-beta/geoserver-2.9-beta-war.zip/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.9-beta/geoserver-2.9-beta.exe/download)). Our mac dmg is late to the party, we will update the blog post when it arrives.

Highlights:



	
  * This release requires Java 8.
We have identified one [known incompatibility](https://github.com/geoserver/geoserver/wiki/Spring-4-Upgrade) and may need to adjust our roadmap based on your testing and feedback.

	
  * Documentation has a [new layout](http://docs.geoserver.org/latest/en/user/) grouping service [description and configuration](http://docs.geoserver.org/latest/en/user/services/wms/index.html) reference together. Services that are an optional install (such as CSW and WPS) have been brought into a [consistent location](http://docs.geoserver.org/latest/en/user/services/index.html) so you can easily see what GeoServer is capable of rather than getting lost in extensions.

	
  * This release includes support for [perpendicular offset](http://docs.geoserver.org/latest/en/user/styling/sld-reference/linesymbolizer.html#perpendicularoffset) in SLD (see SLD cookbook for an [example](http://docs.geoserver.org/latest/en/user/styling/sld-cookbook/lines.html#offset-line)).

	
  * UTFGrid support in [WMS GetMap](http://docs.geoserver.org/latest/en/user/services/wms/outputformats.html)

	
  * Internally we have upgraded the user interface library - taking the opportunity to update [global](http://docs.geoserver.org/latest/en/user/configuration/globalsettings.html), [image processing](http://docs.geoserver.org/latest/en/user/configuration/image_processing/index.html) and [raster access](http://docs.geoserver.org/latest/en/user/configuration/raster_access.html) screens. The layer group page has also been split into tabs. By popular request the button to add a new layer has been renamed to "Add new layer".

	
  * Legend graphic has always been auto-generated, you can [use your own](http://docs.geoserver.org/latest/en/user/data/webadmin/styles.html#add-a-legend) custom icons.

	
  * For installations without direct file system access you can now [manage resources](http://docs.geoserver.org/latest/en/user/rest/api/resources.html) (icons, fonts,templates) using the REST API.

	
  * An useful improvement to the [aggregation process](http://docs.geoserver.org/latest/en/user/services/wps/processes/gs.html#aggregation-process) is the group aggregate queries (sum, average, count) by an attribute.

	
  * For more information, as always, check the beta [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=12100) (and milestone [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=11401&styleName=&projectId=10000))


This 2.9-beta release is released in conjunction with GeoTools 15-beta and GeoWebCache 1.9-beta. Thanks to Jody Garnett (Boundless) for this release.

A beta release often features lots of last-moment pull requests - thanks to Andrea Amie (GeoSolutions) and Ben Caradoc-Davies (Transient) for their assistance during this review cycle. A further thanks to Larry Shaffer (Boundless) and Chris Del Pino (Boundless) for their build assistance.

The big news for GeoServer 2.9-beta is upgrading our user interface from Wicket 1.4 to Wicket 7. A [sprint](https://wiki.osgeo.org/wiki/GeoServer_Code_Sprint_2016) was organized for this labour intensive task, with plenty of hard work and manual testing. We would like to thank our sponsors [OSGeo](http://www.osgeo.org/), [Boundless](http://boundlessgeo.com/), [Vivid Solutions](http://www.vividsolutions.com/), [How 2 Map](http://www.how2map.com/), [San Jose Water Company](https://www.sjwater.com/), [Transient](http://transient.nz/) and [Geobeyond](http://www.geobeyond.it/). We should also thank sprint participants and in-kind sponsors scitus development, GeoSolutions, CCRi, Astun Technology and Voyager for making this event possible.


## About Geoserver 2.9


Articles, docs, blog posts and presentations:



	
  * [GeoServer code sprint success](http://blog.geoserver.org/2016/01/25/geoserver-code-sprint-success/) and [wicket migration code sprint](https://github.com/geoserver/geoserver/wiki/Wicket-migration-code-sprint)

	
  * [GeoServer Plugin for QGIS](http://blog.geoserver.org/2015/12/23/geoserver-explorer-plugin-for-qgis/)

	
  * [REST configuration Resources](http://docs.geoserver.org/latest/en/user/rest/api/resources.html) (docs)



