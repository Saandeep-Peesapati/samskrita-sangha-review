"""Accessible static grammar roadmap and lessons, progressively enhanced by JS."""
from html import escape as e
from course_content import LESSONS, STAGES

BY_ID = {lesson['id']:lesson for lesson in LESSONS}
BASE = 'https://en.wikisource.org/wiki/Sanskrit_Grammar_(Whitney)'
CHAPTERS = {'I':'Alphabet', 'II':'Pronunciation', 'IV':'Cases, gender & number', 'V':'Noun declension', 'VII':'Pronouns', 'IX':'The present system'}
def url(id): return f'learn-{id}.html'
def link(id): return f'<a href="{url(id)}">{e(BY_ID[id]["title"])}</a>'
def shell_start(): return '<div class="container course" data-course-ids="'+','.join(BY_ID)+'">'
def progress():
    return '''<div class="course-progress course-interactive" hidden><div class="progress-heading"><span>Your progress</span><strong data-progress-label>0 of 12 complete</strong></div><progress data-progress max="12" value="0" aria-label="Lessons completed"></progress><p class="storage-note" data-storage-note>Saved in this browser. No account needed.</p><p class="course-status" data-progress-status role="status" aria-live="polite"></p></div>'''

def learning_page(root, intro, btn, icon, escape):
    out=shell_start()+'''<div class="course-intro"><span class="eyebrow">A foundation in Sanskrit grammar</span><h1>One branch at a time.</h1><p>Learn to read and build simple Sanskrit sentences. Start at the roots, explore the branches, and bring it all together.</p><div class="course-facts"><span>12 lessons</span><span>Complete beginners</span><span>English · Devanagari · IAST</span></div></div>'''
    out+='<div class="course-topline"><div><h2 id="tree-heading">Your learning tree</h2><p>Follow the numbers for a suggested order. Every lesson is open to you.</p><a class="button primary" data-resume href="learn-sounds.html">Start with sounds '+icon('arrow')+'</a></div>'+progress()+'</div>'
    out+='<noscript><p class="course-note">Every lesson and practice solution is available without JavaScript. Enable JavaScript for interactive quizzes and saved completion progress.</p></noscript><nav class="learning-tree" aria-labelledby="tree-heading">'
    for n,(label,ids) in enumerate(STAGES,1):
        out+=f'<section class="tree-stage" aria-labelledby="stage-{n}"><h3 class="stage-label" id="stage-{n}"><span>{n:02}</span>{e(label)}</h3><ol class="tree-row tree-row-{len(ids)}">'
        for id in ids:
            item=BY_ID[id]; number=LESSONS.index(item)+1
            out+=f'''<li value="{number}"><a class="tree-node" href="{url(id)}" data-node="{id}"><span class="node-top"><span class="node-number">Lesson {number:02}</span><span class="node-status" data-node-status>Open lesson</span></span><span class="node-title">{e(item['title'])}</span><span class="node-description">{e(item['subtitle'])}</span><span class="node-foot">10 min · Read &amp; practise {icon('arrow')}</span></a></li>'''
        out+='</ol></section>'
    out+='</nav><div class="tree-finish"><span aria-hidden="true">✦</span><h2>Your first sentences, your own words.</h2><p>Return to any branch whenever you need a refresher.</p></div>'
    out+='''<details class="progress-reset course-interactive" hidden><summary>Reset my learning progress</summary><p>This clears completion marks for this course in this browser. Lessons remain available.</p><button type="button" class="button secondary" data-reset-progress>Clear all completion marks</button></details>'''
    return out+'</div>'

