#!/usr/bin/env python3
"""Checks every built page: internal links and #anchors resolve, images exist,
ids are unique, and elements are properly closed. Run from the site root:

    python3 tools/check_links.py
"""
import os
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.stack, self.errors = [], [], [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        for key in ('href', 'src'):
            if key in a and a[key]:
                self.links.append((tag, a[key]))
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.errors.append(f'unexpected </{tag}> (open: {self.stack[-3:]})')


def pages():
    for d, _, files in os.walk(ROOT):
        if '/.git' in d or '/tools' in d:
            continue
        for f in files:
            if f.endswith('.html'):
                yield os.path.join(d, f)


parsed = {}
for path in pages():
    p = Page()
    with open(path, encoding='utf-8') as fh:
        p.feed(fh.read())
    parsed[path] = p

problems = []
for path, p in parsed.items():
    rel = os.path.relpath(path, ROOT)
    if p.stack:
        problems.append(f'{rel}: unclosed {p.stack}')
    problems += [f'{rel}: {e}' for e in p.errors]
    dupes = {i for i in p.ids if p.ids.count(i) > 1}
    if dupes:
        problems.append(f'{rel}: duplicate ids {sorted(dupes)}')
    for tag, url in p.links:
        u = urlparse(url)
        if u.scheme in ('http', 'https', 'mailto', 'tel') or url.startswith('//'):
            continue
        base = ROOT if url.startswith('/') else os.path.dirname(path)
        target = os.path.normpath(os.path.join(base, unquote(u.path.lstrip('/')))) if u.path else path
        if os.path.isdir(target):
            target = os.path.join(target, 'index.html')
        if not os.path.exists(target):
            problems.append(f'{rel}: missing {url}')
            continue
        if u.fragment and target.endswith('.html'):
            tp = parsed.get(target)
            if tp is not None and u.fragment not in tp.ids:
                problems.append(f'{rel}: missing anchor {url}')

print(f'Checked {len(parsed)} pages.')
if problems:
    print('\n'.join(problems))
    sys.exit(1)
print('All links, anchors and images resolve; HTML is well formed.')
