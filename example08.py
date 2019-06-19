#クラスのインポート
from reportlab.pdfgen import canvas #描写領域を表現
from reportlab.pdfbase import pdfmetrics　#PDFの構造を表現
from reportlab.pdfbase.cidfonts import UnicodeCIDFont　#フォントを表現
import reportlab.lib.units as unit　#単位を表現
import reportlab.lib.pagesizes as pagesizes　#用紙サイズを表現

#フォントの登録
pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))

#PDFを作る
pdf = canvas.Canvas("example.pdf",pagesize = pagesizes.A4)#キャンバスの作成
pdf.setFont("HeiseiKakuGo-W5" , 14)#文字を書く
pdf.drawString(10 * unit.mm, 270 * unit.mm, "はじめてのPDF")　#文字の配置　x座標、y座標
pdf.save()
