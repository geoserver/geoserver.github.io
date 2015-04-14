# http://geoserver.org

This repository contains the source for the Github generated [GeoServer home page](http://geoserver.org/). 

## Developing 

The site is built with [Jekyll](https://github.com/jekyll/jekyll). To perform a single build of the site:

    jekyll build

The site contents will result in the ``_site`` directory.

Jekyll can also be run in "watch" mode for development:

    jekyll serve -w

The site contents will be served at http://localhost:4000. 

## Releases

When a release is performed the site contents are updated to reflect the new release. Below is the 
process of updating site contents for a stable release.

1. Update ``release/stable/index.html`` with the details of your new release. The the ``version`` tag in the page preamble to the current version, and the ``jira_version`` are required. This is the number after ``fixforversion`` in links to that version on [Jira](https://jira.codehaus.org/browse/GEOS#selectedTab=com.atlassian.jira.plugin.system.project%3Aversions-panel), for example, ``https://osgeo-org.atlassian.net/projects/GEOS/versions/10160`` for ``2.7-RC1`` has ``jira_version`` of ``10160``.

2. Copy stable to the appropriate version number (so your blog post has something to link to). For example if the ``version`` is ``2.5.2`` make a copy using:

        cp -R release/stable release/2.5.2

3. Update the ``release/2.8.x/index.html`` with the next ``jira_version`` from the roadmap on [ Jira](https://osgeo-org.atlassian.net/projects/GEOS?selectedItem=com.atlassian.jira.jira-projects-plugin:release-page). This is the number after ``fixforversion`` in links to that version, for example, ``https://osgeo-org.atlassian.net/projects/GEOS/versions/10163`` for ``2.8-beta`` has ``jira_version`` of ``10163``.

4. Update ``_config.yml`` and update the ``stable_version`` property to the current version. This change will be reflected on ``index.html`` and ``download/index.html``.

5. Update the ``download/index.html` by adding your new page to the list.

If performing a maintenance or development release, repeat the above process replacing "stable" 
with "dev" or "maintain" accordingly.

If creating a new branch, change the entries for "maintain", "stable", and "dev" to reflect the new branch identities.
