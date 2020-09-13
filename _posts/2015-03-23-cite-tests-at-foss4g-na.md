---
author: geoserver
comments: true
date: 2015-03-23 21:16:36+00:00
layout: post
link: http://blog.geoserver.org/2015/03/23/cite-tests-at-foss4g-na/
slug: cite-tests-at-foss4g-na
title: CITE Tests at FOSS4G-NA
wordpress_id: 2184
---

Thanks to some last minute planning, and Boundless renting space, we were able to set aside some time for a code sprint after the FOSS4G-NA conference. One of the goals of this sprint was to onboard new developers to build and run CITE tests. We also had Jim Hughes from GeoMesa joining us as a new GeoServer community member.




![](https://lh3.googleusercontent.com/GoPLpY2KVwzCOm_-RpG0CgpuA9XlUnz2KnsWEDhSNbwLXhEKU0ne2IU3VnZUF5CY9Rtzzo9aoIiphi1rA_OOXv66Fz53E_PZX-m6NbgZ8U6JS0Qq2nEKVHeo8CcwJp1WhUnUIK0)




_**Clockwise from the bottom left corner:** Torben Barsballe (Boundless), Travis Brundage (Boundless), Kevin Smith (Boundless), Andrea Aime (GeoSolutions)_




_**Offscreen:** Jim Hughes (GeoMesa), Jody Garnett (Boundless), Tyler Battle (Boundless)_





Andrea introduced us to the[ OGC Compliance Testing Program](http://cite.opengeospatial.org/) (CITE), which provides resources for ensuring conformance with the OGC Standards.




One of the core tools within CITE is the[ Test, Evaluation, And Measurement](http://opengeospatial.github.io/teamengine/index.html) (TEAM) Engine, which executes test suites written using the OGC Compliance Test Language (CTL). This is the official test framework of the CITE program, and all CITE tests published by the OGC are written for the TEAM engine, using CTL.




Currently, we execute a number of nightly geoserver builds that run CITE tests:






	
  * cite-wcs-1.0

	
  * cite-wcs-1.1

	
  * cite-wfs-1.0

	
  * cite-wfs-1.1

	
  * cite-wms-1.1

	
  * cite-wms-1.3




These do not encompass the full set of CITE tests published by the OGC. In the interests of adding better test coverage, it is important to familiarize new developers with how the CITE tests are build and run.




During the code sprint, we attempted to set up and execute tests on a local instance of the TEAM engine. This entailed:






	
  * Building the[ latest GeoServer](https://github.com/geoserver/geoserver)

	
  * Building the[ latest TEAM engine](https://github.com/opengeospatial/teamengine)

	
  * Building [the ets-wfs10 test suite](https://github.com/opengeospatial/ets-wcs10), provided by the OGC




To run the WFS 1.0 CITE tests, we:






	
  * Ran geoserver using citewfs-1.0 data directory

	
  * Ran the TEAM Engine on a local tomcat server

	
  * Configured the WFS test suite in the TEAM engine, and ran it.




There were a few hiccups during this process, but closely following the existing documentation was sufficient to get the CITE tests running properly. While I did not run into this issue, Andrea mentioned that bugs in the CITE tests themselves are about as common as bugs in the OGC-compliant GeoServer services. This makes running CITE tests a bit of a treasure hunt between which test failures are coming from from the tests, and which are coming from the service being tested.




![](https://lh4.googleusercontent.com/4F0_-w17oOLFSQHmYhXeoSP9Pc0yBnRLWHE2Be9tVI7fuxyoJmeW_G6w0BWuQs7IAdCmf5xyL2E1ZmnM27NQHxbPamQ-kJ_yvwHdw3NURF1zQldv7wOvXytbcEL1n1pGTxxcGFU)




_**Successful WFS 1.0 CITE Tests!**_





After I succeed in getting the WFS 1.0 test suite running, I tried building the WCS 1.0 test suite (which was a bit more complicated). I was able to get the tests running, but encountered a number of test failures. Among other things, the WCS CITE tests fail if the endpoint they are querying also publishes WCS 1.1 resources. This means that in order to properly run the tests, you have to build GeoServer without WCS 1.1. There also other test failures that I was unable to debug during the sprint.





## Thanks


We would like to thank the GeoServer community for welcoming newcomers, Boundless for renting the space and congratulate Jim Hughes on his new community modules.
