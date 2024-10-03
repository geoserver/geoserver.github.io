---
author: Peter Smythe
date: 2024-09-02
layout: post
title: GeoServer 2.26-M0 Release
categories:
- Announcements
tags:
- Release
version: 2.26-M0
--- 

# Hey, we need your help, please!

One of the frameworks that GeoServer is built upon is [Apache Wicket](https://wicket.apache.org/), and it needs to be upgraded to a later, supported version.  This is a substantial change that potentially affects every GUI (graphical user interface) page, so we are asking the **GeoServer community** to review each GUI page to check if there are any failures that need to be handled manually.  As a user, you are the very best people to do this testing, as you are most familiar with the GUI, and it's a great way for you to relieve some of the pressure on the over-worked developers.  **Here's how you can help**:

## Every GUI page!?!

You do not need to review every single page, if the task is broken down into bite-sized chunks and split across multiple testers!  That's what [this spreadsheet](https://docs.google.com/spreadsheets/d/1pQmncG4zxpgJnHxeI4myFfOBD17U2CIMcy59II4XAfo/edit) intends to coordinate.  Please pick pages that are familiar to you and that have not already been checked by another helpful volunteer.  Update the spreadsheet to indicate that you have tested a page and document any strange results for a developer to investigate further.

## How do I spot the differences?

We would like you to compare the new milestone 2.26-M0 version against the latest stable version (2.25.3), by opening 2 browser tabs and performing the same action in each tab, to see if the GUI is identical.  It should look the same; if not, please indicate on the testing spreadsheet for someone else to double check.

## How do I run the new milestone 2.26-M0 version?

### Docker

If you (or your DevOps team) are already using a Docker image with your own data, that's wonderful, you're half way there.  (`docker pull docker.osgeo.org/geoserver:2.26-M0`)

If not, we have packaged 2.26-M0 as a Docker image as the most portable way to distribute the task to you.  You need Docker installed ([https://docs.docker.com/get-started/get-docker/](https://docs.docker.com/get-started/get-docker/)) and then you need to configure it to run with the extensions and community modules that you're familiar with.  Even more preferable would be if you can also run it using your own data.  You should refer to the configuration instructions in the [README.md](https://github.com/geoserver/docker)

_BTW, this is also a great opportunity, if you have been thinking about it, for your company to make the switch to a containerised version - we're here to assist you with getting started, if you assist us with the testing!  Also, once you have set up Docker and your own data, you will be in a fine position to respond to our pleas to test release candidates (both major and minor) with your own data, prior to the release being made - so that you know it will work for you!  Win-win!_

Here's a simple example to work from:

```
  docker run -p8081:8080 --rm --name geoserver-2-26-M0 \
	--mount src="my-local-drive/my-GEOSERVER_DATA_DIR",target=/opt/geoserver_data/,type=bind \
	--mount src="my-local-drive/my-directory-with-extensions",target=/opt/additional_libs,type=bind \
	docker.osgeo.org/geoserver:2.26-M0  
```

Here's a more comprehensive example to work from:

```
  docker run -p8081:8080 --rm --name geoserver-2-26-M0 \
	--env CATALINA_OPTS="-Xms1024m -Xmx4096m -DALLOW_ENV_PARAMETRIZATION=true-this-is-another-way-of-defining-env-variables " \
	--env INSTALL_EXTENSIONS=true --env STABLE_EXTENSIONS="authkey,css,monitor,web-resource,gwc-s3,geopkg-output,sqlserver,charts,vectortiles" \
	--env POSTGRES_JNDI_ENABLED=true \
	--mount src="my-local-drive/my-jndi-context.xml",target=/opt/config_overrides/context.xml,type=bind \
	--mount src="my-local-drive/my-GEOSERVER_DATA_DIR",target=/opt/geoserver_data/,type=bind \
	--mount src="my-local-drive/my-directory-with-extensions",target=/opt/additional_libs,type=bind \
	--mount src="my-local-drive/geoserver-environment.properties",target=/opt/environment/geoserver-environment.properties,type=bind \
	--env ALLOW_ENV_PARAMETRIZATION=true --env ENV_PROPERTIES=/opt/environment/geoserver-environment.properties \
	docker.osgeo.org/geoserver:2.26-M0  
```
Ref: more on [environment-variables](https://github.com/geoserver/docker?tab=readme-ov-file#environment-variables)

You can then access GeoServer in your browser on: [http://localhost:8081/geoserver/web/](http://localhost:8081/geoserver/web/)

### Binary package

The normal binary package (and extensions/community modules) are also available via SourceForge: [https://sourceforge.net/projects/geoserver/files/GeoServer/2.26-M0/](https://sourceforge.net/projects/geoserver/files/GeoServer/2.26-M0/)

Remember to install this new version on a different port e.g. 8081 so that you can run the 2 versions side by side for comparison.

Ref: [installation instructions](https://docs.geoserver.org/latest/en/user/installation/index.html)

## I want to run all the extensions!

Great!  Here's the full list to include in the command above:

> app-schema,authkey,cas,charts,control-flow,css,csw-iso,csw,db2,dxf,excel,feature-pregeneralized,gdal,geofence,geofence-server,geofence-wps,geopkg-output,grib,gwc-s3,h2,imagemap,importer,inspire,jp2k,libjpeg-turbo,mapml,mbstyle,metadata,mongodb,monitor,mysql,netcdf-out,netcdf,ogr-wfs,ogr-wps,oracle,params-extractor,printing,pyramid,querylayer,rat,sldservice,sqlserver,vectortiles,wcs2_0-eo,web-resource,wmts-multi-dimensional,wps-cluster-hazelcast,wps-download,wps-jdbc,wps,xslt,ysld

### And community modules too:

> acl,activeMQ-broker,backup-restore,cog-azure,cog-google,cog-http,cog-s3,colormap,cov-json,datadir-catalog-loader,dds,elasticsearch,features-autopopulate,features-templating,flatgeobuf,gdal-wcs,gdal-wps,geopkg,gpx,graticule,gs-jwt-headers,gsr,gwc-azure-blobstore,gwc-distributed,gwc-mbtiles,gwc-sqlite,hz-cluster,iau,importer-jdbc,jdbcconfig,jdbc-metrics,jdbcstore,jms-cluster,libdeflate,mbtiles,mbtiles-store,mongodb-schemaless,monitor-kafka,ncwms,netcdf-ghrsst,notification,ogcapi-coverages,ogcapi-dggs,ogcapi-features,ogcapi-images,ogcapi-maps,ogcapi-styles,ogcapi-tiled-features,ogcapi-tiles,ogr-datastore,opensearch-eo,pgraster,proxy-base-ext,s3-geotiff,sec-keycloak,sec-oauth2-geonode,sec-oauth2-github,sec-oauth2-google,sec-oauth2-openid-connect,smart-data-loader,solr,spatialjson,stac-datastore,taskmanager-core,taskmanager-s3,vector-mosaic,vsi,webp,web-service-auth,wfs-freemarker,wps-longitudinal-profile,wps-remote

## Show me an example of what I am looking for

TODO screenshots

#### I get you, it's actually quite quick and easy to do, because I already know the GUI from using it.

Precisely.  That's why we're reaching out for YOUR help.

## But I already use a different GeoServer Docker image

It should be relatively easy to translate the config from your current Docker image to the [OSGeo Docker images](https://docker.osgeo.org/repository/geoserver-docker/v2/geoserver/manifests/2.26-M0) built from the [OSGeo Docker repo](https://github.com/geoserver/docker), which is the only place that 2.26-M0 is readily available from.  If you (or your Docker image provider) want to make 2.26-M0 available for others to use, please send us the link.  

You can then compare your current Docker image to 2.26-M0.

## There are errors in the browser console window!!!

You're a Geek for looking!  

Thanks, you can ignore the CSP (Content Security Policy) errors, for now.  You're welcome to highlight others in the spreadsheet, but we're looking for visible differences in the GUI actually.


# Thank you for your help. This is an important step towards our spring-framework-6 roadmap.
