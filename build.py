#!/usr/bin/env python3

import json
from jinja2 import Template

def generate_html(template, items, lang):
    model = map(lambda x: {
        "name": x["name"][lang],
        "url": x["url"],
        "image": x["image"],
        "description": x["description"][lang],
        "tags": x["tags"]
    }, items)
    html = Template(template).render(items=model)
    with open(f'index_{lang}.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    with open('template.html', 'r', encoding='utf-8') as f:
        template = f.read()
    with open('items.json', 'r', encoding='utf-8') as f:
        items = json.load(f)
    for lang in ['en', 'zh']:
        generate_html(template, items, lang)
