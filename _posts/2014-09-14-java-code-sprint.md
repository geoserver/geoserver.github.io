---
author: geoserver
comments: true
date: 2014-09-14 05:29:22+00:00
layout: post
link: http://blog.geoserver.org/2014/09/14/java-code-sprint/
slug: java-code-sprint
title: Java Code Sprint
wordpress_id: 2002
categories:
- Behind The Scenes
tags:
- foss4g
- sprint
---

## **Day 1 Quality Assurance**


Thanks to the [foss4g](https://2014.foss4g.org) and [WhereCampPDX](http://wherecamppdx.org) for


### Automated Testing with CITE Team Engine


Andrea and Justin have lead the charge updating the GeoServer CITE tests (see [Cite Sprint](https://github.com/geoserver/geoserver/wiki/CITE%20Sprint)).

The goals are initially modest: enable developers (other than Justin) to setup and run CITE tests.

Justin is working on updating our "easy to use" CITE test harness build, while the others are hitting the latest version of the CITE tests and checking both ends, tests and GeoServer, for errors (and finding issues on both sides): Andrea Aime is working WCS tests, Mauro Bartolomeoli on the WFS ones, Jared Erickson and Brad Hards on the WMS ones.


### GeoServer Manual Testing with 2.6 Nightly


Our plea to test 2.6-RC1 was not incredibly successful, so we are in for a bit of manual testing:



	
  * [2.6-beta released](http://blog.geoserver.org/2014/07/24/geoserver-2-6-beta-released/) <-- contains our "help please" test request

	
  * [2.6-x Nightly Build](http://geoserver.org/release/2.6.x/) <-- update: fixed download link for nightly releases


Thanks: Cristiane Andrioli, Flavio Conde, Ivan Martinez

Random fixes:

	
  * Update link for nightly release (Jody)

	
  * Nightly build is running again (Justin)

	
  * Documentation for weather symbols, custom WKT symbols, bulk custom WKT geometry

	
  * Testing of marlin, install instructions, package as geoserver extensions (Chris Marx, Ian Turton)

	
  * Testing Oracle+Curved test (Ian Turton)




## **GeoServer Day 2**


If you would like to join us tomorrow:



	
  * Sunday, September 14th: Boundless is arranging facilities at [nedspace](http://nedspace.com/) from 10am-4pm.


