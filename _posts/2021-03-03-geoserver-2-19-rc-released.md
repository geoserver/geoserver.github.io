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

We are happy to announce GeoServer [2.19-RC](http://geoserver.org/release/2.19-RC/) release candidate is available for testing. Downloads are available ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19-RC/geoserver-2.19-RC-bin.zip/download) and [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19-RC/geoserver-2.19-RC-war.zip/download)) along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19-RC/geoserver-2.19-RC-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19-RC/extensions/).

This is a GeoServer release candidate made in conjunction with GeoTools 25-RC and GeoWebCache 1.19-RC.

  * Release candidates are a community building exercise and are not intended for production use.
  * We ask the community (everyone: individuals, organizations, service providers) to download and thoroughly test this release candidate and report back.
  * Participating in testing release candidates is a key expectation of our [open source social contract](http://www.ianturton.com/talks/foss4g.html#/). We make an effort to thank each person who tests in our release announcement and project presentations!
  * GeoServer [commercial service providers](http://geoserver.org/support/) are fully expected to test on behalf of their customers.

## Release Candidate Testing Priorities

This is an exciting release and a lot of great new functionality has been added. We would like to ask for your assistance testing the following:

  * The number one testing priority is to try out GeoServer with your data! _Mass market open source thrives on having many people to review. Scientific open source like GeoServer thrives on exposure to many datasets_.
  * Help check that new [extension download bundles](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19-RC/extensions/) have contain everything needed, including appropriate readme instructions and open source license information.
  * The rest of this blog post highlights new features for GeoServer 2.19, please try out these features, read the documentation links, and ask questions.

Known Issues:

  * Layer configured with missing style throws NPE

## MapML extension

The MapML plugin has been under developer for some time as a community module and is now ready for a wider audience.

(example)

(screen snap)

(documentation link)

(thanks to contributor and customer for this development)

## WPS JDBC extension

The WPS JDBC extension allows to share the status of asynchronous WPS requests across a GeoServer cluster. The status of 
all requests, past and ongoing, can be stored in a database, for later reference.

The module uses GeoTools JDBC stores to access databases, create the necessary tables, and track status. 
Connection parameters are provided as property files, e.g.:


```
user=postgres
port=5432
password=******
passwd=******
host=localhost
database=gsstore
driver=org.postgresql.Driver
dbtype=postgis
```

For more information, refer to the [module documentation](https://docs.geoserver.org/latest/en/user/extensions/wps-jdbc/index.html).

We'd like to thank Ian Turton for developing the module on behalf of GeoSolutions, Alessio Fabiani for providing
documentation for it, and Andrea Aime for performing the QA and graduation steps.

## WPS Download extension

The WPS download plugin provides processes assisting in the download of large amounts of data,
allowing to use asynchrounous request, when usage of WFS, WCS or WMS for the same job would lead to HTTP timeouts.
Also, download limits can be configured to avoid excessively large requests: size in MB, number of features, number
of animation frames.

In particular, the following processes are available:

*  ``DownloadEstimator``, verifying that a raster/vector download about to be attempted will fit the download limits.
* ``DownloadProcess``, allowing to download either raster or vector data, reproject and clip them
* ``DownloadMapProcess``, allows to download a large map matching what is visible on a client (which may be using tiles and display on a multi-screen), eventually dynamically fetching layers from remote WMS servers as well. It's also possible to decorate the final map using the standard [decoration layouts](https://docs.geoserver.org/latest/en/user/services/wms/decoration.html#wms-decorations).
* ``DownloadAnimationProcess``, allows to build a MP4 movie given a set of layers and times.

(screen snap)

(documentation link)

(thanks to contributor and customer for this development)

## WMTS Multidimensional extension

(intro)

(example)

(screen snap)

(documentation link)

(thanks to contributor and customer for this development)

## Params-extractor extension

(intro)

(example)

(screen snap)

(documentation link)

(thanks to contributor and customer for this development)

## GeoWebCache-S3 extension

## Retire ArcSDE Extensions

The ArcSDE Extension has been retired.
  
In this case we found that the extension is no longer actively used, and lacked sufficient feedback and resources for continued development. The last tested ArcSDE 10.2.2 version is no longer available, making the required jars required for installation inaccessible.


## Retire the Script community module

The Script community module has been retired.

The module provided scripting abilities for GeoServer, allowing to add WPS processes and small REST services in scripting languages, 
and storing them in the data directory. 

Unfortunately the module fell un-maintained and would no longer build nor work.


## Codebase updates and Quality Assurance

GeoServer continues to be build with the latest open source technologies:

* GeoTools 26-RC
* GeoWebCache 1.19-RC
* JAI-EXT 1.1.19
* JTS 1.18.1
* GeoFence 3.4.7
* Upgrade oshi-core from 5.4.0 to 5.5.0 for new Apple hardware support
* Freemarker 2.3.31
  
We do not get a chance to talk about the code-base that makes up GeoServer often, but recent changes and improvements deserve some praise. The GeoServer team has really embraced automating code checks, starting with simply formatting the code in a consistent fashion, to more advanced techniques checking for common mistakes.

* Switch most of the unit tests from JUnit 3 to JUnit 4
* Remove usage of Vector/Hashtable, replace with ArrayList and HashMap, add PMD rule to enforce it
* Remove un-necessary casts from code, add PMD rule to enforce it
* Replace try/finally with try-with-resources, add a PMD rule to enforce it
* Collapse catch statements with the same body in a multi-catch, add PMD rule to enforce it
* Avoid assertTrue for tests that can be expressed with dedicated assertions. Add PMD rule to enforce it.
* Replace iterator loops with enhanced for loops, add a QA rule to enforce it.
* Run PMD checks on test sources as well.
* Use Collection.isEmpty() when checking for item availability
* Remove explicit types when diamond operator can be used instead. Added a PMD rule to enforce it.
* Remove or suppress unchecked casts, enable the Java compiler lint option for it.

Although all these changes sound small in isolation, the fact that they are performed on the entire codebase, and checked each time a pull-request is proposed, really provides confidence in the technology we publish.

Thanks to Andrea for this valuable work.

## And more!

There are several other new features and improvements, including:

  * Upgrade SQL Server packaging to use open source JDBC driver
  * Setting Entity Expansion limit on WFS XML Readers
  * Tutorial on [running geoserver in cloud foundary](https://docs.geoserver.org/latest/en/user/tutorials/cloud-foundry/run_cf.html).
  * Updated DB2 [installation instructions](https://docs.geoserver.org/latest/en/user/data/database/db2.html)
  

Find out more in the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16766).

## About GeoServer 2.19

Additional information on GeoServer 2.19 series:

  * Release notes ([2.19-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16766))

