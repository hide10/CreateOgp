import sys, textwrap
from PIL import Image, ImageDraw, ImageFont

OGP_WIDTH = 1200
OGP_HEIGHT = 630
BG_COLOR = "#309AC1"
TEXT_WRAP_WIDTH = 10
FONT_PATH = "NotoSansJP-Medium.otf"


def create_ogp(text):
    # 新しいImageオブジェクトを生成
    im = Image.new("RGB", (OGP_WIDTH, OGP_HEIGHT), BG_COLOR)
    # Drawオブジェクトを生成
    draw = ImageDraw.Draw(im)

    # 画像横幅の3/4を文字数で賄うフォントサイズを計算する
    if len(text) < TEXT_WRAP_WIDTH:
        text_len = len(text)
    else:
        text_len = TEXT_WRAP_WIDTH
    font_size = OGP_WIDTH / 4 * 3 / text_len
    # フォントの指定
    font = ImageFont.truetype(FONT_PATH, int(font_size))

    # テキストを折り返す
    wrap_text = textwrap.fill(text, TEXT_WRAP_WIDTH)

    # 描画時のテキストサイズを取得
    text_width, text_height = draw.textsize(wrap_text, font)

    # 描画位置が真ん中あたりになるように調整
    position = ((OGP_WIDTH - text_width) / 2,
                (OGP_HEIGHT - text_height) / 2 - 50)
    # 文字描画
    draw.text(position, wrap_text, font=font)
    # ファイル保存
    im.save(text + ".png", "PNG")
    # 表示確認
    im.show()


for in_file in sys.argv[1:]:
    # 引数ベースでOGP画像を作成
    create_ogp(in_file)
