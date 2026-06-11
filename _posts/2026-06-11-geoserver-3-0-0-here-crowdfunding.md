---
author: Nuno Oliveira
layout: post
title: GeoServer 3 is here, from crowdfunding to release
date: 2026-06-11
categories:
- Behind The Scenes
tags:
- GeoServer 3
- Crowdfunding
- Community
- Release
---

[GeoServer 3.0 is now generally available]({% post_url 2026-06-11-geoserver-3-0-0-released %}). This post is not a feature announcement, those have been written, and the release notes cover the details. This is something we get to do less often: closing the loop on a promise. The modernisation work the community funded is finished and shipping, and we want to account for what that funding set out to achieve and what it delivered.

The result is a platform brought back onto a current, supported foundation. The work reached across the wider ecosystem rather than GeoServer alone, and the scope the campaign promised has been covered.

## **The bet the community made**

The case for GeoServer 3 was clear. Spring 5 was reaching the end of security support, and staying on a supported, modern Java platform meant moving to JDK 17\. That upgrade was the trigger for much of what followed, because it could not happen in isolation: it cascaded into Spring 7, Jakarta, modern servlet containers, and updated libraries across the stack, and the ageing image-processing components had to be replaced along the way. None of this is the kind of work that wins a feature vote, yet all of it keeps GeoServer current and dependable for the years ahead. Our goal was to take this foundational work directly, in one coordinated effort across the whole ecosystem, rather than letting it pile up.

Funding it required a structure built on trust. [The financial target was 550,000 €](https://geoserver.org/sponsor/gs3-crowdfunding). Camptocamp, GeoCat, and GeoSolutions each contributed 50,000 €, and the consortium provided coordination, delivery capacity, and co-funding to move the project forward. That left a community funding goal of 400,000 €, pledged by sponsors, community members, and individual donors during a commitment phase, with funds collected only once the target was reached, so the work could begin fully funded rather than at risk of stalling partway. In May 2025 the [campaign passed its goal](https://geoserver.org/behind%20the%20scenes/2025/05/13/gs3-crowdfunding-surpassed.html), and the work began fully funded. GeoServer 3.0 is the moment it pays out.

## **What the funding delivered**

GeoServer 3 set out to modernise the platform from the foundation up, and that is what this release delivers. The work was a coordinated programme rather than a single change, where a handful of major upgrades each set off a chain of smaller, necessary changes across the codebase. The items below are the headline changes that triggered much of the surrounding effort.

**A modern Java foundation.** The GeoServer ecosystem now runs on JDK 17 and Spring 7, the central upgrade that drove the rest of the work and brings GeoServer back onto a current, supported stack. That move cascaded into Jakarta, modern servlet containers, and a wide set of supporting libraries that all had to be carried forward together. The project worked through the dependency tree end to end, so the platform sits on a clean, maintainable base.

**Modern raster processing.** ImageN has replaced the legacy image-processing engine, putting raster processing on a modern foundation that is far easier to maintain going forward.

**Reinforced security.** Security and vulnerability management have been strengthened throughout, putting GeoServer on a stronger footing for the kinds of compliance and assurance its users increasingly need.

**A refreshed administration experience and documentation.** The administration interface has been rebuilt with a new context-driven design, and the documentation has been refreshed and updated alongside it.

Just as importantly, this was never only about GeoServer. The funded work carried across the ecosystem, and 3.0 ships together with GeoTools and GeoWebCache, with the integration work for GeoServer Cloud following on, making GeoServer well suited to cloud-native and containerised deployments. For most deployments the upgrade from 2.28.x is straightforward, with no changes required to the data directory. The migration guide provides the necessary instructions for the rest. The release candidate phase let organisations prove all of this in their own environments, and that feedback shaped the final release.

All of this scope was delivered and is available now in the GeoServer 3.0 release.

## **Thank you**

GeoServer is critical infrastructure for countless organisations, and keeping a platform like that healthy depends on funding the unglamorous foundational work that rarely attracts attention on its own. That a community came together to back this effort, and saw it through to a successful delivery, is a meaningful example of how open source can sustain itself when its users choose to invest in it.

That investment had a lot of people behind it. Thank you to every organisation that pledged, every individual who donated, and everyone who tested, reported, reviewed, and contributed code: this release exists because you decided it should. Thank you also to the consortium teams at Camptocamp, GeoCat, and GeoSolutions, who carried it from a funding target to a shipped release.

GeoServer 3 is the foundation for everything the project does next. It is here because the community built it together.

{% include gs3-sponsors.html %}