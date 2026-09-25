"""Standard-library checks for the generated HTML, content and local links."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json

ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__()
        self.ids=[]; self.links=[]; self.tags=[]; self.current=[]
        self.feed(text)
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs); self.tags.append(tag)
        if 'id' in attrs:self.ids.append(attrs['id'])
        if attrs.get('aria-current') in ('page','location'):self.current.append(attrs.get('href'))
        for key in ('href','src'):
            if attrs.get(key):self.links.append(attrs[key])
        if tag=='img':assert 'alt' in attrs
        if attrs.get('target')=='_blank':assert 'noopener' in attrs.get('rel','')

pages={p.name:Page(p.read_text(encoding='utf-8')) for p in ROOT.glob('*.html')}
count=0
for name,page in pages.items():
    assert page.tags.count('main')==1 and page.tags.count('h1')==1 and page.tags.count('footer')==1,name
    assert len(page.ids)==len(set(page.ids)),name
    assert page.current==[('learn.html' if name.startswith('learn-') else name)],name
    for link in page.links:
        assert link!='#',(name,'Empty link')
        url=urlsplit(link)
        if url.scheme:continue
        dest=ROOT/unquote(url.path or name)
        assert dest.exists(),(name,link)
        if url.fragment and dest.name in pages:assert unquote(url.fragment) in pages[dest.name].ids,(name,link)
        count+=1
data=json.loads((ROOT/'data/content.json').read_text(encoding='utf-8'))
for group in ('talks','activities','articles'):
    ids=[item['id'] for item in data[group]]
    assert len(ids)==len(set(ids))

def luminance(color):
    rgb=[int(color[i:i+2],16)/255 for i in (1,3,5)]
    rgb=[c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4 for c in rgb]
    return sum(a*b for a,b in zip(rgb,[.2126,.7152,.0722]))
for label,fg,bg in [('body','#302c29','#fbf9f4'),('muted','#68615a','#f5ead5'),('saffron','#9a501d','#f5ead5'),('badge','#764417','#f5ead5'),('primary','#ffffff','#651e32'),('WhatsApp','#ffffff','#176440')]:
    values=sorted([luminance(fg),luminance(bg)])
    ratio=(values[1]+.05)/(values[0]+.05)
    assert ratio>=4.5,(label,ratio)
    print(f'{label} contrast: {ratio:.2f}:1')
print(f'PASS: {len(pages)} pages, {count} local links/assets, unique anchors, page landmarks, active navigation, image alt text, external-link safety, content IDs and text contrast.')
