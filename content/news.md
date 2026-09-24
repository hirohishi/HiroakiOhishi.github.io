<!--
お知らせの書き方（このファイルを編集して保存するだけで、1〜2分後にサイトへ反映されます）

・1件は「## 日付 | 種類」の行から、次の「##」の手前まで。新しいものを上に書く。
・見出しの次の1行目 = タイトル、2行目以降 = 本文（本文は省略可）。
・リンクだけの行はボタン風のリンク列になる。書き方は [表示する文字](https://...)
・「---en---」の行から下は英語ページ用。1行目 = 英語タイトル、以降 = 英語本文。
  「---en---」ごと省略すると、その件は英語ページには出ません。
・種類の例: Release / Grant / Appointment / Paper / Talk / Award
・この囲み（<!- - から - ->）の中はサイトに表示されません。
-->

## 2026.09 | Release
背景除去ツール darksec を公開しました
広視野画像から焦点外の背景を除去する Dark sectioning（Cao et al., *Nature Methods* 2025）の GPU 実装です。アルゴリズムは原著のもので、出力が原著実装と一致することを確認したうえで約30倍高速化しました。あわせて、画像ごとの正規化をデータセット×チャンネル単位の較正に置き換え、実験内のすべての画像が同じ変換を受けるようにしています。
[GitHub](https://github.com/hirohishi/darksec) [DOI 10.5281/zenodo.22782788](https://doi.org/10.5281/zenodo.22782788)
---en---
Released darksec
A GPU implementation of Dark sectioning (Cao et al., *Nature Methods* 2025) for removing out-of-focus background from widefield images. The algorithm is the published one: darksec reproduces its output and runs about 30× faster, and replaces the per-image normalisation with a single calibration per dataset and channel, so that every image in an experiment receives the same transform.
[GitHub](https://github.com/hirohishi/darksec) [DOI 10.5281/zenodo.22782788](https://doi.org/10.5281/zenodo.22782788)

## 2026.06 | Grant
獨協医科大学 研究助成金（共同研究）に採択されました
課題名：腎がんを起点とした癌化と細胞老化の運命分岐ダイナミクスの解明
---en---
Awarded a Dokkyo Medical University Research Grant (collaborative)
Project: fate-branching dynamics of transformation and cellular senescence originating from renal cancer.

## 2026.01 | Appointment
獨協医科大学 医学部 ゲノム医科学講座に学内准教授として着任しました
---en---
Appointed Associate Professor, Department of Medical Genome Science, Dokkyo Medical University
