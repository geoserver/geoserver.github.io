# Building the GeoServer website (Docker + Jekyll)

This file documents how to build the site locally using Docker so you don't have to install Ruby or Jekyll locally.

Prerequisites
- Docker
- A working Git checkout of this repository

Optional (local install)
- If you prefer to build locally without Docker: Ruby + RubyGems, Bundler (`gem install bundler`) and the repository checked out.

Docker: build only

- Replace `ABS_PATH_TO_REPO` with the absolute path to this repository on your machine (Windows examples use `d:/...`):

```bash
# Build only: installs gems inside container and builds the static site into _site
docker run --rm -v "ABS_PATH_TO_REPO:/srv/jekyll" -w /srv/jekyll jekyll/jekyll:4 \
  bash -lc "bundle install --jobs 4 --retry 3 && bundle exec jekyll build"
```

Docker: serve locally (with auto-reload)

- This runs the site and exposes it on port 4000 on your host. Use `--host 0.0.0.0` so the container binds to the mapped interface.

```bash
docker run --rm -p 4000:4000 -v "ABS_PATH_TO_REPO:/srv/jekyll" -w /srv/jekyll jekyll/jekyll:4 \
  bash -lc "bundle install --jobs 4 --retry 3 && bundle exec jekyll serve --watch --host 0.0.0.0"
```

Windows path notes
- When using PowerShell or CMD on Windows, quote the volume path as shown above: `"d:/path/to/repo:/srv/jekyll"`.
- If you see an error about the working directory, omit `-w /srv/jekyll` and `cd` into the folder inside the container:

```bash
docker run --rm -v "ABS_PATH_TO_REPO:/srv/jekyll" jekyll/jekyll:4 bash -lc "cd /srv/jekyll && bundle install --jobs 4 --retry 3 && bundle exec jekyll build"
```

Notes
- Liquid variables (like `{{site.stable_branch}}`) come from `_config.yml` (for example `stable_branch: 2.28.x`).
- To update the value that appears site-wide, edit `_config.yml` and re-run the build.
