## Release notes
{% for issueTypeName in issueTypeNames %}

{{issueTypeName}}:

   {% for issue in projectIssues.issues %}
      {% if issue.fields.issuetype.name == issueTypeName %}
* [{{ issue.key }}]({{ jiraBaseUrl }}/browse/{{ issue.key }}) {{ issue.fields.summary }}
      {% endif %}    
   {%- endfor %}
{%- endfor %}

For the complete list see [{{ release.name }}](https://github.com/geoserver/geoserver/releases/tag/{{ release.name }}) release notes.