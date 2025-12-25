# coding: utf-8

"""
Ball
"""

import math

class Ball:

    def __init__(self, x, y, r, color="white"):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.color = color

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_speed(self, spd, deg):
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad)
        self.vy = spd * math.sin(rad)

    def update(self, cvs):

        # Move
        self.x = self.x + self.vx
        self.y = self.y + self.vy

        # Draw
        cvs.create_oval(self.x - self.r, self.y - self.r,
                        self.x + self.r, self.y + self.r,
                        fill=self.color, width=0)
                               
        
