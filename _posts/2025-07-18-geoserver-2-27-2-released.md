---
author: Peter Smythe
date: 2025-07-18
layout: post
title: GeoServer 2.27.2 Release
categories:
- Announcements
tags:
- Release
release: release_227
version: 2.27.2
jira_version: 17209
--- 

<div style="text-align: center; margin: 20px 0;">
  <iframe src="https://portal.ogc.org/public_ogc/compliance/srv_ogc_compliance_badge2.php?id=102&pid=1846" 
          width="250"
          frameborder="0"
          style="float: right; margin: 0 0 10px 15px; border: none; height: auto; min-height: 1000px">
  </iframe>
</div>

GeoServer [2.27.2](/release/2.27.2/) release is now available
with downloads
([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.2/geoserver-2.27.2-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.2/geoserver-2.27.2-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.2/GeoServer-2.27.2-winsetup.exe/download)), along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.2/geoserver-2.27.2-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.27.2/extensions/).

This is a stable release of GeoServer recommended for production use.
GeoServer 2.27.2 is made in conjunction with GeoTools 33.2, and GeoWebCache 1.27.2. 

Thanks to Peter Smythe (AfriGIS) for making this release. 

## CITE certification achieved

The GeoServer team are really pleased to announce that our long-lost CITE Certification has been regained (for 2.27) over the last 6 months.

OGC CITE Certification is important for two reasons:

* Provides a source of black-box testing ensuring that each GeoServer release behaves as intended.
* Provides a logo and visibility for the project helping to promote the use of open standards.

