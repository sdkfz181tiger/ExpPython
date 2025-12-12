# coding: utf-8

"""
かじるプログラミング_tkinter
"""

import math
import random
import sprite
import tkinter

# フレーム
F_RATE = 30 # 1秒間に実行するフレーム回数
F_INTERVAL = 1000 / F_RATE # 1フレームの間隔

# キャンバスの幅と高さ
W, H = 480, 320

# フォント
FONT = ("Arial", 16)

# マウスの座標
mx, my = 0, 0

# 背景画像とイメージ
bg_photo, bg_image = None, None

# 鬼軍団の数
TOTAL_DEMONS = 10

# 鬼軍団
demons = []

# 鬼カウンタ
counter = TOTAL_DEMONS

# タイマー
timer = F_RATE * 30 # 残り時間(30秒)

def init():
    """ 初期化関数 """
    global bg_photo, bg_image

    # 背景
    bg_photo = tkinter.PhotoImage(file="images/bg_jigoku.png")
    bg_image = cvs.create_image(W/2, H/2, image=bg_photo)

    # 鬼軍団
    for i in range(TOTAL_DEMONS):
        x = random.random() * W
        y = random.random() * H
        demon = sprite.DemonSprite(cvs, x, y, 20)
        spd = random.randint(1, 4)
        deg = random.randint(0, 360)
        demon.move(spd, deg) # ランダムで移動
        demons.append(demon)
    
def update():
    """ 更新関数 """
    global timer
    
    cvs.delete("hud")

    # マウス座標を描画
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # 鬼カウンタを描画
    msg = "残り鬼軍団: {}".format(counter)
    cvs.create_text(20, 20, text=msg,
                    fill="white", font=FONT, tag="hud", anchor="nw")

    # タイマーを描画
    msg = "残り時間: {:.2f}秒".format(timer / F_RATE)
    cvs.create_text(W-20, 20, text=msg,
                    fill="white", font=FONT, tag="hud", anchor="ne")

    # 鬼軍団
    for demon in demons:
        overlap_area(demon) # 画面外判定
        demon.update(cvs)

    # タイマー
    timer = timer - 1

    # 画面更新
    if 0 < counter and 0 <= timer:
        root.after(F_INTERVAL, update)
    else:
        # ゲーム判定
        msg = "GAME CLEAR" if counter <= 0 else "GAME OVER"
        cvs.create_text(W/2, H-40, text=msg,
                        fill="white", font=FONT, tag="hud")

def overlap_area(obj):
    if obj.x < 0: obj.set_x(W)
    if W < obj.x: obj.set_x(0)
    if obj.y < 0: obj.set_y(H)
    if H < obj.y: obj.set_y(0)

def on_mouse_clicked(e):
    global counter
    #print("Clicked:", e.x, e.y)

    # 鬼軍団
    for demon in demons:
        if demon.is_inside(e.x, e.y):
            if demon.is_dead(): continue
            demon.die(cvs)
            counter = counter - 1 # 鬼カウンタをマイナス1
            break

def on_mouse_moved(e):
    global mx, my
    mx, my = e.x, e.y

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)
root.bind("<Button>", on_mouse_clicked) # マウス(Click)
root.bind("<Motion>", on_mouse_moved) # マウス(Motion)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
init()
update()
root.mainloop()
