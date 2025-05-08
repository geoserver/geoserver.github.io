---
author: Jody Garnett
layout: post
title: GeoServer 2025 Q2 Developer Update
date: 2025-05-13
categories:
- Behind The Scenes
---

The GeoServer team charging ahead with our [2025 roadmap plans]({% post_url 2025-01-13-roadmap %}).

## GeoServer 3 Milestone 1 Preparation

The big news is that GeoServer 3 crowdfunding campaign phase one has been successful, allowing the [project activities](https://docs.google.com/document/d/1EmI1kDsqeoxB9GANiiaZy56RY0pWbl6GqD4fq8EJ4oo/edit?tab=t.0#heading=h.u9va0zovek8y) to be scheduled.

* **Milestone 1 : Preparation** (May-July)  
  Doing everything possible ahead of time before the migration to spring-framework-6.
  
  Milestone 1 is already in progress, see headings below for specific activities. 
  
  Milestone 1 activities will be taking place on the ``main`` branch ahead of the GeoServer 2.28 release.
  As tasks are completed feedback and testing of nightly builds is appreciated.
  
* **Milestone 2 : Migration** (August-October)  
  Requires a coordinated "code-freeze" across nine codebases migrating to spring-framework-6. 

  This activity is going to take careful planning, and we anticipate scheduling an in-person sprint for migration.
  
  While initial work may occur on a `dev` branch, GeoServer 3 will take over the `main` branch after the September release of GeoServer 2.28.0.

* **Milestone 3: Delivery** (November - December)  
  The moment we have the code-base working again Milestone 3 can start welcoming testing of nightly builds, checking integration with downstream applications, and anyone wishing to work on a community module.
  
  Ideally we would like to have GeoServer 3 available by year end.

<img src="/img/posts/2.26/gs-milestones.svg" alt="GeoServer 3 Milestones" style="display:block; margin-left:auto; margin-right:auto; width:100%;"/>

## CITE Certification

A great deal of progress has been made on CITE Certification with the most recent [GeoServer 2.27.0 Release]({% post_url 2025-04-03-geoserver-2-27-0-released %}) passing tests! This is great for interoperability and project stability as the CITE tests act as external "blackbox" testing framework and verifies that GeoServer is operating as intended. 

We are presently determining how to pay for certification:

* OSGeo has negotiated a reduced rate of $150 annual cost per test.
* We are prioritizing tests where we can act as a "reference implementation" (so no annual cost)

While GeoServer presently "implements" these standards, our sponsorship level is not sufficient to allow us to feel comfortable paying an annual costs of between $450 and $900 for certification each year.

**Is our community interested in sponsoring CITE certification?**

We would like confirmation that certification is valuable to the community. If you think it is valuable please let us know, or if you are interesting in sponsoring certification please speak up!

Many thanks to prior sponsors of [this activity]({% post_url 2019-11-14-cite-test-automation-request-for-proposal %}) including
[Gaia3D](https://gaia3d.com), and [OSGeo:UK](https://uk.osgeo.org).

## ImageN Online Sprint (May 26-27)

The biggest GeoServer 3 Milestone 1 activity is restarting the ImageN project and combining forces with JAI-Ext for a new image processing engine.

* ImageN represents the Oracle donation of the original Java Advanced Imaging codebase to the Eclipse Foundation (using a new name that does not contain "Java").
* The [ImageN project](https://projects.eclipse.org/projects/technology.imagen) is being restarted, with Andrea and Daniele being recenlty added to the project.
* Project [website](https://projects.eclipse.org/projects/technology.imagen) has been updated with a slightly revised scope to reflect addition of the JAI-Ext codebase
* We will be cutting some unused functionality, such as RMI, and restructuring the the maven build to reflect some of the lessons learned with JAI-Ext and GeoTools build practicies.
* Andrea has a rough project plan [here](https://github.com/aaime/imagen/wiki/JAI%E2%80%90Ext-GeoTools-GeoWebCache-GeoServer,-migration-to-ImageN) which we will capture as a project board in the weeks ahead.

## Wicket 10 Prep

A big accomplisment in the recent [GeoServer 2.27.0 Release]({% post_url 2025-04-03-geoserver-2-27-0-released %}) is progress made towards getting ready for Wicket 10.

* Wicket 9
* Wicket Dialog
* Wicket Content Security Policy

There is not much more we can [work on](https://cwiki.apache.org/confluence/display/WICKET/Migration+to+Wicket+10.0) before upgrading to [Wicket 10](https://wicket.apache.org/start/wicket-10.x.html) which needs to wait for Milestone 2.

It is great we have tackled many of the technical challenges above, and have received positive response from GeoServer 2.27.0 testers.