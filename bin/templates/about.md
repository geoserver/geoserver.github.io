# About GeoServer {{ series }} Series

Additional information on GeoServer {{ series }} series:

{% set docs_host = 'docs' if series.split('.')[0]|int >= 3 else 'docs-archive' -%}
* [GeoServer {{ series }} User Manual](https://{{ docs_host }}.geoserver.org/{{ series }}.x/en/user/)
{% block features %}
{% endblock %}

Release notes:
{% for version in versions %}
   {%- if loop.index0 == 0 %}
( 
   {%- else %}
|  
   {%- endif %}
 [{{version.name}}](https://github.com/geoserver/geoserver/releases/tag/{{version.name}})
{% endfor %}
)