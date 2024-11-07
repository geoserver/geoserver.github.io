---
layout: default
title: GeoServer 3 Crowdfunding
---

# GeoServer 3 Crowdfunding

GeoServer is at a critical turning point and it needs your help to continue its journey as the leading free and open-source platform for geospatial data. With **GeoServer 3** we are transforming the way you interact with geospatial data—making it faster, more intuitive, and more secure.

<img src="/img/posts/2.26/gs3-crowdfunding.png" alt="GeoServer 3 Crowdfunding" style="display:block; margin-left:auto; margin-right:auto; width:30%;"/>

This major upgrade, led by Camptocamp, GeoSolutions, and GeoCat, will deliver:

* **Future-Proof Performance**: A modernized core for compatibility with the latest data management and deployment technologies.

* **Enhanced Image Processing**: Faster, smoother handling of spatial imagery and larger datasets.

* **Improved Security and Compliance**: Meet regulatory standards and protect your data with the latest security enhancements.

* **Streamlined User Experience**: Easier navigation, integrating new services, and empowering users at all levels.

The scope of this work is beyond routine updates or maintenance since the transition to GeoServer 3 requires extensive redevelopment of core systems as well as implementing **modern security practices** and also thorough **testing and validation** across all GeoServer extensions.

The consortium members - **Camptocamp**, **GeoSolutions**, and **GeoCat**- have a long-standing history of supporting and contributing to GeoServer and are fully committed to the success of this migration. However, this is a major effort that cannot be completed without community support.

By supporting this crowdfunding campaign, you are investing in the future of GeoServer and helping to sustain the innovative, open-source geospatial community.

### Why GeoServer 3

As the digital landscape evolves, staying up-to-date with the latest technology is no longer optional — **it’s essential**. GeoServer 3 is being developed to address crucial challenges and ensure that GeoServer remains a reliable and secure platform for the future. Several key factors make this upgrade critical right now:

* **Regulatory Compliance**: New regulations, including the CISA known exploited vulnerabilities list, demand that systems be fully patched to ensure operational readiness. Without the latest updates, GeoServer risks falling short of these standards, which is why migrating to Spring 6 is essential.

* **End of Support for Spring 5**: By January 2025, Spring 5 will no longer receive security updates, leaving systems vulnerable. As GeoServer operates as middleware between web services and essential data layers, this upgrade to Spring 6 is crucial to maintaining secure connections and protecting data from potential breaches.

* **Security Enhancements**: Upgrading to Spring 6 enables OAuth2 protocols for secure authentication, especially critical for large-scale or enterprise-level use. These advancements will help organizations meet evolving security requirements and protect sensitive geospatial data.

* **Switching to JDK 17**: This upgrade also marks GeoServer’s transition to JDK 17, which brings improvements in performance, security, and long-term support. Keeping GeoServer aligned with the latest Java versions ensures compatibility with modern deployment technologies Tomcat 10 and Jakarta and future-proofs the platform.

* **Improved Image Processing**: GeoServer 3 will replace the outdated Java Advanced Imaging (JAI) library with the more modern and flexible ImageN toolkit. This switch will significantly enhance image processing capabilities, enabling faster handling of large spatial datasets and improving Java compatibility.

* **Future-Proof Technology Stack**: With the migration to Spring 6 and the shift to JDK 17, GeoServer 3 ensures long-term viability. Addressing the entire GeoServer stack, including enterprise components GeoFence and Cloud Native GeoServer, allows organizations to seamlessly adopt modern infrastructure and deployment models without compromising performance or security.

