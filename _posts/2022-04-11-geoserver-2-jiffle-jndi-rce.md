---
author: Andrea Aime
date: 2022-04-11
layout: post
title: Jiffle and GeoTools RCE vulnerabilities
categories:
- Vulnerability
---

A few critical vulnerabilities have been located in the GeoServer ecosystem that 
allow Remote Code Execution. This article describes the vulnerabilities, their mitigation,
and links to patched versions of the various projects involved.

All the issues described in this post have been patched in:

* GeoServer [2.20.4](/release/2.20.4/), [2.19.6](/release/2.19.6/) or [2.18.6](/release/2.198.6/)
* GeoWebCache [1.20.2](https://sourceforge.net/projects/geowebcache/files/geowebcache/1.20.2/), [1.19.3](https://sourceforge.net/projects/geowebcache/files/geowebcache/1.19.3/) or [1.18.5](https://sourceforge.net/projects/geowebcache/files/geowebcache/1.18.5/)
* GeoTools [26.4](https://sourceforge.net/projects/geotools/files/GeoTools%2026%20Releases/26.4/), [25.6](https://sourceforge.net/projects/geotools/files/GeoTools%2025%20Releases/25.6/) or [24.6](https://sourceforge.net/projects/geotools/files/GeoTools%2025%20Releases/24.6/)
* JAI-EXT [1.1.22](https://github.com/geosolutions-it/jai-ext/releases/tag/1.1.22)

The rest of the POST describes the issues and their mitigation.

## RCE in Jiffle

The Jiffle map algebra language, provided by jai-ext, allows efficiently execute map algebra over large images.
A vulnerability has been recently found in Jiffle, that allows a Code Injection to be performed by properly crafting a Jiffle invocation.

In the case of GeoServer, the injection can be performed from a remote request.

### Assessment

**GeoTools** includes the Jiffle language as part of the ``gt-process-raster-<version>`` module, applications
using it should check whether it's possible to provide a Jiffle script from remote, and if so, upgrade
or remove the functionality (see also the GeoServer mitigation, below).

**Stand-alone GeoWebCache** is not affected, as it does not include Jiffle support.

The issue is of particular interest for **GeoServer** users, as GeoServer embeds Jiffle in the base WAR
package. Jiffle is available as a OGC function, for usage in SLD rendering transformations.

This allows for a Remote Code Execution in properly crafted OGC requests, as well as from the
administration console, when editing SLD files.

### Mitigations

In case you cannot upgrade at once, then the following mitigation is strongly recommended:

1. Stop GeoServer
2. Open the war file, get into ``WEB-INF/lib`` and remove the ``janino-<version>.jar``
3. Restart GeoServer.

This effectively removes the Jiffle ability to compile scripts in Java code, from any of the potential
attack vectors (Janino is the library used to turn the Java code generated from the Jiffle script,
into executable bytecode). 

GeoServer should still work properly after the removal, but any attempt to use Jiffle will result in an exception.

### Resolution

Issue:

* [GEOS-10458](https://osgeo-org.atlassian.net/browse/GEOS-10458) Upgrade to JAI-EXT 1.1.22

## RCE in JNDI lookups

The GeoTools data stores, as well as the disk quota mechanism of GeoWebCache, and the JDBC user/role
providers for GeoServer can all fetch connection pools from JNDI.

A properly crafted JNDI source name can cause uncontrolled deserialization of classes and eventually
a Remote Code Execution, in a way similar to Log4Shell. However, unlike Log4Shell, it requires the
administrator to enter these strings.

### Mitigations

In terms of mitigation, **GeoTools** users should make sure the JNDI strings given to stores cannot
be provided from remote, or external parties, without validation.

**Stand-alone GeoWebCache** users must now allow external or remote users to change the 
disk quota XML configuration files, guarding both local file system access, and the REST
configuration API. The REST API can only be accessed authenticating as administrator, 
good practices in this regard involve:
- Disallowing remote access to the "/rest" endpoint in a GeoWebCache installation
- Rotating the administrator passwords.

GeoServer is affected though the Web administration interface and the REST configuration API,
both of which require an administrator login to be used in order to setup JNDI connection strings.
In order to mitigate the issue:
- Disallow remote access to the "/rest" and "/web" endpoints in a GeoServer installation.
- Change/rotate the administrator passwords.

### Resolution

The following issues have been resolved, and patched releases are available.

Issue:

* [GEOT-7115](https://osgeo-org.atlassian.net/browse/GEOT-7115) Streamline JNDI lookups

Thanks to Andrea Aime (GeoSolutions) for working so hard on this fix.

## SpringShell

Both GeoServer and GeoWebCache use Spring MVC, for REST API controllers in both projects,
and for the OGC API, GSR and taskmanager community  modules, in GeoServer.
The projects are commonly deployed as WAR files in Tomcat, with a fair amount of deploys
using Java 11 and above.

This sets up both projects for exploit via the [SpringShell vulnerability](https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement).
however we [looked]({% post_url 2022-04-01-spring %}), and could not find an actual attack vector.

This release train updates to newer a version of spring-framework that patched this potential issue.

### Mitigations

For those that cannot upgrade, the recommended mitigations are:
- Run GeoServer and GeoWebCache on Java 8 instead, which is not vulnerable to the issue.
- Upgrade Tomcat to [the releases that patched the attack vector](https://spring.io/blog/2022/04/01/spring-framework-rce-mitigation-alternative), either 9.0.62 or 8.5.78 (don't try to use Tomcat 10.x, GeoServer cannot run on it due to incompatible J2EE libraries).
- For extra security, limit access to the REST API, and remove community modules providing new service endpoints (OGC API, GSR, taskmanager).

### Resolution

Although GeoServer [assessment]({% post_url 2022-04-01-spring %}) did not identify any issue
we have now updated the the spring framework library.

Issue:

* [GEOS-10445](https://osgeo-org.atlassian.net/browse/GEOS-10445) Upgrade springframework from
  5.1.20.RELEASE to 5.2.20.RELEASE

Thanks to Gabriel Roldan (camptocamp) for troubleshooting and performing this spring-framework update.
