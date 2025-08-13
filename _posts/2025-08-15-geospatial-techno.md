---
author: Nima Ghasemloo
layout: post
title: Exploring Types of WPS Operations in GeoServer
date: 2025-08-15
categories:   
- Tutorials
---

[GeoSpatial Techno](https://www.youtube.com/@geospatialtechno) is a startup focused on geospatial information that is providing e-learning courses to enhance the knowledge of geospatial information users, students, and other startups. The main approach of this startup is providing quality, valid specialized training in the field of geospatial information.

( [YouTube](https://www.youtube.com/@geospatialtechno)
| [LinkedIn](https://www.linkedin.com/in/geospatialtechno)
| [Facebook](https://www.facebook.com/geospatialtechno)
| [X](https://twitter.com/geospatialtechn)
)

----

### Exploring Types of WPS Operations in GeoServer
This session covers the various Web Processing Service (WPS) operations available in GeoServer, emphasizing their roles within spatial data processing workflows.

For the complete video tutorial, click [here](https://www.youtube.com/watch?v=HnvPVTrouQI&list=PL_ITaxp1Ob4ssvlwT5nkMD5arveD8fxc8).

[![](https://img.youtube.com/vi/HnvPVTrouQI/0.jpg)](https://www.youtube.com/watch?v=HnvPVTrouQI&list=PL_ITaxp1Ob4ssvlwT5nkMD5arveD8fxc8)

## Introduction
The OGC WPS interface defines three mandatory operations that every compliant server must implement:

- **GetCapabilities**: Retrieves metadata about the server's available processes.
- **DescribeProcess**: Provides detailed information about a specific process.
- **Execute**: Runs a selected geospatial process with user-defined inputs.

These operations form the foundation of WPS-based geospatial analysis over the web.

**Note**: GeoServer does not include the WPS functionality by default. Follow this [tutorial](https://geoserver.org/tutorials/2025/07/06/geospatial-techno.html) to download and install the WPS extension.

**Note**: This tutorial uses GeoServer version 2.25.3. Ensure that the WPS extension matches your GeoServer version precisely to prevent compatibility issues.


## GetCapabilities
The **GetCapabilities** operation enables clients to query the server for service metadata, including available processes, supported versions, and provider details.

An example HTTP GET request for GetCapabilities:

      http://localhost:8080/geoserver/ows?service=wps&version=1.0.0&request=GetCapabilities

Key parameters:

- `service = wps`: Indicates a WPS request.
- `version = 1.0.0`: Specifies the WPS version.
- `request = GetCapabilities`: Defines the operation.

The resulting XML document provides a comprehensive overview of the WPS service, including server info, available processes, supported languages, and operational metadata.

## DescribeProcess
The **DescribeProcess** operation allows clients to request detailed information about specific processes available on the WPS server. It includes descriptions of required inputs, allowable formats, and expected outputs.

Here is an example of how this operation can be used for the `Buffer` process:

      http://localhost:8080/geoserver/ows?service=wps&version=1.0.0&request=DescribeProcess&identifier=JTS:buffer

There are four required parameters and values being passed to the WPS server:
- The service parameter is `WPS`.
- The version parameter is `1.0.0`.
- The request parameter tells the server that the operation requested is `DescribeProcess`.
- The identifier parameter tells the server what specific process is being described. Here is `JTS:buffer`.

The response XML details the process, including identifiers, title, abstract, inputs, outputs, data formats, and constraints.

## Execute
The **Execute** operation  lets clients initiate geospatial processes or algorithms. It typically involves sending a request with process details, input data, parameters, and output preferences, after which the server processes the request and returns results.

For example, you can use a pre-defined demo request such as **WPS_aggregate_1.0.xml** from the demo section to test execution. To do this, navigate to the **Demos** section and select the **Demo Requests** option. From the Request drop-down list, select **WPS_aggregate_1.0.xml** request.

This operation provides a flexible, standardized method for running geospatial analyses via the web, making advanced processing tools accessible to a broader audience.

----

In this session, we covered the OGC WPS interface standard and its main operations. To explore the full tutorial, watch the [video](https://www.youtube.com/watch?v=HnvPVTrouQI&list=PL_ITaxp1Ob4ssvlwT5nkMD5arveD8fxc8).