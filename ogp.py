import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

OGP_WIDTH = 1200
OGP_HEIGHT = 630
FILE_FONT = "C:\\Users\\kobayashi\\Dropbox\\blog\\OgpMake\\Noto_Sans_JP\\NotoSansJP-Light.otf"


def make_ogp(text):
    text = textwrap.fill(text, 10)

    im = Image.new("RGB", (OGP_WIDTH, OGP_HEIGHT), "#309AC1")
    draw = ImageDraw.Draw(im)

    # フォントを読み込む
    font = ImageFont.truetype(FILE_FONT, 90)
    # フォントの高さを計算する
    text_width, text_height = draw.textsize(text, font)
    # フォントの出力位置（画像の概ね真ん中）を計算する
    position = ((OGP_WIDTH - text_width) / 2,
                (OGP_HEIGHT - text_height) / 2 - 50)
    # 元画像にテキストを合成
    draw.text(position, text, font=font)

    # PNGに変換
    im.save("test.png", format="PNG")
    im.show()


make_ogp("新型コロナワクチン接種、3回目は人生最悪クラスの悪寒を経験する")
