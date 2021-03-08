---
author: aaime
comments: true
date: 2017-02-23 03:32:22+00:00
layout: post
link: http://blog.geoserver.org/2017/02/23/geoserver-2-11-beta-released/
slug: geoserver-2-11-beta-released
title: GeoServer 2.11-beta released
wordpress_id: 2795
categories:
- Announcements
---

We are happy to announce the release of [GeoServer 2.11-beta](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11-beta/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11-beta/geoserver-2.11-beta-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11-beta/geoserver-2.11-beta-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10-beta/geoserver-2.11-beta.dmg/download) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11-beta/geoserver-2.11-beta.exe/download)) along with docs and extensions.

This is a beta release of GeoServer made in conjunction with GeoTools 16-beta.

We want to encourage people to test the release thoughly and report back any issue found. With no further delay, let's see what's new, that is, what is there to test!


## YSLD module graduated to supported land


The YSLD styling language has been graduated to supported land, becoming an official extension. YSLD is a YAML based language which closely matches the stucture of SLD, and the internal data model that GeoServer’s renderer uses. Here is an example from the YSLD Cook Book:

    
    <span class="l-Scalar-Plain">title</span><span class="p-Indicator">:</span> <span class="s">'YSLD</span> <span class="s">Cook</span> <span class="s">Book:</span> <span class="s">Simple</span> <span class="s">Line'</span>
    <span class="l-Scalar-Plain">feature-styles</span><span class="p-Indicator">:</span>
    <span class="p-Indicator">-</span> <span class="l-Scalar-Plain">name</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">name</span>
      <span class="l-Scalar-Plain">rules</span><span class="p-Indicator">:</span>
      <span class="p-Indicator">-</span> <span class="l-Scalar-Plain">symbolizers</span><span class="p-Indicator">:</span>
        <span class="p-Indicator">-</span> <span class="l-Scalar-Plain">line</span><span class="p-Indicator">:</span>
            <span class="l-Scalar-Plain">stroke-color</span><span class="p-Indicator">:</span> <span class="s">'#000000'</span>
            <span class="l-Scalar-Plain">stroke-width</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">3
    </span>


Compared to SLD it sports a similar structure, but in a more compact and readable syntax. Here the same example can be expressed in a more compact format:

    
    <span class="l-Scalar-Plain">line</span><span class="p-Indicator">:</span>
    <span class="l-Scalar-Plain">  stroke-color</span><span class="p-Indicator">:</span> <span class="s">'#000000'</span>
    <span class="l-Scalar-Plain">  stroke-width</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">3</span>


