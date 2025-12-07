# coding: utf-8

"""
かじるプログラミング_tkinter
"""

import math
import tkinter

class Sprite:

    def __init__(self, cvs, file, x, y, color="white"):
        # Oval
        self.oval = cvs.create_oval(0, 0, 10, 10,
                                    fill=color, width=0)
        # Image
        self.img, w, h = ImageLoader.load_image(cvs, file, x, y)
        self.x = x
        self.y = y
        self.r = (w if w < h else h) / 2
        self.vx = 0
        self.vy = 0
        self.dead = False

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def move(self, spd, deg):
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad)
        self.vy = spd * math.sin(rad)

    def stop(self):
        self.move(0, 0)
    
    def die(self):
        self.dead = True
        self.stop()

    def is_dead(self):
        return self.dead

    def collide(self, other):
        dst = ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
        if dst < (self.r + other.r): return True
        return False

    def update(self, cvs):

        # Move
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
        # Draw
        cvs.coords(self.oval,
                   self.x - self.r, self.y - self.r,
                   self.x + self.r, self.y + self.r)
            
        # Image
        cvs.coords(self.img, self.x, self.y)
        
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
        
