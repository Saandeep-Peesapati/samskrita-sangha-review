"""Build the static site with Python's standard library: python scripts/build.py."""
from pathlib import Path
from html import escape
from datetime import date
import json
from course_pages import learning_page, build_lessons

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'data/content.json').read_text(encoding='utf-8'))
NAV = [('index','Home'),('about','About'),('learn','Learn Samskrita'),('talks','Invited Talks'),('activities','Activities'),('blogs','Blog'),('gallery','Gallery'),('members','Members'),('contact','Contact')]
PATHS = {
 'arrow':'M5 12h14m-5-5 5 5-5 5',
 'external':'M14 3h7v7m0-7L10 14M10 3H3v18h18v-7',
 'video':'m9 7 8 5-8 5V7ZM3 3h18v18H3z',
 'audio':'M9 18V5l12-2v13M9 8l12-2M9 18c0 2-6 4-6 1s6-3 6-1Zm12-2c0 2-6 4-6 1s6-3 6-1Z',
 'pdf':'M14 2H4v20h16V8l-6-6Zm0 0v6h6M8 13h8M8 17h6',
 'book':'M12 5C8 2 3 3 2 4v16c3-2 7-2 10 0m0-15c4-3 9-2 10-1v16c-3-2-7-2-10 0V5Z',
 'chat':'M21 11a9 9 0 0 1-9 9H3l2-4a9 9 0 1 1 16-5ZM8 10h8M8 14h5',
 'science':'M9 3h6m-5 0v7L4 20c0 1 1 1 2 1h12c1 0 2 0 2-1l-6-10V3M7 15h10',
 'mail':'M3 5h18v14H3V5Zm0 0 9 8 9-8',
 'copy':'M9 8h12v13H9V8ZM5 16H3V3h12v2',
 'calendar':'M3 5h18v16H3V5ZM3 10h18M8 2v6m8-6v6',
 'image':'M3 3h18v18H3V3Zm0 14 6-6 4 4 3-3 5 5M16 7h.01',
 'people':'M16 21v-3a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v3M9 3a4 4 0 1 0 0 8 4 4 0 0 0 0-8Zm7 1a4 4 0 0 1 0 7m6 10v-3a4 4 0 0 0-3-4',
 'menu':'M3 6h18M3 12h18M3 18h18',
 'close':'m6 6 12 12M6 18 18 6',
 'chevron':'m6 9 6 6 6-6',
 'pin':'M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0ZM12 7a3 3 0 1 0 0 6 3 3 0 0 0 0-6Z'
}
def e(value): return escape(str(value), quote=True)
def icon(name):
 return f'<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="{PATHS.get(name, PATHS["external"])}"/></svg>'
def btn(url, label, primary=False, symbol='arrow', external=False):
 return f'<a class="button {"primary" if primary else "secondary"}" href="{e(url)}"{(" target="+chr(34)+"_blank"+chr(34)+" rel="+chr(34)+"noopener noreferrer"+chr(34)) if external else ""}>{icon(symbol)}<span>{e(label)}</span></a>'
def intro(label,title,subtitle):
 return f'<div class="page-intro"><span class="eyebrow">{e(label)}</span><h1>{e(title)}</h1><p>{e(subtitle)}</p><span class="divider" aria-hidden="true"></span></div>'
def layout(page,title,body):
 links=''.join(f'<li><a href="{key}.html"{chr(32)+"aria-current="+chr(34)+"page"+chr(34) if key==page else ""}>{label}</a></li>' for key,label in NAV)
 course_assets='\n  <link rel="stylesheet" href="css/course.css"><script src="js/learning.js" defer></script>' if page=='learn' else ''
 return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Samskrita Sangha at the Indian Institute of Science, Bengaluru. Explore Sanskrit talks, study circles, articles, and our campus community.">
  <title>{e(title)} — Samskrita Sangha IISc</title>
  <link rel="icon" href="images/logo.png"><link rel="stylesheet" href="css/style.css"><link rel="stylesheet" href="css/learning.css">
  <script src="js/site.js" defer></script>{course_assets}
