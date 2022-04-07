---
author: Andrea Aime
date: 2022-04-11
layout: post
title: Critical vulnerability patches, GeoServer 2.20.4 and GeoServer 2.19.6 Released
categories:
- Announcements
tags:
- Release
release: release_220
version: 2.20.4
jira_version: 16838
---

A couple of critical vulnerabilities have been located in the GeoServer ecosystem that 
allow Remote Code Execution. This article describes the vulnerabilities, their mitigation,
and links to patched versions of the various projects involved.

All the issues described in this post have been patched in:
* JAI-EXT 1.1.22
* GeoTools 26.4 and 25.6
* GeoWebCache 1.20.2 or 1.19.2
* GeoServer 2.20.4 or 2.19.6

The rest of the POST describes the issues and their mitigation.

RCE in Jiffle
=============

The Jiffle map algebra language, provided by jai-ext, allows efficiently excute map algebra over large images.
A vulnerability has been recently found in it, that allows to perform a Code Injection by properly crafting a Jiffle invocation. In the case of GeoServer, the injection can be performed from a remote request.

Mitigations
-----------

**GeoTools** includes the Jiffle language as part of the ``gt-process-raster-<version>`` module, applications
using it should check whether it's possible to provide a Jiffle script from remote, and if so, upgrade
or remove the functionality (see also the GeoServer mitigation, below).

**Stand-alone GeoWebCache** is not affected, as it does not include Jiffle support.

The issue is of particular interest for **GeoServer** users, as GeoServer embeds Jiffle in the base WAR
package, and exposes it as a OGC function, for usage in SLD rendering transformations, allowing for a Remote Code Execution in properly crafted OGC requests, as well as from the administration console, while editing SLD files.
In case you cannot upgrade at once, then the following mitigation is strongly recommended:

- Stop GeoServer
- Open the war file, get into ``WEB-INF/lib`` and remove the ``janino-<version>.jar``
- Restart GeoServer.

This effectively removes the Jiffle ability to compile scripts in Java code, from any of the potential
attack vectors (Janino is the library used to turn the Java code generated from the Jiffle script, into executable bytecode). 
GeoServer should still work properly after the removal, but any attempt to use Jiffle will result in an exception.

RCE in JNDI lookups
===================

The GeoTools data stores, as well as the disk quota mechanism of GeoWebCache, and the JDBC user/role
providers for GeoServer can all fetch connection pools from JNDI.

A properly crafted JNDI source name can cause uncontrolled deserialization of classes and eventually
a Remote Code Execution, in a way similar to Log4Shell. However, unlike Log4Shell, it requires the
administrator to enter these strings.

Mitigations
-----------

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

SpringShell
-----------

Both GeoServer and GeoWebCache use Spring MVC, for REST API controllers in both projects,
and for the OGC API, GSR and taskmanager community  modules, in GeoServer.
The projects are commonly deployed as WAR files in Tomcat, with a fair amount of deploys
using Java 11 and above.

This sets up both projects for exploit on the [SpringShell vulnerability](https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement). We looked, and could
not find an actual attack vector yet, but this release train contains updated Spring that patches
the potential issue.

For those that cannot upgrade, the recommended mitigations are:
- Run GeoServer and GeoWebCache on Java 8 instead, which is not vulnerable to the issue.
- Upgrade Tomcat to [the releases that patched the attack vector](https://spring.io/blog/2022/04/01/spring-framework-rce-mitigation-alternative), either 9.0.62 or 8.5.78 (don't try to use Tomcat 10.x, GeoServer cannot run on it due to incompatible J2EE libraries).
- For extra security, limit access to the REST API, and remove community modules providing new service endpoints (OGC API, GSR, taskmanager).

GeoServer 2.20.4 release
------------------------

GeoServer [2.20.4](/release/2.20.4/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.4/geoserver-2.20.4-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.4/geoserver-2.20.4-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.4/GeoServer-2.20.4-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.4/geoserver-2.20.4-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.20.4/extensions/).

This is a stable release of the 2.20.x series recommended for production systems. This release was made in conjunction with GeoTools 26.4.

Thanks to everyone who contributed, and to Andrea Aime (GeoSolutions) for making this release.

GeoServer 2.19.6 release
------------------------

GeoServer [2.19.6](/release/2.19.6/) release is now available with downloads ([bin](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.6/geoserver-2.19.6-bin.zip/download), [war](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.6/geoserver-2.19.6-war.zip/download), [windows](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.6/GeoServer-2.19.6-winsetup.exe/download)), along with [docs](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.6/geoserver-2.19.6-htmldoc.zip/download) and [extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/2.19.6/extensions/).

This is an extra maintenance release of the 2.19.x series recommended for production systems. This release was made in conjunction with GeoTools 25.6.

Thanks to everyone who contributed, and to Andrea Aime (GeoSolutions) for making this release.

GeoWebCache releases
--------------------

Release artifacts for GeoWebCache can be found on SourceForge:

- GeoWebCache [1.20.2](https://sourceforge.net/projects/geowebcache/files/geowebcache/1.20.2/)
- GeoWebCache [1.19.2](https://sourceforge.net/projects/geowebcache/files/geowebcache/1.19.2/)
