---
author: Jody Garnett
layout: post
title: GeoServer 2025 Q4 Developer Update
date: 2025-10-14
categories:
- Behind The Scenes
---

The GeoServer team is making great progress on our [2025 roadmap plans]({% post_url 2025-01-13-roadmap %}), with [CITE Certification Achieved]({% post_url 2025-07-16-cite-certification %}), and [GeoServer 3](/sponsor/gs3-crowdfunding/) underway, the project is going well.

{% include 2025-sponsors.html %}

## Security 

We have added a "disclosure" field to our issue tracker to better schedule communication around security vulnerability resolution. To allow everyone time to upgrade, disclosure is scheduled some time after an issue is both fixed and available in stable and maintenance release streams. Managing this communication has proven difficult during the release process.

Thanks to Jody, Andrea and Peter for working with the issue tracker, security procedure, and updating the script used to generate release blog posts.

We continue to be in need of resources, both developer resources and funding, to address the expectations placed on open source projects. If you are in a position to support this activity, please contact us at [geoserver-security@lists.osgeo.org ](geoserver-security@lists.osgeo.org).

## GeoServer 3

The big news is the completion of **Milestone 1 : Preparation** with the release of GeoServer 2.28.0, allowing the **Milestone 2 : Migration** activities to proceed as scheduled. 

For more information on GeoServer 3 development, review the [project plan](https://docs.google.com/document/d/1iCqob2R5Zcs9liODq2UGGiOUQhFWQJrjZCJxBVUP5Q4/edit?usp=sharing) and [GeoServer 3 Crowdfunding](https://geoserver.org/sponsor/gs3-crowdfunding) FAQ.

### GeoServer 3 Milestone 1 Completed

The release of GeoServer 2.28.0 represents the end of **Milestone 1: Preparation**:

* Upgrade from Java Advanced Imaging 1.1.3 to Eclipse ImageN 0.9.0.
  
* Java 17 LTS minimum, ending support for Java 11.

* Lots of build improvements, with the highlight being a **bill-of-materials** "geotools" ``pom.xml`` file to manage versions across GeoTools, GeoWebCache, and GeoServer.

* A new community module, **gs-sec-oidc-plugin**, replacing **gs-oauth2** plugins.

### GeoServer 3 Milestone 2 Underway

GeoServer 3 Milestone 2: Migration is underway:

* Friday 17 October: Code Freeze
 
  We will be freezing the main branches of the related projects on Friday 17 Oct 2025, in preparation for the Milestone 2 code sprint.  Please follow the [announcement](https://discourse.osgeo.org/t/main-branch-freeze-on-friday-17th/150074) on Discourse.
  
* Monday 20 October: Code Sprint
  
  With the branches frozen, the GeoServer 3 team is assembling for an intensive code sprint to start the migration to Spring Framework 3.

<img src="/img/posts/2.26/gs-milestones.svg" alt="GeoServer 3 Milestones" style="display:block; margin-left:auto; margin-right:auto; width:100%;"/>

### Crowdfunding

Thanks to sponsors for supporting [GeoServer 3 crowdfunding](/sponsor/gs3-crowdfunding), we hope you are pleased with the progress thus far and look forward to sharing GeoServer 3 with you in the months ahead.

{% include gs3-sponsors.html %}