</head>
<body data-page="{page}">
<a class="skip-link" href="#main-content">Skip to content</a>
<header class="site-header"><nav class="main-nav container" aria-label="Main navigation">
 <a class="brand" href="index.html" aria-label="Samskrita Sangha IISc home"><span><span class="brand-name" lang="sa">संस्कृतसङ्घः</span><span class="brand-caption">Samskrita Sangha · IISc</span></span></a>
 <button class="menu-toggle secondary" type="button" aria-expanded="false" aria-controls="primary-navigation">{icon('menu')}<span>Menu</span></button>
 <ul class="nav-links" id="primary-navigation">{links}</ul>
</nav></header>
<main id="main-content" tabindex="-1">{body}</main>
<footer class="site-footer"><div class="container footer-inner"><div><span class="footer-name">Samskrita Sangha</span><p>Indian Institute of Science, Bengaluru</p></div><p class="footer-motto" lang="sa">सा विद्या या विमुक्तये</p><a class="text-link" href="contact.html">Get in touch {icon('arrow')}</a></div></footer>
<div class="toast" role="status" aria-live="polite" aria-atomic="true"></div>
</body></html>'''
def dated(item):
 if not item.get('date'): return e(item.get('year','Date to be announced'))+' · Exact date not recorded'
 d=date.fromisoformat(item['date'])
 return f'<time datetime="{d.isoformat()}">{d.day} {d.strftime("%B %Y")}</time>'+(' <span class="date-note">· Date to be confirmed</span>' if item.get('tentative') else '')
def actions(item,kind):
 out='<div class="item-actions">'
 if item.get('url'):
  out+=btn(item['url'], {'video':'Watch recording','audio':'Listen to audio','pdf':'Read PDF','external':'Read article'}.get(item.get('type'),'Open resource'), True, item.get('type','external'),True)
 elif item.get('type'):
  out+=f'<span class="availability">{icon(item["type"])}{e(item.get("resourceName","Article"))} · Link coming soon</span>'
 out+=f'<button type="button" class="text-button enhanced-only" data-share="{e(item["id"])}" aria-label="Copy link to {e(item["title"])}">{icon("copy")}<span>Copy link</span></button>'
 if kind in ('talks','activities') and item.get('date'):
  out+=f'''<details class="calendar-actions enhanced-only"><summary>{icon('calendar')} Add to calendar</summary><div class="calendar-options"><p>Time not recorded. Saves as an all-day event.{(' Date is tentative.' if item.get('tentative') else '')}</p><button type="button" class="text-button" data-calendar="ics">Download .ics (Apple / Outlook)</button><button type="button" class="text-button" data-calendar="google">Google Calendar {icon('external')}</button></div></details>'''
 return out+'</div>'
def record(item,kind,compact=False):
 year=item.get('date',item.get('year',''))[:4]
 attrs=f'data-record data-title="{e(item["title"])}" data-speaker="{e(item.get("speaker",""))}" data-resource="{e(item.get("resourceName",""))}" data-year="{year}" data-date="{item.get("date","")}" data-category="{e(item["category"])}" data-tentative="{str(item.get("tentative",False)).lower()}" data-location="{e(item.get("location",""))}" data-url="{e(item.get("url") or "")}"'
 body=f'<div class="record-meta"><span class="badge">{e(item["category"])}</span><span class="date">{dated(item)}</span></div><h3>{e(item["title"])}</h3>'
 if item.get('speaker'): body+=f'<p class="speaker">{e(item["speaker"])}</p>'
 if item.get('description'): body+=f'<p>{e(item["description"])}</p>'
 if item.get('students'): body+=f'<dl class="record-facts"><div><dt>Participants</dt><dd>{item["students"]} students</dd></div><div><dt>Venue</dt><dd>{e(item["location"])}</dd></div></dl>'
 if compact:
  body+=f'<a class="text-link" href="{kind}.html#{e(item["id"])}">Explore {"talk" if kind=="talks" else "activity"} {icon("arrow")}</a>'
 else: body+=actions(item,kind)
 if kind == 'blogs': body=body.replace('<h3>', '<h2>').replace('</h3>', '</h2>')
 return f'<article class="record {"compact-record" if compact else ""}" id="{e(item["id"])}" {attrs} tabindex="-1">{body}</article>'
def filters(kind,items,calendar=False):
 years=sorted({i.get('date',i.get('year',''))[:4] for i in items},reverse=True)
 categories=sorted({i['category'] for i in items})
 return f'''<form class="filters enhanced-only" role="search" aria-label="Search {kind}"><label class="search-field">Search {kind}<input type="search" name="q" placeholder="Title, speaker, or resource" autocomplete="off"></label><label>Year<select name="year"><option value="">All years</option>{''.join(f'<option>{y}</option>' for y in years)}</select></label><label>Category<select name="category"><option value="">All categories</option>{''.join(f'<option>{e(c)}</option>' for c in categories)}</select></label><label>Sort by<select name="sort"><option value="newest">Newest first</option><option value="oldest">Oldest first</option></select></label><button class="text-button reset-filters" type="reset">Reset filters</button></form>
