---
author: Andrea Aime
date: 2021-12-13
layout: post
title: Log4J2 zero day vulnerability assessment
categories:
- Announcements
---

The Java world has been taken by storm, last week, by the Log4J2 Log4Shell vulnerability, code [CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228), which allows remote code execution by simply making API calls to the vulnerable servers. The understanding of the vulnerability is still evolving and the reports are being updated, we are monitoring them closely and adapting as needed. **The following information is based on our current understanding of the vulnerability and will be updated as new information is released**.

Let us state this clearly: **GeoServer, following our own investigation, as well as our understanding of the reported vulnerability, is not vulnerable to CVE-2021-44228 since it does not use Log4J2!**

In more detail, GeoServer uses Log4J 1.2.17 and it is crucial to understand that Log4J and Log4J2 are not the same library: the 2 is in the name, it is not just a version number, Log4J2 is a full rewrite of Log4J. As a consequence GeoServer is not vulnerable in the same way reported in [CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228): our current understanding is that it cannot be made to perform a remote code execution by simply crafting an appropriate HTTP request. 

However, **Log4J 1.2 has smaller vulnerabilities**, which may trigger when loading the configuration files. It happens if the attacker manages to:

* Get write access to the GeoServer log configuration files.
* Set up in them a new JMSAppender configuration, in which the TopicConnectionFactoryBindingName or TopicBindingName point to a remote server providing malicious classes.
* Force GeoServer to reload the logging configuration.

Log4J 1.2.17 is also vulnerable to [CVE-2019-17571](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17571). This is even narrower than the issue above, as the SocketServer class needs to be run from the command line explicitly.

**That said, It is important to note that GeoServer default configuration is not vulnerable to these and the attacker would need to go and modify the logging configuration files in order to trigger it.**

### Checking for vulnerabilities

How to check if your server is vulnerable:
* Check the [log configuration files](https://docs.geoserver.org/stable/en/user/configuration/logging.html), make sure there is no JMSAppender.
* Make sure that no one outside of your organization can get write access to the logging configuration files, e.g.:
   * No one outside your organization has admin access to GeoServer. The REST API allows writing in the data directory using the [resource endpoint](https://docs.geoserver.org/stable/en/user/rest/api/resources.html), and if the [web resource extension](https://docs.geoserver.org/latest/en/user/configuration/tools/resource/install.html) is installed, admins will also be allowed to edit the files via the GUI.
   * No one outside your organization has console access to the server (e.g, SSH, terminal services), and if they do, they don’t have write permission to the GeoServer configuration files.


### Threat elimination
The GeoServer project has released a sanitized version of the Log4J 1.2.17 library, which simply does not include the classes involved in vulnerabilities [CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228) and [CVE-2019-17571](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17571). **This library is also usable with older versions of GeoServer**. 

The file is available in [our Nexus repository](https://repo.osgeo.org/repository/geotools-releases/log4j/log4j/1.2.17.norce/log4j-1.2.17.norce.jar). Simply remove the existing log4j-1.2.17.jar and drop in the new [log4j-1.2.17.norce.jar](https://repo.osgeo.org/repository/geotools-releases/log4j/log4j/1.2.17.norce/log4j-1.2.17.norce.jar) in the geoserver/webapps/WEB-INF/lib folder, and then restart tomcat.

We are also aware that Log4J 1.2.17 is an “End Of Life” (EOL) project, and are actively looking for funding to perform an upgrade to more recent versions of them. All new logging libraries have a different API and a different configuration file layout, with potential backwards compatibility issues, so this will be likely done on newer versions of GeoServer (2.21.x).
