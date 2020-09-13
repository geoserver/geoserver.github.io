---
author: geoserver
comments: true
date: 2015-12-23 16:54:46+00:00
layout: post
link: http://blog.geoserver.org/2015/12/23/geoserver-explorer-plugin-for-qgis/
slug: geoserver-explorer-plugin-for-qgis
title: GeoServer Explorer Plugin for QGIS
wordpress_id: 2458
categories:
- Developer notes
- Elsewhere
---

Victor Olaya has just [announced](http://boundlessgeo.com/2015/12/announcing-the-new-geoserver-qgis-plugin/) the QGIS GeoServer Explorer plugin which uses the REST API to configure GeoServer.  This plugin serves as a QGIS-based tool to configure and manage GeoServer catalogs, acting as a GUI for GeoServer.

[caption id="attachment_2459" align="aligncenter" width="514" caption="Browsing GeoServer Catalog"][![](http://geoserver.wpengine.com/wp-content/uploads/2015/12/qgis_plugin_screensnap1.png)](http://blog.geoserver.org/2015/12/23/geoserver-explorer-plugin-for-qgis/qgis_plugin_screensnap/)[/caption]

The GeoServer Explorer plugin also wraps up some QGIS functionality making it possible to perform operations that go beyond the capabilities of the REST API and easily perform more complex workflows:



	
  * For instance, uploading a layer in a format not supported by the REST API is done in the same way as uploading a simple shapefile. The plugin will take care of converting its format before uploading, without the user noticing it. Pre-upload hooks can be set up, to process all layers before they are published (for instance, running some topology check or a geometry simplification routine.)

	
  * Styling can be defined in QGIS using its symbology tools and will be converted to SLD when publishing a layer. This allows a layer to be published with the same style as it has when rendered as part of a QGIS project.


The GeoServer Explorer plugin integrates with other QGIS plugins, like the Processing framework. This allows easy automation of tasks such as publishing a set of layers or seeding a GWC layer, and these tasks can also be integrated in workflows using the QGIS Processing Graphical modeler.

[caption id="attachment_2460" align="aligncenter" width="487" caption="QGIS GeoServer Explorer REST API Integration"][![QGIS GeoServer Explorer REST API Integration](http://geoserver.wpengine.com/wp-content/uploads/2015/12/qgis_plugin_diagram1.png)](http://blog.geoserver.org/2015/12/23/geoserver-explorer-plugin-for-qgis/qgis_plugin_diagram/)[/caption]


## QGIS GeoExplorer Plugin


The GeoServer Explorer plugin is available in the QGIS plugins server, and can now be downloaded from within QGIS using the plugin manager.

[caption id="attachment_2467" align="aligncenter" width="511" caption="GeoServer Explorer Installation"][![GeoServer Explorer Installation](http://geoserver.wpengine.com/wp-content/uploads/2015/12/qgis_plugin_install1.png)](http://blog.geoserver.org/2015/12/23/geoserver-explorer-plugin-for-qgis/qgis_plugin_install/)[/caption]

For developers the source code is available on github ([https://github.com/boundlessgeo/qgis-geoserver-plugin](https://github.com/boundlessgeo/qgis-geoserver-plugin)), [GPL](https://github.com/boundlessgeo/qgis-geoserver-plugin/blob/master/LICENSE.txt) with details on how to [contribute](https://github.com/boundlessgeo/qgis-geoserver-plugin/blob/master/CONTRIBUTING.rst).

We would like to thank Victor for his hard work, the community members who encouraged this release, and Boundless for making this plugin available for wider use. We look forward to seeing continued GeoServer and QGIS community collaboration.
