---
author: Jody Garnett
layout: post
title: GeoServer 2024 Q4 Developer Update
date: 2024-10-04
categories:
- Behind The Scenes
---

The GeoServer team working on sharing our [roadmap plans]({% post_url 2024-01-03-roadmap %}) plans and providing greater transparency on our community participation and funding goals.

## GeoServer Developer Forum

If you have sent email to `geoserver-devel` list this week you have been met with the following reply:

```
This list is now closed, join us on geoserver developer forum:
https://discourse.osgeo.org/invites/7DX66egwux
```

That is right, developer communication has moved to [GeoServer Developer](https://discourse.osgeo.org/c/geoserver/developer/63) on discourse.

* To post join the [geoserver-developer](https://discourse.osgeo.org/t/welcome-to-osgeo/) group.
* [About the GeoServer Developer category ](https://discourse.osgeo.org/t/about-the-geoserver-developer-category/85608) has all the details (even email).
* There are [improved instructions](https://discourse.osgeo.org/t/welcome-to-osgeo/5#p-6-developer-github-login-2) on how to sign up using github.

How to help:

* Accept the [invite](https://discourse.osgeo.org/invites/7DX66egwux) - it is quick and easy joining the group and navigate to the forum in one go.
* Update communication details for [website](https://github.com/geoserver/geoserver.github.io/blob/main/devel/index.html) and [developer guide](https://github.com/geoserver/geoserver/blob/main/doc/en/developer/source/introduction.rst).

<img src="/img/posts/2.26/devel-forum.png" alt="Discourse Fourm" width="75%" height="75%">

## GeoServer 3 Crowdfunding

The consortium of Camptocamp, GeoSolutions and GeoCat have responded to our [roadmap challenge]({% post_url 2024-01-03-roadmap %}) with a bold [GeoServer 3 Call for Crowdfunding]( {% post_url 2024-09-10-gs3 %}) established as a multi-party contract.

* The fundraising target has now been set, see updated [post]( {% post_url 2024-09-10-gs3 %}), and [milestone deliverables](https://docs.google.com/document/d/1iCqob2R5Zcs9liODq2UGGiOUQhFWQJrjZCJxBVUP5Q4/edit?usp=sharing) established.
* [GSIP-226 - GeoServer 3](https://github.com/geoserver/geoserver/wiki/GSIP-226)

How to help:

* Share the [call for crowdfunding]( {% post_url 2024-09-10-gs3 %}) in your region.
* To express your interest or pledge support contact us directly at [gs3-funding@googlegroups.com](mailto:gs3-funding@googlegroups.com), or via [online form](https://forms.gle/EFML8NSJSCtzjWUY6).

<img src="/img/posts/2.26/gs3-crowdfunding-form.png" alt="Crowdfunding Form" width="50%" height="50%">

## Wicket 9 upgrade

[GEOS-11275](https://osgeo-org.atlassian.net/browse/GEOS-11275): Brad and David have made considerable progress on Wicket UI updates. After a [year of effort](https://github.com/geoserver/geoserver/pull/7154) the [first results](https://github.com/geoserver/geoserver/pull/7872) towards Wicket 10 are being merged onto the `main` branch.

Thanks to Brad for doing much of the difficult work starting this activity, and to David for working hard to stabilize this work for testing.

Peter and Jody started a wicket test plan and evaluated an initial [2.26-M0](https://github.com/geoserver/geoserver/releases/tag/2.26-M0) milestone release.

How to help:

* Test a [2.27.x](/release/2.27.x/) nightly build, clearly noting problems in the [Wicket Test Plan](https://docs.google.com/spreadsheets/d/1pQmncG4zxpgJnHxeI4myFfOBD17U2CIMcy59II4XAfo/edit?usp=sharing).
* Developer assistance is needed to resolve the content-security-policy warnings reported during testing
* David has outlined what is needed for a [new GSModalDialog](https://github.com/geoserver/geoserver/pull/7871) to replace the functionality being removed in Wicket 10.

```
docker pull docker.osgeo.org/geoserver:2.27.x
docker run -it -p8081:8080 docker.osgeo.org/geoserver:2.27.x
```

## Spring Security 5.8 update

[GEOS-11271](https://osgeo-org.atlassian.net/browse/GEOS-11271): Andreas Watermeyer (ITS Digital Solutions) has completed this activity ahead of the GeoServer 2.26.0 release.

How to help:

* The next step is going through the [Preparing for 6.0](https://docs.spring.io/spring-security/reference/5.8/migration/index.html) checklist

## Spring Security OAuth2 replacement

[GEOS-11272](https://osgeo-org.atlassian.net/browse/GEOS-11272): Andreas Watermeyer (ITS Digital Solutions) set up new community modules to work on this activity. This is a new implementation as the spring security internals have changed, and the new spring api allows for a cleaner implementation.

How to help:

* This work will require extensive testing in different environments.
* Ideas on unit testing and increasing test coverage with test containers are very welcome.


## Support and sponsorship

We would like to welcome a new project sponsor:

> [Route4Me](https://route4me.com/) - Simplify Last Mile Complexity: proven route planning and route optimization software.
>
> ![Route4Me](/sponsor/img/route4me-logo.svg)

The GeoServer project steering committee seeks sponsorship to fund maintenance activities, code sprints, and research and development that is beyond the reach of an individual contributor or organization.

* We have worked with OSGeo to provide [sponsorship guidance](https://www.osgeo.org/about/how-to-become-a-sponsor/) for individual consultants, small organisation, companies and public institutions of different sizes.
* GeoServer has a new [sponsorship page](/sponsor/) on our website collecting this information for our project.
* GeoServer now lists sponsors logos on our [home page](/), alongside core contributors.

We would like to thank everyone who has responded thus far:

* Sponsors: [How 2 Map](https://www.how2map.com/), [illustreets](https://illustreets.com/), and [Route4Me](https://route4me.com/).
* Individual Donations: Peter Rushforth, Marco Lucarelli, Gabriel Roldan, Jody Garnett, Manuel Timita, Andrea Aime
