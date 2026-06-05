# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

The website for the **Computational Intelligence, Control & Information (CI²) Lab** at Texas Tech University (PI: Dr. Stas Tiomkin). It is a [Jekyll](https://jekyllrb.com/) site built on the **[al-folio](https://github.com/alshedivat/al-folio) v1.x** academic theme. The site was migrated from a hand-rolled HTML5 UP static site to al-folio in 2026.

> al-folio's own upstream docs (`AGENTS.md`, `docs/`, `.github/`, `test/`) were left in the repo for reference but are **excluded from the build** (see `exclude:` in `_config.yml`) and describe developing the *theme's gems*, not this site. Ignore them for lab-site work.

## al-folio v1.x architecture (important)

This is **not** a self-contained theme. The runtime — every `_layouts/*.liquid`, `_includes/*.liquid`, Sass, JS, and custom Liquid tags — ships in **versioned Ruby gems** (`al_folio_core` is the hub; `al_icons`, `al_search`, `al_math`, `al_img_tools`, etc. are feature gems). `_config.yml` sets `theme: al_folio_core`. Consequences:

- **There are no `_layouts/` or `_includes/` directories here.** To see how a layout renders, read the gem under `vendor/bundle/ruby/3.4.0/gems/al_folio_core-*/`. You can override a layout/include locally by creating the same path in this repo, but prefer config/front-matter changes.
- **Features are double-gated:** a site-wide flag in `_config.yml` (`enable_math`, `search_enabled`, `features.cv.enabled`, …) **and** per-page front matter. A feature renders only when both are on; otherwise its tag emits nothing (fails silently).
- The `Gemfile` plugin list and `_config.yml`'s `plugins:` list must stay in sync — adding/removing a plugin means editing both.

## Local toolchain gotcha — READ BEFORE `bundle install`

This machine's Ruby (`ruby-3.4.1`) and Command Line Tools are **both broken for compiling native C++ gems** (eventmachine, etc.):

1. The Ruby was built with `CXX="false"` in its `rbconfig`.
2. The CLT libc++ header dir (`/Library/Developer/CommandLineTools/usr/include/c++/v1`) is **empty**; the real headers are only in the SDK.

`bin/fix_cxx.rb` is a build-time shim that patches both **in-memory for build subprocesses only** (it does not touch the global Ruby/toolchain). Always install with it:

```bash
RUBYOPT="-r$(pwd)/bin/fix_cxx.rb" bundle install
```

Plain `bundle install` will fail with `'iostream' file not found` / `make: *** [binder.o] Error 1`. Once gems are compiled, the shim is **not** needed for `jekyll build`/`serve`. The permanent fix (then delete the shim): reinstall CLT (`sudo rm -rf /Library/Developer/CommandLineTools && xcode-select --install`) and use a Ruby built with a working C++ compiler.

## Dev loop

```bash
bundle exec jekyll serve --port 4001     # dev server → http://localhost:4001/  (baseurl is blank)
bundle exec jekyll build                 # production build to _site/
```

ImageMagick (`convert`, on PATH) generates responsive `.webp` variants for everything in `assets/img/` at build time — first build is slower. Gems install to `vendor/bundle` (bundler path is set locally).

## Where the content lives (this is what you'll actually edit)

- **`_config.yml`** — site identity, nav, scholar/author highlighting, feature flags. **Set `url`/`baseurl` before deploying** (blank baseurl = user/org page or custom domain; `/LabWebsite` = GitHub project page).
- **Homepage** → `_pages/about.md` (lab intro; `image: stas.jpg` is the PI photo in the profile slot).
- **People** → `_pages/profiles.md` (the `profiles:` list: one block per member, `image:` + `content:` + `more_info:`). Each member's bio is a fragment in `_pages/prof_<name>.md`, rendered by the `profiles` layout. **These fragments are in `_config.yml`'s `exclude:` list** — if you add a member, add their `prof_*.md` to that list too, or it gets published as a stray page.
- **Research** → `_pages/projects.md` (repurposed: title/permalink are "research") + cards in `_projects/*.md` (front matter: `title`, `description`, `importance` for ordering, `img` optional).
- **Publications** → `_bibliography/papers.bib`. Add BibTeX entries; `selected={true}` surfaces a paper on the homepage. Rendered by jekyll-scholar. Keep stray-text comments inside `@comment{...}` — bare `%` lines break the parser.
- **News** → `_news/*.md` (short `inline: true` announcements shown on the homepage and `/news/`).
- **Contact / socials** → `_data/socials.yml` (email, scholar id, etc.).
- **Images** → `assets/img/`. Member headshots are named per `profiles.md`. `joshua.jpg` / `volodymyr.jpg` are **placeholder initial-avatars** generated with ImageMagick — replace with real photos when available.

## Deploying

`.github/workflows/deploy.yml` (from al-folio) builds and publishes to GitHub Pages. It's currently excluded from the *site* build but still active as a workflow if this repo is pushed to GitHub. Set `url`/`baseurl` first, and add a `CNAME` file if using a custom domain.
