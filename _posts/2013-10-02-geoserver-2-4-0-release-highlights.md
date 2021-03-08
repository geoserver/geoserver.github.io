---
author: geoserver
comments: true
date: 2013-10-02 05:52:00+00:00
layout: post
link: http://blog.geoserver.org/2013/10/02/geoserver-2-4-0-release-highlights/
slug: geoserver-2-4-0-release-highlights
title: GeoServer 2.4.0 Release Highlights
wordpress_id: 1656
categories:
- Developer notes
---

We noticed out friends at Slashgeo [could not quite figure](http://www.slashgeo.org/2013/09/24/GeoServer-24-Released) out what is new with the GeoServer 2.4.0 release - so we have updated the [release announcement](http://blog.geoserver.org/2013/09/20/geoserver-2-4-released/) with a 2.4.0 feature list.

For a more complete story check out the State of GeoServer 2013 presentation on on [elogeo](http://elogeo.nottingham.ac.uk/xmlui/handle/url/229) or [slideshare](http://www.slideshare.net/jgarnett/state-of-geo-server-foss4g-2013-26387643).

Let me call out several significant developments from the GeoServer product story:



	
  * **CSS Extension:** David Winslow is a long standing member of the GeoServer community, however his most significant work has been hiding in the community modules. With this release of GeoServer the CSS module has become a formal GeoServer extension.
[![](/img/uploads/css-300x2741.png)](http://blog.geoserver.org/2013/10/02/geoserver-foss4g-2013/css/)
This module being brought into core is having a serious impact on the GeoServer usability story and is an excellent contribution. The documentation has been updated with a complete [CSS cookbook](http://docs.geoserver.org/latest/en/user/extensions/css/cookbook.html) (as a counterpoint to the [SLD cookbook](http://docs.geoserver.org/latest/en/user/styling/sld-cookbook/index.html)) and represents a great learning aid.
_Talking points: there are some technical reasons (the CSS module is written in Scala rather than Java) why it has remained a community module up until now. The GeoServer community opening up, even a little bit, to other JVM languages is an interesting change of strategy._

	
  * **Time boxed release model: **GeoServer 2.4.0 was released on time with little drama.
[![](/img/uploads/time_box-300x1831.png)](http://blog.geoserver.org/2013/10/02/geoserver-foss4g-2013/time_box/)
_Talking points: This is kind of old news now, but with all the mad panic around FOSS4G releases seen over the course of the week I have to call out the GeoServer community for being excellent. It is not enough to release open source software, releasing on schedule is the new normal._

	
  * **NetCDF and GeoTools Raster API improvements
**[![](/img/uploads/netcdf-300x142.png)](http://blog.geoserver.org/2013/10/02/geoserver-foss4g-2013/netcdf/)
_Talking points: This change is flying under the radar, but is significant from a product story as it is opening up new markets to the GeoServer application. It is a long term play, and there is work to be done, but it is wonderful to see the first steps taken in a responsible and measured manner._

	
  * **Importer community module** (heading to extension shortly!) offering a wizard like process for the bulk publication of data, automating common activities such as transformation and generation of default styling.
[![](/img/uploads/importer-300x146.png)](http://blog.geoserver.org/2013/10/02/geoserver-foss4g-2013/importer/)
_Talking points: This represents a significant contribution from the downstream OpenGeo Suite being donated back to the GeoServer community to enable collaboration and improvement. GeoServer has a number of downstream distributions and this is a great example of healthy community participation._



