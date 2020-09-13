---
author: geoserver
comments: true
date: 2010-01-26 17:51:22+00:00
layout: post
link: http://blog.geoserver.org/2010/01/26/securing-restful-services-with-geoserver-2-0-1/
slug: securing-restful-services-with-geoserver-2-0-1
title: Securing RESTful Services with GeoServer 2.0.1
wordpress_id: 438
categories:
- Announcements
- Developer notes
---

A feature that has become quite popular in GeoServer over the last year has been the [RESTful configuration plug-in](http://docs.geoserver.org/2.0.x/en/user/extensions/rest/index.html) ("restconfig"),  that allows one to configure a GeoServer instance programmatically via simple HTTP operations.

Recently the issue of security has come up with regards to the restconfig plug-in. Essentially it boils down to the fact that GeoServer allows anonymous access to any resource or service when the HTTP request method is GET. In the case of restconfig this can make sensitive information available anonymously such as database connection parameters which can contain passwords and the like.

To remedy this situation in 2.0.1 the GeoServer security subsystem has been extended to allow for configuring access to RESTful services. This is documented in the [user guide](http://docs.geoserver.org/2.0.x/en/user/security/sec_rest.html).

The major caveat for users upgrading to 2.0.1 is that any systems that depended on the previous behavior of allowing GET access to resources without authentication will undoubtedly break. In this case users have two options:




  
  1. Start supplying administrator credentials with all requests
  
  2. [Reconfigure](http://docs.geoserver.org/2.0.x/en/user/security/sec_rest.html#providing-anonymous-read-only-access) GeoServer to allow for anonymous access for GET operations


A [patch](http://blog.geoserver.org/2010/01/26/rest-security-update-for-1-7-x/) has been created for 1.7.x users as well.

Try it out. Please report any issues to the [GeoServer users list](mailto:geoserver-users@lists.sourceforge.net). Thanks for using GeoServer!
