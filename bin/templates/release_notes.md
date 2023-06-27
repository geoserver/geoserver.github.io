## Release notes
{% for issue_type_name in issue_type_names %}

{{issue_type_name}}:

   {% for issue in project_issues.issues %}
      {% if issue.fields.issuetype.name == issue_type_name %}
* [{{ issue.key }}]({{ jira_base_url }}/browse/{{ issue.key }}) {{ issue.fields.summary }}
      {% endif %}    
   {%- endfor %}
{%- endfor %}

For the complete list see [{{ release.name }}](https://github.com/geoserver/geoserver/releases/tag/{{ release.name }}) release notes.