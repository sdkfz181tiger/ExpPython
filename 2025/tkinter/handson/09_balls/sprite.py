# coding: utf-8

"""
かじるプログラミング
"""

import math

class Ball:

    def __init__(self, x, y, r,
                 color_alive="white",
                 color_dead="gray"):
        self.x = x
        self.y = y
        self.r = r
        self.color_alive = color_alive
        self.color_dead = color_dead
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

    def collide(self, other):
        dst = ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
        if dst < (self.r + other.r): return True
        return False

    def update(self, cvs):

        # Move
        self.x = self.x + self.vx
        self.y = self.y + self.vy

        # Fill
        fill = self.color_alive if not self.dead else self.color_dead

        # Draw
        cvs.create_oval(self.x - self.r, self.y - self.r,
                        self.x + self.r, self.y + self.r,
                        fill=fill, width=0)
                               
        
