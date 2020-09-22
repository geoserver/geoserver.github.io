---
author: jgarnett
comments: false
date: 2020-09-08 22:38:00+00:00
layout: post
link: http://blog.geoserver.org/2020/09/08/geoserver-2-18-rc-released/
slug: geoserver-2-18-rc-released
title: GeoServer 2.18-RC Release Candidate
wordpress_id: 3144
categories:
- Announcements
tags:
- Release Candidate
---




The GeoServer community is pleased to share the availability of [GeoServer 2.18-RC](http://geoserver.org/release/2.18-RC/) Release Candidate for testing. Downloads are available ([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18-RC/geoserver-2.18-RC-bin.zip/download) and [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18-RC/geoserver-2.18-RC-war.zip/download)) along with [documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18-RC/geoserver-2.18-RC-htmldoc.zip/download) and more than 40 [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18-RC/extensions/).







This is a GeoServer release candidate made in conjunction with GeoTools 24-RC and GeoWebCache 1.18-RC.







  * Release candidates are a community building exercise and are not intended for production use.
  * We ask the community (everyone: individuals, organizations, service providers) to download and thoroughly test this release candidate and report back.
  * Participating in testing release candidates is a key expectation of our [open source social contract](http://www.ianturton.com/talks/foss4g.html#/). We make an effort to thank each person who tests in our release announcement and project presentations!






We would like to thank everyone who contributed to this release. Jody Garnett (GeoCat) for this release candidate downloads and setting up the 2.18.x branch. 







### Release Candidate Testing Priorities







We would like to ask for your assistance testing the following:







  * The number one testing priority is to try out GeoServer with your data! _Mass market open source thrives on having many people to review. Data driven open source like GeoServer thrives on exposure to many datasets._
  * The rest of this blog post highlights new features for GeoServer 2.17, please try out these features, read the documentation links, and ask questions.






Thanks to Jukka Rahkonen and Brad Hards for initial testing. To add your name to the list for the 2.18 release announcement: download the release candidate, try it out, and let us know (on the [user list](https://lists.sourceforge.net/mailman/listinfo/geoserver-users), [twitter](https://twitter.com/GeoserverO), or [LinkedIn](https://www.linkedin.com/groups/813717/)).







### Black Lives Matter







The casual use of the word "slave" in computer software is an unnecessary reference to a painful human experience that continue to impact society.







  * Change to the use of primary / replica in description of GeoServer [clustering](https://docs.geoserver.org/latest/en/user/community/jms-cluster/activemq/JDBC.html) (although new diagrams would be welcome)
  * Change to use of allow-list / deny-list
  * Changed to use of keystore password
  * Changing our repository to a "main" branch will be scheduled when both the [git command line tool](https://sfconservancy.org/news/2020/jun/23/gitbranchname/) and [GitHub repository infrastructure](https://github.com/github/renaming) roll out planned improvements for a seamless transition.






David Blasby (GeoCat) worked on [this issue](https://github.com/geoserver/geoserver/pull/4457) as part of the OSGeo Bolsena 2020 Work-from-home code-sprint.







### User interface creature comforts







A couple small but important changes to the GeoServer user interface make a significant difference to how you interact with the application and how easy it is to publish your data.







Andrea Aime (GeoSolutions) has taken the time to add an "Apply" functionality to most page, and ensure each screen has consistent buttons:







  * **Apply(new):** used to apply your setting change the running application so you can try them out, leaving the page open so you can experiment with applying different settings to see the effect.
  * **Save:** saves your setting change, returning to the initial welcome page.
  * **Cancel:** returns to the welcome page, abandoning and setting changes made.



![save, apply, cancel buttons](http://blog.geoserver.org/wp-content/uploads/2020/09/image.png)
*Consistent Save, Apply, Cancel buttons for pages*





Some configuration activities, such as WPS security, use nested pages to fine tune configuration options. These pages now consistently use **OK** and **Cancel** to return from a nested page.

![ok, cancel buttons](http://blog.geoserver.org/wp-content/uploads/2020/09/image-1.png)
*Consistent OK, Cancel buttons for nested pages*


Finally Michel Gabriël (GeoCat) arranged for these buttons to float to remain visible when scrolling through long pages.







The combination of consistent button names, in a consistent location, with an Apply button provide an improved experience when configuring GeoServer.







### Jiffle scripts now supporting multi-band outputs







The Jiffle scripting language is used to run raster algebra against one or more input raster layers. In this release we added the ability to generate multi-band outputs, whilst previous versions of Jiffle could generate only single-banded outputs. 







Here is an interesting example of how this can be useful. Let's take an image mosaic with time dimension, and configure its generation mode to "stack". This will make the mosaic use each image matching the request as an output band. Then, let's make a WMS request with two times, thus, generating an image with two bands, allowing for a before/after comparison, and use the following style, reporting in output the before, the after, and the difference, using Jiffle as a rendering transformation:






    
    <code><?xml version="1.0" encoding="UTF-8"?>
    <StyledLayerDescriptor xmlns="http://www.opengis.net/sld"
     xmlns:ogc="http://www.opengis.net/ogc"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:schemaLocation="http://www.opengis.net/sld
    http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd"
     version="1.0.0">
      <NamedLayer>
        <Name>InputLayer</Name>
        <UserStyle>
          <Title>Time comparison</Title>
          <FeatureTypeStyle>
            <Transformation>
              <ogc:Function name="ras:Jiffle">
                <ogc:Function name="parameter">
                  <ogc:Literal>coverage</ogc:Literal>
                </ogc:Function>
                <ogc:Function name="parameter">
                  <ogc:Literal>script</ogc:Literal>
                  <ogc:Literal>
                    before = src[0];
                    after = src[1];
                    dest[0] = before;
                    dest[1] = after;
                    dest[2] = after - before;
                  </ogc:Literal>
                </ogc:Function>
                <ogc:Function name="parameter">
                  <ogc:Literal>bandNames</ogc:Literal>
                  <ogc:Literal>before,after,difference</ogc:Literal>
                </ogc:Function>
              </ogc:Function>
            </Transformation>
            <Rule>
              <RasterSymbolizer>
                <Opacity>1.0</Opacity>
                <ChannelSelection>
                  <GrayChannel>
                    <SourceChannelName>3</SourceChannelName>
                  </GrayChannel>
                </ChannelSelection>
                <ColorMap>
                  <ColorMapEntry color="#800000" quantity="-1"/>
                  <ColorMapEntry color="#008000" quantity="1"/>
                </ColorMap>
              </RasterSymbolizer>
            </Rule>
          </FeatureTypeStyle>
        </UserStyle>
      </NamedLayer>
    </StyledLayerDescriptor></code>







The result is a color code map showing red when the change is negative, green where it's positive. As a bonus, running a GetFeatureInfo on the map would return all 3 values, before, after, and difference. 





![](http://blog.geoserver.org/wp-content/uploads/2020/09/difference.png)





Source maps are also available for reference:





![](http://blog.geoserver.org/wp-content/uploads/2020/09/before.png)



![](http://blog.geoserver.org/wp-content/uploads/2020/09/after.png)





### Map projections news







This release comes with support for Goode's interrupted Homolosine, including both the projection itself, and the advanced projection handling machinery to handle on the fly source data slicing.







This means one can use a common map, like Natural Earth or OSM land masses and seas, and use it without any preparation, obtaining the following:





![](http://blog.geoserver.org/wp-content/uploads/2020/09/homolosine-1024x427.png)





Still in the projections support department, we can cite:







  * Support for the Polyconic spherical case
  * Improvements in the Azimuthal Equidistant support, with better handling of source slicing when the CRS has false origins.






The following map is a polar Azimuthal Equidistant, with false origins, generated from data originally in web mercator (hence the hole in Antarctica):




![](http://blog.geoserver.org/wp-content/uploads/2020/09/Selezione_999642.png)





### Vector tiles improvements







The vector tiles extension can now work hand-in-hand with the [pre-generalized data store](https://docs.geoserver.org/2.18.x/en/user/data/vector/featurepregen.html), significantly speeding up the generation of MVTs out of a large dataset. A typical example of this case is generating vector tiles out of a OpenStreetMap import performed via imposm3, along with [generalized tables](https://imposm.org/docs/imposm3/latest/mapping.html#generalized-tables).







### Map-box GL styles language support improved







MBStyle support continues to improve with support for the dynamic expressions allowing a both feature attributes and "camera" information such as zoom level to be included.






    
    <code>{ "version": 8,
      "name": "landmarks",
      "layers": [
          {   "id": "Expression example",
              "type": "circle",
              "paint": {
                  "circle-color": "#dd9933",
                  "circle-radius": ["/",["get","LAND"],15],
              }
          }
      ]
    }</code>





![](http://blog.geoserver.org/wp-content/uploads/2020/09/image-4.png)Mapbox Style Expression example





GeoServer continues to support the earlier "function stop" approach for compatibility with the vast majority of examples online.







### Community Modules







The GeoServer project devotes space to community research and development activities.







  * The GeoPackage community module is having a breakout of creativity with a host of fascinating functionality being added by Andrea Amie (GeoSolutions).
    * Dumping a GeoPackage with WPS or WFS output formats is now significantly faster, thanks to insert batching and improved selection of settings/pragma while creating the SQLite database.
    * GeoPackage WPS output can now inline linked metadata and add OWS Contexts for request and data, providing full provenance information.
    * GeoPackage WPS output can now include styles, based on an experimental style extension along with semantic annotations linking styles to data.
    * Activity is ongoing to add a generalized tables extension, similar to the pre-generalized store, but built into the GeoPackage itself.
  * A new module looking at attribute labeling has been started by Fernando Miño.
  * Fixed an issue with JMS plugin replicating SLD styles
  * JDBCStore speed improvement with automatic caching of select directories
  * The WPS download module can now preserve the original resolutions when working against heterogeneous CRS mosaic, for the granules that are matching the requested output CRS.
  * The GRS module has been made available, adding ArcGIS REST compatibility API.
  * The JSON-LD community module has been extended to support custom JSON output too, and renamed to wfs-template.






If you are interested in seeing any of this work included on the GeoServer roadmap contact the developer to learn how to participate or fund the activity.







### And more







Other fixes and improvements include:







  * LayerGroups now list a default style in the capabilities document for greater client compatibility
  * CSW module performance fix when paging output
  * Josh Fix introduced a [proposal](https://github.com/geoserver/geoserver/wiki/GSIP-188) to help determine GridCoverageReader object types to help work with Cloud Optimized GeoTIFF images.
  * Importer has been improved with better logging and error messages
  * REST API allows changing name and workspace of a data store
  * The latest JTS 1.17.1 release
  * MetadataLinkInfo allows more metadata types to be edited, including optional about field
  * GetFeatureInfo templates can now call static methods, such as Math functions, providing additional control.
  * Styled editor now provides a choose image dialog for setting legend image
  * PDF output can now include WMS decorations 






Find out more in the [release notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16783).







## About GeoServer 2.18







Additional information on GeoServer 2.18 series:







  * GeoServer Orientation ([slides](https://t.co/fvBTLMia6f?amp=1)|[video](https://youtu.be/bdkk5eVR674))
  * Release Notes ([2.18-RC](http://* https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16783))


