# 文字列OGP画像の生成プログラム

ブログやSNSなどの投稿で使用するOGP画像を用意するのが面倒なので生成できるようにしました。

## 事前準備

1. フォントファイルを用意してください。
1. プログラム中の FONT_PATH で上記フォントを指定してください。

自分が作成する時はGoogleフォントをお借りしました。

[Noto Sans Japanese - Google Fonts](https://fonts.google.com/noto/specimen/Noto+Sans+JP)

## 使い方

引数として渡した文字列を良い感じに描画した画像を「文字列A.PNG」「文字列B.PNG」としてPNG画像に保存します。

    python create_ogp.py 文字列A 文字列B

以上
