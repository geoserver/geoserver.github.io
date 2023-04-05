---
author: Jody Garnett
layout: post
title: OGC Filter Injection Vulnerability Statement
date: 2023-02-20
categories:   
- Vulnerability
---

A vulnerability has located in the GeoTools Library that allows SQL Injection using OGC Filter and Function expressions.

* [CVE-2023-25157 OGC Filter SQL Injection Vulnerabilities](https://github.com/geoserver/geoserver/security/advisories/GHSA-7g5f-wrx8-5ccf) (GeoServer)
* [CVE-2023-25158 OGC Filter SQL Injection Vulnerabilities](https://github.com/geotools/geotools/security/advisories/GHSA-99c3-qc2q-p94m) (GeoTools)

If you wish to report a security vulnerability, see instructions on [responsible reporting](http://geoserver.org/issues/).
We also welcome [your direct financial support](https://github.com/geoserver/geoserver/wiki/Sponsor).

Assessment
----------

SQL Injection Vulnerabilities have been found with:

* ``PropertyIsLike`` filter, when used with a String field and any relational database based Store, or with a PostGIS DataStore with encode functions enabled, or with any image mosaic with an index stored in a relational database.
* ``strEndsWith`` function, when used with a PostGIS DataStore with encode functions enabled
* ``strStartsWith`` function, when used with a PostGIS DataStore with encode functions enabled
* ``FeatureId`` filter, when used with any database table having a String primary key column and when prepared statements are disabled
* ``jsonArrayContains`` function, when used with a String or JSON field and with a PostGIS or Oracle DataStore (GeoServer 2.22.0+ only)
* ``DWithin`` filter, when used with an Oracle DataStore

Mitigation
----------

We recommend upgrading. The following list of mitigations is addressing some of the issues (e.g., the `PropertyIsLike` issue has no mitigation for tables with a string field):

1. Disabling the PostGIS Datastore *encode functions* setting to mitigate ``strEndsWith``, ``strStartsWith`` (will cause severe slowdowns in parts of the WMTS multidimensional plugin functionality, if in use).
2. Enabling the PostGIS DataStore *preparedStatements* setting to mitigate the ``FeatureId`` vulnerability.
3. No mitigation is available for ``PropertyIsLike`` filter, you may choose to disable database DataStores until you are able to upgrade.
4. No mitigation is available for ``DWithin`` with Oracle DataStore, you may choose to disable Oracle DataStores until you are able to upgrade.
5. As a good practice to limit the attack surface, it's important to give the database account used for connection pools the minimum required level of privileges (e.g., read-only unless WFS-T/importer/REST granule harvesting are used, access limited only to the schemas and tables needed for production usage)

Resolution
----------

Issues:

* [GEOT-7302 Escape user inputs in SQL queries](https://osgeo-org.atlassian.net/browse/GEOT-7302)
* [GEOS-10842 Escape user inputs in SQL queries](https://osgeo-org.atlassian.net/browse/GEOS-10842)
* [GEOS-10839 Add JDBC Configuration parameter to disable SQL comments and pretty-printing](https://osgeo-org.atlassian.net/browse/GEOS-10839)
  
  A related issue with the community jdbc-config module.

Patched releases:

* [GeoServer 2.23.0]({% post_url 2023-04-05-geoserver-2-23-0-released %}) scheduled release
* [GeoServer 2.22.2]({% post_url 2023-02-20-geoserver-2-22-2-released %}) stable release
* [GeoServer 2.21.4]({% post_url 2023-02-20-geoserver-2-21-4-released %}) maintenance
* [GeoServer 2.20.7]({% post_url 2023-02-20-geoserver-2-20-7-released %}) 
* [GeoServer 2.19.7]({% post_url 2023-02-20-geoserver-2-19-7-released %})
* [GeoServer 2.18.7]({% post_url 2023-02-20-geoserver-2-18-7-released %})

If you wish to volunteer to backport these fixes to other GeoServer series and make a release co-ordinate on the [developers list](https:/devel/). If you are not in a position to collaborate reach out to a [commercial support provider](https:/support) to act on your behalf. 

Thanks to [Steve Ikeoka](https://github.com/sikeoka) for responsibly reporting and fixing these issues. Thanks to Jody Garnett (GeoCat) for the stable and maintenance releases. Thanks to Andrea Aime (GeoSolutions) for back porting this fix to versions of GeoTools and GeoServer that are otherwise no longer receiving releases.
