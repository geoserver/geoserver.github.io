---
author: geoserver
comments: true
date: 2015-09-29 23:11:14+00:00
layout: post
link: http://blog.geoserver.org/2015/09/29/new-repository-and-release-delay/
slug: new-repository-and-release-delay
title: New repository and release delay
wordpress_id: 2356
categories:
- Developer notes
---

A quick message for all those who have been asking - I have started the GeoServer 2.8 release process but have run into a snag. The repo.boundlessgeo.com maven repository has been slowed down due to increased network traffic. We are setting up a replacement (cloud hosted which will allow allow more developers to manage).

What I would like to ask is for developers to try it out by adding the following to maven **settings.xml**:

    
      <mirrors>
        <mirror>
          <id>boundlessgeo</id>
          <name>Boundless Cloud Repository</name>
          <url>https://boundless.artifactoryonline.com/boundless/main</url>
          <mirrorOf>boundless</mirrorOf>
        </mirror>
      </mirrors>


Please try the above and report back to geoserver-devel, and we can cut over to the new repository tomorrow.

Thank you for your assistance, and please accept our apologies for the delay in releasing 2.8.0.

**Update:** We have now migrated to the new repository.


## Maven Developers


For developers using maven to depend on geoserver jars (for those running a custom geoserver build) please note that we have now migrated to the new repository.

The repository details have not changed:

    
      <repository>
       <id>boundless</id>
       <name>Boundless Maven Repository</name>
       <url>http://repo.boundlessgeo.com/main/</url>
      </repository>


The exception is for projects (such as GeoWebCache, GeoFence, GeoScript) that deploy artifacts. We ask you to change your distributionManagement section to the following:

    
    <distributionManagement>
      <repository>
       <id>boundless</id>
       <name>Boundless Release Repository</name>
       <url>https://boundless.artifactoryonline.com/boundless/release/</url>
       <uniqueVersion>false</uniqueVersion>
      </repository>
      <snapshotRepository>
       <id>boundless</id>
       <uniqueVersion>false</uniqueVersion>
       <name>Boundless Snapshot Repository</name>
       <url>https://boundless.artifactoryonline.com/boundless/snapshot/</url>
      </snapshotRepository>
     </distributionManagement>
    


Contact geoserver-devel if you have any questions.
