---
author: aaime
comments: false
date: 2019-09-18 16:47:40+00:00
layout: post
link: http://blog.geoserver.org/2019/09/18/geoserver-2-16-released/
slug: geoserver-2-16-released
title: GeoServer 2.16.0 released
wordpress_id: 3059
---




We are happy to announce the release of [GeoServer 2.16.0](http://sourceforge.net/projects/geoserver/files/GeoServer/2.16.0/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.16.0/geoserver-2.16.0-bin.zip/download) and [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.16.0/geoserver-2.16.0-war.zip/download)) along with docs and extensions.







This is a GeoServer release candidate made in conjunction with GeoTools 22.0.







## Faster map rendering of complex styles







If you have very complex styles, with lots of rules and complex filtering conditions you'll be pleased to hear that GeoServer 2.16.x can locate the right symbolizer much quicker than previous versions. This is useful, for example, in the [GeoServer home page](http://geoserver.org/) demo map, rendered from OSM data using a OSM Bright clone built with the CSS module.





![](http://blog.geoserver.org/wp-content/uploads/2019/08/Selezione_903-1.png)The GeoSolutions offices in Massarosa (Viareggio), Italy, in the geoserver.org demo map 





## Dynamic densification on reprojection







GeoServer has always reprojected data "point by point", this typically caused long lines represented by just two points to be turn into straight lines, instead of curves, as they were supposed to.







In GeoServer there is a new "advanced projection handling" option in WMS enabling on the fly densification of data, the rendering engine computes how much deformation the projection applies in the area being rendered, and densifies the long lines before reprojection, resulting in eye pleasing curves in output. See a "before and after" comparison here:





![](http://blog.geoserver.org/wp-content/uploads/2019/08/Selezione_896.png)Reprojection, original point by point versus densified mode in 2.16.x





## EPSG database updated to v 9.6







Thanks to the sponsorship of [GeoScience Australia](https://www.ga.gov.au/) the EPSG database has been updated to version 9.6, including roughly a thousand more codes than the previous version available in GeoServer. The code has also been updated to ensure the NTv2 grid shift files between GDA94 and GDA2020 work properly.







![](http://blog.geoserver.org/wp-content/uploads/2019/08/Selezione_898.png)







## Complex GeoJSON output changes







GeoServer WFS can already output GeoJSON out of complex features data sources (app-schema). However, the output can be less than pleasing at times, the following improvements have been made:







  * The property/element alternation typical of GML is preserved, causing deeply nested and ugly to look structures. Not everyone loves to write a "container.x.x" access to reach the x value, with 2.16.x the output skips one of the containers and exposes a direct "container.x" structure
  * XML attributes are now turned into plain JSON properties, and prefixed with a "@"
  * Feature and data types are not lost anymore in translations, preserved by a "@feaureType" and "@dataType" attributes
  * Full nested features are encoded as GeoJSON again, keeping their identifiers






Thanks to the sponsorship of the [French geological survey - BRGM](https://www.brgm.eu) and the [French environmental information systems research center – INSIDE](https://github.com/INSIDE-information-systems/), the 2.16.0 output now looks as follows:






    
    <code>{
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "id": "0001000001",
          "geometry": {
            "type": "Point",
            "coordinates": [51.0684, 1.4298]
          },
          "properties": {
            "@featureType": "Borehole",
            "identifier": {
              "value": "BSS000AAAA",
              "@codeSpace": "http://www.ietf.org/rfc/rfc2616"
            },
            "bholeHeadworks": [
              {
                "type": "Feature",
                "geometry": {
                  "type": "Point",
                  "coordinates": [51.0684, 1.4298]
                },
                "properties": {
                  "@featureType": "BoreCollar",
                  "collarElevation": {
                    "value": -32,
                    "@srsName": "http://www.opengis.net/def/crs/EPSG/0/5720",
                    "@srsDimension": "1",
                    "@uomLabels": "m"
                  }
                }
              }
            ],
    
    </code>







## Status Monitoring module promoted to Core







The [Status Monitoring module](https://docs.geoserver.org/latest/en/user/configuration/status.html#system-status) has been promoted to core, and is now included in the GeoServer status page by default!







This module adds a new tab to the Server Status page, with system statistics so that you can monitor the system which GeoServer is running on from the Web GUI.





![../../_images/gui.png](https://docs.geoserver.org/latest/en/user/_images/gui.png)





## Authentication key module graduated to extension







The "Authkey" module has been graduated to extension, allowing security unaware applications to access GeoServer. Reminder, in order to keep the system secure the keys should be managed as temporary session tokens by an external application (e.g. MapStore can do this).







![](http://blog.geoserver.org/wp-content/uploads/2019/08/Selezione_900.png)







## PostGIS data store improvements







The PostGIS data store sees a few improvements, including:







  * TWKB encoding for geometries for all WMS/WMTS requests, reducing the amount of data travelling from the database to GeoServer
  * The JDBC driver used to transfer all data as ASCII, the code was modified to allow full binary transfer when prepared statements are enabled (driver limitation, binary can only be enabled in that case)
  * SSL encryption control, the driver defaults to have it on with a significant overhead, if the communication is in a trusted network the encryption can be disabled with benefit to performance
  * Improved encoding of "or-ed" filters, which now use the "in" operator where possible, increasing the likeliness that an eventual index o nthat column will be used
  * Native KNN nearest search when using the "nearest" filter function






## OGC/GDAL stores updated to GDAL 2.x







The OGR datastore as well as the GDAL image readers have been updated and now work against GDAL 2.x official binaries, without requiring custom builds any longer.







The OGR datastore can open any vector data source and, in particular, it can use the native FileGBD library when using Windows. It's also interesting to note that it can open Spatialite files, quite important now that the direct Spatialite store is gone.







## Azure GWC blobstore 







Tiles can now be stored in Azure blob containers, increasing GWC compatibility with cloud environments, after the already existing S3 support.







A warning though, Azure does not provide, unlike S3, a mass blob delete API, so on truncate GWC will have to go and remove tiles making a DELETE request for each (using parallel requests of course).







## SLDService community module graduated to extension







The [SLDService](https://docs.geoserver.org/latest/en/user/extensions/sldservice/index.html) community module allowed to generated classified maps of vector data based on criterias such as equal interval, quantiles and unique values.







The same module has now graduated to extension, providing also data filtering based on standard deviation, equal area classification, and offering all the same services on raster data as well (with automatic sub-sampling when the source image is too large).







For example, creating a five classes quantile classification based on states persons over a custom color ramp can be achieved using the following:






    
    <code>curl -v -u admin:geoserver -XGET
      http://localhost:8080/geoserver/rest/sldservice/states/classify.xml?attribute=PERSONS&method=quantile&intervals=5&ramp=CUSTOM&startColor=0xf7fcb9&endColor=0x31a354&fullSLD=true</code>





![](http://blog.geoserver.org/wp-content/uploads/2019/08/Selezione_899.png)





## New Community Modules







  * WMTS styling module, which adds the ability to get/put a style on a per layer basis using restful resources exposed as ResourceURL
  * OGC API module, including implementations of the new OGC Web APIs for Features, Tiles and Styles (more to come in the upcoming months). Mind, these are cool but also prototypes based on specifications still in draft form, we have warned you, the API will likely have a few rounds of changes still before it stabilizes.
  * [MapML](https://docs.geoserver.org/latest/en/user/community/mapml/index.html) community module.  See [this video](https://www.youtube.com/watch?v=14XvqNf4jTE&feature=youtu.be) for step by step installation instructions.






## Other assorted improvements







There are many improvements to look at in the [2.16.0 release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16765), as well as in the 2.16-RC [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16750).  Cherry picking a few, we hav:







  * Integrated GWC fails to seed layers if any data security is configured
  * Default Datastore Parameters panel does not allow https:// protocol values
  * Parameter Extractor plugin cannot mangle URL correctly if Monitor plugin is installed
  * Permit extensibility of Common Formats from Layer Preview page
  * Update name to id in OGC API Collection
  * Add support for configuring ACL in gwc-s3 community module
  * Enhance mongodb schema generation






## About GeoServer 2.16







GeoServer 2.16 has been first released in September 2019.







  * Release notes ([2.16.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16765) and [2.16-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16750))


