#!/usr/bin/env python3
# tools/seed_snippets.py
import os, textwrap
ROOT = "snippets"
LANGS = ["python","java","c","cpp","javascript","go","ruby","php","kotlin","rust","swift","bash"]
TOPICS = [d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT,d))]
SNIPPETS = [
  ("hello-world","Print Hello World"),
  ("fibonacci","Iterative + recursive Fibonacci"),
  ("factorial","Iterative factorial"),
  ("binary-search","Binary search (iterative)"),
  ("bubble-sort","Bubble sort (educational)"),
  ("reverse-string","Reverse a string"),
  ("palindrome-check","Check palindrome"),
  ("prime-check","Check primality (sqrt method)"),
  ("merge-sort","Merge sort (recursive)"),
  ("stack-example","Basic stack implementation")
]

for topic in TOPICS:
    for lang in LANGS:
        folder = os.path.join(ROOT, topic, lang)
        os.makedirs(folder, exist_ok=True)
        for name, desc in SNIPPETS:
            ext = {
                "python": ".py","java":".java","c":".c","cpp":".cpp","javascript":".js",
                "go":".go","ruby":".rb","php":".php","kotlin":".kt","rust":".rs","swift":".swift","bash":".sh"
            }.get(lang,".txt")
            fname = f"{name}{ext}"
            path = os.path.join(folder, fname)
            if os.path.exists(path): continue
            header = f"# Title: {desc}\n# Topic: {topic}\n# Language: {lang}\n# Example: see bottom\n\n"
            body = ""
            if lang == "python":
                body = textwrap.dedent("""\
                def main(n=10):
                    a,b=0,1
                    out=[]
                    for _ in range(n):
                        out.append(a)
                        a,b=b,a+b
                    return out

                if __name__ == '__main__':
                    print(main(10))
                """)
            else:
                body = f"// {desc} - placeholder in {lang}\n"
            with open(path,"w",encoding="utf-8") as f:
                f.write(header+body)
print("Seeding complete.")