Many thanks to all who were involved!  After approximately 10 years, we can once again officially confirm that GeoServer is OGC compliant.  Thank you especially to [Gaia3D](https://gaia3d.com/) and [OSGeo:UK](https://uk.osgeo.org/) for sponsorship covering the expense of CITE Certification for 2025.

For more details, please read the [separate announcement]({% post_url 2025-07-16-cite-certification %}).

## Release notes

New Feature:

* [GEOS-11805](https://osgeo-org.atlassian.net/browse/GEOS-11805) Option to disable the management of stored queries

Improvement:

* [GEOS-11877](https://osgeo-org.atlassian.net/browse/GEOS-11877) Improve CoverageView composition to support noData fill on missing bands/coverages

Bug:

* [GEOS-10728](https://osgeo-org.atlassian.net/browse/GEOS-10728) Cannot download GeoPackage if the source data contains UUID types
* [GEOS-11708](https://osgeo-org.atlassian.net/browse/GEOS-11708) STAC breadcrumbs rendering as plain text
* [GEOS-11820](https://osgeo-org.atlassian.net/browse/GEOS-11820) WCS spatial sub-setting does not work when native CRS != declared CRS
* [GEOS-11832](https://osgeo-org.atlassian.net/browse/GEOS-11832) count=0 service exception for some formats
* [GEOS-11857](https://osgeo-org.atlassian.net/browse/GEOS-11857) Random NPE In LocalWorkspaceCallback
* [GEOS-11862](https://osgeo-org.atlassian.net/browse/GEOS-11862) Layer Preview and Tile Layers page dropdown links broken after updating table
* [GEOS-11865](https://osgeo-org.atlassian.net/browse/GEOS-11865) MapDownloadProcess washes out 1 band gray images when transparency is on
* [GEOS-11866](https://osgeo-org.atlassian.net/browse/GEOS-11866) Prevent requests setting variables that should only be set by GeoServer
* [GEOS-11879](https://osgeo-org.atlassian.net/browse/GEOS-11879) Xalan causes a java.lang.NoClassDefFoundError

Task:

* [GEOS-11831](https://osgeo-org.atlassian.net/browse/GEOS-11831) OseoDispatcherCallback improvements
* [GEOS-11834](https://osgeo-org.atlassian.net/browse/GEOS-11834) Update PMD to 7.13
* [GEOS-11882](https://osgeo-org.atlassian.net/browse/GEOS-11882) Cleanup postgis-jdbc dependencies

For the complete list see [2.27.2](https://github.com/geoserver/geoserver/releases/tag/2.27.2) release notes. 

## Community Updates

We list these community modules purely as a service to the community to raise awareness of interesting add-ons to support, if there is sufficient common interest.  They are not "production ready".

How to make contact: browse the GitHub repo ([https://github.com/geoserver/geoserver/tree/main/src/community](https://github.com/geoserver/geoserver/tree/main/src/community) > module > History) to see who 
* a) made the original commit, 
* b) has been making changes (other than refactoring/dependency updates).

If you want to use a community module (in production), YOU need to arrange funding to 
* a) promote it to an official extension (passing tests, etc.) and 
* b) maintain it going forward.

Community module development:

* [GEOS-11727](https://osgeo-org.atlassian.net/browse/GEOS-11727) OGC API Tiles tests require tile links to be available in the collections resource too
* [GEOS-11728](https://osgeo-org.atlassian.net/browse/GEOS-11728) OGC API Tiles returns an invalid content-disposition header
* [GEOS-11822](https://osgeo-org.atlassian.net/browse/GEOS-11822) OGC API procesess basic implementation
* [GEOS-11829](https://osgeo-org.atlassian.net/browse/GEOS-11829) Features templating ability to override schema
* [GEOS-11830](https://osgeo-org.atlassian.net/browse/GEOS-11830) Smart data loader create store page fails when environment variables are in use
* [GEOS-11839](https://osgeo-org.atlassian.net/browse/GEOS-11839) New Community Module for WPS Download in NetCDF output format for spatiotemporal coverages
* [GEOS-11847](https://osgeo-org.atlassian.net/browse/GEOS-11847) Next link is missing in "Search" OGC API - Features proposal implementation when startIndex is not set
* [GEOS-11870](https://osgeo-org.atlassian.net/browse/GEOS-11870) Singlestore(MemSql) datastore community module
* [GEOS-11871](https://osgeo-org.atlassian.net/browse/GEOS-11871) Allow native execution of group by in DGGS store, when grouping on geometries
* [GEOS-11874](https://osgeo-org.atlassian.net/browse/GEOS-11874) Align OGC API tiles API spec with specification
* [GEOS-11875](https://osgeo-org.atlassian.net/browse/GEOS-11875) Execute OGC API Tiles CITE tests
* [GEOS-11876](https://osgeo-org.atlassian.net/browse/GEOS-11876) WPS Vertical Longitudinal Profile: Support automatic distance computation
* [GEOS-11878](https://osgeo-org.atlassian.net/browse/GEOS-11878) WFS HITS request returns the whole data records on a GML feature templated layer
* [GEOS-11880](https://osgeo-org.atlassian.net/browse/GEOS-11880) OGC API Maps is not showing up in GeoServer home page
* [GEOS-11883](https://osgeo-org.atlassian.net/browse/GEOS-11883) OGC API process description lacks links
* [GEOS-11884](https://osgeo-org.atlassian.net/browse/GEOS-11884) OGC API process HTML input/outputs lack occurrences and formats

# About GeoServer 2.27 Series

Additional information on GeoServer 2.27 series:

* [GeoServer 2.27 User Manual](https://docs.geoserver.org/2.27.x/en/user/)
* [GeoServer 2025 Q2 Developer Update]({% post_url 2025-05-13-developer-update %}) 
* [GeoServer 2025 Roadmap]({% post_url 2025-01-13-roadmap %}) 
* [Content-Security-Policy Headers](https://github.com/geoserver/geoserver/wiki/GSIP-227)
* [OGCAPI Features Extension](https://github.com/geoserver/geoserver/wiki/GSIP-230)
* [File system access isolation](https://github.com/geoserver/geoserver/wiki/GSIP-229)
* [Promote data dir catalog loader to core](https://github.com/geoserver/geoserver/wiki/GSIP-231)

Release notes:
( [2.27.2](https://github.com/geoserver/geoserver/releases/tag/2.27.2)
| [2.27.1](https://github.com/geoserver/geoserver/releases/tag/2.27.1)
| [2.27.0](https://github.com/geoserver/geoserver/releases/tag/2.27.0)
) 

