---
author: bmmpxf
comments: true
date: 2008-04-16 15:04:20+00:00
layout: post
link: http://blog.geoserver.org/2008/04/16/not-news-the-64-bit-question/
slug: not-news-the-64-bit-question
title: '(Not) News: The 64 Bit Question'
wordpress_id: 101
categories:
- Features
---

As time goes on, more and more systems are moving towards 64 bit  architecture.  Pretty much all new servers are 64 bit, and the vast  majority of desktop/laptop systems are 64 bit as well.  (And if you  are running SPARC hardware, well, then you've been running 64 bit  hardware since 1995, but that's a different story.)  We at GeoServer  HQ are starting to get this question more and more:  Does GeoServer  run on 64 bit systems?

The quick answer:  yes!

GeoServer is built entirely on Java.  Therefore, it can run on any  hardware supported by Sun's Java Runtime Environment.  Unlike compiled  languages, like C++, as long as the JRE supports the architecture,  GeoServer can come along for the ride.  Happily, 64 bit support exists  in Java.  So without any redesign or recompiling on our part,  GeoServer can be run on 64 bit systems.  That's points for Java!

However, there are some caveats.  Sun's 64 bit JRE has been known be a  bit buggier than their 32 bit version, which could be of concern in a  production environment.  Also, and probably related, performance takes  a small hit with 64 bit (on the order of a few percent).  Although  there will be more discussion here later about performance tips, this  seems like as good a place as any to mention that if performance is an  issue on your system, we recommend that you look at updating your JRE  to the latest version, if you can.  Version 1.5 is much faster than  1.4, and version 1.6 appears to be roughly twice as fast as 1.5 in the  context of running GeoServer.  So, if you are moving to 64 bit but  can't afford the performance hit, you may want to look at updating  your Java version as well.

Moving to 64 bit doesn't need to be an either/or situation either.  Our servers here (all 64 bit) are running both 32 bit and 64 bit Java instances, with few difficulties.  Your mileage may vary.  And of course, the big advantage of 64 bit is the ability to access more than 4 GB of RAM.  This may not be an issue in your environment now, but if history is any guide, it will be eventually.

For more information on running GeoServer in a production environment, please see [this guide](http://geoserver.org/display/GEOSDOC/2.6+GeoServer+in+Production+Environment).

Many software companies are at pains to inform the community when they  offer 64 bit support.  We have never explicitly mentioned this feature  before because it has been offered from the beginning.  We can't take  credit for the work, but we can surely enjoy the perks.
