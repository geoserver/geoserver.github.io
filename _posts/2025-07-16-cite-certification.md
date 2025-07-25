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

### Developer Documentation

For developers, read more about the [certification process](https://docs.geoserver.org/latest/en/developer/cite-test-guide/index.html#cite-certification) and how to expand on it for additional services.

## CITE Certification Sponsorship

Thank you to [Gaia3D](https://gaia3d.com/) and [OSGeo:UK](https://uk.osgeo.org/) for sponsorship covering the expense of CITE Certification for 2025.

This certification process is expensive, and we will require sponsorship for 2026 if we wish to maintain certified status. 

However, as mentioned above, these CITE tests are automatically run as part of our build process for each new pull request, so we can **unofficially** verify that we pass CITE tests, but we cannot claim to be compliant.

If you/your organization finds the CITE Certification valuable, please contact the Project Steering Committee to sponsor the annual renewal.  The more organizations that are able to sponsor, the lower the expense will be to each organization (sharing the approx USD $1,000 per year cost).
