---
author: Andrea Amie, Jody Garnett
date: 2021-03-03
layout: post
title: GeoServer 2.19-RC Released
categories:
- Announcements
tags:
- Release Candidate
---

We are pleased to announce the release of GeoServer [2.17.5](http://geoserver.org/release/2.17.5/) with downloads (
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.5/geoserver-2.17.5-war.zip/download) |
[bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.5/geoserver-2.17.5-bin.zip/download) ), [documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.5/geoserver-2.17.5-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.5/extensions/) .

We are happy to announce GeoServer [2.19-RC](http://geoserver.org/release/2.19-RC/) release candidate is available for testing. Downloads are available ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19-RC/geoserver-2.19-RC-bin.zip/download) and [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19-RC/geoserver-2.19-RC-war.zip/download)) along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19-RC/geoserver-2.19-RC-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19-RC/extensions/).

This is a GeoServer release candidate made in conjunction with GeoTools 25-RC and GeoWebCache 1.19-RC.

  * Release candidates are a community building exercise and are not intended for production use.
  * We ask the community (everyone: individuals, organizations, service providers) to download and thoroughly test this release candidate and report back.
  * Participating in testing release candidates is a key expectation of our [open source social contract](http://www.ianturton.com/talks/foss4g.html#/). We make an effort to thank each person who tests in our release announcement and project presentations!

## Release Candidate Testing Priorities

This is an exciting release and a lot of great new functionality has been added. We would like to ask for your assistance testing the following:

  * The number one testing priority is to try out GeoServer with your data! _Mass market open source thrives on having many people to review. Scientific open source like GeoServer thrives on exposure to many datasets_.
  * Help check that new [extension download bundles](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19-RC/extensions/) have contain everything needed, including appropriate readme instructions and open source license information.
  * The rest of this blog post highlights new features for GeoServer 2.19, please try out these features, read the documentation links, and ask questions.

Known Issues:

  * Layer configured with missing style throws NPE

## MapML module graduated to extension

...

## Retired Extensions

Several extensions being retired from this release:

  * ArcSDE
  
In each case we found that the extension is no longer used, or lacked sufficient feedback and resources for continued development.

## OGC API Community module

The [OGC API community module](https://docs.geoserver.org/latest/en/user/community/ogc-api/index.html#installing-the-geoserver-ogc-api-module) includes the latest updates for OGC API services:

  * OGC API Maps implementation
  * OGC API Features has a new user interface with a response layout
  * Updated [documentation ](https://docs.geoserver.org/latest/en/user/community/ogc-api/index.html#installing-the-geoserver-ogc-api-module) with a table indicating what core api and draft extensions is implemented by each service

Please try out these new and evolving standards and enjoy their simplicity. We ask interested parties to contribute with testing, coding and financially towards this activity.

## And more!

There are several other new features and improvements, including:

  * Upgrade SQL Server packaging to use open source JDBC driver
  * Setting Entity Expansion limit on WFS XML Readers

Find out more in the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16766).

## About GeoServer 2.19

Additional information on GeoServer 2.19 series:

  * Release notes ([2.19-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16766))

