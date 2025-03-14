---
author: {{author}}
date: {{releaseVersion.releaseDate}}
layout: post
title: GeoServer {{name}} Release
categories:
- Announcements
{% if vulnerability %}
- Vulnerability
{% endif %}
tags:
- Release
{% if series == 'release candidate' %}
- Release Candidate
{% elif series == 'milestone' %}
- Milestone Release
{% endif %}
release: release_{{name[0:1]}}{{name[2:4]}}
version: {{name}}
jira_version: {{releaseVersion.id}}
---