#coding:utf-8
import tkinter as tk

#円の座標
x = 400
y = 300

def move():
    global x, y
    canvas.create_oval(x -20, y - 20, x + 20, x + 20, fill="white", width = 0)
    x = x + 1
    #クリックされた時にそこに描写する
    canvas.create_oval(x -20, y - 20, x + 20, x + 20, fill="red", width = 0)
    root.after(10, move)
# ウィンドウを描く
root = tk.Tk()
root.geometry("600x400")

#Canvasを置く
canvas = tk.Canvas(root, width = 600, height = 400, bg = "white")
canvas.place(x = 0, y = 0)

#イベントを設定する
canvas.bind("<Button-1>", click)

root.mainloop()
