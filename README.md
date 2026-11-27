# blg

腐女子主角 BL 遊戲的試玩原型（手帳風介面）。

- `index.html`：遊戲本體，用瀏覽器打開就能玩，支援直屏／橫屏切換
- `fonts/`：台詞用的 Maple Mono CN Thin 精簡字型；`fonts/yozai/` 是標籤、標題和原主日記用的悠哉字型（都只包含遊戲用到的字）
- `fonts/zen-old-mincho-waka.woff2`、`fonts/genyomin-waka.woff2`：扉頁和歌用的明朝體（Zen Old Mincho／源樣明體，只包含和歌和譯文的字，和歌改動時要重新產生）
- `tools/subset_font.py`、`tools/yozai_slices.py`：劇本改動以後，用這兩個重新產生字型

本機預覽時，請把整個資料夾一起下載，字型才會正確顯示。
