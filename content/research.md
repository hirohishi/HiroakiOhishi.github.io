<!--
研究テーマの書き方（このファイルを編集して保存するだけで、1〜2分後にサイトへ反映されます）

・1テーマは「## 英語の短いラベル」の行から、次の「##」の手前まで。書いた順に 01, 02, 03… と番号が付く。
・ラベルの次の1行目 = タイトル、2行目以降 = 本文。
・リンクだけの行はリンク列になる。書き方は [表示する文字](https://...)
・「---en---」の行から下は英語ページ用（1行目 = 英語タイトル、以降 = 英語本文）。

【公開前の確認】ここはインターネットに公開されます。
未発表の結果・使っている因子やコンストラクト名・標的遺伝子・共同研究先の情報・論文の計画は書かない。
助成金の課題名や発表済み論文で公開されている範囲の言葉にとどめる。
-->

## Epigenome Editing
遺伝子の働きを、狙った場所で細かく調整する
遺伝子がどれだけ働くか（転写）は、DNA の配列そのものだけでなく、DNA やその周りに付く化学的な目印「エピゲノム」によっても調節されています。私たちは、この目印を狙った場所に書き込むことで、遺伝子の働きを細かく、思いどおりに調整する技術の開発に取り組んでいます。
---en---
Tuning gene activity at chosen sites
How strongly a gene is used, its transcription, is set not only by the DNA sequence but also by chemical marks on and around the DNA: the epigenome. We are developing ways to write these marks at chosen places in the genome, so that gene activity can be tuned finely and on demand.

## Live Omics
生きた細胞の中で、ゲノムの動きを見る
細胞の核の中で DNA は折りたたまれ、絶えず動いています。遺伝子がどこにあり、いつ働き、どんな目印が付いているのか。これらを生きた細胞のまま同時に観察できる顕微鏡技術をつくり、遺伝子の働きが決まる瞬間をとらえることを目指しています。
---en---
Watching the genome at work in living cells
Inside the nucleus, DNA is folded and constantly moving. Where is a gene, when is it switched on, and which marks does it carry? We are building imaging methods that capture all of these at once in living cells, to catch the moment a gene's activity is decided.

## Image Processing
顕微鏡画像を、速く、同じ基準で見やすくする
厚みのある試料の顕微鏡画像には、ピントの合っていない部分の光がぼんやりと重なります。この背景を取り除く既存の手法（Dark sectioning）を GPU で高速化し、ひとつの実験のすべての画像を同じ基準で処理できるようにしたツール darksec を公開しています。
[GitHub](https://github.com/hirohishi/darksec)
---en---
Faster, consistent processing of microscope images
Images of thick samples carry a haze of out-of-focus light. We have released darksec, a tool that runs an existing background-removal method (Dark sectioning) on the GPU and processes every image of an experiment with one common calibration.
[GitHub](https://github.com/hirohishi/darksec)
