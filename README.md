# http://geoserver.org

This repository contains the source for the Github generated [GeoServer home page](http://geoserver.org/). 

## Reporting issues

If you stumble into any issue with the GeoServer web site please report it in our [Jira issue tracker](https://osgeo-org.atlassian.net/projects/GEOS/summary) using the ``website`` component.

## Developing 

The site is built with [Jekyll](https://github.com/jekyll/jekyll):

#. Before you start:
    
    gem install bundler jekyll jekyll-feed jekyll-paginate

#. Jekyll can be run in "watch" mode for development:

    bundle exec jekyll serve --watch

   The site contents will be served at [http://localhost:4000](http://localhost:4000). 

   See [TEST.md](TEST.md) for more details.
   
#. Commit to ``main`` branch and the result is published to http://geoserver.org

## Blog

Blog posts are managed as part of the website.

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

When a release is performed, the site contents are updated to reflect the new release. Below is the 
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

2. Update ``_config.yml`` and update the ``stable_version`` property to the current version.
   
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

### Dev Releases

When publishing a milestone, beta or release candidate:

1. Create a new ``_layouts/release_<version>.html`` template by copying the previous template and adding an entry for any new extensions that have been released on the new branch.

   This is the value used for ``release`` when making your announcement blog posts.
  
2. Update ``_config.yml`` update ``dev_version``, the matching release announcement post will be used to generate `release/dev/index.html` page.

   ```
   dev_version:    2.19-RC
   ```
   
4. When no ``dev_version`` is specified `dev_branch`, `dev_jira` and `dev_series` will be used to generate a placeholder `release/dev/index.html` page.
  
   ```
   dev_branch:       main
   dev_jira:         16815
   dev_series:       2.20.x
   ```

3. Update the `main_series`, and `main_jira` to reflect the new version number for `main` branch, this will be used to generate a placeholder for `release/main/index.html` page.
   ```
   main_jira:         16829
   main_series:       2.21.x
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

## Technical Details

### Jekyll Build 

The Jekyll build process [goes through several steps](https://jekyllrb.com/tutorials/orderofinterpretation/):

1. The file `_config.yml` is parsed into [Jekyll::Site](https://github.com/jekyll/jekyll/blob/master/lib/jekyll/site.rb)
   
   * ``site.data`` 
   
1. Makes an inventory of existing content:
   
   * ``site.pages`` contains instances of [Jekyll::Page](https://github.com/jekyll/jekyll/blob/master/lib/jekyll/page.rb) for each page (and post) defined.
   
   * ``site.static_files`` contains [Jekyll::StaticFile](https://github.com/jekyll/jekyll/blob/master/lib/jekyll/static_file.rb)

2. Our custom plugin `_plugins/release.rb` generator is run:
   
   * Processes the posts in ``site.pages``, add additional [Jekyll::PageWithoutAFile](https://github.com/jekyll/jekyll/blob/master/lib/jekyll/page_without_a_file.rb) entries to ``site.pages``
   * Creates a ``site.data.releases`` data structure listing all the releases found for use by the `download/index.html` page.

3. Additional plugins are run:
   
   * jekyll-feed: generates an Atom feed of all the posts
   * jekyll-paginate: uses `_blog/index.html` as a template to generate `page2.html`, `page3.html`, ... `page80.html`

4. At this point all the ``site.pages`` are created each containing:
   
   * ``page.title``
   * ``page.content``
   * ``page.url``
   * ``page.date``
   * ``page.id``
   * ``page.dir``
   * ``page.name``
   * ``page.data`` provided by front-matter at the top of the file
   
   Release pages have:
   
   * ``page.data.version``
   * ``page.data.jira_version``
   * ``page.data.release_date``
   * ``page.data.announce``
   
4. Jekyll process any pages with [Liquid](https://jekyllrb.com/docs/liquid/) into static files in the `_site` folder.
   
   * Variable reference use ``{{`` and ``}}``:
   
     ```
     Download the latest [GeoServer {{site.stable_version}}](/release/stable/index.html) release.
     ```
     
   * Variable filters use ``|`` pipe character to define a processing chain:
   
     ```
     Released {{ page.date | date_to_long_string }}.
     ```
   
   * Tags used to define control flow:
     
     ```
     {% for release in site.data.releaes | where: "series", "2.19"  %}
       {{ release.version }}
     {% endfor %}
     ```
   
   Here is a decent [cheatsheet](https://gist.github.com/JJediny/a466eed62cee30ad45e2) for reference.
   
### Publishing

Commit to `main` and the result is published.

Technical details:

1. Commit to the `main` branch.

2. Workflow [.github/workflows/build-jekyll.yml](.github/workflows/build-jekyll.yml) action is triggered.
   
   * Uses ``ubuntu-latest`` environment
   
   * Uses [JEKYLL DEPLOY ACTION](https://github.com/jeffreytse/jekyll-deploy-action)
   
     * Runs Jekyll build to generate static files (just like normal)
     
     * Commits the resulting static files to the [gh-pages](https://github.com/geoserver/geoserver.github.io/tree/gh-pages) branch

3. GitHub pages settings is configured to publish the `gh-pages` branch to `https://geoserver.github.io`.
  
   * The CNAME `geoserver.org` is used but we have yet to obtain the domain from Planet Federal.
   
   The content is available as the https:/geoserver.org website
