---
author: geoserver
comments: true
date: 2010-12-20 15:38:13+00:00
layout: post
link: http://blog.geoserver.org/2010/12/20/geoserver-2-1-beta3-released-now-with-wms-1-3/
slug: geoserver-2-1-beta3-released-now-with-wms-1-3
title: GeoServer 2.1-beta3 released (now with WMS 1.3)
wordpress_id: 811
categories:
- Announcements
tags:
- beta
- cql
- se
- SLD
- sql
- wms
- wms 1.3
---

The GeoServer community is proud to announce the release of 2.1-beta3, which is now available for [download](http://geoserver.org/display/GEOS/GeoServer+2.1-beta3).

The big feature for this release is support for **WMS 1.3**. Special thanks goes out to [Ordnance Survey](http://www.ordnancesurvey.co.uk/), Great Britain's national mapping agency, for providing [OpenGeo](http://opengeo.org/) with funding to complete the task. With WMS 1.3 mandated by the [INSPIRE Initiative](http://inspire.jrc.ec.europa.eu/), the Ordnance Survey needed to meet the INSPIRE requirements.  Rather than implement a solution on their own, they opted to fund the GeoServer project so that other organizations in the UK and the rest of Europe and the world could all benefit.

This is the value and the beauty of open source.  Government agencies across Europe can now upgrade their servers to the latest GeoServer at no additional cost.  In time, other mapping agencies can and will further benefit one another by funding additional GeoServer improvements, like WFS 2.0 and [Application Schema](http://docs.geoserver.org/latest/en/user/data/app-schema/index.html) configurations for INSPIRE, but the Ordnance Survey deserves special recognition from all GeoServer users for taking the lead.

In addition to WMS 1.3, this release includes some **SLD 1.1 / SE 1.1 enhancements**.  It will be possible to use most SE 1.1 documents, though not every new option is fully supported yet.  User feedback on which new options we should support first is greatly appreciated.  Also funded by Ordnance Survey is a community module to implement the WMS extensions for INSPIRE View Service compliance—namely the language parameter and several extended capabilities fields.

The release also includes a few nice fixes and improvements from beta2, such as [upgrading CQL to ECQL](http://jira.codehaus.org/browse/GEOS-3928), and [a fix](http://jira.codehaus.org/browse/GEOS-4254) by Eli Miller, a newcomer to the GeoServer community, to allow the [REST Config API](http://docs.geoserver.org/latest/en/user/extensions/rest/index.html) to properly handle [SQL Views](http://docs.geoserver.org/latest/en/user/data/sqlview.html).

We encourage you to [download GeoServer 2.1-beta3](http://geoserver.org/display/GEOS/GeoServer+2.1-beta3), try it out, and let us know if there are any bugs.  This software is still a beta, so we recommend testing extensively before running it in a production environment.  That said, we're hoping to move to 2.1.0 release candidates soon, so any and all testing will this process move along faster.

**[Download GeoServer 2.1-beta3](http://geoserver.org/display/GEOS/GeoServer+2.1-beta3)**
