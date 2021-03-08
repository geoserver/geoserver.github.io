---
author: iant
comments: false
date: 2020-04-21 15:17:39+00:00
layout: post
link: http://blog.geoserver.org/2020/04/21/geoserver-2-17-0-released/
slug: geoserver-2-17-0-released
title: GeoServer 2.17.0 Released
wordpress_id: 3125
tags:
- release
---




We are happy to announce GeoServer 2.17.0 release candidate is available for testing. Downloads are [available](http://geoserver.org/release/2.17.0/) ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.0/geoserver-2.17.0-bin.zip/download) and [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.0/geoserver-2.17.0-war.zip/download)) along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.0/geoserver-2.17.0-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.17.0/extensions/).







This is a GeoServer release candidate made in conjunction with GeoTools 23.0 and GeoWebCache 1.17.0.







This is an exciting release and a lot of great new functionality has been added. 







## Fixes since Release Candidate







### Bugs







  * [[GEOS-5188](https://osgeo-org.atlassian.net/browse/GEOS-5188)] - LegendDecoration does not respect target size
  * [[GEOS-9537](https://osgeo-org.atlassian.net/browse/GEOS-9537)] - Restore plugin is not able to correctly restore styles anymore
  * [[GEOS-9551](https://osgeo-org.atlassian.net/browse/GEOS-9551)] - Rendering Transformation can cause bad rendering on reprojection to 3995
  * [[GEOS-9559](https://osgeo-org.atlassian.net/browse/GEOS-9559)] - GeofenceAccessManager fails to cut geometries in coverages
  * [[GEOS-9566](https://osgeo-org.atlassian.net/browse/GEOS-9566)] - Migrate to repo.osgeo.org repository
  * [[GEOS-9567](https://osgeo-org.atlassian.net/browse/GEOS-9567)] - [Backup/Restore] Rest Controller not able to backup secured resources






### Improvement







  * [[GEOS-9512](https://osgeo-org.atlassian.net/browse/GEOS-9512)] - RasterDownload on Heterogeneous CRS Mosaic: avoid reprojection of granules having same CRS as the target CRS.
  * [[GEOS-9543](https://osgeo-org.atlassian.net/browse/GEOS-9543)] - GeoServer REST documentation: Parser error duplicated mapping key






## MBStyle module graduated to extension







The MBStyles module has received a deep review and many visual differences have been resolved, to the point that it can now display properly some of the OpenMapTiles styles as-is, with good fidelity, here is an example:





![](/img/uploads/OpenMapTilesBright.png)





The module has also graduated to extension status, so you will now find it in all releases.







## MBTiles community module reading vector tiles







The above map has been rendered not with one functionality, but two! Did you know one can put vector tiles in a MBTiles file? The community module [mbtiles-store](https://docs.geoserver.org/stable/en/user/community/mbtiles/index.html) can read both raster and vector tiles now, and will serve the tiles for vector rendering.







It makes the perfect match with the MBStyle module, one can read vector tiles and render them using the styles they were designed for. Want to give it a quick try? Go to the OpenMapTiles web site and [download an area of interest](https://openmaptiles.com/downloads/planet/), for personal usage, and configure all layers. Then grab the [osm-bright-gl-style](https://github.com/openmaptiles/osm-bright-gl-style/blob/master/style.json), set it up, and configure it as a ["style group" layer group type](https://docs.geoserver.org/stable/en/user/data/webadmin/layergroups.html#edit-a-layer-group). Done:





![](/img/uploads/styleGroup.png)





## Web resource extension







Ever had to fiddle with the data directory on a remote server, maybe trying to setup the control-flow configuration, or upload a Freemarker template? It can be annoying business, one often needs some sort of side access, like SSH. The [Resource Browser](https://docs.geoserver.org/latest/en/user/configuration/tools/resource/index.html) module, freshly graduated into a supported extension, comes to the rescue, providing a tools page where administrators can browse the data directory, inspect files, edit them, and upload new ones too:





![](/img/uploads/stles.png)



![](/img/uploads/editor.png)





## Manage authorization from each resource







Ever added a new layer and forgot to setup security for it? It's a common occurrence, when the configuration of the layers and its security are done in different pages.







GeoServer 2.17 has a new "Security" tab in each page, allowing you to setup the security for a given resource directly in its configuration page:





![](/img/uploads/layerSecurity-1024x435.png)





Edit security settings there, and the[ layer security configuration](https://docs.geoserver.org/latest/en/user/security/layer.html#security-layer) will be updated as a consequence. The same goes for workspaces and layer groups.







## Track last change of each resource







GeoServer 2.17 tracks, and allows to show, the date of creation and last modification of major configuration resources, such as workspaces, stores and layers, in their respective list page.







Turn it on in the server configuration page, and see the result in list pages:







![](/img/uploads/enableDates.png)





![](/img/uploads/showDates.png)





This new setting is off by default, you'll have to go and explicitly turn it on if you care to see the dates.







## Map rendering improvements







GeoTools label "shield" support already allowed to put together a graphic along with a label, with the goal of supporting road label shields. GeoServer 2.17.0 includes the ability to lay them out separately, so that the mark and labels are not centered with each other but, for example, one above the other. This allows to setup point markers that appear only as long as their label is showing up too:







![](/img/uploads/Selezione_999035.png)







![](/img/uploads/Selezione_999036.png)







It's also possible to setup a background color for the map at the style level, using a new Background element inside UserStyle. Background is a fill:






    
    <em><?</em><strong>xml version="1.0" encoding="UTF-8"</strong><em>?></em><<strong>sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" xmlns:ogc="http://www.opengis.net/ogc" version="1.0.0"</strong>>
      <<strong>sld:NamedLayer</strong>>
        <<strong>sld:Name</strong>>Sea color background</<strong>sld:Name</strong>>
        <<strong>sld:UserStyle</strong>>
          <<strong>sld:Name</strong>>Background sample</<strong>sld:Name</strong>>
          <<strong>sld:Background</strong>>
            <<strong>sld:CssParameter name="fill"</strong>>#F2EFE9</<strong>sld:CssParameter</strong>>
          </<strong>sld:Background</strong>>
          <<strong>sld:FeatureTypeStyle</strong>>
            <<strong>sld:Rule</strong>>
               ...
            <<strong>/sld:Rule</strong>>  
        </<strong>sld:UserStyle</strong>>
      </<strong>sld:NamedLayer</strong>>
    </<strong>sld:StyledLayerDescriptor</strong>>







![](/img/uploads/Selezione_999214.png)







Traditionally one can render multi-script labels by specifying a long list of family names in the "font-family", e.g.:






    
    <<strong>sld:Font</strong>>
      <<strong>sld:CssParameter name="font-family"</strong>>Noto Sans Regular</<strong>sld:CssParameter</strong>>
      <<strong>sld:CssParameter name="font-family"</strong>>Noto Sans Adlam Regular</<strong>sld:CssParameter</strong>>
      <<strong>sld:CssParameter name="font-family"</strong>>Noto Sans Adlam Unjoined Regular</<strong>sld:CssParameter</strong>>
      <<strong>sld:CssParameter name="font-family"</strong>>Noto Sans Armenian Regular</<strong>sld:CssParameter</strong>>
      <<strong>sld:CssParameter name="font-family"</strong>>Noto Sans Balinese Regular</<strong>sld:CssParameter</strong>>
       ...
    </<strong>sld:Font</strong>>







If the font names all share a common prefix, it's now possible to be more concise and just use a function instead, specifying the common base name, letting GeoServer find all possible variants e.g.:






    
    <<strong>sld:Font</strong>>
      <<strong>sld:CssParameter name="font-family"</strong>>
        <<strong>ogc:Function name="fontAlternatives"</strong>>
          <<strong>ogc:Literal</strong>>Noto Sans</<strong>ogc:Literal</strong>>
        </<strong>ogc:Function</strong>>
      </<strong>sld:CssParameter</strong>>
    ...
    </<strong>sld:Font</strong>>
    







As a further labelling related feature, when performing conflict resolution the map renderer can now try to shrink the size of labels in search of a place to fit them. The new vendor option is called "fontShrinkSizeMin" and represents the minimum size to use.  Here is an example, the two polygons share the same TextSymbolizer definition, in one the label size has been reduced to allow the label to fit:







![](/img/uploads/Selezione_999216.png)







Moving to line symbolizers, it's now possible to drape a linear mark along a line. Before, it was just possible to repeat it along a line, but the output would not have looked continuous, especially at turns. Now, if you have a mark that starts and ends at the same height, it can literally be made continuous along the line, e.g. using this style:






    
           <<strong>LineSymbolizer</strong>><br>         <<strong>Stroke</strong>><br>           <<strong>GraphicStroke</strong>><br>             <<strong>Graphic</strong>><br>               <<strong>Mark</strong>>                                  <br>      <<strong>WellKnownName</strong>>wkt://LINESTRING (0 0, 0 -0.5, 0.5 -0.5, 0.5 0.5, 1 0.5, 1 0)</<strong>WellKnownName</strong>><br>                 <<strong>Stroke</strong>><br>                   <<strong>CssParameter </strong><strong>name</strong><strong>="stroke"</strong>>0xFF0000<br>                   </<strong>CssParameter</strong>><br>                   <<strong>CssParameter </strong><strong>name</strong><strong>="stroke-width"</strong>>2</<strong>CssParameter</strong>><br>                   <<strong>CssParameter </strong><strong>name</strong><strong>="stroke-linecap"</strong>>round</<strong>CssParameter</strong>><br>                 </<strong>Stroke</strong>>                                           <br>               </<strong>Mark</strong>>            <br>               <<strong>Size</strong>>20</<strong>Size</strong>>                            <br>             </<strong>Graphic</strong>>                <br>           </<strong>GraphicStroke</strong>>            <br>         </<strong>Stroke</strong>>       <br><<strong>VendorOption </strong><strong>name</strong><strong>="markAlongLine"</strong>>true</<strong>VendorOption</strong>>             <br>       </<strong>LineSymbolizer</strong>><br>







Results in the following (you cannot see at first it, but the size of the mark can be slightly altered to fit the segments length, and if it's not enough, it gets cut and reconnected):







![](/img/uploads/markAlongLine_sqaure_all_angles.png)







As a final note, there has been a number of small improvements to rendering performance, that will be especially visible when rendering a complex map, with many rules, features to be rendered, and labels (you know, like OpenStreetMap).







## Enabled/advertised for layer groups







Up to now, the ability to enable/disable and advertise was limited to layers. No more, in GeoServer 2.17 you can now do the same with layer groups:







![](/img/uploads/enabledAdvertise.png)







## Custom WMS dimension for vector layers too







GeoServer supports standard WMS dimensions, TIME and ELEVATION, on both raster and vector datasets. However, user defined dimensions, also known as custom dimensions, were supported only by raster layers (typically, image mosaics). You can now configure them on vector layers as well:







![](/img/uploads/vector_elevation_time.png)







## WMS cascading improvements







The WMS cascading functionality has seen several improvements, including:







  * Possibility to choose the cascading format, expose the remote layer styles, while choosing which ones to advertise.
  * Possibility to configure min/max scale denominators for cascaded layers, as well as restrict cascading to the  bounding box declared in the capabilities document.




![](/img/uploads/cascading.png)





## GeoWebCache love







Significant improvements have been made to GeoWebCache and its integration with GeoServer, including:







  * Much better startup performance when integrated in GeoServer, the time to load the tiled layers configuration is a fraction of what it used to be.
  * Much faster tile layer listing in the GeoServer "tile layers" page
  * File system tile layout can be configured between classic (small folders), XYZ and TMS (for static cache generation)
  * Better control over failed tile seed operations. Seeding threads used to stop at the first failure, now error tolerance can be configured on the single thread and across the seed job:




![](/img/uploads/Selezione_999213.png)





## JSON-LD community module







[GeoServer 2.16](http://blog.geoserver.org/2019/09/18/geoserver-2-16-released/) introduced a number of improvements in the WFS GeoJSON complex feature output. This release adds instead support for [JSON-LD, as a community module](https://docs.geoserver.org/latest/en/user/community/json-ld/index.html).







Unlike the GeoJSON approach, based on automatic conventions, the JSON-LD module is driven by [configuration, a JSON file](https://docs.geoserver.org/latest/en/user/community/json-ld/configuration.html) giving the output format directives on how to encode the output based on complex input features.







The output format is available for both the WFS and new OGC Features API modules







## OGC API community module updates







The [OGC API community module](https://docs.geoserver.org/latest/en/user/community/ogc-api/index.html#installing-the-geoserver-ogc-api-module) delivers latest updates for OGC API services:







  * An up to date OGC Features API, updated to the last official release, with draft extensions to support filtering and multiple CRSs, along with tiling vector data
  * A OGC Tiles API, providing tiled collections in both rendered (maps, pngs, jpeg) and data (vector tiles) format, with draft extension to support on the fly filtering
  * A draft implementation of the OGC Styles API, supporting description and discovery of styles in multiple formats, and links from collections to their relevant styles, and back.
  * Two more experimental APIs, image API to manage image mosaic contents, and changeset API to figure out which areas of a tiled collection changed as a result of changes to the image mosaic backing them.






Development is still heavily ongoing, and specs are still evolving at a fast pace, but we invite you to try them out, enjoy their simplicity, and contribute to their evolution.







## FlatGeoBuf community module







Are you using GML or GeoJSON to fetch data client side, and you're not happy with the data transfer performance? You need to actually use the geometries client side, for editing, analysis and topological operations, and would like to avoid the clipping done in vector tiles?







Then you are the perfect candidate to try out our new [FlatGeoBuf output format community module](https://docs.geoserver.org/latest/en/user/community/flatgeobuf/installing.html). FlatGeoBuf is "a performant binary encoding for geographic data based on flatbuffers that can hold a collection of Simple Features including circular interpolations as defined by SQL-MM Part 3." While new, it's making its way in several open source projects, it's supported by the latest versions of GDAL/OGR and easy to embed in both OpenLayers and Leaflet. The format can also be streamed out, and rendered progressively client side, like in [this OpenLayers demo](https://bjornharrtell.github.io/flatgeobuf/examples/openlayers/).







![](/img/uploads/Selezione_999217.png)[This is just a screenshot, please follow the link to play with it live!](https://bjornharrtell.github.io/flatgeobuf/examples/openlayers/)







## And more!







There are several other new features and improvements, including:







  * Curved geometries are now supported in SQL Server too, in addition to the existing support for PostGIS and Oracle.
  * Support for [workspace specific stored queries](https://github.com/geoserver/geoserver/wiki/GSIP-183).
  * [java.util.Math has been exposed in Freemarker templates](https://github.com/geoserver/geoserver/wiki/GSIP-181).
  * It's now possible to [contribute an extension without signing an OSGeo CLA](https://github.com/geoserver/geoserver/wiki/GSIP-186), as long as it's self-contained and has a license compatible with GeoServer own.
  * The [ncWMS compatibility community module](https://docs.geoserver.org/latest/en/user/community/ncwms/index.html) has been improved, allowing to query a time list or a time range in GetTimeSeries, as well as ignoring NODATA pixels.
  * When renaming the layers, the pertinent authorization rules will be updated to match.
  * GeoTools has a new "ElasticGeo" community module, which allows to read data from ElasticSearch geo extensions. It still needs a nightly build packaging in Geoserver, volunteers welcomed.
  * GeoPackage can now be used with WMS and WFS time support.
  * Stand alone GeoWebCache has a new Swift blob store module, the integration with GeoServer would require custom packaging for it, volunteers welcomed.






Find out more in the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16782).







## About GeoServer 2.17







Additional information on GeoServer 2.17 series:







  * FOSDEM GeoServer Orientation presentation ([slides](https://www.slideshare.net/jgarnett/geoserver-orientation)|[video](https://ftp.fau.de/fosdem/2020/AW1.126/geoserver.mp4))
  * [Full OSM data directory](https://www.geosolutionsgroup.com/blog/geoserver-osm-styles-full-data-directory-available/) for GeoServer available on GitHub
  * [Code of Conduct](https://github.com/geoserver/geoserver/blob/master/CODE_OF_CONDUCT.md)
  * Release notes ([2.17.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16782), [2.17-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16766))








