"""
悠哉 Yozai Medium（標籤、標題、原主日記用）。
從 @chinese-fonts/yozai 套件的切片中，只複製 index.html 用得到的部分到 fonts/yozai/。
劇本改動以後重新執行：
    npm i @chinese-fonts/yozai
    python3 tools/yozai_slices.py node_modules/@chinese-fonts/yozai/dist/Yozai-Medium
字型授權：SIL OFL 1.1（Y.OzFont / LXGW）
"""
import sys, os, re, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = sys.argv[1]
out = os.path.join(ROOT, "fonts", "yozai")
text = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
used = set(ord(c) for c in text)
used.update(ord(c) for c in "，。、！？：；「」『』（）…—～・0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

def parse_range(r):
    s = set()
    for part in r.split(","):
        part = part.strip().upper().replace("U+", "")
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-"); s.update(range(int(a, 16), int(b, 16) + 1))
        else:
            s.add(int(part, 16))
    return s

css = open(os.path.join(src, "result.css"), encoding="utf-8").read()
blocks = re.findall(r"@font-face\s*\{[^}]*\}", css)
if os.path.isdir(out):
    shutil.rmtree(out)
os.makedirs(out)
keep = []
for b in blocks:
    m = re.search(r"unicode-range:([^;}]*)", b)
    f = re.search(r'url\("?\.?/?([^")]+\.woff2)"?\)', b)
    if not m or not f:
        continue
    if parse_range(m.group(1)) & used:
        shutil.copy(os.path.join(src, f.group(1)), out)
        b = re.sub(r'font-family:\s*"[^"]*"', 'font-family:"Yozai"', b)
        keep.append(b)
open(os.path.join(out, "yozai.css"), "w", encoding="utf-8").write("\n".join(keep) + "\n")
size = sum(os.path.getsize(os.path.join(out, x)) for x in os.listdir(out))
print(len(keep), "slices,", size // 1024, "KB")
