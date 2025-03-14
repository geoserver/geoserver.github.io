---
author: Jody Garnett
layout: post
title: GeoServer 2024 Q3 Developer Update
date: 2024-07-22
categories:
- Behind The Scenes
---

This is a follow up to [2024 roadmap]({% post_url 2024-01-03-roadmap %}) post outlining development opportunities.

First of all thanks to developers and organisations that have responded with offers of in-kind contributions. This blog post is assessing current progress and outlines a way forward to complete the Java 17/Jakarta EE/Spring 6 upgrades.

This post highlights development activities that are **available to be worked on today**, along with interested [developers](https://github.com/geoserver/geoserver/graphs/contributors) and commercial [support providers](/support) available to work on GeoServer roadmap items.

## Spring Framework 6 Tasks

The key challenge we are building towards is a spring-framework 6 update, ideally by the end of 2024 when the version we use now reaches end-of-life.

The tasks below are steps towards this goal.

### Wicket 9 upgrade

Interested Parties:

* Brad has been doing amazing work with the Wicket 9 upgrade and is in need of assistance.
* GeoCat has offered to do manual A/B testing when PR is ready for testing.

Activity:

* [[GEOS-11275]](https://osgeo-org.atlassian.net/browse/GEOS-11275) Wicket 9 upgrade
* [geoserver#7154](https://github.com/geoserver/geoserver/pull/7154)

### Spring Security 5.8 update

Spring Security 5.8 provides a safe stepping stone ahead of the complete spring-framework 6 upgrade and is an activity that can be worked on immediately. 

Interested parties:

- Andreas Watermeyer (ITS Digital Solutions) offered to work on this activity in during the initial January call out, and has indicated they are now ready to start.

Activity:

* [[GEOS-11271]](https://osgeo-org.atlassian.net/browse/GEOS-11271) Upgrade spring-security to 5.8

### Spring Security Core implementation of OAuth2 / OIDC

The spring-security-oauth client has reached end-of-life and a GeoServer OAuth2 support must be rewritten or migrated as a result.

There are two paths to migrate to spring-security-core implementation:

* Option: Migrate the existing community module implementations to spring-security-core in place; with as little loss of functionality as possible. This has the advantage of using existing test coverage to maintain a consistent set of functionality during migration.

* Option: Setup a community module alongside the existing implementation with the goal of making a full supported etension. This approach has the advantages of allowing organisations the ability to do A/B testing as both the old and new implementation would be available alongside each other. This has the advantage of allowing stakeholders to only fund, implement, test functionality as required without disrupting existing use.

Security integrations often require infrastructure to develop and test against, which the core GeoServer team does not have access to for automated tests. We would like to see organisations review their security integration requirements and be on hand to support this development activity.

The initial priority will support for OAuth2 and Open ID Connect (OIDC), parties interested in maintaining support for Google, GeoNode, GitHub are welcome to participate.

Interested Parties:

- Andreas Watermeyer (ITS Digital Solutions) offered to work on this activity, or test as needed.
- GeoCat is interested in this work also, with the goal of bringing the OIDC plugin up to full extension status (if financing is available).

Activity: not started

* [[GEOS-11272]](https://osgeo-org.atlassian.net/browse/GEOS-11272) spring-security-oauth replacement, with spring-security 5.8

### ImageN / JAI Replacement

The image processing library used by GeoServer has been donated to the open source community under the name [ImageN](https://projects.eclipse.org/projects/technology.imagen).

The immediate goal has been to add test cases to this codebase and make an ImageN 1.0 release. Andrea has come up with the *amazing idea* of integrating with JAI-Ext project immediately, to benefit from the improved operators, and jumpstart test coverage.

Interested Parties: 

* Jody (GeoCat) is available to support this activity, or take lead if funding is available.
* Andrea (GeoSolutions) has had a deep dive into the implications for the JAI-EXT project outlining a roadmap for project integration

We would like to see organisations that depend on GeoServer for earth observation and imagery to step forward with funding for this activity.

## 2024 Financial support and sponsorship

Thus far 2024 has not had a strong enough sponsorship response to support the project goals above. As a point of comparison we established a budget of $15,000 with OSGeo last year to take on an [low-level API change](https://www.osgeo.org/opengis-harmonization/) that affected several projects.

This year GeoServer sponsorship has raised between $1,000 and $2,000 which is not enough to plan with or coordinate in-kind contributions offered thus far.

Jody has worked with the OSGeo board to make adjustments to the [sponsorship](https://www.osgeo.org/about/how-to-become-a-sponsor/):

* Guidance has been provided for appropriate sponsorship levels for individual consultants, small organisation, companies and public institutions of different sizes.
* There are clear examples of how to sponsor and donate, along with the the perks and publicity associated with financial support
* GeoServer has a new [sponsorship page](/sponsor/) on our website collecting this information
* GeoServer now lists sponsors logos on our [home page](/), alongside core contributors.

We would like to thank everyone who has responded thus far:

* Sponsors: [How 2 Map](https://www.how2map.com/), [illustreets](https://illustreets.com/)
* Individual Donations: Peter Rushforth, Marco Lucarelli, Gabriel Roldan, Jody Garnett, Manuel Timita, Andrea Aime
