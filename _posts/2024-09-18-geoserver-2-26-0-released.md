---
author: Jody Garnett
date: 2024-09-18
layout: post
title: GeoServer 2.26.0 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_226
version: 2.26.0
jira_version: 16916
--- 

GeoServer [2.26.0](/release/2.26.0/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.0/geoserver-2.26.0-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.0/geoserver-2.26.0-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.0/GeoServer-2.26.0-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.0/geoserver-2.26.0-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26.0/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 2.26.0 is made in conjunction with GeoTools 32.0, GeoWebCache 1.26.0, ImageIO-EXT 1.4.13, and JAI-EXT 1.1.27.

Thanks to Peter Smythe and Jody Garnett for making this release and everyone who has helped out during this release cycle.

## Nightly build testing

This release cycle we asked our new user forum to test a nightly build, as we did not have capacity to make a release candidate.

Thanks to Daniel Calliess for responding during our public testing cycle. Daniel noted that he had to add `/geoserver/webresources` to his proxy for the OpenLayers preview to function. This change is due to an ongoing effort to move all CSS and JS to external resources allowing [Content Security Policy](https://content-security-policy.com/) headers to be introduced.

## Security Considerations

This release addresses security vulnerabilities and is considered is a recommended upgrade for production systems.

* CVE-2024-45748 High (to be disclosed)
* [CVE-2024-34711](https://github.com/geoserver/geoserver/security/advisories/GHSA-mc43-4fqr-c965) Improper ENTITY_RESOLUTION_ALLOWLIST URI validation in XML Processing (SSRF) (High 7.3)
* [CVE-2024-35230](https://github.com/geoserver/geoserver/security/advisories/GHSA-6pfc-w86r-54q6): Welcome and About GeoServer pages communicate version and revision information (Moderate 5.3)
*  [GEOS-11400](https://osgeo-org.atlassian.net/browse/GEOS-11400) About Page Layout and display of build information

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

## Java 17 Support

The binary distribution and the Windows installer now work with Java 17 (the war file already did).
Thanks to Andrea Aime and everyone who worked on testing this in different environments.

![](/img/posts/2.26/java17.png)

* [GEOS-11467](https://osgeo-org.atlassian.net/browse/GEOS-11467) Update Marlin, make the bin package compatible with Java 17

## Search improvement

A small but fun change for the layer preview - it is now easier to find just the layer you are looking for using quotes to isolate an individual word.

* [GEOS-11351](https://osgeo-org.atlassian.net/browse/GEOS-11351) Exact term search in the pages' filters

## Extensive MapML Improvements

Thanks to Natural Resources Canada for sponsoring an extensive set improvements for the MapML extension (carried out by a group of GeoSolutions devs, Andrea Aime, Daniele Romagnoli and Joseph Miller):

![](/img/posts/2.26/mapml.png)

* [GEOS-11322](https://osgeo-org.atlassian.net/browse/GEOS-11322) MapML WMS Vector Representation include query filter
* [GEOS-11324](https://osgeo-org.atlassian.net/browse/GEOS-11324) MapML WMS Vector Representation Style Classes
* [GEOS-11337](https://osgeo-org.atlassian.net/browse/GEOS-11337) Support feature tiles in MapML
* [GEOS-11349](https://osgeo-org.atlassian.net/browse/GEOS-11349) MapML Use WMS Resource Consumption Limit to specify max image size
* [GEOS-11461](https://osgeo-org.atlassian.net/browse/GEOS-11461) Enable MapML Viewer output for WFS getFeature.
* [GEOS-11486](https://osgeo-org.atlassian.net/browse/GEOS-11486) Adding custom dimensions to MapML
* [GEOS-11528](https://osgeo-org.atlassian.net/browse/GEOS-11528) Update MapML viewer to latest release 0.14.0
* [GEOS-11471](https://osgeo-org.atlassian.net/browse/GEOS-11471) Remove Sharding configuration support from MapML

## Demo Requests page rewritten

The Demo Request page has been rewritten to use JavaScript to issue POST examples. This provides a much better user experience:

* **Show Result** lists the response headers to be viewed along side the returned result (with an option for XML pretty printing).
* **Show Result in a New Page** is available to allow your browser to display the result.

![](/img/posts/2.25/demo-request.png)

![](/img/posts/2.25/demo-response.png)

The **WCS Request Builder** and **WPS Request Builder** demos now have the option to show their results in Demo Requests page. Combined these changes replace the previous practice of using an iframe popup, and have allowed the **TestWfsPost** servlet to be removed.

For more information please see the [Demo requests](https://docs.geoserver.org/latest/en/user/configuration/demos/index.html#demos-demorequests) in the User Guide.

Thanks to David Blasby (GeoCat) for these improvements, made on behalf of the GeoCat Live project.

* [GEOS-11390](https://osgeo-org.atlassian.net/browse/GEOS-11390) Replace TestWfsPost with Javascript Demo Page

## Raster Attribute Table Extension

A new extension is available that takes advantage of the GDAL Raster Attribute Table (RAT). This data structure provides a way to associate attribute information for individual pixel values within the raster. This provides a table that links each cell value in the raster to one or more attributes on the fly.

![](/img/posts/2.25/rat-ui.png)

![](/img/posts/2.25/rat-map.png)

Thanks to Andrea Aime (GeoSolutions) for the development and NOAA for sponsoring this new capability. Please see the user guide [Raster Attribute Table support](https://docs.geoserver.org/latest/en/user/extensions/rat/index.html) for more information.

* [GEOS-11376](https://osgeo-org.atlassian.net/browse/GEOS-11376) Graduate Raster Attribute Table to extension

## GeoCSS improvements

GeoCSS can now perform scale dependent rendering by the zoom level, assuming web mercator by default, but allowing the configuration of a different gridset as well. It's also possible to create multi-layer styles and use them as style groups.

```css
@mode 'Flat';
@TileMatrixSet 'WorldCRS84Quad'

tiger:poly_landmarks {

  /* @title parks and green spaces */
  [CFCC in ('D82', 'D32', 'D84', 'D85')] {
    fill: #B4DFB4;
    stroke: #88B588;
  }; 
  …
}

tiger:tiger_roads [@z > 12] {
  stroke: #666666, #FFFFFF;
  stroke-width: 6, 4;
  z-index: 1, 2;
  …
}

…
```

Thanks to Andrea Aime (GeoSolutions) for this work, performed in preparation for the FOSS4G-NA 2024 vector tiles workshop.

* [GEOS-11495](https://osgeo-org.atlassian.net/browse/GEOS-11495) Support multi-layer output in CSS
* [GEOS-11515](https://osgeo-org.atlassian.net/browse/GEOS-11515) Add support for zoom level rule filtering in CSS
* [GEOS-11414](https://osgeo-org.atlassian.net/browse/GEOS-11414) Adding css-uniqueRoleName

## GeoPackage QGIS Compatibility Improvements

A number of issues affecting interoperability with QGIS have been addressed:

GeoPackage extension output could contain field types that are not supported by GDAL.
It turns out the GeoPackage export was picking up some of the file type information intended for PostGIS
resulting output that could not be read by other programs such as QGIS.

We were also able to fix up the TIMESTAMP information representation as DATETIME, making the file format timezone agnostic as intended.

Thanks to David Blasby (GeoCat) for these fixes made on behalf of Zeeland and South Holland.

* [GEOS-11416](https://osgeo-org.atlassian.net/browse/GEOS-11416) GeoPackage output contains invalid field types when exporting content from PostGIS

## Geostationary satellite AUTO code

``AUTO:97004`` has been introduced as a new vendor extension to WMS AUTO codes. It implements the geostastionary satellite project and allows to change the central meridian as part of the GetMap request.

![](/img/posts/2.26/auto97004.png)

Thanks to Andrea Aime (GeoSolutions) for this work, and Eumetsat for sponsoring it.

## labelPoint function improved

The ``labelPoint`` function has been improved with more precise calculation of the polygon label points, and not requiring to specify a tolerance any longer. This helps get better maps, especially with tiling enabled (fixed labelling point no matter which tile is requested):

```xml
  <sld:TextSymbolizer>
    <sld:Geometry>
      <ogc:Function name="labelPoint">
        <ogc:PropertyName>the_geom</ogc:PropertyName>
      </ogc:Function>
    </sld:Geometry>
  </sld:TextSymbolizer>  
```

![](/img/posts/2.26/polyLabelBefore.png)
![](/img/posts/2.26/polyLabelAfter.png)

Thanks to Andrea Aime (GeoSolutions) for this work, performed in preparation for the FOSS4G-NA 2024 vector tiles workshop.

## Improved vector tiles generation

A few new vendor options have been added in GeoServer, that control how vector tiles are built, with the objective of producing smaller, faster, more useful vector tiles.

* ``vt-attributes``: comma separated list of attributes included in the vector tile
* ``vt-labels``: when true, generates a sidecar ``-label`` layer for polygons, with the label point of the polygon (vector tile clients generally cannot produce a good label placement otherewise)
* ``vt-label-attributes``:: attributes included in the label point layer
* ``vt-coalesce``: if true, takes all features in the tile sharing the same attribute values, and coalesces their geometries into a single multi-geometry.

Here is an example style using the above vendor options, in GeoCSS:

```css
@mode "Flat";

tiger:poly_landmarks {
  fill: gray;
  vt-attributes: 'CFCC,LANAME';
  vt-labels: true;
}

tiger:tiger_roads [@z > 11] {
  stroke: black;
  vt-attributes: 'NAME';
  vt-coalesce: true;
}

tiger:poi [@z > 12] {
  mark: symbol(square);
}
```

The GWC layer preview has also been improved to show the vector tile feature attributes on hover:

![](/img/posts/2.26/vt-preview.png)

Thanks to Andrea Aime (GeoSolutions) for this work, performed in preparation for the FOSS4G-NA 2024 vector tiles workshop.

## New image mosaic merge behaviors, MIN and MAX

These two new image mosaic merge modes activate when multiple images overlap with each other, choosing respectively the minimum and maximum value amongst the super-imposed pixels.

![](/img/posts/2.26/mosaic-merge-max.png)

Thanks to Andrea Aime for the work, and the US National Research Laboratory for sponsoring it.

## OGC APIs feeling "at home"

OGC API modules now nicely slot into the home page in the corresponding functional section, e.g., since both provide raw vector data, both OGC API Features and WFS show up in the same area:

![](/img/posts/2.26/ogcapi_home.png)

Thanks to David Blasby (GeoCat) for this work.

## Other community module updates

The "Data Directory loader", by Gabriel Roldan (Camptocamp), is a replacement data directory loader, reading the XML configuration files at startup. It has been optimized to achieve better parallelism and be more efficient over network file systems. It can be found amongst the [nightly builds](https://build.geoserver.org/geoserver/2.26.x/community-latest/geoserver-2.26-SNAPSHOT-datadir-catalog-loader-plugin.zip), it's a simple drop in replacement, just unzip the plugin in ``WEB-INF/lib`` and restart. Let us know how it works for you.


The [WFS HTML Freemaker output format](https://docs.geoserver.org/latest/en/user/community/wfs-freemarker/index.html) is a community module generating HTML in response to GetFeature, using the GetFeatureInfo Freemarker templates.

The [graticules module](https://docs.geoserver.org/latest/en/user/community/graticules/index.html) is the combination of a data store and a rendering transformation allowing to generate graticules at multiple resolutions, and optionally placing the graticul labels at the map borders.

![](/img/posts/2.26/graticules.png)

## 2024 Roadmap Progress

* [GEOS-11271](https://osgeo-org.atlassian.net/browse/GEOS-11271) Upgrade spring-security to 5.8

## Release notes

New Feature:

* [GEOS-11322](https://osgeo-org.atlassian.net/browse/GEOS-11322) MapML WMS Vector Representation include query filter
* [GEOS-11324](https://osgeo-org.atlassian.net/browse/GEOS-11324) MapML WMS Vector Representation Style Classes
* [GEOS-11352](https://osgeo-org.atlassian.net/browse/GEOS-11352) REST service for URL checks
* [GEOS-11376](https://osgeo-org.atlassian.net/browse/GEOS-11376) Graduate Raster Attribute Table to extension
* [GEOS-11390](https://osgeo-org.atlassian.net/browse/GEOS-11390) Replace TestWfsPost with Javascript Demo Page
* [GEOS-11414](https://osgeo-org.atlassian.net/browse/GEOS-11414) Adding css-uniqueRoleName

Improvement:

* [GEOS-11271](https://osgeo-org.atlassian.net/browse/GEOS-11271) Upgrade spring-security to 5.8
* [GEOS-11325](https://osgeo-org.atlassian.net/browse/GEOS-11325) Add properties to set additional security headers
* [GEOS-11337](https://osgeo-org.atlassian.net/browse/GEOS-11337) Support feature tiles in MapML
* [GEOS-11338](https://osgeo-org.atlassian.net/browse/GEOS-11338) CapabilityUtil SearchMinMaxScaleDenominator should include support for multiple NamedLayers
* [GEOS-11349](https://osgeo-org.atlassian.net/browse/GEOS-11349) MapML Use WMS Resource Consumption Limit to specify max image size
* [GEOS-11351](https://osgeo-org.atlassian.net/browse/GEOS-11351) Exact term search in the pages' filters
* [GEOS-11369](https://osgeo-org.atlassian.net/browse/GEOS-11369) Additional authentication options for cascaded WMS|WMTS data stores
* [GEOS-11370](https://osgeo-org.atlassian.net/browse/GEOS-11370) Refactor inline JavaScript in the TestWfsPost Page
* [GEOS-11371](https://osgeo-org.atlassian.net/browse/GEOS-11371) Refactor inline JavaScript in the GetMap OpenLayers format
* [GEOS-11379](https://osgeo-org.atlassian.net/browse/GEOS-11379) Refactor inline JavaScript in the OGC API modules
* [GEOS-11400](https://osgeo-org.atlassian.net/browse/GEOS-11400) About Page Layout and display of build information
* [GEOS-11401](https://osgeo-org.atlassian.net/browse/GEOS-11401) Introduce environmental variables for Module Status page
* [GEOS-11427](https://osgeo-org.atlassian.net/browse/GEOS-11427) metadata: "fix all" to support changing config repeatable field
* [GEOS-11443](https://osgeo-org.atlassian.net/browse/GEOS-11443) REST API does not take effect immediately due to 10 minute authentication cache
* [GEOS-11461](https://osgeo-org.atlassian.net/browse/GEOS-11461) Enable MapML Viewer output for WFS getFeature.
* [GEOS-11467](https://osgeo-org.atlassian.net/browse/GEOS-11467) Update Marlin, make the bin package compatible with Java 17
* [GEOS-11477](https://osgeo-org.atlassian.net/browse/GEOS-11477) Add a max and a min merge mode for image mosaics
* [GEOS-11486](https://osgeo-org.atlassian.net/browse/GEOS-11486) Adding custom dimensions to MapML
* [GEOS-11488](https://osgeo-org.atlassian.net/browse/GEOS-11488) Double-Click-to-Copy featurecaption variable reference
* [GEOS-11495](https://osgeo-org.atlassian.net/browse/GEOS-11495) Support multi-layer output in CSS
* [GEOS-11502](https://osgeo-org.atlassian.net/browse/GEOS-11502) Permit resize on user/group/role palette textbox to allow for extra long role names
* [GEOS-11503](https://osgeo-org.atlassian.net/browse/GEOS-11503) Update mongo schemaless DWITHIN to support non-point geometry
* [GEOS-11515](https://osgeo-org.atlassian.net/browse/GEOS-11515) Add support for zoom level rule filtering in CSS
* [GEOS-11526](https://osgeo-org.atlassian.net/browse/GEOS-11526) GeoFence: slow GeoServer response when there are many roles and layergroups
* [GEOS-11527](https://osgeo-org.atlassian.net/browse/GEOS-11527) Add new vector tiles generation options in style body: vt-attributes, vt-coalesce, vt-labels, vt-label-attributes
* [GEOS-11528](https://osgeo-org.atlassian.net/browse/GEOS-11528) Update MapML viewer to latest release 0.14.0
* [GEOS-11531](https://osgeo-org.atlassian.net/browse/GEOS-11531) When coalescing linestrings in vector tiles output, fuse them to create a single long line

Bug:

* [GEOS-7183](https://osgeo-org.atlassian.net/browse/GEOS-7183) Demo request/wcs/wps pages incompatible with HTTPS/PKI
* [GEOS-11202](https://osgeo-org.atlassian.net/browse/GEOS-11202) CAS extension doesn't use global "proxy base URL" setting for service ticket
* [GEOS-11266](https://osgeo-org.atlassian.net/browse/GEOS-11266) csw-iso: missing fields in summary response
* [GEOS-11314](https://osgeo-org.atlassian.net/browse/GEOS-11314) Error in IconService when style has multiple FeatureTypeStyle
* [GEOS-11385](https://osgeo-org.atlassian.net/browse/GEOS-11385) Demo Requests functionality does not honour ENV variable PROXY_BASE_URL
* [GEOS-11416](https://osgeo-org.atlassian.net/browse/GEOS-11416) GeoPackage output contains invalid field types when exporting content from PostGIS
* [GEOS-11422](https://osgeo-org.atlassian.net/browse/GEOS-11422) MapML License Metadata Stored With Incorrect Keys
* [GEOS-11430](https://osgeo-org.atlassian.net/browse/GEOS-11430) CiteComplianceHack not correctly parsing the context
* [GEOS-11446](https://osgeo-org.atlassian.net/browse/GEOS-11446) [INSPIRE] Incorrect behavior for unsupported languages
* [GEOS-11462](https://osgeo-org.atlassian.net/browse/GEOS-11462) 500 error thrown when double adding a user to a group via REST with JDBC user/group services
* [GEOS-11484](https://osgeo-org.atlassian.net/browse/GEOS-11484) DirectRasterRenderer is not respecting advancedProjectionHandling and continuosMapWrapping format_options
* [GEOS-11530](https://osgeo-org.atlassian.net/browse/GEOS-11530) Adding or removing a grid subset in the layer caching tab, causes the grid dropdown to get duplicated

Task:

* [GEOS-11341](https://osgeo-org.atlassian.net/browse/GEOS-11341) Upgrade NetCDF to 5.3.3
* [GEOS-11360](https://osgeo-org.atlassian.net/browse/GEOS-11360) Upgrade Apache POI from 4.1.1 to 5.2.5
* [GEOS-11362](https://osgeo-org.atlassian.net/browse/GEOS-11362) Upgrade Spring libs from 5.3.32 to 5.3.33
* [GEOS-11374](https://osgeo-org.atlassian.net/browse/GEOS-11374) Upgrade Spring version from 5.3.33 to 5.3.34
* [GEOS-11375](https://osgeo-org.atlassian.net/browse/GEOS-11375) GSIP 224 - Individual contributor clarification
* [GEOS-11393](https://osgeo-org.atlassian.net/browse/GEOS-11393) Upgrade commons-io from 2.12.0 to 2.16.1
* [GEOS-11395](https://osgeo-org.atlassian.net/browse/GEOS-11395) Upgrade guava from 32.0.0 to 33.2.0
* [GEOS-11397](https://osgeo-org.atlassian.net/browse/GEOS-11397) App-Schema Includes fix Integration Tests
* [GEOS-11402](https://osgeo-org.atlassian.net/browse/GEOS-11402) Upgrade PostgreSQL driver from 42.7.2 to 42.7.3
* [GEOS-11403](https://osgeo-org.atlassian.net/browse/GEOS-11403) Upgrade commons-text from 1.10.0 to 1.12.0
* [GEOS-11404](https://osgeo-org.atlassian.net/browse/GEOS-11404) Upgrade commons-codec from 1.15 to 1.17.0
* [GEOS-11407](https://osgeo-org.atlassian.net/browse/GEOS-11407) Upgrade jackson from 2.15.2 to 2.17.1
* [GEOS-11464](https://osgeo-org.atlassian.net/browse/GEOS-11464) Update Jackson 2 libs from 2.17.1 to 2.17.2
* [GEOS-11470](https://osgeo-org.atlassian.net/browse/GEOS-11470) Upgrade the version of Mongo driver for schemaless plugin from 4.0.6 to 4.11.2
* [GEOS-11471](https://osgeo-org.atlassian.net/browse/GEOS-11471) Remove Sharding configuration support from MapML
* [GEOS-11472](https://osgeo-org.atlassian.net/browse/GEOS-11472) Upgrade freemarker from 2.3.31 to 2.3.33
* [GEOS-11473](https://osgeo-org.atlassian.net/browse/GEOS-11473) Upgrade guava from 33.2.0 to 33.2.1
* [GEOS-11475](https://osgeo-org.atlassian.net/browse/GEOS-11475) Upgrade commons-codec from 1.17.0 to 1.17.1
* [GEOS-11478](https://osgeo-org.atlassian.net/browse/GEOS-11478) Upgrade commons-lang3 from 3.14.0 to 3.15.0
* [GEOS-11479](https://osgeo-org.atlassian.net/browse/GEOS-11479) Upgrade junit from 4.13.1 to 4.13.2
* [GEOS-11480](https://osgeo-org.atlassian.net/browse/GEOS-11480) Update map fish-print-lib 2.3.1
* [GEOS-11506](https://osgeo-org.atlassian.net/browse/GEOS-11506) Upgrade Spring version from 5.3.37 to 5.3.39 and Spring security from 5.8.13 to 5.8.14
* [GEOS-11508](https://osgeo-org.atlassian.net/browse/GEOS-11508) Update OSHI from 6.4.10 to 6.6.3
* [GEOS-11512](https://osgeo-org.atlassian.net/browse/GEOS-11512) Upgrade jasypt from 1.9.2 to 1.9.3
* [GEOS-11532](https://osgeo-org.atlassian.net/browse/GEOS-11532) Update to JTS 1.20.0
* [GEOS-11533](https://osgeo-org.atlassian.net/browse/GEOS-11533) Update org.apache.commons.vfs2 to 2.9.0
* [GEOS-11544](https://osgeo-org.atlassian.net/browse/GEOS-11544) Upgrade to ImageIO-EXT 1.4.13
* [GEOS-11545](https://osgeo-org.atlassian.net/browse/GEOS-11545) Update to JAI-EXT 1.1.27

For the complete list see [2.26.0](https://github.com/geoserver/geoserver/releases/tag/2.26.0) release notes. 

## Community Updates

Community module development:

* [GEOS-10690](https://osgeo-org.atlassian.net/browse/GEOS-10690) Task manager plugin is missing dependencies
* [GEOS-10824](https://osgeo-org.atlassian.net/browse/GEOS-10824) gs-flatgeobuf extension can clash with "directory of shapefiles" datastores
* [GEOS-11331](https://osgeo-org.atlassian.net/browse/GEOS-11331) OAuth2 can throw a " java.lang.RuntimeException: Never should reach this point"
* [GEOS-11358](https://osgeo-org.atlassian.net/browse/GEOS-11358) Feature-Autopopulate Update operation does not apply the Update Element filter
* [GEOS-11381](https://osgeo-org.atlassian.net/browse/GEOS-11381) Error in OIDC plugin in combination with RoleService
* [GEOS-11412](https://osgeo-org.atlassian.net/browse/GEOS-11412) Remove reference to JDOM from JMS Cluster (as JDOM is no longer in use)
* [GEOS-11445](https://osgeo-org.atlassian.net/browse/GEOS-11445) OGCAPI ServiceDescriptors
* [GEOS-11466](https://osgeo-org.atlassian.net/browse/GEOS-11466) move reusable elements of the graticule plugin to GeoTools 
* [GEOS-11469](https://osgeo-org.atlassian.net/browse/GEOS-11469) Datadir catalog loader does not decrypt HTTPStoreInfo passwords
* [GEOS-11518](https://osgeo-org.atlassian.net/browse/GEOS-11518) DGGS JDBC store SQL encoder should not force the timezone to CET
* [GEOS-11519](https://osgeo-org.atlassian.net/browse/GEOS-11519) Make DGGS rHealPix tests run again
* [GEOS-11521](https://osgeo-org.atlassian.net/browse/GEOS-11521) Expose a JNDI variant of the DGGS Clickhouse datastore
* [GEOS-11541](https://osgeo-org.atlassian.net/browse/GEOS-11541) STAC search endpoint sortby query not working with POST

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.26 Series

Additional information on GeoServer 2.26 series:

* [GeoServer 2.26 User Manual](https://docs.geoserver.org/2.26.x/en/user/)
* [GeoServer 2024 Q3 Developer Update]({% post_url 2024-07-22-developer-update %}) 
* [Raster Attribute Table extension](https://github.com/geoserver/geoserver/wiki/GSIP-222)
* [Community module graduation, amending generality rule](https://github.com/geoserver/geoserver/wiki/GSIP-223)
* [Individual contributor clarification](https://github.com/geoserver/geoserver/wiki/GSIP-224)
* [Migrate geoserver-users from SourceForge to discourse](https://github.com/geoserver/geoserver/wiki/GSIP-225)

Release notes:
( [2.26.0](https://github.com/geoserver/geoserver/releases/tag/2.26.0)
| [2.26-M0](https://github.com/geoserver/geoserver/releases/tag/2.26-M0)
) 

