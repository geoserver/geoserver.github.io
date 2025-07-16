---
author: Peter Smythe
date: 2025-07-16
layout: post
title: CITE Certification achieved
categories:
- Announcements
tags:
- Release
--- 

<div style="text-align: center; margin: 20px 0;">
  <iframe src="https://portal.ogc.org/public_ogc/compliance/srv_ogc_compliance_badge2.php?id=102&pid=1846" 
          width="250"
          frameborder="0"
          style="float: right; margin: 0 0 10px 15px; border: none; height: auto; min-height: 1500px">
  </iframe>
</div>

# CITE Certification

The GeoServer team are really pleased to announce that our long-lost CITE Certification has been regained (for 2.27) over the last 6 months.

OGC CITE Certification is important for two reasons:

* Provides a source of black-box testing ensuring that each GeoServer release behaves as intended.
* Provides a logo and visibility for the project helping to promote the use of open standards.

Recent activity:

* As part of a Camptocamp organized ``OGC API - Features`` sprint **Gabriel** was able setup a GitHub workflow restoring the use of CITE testing for black-box testing of GeoServer. Gabriel focused on ``OGC API - Features`` certification but found WMS 1.1 and WCS 1.1 tests would also pass out of the box, providing a setup for running the tests in each new pull request.
* **Andrea** made further progress certifying the output produced by GeoServer, restoring the WMS 1.3, WFS 1.0 and WFS 1.1 tests, as well as upgrading the test engine to the latest production release. In addition, CITE tests that weren’t run in the past have been added, like WFS 2.0 and GeoTIFF, while other new tests are in progress, like WCS 2.0, WMTS 1.0 and GeoPackage.
* **Peter** set up multiple GeoServers for the testing and to act as reference implementations (hosting graciously provided by the Open Source Geospatial Foundation) and ran the test suites.
* **Angelos** Tzotsos (OSGeo) submitted the certification request to OGC.
* **Gobe** Hobona (OGC) approved all of our submissions.

Many thanks to all who were involved!  After approximately 10 years, we can once again officially confirm that GeoServer is OGC compliant.

Restoring CITE Compliance has been a project goal for a number of years, and an ongoing sponsorship goal for the GeoServer project. Many thanks to prior sponsors of this activity including Gaia3D, and OSGeo:UK.

## Documentation

For developers, read more about the [certification process](https://docs.geoserver.org/latest/en/developer/cite-test-guide/index.html#cite-certification) and how to expand on it.

## The Bad News

This certification process is expensive, and we no longer have funding to repeat it.  However, as mentioned above, these CITE tests are automatically run as part of our build process for each new pull request, so we can **unofficially** verify that we remain OGC compliant - and that is our guarantee to you.

But, if you/your company finds the CITE Certification valuable to your business, then you should please contact the PSC to offer to fund the annual renewal.  The more companies are able to do this, the more the financial load (approx USD 1000 per year) can be shared.

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
( [2.27.1](https://github.com/geoserver/geoserver/releases/tag/2.27.1)
| [2.27.0](https://github.com/geoserver/geoserver/releases/tag/2.27.0)
) 

