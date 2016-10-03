# xion_to_txt

`img`には[xion.pdf](http://conlinguistics.org/arka/images/xion.pdf)をページごとに[PDFtoPNG](http://pdf2png.com/ja/)でPNG化したもの、`docs`にはそれらを[GoogleドライブのOCR機能](https://support.google.com/drive/answer/176692)を利用して文書形式にしたものを格納

## コミットメモ

* `txts_docx2txt`
  * [docx2txt](https://pypi.python.org/pypi/docx2txt/0.6)を使用して抽出したテキスト＋使用したスクリプト

* `first_draft`
  * `txts_docx2txt`の人力による第一段階の清書。 整形とかはこの段階でだいたいやっておく。

* `first_draft_with_wrong_arka`
  * `txts_docx2txt`の人力による第一段階の清書のうち、幻字などが未修正のまま含まれているもの。誤った幻字は`[FIXME--`と`]`で囲むこと。

## 整形方法
1. 日本語文中の半角スペースを改行に置き換える(`([^!?a-zA-Z,əɔı|).0-9])[ ]`→`\1\n`がお薦め)
2. 元のpdfを見ながら、整形していく。  
    * 日本語の地の文の冒頭は全角スペースを入れる。鍵カッコがあるときは字下げしない。
	* 3点リーダーは必ず`……`、ダッシュは必ず`――`の形式に修正する。
	* 拗音・促音・画数の多い漢字の読み間違いが意外と多いので修正する。
	* 日本語文中の疑問符・感嘆符は全角。
	* アルカ部分は`[ARKA--`と`]`で囲む。幻字を読む気力がないときは、誤字を`[FIXME--`と`]`で囲む。
