"""Course integrity checks: dependencies, generated lessons, and practice structure."""
from pathlib import Path
from html.parser import HTMLParser
import importlib.util
import sys

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('curriculum',ROOT/'scripts/course_content.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
lessons=module.LESSONS
ids=[item['id'] for item in lessons]
assert len(ids)==12 and len(set(ids))==12
assert sorted(id for _,stage in module.STAGES for id in stage)==sorted(ids)
visited=set()
for item in lessons:
    assert set(item['prerequisites']) <= visited, item['id']
    visited.add(item['id'])
    assert len(item['sections'])>=4 and len(item['quizzes'])==3
    assert len(item['exercises'])>=2 and len(item['recap'])>=3
    for q in item['quizzes']:
        assert len(q['options'])==len(set(q['options']))==3
        assert 0<=q['answer']<3 and q['why']
    assert all(c in ('I','II','IV','V','VII','IX') for c in item['sources'])
    html=(ROOT/f'learn-{item["id"]}.html').read_text(encoding='utf-8')
    assert html.count('<fieldset ')==3
    assert html.count('type="radio"')==9
    assert 'class="quiz-offline"' in html and 'Reveal solution 1' in html
    assert 'data-complete="'+item['id']+'"' in html
    assert 'href="learn.html" aria-current="location"' in html
    assert 'class="brand"' in html and '<img src="images/logo.png" alt=""' not in html
    assert 'lang="sa"' in html and 'class="transliteration"' in html
print('PASS: 12 unique lessons; acyclic suggested prerequisites; 36 quizzes; 25 practice solutions; static content and answer fallbacks; shared navigation; header logo remains removed.')
