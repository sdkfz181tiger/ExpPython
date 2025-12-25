# coding: utf-8

"""
かじるプログラミング_tkinter
"""

import math
import tkinter

class Ball:

    def __init__(self, cvs, x, y, r, color="white"):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.dead = False
        # Oval
        self.oval = cvs.create_oval(x-r, y-r, x+r, y+r,
                                    fill=color, width=0)

    def update(self, cvs):

        # Move
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
        # Draw
        cvs.coords(self.oval,
                   self.x - self.r, self.y - self.r,
                   self.x + self.r, self.y + self.r)

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
        # Oval
        cvs.itemconfig(self.oval, fill="red")

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
        
