"""Builds index.html: the Médongaule web-size photographs as homepage-style collage spreads.

    python3 build.py      # template.html + manifest.json + .wordmark.svg -> index.html

The order mixes the three groups the way the reference does (mostly gardens, a person now and then, the odd build-up shot).
"""
import json

M = json.load(open('manifest.json'))
PAL = json.load(open('palettes.json'))          # five main colours per photograph, from palette.swift
g = [m for m in M if m['c'] == 'g']; p = [m for m in M if m['c'] == 'p']; b = [m for m in M if m['c'] == 'b']
order, i = [], 0
while g or p or b:
    i += 1
    if g: order.append(g.pop(0))
    if p and i % 5 == 0: order.append(p.pop(0))
    if b and i % 15 == 0: order.append(b.pop(0))
    if not g: order += p + b; p = b = []
def entry(m):
    e = {'f': m['f'], 'c': m['c'], 'w': m['w'], 'h': m['h'], 'p': PAL[m['f']]}
    if m.get('poster'): e['x'] = 1                                   # a poster with words on it, never the tall photo on the left
    if m.get('m'): e.update(m=m['m'], mw=m['mw'], mh=m['mh'])        # its mobile cut, for tall frames
    return e
data = json.dumps([entry(m) for m in order], separators=(',', ':'))
page = open('template.html', encoding='utf-8').read()
page = page.replace('{{WORDMARK}}', open('.wordmark.svg', encoding='utf-8').read()).replace('{{MANIFEST}}', data)
open('index.html', 'w', encoding='utf-8').write(page)
print(len(order), 'photographs')
