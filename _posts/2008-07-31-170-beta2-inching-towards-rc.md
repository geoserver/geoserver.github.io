---
author: bmmpxf
comments: true
date: 2008-07-31 15:11:26+00:00
layout: post
link: http://blog.geoserver.org/2008/07/31/170-beta2-inching-towards-rc/
slug: 170-beta2-inching-towards-rc
title: '1.7.0-beta2: Inching Towards RC'
wordpress_id: 116
categories:
- Announcements
---

The GeoServer team has been working full steam ahead on the new branch (1.7.x) of GeoServer.  With [1.7.0-beta2](http://geoserver.org/display/GEOS/GeoServer+1.7.0-beta2) released, [KML regionating](http://geoserver.org/display/GEOS/GSIP+20+-+Automated+Regionating+in+KML+MapProducer) has been optimized.  Regionating is the process of automatically filtering what data is shown based on an attribute of that data (say, only showing large features when zoomed out).  Currently regionating is only functional for KML output, but this may eventually change.  Also, [per-layer security](http://geoserver.org/display/GEOS/GSIP+19+-+Per+layer+security) has been added and enhanced, which people have been asking about on the mailing list for some time.  Per-layer security* will allow for layers to be viewable based on certain security credentials.  _*The development team is looking for a better, more succinct name than "per-layer security."  If you have an awesome name suggestion, [meet us in IRC](http://geoserver.org/display/GEOSDOC/3+IRC) and tell us!

_This is still a beta, so bugs will occur.  Nevertheless, if you find one, [please let us know](http://jira.codehaus.org/browse/GEOS).  Also, we still haven't abandoned the 1.6.x branch (the most recent stable version remains at [1.6.4](http://geoserver.org/display/GEOS/GeoServer+1.6.4)), so if you're not looking for cutting edge (or if you're looking to run [GeoServer in a production environment](http://geoserver.org/display/GEOSDOC/2.6+GeoServer+in+Production+Environment)), [1.6.4](http://geoserver.org/display/GEOS/GeoServer+1.6.4) is the version you want.

We'll be unveiling some exciting news about the future of GeoServer fairly soon, so stay tuned!
