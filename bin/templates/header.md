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
release: release_{{ name.split('.')[0] }}{{ name.split('.')[1].split('-')[0] }}
version: {{name}}
jira_version: {{releaseVersion.id}}
---