def block_html(block):
    kind=block[0]
    if kind=='p': return f'<p>{block[1]}</p>'
    if kind=='note': return f'<aside class="concept-note"><strong>Keep in mind</strong><p>{block[1]}</p></aside>'
    if kind=='table':
        _,caption,headers,rows=block
        return '<div class="grammar-table-wrap" role="region" aria-label="'+e(caption)+'" tabindex="0"><table class="grammar-table"><caption>'+e(caption)+'</caption><thead><tr>'+''.join('<th scope="col">'+e(h)+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join((('<th scope="row">' if j==0 else '<td>')+str(cell)+('</th>' if j==0 else '</td>')) for j,cell in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div>'
    if kind=='examples':
        return '<div class="worked-examples">'+''.join(f'<figure class="worked-example"><p lang="sa">{e(sa)}</p><p class="transliteration">{e(roman)}</p><p class="example-meaning">{e(meaning)}</p><figcaption>{e(reason)}</figcaption></figure>' for sa,roman,meaning,reason in block[1])+'</div>'
    raise ValueError(kind)

def lesson_page(item, icon):
    number=LESSONS.index(item)+1
    out=shell_start()+f'''<nav class="lesson-breadcrumb" aria-label="Breadcrumb"><a href="learn.html">Learning tree</a><span aria-hidden="true">/</span><span>Lesson {number:02}</span></nav><header class="lesson-intro"><span class="eyebrow">Foundation grammar · Lesson {number:02} of 12</span><h1>{e(item['title'])}</h1><p>{e(item['subtitle'])}</p><span class="study-time">About 10 minutes · Read, reflect &amp; practise</span></header>'''
    out+='<div class="lesson-layout"><aside class="lesson-sidebar"><details class="lesson-outline" open><summary>In this lesson</summary><nav aria-label="On this page"><ol><li><a href="#outcomes">What you’ll learn</a></li>'+''.join(f'<li><a href="#concept-{n}">{e(s["title"])}</a></li>' for n,s in enumerate(item['sections'],1))+'<li><a href="#mistakes">Common mistakes</a></li><li><a href="#lesson-quiz">Check your understanding</a></li><li><a href="#lesson-practice">Practise on your own</a></li><li><a href="#recap">Recap &amp; next steps</a></li></ol></nav></details>'+progress()+'</aside><article class="lesson-body" data-lesson="'+item['id']+'">'
    out+='<section class="lesson-outcomes" id="outcomes"><span class="eyebrow">By the end</span><h2>What you’ll learn</h2><ul>'+''.join('<li>'+e(s)+'</li>' for s in item['objectives'])+'</ul>'
    out+=('<p class="suggested-lessons"><strong>Helpful first:</strong> '+', '.join(link(id) for id in item['prerequisites'])+'. These are suggestions; you can explore in any order.</p>' if item['prerequisites'] else '<p class="suggested-lessons">No prior Sanskrit knowledge needed. Take your time and read the examples aloud.</p>')+'</section>'
    out+='<p class="notation-note">Every example pairs Devanagari with IAST and an English meaning. Word boundaries stay visible; full external sandhi is postponed so you can focus on forms.</p>'
    for n,s in enumerate(item['sections'],1):
        out+=f'<section class="concept-section" id="concept-{n}"><span class="concept-number">{n:02}</span><h2>{e(s["title"])}</h2>'+''.join(block_html(b) for b in s['blocks'])+'</section>'
    out+='<section class="mistakes-panel" id="mistakes"><h2>Common mistakes</h2><ul>'+''.join('<li>'+e(t)+'</li>' for t in item['mistakes'])+'</ul></section>'
    out+='<section class="quiz-section" id="lesson-quiz"><span class="eyebrow">Pause &amp; check</span><h2>Check your understanding</h2><p>Choose one answer for each question. You can retry as often as you like.</p><form class="lesson-quiz course-interactive" hidden novalidate>'
    for n,q in enumerate(item['quizzes'],1):
        out+=f'<fieldset data-answer="{q["answer"]}" aria-describedby="feedback-{n}"><legend>{n}. {e(q["question"])}</legend>'
        for j,option in enumerate(q['options']):
            out+=f'<label class="quiz-option"><input type="radio" name="question-{n}" value="{j}"><span>{e(option)}</span></label>'
        out+=f'<p class="quiz-feedback" id="feedback-{n}" hidden data-explanation="{e(q["why"])}" data-correct-text="{e(q["options"][q["answer"]])}"></p></fieldset>'
    out+='<div class="quiz-actions"><button type="submit" class="button primary">Check answers</button><button type="reset" class="button secondary">Try again</button></div><p class="quiz-summary" role="status" aria-live="polite" tabindex="-1"></p></form><div class="quiz-offline"><p>With JavaScript off, try each question, then open its answer.</p>'
    for q in item['quizzes']:
        out+='<details><summary>'+e(q['question'])+'</summary><ul>'+''.join('<li>'+e(v)+'</li>' for v in q['options'])+'</ul><p><strong>Answer: '+e(q['options'][q['answer']])+'</strong> '+e(q['why'])+'</p></details>'
    out+='</div></section><section class="lesson-practice" id="lesson-practice"><span class="eyebrow">Make it your own</span><h2>Practise on your own</h2><p>Write an answer or say it aloud before opening the solution.</p>'
    for n,ex in enumerate(item['exercises'],1):
        out+=f'<div class="practice-item"><h3>{n}. {e(ex["question"])}</h3><details><summary>Reveal solution {n}</summary><div class="practice-answer">{ex["answer"]}</div></details></div>'
    out+='</section><section class="lesson-recap" id="recap"><span class="eyebrow">Take this with you</span><h2>Lesson recap</h2><ul>'+''.join('<li>'+e(t)+'</li>' for t in item['recap'])+'</ul><button type="button" class="button primary course-interactive" hidden data-complete="'+item['id']+'" aria-pressed="false">Mark lesson complete</button><p class="completion-help">Completion is your choice. Every lesson stays accessible.</p></section>'
    out+='<nav class="lesson-pagination" aria-label="Lesson navigation">'
    if number>1: out+='<a href="'+url(LESSONS[number-2]['id'])+'"><span>← Previous lesson</span><strong>'+e(LESSONS[number-2]['title'])+'</strong></a>'
    if number<len(LESSONS): out+='<a href="'+url(LESSONS[number]['id'])+'"><span>Next lesson →</span><strong>'+e(LESSONS[number]['title'])+'</strong></a>'
    else: out+='<a href="learn.html"><span>Return to the tree →</span><strong>Review your learning journey</strong></a>'
    out+='</nav><section class="lesson-references" aria-labelledby="reference-heading"><h2 id="reference-heading">Sources &amp; further reading</h2><p>Original explanations, examples, and exercises prepared for this course. Grammatical foundations: William Dwight Whitney’s public-domain <cite>Sanskrit Grammar</cite>. Historical terminology and transliteration have been adapted to a beginner sequence using IAST.</p><ul>'+''.join(f'<li><a href="{BASE}/Chapter_{c}" target="_blank" rel="noopener noreferrer">Chapter {c}: {e(CHAPTERS[c])}</a></li>' for c in item['sources'])+f'</ul><p><a href="{BASE}" target="_blank" rel="noopener noreferrer">Original text &amp; public-domain notice</a></p></section></article></div></div>'
    return out

def build_lessons(root, layout, icon):
    for item in LESSONS:
        html=layout('learn',item['title'],lesson_page(item,icon))
        html=html.replace('href="learn.html" aria-current="page"','href="learn.html" aria-current="location"')
        (root/url(item['id'])).write_text(html,encoding='utf-8')
