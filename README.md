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

1. Update ``release/stable/index.html`` with the details of your new release. The ``version``, ``jira_version``, and ``release_date`` should all be updated. The value for ``jira_version`` can be found by navigating to that version on [Jira](https://osgeo-org.atlassian.net/projects/GEOS?selectedItem=com.atlassian.jira.jira-projects-plugin:release-page) and examining the URL. For example, for example, ``2.7.2`` links to ``https://osgeo-org.atlassian.net/projects/GEOS/versions/10601``, giving a ``jira_version`` of ``10601``. For a maintenance or development release, instead modify ``release/maintain/index.html`` or ``release/dev/index.html`` respectively. You can also update the value of ``jira_version`` in ``release/2.7.x/index.html`` to be the same as this latest release.

2. Copy stable to the appropriate version number (so your blog post has something to link to). For example if the ``version`` is ``2.7.2`` make a copy using:

        cp -r release/stable release/2.7.2

   For a maintenance or development release, instead copy ``release/maintain`` or ``release/dev`` respectively.

4. Update ``_config.yml`` and update the ``stable_version`` property to the current version. This change will be reflected in ``index.html`` and ``download/index.html``. For a maintenance or development release, instead change ``maintain_version`` or ``dev_version`` respectively.

5. Update the ``download/index.html`` by adding your new page to the list of releases. To find this list, do a text search for ``releases``. You should find a section that looks like this:

        <ul class="list-inline">
          <li><a href="/release/2.7.2">2.7.2</a></li>
          <li><a href="/release/2.7.1.1">2.7.1.1</a></li>
          <li><a href="/release/2.7.1">2.7.1</a></li>
          <li><a href="/release/2.7.0">2.7.0</a></li>
        </ul>
        <ul class="list-inline">
          <li><a href="/release/2.7-RC1">2.7-RC1</a></li>
          <li><a href="/release/2.7-beta">2.7-beta</a></li>
        </ul>

   There are seperate sections for each of stable, maintenance and development. Ensure you have the right section, then add a line to the top of the list for your version. Try to keep the lists balanced, and limit each list to no more than 4 items - create a third list row if necessary.

If creating a new release branch, there are a few additional steps that are required:

1. Change all the entries for ``release/maintain/index.html``, ``release/stable/index.html``, ``release/maintain/index.html``, and ``release/dev/index.html`` to reflect the new branch identities.

2. Update  the ``stable_version``, ``maintain_version``, and ``dev_version`` properties in ``_config.yml``. ``dev_version`` should be blank.

3. When updating ``download/index.html``, copy the current ``maintenance`` section to the ``archived`` section, copy the current ``stable`` section to the ``maintenance`` section, and update the ``stable`` section with the releases from the new stable branch.

4. Create the download page for nightly builds. For example, if creating the branch ``2.8.x``, copy ``releases/2.7.x/`` to ``releases/2.8.x`` and update ``index.html`` with the appropriate versions.
