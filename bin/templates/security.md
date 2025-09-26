## Security Considerations

{% if urgency_level == 'urgent' %}
This release addresses security vulnerabilities and is an urgent update for production systems.
{% elif urgency_level == 'important' %}
This release addresses security vulnerabilities and is an important upgrade for production systems.
{% else %}
This release addresses security vulnerabilities for production systems.
{% endif %}

{% if urgency_level == 'urgent' and undisclosed_vulnerabilities %}
{% if concurrent_releases %}
This update is considered urgent and is released concurrently with {{ concurrent_releases|join(', ') }}. Details will be provided when everyone has had an opportunity to upgrade.
{% else %}
This update is considered urgent and is released concurrently with other maintenance releases. Details will be provided when everyone has had an opportunity to upgrade.
{% endif %}
{% endif %}

{% if disclosed_vulnerabilities %}
<!-- Disclosed vulnerabilities with CVE details -->
{% for issue in disclosed_vulnerabilities %}
* [{{ issue.key }}]({{ jira_base_url }}/browse/{{ issue.key }}) {{ issue.fields.summary }}
{% endfor %}

{% if disclosed_vulnerabilities|length > 0 %}
The use of the CVE system allows the GeoServer team to reach a wider audience than blog posts. 
{% endif %}
{% endif %}

{% if undisclosed_vulnerabilities %}
This release contains vulnerabilities that have not yet been disclosed; details will be provided later.
{% endif %}

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.

{% if disclosed_vulnerabilities %}
<!-- Helper text for updating prior announcements - not displayed in final output -->
<!--
PRIOR BLOG POST UPDATES NEEDED:
The following disclosed vulnerabilities should be added to prior release announcements:

{% for issue in disclosed_vulnerabilities %}
* [{{ issue.key }}]({{ jira_base_url }}/browse/{{ issue.key }}) {{ issue.fields.summary }}
  <!-- Fixed in: {% if issue.fields.fixVersions %}{% for version in issue.fields.fixVersions %}{{ version.name }}{% if not loop.last %}, {% endif %}{% endfor %}{% endif %} -->
{% endfor %}

Search for blog posts that need updating using these versions.
-->
{% endif %}