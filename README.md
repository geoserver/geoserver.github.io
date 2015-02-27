# http://geoserver.org

This repository contains the source for the Github generated http://geoserver.org. 

## Developing 

The site is built with [Jekyll](https://github.com/jekyll/jekyll). To perform a single build of the site:

    jekyll build

The site contents will result in the ``_site`` directory.

Jekyll can also be run in "watch" mode for development:

    jekyll serve -w

The site contents will be served at http://localhost:4000. 

## Releases

When a release is performed the site contents is updated to reflect the new release. Below is the 
process of updating site contents for a stable release.

1. Update ``release/stable/index.html`` with the details of your new release. The the ``version`` tag in the page preamble to the current version, and the jira_version are required. 

2. Copy stable to the appropriate version number (so your blog post has something to link to). For example if the ``version`` is ``2.5.2`` make a copy using:

        cp -R release/stable release/2.5.2

3. Update the ``release/2.5.x/index.html`` with the next jira_version from the roadmap.

4. Update ``_config.yml`` and update the ``stable_version`` property to the current version. This change will be reflected on ``index.html`` and ``download/index.html``.

5. Update the ``download/index.html` by adding your new page to the list.

If performing a maintenance or development release, repeat the above process replacing "stable" 
with "dev" or "maintain" accordingly. 
