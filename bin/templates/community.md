## Community Updates

Community module development:

{% for issue in community_updates %}
* [{{ issue.key }}]({{ jiraBaseUrl }}/browse/{{ issue.key }}) {{ issue.fields.summary }}
{% endfor %}

Community moduels are shared as source code to encourage collaboration. If a topic being explored is of interest to you please contact the module developer to offer assistance.