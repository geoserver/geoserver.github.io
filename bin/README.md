# Announcement Generation

The announcement script is written in python:
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Write a blog post announcing the new release:
```
cd bin
python3 announcement.py username password 2.23.2 --geotools  29.2 --geowebcache 1.23.2
```

``username`` and ``password`` are your JIRA credentials.

A post is generated to standard out for your review.

* The header information should be correct, picking up your user name from git global config.

* Check the included release notes.

* Edit ``bin/templates/aboutXXX.md`` to list any new features for the about section.
  
  At the start of a new series (milestone or release candidate) a new template will be needed. You can create a new template by copying the previous example.

* Force a security vulnerability section with ``--security`` (although this will be added automatically if any vulnerabilities are detected in the release)

* Security vulnerability options:
  * ``--urgency normal|important|urgent`` - Set security urgency level (default: important)
  * ``--concurrent "2.28.3,2.26.7"`` - Mention concurrent security releases (comma-separated)
  * ``--disclosure 2.27.0`` - Generate updates for prior blog posts when vulnerabilities are disclosed

* Announcement text based on version, use ``--override stable`` or ``--override maintenance`` if the guess was incorrect

Generate to a file using the date supplied by Jira:

```
python3 announcement.py username password 2.23.2 --geotools  29.2 --geowebcache 1.23.2 --post
```

## Python Setup

This script uses python3 (macOS example):
```
brew install python
```

To install required modules:
```
pip3 install -r requirements.txt
```

To confirm installation:
```
python3 announcement.py
```

## Python Virtual Environment Setup (Optional)

To establish virtual environment (macOS example):
```
brew install virtualenv
virtualenv venv
```

To activate python:
```
source venv/bin/activate
```

To install requirements into virtual environment:
```
pip install -r requirements.txt
```

To confirm installation:

```
python anouncement.py
```

### Technical Details

The python ``announcement.py`` script makes use of the Jira REST API to determine information about the release being made.

Posts are generated using Jenga2 templates located in ``bin/templates``. You can fine tune the about section for each series by adding ``aboutXXX.md`` file documenting new features.

It does check that the release is made, in order to ensure to ensure that a release date is provided.

The specific text genrated is based on checking the version number (for ``RC`` release candidate, ``M`` milestone, ``<4`` stable, or ``<7`` maintenance).

The security consideration sections is optional, with the flag including the post content and updating the header tags so the post is correctly indexed.

## Security Vulnerability Handling

The announcement script now includes enhanced support for security vulnerability disclosure management (GEOS-11928):

### Automatic Vulnerability Detection

The script automatically detects vulnerabilities using multiple approaches:

1. **Disclosure Field** - Issues with the custom "Disclosure" field set (customfield_11057)
2. **Component-based** - Issues with component "Vulnerability" (legacy approach)
3. **Level Field** - Issues with level "Vulnerability" (restricted visibility until disclosed)

### Disclosed vs Undisclosed Vulnerabilities

Vulnerabilities are categorized as:

* **Disclosed** - Issues with a disclosure version that is already released
* **Undisclosed** - Issues without disclosure or with future disclosure versions

The security section template handles both types appropriately.

### Security Urgency Levels

The ``--urgency`` option supports three levels:

* ``normal`` - Standard security update messaging
* ``important`` - Recommended security update (default)
* ``urgent`` - Critical security update requiring immediate attention

### Concurrent Releases

Use ``--concurrent`` to mention other versions released simultaneously for the same vulnerabilities:

```
python3 announcement.py user pass 2.26.4 --concurrent "2.28.3,2.25.8"
```

### Prior Blog Post Updates

When vulnerabilities are publicly disclosed, use the ``--disclosure`` option to generate update text for prior release announcements:

```
python3 announcement.py user pass 2.26.4 --disclosure 2.27.0
```

This generates:
* List of vulnerabilities scheduled for disclosure in the specified version
* Blog posts that need updating
* Ready-to-use security section text

### JIRA Security Model

**Important:** Issues with ``level = Vulnerability`` have restricted visibility in JIRA and won't appear in queries until they are scheduled for disclosure. This is by design for security. The script handles this properly by:

1. Relying on the Disclosure field for detecting scheduled disclosures
2. Supporting component-based vulnerability detection for backward compatibility
3. Providing clear messaging when no vulnerabilities are found

### Field Mappings

* ``customfield_11057`` - Disclosure field (version when vulnerability will be disclosed)
* ``level = Vulnerability`` - Issues with restricted visibility (security-by-design)
* ``component = Vulnerability`` - Legacy vulnerability component approach


# Preview the finished pages (Docker Compose)

You don't need to install Jekyll to preview the pages before creating a PR, just use the included `docker-compose.yml` from the repository root and then open http://localhost:4000 to preview the site:

```
docker compose up
```

Fallback:

```
docker run --rm -it -v "$PWD":/srv/jekyll -p 4000:4000 jekyll/jekyll:4 \
  jekyll serve --host 0.0.0.0 --watch --force_polling --livereload
```

Tips:
- Use `--force_polling` on Windows to ensure file-change detection works.
- `--livereload` automatically refreshes the browser on edits.