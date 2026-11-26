"""
從 index.html 收集用到的字，產生 Maple Mono CN Thin 的精簡字型。
劇本改動以後重新執行一次：
    python3 tools/subset_font.py path/to/MapleMono-CN-Thin.ttf
字型下載：https://github.com/subframe7536/maple-font/releases （MapleMono-CN-unhinted.zip）
"""
import sys, os
from fontTools import subset

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = sys.argv[1]
text = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
# 常用標點與英數字一律保留
text += "，。、！？：；「」『』（）《》〈〉…—～・ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
chars = "".join(sorted(set(text)))

for flavor in ("woff2", "woff"):
    opts = subset.Options()
    opts.flavor = flavor
    opts.layout_features = ["*"]
    font = subset.load_font(src, opts)
    sub = subset.Subsetter(opts)
    sub.populate(text=chars)
    sub.subset(font)
    out = os.path.join(ROOT, "fonts", "maple-mono-cn-thin." + flavor)
    font.flavor = flavor
    font.save(out)
    print(out, os.path.getsize(out) // 1024, "KB")
