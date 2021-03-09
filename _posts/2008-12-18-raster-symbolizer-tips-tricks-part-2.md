---
author: simone.giannecchini
comments: true
date: 2008-12-18 14:36:59+00:00
layout: post
link: http://blog.geoserver.org/2008/12/18/raster-symbolizer-tips-tricks-part-2/
slug: raster-symbolizer-tips-tricks-part-2
title: Raster Symbolizer tips & tricks - part 2
wordpress_id: 160
categories:
- Developer notes
- Tips and Tricks
- Tutorials
tags:
- raster
- RasterSymbolizer
- SLD
- style
- wms
---

A new post on the Raster Symbolizer tips & tricks, this time I am going to show how to build an RGB image using 8 bits or unsigned 16 bits multi band coverages.

I have been playing lately with some remote sensing data for the geoSDI project specifically the emissive subdataset coming from the  MODIS sensor on-board the TERRA satellite. A small sample dataset can be found [here](http://geosdi.nsdi.it/geotif_16Band/EmissiveCampania.tif). Its gdalinfo is here below:

Files: EmissiveCampania.tiff
Size is 63, 156
Coordinate System is:
GEOGCS["WGS 84",
DATUM["WGS_1984",
SPHEROID["WGS 84",6378137,298.2572235630016,
AUTHORITY["EPSG","7030"]],
AUTHORITY["EPSG","6326"]],
PRIMEM["Greenwich",0],
UNIT["degree",0.0174532925199433],
AUTHORITY["EPSG","4326"]]
Origin = (13.742259882413393,41.506517193315830)
Pixel Size = (0.032872864093301,-0.009584951678830)
Metadata:
AREA_OR_POINT=Area
Image Structure Metadata:
INTERLEAVE=BAND
Corner Coordinates:
Upper Left  (  13.7422599,  41.5065172) ( 13d44'32.14"E,
Lower Left  (  13.7422599,  40.0112647) ( 13d44'32.14"E,
Upper Right (  15.8132503,  41.5065172) ( 15d48'47.70"E,
Lower Right (  15.8132503,  40.0112647) ( 15d48'47.70"E,
Center      (  14.7777551,  40.7588910) ( 14d46'39.92"E,
Band 1 Block=63x65 Type=UInt16, ColorInterp=Gray
NoData Value=65535
Band 2 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535
Band 3 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535
Band 4 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535
Band 5 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535
Band 6 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535
Band 7 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535
Band 8 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535
Band 9 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535
Band 10 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535
Band 11 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535
Band 12 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535
Band 13 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535
Band 14 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535
Band 15 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535
Band 16 Block=63x65 Type=UInt16, ColorInterp=Undefined
NoData Value=65535

The goal was to build a simple RGB on the fly (WCS usage is als envisioned, hence we could not just build it offline) by using bands 11, 9 and 1 respectively.

The style I have used for doing this is reported here below, it is a nice guideline in case you want to do something similar with Landsat data as an instance and create a false color image from the oiriginal dataset ( I might blog about that as well sooner or later :-) ).

<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor
xmlns="http://www.opengis.net/sld"
xmlns:ogc="http://www.opengis.net/ogc"
xmlns:xlink="http://www.w3.org/1999/xlink"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd" version="1.0.0">
<UserLayer>
<Name>raster_layer</Name>
<LayerFeatureConstraints>
<FeatureTypeConstraint/>
</LayerFeatureConstraints>
<UserStyle>
<Name>raster</Name>
<Title>A boring default style</Title>
<Abstract>A sample style for rasters</Abstract>
<FeatureTypeStyle>
<FeatureTypeName>Feature</FeatureTypeName>
<Rule>
<RasterSymbolizer>
<Opacity>1.0</Opacity>
<ChannelSelection>
<RedChannel>
<SourceChannelName>11</SourceChannelName>
</RedChannel>
<GreenChannel>
<SourceChannelName>9</SourceChannelName> >
</GreenChannel>
<BlueChannel>
<SourceChannelName>1</SourceChannelName>
</BlueChannel>
</ChannelSelection>
</RasterSymbolizer>
</Rule>
</FeatureTypeStyle>
</UserStyle>
</UserLayer>
</StyledLayerDescriptor>

[![RGB rendering of bands 11,9,1](http://blog.geoserver.org/wp-content/uploads/wms1.jpeg)](http://blog.geoserver.org/wp-content/uploads/wms1.jpeg)

Since we are here, I will also show another rendering we have set up which applies a user defined colormap to band 11 (emissive temperature) which ranges from blu to red. Here is the style:

<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor
xmlns="http://www.opengis.net/sld"
xmlns:ogc="http://www.opengis.net/ogc"
xmlns:xlink="http://www.w3.org/1999/xlink"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd" version="1.0.0">
<UserLayer>
<Name>raster_layer</Name>
<LayerFeatureConstraints>
<FeatureTypeConstraint/>
</LayerFeatureConstraints>
<UserStyle>
<Name>raster</Name>
<Title>A boring default style</Title>
<Abstract>A sample style for rasters</Abstract>
<FeatureTypeStyle>
<FeatureTypeName>Feature</FeatureTypeName>
<Rule>
<RasterSymbolizer>
<Opacity>1.0</Opacity>
<ChannelSelection>
<GrayChannel>
<SourceChannelName>11</SourceChannelName>
</GrayChannel>
</ChannelSelection>
<ColorMap extended="true">
<ColorMapEntry color="#0000ff" quantity="3189.0"/>
<ColorMapEntry color="#009933" quantity="6000.0"/>
<ColorMapEntry color="#ff9900" quantity="9000.0" />
<ColorMapEntry color="#ff0000" quantity="14265.0"/>
</ColorMap>
</RasterSymbolizer>
</Rule>
</FeatureTypeStyle>
</UserStyle>
</UserLayer>
</StyledLayerDescriptor>

and here is the result:

[![Band 11 (emissive temperature) with colormap](/img/uploads/wms11-300x265.jpg)](http://blog.geoserver.org/wp-content/uploads/wms11.jpeg)

Enjoy,

Simone.
