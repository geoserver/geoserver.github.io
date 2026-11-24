---
author: geoserver
comments: true
date: 2013-02-26 15:27:22+00:00
layout: post
link: http://blog.geoserver.org/2013/02/26/geoserver-2-3-rc1-released/
slug: geoserver-2-3-rc1-released
title: GeoServer 2.3-RC1 Released
wordpress_id: 1341
categories:
- Announcements
- Features
---

The GeoServer team is happy to announce the release of GeoServer 2.3-RC1, available for download. This release contains a number of bug fixes and small improvements since [2.3-beta]({% post_url 2013-01-29-geoserver-2-3-beta-released %}). Here is a quick summary:



	
  * faster computation of layer bounding box for Oracle data sources when the table is not in the user's schema ([[GEOS-5535](https://osgeo-org.atlassian.net/browse/GEOS-5535)])

	
  * a few improvements to SLD 1.1 compatibility, fixing a few bits that are available in SLD 1.0 but not quite working when read from SLD 1.1 ([[GEOS-4718](https://osgeo-org.atlassian.net/browse/GEOS-4718)], [[GEOS-5544](https://osgeo-org.atlassian.net/browse/GEOS-5544)])

	
  * fix for HTML templates not being used when the SLD has a large number or rules ([[GEOS-5534](https://osgeo-org.atlassian.net/browse/GEOS-5534)])

	
  * improvements in the integration of the new GeoWebCache disk quota subsystem ([[GEOS-5633](https://osgeo-org.atlassian.net/browse/GEOS-5633)], [[GEOS-5597](https://osgeo-org.atlassian.net/browse/GEOS-5597)], [[GEOS-5634](https://osgeo-org.atlassian.net/browse/GEOS-5634)])

	
  * handling the same parameter used multiple times in the same request ([[GEOS-5645](https://osgeo-org.atlassian.net/browse/GEOS-5645)])

	
  * ability to recover the master password in case it's lost ([[GEOS-5606](https://osgeo-org.atlassian.net/browse/GEOS-5606)])

	
  * fixed a number of extensions that were not properly working in 2.3-beta, app-schema and excel, ([[GEOS-5496](https://osgeo-org.atlassian.net/browse/GEOS-5496)], [[GEOS-5629](https://osgeo-org.atlassian.net/browse/GEOS-5629)])

	
  * GetLegendGraphics won't cut out large point symbols anymore, it will rescale them instead ([[GEOS-5592](https://osgeo-org.atlassian.net/browse/GEOS-5592)), and made GetLegendGraphics work against layers whose geometry type is unkonwn ([[GEOS-5587](https://osgeo-org.atlassian.net/browse/GEOS-5587)])


See the [change log](#release-notes) for all the details. Special thanks to everyone who contributed for this release.

Try out the release candidate today and help us by reporting any issues found on the [GeoServer mailing list](https://web.archive.org/web/20130226/http://geoserver.org/display/GEOS/Mailing+Lists) and in the [bug tracker](https://osgeo-org.atlassian.net/issues/?jql=project%3DGEOS).

## Release notes

Improvement:

* [GEOS-3847](https://osgeo-org.atlassian.net/browse/GEOS-3847) GWC needs to get proxy prefix from GSs configuration
* [GEOS-5573](https://osgeo-org.atlassian.net/browse/GEOS-5573) Missing i18 support for Pallete headers for selected and avaliable columns
* [GEOS-5601](https://osgeo-org.atlassian.net/browse/GEOS-5601) Create passthrough tile recycler
* [GEOS-5606](https://osgeo-org.atlassian.net/browse/GEOS-5606) Add a possibility to obtain a forgotten master password
* [GEOS-5608](https://osgeo-org.atlassian.net/browse/GEOS-5608) Make the exception translation filter configurable

Bug:

* [GEOS-4718](https://osgeo-org.atlassian.net/browse/GEOS-4718) SLD 1.1.0 GraphicFill (Polygon Symbolizer)  is not working
* [GEOS-5491](https://osgeo-org.atlassian.net/browse/GEOS-5491) ldap group mapping to admin role fails
* [GEOS-5518](https://osgeo-org.atlassian.net/browse/GEOS-5518) "Validate" SLD - "Parameter message can't be null"
* [GEOS-5528](https://osgeo-org.atlassian.net/browse/GEOS-5528) Server Status timestamps
* [GEOS-5534](https://osgeo-org.atlassian.net/browse/GEOS-5534) GetFeatureInfo templates don't work when layer has more than 20 class breaks
* [GEOS-5535](https://osgeo-org.atlassian.net/browse/GEOS-5535) Use of SDO_TUNE.EXTENT_OF - doesn't include schema
* [GEOS-5544](https://osgeo-org.atlassian.net/browse/GEOS-5544) SLD 1.1 - External Graphics
* [GEOS-5556](https://osgeo-org.atlassian.net/browse/GEOS-5556) count=0 - WFS GetFeature
* [GEOS-5587](https://osgeo-org.atlassian.net/browse/GEOS-5587) Exception in WMS GetLegendGraphic WMS on a layer with a geometry type of GEOMETRY
* [GEOS-5592](https://osgeo-org.atlassian.net/browse/GEOS-5592) GetLegendGraphic doesn't correcly render symbols bigger than icon requested size
* [GEOS-5597](https://osgeo-org.atlassian.net/browse/GEOS-5597) GWC_DISKQUOTA_DISABLED not respected
* [GEOS-5602](https://osgeo-org.atlassian.net/browse/GEOS-5602) REST GETs and authentication under 2.3
* [GEOS-5607](https://osgeo-org.atlassian.net/browse/GEOS-5607) Layer groups in container mode break layer preview page
* [GEOS-5624](https://osgeo-org.atlassian.net/browse/GEOS-5624) gs:Aggregate fails to encode output as WPS response document
* [GEOS-5628](https://osgeo-org.atlassian.net/browse/GEOS-5628) CatalogInfo objects will be cloned and rendered often useless when working against the GUI with multiple tabs open
* [GEOS-5629](https://osgeo-org.atlassian.net/browse/GEOS-5629) Monitoring and Excel modules use conflicting versions of Apache POI
* [GEOS-5630](https://osgeo-org.atlassian.net/browse/GEOS-5630) Fix Management of multivalued custom dimensions
* [GEOS-5633](https://osgeo-org.atlassian.net/browse/GEOS-5633) Disk quota never goes down
* [GEOS-5634](https://osgeo-org.atlassian.net/browse/GEOS-5634) enabling "disk quota" causes disk quota page to bug-out
* [GEOS-5645](https://osgeo-org.atlassian.net/browse/GEOS-5645) GET Request including same parameter multiple times fails
* [GEOS-5649](https://osgeo-org.atlassian.net/browse/GEOS-5649) Performing WMS over a cascaded WFS 1.0 store fails with exceptions

Task:

* [GEOS-5375](https://osgeo-org.atlassian.net/browse/GEOS-5375) Update JAITools dependency to 1.3.0
* [GEOS-5496](https://osgeo-org.atlassian.net/browse/GEOS-5496) Add gt-complex to app-schema plugin release descriptor
