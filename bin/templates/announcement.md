GeoServer [{{release}}](/release/{{release}}/) release is now available
with downloads (
[bin](https://sourceforge.net/projects/geoserver/files/GeoServer/{{release}}/geoserver-{{release}}-bin.zip/download),
[war](https://sourceforge.net/projects/geoserver/files/GeoServer/{{release}}/geoserver-{{release}}-war.zip/download),
[windows](https://sourceforge.net/projects/geoserver/files/GeoServer/{{release}}/GeoServer-{{release}}-winsetup.exe/download))
, along with 
[docs](https://sourceforge.net/projects/geoserver/files/GeoServer/{{release}}/geoserver-{{release}}-htmldoc.zip/download) and
[extensions](https://sourceforge.net/projects/geoserver/files/GeoServer/{{release}}/extensions/).

{% block description %}
{% endblock %}

{%- if dependency is defined and dependency|length > 0 -%}
GeoServer {{name}} is made in conjunction with 
   {%- for project,version in dependency -%}
      {%- if loop.index0 != 0 -%}
      , 
      {%- endif %}
      {%- if loop.index == dependency|length and dependency|length > 1 %}
 and 
      {%- endif %}
 {{project}} {{version}}
   {%- endfor -%}
. 
{% endif %}

Thanks to {{author}} for making this release.