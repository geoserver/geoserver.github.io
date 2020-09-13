---
author: geoserver
comments: true
date: 2010-05-17 14:18:51+00:00
layout: post
link: http://blog.geoserver.org/2010/05/17/oracle-georaster-custom-jdbc-access/
slug: oracle-georaster-custom-jdbc-access
title: Oracle GeoRaster & Custom JDBC Access
wordpress_id: 630
categories:
- Features
tags:
- Features
- images
- jdbc
- Mosaic
- oracle
- raster
---

With the soon-to-be-released GeoServer 2.0.2, there are some exciting new features, two of which I would like to mention here.

GeoServer will soon be able to handle [raster/image data in customized JDBC database layouts](http://docs.geoserver.org/stable/en/user/data/customjdbcaccess.html). This is useful for special use cases or existing image databases, offering the freedom of choosing individual table layouts, provided the needed data and image meta information is available.

Because of this new feature, GeoServer will be able to serve [Oracle GeoRaster](http://docs.geoserver.org/stable/en/user/data/oraclegeoraster.html) files.  This new functionality is due to improvements to underlying GeoTools imagemosaic-jdbc module.

For those who aren't familiar, the imagemosaic-jdbc extension enables storing tiles and pyramids into a JDBC database. This is useful for building and storing an image SQL database from scratch, following a predefined table layout.  See the [image mosaic tutorial](http://docs.geoserver.org/stable/en/user/tutorials/imagemosaic-jdbc/imagemosaic-jdbc_tutorial.html) for more information on how this works.
