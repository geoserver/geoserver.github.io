---
author: jgarnett
comments: false
date: 2017-04-27 05:12:49+00:00
layout: post
link: http://blog.geoserver.org/2017/04/27/geoserver-monthly-bug-stomp/
slug: geoserver-monthly-bug-stomp
title: GeoServer monthly bug stomp
wordpress_id: 2860
categories:
- Behind The Scenes
tags:
- BugFix
---

Our monthly GeoServer bug stomps are moving to the last Friday of each month.

[![bug_stomp](/img/uploads/bug_stomp.png)](/img/uploads/bug_stomp.png)

Previously these events were [scheduled](http://blog.geoserver.org/2016/11/09/bug-stomp/) when people were available, making planning difficult. By choosing a set date each month it is easier to schedule a time to participate for all involved.


## Tips for Participating


Thanks to Matt Kruszewski for the following notes on how to take part.

**Before you start**

Get ready:



 	
  1. Join the gitter.im channel [geoserver/geoserver](https://gitter.im/geoserver/geoserver), you can sign in with your github id.

 	
  2. Sign up for [Jira](https://osgeo-org.atlassian.net/projects/), so you can review and add to bugs.

 	
  3. Join the [geoserver-devel@lists.sourceforge.net](https://lists.sourceforge.net/lists/listinfo/geoserver-devel) and introduce yourself!  In your email, you can be asked to be added to the Jira development team (so you can volunteer to work on a bug during the sprint).

 	
  4. Double check the [contributing guidelines](https://github.com/geoserver/geoserver/blob/master/CONTRIBUTING.md) (you may need to sign a code license agreement prior to starting work.)


Git ready:


<blockquote>

> 
> _# GeoServer uses Fork & Branch GitFlow_
_ # Fork the geoserver/geoserver project on github, then clone it locally and add the main_
_ # project as an upstream._
> 
> 
_git clone https://github.com/{you}/geotools.git_

_git remote add upstream https://github.com/geoserver/geoserver.git_

_git pull --rebase upstream_

_git checkout -b myBugfixBranch_

_# Before making a pull request, make sure you are up-to-date with upstream._

_git pull --rebase upstream master_

_# (or, rebase)_</blockquote>




For the bug stomp you should work on a branch from master.






 	
  * When your branch is finished, publish it to your fork, and then create a pull request to geoserver/geoserver.

 	
  * For more details, see [Geoserver Developer Guide on using Git](http://docs.geoserver.org/stable/en/developer/source.html#git).




Eclipse or InteliJ recommended:






 	
  * If you are setting up GeoServer for the first time as developer [Quickstart](http://docs.geoserver.org/stable/en/developer/quickstart/index.html#run-geoserver-from-eclipse) in the developers guide.




**Stomping**


If you get stuck or are unsure of how to proceed, ask on gitter!

To find an issue to work on:



 	
  1. Ask on Gitter, and use the [Jira triage list](https://osgeo-org.atlassian.net/issues/?jql=project%20in%20(GEOS%2C%20GEOT)%20AND%20status%20in%20(Open%2C%20%22In%20Progress%22%2C%20Reopened)%20AND%20resolution%20%3D%20Unresolved%20AND%20Triage%20%3D%20sprint%20ORDER%20BY%20key%20DESC%2C%20summary%20DESC%2C%20priority%20DESC%2C%20updated%20DESC) of good candidates (triage=sprint).

 	
  2. At the start of the sprint we [review new bugs](https://osgeo-org.atlassian.net/issues/?jql=project%20in%20(GEOS%2C%20GEOT)%20AND%20status%20in%20(Open%2C%20%22In%20Progress%22%2C%20Reopened)%20AND%20resolution%20%3D%20Unresolved%20AND%20created%20%3E%3D%20-4w%20ORDER%20BY%20created%20ASC%2C%20key%20DESC%2C%20summary%20DESC%2C%20priority%20DESC%2C%20updated%20DESC).


Style:

 	
  1. Make sure to follow the [contribution guidelines](https://github.com/geoserver/geoserver/blob/master/CONTRIBUTING.md)

 	
  2. Format your code using the eclipse formatter profile [here](http://docs.geotools.org/latest/developer/conventions/code/style.html). The same formatter is used for GeoTools and GeoServer.

 	
  3. Make sure to add the license boilerplate

 	
  4. Consult the [GeoTools code conventions](http://docs.geotools.org/latest/developer/conventions/index.html) for common habits

 	
  5. Documentation is required for a UI fix, javadocs for public classes appreciated.


Testing:

 	
  1. Test your fix!

 	
  2. See [Testing](http://docs.geoserver.org/stable/en/developer/programming-guide/testing/index.html) in the GeoServer Developers Guide

 	
  3. Since this is a bug stomp, look at how the code around yours is tested and build on that.


Pull Request

 	
  1. Make a pull request from your branch on your fork to geoserver/geoserver master.

 	
  2. Ask for a review on gitter

 	
  3. Make revisions based on feedback and comments. Additional commits to the branch in your fork are automatically reflected in the PR.


Tips and Tricks

 	
  * We work closely with the GeoTools library for data access, rendering and processing - you may need a checkout of the GeoTools library to be effective.

 	
  * For the bug stomp, pick a bug you can fix, not one you need to fix.

 	
    * Many older issues are already fixed, start by trying to reproduce the problem.

 	
    * Many worth while bugs cannot be fixed in a day




 	
  * Don’t get stuck. Timebox yourself and don’t be afraid to discuss the problem on gitter.

 	
  * Use the code formatter!

 	
  * Don’t worry about making mistakes!  You can run findbugs, or ask for a shared screen code review before submitting your pull request (or “relax and realize the internet is full of fail”.)


Follow-up

 	
  * After the bug stomp, reply to the geoserver-devel email thread with a summary of your progress


Most of all welcome to GeoServer and thanks for taking part.
