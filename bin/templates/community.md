## Community Updates

Community module development:

{% for issue in community_updates %}
* [{{ issue.key }}]({{ jira_base_url }}/browse/{{ issue.key }}) {{ issue.fields.summary }}
{% endfor %}

Community modules are shared as source code to encourage collaboration. If a topic being explored is of interest to you, please contact the module developer to offer assistance.