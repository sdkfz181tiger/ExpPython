# coding: utf-8

"""
かじるプログラミング_tkinter
"""

import math
import random
import sprite
import tkinter

# キャンバスの幅と高さ
W, H = 600, 400

# Font
FONT = ("Arial", 16)

# マウスの座標
mx, my = 0, 0

# Balls
balls = []

# Counter
counter = 0

def init():
    global counter

    # Balls
    for i in range(10):
        x = random.random() * W
        y = random.random() * H
        ball = sprite.Ball(cvs, x, y, 20)
        spd = random.randint(1, 4)
        deg = random.randint(0, 360)
        ball.move(spd, deg) # Move
        balls.append(ball)

    # Counter
    counter = len(balls)
    
def update():
    
    cvs.delete("hud")

    # マウス座標
    msg = "x:{}, y:{}".format(mx, my)
    cvs.create_text(mx, my, text=msg,
                    fill="white", font=FONT, tag="hud")

    # カウンター
    msg = "COUNTER: {}".format(counter)
    cvs.create_text(20, 20, text=msg,
                    fill="white", font=FONT, tag="hud", anchor="nw")

    for ball in balls:
        overlap_area(ball) # Overlap
        ball.update(cvs)

    # Update
    if 0 < counter:
        root.after(30, update)

def overlap_area(obj):
    if obj.x < 0: obj.set_x(W)
    if W < obj.x: obj.set_x(0)
    if obj.y < 0: obj.set_y(H)
    if H < obj.y: obj.set_y(0)

def on_mouse_moved(e):
    global mx, my
    mx, my = e.x, e.y

def on_mouse_clicked(e):
    global counter
    #print("Clicked:", e.x, e.y)

    # Balls
    for ball in balls:
        if ball.is_inside(e.x, e.y):
            if ball.is_dead(): continue
            ball.die(cvs)
            counter = counter - 1 # Counter
            break

def on_key_pressed(e):
    print("Key:", e.keysym)

def on_key_released(e):
    print("Key:", e.keysym)

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)
root.bind("<Motion>", on_mouse_moved) # マウス(Motion)
root.bind("<Button>", on_mouse_clicked) # マウス(Click)
root.bind("<KeyPress>", on_key_pressed) # キーボード(Press)
root.bind("<KeyRelease>", on_key_released) # キーボード(Release)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
init()
update()
root.mainloop()
