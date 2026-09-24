#!/usr/bin/env python3
"""content/*.md から index.html / en.html の自動生成部分を作り直す。

GitHub Actions のデプロイ前に実行される。手元で確認したいときは
    python3 build/build.py
書式エラーがあると理由を表示して終了コード 1 で止まる
（その場合デプロイは行われず、公開中のページはそのまま残る）。
"""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = {"ja": ROOT / "index.html", "en": ROOT / "en.html"}
EN_SPLIT = "---en---"
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


class ContentError(Exception):
    pass


# ---------- parsing ----------
def read_blocks(path):
    """'## 見出し' ごとに {head, ja:[lines], en:[lines], line} を返す"""
    if not path.exists():
        raise ContentError(f"{path.relative_to(ROOT)} が見つかりません")
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    blocks, cur = [], None
    for no, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if line.startswith("## "):
            cur = {"head": line[3:].strip(), "ja": [], "en": None, "line": no}
            blocks.append(cur)
        elif not line:
            continue
        elif cur is None:
            if line.startswith("#"):
                continue
            raise ContentError(f"{path.name} {no}行目: 最初の「## 」より前に文章があります")
        elif line == EN_SPLIT:
            if cur["en"] is not None:
                raise ContentError(f"{path.name} {no}行目: 「{EN_SPLIT}」が1件の中に2回あります")
            cur["en"] = []
        else:
            (cur["en"] if cur["en"] is not None else cur["ja"]).append(line)
    return blocks


def is_link_row(line):
    rest = LINK_RE.sub("", line)
    return bool(LINK_RE.search(line)) and not re.sub(r"[\s·|/／、,]", "", rest)


def inline(text):
    """HTML エスケープ + [文字](URL) → <a> + *強調* → <em>"""
    out, pos = [], 0
    for m in LINK_RE.finditer(text):
        out.append(_emph(html.escape(text[pos:m.start()])))
        label, url = m.group(1), m.group(2)
        if re.match(r"^(https?://|mailto:)", url):
            ext = ' target="_blank" rel="noopener"' if url.startswith("http") else ""
            out.append(f'<a href="{html.escape(url, quote=True)}"{ext}>{_emph(html.escape(label))}</a>')
        else:
            out.append(html.escape(m.group(0)))
        pos = m.end()
    out.append(_emph(html.escape(text[pos:])))
    return "".join(out)


def _emph(s):
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)


def split_body(lines, where):
    if not lines:
        raise ContentError(f"{where}: タイトル行がありません")
    title, paras, links = lines[0], [], []
    for ln in lines[1:]:
        (links if is_link_row(ln) else paras).append(ln)
    return title, paras, links


def links_html(rows):
    items = [LINK_RE.findall(r) for r in rows]
    anchors = "".join(inline(f"[{t}]({u})") for row in items for t, u in row)
    return f'<div class="nlinks">{anchors}</div>' if anchors else ""


# ---------- rendering ----------
def render_news(blocks, lang):
    lis = []
    for b in blocks:
        where = f"news.md {b['line']}行目「## {b['head']}」"
        date, _, cat = (p.strip() for p in b["head"].partition("|"))
        if not date:
            raise ContentError(f"{where}: 日付がありません（例: ## 2026.09 | Release）")
        lines = b["ja"] if lang == "ja" else b["en"]
        if lang == "en" and not lines:
            continue
        title, paras, links = split_body(lines, where + (" の英語部分" if lang == "en" else ""))
        body = "".join(f"<p>{inline(p)}</p>" for p in paras)
        chip = f'<span class="ncat">{html.escape(cat)}</span>' if cat else ""
        lis.append(f'      <li><time>{html.escape(date)}</time><div>{chip}'
                   f'<div class="t">{inline(title)}</div>{body}{links_html(links)}</div></li>')
    return '<ul class="news">\n' + "\n".join(lis) + "\n    </ul>"


def render_research(blocks, lang):
    arts, n = [], 0
    for b in blocks:
        where = f"research.md {b['line']}行目「## {b['head']}」"
        lines = b["ja"] if lang == "ja" else b["en"]
        if lang == "en" and not lines:
            continue
        n += 1
        title, paras, links = split_body(lines, where + (" の英語部分" if lang == "en" else ""))
        body = "".join(f"<p>{inline(p)}</p>" for p in paras)
        arts.append(f'      <article class="theme"><div class="tn">{n:02d}</div>'
                    f'<div class="tcat">{html.escape(b["head"])}</div><h3>{inline(title)}</h3>'
                    f'{body}{links_html(links)}</article>')
    return '<div class="themes">\n' + "\n".join(arts) + "\n    </div>"


def replace_between(page, name, new, path):
    start, end = f"<!-- AUTO:{name} -->", f"<!-- /AUTO:{name} -->"
    pat = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if len(pat.findall(page)) != 1:
        raise ContentError(f"{path.name} に目印 {start} … {end} が1組ありません")
    return pat.sub(lambda _: f"{start}\n    {new}\n    {end}", page)


def main():
    try:
        news = read_blocks(ROOT / "content" / "news.md")
        research = read_blocks(ROOT / "content" / "research.md")
        if not news:
            raise ContentError("news.md にお知らせが1件もありません")
        out = {}
        for lang, path in PAGES.items():
            page = path.read_text(encoding="utf-8")
            page = replace_between(page, "news", render_news(news, lang), path)
            page = replace_between(page, "research", render_research(research, lang), path)
            out[path] = page
        for path, page in out.items():  # 全部そろってから書き込む
            path.write_text(page, encoding="utf-8")
        print(f"OK: お知らせ {len(news)} 件 / 研究テーマ {len(research)} 件を反映しました")
    except ContentError as e:
        print(f"::error::{e}")
        print(f"書式エラー: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
