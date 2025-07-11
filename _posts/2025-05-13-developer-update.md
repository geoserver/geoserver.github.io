---
author: Jody Garnett
layout: post
title: GeoServer 2025 Q2 Developer Update
date: 2025-05-13
categories:
- Behind The Scenes
---

The GeoServer team is charging ahead with our [2025 roadmap plans]({% post_url 2025-01-13-roadmap %}).

{% include 2025-sponsors.html %}

## CITE Certification

A great deal of progress has been made on CITE Certification with the most recent [GeoServer 2.27.0 Release]({% post_url 2025-04-03-geoserver-2-27-0-released %}) passing tests! This is great for interoperability and project stability as the CITE tests act as an external "blackbox" testing framework and this verifies that GeoServer is operating as intended. 

We are presently determining how to pay for certification:

* The Open Source Geospatial Foundation has negotiated a reduced rate of $150 annual cost per standard certified.
* We are prioritizing tests where we can act as a "reference implementation" resulting in no annual cost for OSGeo.
* For Web Feature Service we pass tests for WFS 2.0, WFS 1.1, and WFS 1.0 which would add up to $450. It may be worthwhile only being certified for the latest WFS 2.0 to reduce the costs to $150.
* There are also now CITE tests for output formats. This would allow the WFS and WPS output to be certified on individual formats like GeoPackage and GeoTIFF.

While GeoServer presently "implements" these standards, our sponsorship level is not sufficient to allow us to feel comfortable paying annual costs for "certification".

Full certification amounts to $900 a year, while certifying only the latest services amounts to $450 a year.

| OGC Standard |  | Full Certification |  | Latest Services  |
| ------------ | -----: | ------ | -----: | ------ | 
| *Services* | | |
| OGC API - Features | $150 | Certified | $150 | Certified |
| WCS 2.0.1 | $0 | Reference | $0 | Reference |
| WCS 1.1.1 | $0 | Reference | $0 | Reference |
| WCS 1.0 | $0 | Reference | $0 | Reference |
| WFS 2.0 | $150 | Certified | $150 | Certified |
| WFS 1.1.0 | $150 | Certified | $0 | Implements |
| WFS 1.0.0 | $0 | Reference | $0 | Reference |
| WMS 1.3.0 | $150 | Certified | $150 | Certified |
| WMS 1.1.1 | $150 | Certified | $0 | Implements |
| WMTS 1.0.0 | $0 | Reference | $0 | Reference |
| *Data formats and encodings* | | |
| GeoTIFF 1.1 | $150 | Certified |$0 | Implements |
| GeoPackage 1.2 | $150 | Certified | $0 | Implements |
| | |

