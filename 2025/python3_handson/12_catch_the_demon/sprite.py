# coding: utf-8

"""
かじるプログラミング_tkinter
"""

import math
import random
import tkinter

# 鬼クラス
class Demon:

    def __init__(self, cvs, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.dead = False
        # 円
        self.oval = cvs.create_oval(x-r, y-r, x+r, y+r,
                                    fill="gray", width=0)
        # イメージ(赤鬼、緑鬼、青鬼)
        self.type = random.choice(("r", "g", "b"))
        
        file_alive = "images/dmn_alive_{}.png".format(self.type)
        self.photo_alive = tkinter.PhotoImage(file=file_alive)
        
        file_dead = "images/dmn_dead_{}.png".format(self.type)
        self.photo_dead = tkinter.PhotoImage(file=file_dead)

        self.image = cvs.create_image(x, y, image=self.photo_alive)

    def update(self, cvs):

        # 座標の更新
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
        # 円の座標を更新
        cvs.coords(self.oval,
                   self.x - self.r, self.y - self.r,
                   self.x + self.r, self.y + self.r)
        
        # イメージの座標を更新
        cvs.coords(self.image, self.x, self.y)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def is_inside(self, x, y):
        if x < self.x - self.r: return False
        if self.x + self.r < x: return False
        if y < self.y - self.r: return False
        if self.y + self.r < y: return False
        return True

    def die(self, cvs):
        self.dead = True
        self.stop()
        # 円の色を更新
        cvs.itemconfig(self.oval, fill="red")
        # イメージの画像を更新
        cvs.itemconfig(self.image, image=self.photo_dead)

    def is_dead(self):
        return self.dead

    def move(self, spd, deg):
        radian = deg * math.pi / 180
        self.vx = spd * math.cos(radian)
        self.vy = spd * math.sin(radian)

    def stop(self):
        self.move(0, 0)

class ImageLoader:

    photos = {} # Cache

    @staticmethod
    def load_photo(file):
        if file not in ImageLoader.photos:
            ImageLoader.photos[file] = tkinter.PhotoImage(file=file)
        photo = ImageLoader.photos[file]
        return photo, photo.width(), photo.height()

    @staticmethod
    def load_image(cvs, file, x=0, y=0):
        photo, w, h = ImageLoader.load_photo(file)
        return cvs.create_image(x, y, image=photo), w, h
        
