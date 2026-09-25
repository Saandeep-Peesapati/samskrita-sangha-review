# Samskrita Sangha IISc

A self-contained static site. Open `index.html` directly, or run:

```sh
python -m http.server 8000 --bind 127.0.0.1
```

Then visit `http://localhost:8000`. No npm build, remote fonts, API keys, or backend are required. The site keeps its original eight page URLs and adds `learn.html` and twelve `learn-*.html` lesson pages.

## Editing content

Edit `data/content.json`, then run `python scripts/build.py`. This rebuilds all 21 HTML pages with a shared header/footer and updates the homepage. Rebuild when announcing events or when upcoming dates pass. HTML is committed/generated so visitors do not need Python or JavaScript to read the site. Edit shared page templates in `scripts/build.py`, styles in `css/style.css`, and behavior in `js/site.js`.

- Each talk, activity, and article needs a unique stable `id`, a `title`, and a `category`. Keep IDs stable to preserve shared links.
- Dates use `YYYY-MM-DD`. Camps with only a known year use `year`, and remain in a separate undated agenda. Unknown times are never invented: calendar exports are explicitly all-day.
- Set `tentative` to `true` for unconfirmed dates. These are labeled in the UI, marked tentative in `.ics` files, and identified in Google Calendar titles.
- Resources support `video`, `audio`, `pdf`, and `external`. Add their real `url` to enable the corresponding action. Null URLs display an availability message.
- Gallery `src` paths are relative to the site root. Add the actual files and rebuild. Posters use `object-fit: contain` to preserve their text. Missing files use a local placeholder and a clear lightbox message.
- Search, year/category, sort, view, and month are saved in the URL. Direct item links remove filters so the target remains accessible. Activity sorting is within each category; the talks timeline also reorders years.

## Content still required from the original download

The source included `abc`/`bcd`/`xyz` placeholders, generic LinkedIn homepage links, empty resource links, and missing gallery photographs. These are now honest availability states rather than working-looking fake actions. No replacement people, URLs, dates, articles, or photographs were invented.

- Confirm the talk dates **19 August 2025** and **11 March 2025**, originally suffixed with question marks in the talks page.
- Supply notes/video for Tarka Sangraha Lecture 1 and audio for Lecture 2.
- Add the two blog URLs and real author names.
- Add the 2026 camp teacher, exact dates for both camps, member profile URLs, and alumni details.
- Supply `images/gallery/shibira-2026.jpg`, `a.jpg`, `b.jpg`, and the second gallery caption (or update those paths in the data file).
- Add confirmed upcoming events. With the supplied data, the homepage correctly shows no dated upcoming event.

The original email, WhatsApp group, UPI ID, and recording URLs are preserved. The YouTube channel URL now includes `https://`.

## Implementation coverage

The requested items 1–48 are addressed: narrow layouts and compact tablet/mobile navigation; wrapping contact text and stacked records; selected navigation; action hierarchy and contrast; serif/sans typography with Devanagari fallbacks; consistent spacing, icons, cards, avatars, footer and page introductions; revised homepage, timeline, activities, editorial blog, gallery, members and contact layouts; search and URL-backed filters; calendar/phone agenda and `.ics`/Google Calendar export; deep links, clipboard feedback, gallery lightbox, expand/collapse controls and typed resources; focus styles, skip navigation, empty/missing states, reduced motion and reserved image space.

Item 49 explicitly suggests considering dark mode and print layouts later. They remain deferred, without automatic inversion or an unreviewed print theme.

## Checks

`node tests/calendar.cjs` exercises the actual calendar handlers with dependency-free assertions, including Unicode, escaping, leap years, date rollover and tentative dates.

`tests/browser.cjs` is a repeatable Playwright regression suite. Install Playwright separately in a development environment, start the site at port 8765, and run `node tests/browser.cjs`. Set `CHROME_PATH` to use an installed Chromium browser and `SITE_URL` to change the server address. `TEST_OUTPUT` controls screenshot/download output.

The current environment blocks standalone browser processes. Browser verification was instead performed in the Codex in-app browser. See `VERIFICATION.md` for the checks actually run; the standalone Playwright suite is provided but has not completed here.

## Homepage and learning update

The homepage now pairs a prominent, uncropped copy of the original logo with the title; its Sanskrit motto, invocation, and footer motto are bold. The logo retains its original 186 × 228 aspect ratio. All pages include Learn Samskrita in the navigation. The small header logo has been removed; the large homepage emblem remains.

The learning page now opens with a branching roadmap to twelve foundation grammar lessons. Lessons are for complete beginners, with English explanations, Devanagari, IAST, worked examples, tables, common mistakes, three quiz questions each, additional revealable practice, and a recap. Allow roughly ten minutes per lesson including practice. All lessons are freely accessible.

Edit `scripts/course_content.py` for the curriculum and text, `scripts/course_pages.py` for the learning templates, `css/course.css` for course layout, and `js/learning.js` for quizzes and completion. Then run `python scripts/build.py`. `css/learning.css` retains the homepage identity styles. `scripts/learning.py` is a compatibility import; it no longer contains the earlier one-page lesson.

Progress uses the `samskrita-foundation-progress-v1` localStorage key on the same browser and origin. There is no account, backend, analytics, or server-side progress collection. Completion is manual and reversible; quizzes do not lock lessons. The tree offers a resume link and an explicit reset control. Storage errors leave lessons and quizzes usable with a truthful notice. Use a consistent HTTP origin for predictable persistence; file-URL storage behaviour varies between browsers.

Run `python tests/validate.py`, `python tests/course_content.py`, `node tests/course-progress.cjs`, and `node --check js/learning.js`. Browser checks actually performed are documented in `VERIFICATION.md`.

Grammatical source chapters and rights notes appear on every lesson and in `LEARNING-SOURCES.md`. Explanations and practice are newly written; historical books remain on their source hosts. Full external sandhi and advanced grammar are deliberately outside this foundation course. Examples keep word boundaries visible and may retain pause forms for teaching.

## GitHub Pages review site

This repository contains the complete static site, its content and assets, build scripts, source notes, and validation checks. The public bookshelf section has been removed from the learning tree; individual lessons retain their source citations.

Publish from the `main` branch and repository root in Settings → Pages. The `.nojekyll` file serves the generated HTML directly. No backend or secrets are required. After editing lesson content or templates, run `python scripts/build.py` and include the regenerated HTML in the commit. Relative asset and lesson URLs support a GitHub Pages project path.
