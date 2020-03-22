---
author: geoserver
comments: true
date: 2010-04-09 14:49:18+00:00
layout: post
link: http://blog.geoserver.org/2010/04/09/sld-cookbook/
slug: sld-cookbook
title: SLD Cookbook
wordpress_id: 576
categories:
- Announcements
- Tips and Tricks
tags:
- cookbook
- reference
- SLD
- style
- styling
---

Styling map layers in GeoServer can be challenging.  While there are [some](http://blog.geoserver.org/2010/04/05/styling-geoserver-layers-with-css/) [ways](http://blog.opengeo.org/2009/05/05/styler/) to craft map layers without ever needing to look at Styled Layer Descriptor (SLD) code, there are some who don't want an intermediary and want to code with SLD directly.  For those, there are few options:

1. Read the [OGC SLD 1.0 specification](http://www.opengeospatial.org/standards/sld).  At 100+ pages, it can be a bit dense.
2. Read the [SLD schema](http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd).  Because, really, who doesn't love interpreting schemas?

Failing those, the would-be map stylist is usually out of luck, needing to eke out an understanding of styling by asking on [mailing lists](https://lists.sourceforge.net/lists/listinfo/geoserver-users) and doing web searches.

When I was learning SLD, I wanted simple examples that I could understand and edit.  I wanted screenshots.  I wanted to know which line of code did what.  I wanted to look up styles as if they were in a recipe book.  But this type of reference didn't exist at the time.

The [SLD Cookbook](http://docs.geoserver.org/stable/en/user/styling/sld-cookbook/index.html) is that reference.  It is a "practical reference" to show how map styling works.  It is not designed to be exhaustive, and it won't tell you about every possible edge case.  But it also has no SLDs that are hundreds of lines long, a strong hurdle to comprehension.

Want to know how to style a simple point?  [Look at the example](http://docs.geoserver.org/stable/en/user/styling/sld-cookbook/points.html#simple-point), [download the SLD](http://docs.geoserver.org/stable/en/user/_downloads/point_simplepoint.sld) (and the [shapefile](http://docs.geoserver.org/stable/en/user/_downloads/sld_cookbook_point.zip) that generated the screenshot too, if you'd like), and [read the details](http://docs.geoserver.org/stable/en/user/styling/sld-cookbook/points.html#details).  See which line of code accomplishes what, so if you want to make the points blue instead of red, you'll know what line to change (line 8 in this case).  Want to see how to make a style where lines are styled differently by [data attributes](http://docs.geoserver.org/stable/en/user/styling/sld-cookbook/lines.html#attribute-based-line)? Or by [zoom level](http://docs.geoserver.org/stable/en/user/styling/sld-cookbook/lines.html#zoom-based-line)?  Refer as necessary.  Even those experienced with SLD may find the examples useful.

There are a few examples mixed in that leverage extensions to GeoServer/GeoTools ([polygon fill hatching](http://docs.geoserver.org/stable/en/user/styling/sld-cookbook/polygons.html#hatching-fill), [labels that follow lines](http://docs.geoserver.org/stable/en/user/styling/sld-cookbook/lines.html#label-following-line)) but for the most part, the examples are perfectly valid according to the SLD 1.0 specification.

I'm sure that more examples can and will be added in time.  I've already received some very good feedback from others, and some styles will likely be optimized.  But every example, every screenshot, and every SLD was tested in the [most recent version of GeoServer](http://geoserver.org/display/GEOS/Stable).

So [take a look](http://docs.geoserver.org/stable/en/user/styling/sld-cookbook/index.html), and get styling!  I hope you enjoy.  Special thanks goes out to [Geonovum](http://www.geonovum.nl/), who funded this project.  I personally appreciate it.
