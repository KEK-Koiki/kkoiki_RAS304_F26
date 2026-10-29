"""Build priced tables and product cards from the small JSON catalogs.

Run from any directory: python tools/bom/render.py --check
Omit --check to write the generated Markdown/CSV/sourcing record.
"""
from pathlib import Path
from decimal import Decimal
import argparse,csv,html,io,json,re

ROOT=Path(__file__).resolve().parents[2]
def load(name):
    return json.loads((ROOT/'data/bom'/name).read_text(encoding='utf-8'))
def money(number):
    return f'{Decimal(str(number)):.2f}'
def photo(part,width):
    path=part.get('local_image')
    if not path:return ''
    path=path.replace('../static/','../../static/')
    return f'<img src="{path}" alt="{html.escape(part["mpn"])} supplier reference photo" width="{width}" loading="lazy">'
def table(parts):
    rows=['<div class="bom-table" markdown>','','| Part / reference photo | Ref. / Qty | Manufacturer & example MPN | Unit USD | Line USD | Sources |','| --- | --- | --- | ---: | ---: | --- |']
    for p in parts:
        links=f'[Supplier]({p["source"]})'
        links+=f' · [Datasheet]({p["datasheet"]})' if p.get('datasheet') else ' · specs/docs on supplier page'
        rows.append(f'| {photo(p,78)}<br>**{p["description"]}** | {p["refs"]}<br>**{p["qty"]} pcs** | {p["manufacturer"]}<br><code>{p["mpn"]}</code> | ${money(p["price"])} | **${money(p["line_total"])}** | {links} |')
    return '\n'.join(rows+['','</div>'])
def selected_card(p):
    template=(ROOT/'templates/components/selected-card.html').read_text(encoding='utf-8')
    values={'PHOTO':photo(p,160),'REFS':p['refs'],'QUANTITY':str(p['qty']),
            'PIECES':'pieces' if p['qty']>1 else 'piece','MPN':p['mpn'],
            'DESCRIPTION':p['description'],'PRICE':money(p['price']),
            'EXTENDED':money(p['line_total']),'SOURCE':p['source'],
            'DATASHEET':p.get('datasheet',p['source'])}
    for key,value in values.items():template=template.replace('{{'+key+'}}',value)
    return template
def outputs():
    groups=[load('core.json'),load('passives.json'),load('interfaces.json')]
    parts=[p for group in groups for p in group]
    for p in parts:
        if p['qty']<1 or p['price']<0:raise ValueError(f'Invalid purchasing inputs: {p["mpn"]}')
        p['line_total']=float(Decimal(str(p['price']))*p['qty'])
    adapter=load('adapter.json');adapter['line_total']=adapter['price']*adapter['qty']
    totals=[sum(Decimal(str(p['line_total'])) for p in g) for g in groups]
    subtotal=sum(totals)
    tokens={'CORE_TABLE':table(groups[0]),'PASSIVE_TABLE':table(groups[1]),
            'INTERFACE_TABLE':table(groups[2]),'ADAPTER_TABLE':table([adapter]),
            'CORE_TOTAL':money(totals[0]),'PASSIVE_TOTAL':money(totals[1]),
            'INTERFACE_TOTAL':money(totals[2]),'SUBTOTAL':money(subtotal),
            'WITH_ADAPTER':money(subtotal+Decimal(str(adapter['line_total']))),
            'FIT_NOTES':'\n'.join(f'- **{p["refs"]} / {p["mpn"]}:** {p["note"]}' for p in parts if p['note'])}
    bom=(ROOT/'templates/bom/page.md').read_text(encoding='utf-8')
    for key,value in tokens.items():bom=bom.replace('{{'+key+'}}',value)
    if '{{' in bom:raise ValueError('Unresolved BOM template token')
    current=(ROOT/'docs/02-Component-Selection/Component-Selection.md').read_text(encoding='utf-8')
    start=current.index('<div class="component-cards" markdown>')
    end=current.index('*Product images:',start)
    cards='<div class="component-cards" markdown>\n'+''.join(selected_card(p) for p in groups[0])
    # The optional external supply has its own small template.
    extra=(ROOT/'templates/components/adapter-card.html').read_text(encoding='utf-8')
    for key,value in {'PHOTO':photo(adapter,160),'PRICE':money(adapter['price']),
                      'SOURCE':adapter['source'],'DATASHEET':adapter['datasheet']}.items():
        extra=extra.replace('{{'+key+'}}',value)
    cards+=extra+'</div>\n\n'
    component=current[:start]+cards+current[end:]
    stream=io.StringIO(newline='');writer=csv.writer(stream)
    writer.writerow(['Group','References','Quantity','Description','Manufacturer','Example MPN','Unit USD (qty 1)','Extended USD','Supplier URL','Selection notes'])
    for p in parts:writer.writerow([p['group'],p['refs'],p['qty'],p['description'],p['manufacturer'],p['mpn'],money(p['price']),money(p['line_total']),p['source'],p['note']])
    record=load('metadata.json');record['subtotal']=str(subtotal);record['parts']=parts;record['optional_adapter']=adapter
    return {'docs/03-BOM/BOM.md':bom,
            'docs/02-Component-Selection/Component-Selection.md':component,
            'docs/03-BOM/encoder-revb-bom.csv':'\ufeff'+stream.getvalue(),
            'docs/03-BOM/encoder-parts-sources.json':json.dumps(record,indent=2,ensure_ascii=False)+'\n'}
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='Report differences without changing files')
    args=parser.parse_args();different=[]
    for name,text in outputs().items():
        path=ROOT/name
        # CSV contains CRLF by design; Markdown comparisons ignore checkout newline style.
        existing=path.read_bytes().decode('utf-8').replace('\r\n','\n')
        same=(json.loads(existing)==json.loads(text)) if path.suffix=='.json' else (existing==text.replace('\r\n','\n'))
        if not same:
            different.append(name)
            if not args.check:path.write_bytes(text.encode('utf-8'))
    if args.check and different:raise SystemExit('Generated files differ: '+', '.join(different))
    print('BOM/card outputs match.' if args.check else 'Updated '+str(len(different))+' generated files.')
if __name__=='__main__':main()
