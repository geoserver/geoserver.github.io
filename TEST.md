Testing the site locally
------------------------

It is possible to test the web site before committing, full instructions available here: [Testing your GitHub Pages site locally with Jekyll](
https://docs.github.com/en/github/working-with-github-pages/testing-your-github-pages-site-locally-with-jekyll)

If you have already installed all the dependencies, just run:

```
bundle exec jekyll serve --watch
```

Then navigate to [http://localhost:4000](http://localhost:4000).

Not finding the blog post you just wrote? It could be, because it's labelled for a future date (and you are preparing in advance).
If that's the case, it can be shown by adding ``--future`` to the jekyll startup:

```
bundle exec jekyll serve --watch --future
```

