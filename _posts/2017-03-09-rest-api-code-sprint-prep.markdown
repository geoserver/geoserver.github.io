---
author: jgarnett
comments: true
date: 2017-03-09 15:34:44+00:00
layout: post
link: http://blog.geoserver.org/2017/03/09/rest-api-code-sprint-prep/
slug: rest-api-code-sprint-prep
title: REST API Code Sprint Prep
wordpress_id: 2807
categories:
- Developer notes
tags:
- sponsorship
- sprint
---

In our previous blog post we highlighted the [GeoServer Code Sprint 2017](http://blog.geoserver.org/2017/01/23/geoserver-code-sprint-2017/) taking place at the of this month. We are all looking forward to GeoSolutions [hosting us in beautiful Tuscany](http://www.geo-solutions.it/blog/geoserver-code-sprint-2017/) and have lots of work to do.

One of the secrets (and this comes as no surprise) to having a successful code sprint is being prepared. With this year's REST API migration from restlet to spring model-view-controller we want to have all technical decisions made, and examples for the developers to work from, prior to any boots hitting the ground in Italy.

But before we get into the details ...


## Code Sprint Sponsors


We would like to thank our sprint sponsors - we are honoured that so many organizations have stepped up world wide to fund this activity.

[Gaia3D](http://www.gaia3d.com/en/) is a professional software company in the field of geospatial information and Earth science technology. We would like to thank Gaia3D for their gold sponsorship.

![Gaia3d](http://blog.geoserver.org/wp-content/uploads/2017/03/Gaia3d-300x112.png)

[Insurance Australia Group](http://iag.com.au/) (IAG) is our second gold sponsor. This is a great example of open source being used, and supported, by an engineering team. Thanks to Hugh Saalmans and the Location Engineering team at IAG for your support.

[![iag_logo](http://blog.geoserver.org/wp-content/uploads/2017/03/iag_logo-300x300.png)](http://blog.geoserver.org/wp-content/uploads/2017/03/iag_logo.png)

[Boundless](https://boundlessgeo.com/) is once again sponsoring the GeoServer team. Boundless provides a commercially supported open source GIS platform for desktop, server, mobile and cloud. Thanks to Quinn Scripter and the Boundless suite team for their gold sponsorship.



[![Boundless_Logo](http://blog.geoserver.org/wp-content/uploads/2017/03/Boundless_Logo.png)](http://blog.geoserver.org/wp-content/uploads/2017/03/Boundless_Logo.png)

[How 2 Map](http://www.how2map.com) is pleased to support this year's event with a bronze sponsorship.

[![How2map_logo](http://blog.geoserver.org/wp-content/uploads/2017/03/How2map_logo.png)](http://blog.geoserver.org/wp-content/uploads/2017/03/How2map_logo.png)

I am overjoyed [FOSSGIS](https://www.fossgis.de) (German local OSGeo chapter) is supporting us with a bronze sponsorship. This sponsorship means a lot to us as the local chapter program focuses on users and developers; taking the time to support our project directly is a kind gesture.

[![fossgis_logo](http://blog.geoserver.org/wp-content/uploads/2017/03/fossgis_logo.png)](http://blog.geoserver.org/wp-content/uploads/2017/03/fossgis_logo.png)




### Sponsorship Still Needed


While we have a couple of verbal commitments to sponsor - **we are still $1500 USD off the pace**. If your organization has some capacity to financially support this activity we would dearly love your support.

_This is an official OSGeo activity; any excess money is returned to the foundation to help the next open source sprint.  OSGeo sponsorship is cumulative. Check their website for details on how your helping out the geoserver team [can be further recognized](http://www.osgeo.org/sponsorship/opportunities)._

For sponsorship details [visit the wiki page](https://wiki.osgeo.org/wiki/Java_2017_Code_Sprint#How_to_Sponsor) (or contact [Jody Garnett](mailto:jody.garnett@gmail.com) for assistance).

**Update: **Since this post was published we are happy to announce new sponsor(s).

Thanks to Caroline Chanlon and the team at [Atol Conseils et Développements](https://www.atolcd.com) for bronze sponsorship.

[![atol_logo](http://blog.geoserver.org/wp-content/uploads/2017/03/atol_logo-1024x229.png)](http://blog.geoserver.org/wp-content/uploads/2017/03/atol_logo.png)

**Update:** Thanks to David Ghedini ([acugis.com](https://www.acugis.com)) and others donating smaller amounts via the [OSGeo paypal button](http://osgeo.org).


## Getting Ready for REST


In this week's GeoServer meeting we had a chance to sit down and plan out the steps needed to get ready.

The majority of prep will go into performing the restlet to spring mvc migration for a sample REST API end point to produce a "code example" for developers to follow. We have selected the rest/styles endpoint as one of the easier examples:



 	
  1. **Preflight check:** Before we start we want to have a good baseline of the current REST API responses. We would like to double check that each endpoint has a JUnit test case that checks the response against a reference file. Most of our tests just count the number of elements, or drill into the content to look for a specific value. _The goal is to use these reference files as a quick "regression test" when performing the migration._

 	
  2. **Migrate rest/styles from StyleResource (restlet) to StyleController (spring):** This should be a bit of fun, part of why spring model-view-controller was selected. Our goal is to have one Controller per end-point, and configure the controller using annotations directly in the Java file. This ends up being quite readable with variable names being taken directly out of the URL path. It is also easier to follow since you do not have to keep switching between XML and Java files to figure out what is going on.  _It is important that the example is "picture perfect" as it will be used as a template by the developers over the course of the sprint, and will be an example of the level of quality we expect during the activity.
[![code-example](http://blog.geoserver.org/wp-content/uploads/2017/03/code-example.png)](http://blog.geoserver.org/wp-content/uploads/2017/03/code-example.png)_

 	
  3. **Create StyleInfo bindings (using XStream for xml and json generation):** The above method returns a StyleInfo data structure, our current restlet solutions publishes each "resource" using the XStream library. We think we can adapt our XStream work for use in spring model-view-controller by configuring a binding for StyleInfo and implementing in using XStream.  _This approach is the key reason we are confident in this migration being a success; existing clients that depend on exactly the same output from GeoServer - should get exactly the same output.
_

 	
  4. **StyleController path management:** There is some work to configure each controller, while we have the option of doing some custom logic inside each controller we would like to keep this to a minimum.  _This step is the small bit of applicationContext.xml configuration work we need to do for each controller, we expect it to be less work then reslet given the use of annotations.
_

 	
  5. **Reference Documentation Generation:** We are looking into a tool called swagger for documentation generation. Our current reference documentation only lists each end-point (and does not provide information on the request and response expected - leaving users to read the examples or try out the api in an ad-hoc fashion). _See screen snap below, our initial experience is positive, but the amount of work required is intimidating._
[![swagger-editor](http://blog.geoserver.org/wp-content/uploads/2017/03/swagger-editor.png) ](http://blog.geoserver.org/wp-content/uploads/2017/03/swagger-editor.png)

 	
  6. **Updated examples for cURL and Python:** We would like to rewrite our examples in a more orderly fashion to make sure both XML and JSON sample requests and responses are provided. _Ideally we will inline the "reference files" from the JUnit regression test in step 1 to ensure that the documentation is both accurate and up to date._


You can see a pretty even split in our priorities between performing the migration, and updating the documentation. We believe both of these goals need to be met for success.


## Next stop Tuscany


Although this blog post focuses on the sponsorship/planning/logistics side of setting up a code sprint there is one group without whom this event could not happen - our sprint participants and in-kind sponsors (providing a venue & staff).

Thanks to [GeoSolutions](http://www.geo-solutions.it) for [hosting us](http://www.geo-solutions.it/blog/geoserver-code-sprint-2017/), and to [Astun](http://astuntechnology.com), [Boundless](http://boundlessgeo.com), [GeoSolutions](http://www.geo-solutions.it) for the hands-on participation that makes this sprint possible

For more information:



 	
  * [Java 2017 Code Sprint](https://wiki.osgeo.org/wiki/Java_2017_Code_Sprint) (OSGeo Wiki) used for planning and logistics

 	
  * [REST API Refresh](https://github.com/geoserver/geoserver/wiki/REST-API-Refresh) (GeoServer Wiki) code example and technical decisions