<div class="results-toolbar enhanced-only"><p class="results-count" role="status" aria-live="polite"></p>{('<div class="view-switch" role="group" aria-label="Event view"><button type="button" data-view="list" aria-pressed="true">List</button><button type="button" data-view="calendar" aria-pressed="false">'+icon('calendar')+' Calendar</button></div>') if calendar else ''}</div>
<div class="empty-state" data-empty hidden><h2>No matching results</h2><p>Try a different title, speaker, year, or category.</p><button type="button" class="button secondary" data-reset>Clear filters</button></div>'''
def calendar_panel():
 return f'''<section class="calendar-panel" aria-label="Event calendar" hidden><div class="calendar-heading"><h2 id="calendar-month"></h2><div class="calendar-navigation"><button type="button" class="secondary" data-month="-1" aria-label="Previous month">←</button><button type="button" class="secondary" data-today>This month</button><button type="button" class="secondary" data-month="1" aria-label="Next month">→</button></div></div><p class="muted">Dates with events link to the agenda below. On phones, the agenda is the calendar view.</p><div class="month-grid" aria-label="Month overview"></div><div class="agenda" aria-live="polite"></div><div class="undated-agenda"></div></section>'''

hero='''<section class="hero"><div class="container hero-inner hero-split"><div class="hero-identity"><div class="emblem-frame"><img class="hero-logo" src="images/logo.png" alt="Samskrita Sangha IISc emblem: a lamp within a blue crest" width="186" height="228" fetchpriority="high"></div><p class="identity-name" lang="sa">संस्कृतसङ्घः</p><span class="identity-caption">Indian Institute of Science</span></div><div class="hero-copy"><span class="eyebrow">A living tradition at IISc · Bengaluru</span><h1>Samskrita<br>Sangha</h1><p class="hero-motto" lang="sa"><strong>सा विद्या या विमुक्तये</strong></p><p class="hero-description">A community of learning, conversation,<br>and discovery through Sanskrit.</p><div class="hero-actions">'''+btn('learn.html','Learn Samskrita',True,'book')+btn('activities.html','Explore our activities',False,'arrow')+'''</div></div><div class="hero-invocation"><span class="eyebrow">An invocation to learning</span><p class="hero-verse" lang="sa"><strong>वाक्यकारं वररुचिं भाष्यकारं पतञ्जलिम्।<br>पाणिनिं सूत्रकारं च प्रणतोऽस्मि मुनित्रयम् ॥</strong></p></div></div></section>'''
home=hero+'<div class="container home-content"><section class="upcoming-section"><div><span class="eyebrow">On the horizon</span><h2>Upcoming at the Sangha</h2><p>Talks, reading circles, and opportunities to learn together.</p></div><div class="upcoming-content">'
upcoming=[(i,k) for k in ('talks','activities') for i in DATA[k] if i.get('date','')>=date.today().isoformat()]
if upcoming:
 home+=''.join(record(i,k,True) for i,k in sorted(upcoming,key=lambda x:x[0]['date'])[:4])
else:
 home+='<p class="upcoming-title">New dates will be announced here.</p><p>Stay connected for the next invited talk or campus activity.</p>'+btn('contact.html','Stay in touch',True,'chat')
home+='</div></section><section class="section"><div class="section-heading"><div><span class="eyebrow">From the archive</span><h2>Ideas worth returning to</h2></div><a class="text-link" href="talks.html">All invited talks '+icon('arrow')+'</a></div><div class="record-grid">'+''.join(record(i,'talks',True) for i in DATA['talks'][:2])+'</div></section>'
home+='<section class="section"><div class="section-heading"><div><span class="eyebrow">Study & practice</span><h2>Learning, together</h2></div><a class="text-link" href="activities.html">All activities '+icon('arrow')+'</a></div><div class="record-grid">'+''.join(record(i,'activities',True) for i in sorted([i for i in DATA['activities'] if i.get('date')],key=lambda i:i['date'],reverse=True)[:2])+'</div></section></div>'

about='<div class="container">'+intro('Our vision & purpose','A language. A shared pursuit.','Preserving, celebrating, and exploring Sanskrit at IISc.')+'''<section class="mission"><span class="eyebrow">Samskrita Sangha</span><h2>A meeting place for curious minds</h2><p class="lead">Samskrita Sangha at the Indian Institute of Science, Bengaluru, is dedicated to preserving, celebrating, and exploring the Sanskrit language—one of the world’s richest intellectual and literary traditions.</p><p>Our mission is to demystify Sanskrit for the campus community, moving beyond pure grammar drills to cultivate an appreciation for classical poetics, computational linguistics, scientific treatises, and timeless philosophical literature.</p></section><section class="section"><div class="section-heading"><div><span class="eyebrow">Core pursuits</span><h2>What we do</h2></div></div><div class="pillars">'''
for symbol,title,body in [('chat','Active communication','Conducting 10-day intensive spoken Sanskrit workshops (संभाषणशिबिरम्) in collaboration with Samskrita Bharati, empowering students to converse in simple Sanskrit.'),('book','Classical text circles','Weekly reading groups dissecting foundational shastras, poetics (Kavyaprakasha, Kadambari), and the Bhagavad Gita through rigorous padachheda and anvaya breakdown.'),('science','Science & philosophy','Inviting scholars, scientists, and philosophers to deliver public lectures exploring Indian mathematical traditions, logic (Nyaya), and ancient scientific literature.')]:
 about+=f'<article class="pillar"><span class="icon-tile">{icon(symbol)}</span><h3>{e(title)}</h3><p>{e(body)}</p></article>'
about+='</div></section><section class="welcome-panel"><span class="eyebrow">Open participation</span><h2>There is a place for everyone</h2><p>All students, research scholars, staff, faculty, and campus residents across IISc departments are welcome to attend our weekly swadhyaya circles and lectures. No prior knowledge of the language is required.</p>'+btn('contact.html','Join the Sangha',True,'people')+'</section></div>'

talks='<div class="container archive" data-archive="talks">'+intro('Discourses & perspectives','Invited talks & lectures','Explore scholarly discourses, public lectures, and philosophical conversations at IISc.')+filters('talks',DATA['talks'],True)+'<div class="archive-list timeline">'
for y in sorted({i['date'][:4] for i in DATA['talks']},reverse=True):
 talks+=f'<section class="record-group" data-group="{y}"><h2 class="timeline-year">{y}</h2><div class="group-records">'+''.join(record(i,'talks') for i in DATA['talks'] if i['date'].startswith(y))+'</div></section>'
talks+='</div>'+calendar_panel()+'</div>'

activities='<div class="container archive" data-archive="activities">'+intro('Initiatives & circles','Learning through participation','Weekly study circles, spoken Sanskrit camps, and ongoing campus sessions.')+filters('resources',DATA['activities'],True)+'<div class="accordion-tools enhanced-only"><button class="text-button" type="button" data-expand="true">Expand all</button><span aria-hidden="true">/</span><button class="text-button" type="button" data-expand="false">Collapse all</button></div><div class="archive-list activity-list">'
for category,title,desc,symbol in [('Reading circles','Weekly classes & reading circles','Regular sessions covering grammatical analysis, text reading, and philosophical dialogues.','book'),('Spoken Sanskrit camps','Spoken Sanskrit camps','10-day intensive spoken Sanskrit camps conducted across campus in coordination with Samskrita Bharati.','chat')]:
 activities+=f'<details class="activity-group record-group" data-group="{e(category)}" open><summary><h2 class="summary-title">{icon(symbol)}<span>{e(title)}<span class="sanskrit-subtitle" lang="sa">{"साप्ताहिक-वर्गाः" if symbol=="book" else "संभाषणशिबिरम्"}</span></span></h2>{icon("chevron")}</summary><div class="activity-content"><p class="group-description">{e(desc)}</p><div class="group-records">'+''.join(record(i,'activities') for i in sorted([i for i in DATA['activities'] if i['category']==category],key=lambda i:i.get('date',i.get('year','')),reverse=True))+'</div></div></details>'
activities+='</div>'+calendar_panel()+'</div>'

blogs='<div class="container archive" data-archive="blogs">'+intro('Articles & reflections','The Sangha journal','Literary commentary, mathematical explorations, and essays from our community.')+filters('articles',DATA['articles'])+'<div class="archive-list editorial-list"><div class="group-records">'+''.join(record(i,'blogs') for i in sorted(DATA['articles'],key=lambda i:i['date'],reverse=True))+'</div></div><p class="editorial-note">Article links and author details will appear as they become available.</p></div>'

gallery='<div class="container">'+intro('Moments & memories','The gallery','Glimpses of our camps, invited talks, exhibitions, and campus activities.')+'<p class="gallery-note">Photographs are awaiting upload. Each collection keeps its place below; full-size viewing becomes available when its image is added.</p><div class="gallery-grid">'
for item in DATA['gallery']:
 available=(ROOT/item['src']).exists()
 gallery+=f'''<figure class="gallery-card" id="{item['id']}"><a class="gallery-open" href="{item['src'] if available else 'images/image-unavailable.svg'}" data-gallery="{e(item['src'])}" data-title="{e(item['title'])}" aria-label="Open {e(item['title'])}"><span class="gallery-image"><img src="{item['src'] if available else 'images/image-unavailable.svg'}" alt="{e(item['alt']) if available else 'Image awaiting upload'}" width="600" height="450" loading="lazy" data-fallback><span class="gallery-zoom">{icon('image')} View full size</span></span></a><figcaption><h2>{e(item['title'])}</h2><p>{'View photograph' if available else 'Image awaiting upload'}</p></figcaption></figure>'''
gallery+='</div><dialog class="lightbox" aria-labelledby="lightbox-caption"><div class="lightbox-top"><span class="lightbox-counter"></span><button class="button secondary" type="button" data-lightbox-close>'+icon('close')+' Close</button></div><div class="lightbox-stage"><img alt=""><p class="lightbox-error" hidden>Image unavailable. This photograph has not been uploaded yet.</p></div><div class="lightbox-bottom"><button class="secondary" type="button" data-lightbox-prev aria-label="Previous image">←</button><h2 id="lightbox-caption"></h2><button class="secondary" type="button" data-lightbox-next aria-label="Next image">→</button></div></dialog></div>'

members='<div class="container">'+intro('Our community','Members & volunteers','The students, research scholars, and alumni carrying forward our initiatives at IISc.')+'<section class="section"><div class="section-heading"><h2>Active committee & volunteers</h2></div><div class="member-grid">'
for m in DATA['members']:
 initials=''.join(n[0] for n in m['name'].split()[:2])
 members+=f'<article class="member-card"><div class="member-top"><span class="avatar" aria-hidden="true">{initials}</span><div><h3>{e(m["name"])}</h3><p class="member-role">{e(m["role"])}</p></div></div><p class="member-dept">{e(m["department"])}</p><div class="member-actions">'+(f'<a class="text-link" href="mailto:{e(m["email"])}" aria-label="Contact the committee about {e(m["name"])}">{icon("mail")} Contact committee</a>' if m.get('email') else '<span class="muted">Profile link to be added</span>')+'</div></article>'
members+='</div></section><section class="section alumni-section"><div><span class="eyebrow">Continuing connections</span><h2>Alumni directory</h2><p>Batch of 2024–2025</p></div><div class="empty-panel"><h3>Alumni details are being prepared.</h3><p>Contact the committee to contribute or update a profile.</p><a class="text-link" href="contact.html">Contact the Sangha '+icon('arrow')+'</a></div></section></div>'

email='samskrutasangha.iisc@gmail.com'
contact='<div class="container">'+intro('Connect','Come be part of the conversation','Get in touch with the student committee or join our community circles.')+'<div class="contact-layout"><section class="contact-methods" aria-labelledby="contact-heading"><h2 id="contact-heading">Reach the Sangha</h2>'
contact+=f'<article class="contact-method"><span class="icon-tile">{icon("mail")}</span><div><h3>Email us</h3><a class="contact-email" href="mailto:{email}">{email}</a><div class="contact-actions">'+btn('mailto:'+email,'Write to us',True,'mail')+f'<button class="text-button enhanced-only" type="button" data-copy="{email}">{icon("copy")}<span>Copy email</span></button></div></div></article>'
contact+='<article class="contact-method"><span class="icon-tile">'+icon('chat')+'</span><div><h3>WhatsApp community</h3><p>Connect with our campus circles.</p><a class="button whatsapp" href="https://chat.whatsapp.com/JSRgm77b3J9LOLZXSMdBfJ" target="_blank" rel="noopener noreferrer">'+icon('chat')+' Join on WhatsApp</a></div></article>'
contact+='<article class="contact-method"><span class="icon-tile">'+icon('video')+'</span><div><h3>YouTube channel</h3><p>Revisit talks and shared learning.</p>'+btn('https://www.youtube.com/@SamskrutaSanghaIIScसंस्कृतसङ्घ','Visit our channel',False,'video',True)+'</div></article></section><aside class="support-panel"><span class="eyebrow">Support our work</span><h2>Help learning flourish</h2><p>Contributions help organize speaking camps and student reading materials.</p><div class="upi-block"><span class="field-label">UPI ID</span><strong>samskrutasangha.iisc@sbi</strong><button class="text-button enhanced-only" type="button" data-copy="samskrutasangha.iisc@sbi">'+icon('copy')+'<span>Copy UPI ID</span></button></div><p class="muted">For questions about supporting an activity, please contact the committee.</p></aside></div></div>'

learn=learning_page(ROOT, intro, btn, icon, e)
for page,title,body in [('index','Home',home),('about','About',about),('learn','Learn Samskrita',learn),('talks','Invited Talks',talks),('activities','Activities',activities),('blogs','Blog',blogs),('gallery','Gallery',gallery),('members','Members',members),('contact','Contact',contact)]:
 (ROOT/f'{page}.html').write_text(layout(page,title,body),encoding='utf-8')
build_lessons(ROOT, layout, icon)
print('Built 9 site pages and 12 grammar lessons.')
