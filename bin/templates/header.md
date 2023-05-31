---
author: {{author}}
date: {{releaseVersion.releaseDate}}
layout: post
title: GeoServer {{name}} Release
categories:
- Announcements
tags:
- Release
{% if series == 'release candidate' %}
- Release Candidate
{% elif series == 'milestone' %}
- Milestone Release
{% endif %}
{% if vulnerability %}
- Vulnerability
{% endif %}
release: release_{{name[0:1]}}{{name[2:4]}}
version: {{name}}
jira_version: {{releaseVersion.id}}
---