# xion_to_txt

`img`には[xion.pdf](http://conlinguistics.org/arka/images/xion.pdf)をページごとに[PDFtoPNG](http://pdf2png.com/ja/)でPNG化したもの、`docs`にはそれらを[GoogleドライブのOCR機能](https://support.google.com/drive/answer/176692)を利用して文書形式にしたものを格納

## コミットメモ

* `txts_docx2txt`
  * [docx2txt](https://pypi.python.org/pypi/docx2txt/0.6)を使用して抽出したテキスト＋使用したスクリプト

* `cleaned_txt`
  * `txts_docx2txt`を人力で清書したもの