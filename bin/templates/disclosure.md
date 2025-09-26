<!-- Template for generating content to update prior blog posts with disclosed vulnerabilities -->

## Security Disclosure Update

The following vulnerabilities have been publicly disclosed and should be added to prior release announcements:

{% for issue in disclosed_vulnerabilities %}
**{{ issue.key }}** - {{ issue.fields.summary }}
{% if issue.fields.fixVersions %}
- Fixed in: {% for version in issue.fields.fixVersions %}{{ version.name }}{% if not loop.last %}, {% endif %}{% endfor %}
{% endif %}

- JIRA Link: [{{ issue.key }}]({{ jira_base_url }}/browse/{{ issue.key }})

{% endfor %}

## Blog Posts That Need Updating

Based on the fix versions above, search for and update the following blog post patterns:
{% set updated_versions = [] %}
{% for issue in disclosed_vulnerabilities %}
  {% if issue.fields.fixVersions %}
    {% for version in issue.fields.fixVersions %}
      {% if version.name not in updated_versions %}
        {% set _ = updated_versions.append(version.name) %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% for version in updated_versions %}
- `{{ version.replace('.', '-') }}-released.md` (GeoServer {{ version }} release announcement)
{% endfor %}

## Security Section Text to Add

For each blog post listed above, add or update the Security Considerations section with:

```markdown
## Security Considerations

This release addresses security vulnerabilities and is considered an important upgrade for production systems.

{% for issue in disclosed_vulnerabilities %}
* [{{ issue.key }}]({{ jira_base_url }}/browse/{{ issue.key }}) {{ issue.fields.summary }}
{% endfor %}

The use of the CVE system allows the GeoServer team to reach a wider audience than blog posts.

See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.
```

## Instructions

1. Search for each blog post file listed above in the `_posts/` directory
2. Find the Security Considerations section (or add one if it doesn't exist)
3. Add the vulnerability details as shown above
4. Commit and push the changes to update all affected announcements