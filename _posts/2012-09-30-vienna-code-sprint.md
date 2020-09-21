---
author: geoserver
comments: true
date: 2012-09-30 20:11:50+00:00
layout: post
link: http://blog.geoserver.org/2012/09/30/vienna-code-sprint/
slug: vienna-code-sprint
title: Vienna Code Sprint
wordpress_id: 1176
categories:
- Behind The Scenes
- Developer notes
---

This past week a few of the GeoServer developers gathered for a code sprint in Vienna, Austria. The sprint was planned by some of the OpenLayers developers and they graciously allowed us to join the party and share the venue for the week.

Attendees from the GeoServer community included Andrea Aime, Niels Charlier, Justin Deoliveira, Alessio Fabiani, Christian Mueller, and Victor Olaya. With this seasoned team of committers in one location we decide to tackle a problem that has been plaguing developers for quite some time. Slow build and test times.

GeoServer, having been around for a while, has accumulated a large number of test cases in its 10+ years of existence. As of today the GeoServer code base contains 695 test classes and 3189 individual test cases. Wow. While many wouldn't really consider good test coverage a problem it does come with a price. The more tests a project has the longer it takes to build.

Now like any other best practice following open source project we do have a continuous integration server that runs the tests whenever someone pushes up a change. But being the responsible bunch we are the developers usually run tests before a commit to ensure nothing breaks, especially for larger changes. Long build times start to make things tedious pretty fast. There is only so much coffee a developer can drink in one day.

Ok, enough about the problem, those interested in learning more should read over the [recent GSIP](http://geoserver.org/display/GEOS/GSIP+80+-+Testing+Overhaul) that explains the problem and solution in detail. During the sprint the team outlined three goals: improving overall test times, upgrading the codebase to JUnit 4, and setting ourselves up to continue to make testing improvements in the future.

I am very excited to report that we accomplished all three of these goals. The 6 of us worked tirelessly to update every single test case in the codebase and the end result was about a 50% improvement making the build run twice as fast. The following chart shows the improvements in the various modules.

[](http://blog.geoserver.org/2012/09/30/vienna-code-sprint/test_times-2/)[![](http://geoserver.wpengine.com/wp-content/uploads/2012/09/test_times21.png)](http://blog.geoserver.org/2012/09/30/vienna-code-sprint/test_times-3/)

Great stuff. Thanks again to the developers who attended and made it such a productive week.

We’d also like to extend a very special thank you to the [Research Group Cartography](http://cartography.tuwien.ac.at/content07en/index.php) of the Vienna University of Technology for sponsoring the sprint by providing such an excellent venue. And an even bigger thanks to Andreas Hocevar who secured the venue, planned accommodations for attendees, and kept us all sufficiently caffeinated by brining along is espresso machine. Also a congratulations to the OpenLayers team who made some awesome [progress toward OL3](http://openlayers.org/blog/2012/09/28/ol3-vienna-code-sprint-report/).
