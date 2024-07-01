---
author: ianturton
comments: false
date: 2020-09-26
layout: post
title: GeoServer 2.18.0 Released
categories:
- Announcements
tags:
- Release
release: release_218
version: 2.18.0
jira_version: 16796
---

The GeoServer community is pleased to share the availability
of [GeoServer 2.18.0](http://geoserver.org/release/2.18.0/)
Release. Downloads are available
([zip](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.0/geoserver-2.18.0-bin.zip/download)
and
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.0/geoserver-2.18.0-war.zip/download))
along with
[documentation](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.0/geoserver-2.18.0-htmldoc.zip/download)
and more than 40
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.0/extensions/).

This GeoServer release is made in conjunction with [GeoTools 24.0](https://geotoolsnews.blogspot.com/2020/09/geotools-240-released.html)
and GeoWebCache 1.18.0.

We would like to thank everyone who contributed to this release, and helped with testing it.

Thanks to Jukka Rahkonen, Jody Garnett and Brad Hards for initial testing of this release. This release was carried out by Ian Turton of Astun Technology and the support of the UK Hydrographic Office.

### Security Considerations

**2024-06-30 Update:** The following mitigation has been provided:

* [CVE-2024-36401](https://github.com/geoserver/geoserver/security/advisories/GHSA-6jj6-gm7p-fcvv) Remote Code Execution (RCE) vulnerability in evaluating property name expressions (Critical)

  A [patch](https://sourceforge.net/projects/geoserver/files/GeoServer/2.18.0/geoserver-2.18.0-patches.zip/download) (replacing `gt-app-schema`, `gt-complex` and `gt-xsd-core` jars) has been provided by Andrea (GeoSolutions)

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

### Black Lives Matter

The casual use of the word "slave" in computer software is an unnecessary
reference to a painful human experience that continue to impact society.

  * Change to the use of primary / replica in description of GeoServer
  [jms-clustering](https://docs.geoserver.org/latest/en/user/community/jms-cluster/index.html)
  * Change to use of allow-list / deny-list 
  * Changed to use of key store password 
  * Changing our repository to a "main" branch will be scheduled when both the [git command line
  tool](https://sfconservancy.org/news/2020/jun/23/gitbranchname/) and
  [GitHub repository infrastructure](https://github.com/github/renaming)
  roll out planned improvements for a seamless transition.

David Blasby (GeoCat) worked on [this
issue](https://github.com/geoserver/geoserver/pull/4457) as part of the
OSGeo Bolsena 2020 Work-from-home code-sprint.

### User interface creature comforts

A couple small but important changes to the GeoServer user interface
make a significant difference to how you interact with the application
and how easy it is to publish your data.

Andrea Aime (GeoSolutions) has taken the time to add an "Apply"
functionality to most page, and ensure each screen has consistent buttons:

  + **Apply** (new): used to apply your setting change the running
  application so you can try them out, leaving the page open so you
  can experiment with applying different settings to see the effect.
  + **Save:** saves your setting change, returning to the initial
  welcome page.  
  + **Cancel:** returns to the welcome page, abandoning
  and setting changes made.

![](/img/uploads/image.png)

Consistent Save, Apply, Cancel buttons for pages

Some configuration activities, such as WPS security, use nested pages to
edit detailed settings. These pages now consistently use:

  + **OK:** modify settings, returning to page being edited so they can be saved.
  + **Cancel:** abandon any changes and return to the page being edited.

![](/img/uploads/image-1.png)

Consistent OK, Cancel buttons for nested pages

Finally Michel Gabriël (GeoCat) arranged for these buttons to float to
remain visible when scrolling through long pages.

The combination of consistent button names, in a consistent location, with
an Apply button provide an improved experience when configuring GeoServer.

### Jiffle scripts now supporting multi-band outputs

The Jiffle scripting language is used to run raster algebra against one
or more input raster layers. In this release we added the ability to
generate multi-band outputs, whilst previous versions of Jiffle could
generate only single-banded outputs.

Here is an interesting example of how this can be useful. Let's take an
image mosaic with time dimension, and configure its generation mode to
"stack". This will make the mosaic use each image matching the request
as an output band. Then, let's make a WMS request with two times,
thus, generating an image with two bands, allowing for a before/after
comparison, and use the following style, reporting in output the before,
the after, and the difference, using Jiffle as a rendering transformation:


~~~xml
<?xml version="1.0"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd" version="1.0.0">
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
</StyledLayerDescriptor>
~~~

The result is a color code map showing red when the change is negative,
green where it's positive. As a bonus, running a `GetFeatureInfo` request
on the map would return all 3 values, before, after, and difference.

![](/img/uploads/difference.png)

Source maps are also available for reference:

![](/img/uploads/before.png)

![](/img/uploads/after.png)

### Map projections news

This release comes with support for Goode's interrupted Homolosine,
including both the projection itself, and the advanced projection handling
machinery to handle on the fly source data slicing.

This means one can use a common map data, like Natural Earth or OSM land masses
and seas, and use it without any preparation, obtaining the following:

![](/img/uploads/homolosine-1024x427.png)

Still in the projections support department, we can report:

  * Support for the Polyconic spherical case
  * Improvements in the Azimuthal Equidistant support, with better handling of source slicing
  when the CRS has false origins.

The following map is a polar Azimuthal Equidistant, with false origins,
generated from data originally in web mercator (hence the hole in
Antarctica):

![](/img/uploads/Selezione_999642.png)

### Vector tiles improvements

The vector tiles extension can now work
hand-in-hand with the [pre-generalized data
store](https://docs.geoserver.org/2.18.x/en/user/data/vector/featurepregen.html),
significantly speeding up the generation of MVTs out of a large
dataset. A typical example of this case is generating vector tiles out
of a OpenStreetMap import performed via `imposm3`, along with [generalized
tables](https://imposm.org/docs/imposm3/latest/mapping.html#generalized-tables).

### Map-box GL styles language support improved

MBStyle support continues to improve with support for the dynamic
expressions allowing a both feature attributes and "camera" information
such as zoom level to be included.

~~~js
{ "version": 8,
  "name": "landmarks", "layers": [
      {   "id": "Expression example",
          "type": "circle", "paint": {
              "circle-color": "#dd9933", "circle-radius":
              ["/",["get","LAND"],15],
          }
      }
  ]
}
~~~

![](/img/uploads/image-4.png)

Mapbox Style Expression example

GeoServer continues to support the earlier "function stop" approach for
compatibility with the vast majority of examples online.

### Community Modules

The GeoServer project devotes space to community research and development
activities.
  * The GeoPackage community module is having a breakout of creativity
  with a host of fascinating functionality being added by Andrea Aime
  (GeoSolutions).
    * Dumping a GeoPackage with WPS or WFS output formats is now
    significantly faster, thanks to insert batching and improved selection
    of settings/pragma while creating the SQLite database.  
    * GeoPackage
    WPS output can now in-line linked metadata and add OWS Contexts for
    request and data, providing full provenance information.  
    * GeoPackage
    WPS output can now include styles, based on an experimental style
    extension along with semantic annotations linking styles to data.
    * Activity is ongoing to add a generalized tables extension, similar
    to the pre-generalized store, but built into the GeoPackage itself.
  * A new module looking at attribute labeling has been started by
  Fernando Miño.  
  * Fixed an issue with JMS plugin replicating SLD
  styles 
  * `JDBCStore` speed improvement with automatic caching of select
  directories 
  * The WPS download module can now preserve the original
  resolutions when working against heterogeneous CRS mosaic, for the
  granules that are matching the requested output CRS.  
  * The GRS module has been made available, adding ArcGIS REST compatibility API.  
  * The JSON-LD community module has been extended to support custom JSON
  output too, and renamed to wfs-template.

If you are interested in seeing any of this work included on the GeoServer
road map contact the developer to learn how to participate or fund the
activity.

### And more

Other fixes and improvements include:

  * `LayerGroups` now list a default style in the capabilities
  document for greater client compatibility 
  * CSW module performance fix when paging output 
  * Josh Fix introduced a [proposal](https://github.com/geoserver/geoserver/wiki/GSIP-188)
  to help determine `GridCoverageReader` object types to help work
  with Cloud Optimized GeoTIFF images.  
  * Importer has been improved with better logging and error messages 
  * REST API allows changing name and workspace of a data store 
  * The latest JTS 1.17.1 release 
  * `MetadataLinkInfo` allows more metadata types to be edited, including
  optional about field 
  * `GetFeatureInfo` templates can now call static
  methods, such as Maths functions, providing additional control.  
  * Styled editor now provides a choose image dialog for setting legend
  image 
  * PDF output can now include WMS decorations

Find out more in the [release
notes](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16796).

## About the GeoServer 2.18 Series

Additional information on GeoServer 2.18 series:
  
  * GeoServer Orientation
  ([slides](https://t.co/fvBTLMia6f?amp=1)|[video](https://youtu.be/bdkk5eVR674))
  * Release Notes
  ([2.18.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16796)
  | [2.18-RC](
  https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16783))


