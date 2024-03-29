---
author: tbarsballe
comments: false
date: 2018-09-24 16:00:22+00:00
layout: post
link: http://blog.geoserver.org/2018/09/24/geoserver-2-14-0-released/
slug: geoserver-2-14-0-released
title: GeoServer 2.14.0 Released
wordpress_id: 2969
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_214
version: 2.14.0
jira_version: 16734
---

We are happy to announce the release of [GeoServer 2.14.0](http://sourceforge.net/projects/geoserver/files/GeoServer/2.14.0/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.14.0/geoserver-2.14.0-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.14.0/geoserver-2.14.0-war.zip/download), and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.14.0/geoserver-2.14.0.exe/download)) along with docs and extensions.





This is the first stable release of the 2.14 series of GeoServer, and is recommended for all production systems. With this release, the 2.13 series moves to maintenance, and the 2.12 series moves to unsupported.


This release is made in conjunction with GeoTools 20.o and GeoWebCache 1.14.0




This release includes a number of new features and improvements:





## WMS “nearest match” support for time dimension


WMS time dimension can now be configured for “nearest match”, that is, to return the nearest time to the one requested (either explicitly, or implicitly via the default time value).

[![](/img/uploads/Selezione_350.png)](/img/uploads/Selezione_350.png)

In case of mismatch the actual time used will be returned along with the response as a HTTP header. It is also possible to configure a maximum tolerance, beyond that the server will throw a service exception.


## Channel selection name allow expressions






GeoServer 2.14.0 allows expressions to be used in SourceChannelName SLD elements, and in their code counterpart, thus allowing dynamic channel selection. This is welcomed news for anyone building applications that display multispectral or hyperspectral data, thus avoiding the need to build many different styles for the various interesting false color combinations.











Here is an SLD example:








    
    <code data-blogger-escaped-style="background: transparent; border-radius: 3px; border: 0px; box-sizing: border-box; display: inline; font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, Courier, monospace; font-size: 13.6px; line-height: inherit; margin: 0px; overflow: visible; padding: 0px; word-break: normal; word-wrap: normal;"><RasterSymbolizer>
      <ChannelSelection>
        <RedChannel>
          <SourceChannelName>
              <ogc:Function name="env">
                 <ogc:Literal>B1</ogc:Literal>
                 <ogc:Literal>2</ogc:Literal>
              </ogc:Function>
          </SourceChannelName>
        </RedChannel>
        <GreenChannel>
          <SourceChannelName>
              <ogc:Function name="env">
                 <ogc:Literal>B2</ogc:Literal>
                 <ogc:Literal>5</ogc:Literal>
              </ogc:Function>
          </SourceChannelName>
        </GreenChannel>
        <BlueChannel>
          <SourceChannelName>
              <ogc:Function name="env">
                 <ogc:Literal>B3</ogc:Literal>
                 <ogc:Literal>7</ogc:Literal>
              </ogc:Function>
          </SourceChannelName>
        </BlueChannel>
      </ChannelSelection>
    <RasterSymbolizer>
    </code>




## Map algebra


This release adds support for an efficient map algebra package knows as Jiffle. Jiffle has been the work of a former GeoTools contributor, Michael Bedwards, that has been salvaged, upgraded to support Java 8, and integrated in jai-ext. From the there support has been added into the GeoTools gt-process-raster module and as a result in GeoServer WPS, to be used either directly or as a rendering transformation.

The following SLD style calls onto Jiffle to perform a NDVI calculation on top of Sentinel 2 data:





    
    <span data-blogger-escaped-style="border: 0px; color: #007020; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="cp"><?xml version="1.0" encoding="UTF-8"?></span>
    <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><StyledLayerDescriptor</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">xmlns=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"http://www.opengis.net/sld"</span> 
    <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">   xmlns:ogc=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"http://www.opengis.net/ogc"</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">xmlns:xlink=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"http://www.w3.org/1999/xlink"</span> 
    <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">   xmlns:xsi=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"http://www.w3.org/2001/XMLSchema-instance"</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">xsi:schemaLocation=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"http://www.opengis.net/sld</span>
    <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">http://schemas.opengis.net/sld/1.0.0/StyledLayerDescriptor.xsd"</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">version=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"1.0.0"</span><span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt">></span>
      <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><NamedLayer></span>
        <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><Name></span>Sentinel2 NDVI<span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></Name></span>
        <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><UserStyle></span>
          <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><Title></span>NDVI<span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></Title></span>
          <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><FeatureTypeStyle></span>
            <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><Transformation></span>
              <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><ogc:Function</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">name=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"ras:Jiffle"</span><span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt">></span>
                <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><ogc:Function</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">name=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"parameter"</span><span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt">></span>
                  <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><ogc:Literal></span>coverage<span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></ogc:Literal></span>
                <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></ogc:Function></span>
                <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><ogc:Function</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">name=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"parameter"</span><span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt">></span>
                  <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><ogc:Literal></span>script<span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></ogc:Literal></span>
                  <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><ogc:Literal></span>
                    nir = src[7];
                    vir = src[3];
                    dest = (nir - vir) / (nir + vir);
                  <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></ogc:Literal></span>
                <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></ogc:Function></span>
              <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></ogc:Function></span>
            <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></Transformation></span>
            <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><Rule></span>
              <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><RasterSymbolizer></span>
                <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><Opacity></span>1.0<span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></Opacity></span>
                <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><ColorMap></span>
                  <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><ColorMapEntry</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">color=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"#000000"</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">quantity=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"-1"</span><span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt">/></span>
                  <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><ColorMapEntry</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">color=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"#0000ff"</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">quantity=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"-0.75"</span><span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt">/></span>
                  <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><ColorMapEntry</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">color=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"#ff00ff"</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">quantity=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"-0.25"</span><span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt">/></span>
                  <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><ColorMapEntry</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">color=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"#ff0000"</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">quantity=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"0"</span><span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt">/></span>
                  <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><ColorMapEntry</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">color=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"#ffff00"</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">quantity=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"0.5"</span><span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt">/></span>
                  <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"><ColorMapEntry</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">color=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"#00ff00"</span> <span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="na">quantity=</span><span data-blogger-escaped-style="border: 0px; color: #4070a0; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: inherit; margin: 0px; padding: 0px; vertical-align: baseline;" class="s">"1"</span><span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt">/></span>
                <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></ColorMap></span>
              <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></RasterSymbolizer></span>
            <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></Rule></span>
          <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></FeatureTypeStyle></span>
        <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></UserStyle></span>
      <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></NamedLayer></span>
    <span data-blogger-escaped-style="border: 0px; color: #062873; font-family: inherit; font-size: 14.4px; font-style: inherit; font-weight: bold; margin: 0px; padding: 0px; vertical-align: baseline;" class="nt"></StyledLayerDescriptor></span>


The performance is good enough for interactive display, and the result looks as follows (click to enlarge):

[![](/img/uploads/s2-ndvi-300x200.png)](/img/uploads/s2-ndvi.png)


## PostGIS store improvements and measured geometries support


The PostGIS datastore has been for years the only one that could encode a few filter functions used in filters down into native SQL, but it required a datastore creation flag to be enabled.
Starting with this release it will do so by default.

The functions supported for SQL encoding by the store are:



 	
  * String functions: strConcat, strEndsWith, strStartsWith, strEqualsIgnoreCase, strIndexOf, strLength, strToLowerCase, strToUpperCase, strReplace, strSubstring, strSubstringStart, strTrim, strTrim2

 	
  * Math functions: abs, abs_2, abs_3, abs_4, ceil, floor

 	
  * Date functions: dateDifference


This release adds support for “array” data type in the store, with full reading and writing support, as well as native filtering (with index support, where feasible).

Finally, it’s now possible to read geometries with measures from PostGIS and encode the results in GML. GML does not natively support measures, so the encoding is off by default and you’ll have to enable it explicitly, as well as ensure that the clients involved in WFS usage recognize this extra ordinate. The work will continue in the next few month in order to cover more formats.

[![](/img/uploads/Selezione_351.png)](/img/uploads/Selezione_351.png)







## Image mosaic improvements


The image mosaic module never sleeps, in this release we see the following improvements:



 	
  * Support for remote images (e.g. S3 or Minio). In order to leverage this the mosaic index will have to be created up-front (manually, or with some home grown tools)

 	
  * A new “virtual native resolution” read parameter allows the mosaic to compose outputs respecting a native resolution other than its native one (useful in case you want to give selective resolution access to different users)

 	
  * Supporting multiple WKBs footprint for pixel precise overviews masking

 	
  * A new read mask parameter allows to cut the image to a given geometry (again, helps in providing different selective views to different users)

 	
  * Speed up NetCDF mosaics by allowing usage of stores coming from a repository, instead of re-creating them every time a NetCDF file is needed (to be setup in the auxiliary store config file, while the repository instance needs to be passed as a creation hint).

 	
  * The mosaic now works against images without a proper CRS, setting them into the “CRS not found” wildcard CRS, aka “EPSG:404000”




## App-schema improvements


The app-schema module got significant performance and functionality improvements since 19.x series, in particular:



 	
  * Better delegation of spatial filters on nested properties to native database

 	
  * Improved support for multiple nested attribute matches in filters

 	
  * It is now possible to use Apache SOLR as a data source for app-schema

 	
  * The configuration files can be hosted on a remote HTTP server




## The MongoDB store upgrades to official extension


Wanted to use the MongoDB store but worried about its unsupported status? Worry no more, in GeoServer 2.14 the MongoDB datastore upgraded to official extension status.






## Style editor improvements


[![](/img/uploads/side_by_side.png)](/img/uploads/side_by_side.png)

The GeoServer style editor now includes a fullscreen side-by-side editing mode, to make it easier to preview your styles while editing them. Click the fullscreen button at the top-right of the screen to toggle fullscreen mode.

The toolbar also has two new additions, a color picker helping to find the right color and turn it into a HEX specification, and a file chooser that allows to pick an external graphic and build the relevant ExternalGraphic element:

[![](/img/uploads/Selezione_354.png)](/img/uploads/Selezione_354.png)

[![](/img/uploads/Selezione_355.png)](/img/uploads/Selezione_355.png)







## Windows build restored


GeoServer failed to properly build on Windows for a long time. GeoServer 2.14.x is the first branch in years to successfully build on Windows, and we have added an AppVeyor build to help keep the build going in the future.

The work to make it build there has been fully done in spare time, and we are still experiencing random build failures. If you are a Java developer on Windows, we could really use your help to keep GeoServer Windows build friendly.


## New community modules





The 2.14 series comes with a few new community modules, in particular:



 	
  * OAuth2 OpenID connect module (still very much a work in progress)

 	
  * A WFS3 implementation has been added that matches the current WFS3 specification draft, and it’s being updated to become an official compliant one.


Mind, community modules are not part of the release, but you can find them in the [nightly builds](http://geoserver.org/release/master/) instead.






## JTS Upgrade


Java Topology Suite (JTS) has been upgraded to version 1.16. This marks a significant change in package naming, the library has switched from "com.vividsolutions" to "org.locationtech"  packages and all GeoServer code has been updated to follow suit.

This has some side-effects on output produced by [REST](http://docs.geoserver.org/stable/en/user/rest/index.html#rest) featuretype and structured coverage requests, specifically the package names used for geometry types in the binding parameter of any geometry attributes.

Any REST clients which rely on this binding information should be updated to support the new names. GeoServer will still support reading the old "com.vividsolutions" names, but will only output the new"org.locationtech" names.

For more details, refer to the [upgrade guide](http://docs.geoserver.org/stable/en/user/installation/upgrade.html#jts-type-bindings-geoserver-2-14-and-newer) in the GeoServer documentation.








## Other assorted improvements


There are many improvements to look at in the release notes ([2.14.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16734) | [2.14-RC](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=16718)), cherry picking a few here:



 	
  * The ncWMS community module has seen significant performance improvements

 	
  * WPS has a CSV input/output supporting geometryless data, as well as geometries with WKT encoding, as well as supporting pure PNG/JPEG image for raster data

 	
  * Time/Elevation parsers are no longer silently cutting the read data to 100 entries

 	
  * The WMTS multidimensional GetHistogram operation is now significantly faster, and a new GetDomainValues operation allows to page through the values of a domain (time, elevation) that has too many values to be efficiently explored with DescribeDomain or GetFeature. The DescribeDomain was also improved to allow a selection of the domains that should be described.

 	
  * The SLDService community module has now the ability to return a full SLD style (as opposed to snippets), allows for custom classification and custom color selection. Also, keep an eye on this module, as it’s about to graduate to supported status

 	
  * The monitoring module can now log the hit/miss status of tiled requests, quite helpful to verify the benefit of caching, especially while using WMS direct integration

 	
  * Fix "Chunk [] is not a valid entry" error for the embedded GWC reload endpoint

 	
  * Tiled layers preview does not use Proxy Base Url

 	
  * featuretype.xml bindings reference com.vividsolutions.jts classes




## Security consideration






Please update your production instances of GeoServer to receive the latest security updates and fixes.




This release addresses several security vulnerabilities:



 	
  * Prevent arbitrary code execution via Freemarker Template injection

 	
  * XXE vulnerability in GeoTools XML Parser

 	
  * XXE vulnerability in WPS Request builder

 	
  * Various library upgrades (see above) from versions with known CVEs

 	
  * Potential access to admin pages without being logged in


Thanks to Steve Ikeoka, Kevin Smith, Brad Hards, Nuno Oliveira and Andrea Aime for providing fixes to these issues.




If you encounter a security vulnerability in GeoServer, or any other open source software, please take care to report the issue in a [responsible fashion](http://docs.geoserver.org/stable/en/user/introduction/gettinginvolved.html#bug-tracking).












## About GeoServer 2.14





 	
  * [State of GeoServer 2.14](https://www.slideshare.net/jgarnett/state-of-geoserver-214) (SlideShare)

 	
  * [GeoServer Ecosystem](https://www.slideshare.net/jgarnett/geoserver-ecosystem-2018) (SlideShare)

 	
  * [GeoServer Developers Workshop](https://www.slideshare.net/jgarnett/geoserver-developers-workshop) (SlideShare)