With this work, GeoServer is moving into a more secure, high-performing future—ready to tackle the evolving needs of the geospatial community. For more information on the work to be performed and its phases, please visit [this](https://docs.google.com/document/d/1iCqob2R5Zcs9liODq2UGGiOUQhFWQJrjZCJxBVUP5Q4/edit?usp=sharing) document.

### Crowdfunding structure

The crowdfunding will be structured in **two phases** to ensure success:

1. **Commitment Phase**: Sponsors and community members will pledge their financial support during this phase, but no funds will be collected. The goal is to reach a **predefined target** that covers the full scope of work necessary for the migration.

2. **Funding Activation**: Once the target is reached, the crowdfunding will be activated, and sponsors will be invoiced for their pledged amounts. This ensures there is enough financial backing to complete the migration without risking underfunding.

This structured approach ensures that GeoServer 3 is fully funded before any work begins, preventing the risk of an incomplete migration. This guarantees that the project will have the necessary resources to be completed in its entirety.

This structure forms a multi-party agreement:

* **Consortium**: Three companies are forming a consortium (Camptocamp, GeoSolutions, and GeoCat) providing expertise, a proven track record, and capacity. These companies are also taking on responsibility for project management, estimating, and importantly risk.

* **Supporters**: We are seeking organisations to pledge their support via funding during the commitment phase. No funds will be collected until we reach the target established below for the full scope of work necessary.

* **Community**: We ask that our community step forward to match the contributions above with both financial contributions and in-kind development and testing.

### Crowdfunding target

The financial target is ambitious, 550,000.00 €. CamptoCamp, GeoCat and GeoSolutions have generously stepped up and will provide 50,000.00€ each, **which means the current funding goal starts at 400,000.00 €**.  Here below you will find the live updated situation as far as committed funding is concerned.

<iframe width="365" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRDiW5o0JloWBboIF2ENwWfmQwCJesfQ_MXgNB5iWuB45oQpy_zktRhaO-ZAQaEcMMO27H68exIhkwh/pubchart?oid=626067055&amp;format=interactive"></iframe>
<iframe width="365" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRDiW5o0JloWBboIF2ENwWfmQwCJesfQ_MXgNB5iWuB45oQpy_zktRhaO-ZAQaEcMMO27H68exIhkwh/pubchart?oid=518709836&amp;format=interactive"></iframe>

### How to participate

If you are ready to support GeoServer 3, please, fill [this](https://forms.gle/EFML8NSJSCtzjWUY6) online form or contact us at [gs3-funding@googlegroups.com](mailto:gs3-funding@googlegroups.com) to express your interest and pledge your support.

Thanks to the following organisations for pledging their support:

* DLR
* Geocrafter - Geospatial Studio
* HL Consulting
* JDEV
* Plangis
* Quarticle Research Srl
* Region Västra Götaland
* Terrestris
* Value AG
* Western Run Adventures, LLC
* geosos

And individual donations: Abhijit Gujar, Laurent Bourgès.

Thank you, together we can secure the future of GeoServer for years to come.

### FAQ

This section addresses common questions that have been asked by sponsors and community members.

#### Q: What work actually needs to be done?

The [project plan](https://docs.google.com/document/d/1EmI1kDsqeoxB9GANiiaZy56RY0pWbl6GqD4fq8EJ4oo/edit?tab=t.0) outlines of the following milestones:

*  *Milestone 1: Preparation*

   This activity is targeted for the bulk of the work, doing everything possible ahead of time before the migration to spring-framework-6. Major updates to Wicket user interface library, replacing the image processing engine, updating to Java 17 can all be performed ahead of time.

* *Milestone 2: Migration*

  The migration to spring-framework-6 is accomplished coordinated activity across nine codebases. This places a “code-freeze” on development while updates are performed.

* *Milestone 3: Delivery*
  
  With the core projects updated and the end of the "code-freeze" integration testing with downstream applications, user interface updates, can be performed.

The project steering committee shared [2024 roadmap]({% post_url 2024-01-03-roadmap%}) describing the technical challenges.

#### Q: What needs to be updated?

The following updates are required to update to spring-framework-6.

<img src="/img/posts/2.26/gs3-updates.svg" alt="GeoServer 3 Updates" style="display:block; margin-left:auto; margin-right:auto; width:70%;"/>

![](/img/posts/2.26/gs-updates.svg)

#### Q: My organization procurement cannot respond to a crowdfunding campaign, can we fund a specific activity?

We have the flexibility to write your invoice against a specific deliverable outlined in the project plan.

Please note that the items in *Milestone 1 Preparation* are suitable to be funded by an individual contract:

* These deliverables are required to start the migration to spring-framework 6.
* Each item accomplish a specific goal with a clear deliverable that can be pursued immediately.

For organizations operating with an annual budget you may wish to fund an activity such as ImageN from Milestone 1 before year end.

#### Q: OGCAPI Features is mentioned, is this included in the GeoServer 3 crowdfunding activity?

Camptocamp is hosting a codespring in early November on this topic and we anticipate having OGCAPI Features [ready in time](https://github.com/geoserver/geoserver/wiki/GSIP-230) for GeoServer 3.

The transition from OGC Open Web Services (WMS, WFS, WCS) to OGCAPI services will take place over the next several years. Adjusting the GeoServer user interface with this transition is included as part of the GeoServer 3 project plan.

#### Q: Can my developers work in-kind on this activity?

The project steering committee shared [roadmap challenges]({% post_url 2024-01-03-roadmap%}) with an invitation for in-kind contributions earlier in the year.

At the time of writing:

* Only one activity, spring-security update, has been started successfully. Visit the developer forum to discuss the next step on this activity.
* The Wicket update was started but almost lost due to lack of review and testing. There are a number of tasks for Wicket 9 that are in need of assistance.
* OAuth2 rewrite has started, and should be tested and adapted for use in different operational environments.

The key ingredient here is the ability to focus for an extended period of time with access to individuals to test and review the results.

With this experience in mind we are recommending any in-kind contributions help out with the activities above, and look at helping out in Milestone 3.

#### Q: Is there a deadline for GeoServer 3?

This activity is subject to pledges being acquired in Phase 1 and has no deadline.

From a team availability and risk standpoint we would love to start development in January in time for the GeoServer March release cadence.

Initial guidance was that Spring Framework 5.3 would be supported until December 2024. However that timeline was revised and support ended in August 2024.

As a result GeoServer team is running with some risk, and any security vulnerabilities reported for Spring Framework 5.3 will need to be mitigated rather than addressed.

#### Q: What happens if the funding goal is not reached?

The crowdfunding campaign will not collect any funds. The roadmap challenge for the GeoServer Project Steering committee remains.

Some ideas, and why the consortium have recommended crowdfunding:

1. The project can continue to make GeoServer 2 releases on Spring Framework 5.3, however we anticipate organizations losing operational authority as security vulnerabilities are announced.

   As with the Log4J vulnerability a lot of funding/interest may be available very quickly if a serious issue arises, however the *Milestone 2 migration* still requires a sustained effort to accomplish.

   This approach delays the effort until there is an actual emergency. The level of coordination required makes this activity unsuitable to be done in an urgent fashion. The **crowdfunding approach is recommended**.

2. The project could start a new GeoServer 3 branch, making GeoServer 2 releases concurrently as GeoServer 3 is developed.

   The approach of splitting developer resources was recently used for GeoNetwork 3 / GeoNetwork 4 resulted in dividing the project resources for several years.

   During such a transition it is challenging for customers/service providers to set up contracts to work on a system that is not yet a fully functional drop-in-replacement. At the same time it is difficult to justify adding new functionality to the older release as any work done is subject to further migration costs.

   This approach leaves everyone exposed to risk, and is not a good match with the consulting model of GeoServer service providers. The **crowdfunding approach with minimal disruption is recommended**.

3. The project could start a new GeoServer 3 application, delegating to a GeoServer 2 application as functionality is migrated.

   This approach is being started by GeoNetwork 4 / GeoNetwork 5 to accomplish their own Spring Framework 6 migration.

   This approach is more complicated, requiring seperate containers to run Java 11 and Java 21 environments concurrently. The increased complexity requires more funding, however the amount of work is spread out over time and can be achieved with a smaller team.

   This delegation approach may be suitable for the consulting model of GeoServer service providers.  With the risk of using SpringFramework 5.3 being spread out over a longer period of time, the **crowdfunding approach is recommended**.

#### Q: Does this kind of expense happen often?

Yes, significant costs can and do occur, however it is unusual for several such activities to happen concurrently. 

Prior activities of this nature:

* [2023 OpenGIS Harmizonation](https://www.osgeo.org/opengis-harmonization/)
* [2018 Java 11 Update]({% post_url 2018-09-24-java-2018-code-sprint %})
* [2016 Wicket 7 Update](https://wiki.osgeo.org/wiki/GeoServer_Code_Sprint_2016)

Maintaining [project sponsorship](/sponsor/) is important to enable the GeoServer PSC to proactively identify and address roadmap challenges. We have seen an increase in the cadence of Java releases and increased expectations around the handling of security vulnerabilities affecting the project.

As outlined in the [2024 roadmap]({% post_url 2024-01-03-roadmap%}) the project steering committee is being more transparent with sponsorship and costs.

#### Q: Will Cloud Native GeoServer be included?

Yes.

MapStore, GeoNode and Cloud Native GeoServer have been prioritized by initial sponsors and included in Milestone 3.

#### Q: Why not a kickstarter or go fund me?

Prior experience GeoServer tends to be used by organisations rather than individuals.

Individuals are encouraged to donate via GitHub and as outlined on the [GeoServer Sponsorship](/sponsor/) page.