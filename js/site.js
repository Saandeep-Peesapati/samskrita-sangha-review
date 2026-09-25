/* Content and navigation remain usable without these progressive enhancements. */
(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
  const escape = value => String(value).replace(/[&<>"']/g, char => ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[char]));
  const toast = $('.toast');
  let toastTimer;
  function announce(message) {
    clearTimeout(toastTimer);
    toast.textContent = message;
    toast.classList.add('visible');
    toastTimer = setTimeout(() => toast.classList.remove('visible'), 4500);
  }
  async function copyText(text, button) {
    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(text);
      } else {
        const helper = document.createElement('textarea');
        helper.value = text;
        helper.setAttribute('aria-label', 'Text to copy');
        helper.style.cssText = 'position:fixed;top:0;left:0;width:1px;height:1px;opacity:0';
        document.body.append(helper);
        helper.select();
        const copied = document.execCommand('copy');
        helper.remove();
        button.focus({preventScroll:true});
        if (!copied) throw new Error('Clipboard unavailable');
      }
      const label = $('span', button);
      if (label) {
        const original = button.dataset.originalLabel || label.textContent;
        button.dataset.originalLabel = original;
        label.textContent = 'Copied';
        setTimeout(() => { label.textContent = original; }, 2500);
      }
      announce('Copied to clipboard.');
    } catch {
      announce('Copy is unavailable. Select and copy the text in the dialog.');
      let fallback = $('.copy-fallback');
      if (!fallback) {
        fallback = document.createElement('dialog');
        fallback.className = 'lightbox copy-fallback';
        fallback.setAttribute('aria-label', 'Copy manually');
        fallback.innerHTML = '<form method="dialog"><label>Copy this text<input readonly></label><button class="button secondary">Close</button></form>';
        document.body.append(fallback);
      }
      $('input', fallback).value = text;
      fallback.showModal();
      $('input', fallback).select();
    }
  }
  const menu = $('.menu-toggle');
  const navigation = $('.nav-links');
  function closeMenu(returnFocus = false) {
    menu.setAttribute('aria-expanded', 'false');
    navigation.classList.remove('is-open');
    if (returnFocus) menu.focus();
  }
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    navigation.classList.toggle('is-open', open);
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') closeMenu(true);
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.main-nav')) closeMenu();
  });
  matchMedia('(min-width: 76rem)').addEventListener('change', () => closeMenu());

  function itemURL(id) {
    const url = new URL(location.href);
    url.search = ''; // Shared items must not inherit filters which could hide them.
    url.hash = id;
    return url.href;
  }
  document.addEventListener('click', event => {
    const copy = event.target.closest('[data-copy]');
    if (copy) copyText(copy.dataset.copy, copy);
    const share = event.target.closest('[data-share]');
    if (share) copyText(itemURL(share.dataset.share), share);
  });

  // Dates without supplied times are exported as all-day events, never invented times.
  const dateLabel = iso => new Date(iso + 'T12:00:00').toLocaleDateString('en-GB', {day:'numeric',month:'long',year:'numeric'});
  function nextDay(iso) {
    const date = new Date(iso + 'T12:00:00Z');
    date.setUTCDate(date.getUTCDate() + 1);
    return date.toISOString().slice(0,10);
  }
  function icsEscape(value) { return String(value).replace(/\\/g,'\\\\').replace(/\r?\n/g,'\\n').replace(/;/g,'\\;').replace(/,/g,'\\,'); }
  function foldLine(line) {
    const encoder = new TextEncoder();
    let part = '', count = 0;
    const result = [];
    for (const char of line) {
      const size = encoder.encode(char).length;
      if (count + size > 75) { result.push(part); part = ' '; count = 1; }
      part += char; count += size;
    }
    result.push(part);
    return result.join('\r\n');
  }
  document.addEventListener('click', event => {
    const button = event.target.closest('[data-calendar]');
    if (!button) return;
    const record = button.closest('[data-record]');
    const data = record.dataset;
    if (!/^\d{4}-\d{2}-\d{2}$/.test(data.date)) return;
    const start = data.date.replaceAll('-', '');
    const end = nextDay(data.date).replaceAll('-', '');
    const tentative = data.tentative === 'true';
    const title = (tentative ? '[Tentative date] ' : '') + data.title;
    const description = [data.speaker, 'Time not recorded; saved as an all-day event.', tentative ? 'Date to be confirmed by the Sangha.' : '', data.url, itemURL(record.id)].filter(Boolean).join('\n');
    if (button.dataset.calendar === 'google') {
      const url = new URL('https://calendar.google.com/calendar/render');
      url.search = new URLSearchParams({action:'TEMPLATE',text:title,dates:`${start}/${end}`,details:description,location:data.location || ''});
      window.open(url.href, '_blank', 'noopener,noreferrer');
    } else {
      const stamp = new Date().toISOString().replace(/[-:]/g,'').replace(/\.\d{3}/,'');
      const lines = ['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Samskrita Sangha IISc//Events//EN','CALSCALE:GREGORIAN','BEGIN:VEVENT',`UID:${record.id}@samskrita-sangha.iisc`,`DTSTAMP:${stamp}`,`DTSTART;VALUE=DATE:${start}`,`DTEND;VALUE=DATE:${end}`,`SUMMARY:${icsEscape(title)}`,`DESCRIPTION:${icsEscape(description)}`,`LOCATION:${icsEscape(data.location || '')}`,`STATUS:${tentative ? 'TENTATIVE' : 'CONFIRMED'}`,'END:VEVENT','END:VCALENDAR'];
      const url = URL.createObjectURL(new Blob([lines.map(foldLine).join('\r\n')+'\r\n'],{type:'text/calendar;charset=utf-8'}));
      const anchor = document.createElement('a');
      anchor.href = url; anchor.download = record.id+'.ics';
      document.body.append(anchor); anchor.click(); anchor.remove();
      setTimeout(() => URL.revokeObjectURL(url), 10000);
      announce('Calendar file downloaded. Open it in your calendar app.');
    }
  });

  const archive = $('[data-archive]');
  if (archive) {
    const form = $('.filters', archive);
    const records = $$('[data-record]', archive);
    const groups = $$('.record-group', archive);
    const list = $('.archive-list', archive);
    const calendar = $('.calendar-panel', archive);
    const viewButtons = $$('[data-view]', archive);
    let view = 'list', month = '', visible = records;
    const monthKey = date => `${date.getFullYear()}-${String(date.getMonth()+1).padStart(2,'0')}`;
    function setField(name, value) {
      const field = form.elements.namedItem(name);
      if (field.tagName === 'SELECT' && ![...field.options].some(option => option.value === value)) value = field.options[0].value;
      field.value = value;
    }
    function readURL() {
      const params = new URLSearchParams(location.search);
      for (const name of ['q','year','category','sort']) setField(name, params.get(name) || (name === 'sort' ? 'newest' : ''));
      view = calendar && params.get('view') === 'calendar' ? 'calendar' : 'list';
      month = /^\d{4}-(0[1-9]|1[0-2])$/.test(params.get('month') || '') && Number(params.get('month').slice(0,4)) >= 1900 ? params.get('month') : '';
    }
    function writeURL() {
      const url = new URL(location.href);
      for (const name of ['q','year','category','sort']) {
        const value = form.elements.namedItem(name).value.trim();
        if (value && !(name === 'sort' && value === 'newest')) url.searchParams.set(name,value);
        else url.searchParams.delete(name);
      }
      if (view === 'calendar') { url.searchParams.set('view','calendar'); url.searchParams.set('month',month); }
      else { url.searchParams.delete('view'); url.searchParams.delete('month'); }
      if (view === 'calendar' && records.some(record => '#'+record.id === url.hash)) url.hash = '';
      try { history.replaceState(null,'',url); } catch { /* file:// may restrict history. */ }
    }
    function agendaItem(record, undated = false) {
      const data = record.dataset;
      return `<article class="agenda-item" id="agenda-${escape(record.id)}"><p class="date">${undated ? escape(data.year)+' · Exact date not recorded' : dateLabel(data.date)}${data.tentative === 'true' ? ' · Date to be confirmed' : ''}</p><a href="#${escape(record.id)}" data-open-record="${escape(record.id)}">${escape(data.title)}</a>${data.speaker ? '<p class="muted">'+escape(data.speaker)+'</p>' : ''}</article>`;
    }
    function renderCalendar() {
      if (!calendar) return;
      if (!month) month = visible.find(record => record.dataset.date)?.dataset.date.slice(0,7) || monthKey(new Date());
      const [year, m] = month.split('-').map(Number);
      const first = new Date(year, m-1, 1);
      $('#calendar-month').textContent = first.toLocaleDateString('en-GB',{month:'long',year:'numeric'});
      const days = new Date(year,m,0).getDate();
      const offset = (first.getDay()+6)%7;
      const monthly = visible.filter(record => record.dataset.date.startsWith(month));
      let html = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].map(day => `<div class="weekday">${day}</div>`).join('');
      for (let blank = 0; blank < offset; blank++) html += '<div class="calendar-day blank" aria-hidden="true"></div>';
      for (let day = 1; day <= days; day++) {
        const iso = `${month}-${String(day).padStart(2,'0')}`;
        const events = monthly.filter(record => record.dataset.date === iso);
        const today = iso === monthKey(new Date())+'-'+String(new Date().getDate()).padStart(2,'0');
        html += `<div class="calendar-day${today ? ' today' : ''}"><span class="day-number"${today ? ' aria-current="date"' : ''}>${day}</span>${events.map(record => `<a class="calendar-event" href="#agenda-${escape(record.id)}">${escape(record.dataset.title)}</a>`).join('')}</div>`;
      }
      const trailing = (7-(offset+days)%7)%7;
      for (let blank = 0; blank < trailing; blank++) html += '<div class="calendar-day blank" aria-hidden="true"></div>';
      $('.month-grid',calendar).innerHTML = html;
      $('.agenda',calendar).innerHTML = '<h3>Monthly agenda</h3>'+ (monthly.length ? monthly.map(record => agendaItem(record)).join('') : '<p class="agenda-empty">No matching events this month. Choose another month or adjust your filters.</p>');
      const undated = visible.filter(record => !record.dataset.date);
      $('.undated-agenda',calendar).innerHTML = undated.length ? '<h3>Exact dates not recorded</h3>'+undated.map(record => agendaItem(record,true)).join('') : '';
    }
    function apply({save=true, resetMonth=false} = {}) {
      const query = form.elements.q.value.toLocaleLowerCase().trim();
      const year = form.elements.year.value;
      const category = form.elements.category.value;
      const direction = form.elements.sort.value === 'oldest' ? 1 : -1;
      visible = records.filter(record => {
        const data = record.dataset;
        const match = (!year || data.year === year) && (!category || data.category === category) && (!query || [data.title,data.speaker,data.resource,record.textContent].join(' ').toLocaleLowerCase().includes(query));
        record.hidden = !match;
        return match;
      });
      const compare = (a,b) => direction * (a.dataset.date || a.dataset.year).localeCompare(b.dataset.date || b.dataset.year);
      visible.sort(compare);
      for (const parent of $$('.group-records',archive)) $$('[data-record]',parent).sort(compare).forEach(record => parent.append(record));
      groups.forEach(group => { group.hidden = !$$('[data-record]',group).some(record => !record.hidden); });
      if (list.classList.contains('timeline')) groups.sort((a,b) => direction*a.dataset.group.localeCompare(b.dataset.group)).forEach(group => list.append(group));
      $('.results-count',archive).textContent = `${visible.length} ${visible.length === 1 ? 'result' : 'results'}${query || year || category ? ' found' : ' in the archive'}`;
      $('[data-empty]',archive).hidden = visible.length > 0;
      list.hidden = view !== 'list' || !visible.length;
      const accordionTools = $('.accordion-tools',archive);
      if (accordionTools) accordionTools.hidden = view !== 'list' || !visible.length;
      if (calendar) {
        calendar.hidden = view !== 'calendar' || !visible.length;
        if (resetMonth) month = '';
        renderCalendar();
      }
      viewButtons.forEach(button => button.setAttribute('aria-pressed',String(button.dataset.view === view)));
      if (save) writeURL();
    }
    function openHash() {
      let id;
      try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
      const record = records.find(record => record.id === id);
      if (!record) return;
      if (record.hidden) for (const name of ['q','year','category']) setField(name,'');
      view = 'list';
      const detail = record.closest('.activity-group');
      if (detail) detail.open = true;
      apply();
      requestAnimationFrame(() => { record.scrollIntoView({block:'start'}); record.focus({preventScroll:true}); });
    }
    form.addEventListener('submit',event => event.preventDefault());
    form.addEventListener('input', () => {
      groups.forEach(group => { if (group.tagName === 'DETAILS') group.open = true; });
      const url = new URL(location.href); url.hash = '';
      try { history.replaceState(null,'',url); } catch {}
      apply({resetMonth:true});
    });
    form.addEventListener('reset', () => setTimeout(() => apply({resetMonth:true}),0));
    $('[data-reset]',archive).addEventListener('click',() => form.reset());
    viewButtons.forEach(button => button.addEventListener('click',() => { view = button.dataset.view; apply(); }));
    $$('[data-expand]',archive).forEach(button => button.addEventListener('click',() => {
      groups.filter(group => !group.hidden).forEach(group => { group.open = button.dataset.expand === 'true'; });
      announce(button.dataset.expand === 'true' ? 'All activity sections expanded.' : 'All activity sections collapsed.');
    }));
    if (calendar) {
      $$('[data-month]',calendar).forEach(button => button.addEventListener('click', () => {
        const [year,m] = month.split('-').map(Number);
        const next = new Date(year,m-1+Number(button.dataset.month),1);
        if (next.getFullYear() < 1900 || next.getFullYear() > 9999) return;
        month = monthKey(next); apply();
      }));
      $('[data-today]',calendar).addEventListener('click',() => { month = monthKey(new Date()); apply(); });
      calendar.addEventListener('click',event => {
        const link = event.target.closest('[data-open-record]');
        if (!link) return;
        event.preventDefault();
        const url = new URL(location.href); url.hash = link.dataset.openRecord;
        try { history.pushState(null,'',url); } catch { location.hash = link.dataset.openRecord; }
        openHash();
      });
    }
    window.addEventListener('popstate',() => { readURL(); apply({save:false}); openHash(); });
    window.addEventListener('hashchange',openHash);
    readURL(); apply({save:false}); openHash();
  }

  const galleryLinks = $$('[data-gallery]');
  const lightbox = $('.lightbox');
  if (galleryLinks.length && lightbox) {
    const preview = $('.lightbox-stage img',lightbox);
    const error = $('.lightbox-error',lightbox);
    let index = 0, opener, loadToken = 0;
    function showImage(next) {
      index = (next + galleryLinks.length)%galleryLinks.length;
      const link = galleryLinks[index];
      $('#lightbox-caption').textContent = link.dataset.title;
      $('.lightbox-counter',lightbox).textContent = `${index+1} / ${galleryLinks.length}`;
      error.hidden = true;
      preview.hidden = false;
      preview.src = 'images/image-unavailable.svg';
      preview.alt = link.dataset.title;
      const token = ++loadToken;
      const image = new Image();
      image.onload = () => { if (token === loadToken) { preview.src = image.src; preview.alt = link.dataset.title; } };
      image.onerror = () => { if (token === loadToken) { error.hidden = false; preview.hidden = true; } };
      image.src = link.dataset.gallery;
    }
    galleryLinks.forEach((link,i) => link.addEventListener('click',event => {
      event.preventDefault(); opener = link; showImage(i);
      lightbox.showModal(); document.body.classList.add('modal-open');
      $('[data-lightbox-close]',lightbox).focus();
    }));
    $('[data-lightbox-close]',lightbox).addEventListener('click',() => lightbox.close());
    $('[data-lightbox-prev]',lightbox).addEventListener('click',() => showImage(index-1));
    $('[data-lightbox-next]',lightbox).addEventListener('click',() => showImage(index+1));
    lightbox.addEventListener('keydown',event => {
      if (event.key === 'Tab') {
        const controls = $$('button:not([disabled])', lightbox);
        const first = controls[0], last = controls[controls.length - 1];
        if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
        else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
      }
      if (event.key === 'ArrowRight') { event.preventDefault(); showImage(index+1); }
      if (event.key === 'ArrowLeft') { event.preventDefault(); showImage(index-1); }
    });
    lightbox.addEventListener('click',event => {
      if (event.target !== lightbox) return;
      const rect = lightbox.getBoundingClientRect();
      if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) lightbox.close();
    });
    lightbox.addEventListener('close',() => { loadToken++; document.body.classList.remove('modal-open'); opener?.focus(); });
  }
  $$('img[data-fallback]').forEach(image => image.addEventListener('error',() => {
    image.src = 'images/image-unavailable.svg'; image.alt = 'Image unavailable';
  },{once:true}));
})();
