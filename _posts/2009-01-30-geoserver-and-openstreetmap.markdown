---
author: iwillig
comments: true
date: 2009-01-30 18:40:17+00:00
layout: post
link: http://blog.geoserver.org/2009/01/30/geoserver-and-openstreetmap/
slug: geoserver-and-openstreetmap
title: GeoServer and OpenStreetMap
wordpress_id: 177
categories:
- Tips and Tricks
- Tutorials
tags:
- OpenStreetMap
---

[OpenStreetMap](http://openstreetmap.org) is a free and editable map of the world.  Founded in 2004 in the United Kingdom in response to the need for a free geospatial data source, it is a community-driven project, allowing for anyone to edit and contribute information.   It has since grown to include data from almost all countries in the world.  The map generated from their data can be used as an alternative to commercial map layers such as those found in Google Maps.  The OpenStreetMap base layer is rendered using [Mapnik](http://mapnik.org), however since the data is free to download and distribute, it is possible to serve it using GeoServer.   I recently went through the process of rendering OpenStreetMap's data with GeoServer.

**The data**

OpenStreetMap provides [instructions on downloading their data](http://wiki.openstreetmap.org/index.php/Planet.osm).  The full data set is a large file, currently about 4GB when compressed and about 100GB when uncompressed.  (You can [download sections of the data set](http://downloads.cloudmade.com/) as well.)  This data is an XML-based data format that GeoServer cannot read natively.  [PostGIS](http://postgis.refractions.net) is the optimal way of storing such a large volume of data when using GeoServer.  Luckily, there is a converter that allows you to load the OpenStreetMap data into PostGIS called `osm2pgsql`.  This program is a package available on Debian-based distributions (such as Ubuntu), and is also available as a binary on [Windows](http://tile.openstreetmap.org/direct/osm2pgsql.zip)`.
`

Run the following command:

`osm2psql -E 900913 -d osm planet.osm`

This will process the XML information and load the data into a PostGIS database called “osm”. The -E defines the projection of the source data, which in this case is 900913, the projection used in Google Maps, and the default for OpenStreetMap.

If successful, the database will contain the following tables:

`planet_osm_line
planet_osm_point
planet_osm_polygon
planet_osm_roads`

**Making sense of the data**

OpenStreetMap's data can be a bit confusing.  For a first time user like myself, just trying to figure out their naming convention was challenging.  They do, however, have a wonderful [map key](http://wiki.openstreetmap.org/wiki/Map_Features) hidden away in their [wiki](http://wiki.openstreetmap.org).  This page is a lifesaver.

There are two different tables that contain line data, `planet_osm_line `and `planet_osm_roads`. The former includes railroads, subways, and other linear information.  The latter is made up exclusively of roads.  The `planet_osm_point` table has a range of data: subway stations, shopping centers, universities, and even brothels. Lastly the `planet_osm_polygon` table has, but is not limited to, parks, bodies of water, and even buildings in certain urban areas.

**Styling**

[![](http://blog.geoserver.org/wp-content/uploads/all-roads1.tiff)](http://blog.geoserver.org/wp-content/uploads/all-roads1.tiff)

On my map I grouped the roads into three major groups; residential, secondary, and limited-access (highways).  To achieve this grouping I used the following SLD filters.
<table cellspacing="5" border="1" >
<tbody >
<tr >

<td >**Road class**
</td>

<td >**PropertyName**
</td>

<td >**Values**
</td>
</tr>
<tr >

<td >Residential
</td>

<td >highway
</td>

<td >residential OR unclassified
</td>
</tr>
<tr >

<td >Secondary
</td>

<td >highway
</td>

<td >primary OR secondary
</td>
</tr>
<tr >

<td >Limited-access
</td>

<td >highway
</td>

<td >motorway OR trunk
</td>
</tr>
</tbody></table>
I then styled the map to distinctly display the three groups of roads, and also varied their widths depending on the zoom level.  This was the most time-consuming part of the process, as I needed to create and evaluate styles for each zoom level.  The [final SLD](http://blog.geoserver.org/wp-content/uploads/osm_roadssld.zip) is very large, but is available for those interested.

**Final touches**

Since the purpose of this map was to create a viable base layer that anyone can incorporate into their mapping projects, performance was a concern.  To address this, I used [GeoWebCache](http://geowebcache.org), a tile cache mechanism built into GeoServer.  The [GeoWebCache documentation](http://geoserver.org/display/GEOSDOC/5.+GWC+-+GeoWebCache) has details on this process.

**The finished (?) map**

The finished product can be found at [http://demo.opengeo.org/openstreetmap](http://demo.opengeo.org/openstreetmap ).

[![](http://geoserver.wpengine.com/wp-content/uploads/2009/01/all-roads-300x103.png)](http://demo.opengeo.org/openstreetmap)

Feel free to link to this map.  Use this [OpenLayers code](http://blog.geoserver.org/wp-content/uploads/openstreetmaphtml.zip) to get started.  This map is a work in progress.  Future enhancements will include adding public transportation systems, railroads, buildings, and more.  If you have any feedback on this map please email me at iwillig at opengeo dot org.

With GeoServer, PostGIS, OpenLayers and the OpenStreetMap data set, it is possible to build high-quality, professional-looking maps, allowing you to take control of what data you present, define your own mapping aesthetic, and free yourself from having to use commercial map layers.
