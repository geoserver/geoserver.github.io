---
author: Emmanuel Belo
layout: post
title: GeoServer 3.0-RC, a crowdfunded success story
date: 2026-04-21
categories:
- Behind The Scenes
tags:
- GeoServer 3
- Crowdfunding
- Community
- Release Candidate
---

GeoServer [3.0-RC](/release/3.0-RC/) is now available, and with it we can celebrate something bigger than a release candidate.

This milestone is the concrete outcome of a successful community crowdfunding campaign.

When we launched the [GeoServer 3 crowdfunding initiative](/sponsor/gs3-crowdfunding) in September 2024, the goal was ambitious. GeoServer needed more than incremental maintenance. It needed a full platform modernization, including a new generation user experience, a stronger security foundation, a modern Java stack, improved raster processing, and the engineering effort required to carry those changes across the broader GeoServer ecosystem.

That work is now visible in GeoServer 3.0-RC.

## From campaign to release candidate

The GeoServer 3 crowdfunding effort set a total target of **550,000 €**. Camptocamp, GeoCat, and GeoSolutions each committed **50,000 €**, establishing a community funding goal of **400,000 €**. In May 2025, the campaign [surpassed that goal]({% post_url 2025-05-13-gs3-crowdfunding-surpassed %}).

That achievement mattered because GeoServer 3 was never a small upgrade. It required coordinated investment in core platform work that is essential for users, but often difficult to fund through routine maintenance alone:

* migration to a modern Spring and Jakarta based platform
* alignment with JDK 17 and current deployment environments
* replacement of aging raster processing components with ImageN
* stronger security and vulnerability management
* documentation updates and broad compatibility testing
* user interface and usability improvements across the administration experience

The consortium of Camptocamp, GeoCat, and GeoSolutions provided coordination, delivery capacity, and co-funding. Sponsors, community members, and individual donors made it possible to move from planning into implementation.

## What GeoServer 3.0-RC shows

With GeoServer 3.0-RC, the results of that investment are now ready for public testing.

This release candidate introduces a modernized platform with:

* a new context-driven user experience
* a responsive administration interface
* a new full-screen layer preview
* updated documentation in Markdown
* support for modern servlet containers including Tomcat 11 and Jetty 12.1
* a straightforward upgrade path from GeoServer 2.28.x, with no changes to the GeoServer data directory

GeoServer 3.0-RC is also released together with **GeoTools 35-RC** and **GeoWebCache 2.0-RC**, making this an important ecosystem milestone, not just a version bump.

<a href="/img/posts/3.0/welcome-global.png" target="_blank" rel="noopener">
  <img src="/img/posts/3.0/welcome-global.png" alt="GeoServer 3" class="screensnap"
     style="max-width: 95%"/>
</a>

## Why this matters for open source sustainability

Crowdfunding is often discussed in theory as a way to support open source. GeoServer 3 offers a practical example of what that support can achieve.

This campaign did not fund a narrow feature request. It funded the kind of foundational work that keeps a critical open source project healthy: technical modernization, security upgrades, ecosystem testing, documentation improvements, and long-term maintainability.

That is exactly the kind of work communities depend on, and exactly the kind of work that is hardest to finance unless users and organizations step forward together.

GeoServer 3.0-RC proves that this model can work.

## Help us finish strong

The arrival of GeoServer 3.0-RC is also a call for community testing.

We encourage everyone to try the release candidate in their own environment, especially for:

* upgrade workflows from GeoServer 2.28.x
* the new user interface and administration workflows
* deployments on Tomcat 11 and Jetty 12
* raster-heavy and tiling-heavy workloads
* extension compatibility and operational edge cases

You can download GeoServer 3.0-RC from the [release page](/release/3.0-RC/), review the [upgrade instructions](https://docs.geoserver.org/latest/en/user/installation/upgrade3/), or quickly test the Docker image:

```bash
docker run -p 8080:8080 docker.osgeo.org/geoserver:3.0-RC
```

Please share your feedback on the [GeoServer 3.0-RC discourse thread](https://discourse.osgeo.org/t/geoserver-3-0-rc-release-candidate/153541).

<a href="/img/posts/3.0/ol-preview.png" target="_blank" rel="noopener">
  <img src="/img/posts/3.0/ol-preview.png" alt="New full screen layer preview" class="screensnap"/>
</a>

## Thank you

GeoServer 3.0-RC is an important technical milestone, but it is also a community milestone.

Thank you to the organisations, individual donors, developers, testers, and sponsors who helped make this happen. And thank you to the consortium teams at Camptocamp, GeoCat, and GeoSolutions for carrying the work from campaign to release candidate.

GeoServer 3.0-RC is here because the community decided this work was worth funding.

That is worth celebrating.

{% include gs3-sponsors.html %}
