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

1. Copy ``release/stable`` to the number of the previous release. For example if the current release
   is ``2.5.1``:

        cp -R release/stable release/2.5.0

1. Update ``release/stable/index.html`` and the ``version`` tag in the page preamble to the 
   current version.

1. Update ``_config.yml`` and update the ``stable_version`` property to the current version.

If performing a maintenance or development release, repeat the above process replacing "stable" 
with "dev" or "maintain" accordingly. 