*How you can help*: We would really like confirmation that certification is valuable to the community. If you think it is valuable, please let us know in the [Discourse forum](https://geoserver.org/comm/#discourse) or, even better, if you are interested in sponsoring part of the certification, please do speak up!  If we do not hear from anyone, we might not pursue formal certification any further.

Many thanks to prior sponsors of [this activity]({% post_url 2019-11-14-cite-test-automation-request-for-proposal %}) including
[Gaia3D](https://gaia3d.com), and [OSGeo:UK](https://uk.osgeo.org).


## GeoServer 3

The big news is that GeoServer 3 crowdfunding campaign phase one has been successful, allowing the [project plan milestones](https://docs.google.com/document/d/1EmI1kDsqeoxB9GANiiaZy56RY0pWbl6GqD4fq8EJ4oo/edit?tab=t.0#heading=h.u9va0zovek8y) to be scheduled.

We are working around the GeoServer release schedule to avoid disruption to the project:

* **Milestone 1 : Preparation** (May-September)  
  Doing everything possible ahead of time before the migration to spring-framework-6.
  
  Milestone 1 is already in progress, see the headings below for specific activities. 
  
  Milestone 1 activities will be taking place on the ``main`` branch ahead of the GeoServer 2.28 release.
  As tasks are completed, your feedback and continuous testing of nightly builds will be highly appreciated.  **Please [chat to us](https://geoserver.org/comm/#discourse) about how you can automate the testing in your non-production environments.**
  
* **Milestone 2 : Migration** (October-December)  
  Requires a coordinated "code-freeze" across nine codebases migrating to spring-framework-6. 

  This activity is going to take careful planning, and we anticipate scheduling an in-person sprint for the migration.
  
  While initial work may occur on a ``dev`` branch, GeoServer 3 will take over the ``main`` branch after the September release of GeoServer 2.28.0.

* **Milestone 3: Delivery** (January-March)  
  The moment we have the code-base working again, Milestone 3 activities include continuing the testing of nightly builds, checking integration with downstream applications, and feedback from anyone wishing to work on restoring a community module to GeoServer 3.
  
  This pace allows GeoServer 3.0 to be ready in 2026 Q1, respecting our normal time-boxed [release cycle](https://geoserver.org/roadmap/).

<img src="/img/posts/2.26/gs-milestones.svg" alt="GeoServer 3 Milestones" style="display:block; margin-left:auto; margin-right:auto; width:100%;"/>

### Milestone 1

Checking in on Milestone 1 activities, there is lots of work to be done!

#### Spring Framework Preparation, Java 17, and Project and Build Support

To get the codebase ready for widespread change, Gabriel will be looking at setting up a GeoTools "bill of materials" ``pom.xml`` file providing GeoServer and other applications an easy way to manage the currently tested set of dependencies.

* Updating to Java 17 is a key requirement for Spring Framework 6 and JakartaEE so expect many of these dependencies to be updated or replaced over the course of GeoServer 2.28 development. 
* Spring Framework 6 also removes a lot of deprecated APIs and dependencies, providing work to do for GeoWebCache and GeoServer codebases

#### ImageN and JAI-Ext Online Sprint (May 26-27)

The biggest GeoServer 3 Milestone 1 activity is restarting the ImageN project and combining forces with JAI-Ext for a new image processing engine:

* ImageN represents the Oracle donation of the original Java Advanced Imaging codebase to the Eclipse Foundation (using a new name that does not contain "Java").
* The [ImageN project](https://projects.eclipse.org/projects/technology.imagen) is being restarted, with Andrea and Daniele being recently added to the project.
* Project [website](https://projects.eclipse.org/projects/technology.imagen) has been updated with a slightly revised scope to reflect the addition of the JAI-Ext codebase.
* We will be cutting some unused functionality, such as RMI, and restructuring the maven build to reflect some of the lessons learned with JAI-Ext and GeoTools build practices.
* Andrea has a [rough project plan](https://github.com/aaime/imagen/wiki/JAI%E2%80%90Ext-GeoTools-GeoWebCache-GeoServer,-migration-to-ImageN) which we will capture as a [project board](https://github.com/orgs/eclipse-imagen/projects/1) in the weeks ahead.
* Communication is taking place over on the [imagen-dev](https://accounts.eclipse.org/mailing-list/imagen-dev) mailing list.

Andrea and Jody are organizing an ImageN Online Sprint for May 26-27 where the bulk of the work will take place. We plan to follow the same approach as the OpenGIS Harmonization activity where refactor scripts are produced, and tested on the GeoTools / GeoWebCache / GeoServer codebases during development.

#### Spring Security and OAuth2 / OIDC Security Modules

The next technical challenge is the work needed to update to the next version (6) of the Spring Security Framework. There have been considerable API changes, resulting in the need to completely replace the existing OAuth2 and OIDC community modules. Our existing community modules are based on the deprecated spring-security-oauth library which has now reached end of life. The Spring Security Core library now has OAuth2 support, necessitating a new GeoServer extension that makes direct use of the built-in OAuth2 support.

Andreas Watermeyer (ITS Digital Solutions) has working on these activities:

* GeoServer 2.27.0 includes the upgrade to Spring Security 5.8, and there is a checklist to complete before upgrading further to version 6.
* Andreas has a draft [pull request](https://github.com/geoserver/geoserver/pull/7968) re-implementing the OAuth2 security modules, which we are looking forward to incorporating, and we plan to port all the test cases over to ensure that it covers the same functionality.

Ideally GeoServer 2.28.0 will include both the old and the new Spring Security OAuth2 community modules, allowing everyone to upgrade easily and report back any regressions found.

#### Wicket

A big accomplishment in the recent [GeoServer 2.27.0 Release]({% post_url 2025-04-03-geoserver-2-27-0-released %}) is progress towards Wicket 10 by Brad and David:

* Wicket 9
* Wicket Dialog
* Wicket Content Security Policy

There are a few remaining [items to work on](https://cwiki.apache.org/confluence/display/WICKET/Migration+to+Wicket+10.0), such as the Java 17 build, before upgrading to [Wicket 10](https://wicket.apache.org/start/wicket-10.x.html).

It is great that we have already tackled many of the technical challenges above, and have received positive responses from GeoServer 2.27.0 testers.

#### Crowdfunding

[GeoServer 3 crowdfunding](/sponsor/gs3-crowdfunding) has completed the *Commitment Phase* - thank you for your trust and support.  We are now contacting supporters to engage with them further.

{% include gs3-sponsors.html %}