Similarly to SLD and CSS, the user guide contains both a [reference](http://docs.geoserver.org/stable/en/user/styling/ysld/reference/index.html) and a [cookbook](http://docs.geoserver.org/stable/en/user/styling/ysld/cookbook/index.html) to get you started. There is also a [styling workshop](http://docs.geoserver.org/latest/en/user/styling/workshop/index.html) with both CSS and YSLD examples (including an important example for [converting your SLD styles to YSLD](http://docs.geoserver.org/latest/en/user/styling/workshop/ysld/done.html#converting-to-ysld)).


## Vector tiles graduate to extension


The vector tiles community module graduated to extension. The module allows to generate vector tiles out of WMS and WMTS requests, using SLD to filter the contents of the tile at the requested scale. Supported vector tiles formats are MVT (MapBox Vector Tile), GeoJSON vector tiles, and TopoJSON vector tiles.

This allow for much more compact data transfers, reduced tile caches thanks to overzooming support, and allows the client to control styling. Here is an example of the client rendering a world map as a vector tile, and highlighting a specific area by attribute:

[![vectortileoutputafrica](/img/uploads/vectortileoutputafrica.png)](/img/uploads/vectortileoutputafrica.png)



Hop on the [documentation to get more information ](http://docs.geoserver.org/latest/en/user/extensions/vectortiles/index.html)about this extension, along with a couple of presentations highlighting vector tile usage.


## Underlying labels in SLD


A new vendor option allow to underline labels in SLD (and CSS). Just add:

    
    <VendorOption name="underlineText">true</VendorOption>


[![Selezione_197](/img/uploads/Selezione_197.png)](/img/uploads/Selezione_197.png)


## Opaque Container Layer Group Mode


A new layer group mode has been added, called "Opaque Container". It's similar to "single" in that you cannot see the layers contained in it, but it also prevents its layers from showing up at the root level of the capabilities document. This new mode is targeted to building "base maps" that the client is not allowed to take apart into their components.

You can read more about layer [group modes in the GeoServer user guide](http://docs.geoserver.org/latest/en/user/data/webadmin/layergroups.html#layer-group-modes).


## Layer Group Security


The build-in data security can now [secure layer groups too](http://docs.geoserver.org/latest/en/user/security/layer.html#), for both global and workspace specific groups. "Tree" mode groups (named tree, container tree, opaque container) will extend the security rules applied to them to the layers contained.

[![Selezione_196](/img/uploads/Selezione_196.png)](/img/uploads/Selezione_196.png)


## Improved loading and OGC request times for large installations


GeoServer has historically had issues with long startup times on installation having several thousands layers. A group of recent improvements significantly sped up these times making it possible to handle tends of thousands of layers with no particular headaches.

For reference, some tests were run on a Core i7 860, 16GB of memory, 2TB hybrid drive (spinning disk plus SSD cache), on two different data directories:






 	
  * "Many states": 1 workspace, 1 store, 10k layers, 10k cached layers

 	
  * "Large": 1001 workspaces, 11000 stores (a mix of shapefiles, postgis, directory of shapefile, single tiff, arcgrid, mosaics), 42000 layers and 42000 associated tile layers


Startup times have been measured in both "cold" and "warm" mode, "cold" means the operating system file system cache contains none of the configuration files and the startup has to actually read everything from the disk, "warm" means the data dir is fully cached in memory instead:

 	
  * Many states, cold startup: 30s

 	
  * Many states, warm startup: 21s

 	
  * Large, cold startup: 107s

 	
  * Large, warm startup: 45s


As you can see, worst case is loading in excess of 40 thousands layers in less than a minute and a half!

For reference, "Large" startup times with JDBCConfig are 290s for cold startup, and 120s for warm startup. This is mostly due to cached layers loading, if your configuration has none the startup time will be of around 20-30 seconds instead (no matter how many layers are configured, because JDBCConfig loads layers on a as-needed basis at runtime... for a cost, see below).

It is also interesting to compare the times needed to run a GetMap against one of the "topp:states" in the "many states" data directory.
<table border="1" >

<tr >
Version
Throughput req/sec
Avg resp. time ms
</tr>

<tbody >
<tr >

<td >2.10.1
</td>

<td align="center" >169
</td>

<td align="center" >47
</td>
</tr>
<tr >

<td >2.10.1 + JDCBConfig
</td>

<td align="center" >68
</td>

<td align="center" >117
</td>
</tr>
<tr >

<td >2.11-beta
</td>

<td align="center" >233
</td>

<td align="center" >34
</td>
</tr>
</tbody>
</table>



More information can be found in the [initial proposal](https://github.com/geoserver/geoserver/wiki/GSIP%20155), and on the latest mailing list thread about [parallel catalog loading](http://osgeo-org.1560.x6.nabble.com/Achievement-unlocked-partial-parallel-catalog-loading-td5308499.html).


## Improved lookup of EPSG codes


Ever been annoyed by some shapefile with a **.prj** declaration that GeoServer does not understand? If so, try this new release, we pulled some extra heuristics and smarts to figure out the equivalent EPSG code of thousands more cases. This will hopefully reduce guesswork when configuring new vector layers, not to mention significantly speeding up importing large directories of shapefiles in the "Importer" extension.

[![Selezione_198](/img/uploads/Selezione_198.png)](/img/uploads/Selezione_198.png)


## Other assorted improvements


There are many improvements to look at in the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=14404), cherry picking a few here:



 	
  * New REST call allowing a users to modify his/her password (no UI for it yet, sorry)

 	
  * Support JSON encoded exceptions for WFS 2.0 too (was already available for 1.0 and 1.1)

 	
  * Drastically reduced output size for WMS PDF output format, when using a graphic fill based on repeated marks or SVG symbols

 	
  * Improved scalability when using "advanced projection handling" thanks to a new implementation of SoftValueHashMap (used as a cache by the referencing subsystem)

 	
  * Better transparency handling of NODATA and ROI (Region Of Interest)

 	
  * Fixes in computation of global disk quota (if you find you have a negative number, upgrade, wipe out the quota database, and restart)




## Test, test, test!


Now that you know about all the goodies, please go, [download and test](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11-beta/) your favorite ones. Let us know how it went!


## About GeoServer 2.11


GeoServer 2.11 is scheduled for March 2017 release. This puts GeoServer back on our six month "time boxed" release schedule.
