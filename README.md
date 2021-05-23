# http://geoserver.org

This repository contains the source for the Github generated [GeoServer home page](http://geoserver.org/). 

## Reporting issues

If you stumble into any issue with the GeoServer web site please report it in our [Jira issue tracker](https://osgeo-org.atlassian.net/projects/GEOS/summary).

## Developing 

The site is built with [Jekyll](https://github.com/jekyll/jekyll).

Before you start:
    
    gem install bundler jekyll jekyll-feed

Jekyll can also be run in "watch" mode for development:

    bundle exec jekyll serve --watch

The site contents will be served at [http://localhost:4000](http://localhost:4000). 

See [TEST.md](TEST.md) for more details.

## Blog

Blog posts have migrated from wordpress and are now managed as part of the website.

To create a new blog post:

1. Create a new markdown page in ``_posts`` following the filename convention for sort order:

   ``_posts/2021-05-04-may-the-fork-be-with-you.md``
   
2. The post is published using the metadata included at the top of your file.
   
   ```
   ---
   author: Andrea Aime
   date: 2021-05-04
   layout: post
   title: May the fork be with you!
   categories:
   - Developer notes
   ---
   ```
   
3. Popular categories include:
   
   * ``Developer notes``
   * ``Announcements`` -- used for project team and release announcements
   * ``Tips and Tricks``
   * ``Tutorials``
   * ``User perspectives`` 

## Releases

When a release is performed the site contents are updated to reflect the new release. Below is the 
process of updating site contents for a stable release.

1. Write a blog post announcing the new release.
   
   ```
   ---
   author: Andrea Aime
   layout: post
   title: GeoServer 2.19.3 Released
   categories:
   - Announcements
   tags:
   - Release
   release: release_219
   version: 2.19.3
   jira_version: 16816
   ---
   ```
   
   Copy one of the previous blog posts so we end up with a consistent format.
   
   The following information is used to generate a ``release/<version>/index.html`` page:
   
   * ``release``: This is the `_layout` used for the generated release page
   
   * ``version``: The GeoServer version being announced
   
   * ``jira_version``: Used to link to the release notes
     
     The value for ``jira_version`` can be found by navigating to that version on [Jira](https://osgeo-org.atlassian.net/projects/GEOS?selectedItem=com.atlassian.jira.jira-projects-plugin:release-page) and examining the URL. For example, for example, ``2.7.2`` links to ``https://osgeo-org.atlassian.net/projects/GEOS/versions/10601``, giving a ``jira_version`` of ``10601``. For a maintenance or development release, instead modify ``release/maintain/index.html`` or ``release/dev/index.html`` respectively.

4. Update ``_config.yml`` and update the ``stable_version`` property to the current version.
   
   * This change will be reflected in ``index.html`` and ``download/index.html``, and the matching release announcement post will be used to generate the ``release/stable`` page.
     
     Update ``stable_jira`` to be the same as the next release, this is used for the Nightly build page.
     
     ```
     stable_version:   2.19.1
     stable_jira:      16821
     stable_branch:    2.19.x
     ```
   
   * For a maintenance instead change ``maintain_version``, and ``maintain_jira``.
   
     ```
     maintain_version: 2.18.3
     maintain_jira:    16819
     maintain_branch:  2.18.x
     ```

5. Update the ``download/index.html`` by adding your new page to the list of releases. To find this list, do a text search for ``releases``. You should find a section that looks like this:
   
   ```
   <ul class="list-inline">
     <li><a href="/release/2.10.5">2.10.5</a></li>
     <li><a href="/release/2.10.4">2.10.4</a></li>
     <li><a href="/release/2.10.3">2.10.3/a></li>
   </ul>
   <ul class="list-inline">
     <li><a href="/release/2.10.2">2.10.2</a></li>
     <li><a href="/release/2.10.1">2.10.1</a></li>
     <li><a href="/release/2.10.0">2.10.0/a></li>
   </ul>
   <ul class="list-inline">
     <li><a href="/release/2.10-RC1">2.10-RC1</a></li>
     <li><a href="/release/2.10-beta">2.10-beta</a></li>
     <li><a href="/release/2.10-M0">2.10-M0</a></li>
   </ul>
   ```
   
   There are separate sections for `stable` and `maintenance`. Ensure you have the right section, then add a line to the top of the list for your version. Try to keep the lists balanced, and limit each list to no more than 4 items - create a third list row if necessary. Isolate milestones, beta and RC on their own row if you can.

### Development releases

When publishing a milestone, beta or release candidate:

* There is also a special section for `development` we only provide links to milestone, beta and release candidates. These releases are being made available for testing but are not recommended for production use.

* Create a new `_layouts/release_<version>.html` template by copying the previous template and adding an entry for any new extensions that have been released on the new branch.

* Create a release candidate announcement post, using your ``release: release_<version>.html`` for the generated `release` page layout.

* Update `_config.yml` update ``dev_version``, the matching release announcement post will be used to generate `release/dev/index.html` page.

  ```
  dev_version:    2.19-RC
  ```

* When no ``dev_version`` is specified `dev_branch`, `dev_jira` and `dev_series` will be used to generate a placeholder `release/dev/index.html` page.
  
  ```
  dev_branch:       main
  dev_jira:         16815
  dev_series:       2.20.x
  ```

### Final Release

When creating the final release:

1. Update the ``_config.yml`` properties:

   * Update the `maintain_version`, `maintain_jira` and `maintain_branch` using the values from `stable`.
   
   * Update the `stable_version`, `stable_jira` and `stable_branch`.
   
2. The ``dev_version``property in ``_config.yml`` should be blank (as the development period is now over).
   
   Update the `dev_branch` information. For example, if creating the branch `2.21.x`:
   
   ```
   dev_version:
   dev_branch:       main
   dev_jira:         17823
   dev_series:       2.21.x
   ```

2. When updating ``download/index.html``:
   
   * Copy the current ``maintenance`` section to the ``archived`` section
   * Copy the current ``stable`` section to the ``maintenance`` section
   * Update the ``stable`` section with the releases from the new stable branch.
