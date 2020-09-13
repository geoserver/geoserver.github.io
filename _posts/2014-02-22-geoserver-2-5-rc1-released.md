---
author: geoserver
comments: true
date: 2014-02-22 22:07:27+00:00
layout: post
link: http://blog.geoserver.org/2014/02/22/geoserver-2-5-rc1-released/
slug: geoserver-2-5-rc1-released
title: GeoServer 2.5-RC1 Released
wordpress_id: 1796
categories:
- Announcements
---

The GeoServer team is happy to announce the release of [GeoServer 2.5-RC1](http://geoserver.org/display/GEOS/GeoServer+2.5-RC1). Download bundles are provided ([zip](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5-RC1/geoserver-2.5-RC1-bin.zip/download), [war](http://sourceforge.net/projects/geoserver/files/GeoServer/2.5-RC1/geoserver-2.5-RC1-war.zip), [dmg](http://downloads.sourceforge.net/geoserver/geoserver-2.5-RC1.dmg) and [exe](http://downloads.sourceforge.net/geoserver/geoserver-2.5-RC1.exe))  along with documentation and extensions.

GeoServer 2.5 is shaping up to be a great milestone and we would like to thank all those who have downloaded 2.5-beta and submitted feedback and pull requests.



	
  * A couple map rendering issues have been fixed with better white space handling for CSS labels and crisp SVG symbols rendering.

	
  * Konstantin Surzhin has provided many small user interface fixes

	
  * Mauro Bartolomeoli has been untangling a conflict between the css extension and the printing modules.

	
  * Thanks to Andrea for his hard work, and constant review of pull requests.

	
  * Thanks to Jody Garnett and Boundless facilitating this weeks release.

	
  * Check the [release notes](https://jira.codehaus.org/secure/ReleaseNote.jspa?projectId=10311&version=19927) for more details

	
  * This release is made in conjunction with [GeoTools 11-RC1](http://geotoolsnews.blogspot.com.au/2014/02/geotools-11-rc1-released.html).


With all this help GeoServer 2.5 is on track for release in March. We would like to encourage you to download the release candidate and test with your data. This will both help you avoid any surprises, and assist the team in bringing you the best possible GeoServer.


# About GeoServer 2.5


Articles and resources for GeoServer 2.5 series:



	
  * GeoServer 2.5-beta announcement reviews [key features of this release](http://blog.geoserver.org/2014/01/21/geoserver-2-5-beta-released/):

	
    * WCS 2.0 and WCS 2.0 Earth Observation have been added (thanks to DLR and Eumesat for funding this)

	
    * The addition of a batch importer to making setting up GeoServer easier (thanks to [MapStory](http://mapstory.org/)).

	
    * High performance PNG encoder based on [PNGJ library](https://code.google.com/p/pngj/) (Andrea Aime). Improved JPEG performance using [libjpegturbo](http://libjpeg-turbo.virtualgl.org/) available as an optional extension (Simone Giannecchini and Daniele Romagnoli)

	
    * Use of ST_Simplify to improve PostGIS rendering performance (a collaboration with Andrea and Jonathan Moules).

	
    * New implementation of GetFeatureInfo that takes into account symbol shapes, offsets, and dynamic line widths into account (thanks to Eskilstuna municipality for funding this).




	
  * [Using GeoServer at IGN to create new digital maps](http://blog.geoserver.org/2014/01/07/using-geoserver-at-ign-the-french-national-mapping-agency-to-create-new-digital-maps/) is an impressive look at advanced styling deployed by the french mapping agency

	
  * [Labelling a MultiPoint geometry with WPS](http://boundlessgeo.com/2014/02/labelling-a-multipoint-geometry-with-wps/) (Boundless) is a good example of integrating WPS and Styling

	
  * [Achieving extreme GeoServer Scalability with new Marlin vector rasterizer](http://geo-solutions.blogspot.it/2014/02/geoserver-improved-scalability.html) (GeoSolutions) shows an exciting JRE extension that can be used for improved performance. If you are using GeoServer with a large number of CPU cores you owe yourself an hour to try this out.

	
  * [DXF output format promoted to official extension for GeoServer](http://geo-solutions.blogspot.it/2014/01/geoserver-dxf.html) (GeoSolutions)

	
  * [Active Directory based security in GeoServer through LDAP](http://geo-solutions.blogspot.it/2014/01/geoserver-activedirectory.html) (GeoSolutions)



