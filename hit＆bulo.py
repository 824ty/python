# coding:utf-8
import random

a = [random.randint(0,9),
     random.randint(0,9),#　　　　　　コンピュータが考えたランダムな4ケタの数字の出力
     random.randint(0,9),
     random.randint(0,9)]

print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))#　　　　　　　　　テストのための答えを表示する

while True :#　　　　　　　　　　　　　　　4ケタの数字かどうかの判定　(while 条件:)
    isok = False#　　　　　　　　　　　　　フラグの設定。最初は「False」にして、「NG」ということを表す
    while isok == False:#          　　　　=として表現し、以下のwhile構文を繰り返す
        b = input("数を入れてね＞")
        if len(b) != 4:#                   len関数は文字列の長さを求めることが出来る
            print("4桁の数字を入力してください")
        else:#　　　　　　　　　　　　　　 
            kazuok = True#         　　　　kazuokの目的＝4ケタの数字が全部数字かどうかを調べる、　最初は「True」にして「多分OKだろう」と示す
            for i in range(4):#            以下の処理を4回繰り返す：For構文　変数＝i if構文を簡略化した
                if (b[i] < "0") or (b[i] > "9") :#     if構文の場合、「　if (b[0] < "0") or (b[0] > "9"):   print("数字ではありません")　」を0～3まで繰り返すことになる
                    print("4桁の数字を入力してください")
                    kazuok = False#        kazuok=Trueで「数が入力されているだろう」だったが、実際は違かった
                    break#                 Forループの中断
                if kazuok :#               すべて数字だった。
                    isok = True#           isokを含めてすべてOK



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

        print("ヒット" + str(hit))
        print("ブロー" + str(blow))

        if hit == 4:
            print("当たり！")
            break
        
