## Security Considerations

This release addresses security vulnerabilities and is considered an essential upgrade for production systems.

{% for issue in vulnerabilities %}
* [{{ issue.key }}]({{ jira_base_url }}/browse/{{ issue.key }}) {{ issue.fields.summary }}
{%- endfor %}


See project [security policy](https://github.com/geoserver/geoserver/blob/main/SECURITY.md) for more information on how security vulnerabilities are managed.