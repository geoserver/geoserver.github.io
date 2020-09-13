---
author: jgarnett
comments: false
date: 2017-03-23 08:37:08+00:00
layout: post
link: http://blog.geoserver.org/2017/03/23/geoserver-2-11-0-released/
slug: geoserver-2-11-0-released
title: GeoServer 2.11.0 Released
wordpress_id: 2825
categories:
- Announcements
tags:
- release
- stable
---

We are happy to announce the release of [GeoServer 2.11.0](http://geoserver.org/release/2.11.0/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.0/geoserver-2.11.0-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.0/geoserver-2.11.0-war.zip/download), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10.0/geoserver-2.11.0/download) and [exe](https://sourceforge.net/projects/geoserver/files/GeoServer/2.11.0/geoserver-2.11.0.exe/download)) along with docs and extensions.

This is the latest stable release of GeoSever recommended for production system. This release is made in conjunction with GeoTools.

This release is made by Andrea Aime and Alessandro Parma from the GeoSolutions team. We would like to thank these volunteers  and everyone who contributed features, fixes and time during the release process.

Highlights of this release are featured below, for more information please see the release notes ([2.11.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=15501&styleName=Html&projectId=10000), [2.11-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=15301&projectId=10000) | [2.11-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=14404&projectId=10000&) ).


## Change summary since RC1


If you already had a look at 2.11-RC1 announcement, here is an executive summary of [changes since RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15501):



 	
  * Fixed inability to edit layer groups after modifying a group layer order and layer default style

 	
  * Windows service installer now sets up enough memory for GeoServer to run (for production usage you might still want to tweak it)

 	
  * Fixed interactin between layer group and security that sometimes prevented GetMap from succeding

 	
  * Assorted JMS clustering fixes


See the [full changelog](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=15501) for details. Continue reading for an extended presentation of all the new features in 2.11.0


## Highlights


As this is a major release, GeoServer 2.11.0 contains a number of important changes, including both new features and compatibility requirements.


### Improved loading and OGC request times for large installations


GeoServer has historically had issues with long startup times on installations having several thousands layers. A group of recent improvements significantly sped up these times making it possible to handle tends of thousands of layers with no particular headaches.

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



More information can be found in the [initial proposal](https://github.com/geoserver/geoserver/wiki/GSIP%20155), and on the latest mailing list thread about [parallel catalog loading](http://osgeo-org.1560.x6.nabble.com/Achievement-unlocked-partial-parallel-catalog-loading-td5308499.html).

Thanks to Andrea Aime for this great result.


### Improved lookup of EPSG codes


Ever been annoyed by some shapefile with a **.prj** declaration that GeoServer does not understand? If so, try this new release. We pulled some extra heuristics and smarts to figure out the equivalent EPSG code of thousands more cases. This will hopefully reduce guesswork when configuring new vector layers, not to mention significantly speeding up importing large directories of shapefiles in the "Importer" extension.

[![Selezione_198](http://blog.geoserver.org/wp-content/uploads/2017/02/Selezione_198.png)](http://blog.geoserver.org/wp-content/uploads/2017/02/Selezione_198.png)

Thanks to Andrea Aime for this much appreciated usability improvement.


### Underlying labels in SLD


A new vendor option allow to underline labels in SLD (and CSS). Just add:

    
    <VendorOption name="underlineText">true</VendorOption>


[![Selezione_197](http://blog.geoserver.org/wp-content/uploads/2017/02/Selezione_197.png)](http://blog.geoserver.org/wp-content/uploads/2017/02/Selezione_197.png)

Thanks to Nuno Oliveria and GeoSolutions for this new feature.


### Opaque Container Layer Group Mode


A new layer group mode has been added, called "Opaque Container". It's similar to "single" in that you cannot see the layers contained in it, but it also prevents its layers from showing up at the root level of the capabilities document. This new mode is targeted to building "base maps" that the client is not allowed to take apart into their components.

You can read more about [layer group modes in the GeoServer user guide](http://docs.geoserver.org/latest/en/user/data/webadmin/layergroups.html#layer-group-modes).

Thanks to GeoSolutions and City of Helsinki for sponsoring this new feature.


### Layer Group Security


The build-in data security can now [secure layer groups too](http://docs.geoserver.org/latest/en/user/security/layer.html#), for both global and workspace-specific groups. "Tree" mode groups (named tree, container tree, opaque container) will extend the security rules applied to them to the layers contained.



[![Selezione_196](http://blog.geoserver.org/wp-content/uploads/2017/02/Selezione_196.png)](http://blog.geoserver.org/wp-content/uploads/2017/02/Selezione_196.png)

Thanks to GeoSolutions and City of Helsinki for sponsoring this new feature.


### REST API Security Improvement


New REST call allowing a users to modify his/her password (no UI for it yet, sorry). Here is an example cURL command:

    
    curl -i -XPUT -H "Content-type: text/xml" -d '<passwd><newPassword>qqq</newPassword></passwd>' -u userName:currentPassword http://host:8080/geoserver/rest/security/self/passwordInviato il:09:48Da:Emanuele Tajariol


Thanks to Emanuele Tajariol and GeoSolutions for this work.


## Extensions


GeoServer extensions are available as optional downloads adding capabilities to the core application.


### YSLD module graduated to supported


The YSLD styling language has been graduated to supported land, becoming an official extension. YSLD is a YAML based language which closely matches the structure of SLD, and the internal data model that GeoServer’s renderer uses. Here is an example from the YSLD Cook Book:

    
    <span class="l-Scalar-Plain">title</span><span class="p-Indicator">:</span> <span class="s">'YSLD</span> <span class="s">Cook</span> <span class="s">Book:</span> <span class="s">Simple</span> <span class="s">Line'</span>
    <span class="l-Scalar-Plain">feature-styles</span><span class="p-Indicator">:</span>
    <span class="p-Indicator">-</span> <span class="l-Scalar-Plain">name</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">name</span>
      <span class="l-Scalar-Plain">rules</span><span class="p-Indicator">:</span>
      <span class="p-Indicator">-</span> <span class="l-Scalar-Plain">symbolizers</span><span class="p-Indicator">:</span>
        <span class="p-Indicator">-</span> <span class="l-Scalar-Plain">line</span><span class="p-Indicator">:</span>
            <span class="l-Scalar-Plain">stroke-color</span><span class="p-Indicator">:</span> <span class="s">'#000000'</span>
            <span class="l-Scalar-Plain">stroke-width</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">3
    </span>


Compared to SLD it sports a similar structure, but in a more compact and readable syntax. High-level elements are optional, so the same example can be expressed in a more compact format:

    
    <span class="l-Scalar-Plain">line</span><span class="p-Indicator">:</span>
    <span class="l-Scalar-Plain">  stroke-color</span><span class="p-Indicator">:</span> <span class="s">'#000000'</span>
    <span class="l-Scalar-Plain">  stroke-width</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">3</span>


Similarly to SLD and CSS, the user guide contains both a [reference](http://docs.geoserver.org/stable/en/user/styling/ysld/reference/index.html) and a [cookbook](http://docs.geoserver.org/stable/en/user/styling/ysld/cookbook/index.html) to get you started. There is also a [styling workshop](http://docs.geoserver.org/latest/en/user/styling/workshop/index.html) with both CSS and YSLD examples (including an important example for [converting your SLD styles to YSLD](http://docs.geoserver.org/latest/en/user/styling/workshop/ysld/done.html#converting-to-ysld)).

Thanks to Boundless for contributing this module and pushing it to supported status.


### Vector tiles module graduated to supported


The vector tiles community module has been graduated to extension status. The module allows generation of vector tiles out of WMS and WMTS requests, using SLD to filter the contents of the tile at the requested scale. Supported vector tiles formats are MVT (MapBox Vector Tile), GeoJSON vector tiles, and TopoJSON vector tiles.

This allow for much more compact data transfers, reduced tile caches thanks to overzooming support, and allows the client to control styling. Here is an example of the client rendering a world map as a vector tile, and highlighting a specific area by attribute:

[![vectortileoutputafrica](http://blog.geoserver.org/wp-content/uploads/2017/02/vectortileoutputafrica.png)](http://blog.geoserver.org/wp-content/uploads/2017/02/vectortileoutputafrica.png)

Hop on the [documentation to get more information ](http://docs.geoserver.org/latest/en/user/extensions/vectortiles/index.html)about this extension, along with a couple of presentations highlighting vector tile usage.

Thanks to Boundless for contributing this module and pushing it to supported status.


## Upgrade Notes


This section highlights functionality that has changed from prior releases.


### SLD 1.0 LabelPlacement fix default AnchorPoint


An [issue with SLD 1.0 rendering](https://osgeo-org.atlassian.net/browse/GEOT-5632) has been fixed, this may affect the appearance of you WMS GetMap results.

This issue occurs in the following TextSymbolizer example, where the anchorPoint for the label placement has not been defined.

    
    <sld:TextSymbolizer>
     <sld:Label><ogc:PropertyName>name</ogc:PropertyName></sld:Label>
    </sld:TextSymbolizer>


As shown below GeoServer 2.10 and earlier used the incorrect default anchor point. The default anchor point of of x=0.5 and y=0.5 generated a label at the geometry centroid which is more suitable to PolygonSymbolizers.

[caption id="attachment_2826" align="aligncenter" width="300"][![label_anchor_before](http://blog.geoserver.org/wp-content/uploads/2017/03/label_anchor_before-300x221.png)](http://blog.geoserver.org/wp-content/uploads/2017/03/label_anchor_before.png) Prior TextSymbolizer anchor point default[/caption]

For GeoServer 2.11 this mistake has been corrected, the default anchor point is x=0.0 and y=0.5 which is more suited to PointSymbolizers.

[caption id="attachment_2828" align="aligncenter" width="300"][![TextSymbolizer correct anchor point](http://blog.geoserver.org/wp-content/uploads/2017/03/label_anchor_after-300x222.png)](http://blog.geoserver.org/wp-content/uploads/2017/03/label_anchor_after.png) Correct TextSymbolizer anchor point default[/caption]

**Alternative: Provide a Label Placement**

To avoid making use of the default anchor point we recommend defining an label placement. For PolygonSymbolizers the following example is appropriate:

    
    <sld:TextSymbolizer>
     <sld:Label><ogc:PropertyName>name</ogc:PropertyName></sld:Label>
     <sld:LabelPlacement>
      <sld:PointPlacement>
       <sld:AnchorPoint>
        <sld:AnchorPointX>0.5</sld:AnchorPointX>
        <sld:AnchorPointY>0.5</sld:AnchorPointY>
       </sld:AnchorPoint>
      </sld:PointPlacement>
     </sld:LabelPlacement>
    </sld:TextSymbolizer>


For PointSymbolizer we recommend both an anchor point and a displacement (to prevent overlap with the location graphic).

    
    <sld:TextSymbolizer>
     <sld:Label><ogc:PropertyName>name</ogc:PropertyName></sld:Label>
     <sld:LabelPlacement>
      <sld:PointPlacement>
       <sld:AnchorPoint>
        <sld:AnchorPointX>0.0</sld:AnchorPointX>
        <sld:AnchorPointY>0.5</sld:AnchorPointY>
       </sld:AnchorPoint>
       <sld:Displacement>
        <sld:DisplacementX>8.0</sld:DisplacementX>
        <sld:DisplacementY>0.0</sld:DisplacementY>
       </sld:Displacement>
      </sld:PointPlacement>
     </sld:LabelPlacement>
    </sld:TextSymbolizer>


These changes explicitly centre polygon labels, and offset point labels (with an appropriate displacement allowing their graphic to be visible).

[caption id="attachment_2827" align="aligncenter" width="300"][![label_anchor_defined](http://blog.geoserver.org/wp-content/uploads/2017/03/label_anchor_defined-300x221.png)](http://blog.geoserver.org/wp-content/uploads/2017/03/label_anchor_defined.png) TextSymbolizer with defined anchor point[/caption]

**Alternative: Restore the Previous Default**

If you need to “restore” the previous incorrect default value, add the startup parameter:

    
     -Dorg.geotools.renderer.style.legacyAnchorPoint=true


This setting is provided as an alternative to ease the upgrading process.


## And more ...


There are many improvements to look at in the release notes, cherry picking a few here:



 	
  * Support JSON encoded exceptions for WFS 2.0 too (was already available for 1.0 and 1.1)

 	
  * Drastically reduced output size for WMS PDF output format, when using a graphic fill based on repeated marks or SVG symbols

 	
  * Improved scalability when using "advanced projection handling" thanks to a new implementation of SoftValueHashMap (used as a cache by the referencing subsystem)

 	
  * Better transparency handling of NODATA and ROI (Region Of Interest)

 	
  * Fixes in computation of global disk quota (if you find you have a negative number, upgrade, wipe out the quota database, and restart)




## About GeoServer 2.11


Articles, docs, blog posts and presentations:



 	
  * [OAuth2 for GeoServer](http://www.geo-solutions.it/blog/oauth2-geoserver/) (GeoSolutions)

 	
  * [YSLD](http://docs.geoserver.org/stable/en/user/styling/ysld/index.html) has graduated and is now available for download as a supported extension

 	
  * [Vector tiles](http://docs.geoserver.org/latest/en/user/extensions/vectortiles/index.html) has graduate and is now available for download as an extension

 	
  * The rendering engine continues to improve with underlying labels now available as a vendor option

 	
  * A new “[opaque container](http://docs.geoserver.org/latest/en/user/data/webadmin/layergroups.html#layer-group-modes)” layer group mode can be used to publish a basemap while completely restricting access to the individual layers.

 	
  * Layer group security restrictions are now available

 	
  * [Latest in performance optimizations in GeoServer](http://www.geo-solutions.it/blog/performance-geoserver/) (GeoSolutions)

 	
  * Improved lookup of EPSG codes allows GeoServer to automatically match EPSG codes making shapefiles easier to import into a database (or publish individually).


