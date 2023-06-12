# Announcement Generation

Write a blog post announcing the new release:
```
python3 announcement.py username password 2.23.2 --geotools  29.2 --geowebcache 1.23.2
```

A post is generated to standard out for your review.

* The header information should be correct, picking up your user name from git global config
* Check the included release notes
* Edit ``bin/templates/aboutXXX.md`` to list any new features for the about section
* Force a security vulnerability section with ``--security`` (although this will be added if any issues with component ``Vulnerability`` are included in the release)
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