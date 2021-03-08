---
author: Justin Deoliveira
comments: true
date: 2009-01-26 02:14:21+00:00
layout: post
link: http://blog.geoserver.org/2009/01/25/geoserver-172-released/
slug: geoserver-172-released
title: GeoServer 1.7.2 Released
wordpress_id: 171
categories:
- Announcements
- Features
---

The GeoServer team would like to announce the release of [GeoServer 1.7.2](http://geoserver.org/display/GEOS/GeoServer+1.7.2).  This release brings many exciting new features.

The first major improvement is label rendering. In version 1.7.1, GeoServer added support for [curved labeling](http://blog.geoserver.org/2009/01/08/throw-geoserver-a-curve/).  In this version, support is added for [wrapped labels](http://geoserver.org/display/GEOSDOC/LabelingOptions#LabelingOptions-newlabel), which enables a label to span multiple lines. This feature affects the labeling of points and polygons.

[![](/img/uploads/wrappedlabels1.png)](/img/uploads/wrappedlabels1.png)

Thanks to Andrea Aime for all the great labeling improvements.

Another new styling feature is support for [hatching](http://geoserver.org/display/GEOSDOC/Hatching).  Among many other new designs, this allows **railroad styling** to be accomplished for the first time.  Also, polygon hatched fills can now be drawn, and GeoServer ships with a new style, `pophatch.sld`, that can be applied to the topp:states layer to see this in action.

[![](/img/uploads/hatchedfills-300x2141.png)](/img/uploads/hatchedfills1.png)

The 1.7.2 release also brings some great new extensions. The [HTML imagemap extension](http://geoserver.org/display/GEOS/HTML+ImageMap+support) ([download](http://downloads.sourceforge.net/geoserver/geoserver-1.7.2-imagemap-plugin.zip)), contributed by Mauro Bartolomeoli, allows a user to add interactive features to a map without the use of Flash, SVG, or other dynamic content languages. You can check out the [imagemap extension in action](http://geo.openplans.org/states.html).  A special thanks to Mauro for the contribution.

The new and improved DB2 extension ([download](http://downloads.sourceforge.net/geoserver/geoserver-1.7.2-db2ng-plugin.zip)), which allows connection with [IBM DB2 databases](http://www.ibm.com/db2) is based on the [GeoTools JDBC Next Generation](http://geotools.codehaus.org/JDBC+DataStore+-+NG) framework. The extension was contributed by Christian Müller, who is an active member of the [GeoTools](http://geotools.org) community. Special thanks to Christian.

The new [OGR extension](http://geoserver.org/display/GEOS/Ogr2Ogr+based+WFS+output+format) ([download](http://downloads.sourceforge.net/geoserver/geoserver-1.7.2-ogr-plugin.zip)) is based on the [GDAL/OGR](http://www.gdal.org/ogr/) library. The extension adds the ability to output from WFS any of the formats supported by OGR. OGR has a very diverse and comprehensive list of output formats, so this extension very much enhances the utility of the GeoServer WFS.

Improvements were also made to the [GeoExt styler extension](http://geoserver.org/display/GEOS/GeoExt+Styler) ([download](http://downloads.sourceforge.net/geoserver/styler-1.7.2.zip)), which is a new graphical interface for map styling initially released with GeoServer 1.7.1. Tim Schaub, Andreas Hocevar, and the rest of the [GeoExt](http://www.geoext.org) team have added support for labels to the styler application.

[![](/img/uploads/stylerlabels-300x1571.png)](/img/uploads/stylerlabels1.png)

Thanks to the GeoExt team for this great improvement.

In addition, a total of [70 issues](http://jira.codehaus.org/browse/GEOS/fixforversion/14681) were handled for 1.7.2.

Thanks to everyone who contributed features and bug reports for this release. We encourage you to [download GeoServer 1.7.2](http://geoserver.org/display/GEOS/GeoServer+1.7.2), try it out, and let us know what you think. Comments and feedback are always welcome on the [mailing list](mailto:geoserver-users@lists.sourceforge.net), as the community is always interested to hear how people are using GeoServer. Stay tuned for the 1.7.3 release, slated for release in the next month, which will include improvements to [Geo Search](http://blog.geoserver.org/2008/05/13/geoserver-and-googles-geo-search/), and the official release of the REST configuration API.
