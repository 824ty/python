#coding:utf-8
import tkinter as tk

#円の座標
x = 400
y = 300

def move():
    global x, y
    #今の円を消す
    canvas.create_oval(x -20, y - 20, x + 20, x + 20, fill="white", width = 0)
    #x座標を動かす
    x = x + 1
    #円を描写する
    canvas.create_oval(x -20, y - 20, x + 20, x + 20, fill="red", width = 0)
    #再びタイマー設定
    root.after(10, move)
# ウィンドウを描く
root = tk.Tk()
root.geometry("600x400")

#Canvasを置く
canvas = tk.Canvas(root, width = 600, height = 400, bg = "white")
canvas.place(x = 0, y = 0)

#タイマーの設定
root.after(10, move)

root.mainloop()
