"""Check built page links, image targets, anchors and downloadable ZIPs.

Usage: python tools/check_links.py [build-directory]
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import zipfile,json,sys,re
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'site'
class Links(HTMLParser):
 def __init__(self):super().__init__();self.urls=[];self.ids=set()
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):self.ids.add(a['id'])
  for key in ['href','src']:
   if a.get(key):self.urls.append(a[key])
pages={}
for p in root.rglob('*.html'):
 parser=Links();parser.feed(p.read_text(encoding='utf-8'));pages[p.resolve()]=parser
if not pages:raise SystemExit('No built HTML found; run python -m mkdocs build --strict first.')
errors=[];checked=0
for p,parser in pages.items():
 for url in parser.urls:
  u=urlsplit(url)
  if u.scheme or u.netloc or url.startswith('data:'):continue
  site_path=unquote(u.path)
  if site_path.startswith('/kkoiki_RAS304_F26/'):
   site_path=site_path[len('/kkoiki_RAS304_F26'):]
  target=(root/site_path.lstrip('/')) if site_path.startswith('/') else p.parent/site_path
  if not u.path:target=p
  if target.is_dir():target=target/'index.html'
  target=target.resolve();checked+=1
  if not target.exists():errors.append((str(p.relative_to(root)),url,'missing file'))
  elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:errors.append((str(p.relative_to(root)),url,'missing anchor'))
for css in root.rglob('*.css'):
 for target in re.findall(r'@import\s+url\([\"\']([^\"\']+)',css.read_text(encoding='utf-8')):
  checked+=1
  if not (css.parent/target).is_file():errors.append((str(css),'missing CSS import',target))
for p in root.rglob('*.zip'):
 with zipfile.ZipFile(p) as z:
  if z.testzip():errors.append((str(p),'corrupt ZIP'))
print(json.dumps({'html_pages':len(pages),'local_links_checked':checked,'issues':errors},indent=2))
if errors:raise SystemExit(1)
