#!/usr/bin/env python3
import os
ROOT="snippets"
out=["# Snippets Index\nThis is an auto-generated index. Run `python tools/generate_index.py` to update.\n"]
for topic in sorted(os.listdir(ROOT)):
    tpath=os.path.join(ROOT,topic)
    if not os.path.isdir(tpath): continue
    out.append(f"## {topic}\n")
    for lang in sorted(os.listdir(tpath)):
        lpath=os.path.join(tpath,lang)
        if os.path.isdir(lpath):
            files = sorted([f for f in os.listdir(lpath) if not f.startswith('.')])
            if files:
                out.append(f"- **{lang}**")
                for f in files:
                    rel = os.path.join("snippets",topic,lang,f)
                    out.append(f"  - [{f}]({rel})")
    out.append("")
open(os.path.join(ROOT,"README.md"),"w",encoding="utf-8").write("\n".join(out))
print("snippets/README.md updated")
