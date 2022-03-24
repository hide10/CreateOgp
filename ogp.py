# ktaskn.jp
# https://ktaskn.jp/post/9

import os
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

STRIP_WIDTH = 1200
STRIP_HEIGHT = 630
FILE_FONT = "C:\\Users\\kobayashi\\Dropbox\\blog\\OgpMake\\Noto_Sans_JP\\NotoSansJP-Light.otf"

def make_ogp(text):
    # テキストを必要に応じて折り返す
    text = insert_return(text)

    # イメージデータを初期化
    im = Image.new("RGB", (STRIP_WIDTH, STRIP_HEIGHT), "#309AC1")
    draw = ImageDraw.Draw(im)

    # フォントを読み込む
    font = ImageFont.truetype(FILE_FONT, 90)
    # フォントの高さを計算する
    text_width, text_height = draw.textsize(text, font)
    # フォントの出力位置（画像の概ね真ん中）を計算する
    position = ((STRIP_WIDTH - text_width) / 2, (STRIP_HEIGHT - text_height) / 2 - 50)
    # 元画像にテキストを合成
    draw.text(position, text, font=font)

    # PNGに変換
    # buffer = BytesIO()
    im.save("test.png", format="PNG")
    im.show()

# 文字を折り返すメソッド
# もっといい方法考えるべきだが、今回はざっくりと10文字ごとに折り返す
def insert_return(text):
    if len(text) > 20:
        return text[:10] + "\n" + text[10:20] + "\n" + text[20:]
    elif len(text) > 10:
        return text[:10] + "\n" + text[10:20]
    else:
        return text

make_ogp("新型コロナワクチン接種、3回目は人生最悪クラスの悪寒を経験する")
