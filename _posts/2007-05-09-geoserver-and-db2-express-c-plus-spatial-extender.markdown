---
author: Chris Holmes
comments: true
date: 2007-05-09 19:51:58+00:00
layout: post
link: http://blog.geoserver.org/2007/05/09/geoserver-and-db2-express-c-plus-spatial-extender/
slug: geoserver-and-db2-express-c-plus-spatial-extender
title: GeoServer and DB2 Express-C plus Spatial Extender
wordpress_id: 40
categories:
- Developer notes
---

We recently learned about IBM's [DB2 Express-C](http://www-306.ibm.com/software/data/db2/express/) database, a free version of DB2 that comes with less restrictions than the free [Oracle XE](http://www.oracle.com/technology/xe/index.html) (which GeoServer also supports through Oracle Locator).Â  Our main curiosity is if it will work with GeoServer.Â  So we got in touch with David Adler, our community member from IBM, to ask if it will work out of the box.Â  The answer is that it's not quite 'out of the box', but that one only needs to download and install the [spatial extender](http://www-306.ibm.com/software/data/spatial/db2spatial/), which is also a free download.Â  David additionally assures us that the information on[ this developerworks](http://www-128.ibm.com/developerworks/db2/library/techarticle/0301zikopoulos/0301zikopoulos1.html) article is wrong, and that spatial extender is available with the Express-C edition.Â  The only restrictions on it are related to the capacity of the machine you're running it on, only 2 dual core chips and up to 4 gigabytes of ram.Â  But there are no restrictions on the size of the database.Â  If you have some good experience with Express-C and GeoServer please let us know, in the comments or an email.
