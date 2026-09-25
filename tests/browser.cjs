/* Run with Playwright installed and a local server: node tests/browser.cjs */
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');
const { pathToFileURL } = require('node:url');

(async () => {
  const browser = await chromium.launch({headless:true, ...(process.env.CHROME_PATH ? {executablePath:process.env.CHROME_PATH} : {})});
  const base = process.env.SITE_URL || 'http://127.0.0.1:8765';
  const output = process.env.TEST_OUTPUT || path.resolve(__dirname,'../../qa');
  await fs.mkdir(output,{recursive:true});
  const context = await browser.newContext({permissions:['clipboard-read','clipboard-write']});
  const page = await context.newPage();
  const errors = [];
  page.on('pageerror',error => errors.push(error.message));
  const pages = ['index','about','learn','talks','activities','blogs','gallery','members','contact'];
  let layouts = 0;
  async function overflow(label) {
    const result = await page.evaluate(() => ({width:innerWidth,scroll:document.documentElement.scrollWidth,offenders:[...document.querySelectorAll('body *')].filter(el=>{const r=el.getBoundingClientRect();return r.width && (r.right>innerWidth+1 || r.left< -1) && !el.matches('.skip-link');}).slice(0,8).map(el=>el.className)}));
    assert(result.scroll <= result.width+1,`${label}: horizontal overflow ${JSON.stringify(result)}`);
  }
  try {
    for (const width of [280,320,375,800,1120,1440]) {
      await page.setViewportSize({width,height:900});
      for (const name of pages) {
        await page.goto(`${base}/${name}.html`);
        await page.waitForFunction(()=>document.documentElement.classList.contains('js'));
        await overflow(`${name} at ${width}`);
        assert.equal(await page.locator('h1').count(),1);
        assert.equal(await page.locator('nav [aria-current="page"]').getAttribute('href'),`${name}.html`);
        assert.equal(await page.locator('footer').count(),1);
        assert.equal(await page.locator('a[href="#"]').count(),0);
        if (width<1216) {
          await page.locator('.menu-toggle').click();
          assert.equal(await page.locator('.nav-links a:visible').count(),9);
          await overflow(`open menu ${name} at ${width}`);
          await page.keyboard.press('Escape');
          assert.equal(await page.locator('.menu-toggle').getAttribute('aria-expanded'),'false');
        }
        layouts++;
      }
    }
    // Text-only zoom and 400% desktop reflow (320 CSS px).
    await page.setViewportSize({width:800,height:900});
    for (const name of pages) {
      await page.goto(`${base}/${name}.html`);
      await page.evaluate(()=>document.documentElement.style.fontSize='200%');
      await overflow(`${name} enlarged text`);
    }
    await page.setViewportSize({width:1280,height:1000});
    await page.goto(`${base}/talks.html`);
    await page.locator('[name=q]').fill('Arjun');
    assert.equal(await page.locator('[data-record]:visible').count(),1);
    assert(new URL(page.url()).searchParams.get('q') === 'Arjun');
    await page.reload();
    assert.equal(await page.locator('[name=q]').inputValue(),'Arjun');
    assert.equal(await page.locator('[data-record]:visible').count(),1);
    await page.locator('[name=q]').fill('No matching record');
    assert(await page.locator('[data-empty]').isVisible());
    await page.locator('[data-reset]').click();
    await page.waitForFunction(()=>document.querySelectorAll('[data-record]:not([hidden])').length===3);
    await page.locator('[name=sort]').selectOption('oldest');
    assert.equal(await page.locator('[data-record]:visible').first().getAttribute('id'),'sangha-reinauguration');
    await page.locator('[name=year]').selectOption('2025');
    assert.equal(await page.locator('[data-record]:visible').count(),2);
    await page.locator('[name=category]').selectOption('Community');
    assert(await page.locator('[data-empty]').isVisible());
    await page.goto(`${base}/talks.html?year=2024#essentials-of-ramayana`);
    assert(await page.locator('#essentials-of-ramayana').isVisible());
    assert.equal(await page.locator('[name=year]').inputValue(),'');
    await page.locator('#essentials-of-ramayana [data-share]').click();
    assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),`${base}/talks.html#essentials-of-ramayana`);
    await page.locator('#essentials-of-ramayana .calendar-actions summary').click();
    const downloadPromise = page.waitForEvent('download');
    await page.locator('#essentials-of-ramayana [data-calendar=ics]').click();
    const download = await downloadPromise;
    const calendarPath = path.join(output,download.suggestedFilename());
    await download.saveAs(calendarPath);
    const ics = await fs.readFile(calendarPath,'utf8');
    assert(ics.includes('DTSTART;VALUE=DATE:20250819\r\n'));
    assert(ics.includes('DTEND;VALUE=DATE:20250820\r\n'));
    assert(ics.includes('STATUS:TENTATIVE'));
    assert(ics.split('\r\n').every(line=>Buffer.byteLength(line)<=75));
    // Inspect calendar link creation without navigating to an external account.
    await page.evaluate(()=>{window.open = url => {window.capturedCalendarURL=url;};});
    await page.locator('#essentials-of-ramayana [data-calendar=google]').click();
    const google = new URL(await page.evaluate(()=>window.capturedCalendarURL));
    assert.equal(google.hostname,'calendar.google.com');
    assert.equal(google.searchParams.get('dates'),'20250819/20250820');
    await page.goto(`${base}/talks.html?view=calendar&month=2025-08`);
    assert(await page.locator('.calendar-panel').isVisible());
    assert.equal(await page.locator('.agenda-item').count(),1);
    await page.locator('[data-month="1"]').click();
    assert.equal(new URL(page.url()).searchParams.get('month'),'2025-09');
    assert(await page.locator('.agenda-empty').isVisible());
    await page.reload();
    assert.equal(await page.locator('#calendar-month').innerText(),'September 2025');
    await page.locator('[data-month="-1"]').click();
    await page.locator('[data-open-record]').click();
    assert(await page.locator('#essentials-of-ramayana').isVisible());
    await page.goBack();
    assert(await page.locator('.calendar-panel').isVisible());

    await page.goto(`${base}/activities.html`);
    await page.locator('[data-expand=false]').click();
    assert.equal(await page.locator('.activity-group[open]').count(),0);
    await page.locator('[data-expand=true]').click();
    assert.equal(await page.locator('.activity-group[open]').count(),2);
    await page.locator('[name=q]').fill('Audio File');
    assert.equal(await page.locator('[data-record]:visible').count(),1);
    assert.equal(await page.locator('[data-record]:visible').getAttribute('id'),'tarka-sangraha-2');
    await page.goto(`${base}/activities.html?view=calendar&month=2026-06`);
    assert.equal(await page.locator('.agenda .agenda-item').count(),2);
    assert.equal(await page.locator('.undated-agenda .agenda-item').count(),2);
    assert(!(await page.locator('.accordion-tools').isVisible()));
    await page.setViewportSize({width:320,height:900});
    assert(!(await page.locator('.month-grid').isVisible()));
    assert(await page.locator('.agenda').isVisible());
    await overflow('mobile agenda');
    await page.goto(`${base}/blogs.html?category=Mathematics`);
    assert.equal(await page.locator('[data-record]:visible').count(),1);

    await page.goto(`${base}/contact.html`);
    await page.locator('[data-copy]').first().click();
    assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),'samskrutasangha.iisc@gmail.com');
    assert.equal(await page.locator('[data-copy]').first().innerText(),'Copied');
    assert(await page.locator('.toast').innerText());
    await page.evaluate(()=>Object.defineProperty(navigator,'clipboard',{value:{writeText:()=>Promise.reject(new Error('Denied'))},configurable:true}));
    await page.locator('[data-copy]').last().click();
    assert(await page.locator('.copy-fallback').isVisible());
    assert.equal(await page.locator('.copy-fallback input').inputValue(),'samskrutasangha.iisc@sbi');
    await page.keyboard.press('Escape');

    await page.goto(`${base}/gallery.html`);
    await page.locator('[data-gallery]').first().click();
    await page.locator('.lightbox-error').waitFor({state:'visible'});
    assert(await page.locator('.lightbox').isVisible());
    await page.keyboard.press('ArrowRight');
    assert.equal(await page.locator('.lightbox-counter').innerText(),'2 / 3');
    await page.keyboard.press('ArrowLeft');
    assert.equal(await page.locator('.lightbox-counter').innerText(),'1 / 3');
    await page.keyboard.press('Shift+Tab');
    assert(await page.evaluate(()=>document.querySelector('.lightbox').contains(document.activeElement)));
    await page.keyboard.press('Escape');
    assert.equal(await page.evaluate(()=>document.activeElement.matches('[data-gallery]')),true);
    // Simulated uploaded image exercises the success path without inventing site content.
    await page.route('**/images/gallery/shibira-2026.jpg',route=>route.fulfill({path:path.resolve(__dirname,'../images/logo.png'),contentType:'image/png'}));
    await page.locator('[data-gallery]').first().click();
    await page.waitForFunction(()=>document.querySelector('.lightbox-stage img').src.endsWith('shibira-2026.jpg'));
    assert(await page.locator('.lightbox-stage img').isVisible());
    await page.locator('[data-lightbox-close]').click();

    await page.goto(`${base}/index.html`);
    await page.keyboard.press('Tab');
    assert.equal(await page.evaluate(()=>document.activeElement.className),'skip-link');
    await page.keyboard.press('Enter');
    assert.equal(await page.evaluate(()=>document.activeElement.id),'main-content');
    await page.emulateMedia({reducedMotion:'reduce'});
    assert.equal(await page.locator('.toast').evaluate(el=>getComputedStyle(el).transitionDuration),'0s');
    await page.emulateMedia({reducedMotion:'no-preference'});
    for (const [name,width] of [['index',1440],['talks',1440],['activities',800],['contact',320],['index',375]]) {
      await page.setViewportSize({width,height:1000});
      await page.goto(`${base}/${name}.html`);
      await page.screenshot({path:path.join(output,`${name}-${width}.png`),fullPage:true});
    }
    const noJS = await browser.newContext({javaScriptEnabled:false,viewport:{width:320,height:900}});
    const fallback = await noJS.newPage();
    await fallback.goto(`${base}/activities.html`);
    assert.equal(await fallback.locator('.nav-links a:visible').count(),9);
    assert.equal(await fallback.locator('[data-record]:visible').count(),4);
    assert.equal(await fallback.locator('.filters:visible').count(),0);
    assert(await fallback.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    await noJS.close();
    await page.goto(pathToFileURL(path.resolve(__dirname,'../talks.html')).href);
    await page.locator('[name=q]').fill('Arjun');
    assert.equal(await page.locator('[data-record]:visible').count(),1);
    assert.deepEqual(errors,[]);
    console.log(`PASS: ${layouts} responsive page layouts, 9 enlarged-text layouts, navigation, search, filters, URL restore, sorting, sharing, calendar/ICS, agenda, accordions, clipboard and fallback, lightbox, keyboard, reduced motion, no-JS and file://.`);
  } finally { await browser.close(); }
})().catch(error=>{console.error(error);process.exitCode=1;});
