---
author: simone.giannecchini
comments: true
date: 2008-11-20 23:00:40+00:00
layout: post
link: http://blog.geoserver.org/2008/11/20/raster-symbolizer-tricks-part-1/
slug: raster-symbolizer-tricks-part-1
title: Raster Symbolizer tricks - part 1
wordpress_id: 149
categories:
- Developer notes
- Features
- Tips and Tricks
tags:
- raster
- RasterSymbolizer
---

I am going to bother for a few mins in order to show a few things about the raster symbolizer implementation that has landed on 1.7. Ideally this should the first of a series of more posts, but I can't guarantee on that :-).

Anyway, today I have been playing with some bathymetry data for the geoSDI project. I cannot share them since it is classified data but I have been told that I can show some snapshots :-).

Here below you have the gdalinfo on one of the datasets:

Driver: GTiff/GeoTIFF
Files: DEM_Vulcano_Lipari_Salina4326.tif
Size is 3718, 3600
Coordinate System is:
GEOGCS["WGS 84",
....
AUTHORITY["EPSG","4326"]]
Origin = (14.747192412574043,38.660954215168857)
Pixel Size = (0.000090196304703,-0.000090196304703)
Metadata:
AREA_OR_POINT=Point
Image Structure Metadata:
INTERLEAVE=BAND
Corner Coordinates:
....
Band 1 Block=3718x1 Type=Float32, ColorInterp=Gray

As you can see we are talking about Float data. First of all I retiled it with gdal_transalte (striped tiff are pretty bad performance-wise) then I added a few overview using gdaladdo with nearest neighbor interpolation. Once this was done I just throw it at the GeoServer and here is the result for an [untiled](http://imagebin.ca/view/AUHZLSA.html) request ([here](http://imagebin.ca/view/7L7YNIv.html) a detailed request ) and for a [tiled](http://imagebin.ca/view/8xvMcnUF.html) request. Quick explanation, when you set up a raster with no real raster symbolizer element in its style (like for the raster.sld that ships with GeoServer) you can get strange results in case your data is raw, like bathymetries, DEMs and the like. What we do is trying to render something useful by doing a local contrast stretch, hence a tiled request can have the checkerboard approach and an untiled request can look fuzzy since maximum and minimum values are used for the stretch. In the future we might computer approximated statistics for a layer at configuration time and use them for the subsequent renderings.

Beside this I wanted to show a nice extension we implemented for the raster symbolizer element. Check [this](http://pastebin.com/f5db1edce) style as well as [this](http://pastebin.com/f36d60f8a) one (notice that to use the secondo you have to uncheck SLD validation since the extension is not recognized by OGC schemas). They look like the same but if you check the second one you'll see that the color map element looks like this <ColorMap extended="true"> while in the other one it looks like this <ColorMap>. Well, long story short this is an extension I implemented in order to allow people to ask the GeoServer to symbolize raster data using as many colors as possible (specifically 65k) instead of limiting itself to 256. This results in much better looking images but you have to give away some performances. I guess it is something nice to have for layer that you want to cache with TileCache or GeowebCache.

To see you the differences, check the following:



	
  * [256](http://imagebin.ca/view/ODJQAz0h.html) colors

	
  * [256](http://imagebin.ca/view/hDj7xqDx.html) colors - detail

	
  * [65536](http://imagebin.ca/view/wDITwY7.html) colors

	
  * [65536](http://imagebin.ca/view/L__hDR9.html) colors -detail


I guess I have bothered enough.

Ciao a tutti.

PS. I found a minor bug today on the SLDParser which was not parsing the extended attribute. It is now fixed but unless you build things yourself, you won't be able to test these things on 1.7.0. Drop me a few lines in case you want to try the differences and I'll tell you how to fix this problem.
