#coding = utf-8
import random
import tkinter as tk
import tkinter.messagebox as tmsg

#ボタンがクリックされた時の処理
def ButtonClick():
    b = editbox1.get()   #テキスト入力欄に入力された文字列を取得

    isok = False#　　　　　　　　　　　　　フラグの設定。最初は「False」にして、「NG」ということを表す
    
    if len(b) != 4:#                   len関数は文字列の長さを求めることが出来る
            tmsg.showerror("エラー","4桁の数字を入力してください")
    else:
        kazuok = True#         　　　　kazuokの目的＝4ケタの数字が全部数字かどうかを調べる、　最初は「True」にして「多分OKだろう」と示す
        for i in range(4):#            以下の処理を4回繰り返す：For構文　変数＝i if構文を簡略化した
            if (b[i] < "0") or (b[i] > "9") :#     if構文の場合、「　if (b[0] < "0") or (b[0] > "9"):   print("数字ではありません")　」を0～3まで繰り返すことになる
                tmsg.showerror("エラー","4桁の数字を入力してください")
                kazuok = False#        kazuok=Trueで「数が入力されているだろう」だったが、実際は違かった
                break#                 Forループの中断
        if kazuok :#               全て数字だった
            isok = True#           isokを含めてすべてOK
    if isok :
        hit = 0
        for i in range(4):
            if a[i] ==int(b[i]):
                hit = hit + 1

        blow = 0
        for j in range(4):
            for i in range(4):
                if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])) :
                    blow = blow + 1
                    break# ブローを重複して数えないため

        if hit == 4:
            tmsg.showinfo("当たり", "おめでとうございます。当たりです")
            root.destroy()

        else:
            rirekibox.insert(tk.END, b + " /H:" + str(hit) + " B:" + str(blow) + "/n")

a = [random.randint(0,9),
     random.randint(0,9),#　　　　　　コンピュータが考えたランダムな4ケタの数字の出力
     random.randint(0,9),
     random.randint(0,9)]

#メインのプログラム
#ウィンドウを作る

root =tk.Tk()
root.geometry("600x400")
root.title("数当てゲーム")

rirekibox = tk.Text(root, font = ("Helvetica", 14))
rirekibox.place(x = 400, y = 0, width = 200, height = 400)

#ラベルを作る
label1 = tk.Label(root, text = "数を入力してね", font = ("Helvetica, 14"))
label1.place(x = 20 , y = 20)

#テキストボックスを作る
editbox1 = tk.Entry(width = 4, font = ("Helvetica", 28))
editbox1.place(x = 120, y = 60)

#ボタンを作る
button1 = tk.Button(root, text = "チェック", font =("Helvetica", 14), command = ButtonClick )
button1.place(x = 220, y = 60)

#ウィンドウを表示する
root.mainloop()
