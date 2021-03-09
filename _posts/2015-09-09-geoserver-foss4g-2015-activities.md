---
author: geoserver
comments: true
date: 2015-09-09 23:21:47+00:00
layout: post
link: http://blog.geoserver.org/2015/09/09/geoserver-foss4g-2015-activities/
slug: geoserver-foss4g-2015-activities
title: GeoServer FOSS4G 2015 Activities
wordpress_id: 2325
categories:
- Developer notes
---

Next week the open source spatial community is gathering in Seoul Korea for the Free and Open Source Software for Geospatial (FOSS4G) conference - and GeoServer will be there!


[![](/img/uploads/foss4g20151.png)](http://blog.geoserver.org/2015/09/09/geoserver-foss4g-2015-activities/foss4g2015/)


The [final program](http://2015.foss4g.org/programme/presentations/) has just been made available as a [PDF](http://2015.foss4g.org/wp-content/uploads/2014/11/FOSS4G-Seoul-2015-Programme.pdf). As the program does not include sessions abstracts they are included here - after the break.

<!-- more -->


## Monday September 14th


**GeoServer Performance Tuning** ([WS01](http://www.meci.co.kr/societyevent/FOSS4G2015/sessions.html#WS01)) - All day, Room 1, Jody Garnett and Tom Ingold


<blockquote>_GeoServer is renowned OSGeo application for publishing spatial data. Attend this workshop to benchmark, optimise and tune both GeoServer and your data for the best possible performance._
_Speed is critical to both the users experience and ensuring you get the best value out of your infrastructure investment. While we will talk through the effect of cpu and disk performance this workshop is focused on data preparation, benchmarking and JVM performance considerations._
_While we will talk through the effect of cpu and disk performance this workshop is focused on data preparation, benchmarking and JVM performance considerations. _
_GeoServer performance topics include:_

> 
> 
	
>   * _Establishing a performance baseline and JVM performance tuning_
> 
	
>   * _GeoServer services performance considerations_
> 
	
>   * _Rendering performance and style optimisation_
> 
	
>   * _Generated pre generalized vector data and dynamically changing vector data based on scale_
> 
	
>   * _Raster performance considerations and GeoTiff optimisation_
> 
	
>   * _Image format implementations and encoding optimization_
> 

_GeoWebCache topics include:_

> 
> 
	
>   * _Introduction to GeoWebCache and tile map protocols_
> 
	
>   * _Define a tiling strategy and walkthrough the configuration options used to set a tile cache_
> 
	
>   * _GeoWebCache administration and production considerations_
> 

_Some familiarity with GeoServer is expected. Sample data is provided although you are welcome to bring your own and use this workshop to explore your organization's optimisation challenges._</blockquote>




## Tuesday: September 15th


**Beyond GeoServer Basics** ([WS19](http://www.meci.co.kr/societyevent/FOSS4G2015/sessions.html#WS19)) - Morning, Room 3, Tom Ingold and Jody Garnett


<blockquote>_In this workshop, attendees will learn about many different features that GeoServer has to offer beyond simply loading and publishing data. From catalog operations to data filters, you will be exposed to many different aspects of GeoServer configuration that are overlooked. The specific topics that will be covered include: WPS, rendering transforms, SQL Views, WFS-T, the REST API and data filtering. This workshop will assume that you are familiar with basic GeoServer concepts and interaction, such as how to load and publish a shapefile._</blockquote>


**Web Mapping with OGC Services and GeoServer: an Introduction** ([WS20](http://www.meci.co.kr/societyevent/FOSS4G2015/sessions.html#WS20)) - Afternoon, Room 2, Andrea Aime


<blockquote>_This workshop will provide an introduction to OGC services implementation with GeoServer and GeoWebCache. The workshop will cover:_

> 
> 
	
>   * _Setting up vector data, such as shapefile and postgis, in GeoServer_
> 
	
>   * _Setting up raster data, such as geotiff, in GeoServer_
> 
	
>   * _Introduction to the Web Map Service protocol and usage of configured data from external clients_
> 
	
>   * _Creating GeoServer styles with desktop tools_
> 
	
>   * _Introduction to the Web Map Tile Service, with examples using the GeoServer embedded GeoWebCache_
> 

_In order to participate no previous knowledge of GeoServer and OGC services is required, but a basic knowledge of GIS concepts and basic data formats (shapefiles, geotiff) is recommended._</blockquote>




## Wednesday: September 16th


**GeoServer for Spatio-temporal Data Handling With Examples For MetOc And Remote Sensing** - 13:50 Room 11, Andrea Aime, Simone Giannecchini, Daniele Romagnoli


<blockquote>_This presentation will provide detailed information on how to ingest and configure SpatioTemporal in GeoServer to be served using OGC services, with examples from WMS and WCS services. Topics covered are as follows:_

> 
> 
	
>   * _Discussion over existing data formats and how to preprocess them for best serving with GeoServer_
> 
	
>   * _Configuring SpatioTemporal raster and vector data in GeoServer_
> 
	
>   * _Serving SpatioTemporal raster and vector data with OGC Services_
> 
	
>   * _Tips and techniques to optimize performance and allow maximum exploitation of the available data The attendees will be provided with the basic knowledge needed to preprocess and ingest the most common spatiotemporal data from the MetOc and Remote Sensing field for serving via GeoServer._
> 

</blockquote>


**Mapping the world beyond 3857** - 16:00 Room 9, Andrea Aime


<blockquote>_Most popular mapping presentations today, ranging from clients to servers, show and discuss only maps in EPSG:3857, the popular Mercator derived projection used by OSM as well as most commercial tiles providers._

_There is however an interesting, exciting world of map projections out there, that are still being used in a variety of context. This presentation will introduce the advancement made in GeoTools and GeoServer to handle those use cases, where users have a worldwide data set, and need to view all or part of it in multiple projections, some of which valid in a limited area, and requiring the software to perform a proper display of it on the fly, without any preparation._

_We’ll discuss GeoTools/GeoServer “advanced projection handling” manages to deal with these cases, wrapping data, dealing with the poles and the dateline, cutting on the fly excess data, densifying on the fly long lines as needed to ensure a smooth reprojection, for a variety of cases, ranging from seemingly innocuous datum shifts, maps having the prime meridian over the pacific, and the various tricks to properly handle stereographic, transverse mercator, Lambert conic and other limited area projections against world wide source data sets._</blockquote>


**State of GeoServer** - 16:25 Ballroom B, Jody Garnett


<blockquote>_State of GeoServer reviewing the new and noteworthy features introduced in the past year. The project has an aggressive six month release cycle with GeoServer 2.7 and 2.8 being released this year._

_ __These releases bring together exciting new features. A lot of work has been done on processing services with clustering, security and processing control._

_ __The rendering engine continues to improve with the addition of color blending opening up a range of creative possibilities. The CSS extension (used to easily generate OGC standard styles) has been cleaned up with a rewrite._

_This talk will highlighted updates on data import, application schema use, data transforms and the latest from the developer list._

_Attend this talk for a cheerful update on what is happening with this popular OSGeo project. Whether you are an expert user, a developer, or simply curious what these projects can do for you, this talk is for you._</blockquote>


**GeoServer GeoTools BOF** - 17:40 Room 10


<blockquote>_See [wiki](http://wiki.osgeo.org/wiki/FOSS4G_2015_BirdsOfAFeather#GeoServer_.2F_GeoTools_BOF) page for details, and to note your attendence._</blockquote>




## Thursday: September 17th


**GeoServer on Steroids **- 11:25 Ballroom B, Andrea Aime, Simone Giannecchini


<blockquote>

> 
> _Setting up a GeoServer can sometimes be deceptively simple. However, going from proof of concept to production requires a number of steps to be taken in order to optimize the server in terms of availability, performance and scalability. The presentation will show how to get from a basic set up to a battle ready, rock solid installation by showing the ropes an advanced user already mastered. The topics that will be covered in details include:_
> 
> 


> 
> 
	
>   * _Optimize vector and raster data for the deep multi-resolution displays typical of web GIS_
> 
	
>   * _Optimize styling to provide a good balance between map navigability and performance, identifying common performance pitfalls in the styling options_
> 
	
>   * _Setting up caching with GWC for the background layers, identify layers and situations that are not suitable for caching_
> 
	
>   * _Defend against peak hour load by setting service limits and using the control-flow extension_
> 
	
>   * _Using the monitoring extension to control the server in production and identify sources of trouble (long request, clients making too many/too heavy requests, layers and services used the most that could use more tuning attention)_
> 
	
>   * _Solutions for clustering GeoServer and GeoWebCache_
> 
	
>   * _Challenges in scaling beyond the few hundreds concurrent requests, and solutions to get there The presentation will end with real world examples of enterprise deployments of GeoServer implemented by the author as well as its colleagues at GeoSolutions during the years._
> 

</blockquote>


**Mapping in GeoServer with SLD and CSS** - 14:15 Room 10, Andrea Aime


<blockquote>_Various software can style maps and generate a proper SLD document for OGC compliant WMS like GeoServer to use. However, in most occasions, the styling allowed by the graphical tools is pretty limited and not good enough to achieve good looking, readable and efficient cartographic output. For those that like to write their own styles CSS also represents a nice alternatives thanks to its compact-ness and expressiveness._

_Several topics will be covered, providing examples in both SLD and CSS for each, including: mastering multi-scale styling, using GeoServer extensions to build common hatch patterns, line styling beyond the basics, such as cased lines, controlling symbols along a line and the way they repeat, leveraging TTF symbol fonts and SVGs to generate good looking point thematic maps, using the full power of GeoServer label lay-outing tools to build pleasant, informative maps on both point, polygon and line layers, including adding road plates around labels, leverage the labelling subsystem conflict resolution engine to avoid overlaps in stand alone point symbology, blending charts into a map, dynamically transform data during rendering to get more explicative maps without the need to pre-process a large amount of views. The presentation aims to provide the attendees with enough information to master SLD/CSS documents and most of GeoServer extensions to generate appealing, informative, readable maps that can be quickly rendered on screen._</blockquote>




## Friday: September 18th


**Raster Data In GeoServer and GeoTools: Achievements, Issues And Future Developments** - 14:00 Room 9m Andrea Aime, Simone Giannecchini


<blockquote>_The purpose of this presentation is, on a side, to dissect the developments performed during last year as far as raster data support in GeoTools and GeoServer is concerned, while on the other side to introduce and discuss the future development directions._

_Advancements and improvements for the management of multidimensional raster data (NetCDF, GRIB, HDF) and mosaic thereof will be introduced, as well as the available ways to manage sliding windows of data via the REST API and importer._

_Extensive details will be provided on the latest updates for the management of multidimensional raster data used in the Remote Sensing and MetOc fields, including support for WCS EO and WMS EO, and some considerations on the WCS MetOc extensions._

_The presentation will also introduce and provide updates on jai-ext, imageio-ext, and JAITools. jai-ext provides extended JAI operators that correctly handle NODATA and regione of interests (masks), JAITools provides a number of new raster data analysis operators, including powerful and fast raster algebra support, while ImageIO-Ext bridges the gap across the Java world and native raster data access libraries providing high performance access to GDAL, Kakadu and other libraries._

_The presentation will wrap up providing an overview of unresolved issues and challenges that still need to be addressed, suggesting tips and workarounds allowing to leverage the full potential of the systems._</blockquote>


**Advanced Security with GeoServer and GeoFence** - 14:30 Room 13, Andrea Aime, Simone Giannecchini


<blockquote>_The presentation will provide an introduction to GeoServer own authentication and authorization subsystems. We’ll cover the supported authentication protocols, such as from basic/digest authentication and CAS support, check through the various identity providers, such as local config files, database tables and LDAP servers, and how it’s possible to combine the various bits in a single comprehensive authentication tool, as well as providing examples of custom authentication plugins for GeoServer, integrating it in a home grown security architecture._

_We’ll then move on to authorization, describing the GeoServer pluggable authorization mechanism and comparing it with proxy based solution, and check the built in service and data security system, reviewing its benefits and limitations._

_Finally we’ll explore the advanced authentication provider, GeoFence, explore the levels on integration with GeoSErver, from the simple and seamless direct integration to the more sophisticated external setup, and see how it can provide GeoServer with complex authorization rules over data and OGC services, taking into account the current user, OGC request and requested layers to enforce spatial filters and alphanumeric filters, attribute selection as well as cropping raster data to areas of interest._</blockquote>


**Everybody wants (someone else to do) it: Writing documentation for open source software** - 13:25 Ballroom B, Jody Garnett


<blockquote>_Many people will cite how their adoption of software was based on the quality of documentation, and yet documentation can be one of the largest gaps in quality with an open source project._

_This talk will discuss why that is, what you (yes you) can do about it, and how the author has managed to avoid burnout (so far) by learning to accept less-than-perfect grammar._**
**</blockquote>




## Saturday: September 20th


**GeoServer GeoTools Code Sprint** - 9:00 Biz Gangnam Education & Training Center


<blockquote>_See [wiki](http://wiki.osgeo.org/wiki/FOSS4G_2015_Code_Sprint#GeoTools.2FGeoServer) page for details, and to note your attendance._</blockquote>









