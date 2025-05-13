---
author: Jody Garnett
date: 2025-03-17
layout: post
title: GeoServer 2.22.6 Release
categories:
- Announcements
- Vulnerability
tags:
- Release
release: release_222
version: 2.22.6
jira_version: 16898
--- 

GeoServer [2.22.6](/release/2.22.6/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.6/geoserver-2.22.6-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.6/geoserver-2.22.6-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.6/GeoServer-2.22.6-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.6/geoserver-2.22.6-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.22.6/extensions/).

This series has previously reached end-of-life, with this release issued to address a security vulnerability. Please apply this update as a mitigation measure only, and plan to upgrade to a stable or maintenance release of GeoServer.
GeoServer 2.22.6 is made in conjunction with GeoTools 28.6. 

Thanks to Jody Garnett (GeoCat) and Andrea Aime (GeoSolutions) for making this release. 

## Security Considerations

This release addresses security vulnerabilities for those operating in a Java 8 environment:

* [CVE-2024-36401](https://github.com/geoserver/geoserver/security/advisories/GHSA-6jj6-gm7p-fcvv) Remote Code Execution (RCE) vulnerability in evaluating property name expressions (Critical)
  
  For more information see the following [statement]({% post_url 2024-09-12-cve-2024-36401 %}).

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed. 

## Java 8 End-of-life

This GeoServer 2.22.6 is archived and has reached end-of-life. This release uses recent GeoTools 28.6 Java 8 artifacts addressing [CVE-2024-36404](https://github.com/geotools/geotools/security/advisories/GHSA-w3pj-wh35-fq8w).

All future releases will require a minimum of Java 11.

## Release notes

Improvement:

* [GEOS-11102](https://osgeo-org.atlassian.net/browse/GEOS-11102) Allow configuration of the CSV date format
* [GEOS-11116](https://osgeo-org.atlassian.net/browse/GEOS-11116) GetMap/GetFeatureInfo with groups and view params can with mismatched layers/params
* [GEOS-11155](https://osgeo-org.atlassian.net/browse/GEOS-11155) Add the X-Content-Type-Options header
* [GEOS-11246](https://osgeo-org.atlassian.net/browse/GEOS-11246) Schemaless plugin performance for WFS

Bug:

* [GEOS-11138](https://osgeo-org.atlassian.net/browse/GEOS-11138) Jetty unable to start  cvc-elt.1.a / org.xml.sax.SAXParseException

Task:

* [GEOS-11318](https://osgeo-org.atlassian.net/browse/GEOS-11318) Upgrade postgresql from 42.6.0 to 42.7.2

For the complete list see [2.22.6](https://github.com/geoserver/geoserver/releases/tag/2.22.6) release notes. 

## Community Updates

Community module development:

* [GEOS-11412](https://osgeo-org.atlassian.net/browse/GEOS-11412) Remove reference to JDOM from JMS Cluster (as JDOM is no longer in use)

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance. 

# About GeoServer 2.22 Series

Additional information on GeoServer 2.22 series:

* [GeoServer 2.22 User Manual](https://docs.geoserver.org/2.22.x/en/user/)
* [Update Instructions](https://docs.geoserver.org/latest/en/user/installation/upgrade.html)
* [Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/metadata/index.html)
* [CSW ISO Metadata extension](https://docs.geoserver.org/latest/en/user/extensions/csw-iso/index.html)
* [State of GeoServer](https://docs.google.com/presentation/d/1mnOFSvYb8npVudvUR5MSjSTFHc6ZQ_bStafZrBV7LZ8/edit?usp=sharing) (FOSS4G Presentation)
* [GeoServer Beginner Workshop](https://docs.google.com/presentation/d/1fbPLN-1Cs95WK-IxDG1PxCEKyHwFbNBGNkkomxmLr0Y/edit?usp=sharing) (FOSS4G Workshop)
* [Welcome page](https://docs.geoserver.org/latest/en/user/webadmin/welcome.html) (User Guide)

Release notes:
( [2.22.6](https://github.com/geoserver/geoserver/releases/tag/2.22.6)
| [2.22.5](https://github.com/geoserver/geoserver/releases/tag/2.22.5)
| [2.22.4](https://github.com/geoserver/geoserver/releases/tag/2.22.4)
| [2.22.3](https://github.com/geoserver/geoserver/releases/tag/2.22.3)
| [2.22.2](https://github.com/geoserver/geoserver/releases/tag/2.22.2)
| [2.22.1](https://github.com/geoserver/geoserver/releases/tag/2.22.1)
| [2.22.0](https://github.com/geoserver/geoserver/releases/tag/2.22.0)
| [2.22-RC](https://github.com/geoserver/geoserver/releases/tag/2.22-RC)
| [2.22-M0](https://github.com/geoserver/geoserver/releases/tag/2.22-M0)
) 

