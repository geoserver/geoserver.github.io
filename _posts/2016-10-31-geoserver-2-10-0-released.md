---
author: jgarnett
comments: true
date: 2016-10-31 05:29:08+00:00
layout: post
link: http://blog.geoserver.org/2016/10/31/geoserver-2-10-0-released/
slug: geoserver-2-10-0-released
title: GeoServer 2.10.0 released
wordpress_id: 2719
categories:
- Announcements
tags:
- release
- stable
---



The GeoServer team is happy to announce the release of [GeoServer 2.10.0](http://geoserver.org/release/2.10.0/). Downloads are available ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10.0/geoserver-2.10.0-bin.zip), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10.0/geoserver-2.10.0-war.zip), [dmg](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10.0/geoserver-2.10.0.dmg) and [exe](http://sourceforge.net/projects/geoserver/files/GeoServer/2.10.0/geoserver-2.10.0.exe)) along with docs and extensions.

This is the latest stable release of GeoServer intended for production systems. Please note that GeoServer 2.10.0 and GeoServer 2.9.2 include important security updates and we advise all users of GeoServer to upgrade at this time.

This release is made by Ian Turton with the help of the entire GeoServer team. It is built in collaboration with GeoTools 16.0 and GeoWebCache 1.10.0. We would like to thank everyone who provided feedback on the release candidate, ideally we would like more participation.

For more information on this release check the release notes ([2.10.0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=14401&styleName=&projectId=10000), [2.10-RC1](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?projectId=10000&version=14202) | [2.10-beta](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=13902&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) | [2.10-M0](https://osgeo-org.atlassian.net/secure/ReleaseNote.jspa?version=13102&styleName=&projectId=10000&Create=Create&atl_token=BMGO-EVM2-SZYH-VJUH%7C7713dff34af1113724212b6eff4284d334e99cc9%7Clin) ).


### Packaging and Installation





 	
  * The macOS DMG is now signed by the Open Source Geospatial Foundation which is required for the latest macOS. If you are having trouble please check System Preferences Security & Privacy and ensure that apps are allowed from "App Store and identified developers".

[![geoserver-macos-10-12](/img/uploads/geoserver-macos-10.12.png)](/img/uploads/geoserver-macos-10.12.png) macOS 10.12 System Preferences for Security and Privacy

 	
  * The windows installer is now signed by the Open Source Geospatial Foundation. Unfortunately it takes a few days for "Windows SmartScreen" to trust that the application is okay (it is marked as "not commonly downloaded" since we just created it). You will need to click "More Options" to see the option to run the application.

[![SmartScreen warning on Windows 7](/img/uploads/gs-installer-smartscreen.png)](/img/uploads/gs-installer-smartscreen.png) SmartScreen warning on Windows 7

 	
  * For those just starting out the default data directory now includes security restrictions on WFS-T functionality (restricting editing of data to the administrator account by default, it's up to the administrator to change that if they wish).[![selezione_118](/img/uploads/Selezione_118.png)](/img/uploads/Selezione_118.png)


Thanks to Michael Smith and the OSGeo for purchasing a digital certificate - this helps our open source software reach a wider audience. We would also like to extend our thanks to Larry Shaffer for digging in on the macOS and Windows requirements. The signed windows installer has been "built by hand" and we ask for [your feedback](http://geoserver.org/comm/) so Larry can put together an automated system.


### Security Considerations


Aaron Waddell reported an [XXE vulnerability](https://osgeo-org.atlassian.net/browse/GEOT-5514) in the GeoTools library which has now been fixed.

We ask all our users to treat security vulnerabilities with respect and make plans to upgrade to GeoServer 2.10.0 or GeoServer 2.9.2 at this time.


### New Style Editor


This release includes the new [Styled Editor](http://docs.geoserver.org/stable/en/user/styling/webadmin/index.html#style-editor) featured at the FOSS4G 2016 workshop. The editor mixes in the CSS editor preview and layer association abilities for more productive style development (if you are a CSS user you can go straight to the standard CSS editor now, the specific one got retired).




Here are a few screenshots. The main tab is reminiscent of the existing style editor page:

[![selezione_113](/img/uploads/Selezione_113.png)](/img/uploads/Selezione_113.png)

The publishing tab allows to link the style to layers as primary, or as associated/secondary style:

[![selezione_112](/img/uploads/Selezione_112.png)](/img/uploads/Selezione_112.png)



The preview tab is where we expect most of the work to be done, editing the style, and clicking on "Apply" to view how the changes affect the map:

[![selezione_111](/img/uploads/Selezione_111.png)](/img/uploads/Selezione_111.png)

Finally, the layer attributes tab shows the available attributes, their type, a sample value and allows to compute statistics on them:

[![selezione_114](/img/uploads/Selezione_114.png)](/img/uploads/Selezione_114.png)

We would like to thank those who attended the [FOSS4G 2016 styling workshop](http://docs.geoserver.org/stable/en/user/styling/workshop/index.html) for trying out an early milestone release. Special thanks to Andrea for extensive testing/feedback and to Torben for all the hard work during the release candidate.





### Improved QGIS style compatibility


At the FOSS4G 2016 code sprint some work was done to increase the compatibility between QGIS and GeoServer styling. While most of the work was performed on the QGIS [SLD export correctness](http://osgeo-org.1560.x6.nabble.com/FOSS4G-code-sprint-idea-improving-SLD-export-and-GeoServer-compatibility-tt5273812.html#a5283626), some work was also done on the GeoTools/GeoServer side.

First, we taught GeoServer how to handle SE/SLD 1.1 external marks, and implemented support for TTF symbols as external marks (this is how QGIS exports TTF based symbols). Here is an example of the syntax (remember, this is SE, symbology encoding, not SLD 1.0):

    
     <se:Mark>
       <se:OnlineResource xlink:type="simple" xlink:href="ttf://DNR%20Recreation%20Symbols"/>
       <se:Format>ttf</se:Format>
       <se:MarkIndex>64</se:MarkIndex>
       <se:Fill>
         <se:SvgParameter name="fill">#000000</se:SvgParameter>
       </se:Fill>
     </se:Mark>


The result is the extraction of the symbol from the true type font, and its usage in the map as a scalable vector symbol.  Here is a sample from our test suite, with lines overlaying the symbols to easily identify the point locations:

[![externalmark](/img/uploads/externalMark.png)](/img/uploads/externalMark.png)



QGIS ships with a [set of SVG symbols](https://github.com/qgis/QGIS/tree/master/images/svg) which are "interesting", in that they do not contain a fixed fill or stroke color, but parameters that need to be filled by the caller. QGIS then allows the user to specify such values, and fills them in before rendering, thus allowing to treat a SVG in a similar way to a built-in mark (with just a bit less control over the output compared to a mark). Looking at a SVG source we see:





    
    <polygon fill="param(fill)" fill-opacity="param(fill-opacity)"
      stroke="param(outline)" stroke-opacity="param(outline-opacity)"
      stroke-width="param(outline-width)"
      points="290.565,67.281 35.067,509.815 33.98,511.7 545.209,512.093 547.389,512.095 "/>


GeoServer just learned to support these parameters, which are supposed to be added in the SVG URL reference, accoding to the [SVG Parameters 1.0](https://www.w3.org/TR/SVGParamPrimer) spec "URL parameters" approach:

    
     <PointSymbolizer>
       <Graphic>
         <ExternalGraphic>
           <OnlineResource xlink:type="simple" xlink:href="firestation.svg?fill=#FF0000" />
          <Format>image/svg</Format>
         </ExternalGraphic>
         <size>128</size>
       </Graphic>
     </PointSymbolizer>


Which will result in something like:

[![firestationonlyfill](/img/uploads/firestationOnlyFill-150x150.png)](/img/uploads/firestationOnlyFill.png)

There is more work to be done - the team looked at including some of the custom QGIS "well-known" marks in GeoServer, but this work was not completed for the 2.10.0 release. If you are interested in helping out on this or other activities please contact us as a [volunteer](http://geoserver.org/comm/) or [professionally](http://geoserver.org/support/).

We would like to thank Andrea for his cross project leadership on this issue, and to the participants of the FOSS4G code sprint for helping out.





### CSS Styling Improvements


The CSS Extension now sports [nested rule](http://docs.geoserver.org/latest/en/user/styling/css/nested.html)s, allowing for even more compact styles, for example:

    
    [@scale < 3000] {
       mark: symbol(circle);
       :mark {
          fill: gray;
          size: 5
       };
       [type = 'important'] {
          mark: symbol(triangle);
          :mark {
            fill: red;
            stroke: yellow
          }
       }
    }


[Rendering transformation](http://docs.geoserver.org/latest/en/user/styling/css/transformation.html) support has also been added, for example, it's possible to extract contour lines from a raster using the following style:

    
    <span class="c">/* @title Levels */</span>
    <span class="o">*</span> <span class="p">{</span>
      <span class="n">transform</span><span class="o">:</span> <span class="n">ras</span><span class="o">:</span><span class="n">Contour</span><span class="p">(</span><span class="n">levels</span><span class="o">:</span> <span class="m">1100</span> <span class="m">1200</span> <span class="m">1300</span> <span class="m">1400</span> <span class="m">1500</span> <span class="m">1600</span> <span class="m">1700</span><span class="p">);</span>
      <span class="k">z-index</span><span class="o">:</span> <span class="m">0</span><span class="p">;</span>
      <span class="n">stroke</span><span class="o">:</span> <span class="nb">gray</span><span class="p">;</span>
      <span class="n">label</span><span class="o">:</span> <span class="p">[</span><span class="n">numberFormat</span><span class="p">(</span><span class="s1">'#'</span><span class="o">,</span> <span class="n">value</span><span class="p">)];</span>
      <span class="k">font-size</span><span class="o">:</span> <span class="m">12</span><span class="p">;</span>
      <span class="k">font</span><span class="o">-</span><span class="n">fill</span><span class="o">:</span> <span class="nb">black</span><span class="p">;</span>
      <span class="k">font-weight</span><span class="o">:</span> <span class="k">bold</span><span class="p">;</span>
      <span class="n">halo</span><span class="o">-</span><span class="k">color</span><span class="o">:</span> <span class="nb">white</span><span class="p">;</span>
      <span class="n">halo</span><span class="o">-</span><span class="n">radius</span><span class="o">:</span> <span class="m">2</span><span class="p">;</span>
      <span class="o">-</span><span class="n">gt</span><span class="o">-</span><span class="n">label</span><span class="o">-</span><span class="n">follow</span><span class="o">-</span><span class="n">line</span><span class="o">:</span> <span class="n">true</span><span class="p">;</span>
      <span class="o">-</span><span class="n">gt</span><span class="o">-</span><span class="n">label</span><span class="o">-</span><span class="k">repeat</span><span class="o">:</span> <span class="m">200</span><span class="p">;</span>
      <span class="o">-</span><span class="n">gt</span><span class="o">-</span><span class="n">label</span><span class="o">-</span><span class="n">max</span><span class="o">-</span><span class="n">angle</span><span class="o">-</span><span class="n">delta</span><span class="o">:</span> <span class="m">45</span><span class="p">;</span>
      <span class="o">-</span><span class="n">gt</span><span class="o">-</span><span class="n">label</span><span class="o">-</span><span class="n">priority</span><span class="o">:</span> <span class="m">2000</span><span class="p">;</span>
    <span class="p">}</span>




### WMTS improvements


The WMTS service has now its own service configuration page, and if the INSPIRE extension is installed, proper INSPIRE extensions. The WMTS service is also now usable on per-workspace services (aka virtual services).

![selezione_115](/img/uploads/Selezione_115.png)


### "JPEG or PNG" output format for WMS and WMTS


The relase includes support for the ["JPEG or PNG" format](http://www.geo-solutions.it/blog/geoserver-smart-transparency/), which allows the server to dynamically decide if JPEG or PNG is to be returned, based on pixel transparency. This should solve the classic scattered aerial/satellite overlay imagery dilemma, where the imagery is best compressed JPEG, except at the borders of the images, where transparency is needed.






[![selezione_119](/img/uploads/Selezione_119.png)](/img/uploads/Selezione_119.png)








### GetFeatureInfo improvements for coverages


GetFeatureInfo against raster layers now ensures valid XML names are given to attributes, for valid GML outputs, and supports continous map wrapping for geographic projections, as well as working properly for rasters whose coordinate span beyond the 180 degrees East:






[![selezione_116](/img/uploads/Selezione_116.png)](/img/uploads/Selezione_116.png)




We would like to thank Ben Caradoc-Davies for working on this.





### New projections support


GeoTools is now providing support for the Azimuthal equidistant projection:



![](https://4.bp.blogspot.com/-UBN6gDpxNaQ/V-BkebcVO6I/AAAAAAAAAUM/EbKvxsSaCiIL44py0QQacEpEVCnNtLcfwCLcB/s1600/ice-oblique-7m.png)

Support for the rotated pole projections was also added:

![selezione_117](/img/uploads/Selezione_117.png)

Rotated pole support for GRIB2/NetCDF and GeoServer integration by Ben Caradoc-Davies (Transient), with the GeoTools rotated pole projection implementation by Maciej Filocha (ICM), based on code provided by Jürgen Seib (Deutscher Wetterdienst).


### Image mosaic and image pyramid improvements


Both the image mosaic and image pyramid can now be configured to serve multiple coverages no matter what the data source (previously this was possible only if the sources were NetCDF or Grib files).

At the same time the image mosaic now allows more heterogeneous sources, adding to the previous ability of mixing different color models, a newfound ability to support heterogeneous input projections:

[![tutorial_reproj_artifact](/img/uploads/tutorial_reproj_artifact-1.png)](/img/uploads/tutorial_reproj_artifact-1.png)

Thanks to Devon Tucker for working on the heterogeneous input projections. For more information please check out the [documentation examples](http://docs.geoserver.org/latest/en/user/data/raster/imagemosaic/tutorial.html#multi-resolution-imagery-with-reprojection).


### LDAP User Group Service


The LDAP integration was previously limited to "authentication provider" status, e.g. it allowed GeoServer to validate a username/password combo by trying to connect to a LDAP service. GeoServer 2.10 ships with a LDAP based "user group service" instead, meaning, the list of users can be directly fetched from the LDAP, in alternative to the existing XML and JDBC providers.


[![selezione_120](/img/uploads/Selezione_120.png)](/img/uploads/Selezione_120.png)





## Community Modules


The GeoServer community has been very active producing a wide range of exciting capabilities. These modules are not part of a release, and are not officially supported, but most of them can be downloaded as part of our [nightly builds](http://ares.boundlessgeo.com/geoserver/2.10.x/) or built locally. If you are interested in seeing these reviewed and included in future releases of GeoServer please [reach out](http://geoserver.org/comm/) to and ask how you can help.


### YSLD community module


A new styling language, [YSLD](http://docs.geoserver.org/latest/en/user/styling/ysld/index.html), has been added. YSLD is a YAML based language which closely matches the stucture of SLD using a text only representation: indentation is used to represent document structure rather than XML tags; filters are represented using ECQL, and all GeoServer vendor options are supported (with a "x-" prefix).

YSLD allows you to cut down your style for the common case where a style has a single rule inside a single feature style - for example:

    
    - polygon:
      stroke-color: 'blue'
      stroke-width: 1
      fill-color: '#7EB5D3'
    - text:
      label: ${name}
      fill-color: 'black'
      anchor: [0.5, 0.5]
      x-maxDisplacement: 40
      x-autoWrap: 70






As a "[YAML based](http://www.yaml.org)" format common blocks of code can be defined up front, and reused multiple times.

    
    define: &stroke
     stroke-color: 'gray'
     stroke-width: 0.5
    rules:
     - filter: ${region = '1'}
       symbolizers:
       - polygon:
         <<: *stroke
         fill-color: '#8DD3C7'
     - filter: ${region = '2'}
       symbolizers:
       - polygon:
         <<: *stroke
         fill-color: '#FFFFB3'


One feature offered that is not included in SLD is integration with GeoWebCache zoom levels - this allows rules to be enabled for specific zoom levels (avoiding the need to calculate the correct scale denominators by hand).








    
    rules:
    - zoom: [min,5]
      filter: ${type = 'small'}
      symbolizers:
      - ...
    - zoom: [5,max]
      filter: ${type = 'small'}
      symbolizers:
      - ...
    - zoom: [min,5]
      else: true
      symbolizers:
      - ...
    - zoom: [5,max]
      else: true
      symbolizers:
      - ...


One interesting ability of the YSLD module that can be used to help get you started is the ability to take an existing SLD style and translate it 1-1 to YSLD using the REST API:



 	
  * Access as SLD: http://localhost:8080/geoserver/rest/styles/states.sld?pretty=true

 	
  * Access as YSLD: http://localhost:8080/geoserver/rest/styles/states.yaml



    
    <span class="l-Scalar-Plain">name</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">states</span>
    <span class="l-Scalar-Plain">title</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">Population in the United States</span>
    <span class="l-Scalar-Plain">abstract</span><span class="p-Indicator">:</span> <span class="p-Indicator">|-</span>
      <span class="no">A sample filter that filters the United States into three</span>
              <span class="no">categories of population, drawn in different colors</span>
    <span class="l-Scalar-Plain">feature-styles</span><span class="p-Indicator">:</span>
    <span class="p-Indicator">-</span> <span class="l-Scalar-Plain">name</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">name</span>
      <span class="l-Scalar-Plain">rules</span><span class="p-Indicator">:</span>
      <span class="p-Indicator">-</span> <span class="l-Scalar-Plain">name</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">Population < 2M</span>
        <span class="l-Scalar-Plain">title</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">Population < 2M</span>
        <span class="l-Scalar-Plain">filter</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">${PERSONS < '2000000'}</span>
        <span class="l-Scalar-Plain">scale</span><span class="p-Indicator">:</span> <span class="p-Indicator">[</span><span class="nv">min</span><span class="p-Indicator">,</span> <span class="nv">max</span><span class="p-Indicator">]</span>
        <span class="l-Scalar-Plain">symbolizers</span><span class="p-Indicator">:</span>
        <span class="p-Indicator">-</span> <span class="l-Scalar-Plain">polygon</span><span class="p-Indicator">:</span>
            <span class="l-Scalar-Plain">fill-color</span><span class="p-Indicator">:</span> <span class="s">'#A6CEE3'</span>
            <span class="l-Scalar-Plain">fill-opacity</span><span class="p-Indicator">:</span> <span class="l-Scalar-Plain">0.7
      ...</span>





For more information this release includes an extensive [YSLD Reference](http://docs.geoserver.org/stable/en/user/styling/ysld/reference/index.html) (complete with diagrams and examples).

[![ysld-docs](/img/uploads/ysld-docs-1.png)](/img/uploads/ysld-docs-1.png)


### WMTS-ND discovery community module


The module adds WMTS operations helping a client to drill into the domain of a dataset with multiple dimensions, helping in particular with scattered datasets, or ones with related dimensions (e.g., forecasts having two related times, execution time and predicted time). The extra operations are:



 	
  * DescribeDomains, providing a compact description of the available dimension values, and allowing to filter on a range of values for a particular dimension (space included), and see how the domain of the related dimensions change

 	
  * GetHistogram, showing how the available data is distributed along a given dimension

 	
  * GetFeature, to get footprint and dimension values of single features/rasters once a particular domain of interest has been established


The [full specification](http://demo.geo-solutions.it/share/wmts-multidim/wmts_multidim_geosolutions.html) is available online.


### ncWMS community module


The ncWMS community module adds some extra operations and style support specially geared towards multidimensional raster data (including, but not limited to, NetCDF). The operations are a subset of the WMS extension provided by [ncWMS](http://www.resc.rdg.ac.uk/trac/ncWMS/), a NetCDF-CF specific WMS server.
First, a palette oriented styling language is added that only requires to provide a list of color values, which will be applied to the declared data min/max range automatically:


[![redblue-editor](/img/uploads/redblue-editor.png)](/img/uploads/redblue-editor.png)




The palette is then going to be applied to the range of values declared in the layer bands configuration, along with a number of vendor parameter in the request to control the actual range of values to be displayed, color for out of range values, linear vs logarithic palette:




[![redblue-default](/img/uploads/redblue-default.png)](/img/uploads/redblue-default.png)


The request can also include a "animate" parameter that, coupled with the GIF output format and a dimension range, e.g., a time range, will generate an animation in output:


[![countries_flexpart](/img/uploads/countries_flexpart.gif)](/img/uploads/countries_flexpart.gif)




Finally, a GetTimeSeries request parallels GetFeatureInfo and charts/extract the evolution of the phenomenon at a given point against time (also available as a CSV dump):




[![test-flexpart](/img/uploads/test-flexpart-300x257.png)](/img/uploads/test-flexpart.png)




More details and information about the module are available in the [official documentation](http://docs.geoserver.org/stable/en/user/community/ncwms/index.html).





### Backup and restore community module


The backup/restore community module provides a UI and a set of REST service to backup and restore the GeoServer configuration without forcing a full application restart. Each operation is asynchronous, and restores can be subject to dry run, to verify if the restore will complete without errors before actually applying it.

[![usagegui006](/img/uploads/usagegui006.png)](/img/uploads/usagegui006.png)

More information about the module can be found in the [user documentation](http://docs.geoserver.org/latest/en/user/community/backuprestore/index.html).





## About GeoServer 2.10


Articles, docs, blog posts and presentations:



 	
  * [State of GeoServer 2016](http://www.slideshare.net/jgarnett/state-of-geoserver) (slideshare)

 	
  * The [style editor](http://docs.geoserver.org/latest/en/user/styling/webadmin/index.html#style-editor) has been refreshed with the best ideas from the css extension

 	
  * The [styling workshop](http://docs.geoserver.org/latest/en/user/styling/workshop/index.html) has been updated for foss4g 2016 and now includes both CSS and YSLD examples.

 	
  * [Smart transparency in GeoServer with image/vnd.jpeg-png format](http://www.geo-solutions.it/blog/geoserver-smart-transparency/) (GeoSolutions)

 	
  * [QGIS SLD export improvements](http://www.geo-solutions.it/blog/qgis-sld-export/) (GeoSolutions)


Community modules

 	
  * A new community module to [backup/restore](http://docs.geoserver.org/latest/en/user/community/backuprestore/index.html) and restore GeoServer configuration

 	
  * A resource browser is available allowing remote management of styles, icons and fonts (needs building from sources).

 	
  * A new [WMTS multidimensional domain discovery](http://demo.geo-solutions.it/share/wmts-multidim/wmts_multidim_geosolutions.html) community module for discovering patches of data in scattered data sets

 	
  * The YSLD community module has been updated with extensive [documentation](http://docs.geoserver.org/latest/en/user/styling/ysld/index.html)



