import textwrap
from xml.dom.expatbuilder import TEXT_NODE
from PIL import Image, ImageDraw, ImageFont

OGP_WIDTH = 1200
OGP_HEIGHT = 630
TEXT_WRAP = 10
BG_COLOR = "#309AC1"
FONT_FILE = "C:\\Users\\kobayashi\\Dropbox\\blog\\OgpMake\\Noto_Sans_JP\\NotoSansJP-Light.otf"


def create_ogp(text):
    im = Image.new("RGB", (OGP_WIDTH, OGP_HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(im)

    font = ImageFont.truetype(FONT_FILE, 90)
    # テキストを折り返す
    wrap_text = textwrap.fill(text, TEXT_WRAP)
    text_width, text_height = draw.textsize(wrap_text, font)
    position = ((OGP_WIDTH - text_width) / 2,
                (OGP_HEIGHT - text_height) / 2 - 50)
    draw.text(position, wrap_text, font=font)

    im.save(text + ".png", format="PNG")
    im.show()


create_ogp("新型コロナワクチン接種、3回目は人生最悪クラスの悪寒を経験する")
