# Grammar learning tree verification — 25 September 2026

- Built 21 static pages: nine main pages plus twelve separate grammar lessons.
- All 568 local links/assets, anchors, landmarks, navigation states, external-link safety attributes, and image alt attributes pass `tests/validate.py`.
- Curriculum checks pass: twelve unique nodes, every node appears once, acyclic suggested prerequisites, three quizzes per lesson and at least two practice solutions each.
- In-app browser: all 13 learning pages fit 280, 375, 800, and 1280 CSS-pixel viewports without horizontal page overflow. Phone layout also inspected at 320px. Tree branches, phone lesson heading, and present-tense table were visually inspected.
- All 36 quiz questions exercised in the browser using the expected answer key: every lesson returned 3/3. Also checked missing answers, incorrect-answer explanations, changing an answer clearing the old score, and keyboard activation of a practice solution. No browser console errors recorded.
- Completion tested through mark, reload, return to tree, next-incomplete resume, explicit reset, and another reload. Progress tests run the production JavaScript with a storage/DOM harness and cover independent tabs, duplicates/unknown IDs, corrupted data, unmarking, full completion, and blocked storage. This harness is separate from browser rendering checks.
- A temporary script-free lesson fixture showed static teaching content, fallback quiz answers, and practice solutions while hiding inactive interactive controls. The fixtures are excluded from the repo update.
- Tree and present-tense lesson fitted at 800px with 200% root text sizing, using temporary static fixtures. Mobile menu showed all nine links and closed with Escape.
- Sources checked against Whitney's public-domain alphabet, pronunciation, declension, pronoun, and present-system chapters. The La Trobe primer remains an attributed external reading resource.
- The source and generated pages retain the removed small header logo, prominent homepage logo, and bold Sanskrit homepage verses.

Checks: `python scripts/build.py`; `python tests/validate.py`; `python tests/course_content.py`; `node tests/course-progress.cjs`; `node --check js/learning.js`. Earlier full-site checks remain below. No new standalone Playwright run is claimed.

# Verification — 25 September 2026

## Homepage and learning follow-up

- The original logo asset is unchanged. Its large homepage rendering is 186 × 228 pixels on desktop, with proportional scaling on phones. Both hero verses compute to font weight 700.
- Homepage and Learn Samskrita tested at 280, 320, 375, 800, 1120, 1216 and 1440 CSS pixels: no horizontal page scrolling.
- Both changed page layouts also fit at 800px with 200% root text sizing.
- All nine pages carry the new menu item; the other seven pages also passed a layout check at the 1216px desktop-menu breakpoint.
- Mobile menu has nine working links; the learning page has the correct selected state. Homepage learning CTA, lesson-section anchors, and a keyboard-operated answer disclosure were verified.
- The primer's source record, PDF, Whitney's book and linked chapters were opened online. Rights provenance is recorded in `LEARNING-SOURCES.md` and shown beside each book on the page.
- Rebuilt nine static pages and passed internal-link/asset, landmark, selected-navigation and JavaScript syntax checks.

## Earlier redesign verification

Passed in the local Codex browser:

- All eight pages at 280, 320, 375, 800, 1120 and 1440 CSS pixels: no horizontal page overflow, one page title, matching selected navigation and one footer.
- All eight pages with 200% root text sizing at 800px: no horizontal page overflow.
- Tablet menu opens all eight links, separates the brand from navigation, closes with Escape and returns focus.
- Title/speaker/resource search, combined year/category filters, oldest-first sorting, empty-result reset, URL persistence and reload restoration.
- Direct item links reveal their target even with conflicting filters. Copy link and email copy report success and produce the expected clipboard text.
- Calendar month navigation, saved month on reload, empty months, agenda-to-item links and browser Back navigation. Phone layout shows an agenda; year-only camps appear separately.
- Expand/collapse all activity sections and resource-name search.
- Gallery missing-image feedback, next/previous arrow keys, Escape, focus restoration and explicit Tab/Shift+Tab containment. An isolated temporary image fixture exercised successful full-size loading; it is not included in the deliverable.
- A separate no-script fixture kept all navigation and four activity records visible while hiding inactive search controls.

Passed automated checks:

- `python scripts/build.py`: generated eight static pages.
- `python tests/validate.py`: internal links and asset paths, unique anchors, heading/landmark counts, active pages, image alt attributes, external-link rel attributes and content IDs.
- `node --check js/site.js`: JavaScript syntax.
- `node tests/calendar.cjs`: actual calendar handlers, download filename and MIME, date-only boundaries, leap and year rollover, tentative status, UTF-8 line folding, escaping, direct URLs and Google Calendar parameters.
- Text contrast checks: body 13.15:1; muted on pale saffron 5.11:1; saffron label 4.98:1; badge 6.75:1; primary control 11.76:1; WhatsApp control 7.16:1.

Limits: the standalone Playwright browser launch was blocked by the environment, so `tests/browser.cjs` has not completed here. The in-app browser executed the calendar download action and displayed feedback, but its download-event API timed out; downloaded-file contents were verified through the actual handler test instead. External recording/profile/calendar destinations were not authenticated or posted to. Reduced-motion rules were reviewed in CSS; no operating-system preference was changed. Real gallery assets, article/resource links, placeholder names and uncertain dates remain content tasks described in README.md.
