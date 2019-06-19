#クラスのインポート
from reportlab.pdfgen import canvas #描写領域を表現
from reportlab.pdfbase import pdfmetrics#PDFの構造を表現
from reportlab.pdfbase.cidfonts import UnicodeCIDFont#フォントを表現
import reportlab.lib.units as unit#単位を表現
import reportlab.lib.pagesizes as pagesizes#用紙サイズを表現

#フォントの登録
pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))

#PDFを作る
pdf = canvas.Canvas("example.pdf",pagesize = pagesizes.A4)#キャンバスの作成
moji = "あ"

#フォントの大きさは用紙幅と同じ210mmにする
pdf.setFont("HeiseiKakuGo-W5", 210 * unit.mm)
#高さ
h = (297 - 210) / 2 * unit.mm #用紙の中心＝(高さ—フォントサイズ)/2
pdf.drawString(0 * unit.mm, h, moji)
pdf.save()
