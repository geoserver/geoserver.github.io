---
author: Jody Garnett
date: 2021-03-04
layout: post
title: GeoServer repository transition to main branch
categories:
- Announcements
---

The GeoServer project is changing our default branch to ``main``.

*The casual use of the words "master" and "slave" in computer software is an unnecessary reference to a painful human experience that continue to impact society.*

The change is part of an industry shift made possible by the [git](https://sfconservancy.org/news/2020/jun/23/gitbranchname/), [bitbucket](https://bitbucket.org/blog/moving-away-from-master-as-the-default-name-for-branches-in-git), [github](https://github.com/github/renaming) and [gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/221164) projects. The git command line, repository implementations, now support ``main`` as default branch setting.

To update your local repository:

```bash
git branch -m master main
git fetch upstream
git branch -u upstream/main main
```

To [configure your local ``git`` tool](https://github.blog/2020-07-27-highlights-from-git-2-28/#introducing-init-defaultbranch) so that new repositories are created with a ``main`` branch:

```bash
git config --global init.defaultBranch main
```
