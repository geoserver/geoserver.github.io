---
author: jgarnett
comments: false
date: 2019-11-14 00:54:01+00:00
layout: post
link: http://blog.geoserver.org/2019/11/14/cite-test-automation-request-for-proposal/
slug: cite-test-automation-request-for-proposal
title: CITE Test Automation Request for Proposal
wordpress_id: 3068
---




GeoServer Project Steering Committee is seeking a solution for automated CITE [TEAM Engine](https://github.com/opengeospatial/teamengine) tests for [build.geoserver.org](https://build.geoserver.org/view/geoserver/).







If you or your organization is interested in this work please respond to the [geoserver-devel](http://geoserver.org/devel/) email list with your interest by the end of November. Applicants are welcome to email geoserver-devel list, or attend bi-weekly GeoServer meeting, with any questions or clarifications of requirements.







For details, including detailed requirements, see [GSIP-176 fundraising](https://github.com/geoserver/geoserver/wiki/GSIP-176), [maintenance activity](https://github.com/geoserver/geoserver/wiki/CITE-Test-Upgrade) wiki page, and prior [blog post](http://blog.geoserver.org/2019/09/18/join-me-in-funding-an-important-geoserver-initiative/).







**Schedule Update:** Please email geoserver-devel if you are interested in this activity by the end of November, we will evaluate proposal during GeoServer Meeting December 10th.







#### Clarrifications







There are three approaches discussed:







  * **cite command line:** our previous scripts made use of a the cite engine to run tests on the command line.
  * **cite engine service:** The new cite engine has a rest-api, so the testing script could use CURL commands to ask the engine to run the tests
  * **cite engine docker:** The cite engine is also distributed as a docker image, if that makes it easier to manage the rest-api approach 






Any of these approaches can be viable, or you may have additional ideas. The challenge (after our last experience) is setting up something that can be maintained.







Notes:







  * The WFS-T tests required a database to run, the tests created a couple of tables each time (since the transaction request modifies the content)






### Thanks to sponsors







We would like to thank everyone who has supported this activity via [sponsorship](https://github.com/geoserver/geoserver/wiki/Sponsor) and [donation](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=4XZ76BZMEWZ24&source=url).  Special thanks [OSGeo](https://www.osgeo.org) along with activity sponsors [Gaia3D](https://gaia3d.com), and [OSGeo:UK](https://uk.osgeo.org) for help making this possible.





![](http://blog.geoserver.org/wp-content/uploads/2019/11/OSGeo_project.png)



![](http://blog.geoserver.org/wp-content/uploads/2017/03/Gaia3d.png)



![](http://blog.geoserver.org/wp-content/uploads/2019/11/osgeo_uk_logo.png)

