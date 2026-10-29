"""Compare HTML, active assets and style declarations between two MkDocs builds."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import argparse,json,re

class References(HTMLParser):
    def __init__(self):super().__init__();self.urls=[]
    def handle_starttag(self,tag,attributes):
        a=dict(attributes)
        self.urls.extend(a[k] for k in ('src','href') if a.get(k))

def css_rules(text):
    text=re.sub(r'/\*.*?\*/','',text,flags=re.S)
    depth=0;quote=None;start=0;rules=[]
    for i,c in enumerate(text):
        if quote:
            if c==quote and (i==0 or text[i-1]!='\\'):quote=None
        elif c in ('"',"'"):quote=c
        elif c=='{':depth+=1
        elif c=='}':
            depth-=1
            if depth==0:
                normalized=re.sub(r'\s+','',text[start:i+1])
                rules.append(re.sub(r';(?=})','',normalized))
                start=i+1
    return sorted(rules)

def expand_css(path):
    text=path.read_text(encoding='utf-8')
    return re.sub(r'@import\s+url\("([^"]+)"\);',lambda m:expand_css(path.parent/m[1]),text)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('before',type=Path);parser.add_argument('after',type=Path)
    args=parser.parse_args();before=args.before.resolve();after=args.after.resolve()
    differences=[];pages=0;assets=set()
    for page in before.rglob('*.html'):
        relative=page.relative_to(before);target=after/relative;pages+=1
        if not target.exists() or page.read_bytes()!=target.read_bytes():differences.append(str(relative))
        refs=References();refs.feed(page.read_text(encoding='utf-8'))
        for url in refs.urls:
            parts=urlsplit(url)
            if parts.scheme or parts.netloc or not parts.path:continue
            path=unquote(parts.path)
            if path.startswith('/kkoiki_RAS304_F26/'):path=path[len('/kkoiki_RAS304_F26'):]
            p=(before/path.lstrip('/')) if path.startswith('/') else page.parent/path
            p=p.resolve()
            if p.is_file() and p.suffix not in ['.html','.css']:assets.add(p.relative_to(before))
    for name in assets:
        if not (after/name).is_file() or (before/name).read_bytes()!=(after/name).read_bytes():differences.append(str(name))
    same_styles=css_rules(expand_css(before/'stylesheets/extra.css'))==css_rules(expand_css(after/'stylesheets/extra.css'))
    if not same_styles:differences.append('custom CSS selectors/declarations')
    print(json.dumps({'html_pages_compared':pages,'active_assets_compared':len(assets),'same_style_rules':same_styles,'differences':differences},indent=2))
    if not pages or differences:raise SystemExit(1)
if __name__=='__main__':main()
