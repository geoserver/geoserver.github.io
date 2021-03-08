---
author: bmmpxf
comments: true
date: 2016-01-25 23:05:20+00:00
layout: post
link: http://blog.geoserver.org/2016/01/25/geoserver-code-sprint-success/
slug: geoserver-code-sprint-success
title: GeoServer code sprint success
wordpress_id: 2601
categories:
- Behind The Scenes
tags:
- Code Sprint
- developer
- GeoServer
- wicket
---

It's been an exciting time here at GeoServer HQ. To explain, let's start with a little history lesson.


### History


In 2009, [GeoServer released GeoServer 2.0](http://blog.geoserver.org/2009/10/26/geoserver-2-0-released/), sporting a new user interface based on [Apache Wicket](http://wicket.apache.org/). Wicket allows Java developers to construct an AJAX UI with minimal HTML experience. Since its adoption, Wicket has made development of GeoServer more accessible, due the ease of creating graphical configuration pages.

The problem is that we've still been using Wicket version 1.4 all this time, and the current version is 7. We've tried to address this activity at two previous single-day code sprints, which were aborted due to insufficient time and resources. **And the longer we've waited, the more difficult it has become.**

Without an upgrade, we were starting to see less compatibility with modern browsers, which would eventually lead to the UI not being usable. Something needed to be done.


### Enter the code sprint


The [GeoServer PSC](http://docs.geoserver.org/latest/en/developer/policies/psc.html#current-psc) responded to this challenge by contacting sponsors and [organizing a code sprint](https://wiki.osgeo.org/wiki/GeoServer_Code_Sprint_2016).

This was not a small task. The problem is neatly summed up by a graphic created by Jody Garnett explaining the Wicket upgrade:

[![Can you see the difference? Neither can we.](/img/uploads/Wicket-upgrade.png)](/img/uploads/Wicket-upgrade.png) Can you see the difference? Neither can we.

As you can see, **when properly implemented, the visual change for users will be...nothing at all.**

So I was very impressed when we got the go-ahead (and funding!) to meet in Victoria, BC, at the Boundless Canadian office.


### What we did


Developers from the US, Canada, Italy, and Belgium descended upon the diminutive capital of British Columbia to spend a week doing the upgrade.

Since we held off this work for so long, it wasn't as simple as a single upgrade, as we had to [negotiate several API changes in one go](https://github.com/geoserver/geoserver/wiki/Wicket-migration-code-sprint). And GeoServer, being highly extensible software, has dozens of modules and extensions that needed to be tested too:

[![](/img/uploads/codesprint2016modules.png)](/img/uploads/codesprint2016modules.png) And on and on...


### Developer experience


Here is the team and their primary accomplishments:



	
  * **Andrea Aime** (GeoSolutions): Really focused on fixing the build and crushing bugs as they popped up in manual testing. Spent a lot of time migrating the security modules.

	
  * **Torben Barsballe** (Boundless): Unit test fixes. Component testing. Styling fixes. Fixed links on the Styles page Fixed the Layer Importer. Fixed the LegendGraphic display.

	
  * **Niels Charlier** (Scitus): Fixed code and unit tests for many of the core components. Manually tested and fixed many commonly used pages in the UI such as the Layer Preview and Tile Caching sections.

	
  * **Justin Deoliveira** (Voyager Search):  Justin helped out monday-tuesday getting the wicket7 branch to compile and helping everyone learn the tips and tricks of wicket debugging.

	
  * **Jody Garnett** (Boundless): Learned a lot about how Wicket worked, suffered through manual testing and enjoyed making usability improvements to the configuration pages.

	
  * **Jim Hughes** (CCRi): Helped with updates to unit tests. Fixed issues identified by testers.

	
  * **Morgan Thompson** (Boundless): Fixed the CoverageBands panel for raster pages. Tested/upgraded the Stores page. Tested various other pages such as the Security section and NetCDF.

	
  * **Devon Tucker** (Boundless): Manual testing of core GeoServer and some extensions. Fixed some regressions from the Wicket migrations and did some improvements on the Layers page


And one week later, **we are excited to announce that the sprint was a success**, and GeoServer is now running Wicket 7. Hooray!

Here is a [master nightly build](http://geoserver.org/release/master/) - please download and test it out.


### Documentation changes


I was invited to take part in the code sprint, but as I focus on documentation and user experience, I had a lot of down time while the rest of the team was deep in the weeds.

So I took a hard look at the [GeoServer User Manual](http://docs.geoserver.org/latest/user/), and performed a fairly significant restructuring, along with some small improvements in the theme.

You can see the [new documentation](http://docs.geoserver.org/latest/user/), (compare to [an older version](http://docs.geoserver.org/2.7.2/user/)). Details on what was done can be [found on GitHub](https://github.com/geoserver/geoserver/pull/1439). I feel like these changes will make it easier to find information in the documentation, which is fairly extensive.

[![docupgrade](/img/uploads/docupgrade.png)](/img/uploads/docupgrade.png) Documentation Upgrade

More exciting were the visual documentation improvements. I updated the theme of the documentation to increase readability and fix some visual bugs (for example step 10 and higher being cut off).



[![doc_content](/img/uploads/doc_content-1024x394.png)](/img/uploads/doc_content.png) Documentation Theme and Content Update


### Visual Changes and Blue-sky thinking


With so many experienced GeoServer users in the room, we had a short breakout session discussing high-level improvements to the UI and its workflow, in an attempt to answer the question, "**what have you always wished the GeoServer UI would do?**" It didn't take too long to fill up a spreadsheet full of more than two dozen ideas for the next co de sprint- and the team was able to make a few of the easier ones on Thursday and Friday.

The rest of the team decided to follow suit and made a few small visual changes, such as:



	
  * Updating the JAI page (now called "Image Processing")

	
  * Updating the Coverage Access page (now called "Raster Access")

	
  * "Add a new resource" is now called "Add a new layer". (Minuscule change, but this has bugged me _for years_.)

	
  * Group fields consistently in Global Settings


So I guess we got some visual changes in after all. Hooray again!

[![Global Settings](/img/uploads/global-1024x937.png)](/img/uploads/global.png) Adding Headings and Reorganizing Global Settings


### Thanks


Thanks to [OSGeo](http://www.osgeo.org), [Boundless](http://boundlessgeo.com), [Vivid Solutions](http://www.vividsolutions.com/), [How 2 Map](http://www.how2map.com/), [San Jose Water Company](https://www.sjwater.com/), [Transient](http://transient.nz/), [GeoBeyond](http://www.geobeyond.it/), [Scitus](http://www.scitus.be/), [GeoSolutions](http://www.geo-solutions.it/), [CCRi](http://www.ccri.com/), [Astun Technology](https://astuntechnology.com/), and [Voyager Search](https://www.voyagersearch.com/) for sponsoring this work.

It's precisely this kind of support for OSGeo projects that enable our community to thrive.

[![OSGeo_project.png](/img/uploads/OSGeo_project1.png)](/img/uploads/OSGeo_project1.png)



[![DSC01732](/img/uploads/DSC01732-300x199.jpg)](/img/uploads/DSC01732.jpg)  [![DSC01733](/img/uploads/DSC01733-300x199.jpg)](/img/uploads/DSC01733.jpg)

[![DSC01736](/img/uploads/DSC01736-300x199.jpg)](/img/uploads/DSC01736.jpg)   [![DSC01739](/img/uploads/DSC01739-300x199.jpg)](/img/uploads/DSC01739.jpg)

[![DSC01741](/img/uploads/DSC01741-300x199.jpg)](/img/uploads/DSC01741.jpg)  [![IMG_1106](/img/uploads/IMG_1106-1-300x225.jpg)](/img/uploads/IMG_1106-1.jpg)

[![IMG_1111](/img/uploads/IMG_1111-300x225.jpg)](/img/uploads/IMG_1111.jpg)

[![IMG_1112](/img/uploads/IMG_1112-169x300.jpg) ![DSC01734](/img/uploads/DSC01734-199x300.jpg) ![DSC01738](/img/uploads/DSC01738-199x300.jpg)](/img/uploads/IMG_1112.jpg)
