# coding: utf-8

"""
Ball
"""

class Ball:

    def __init__(self, x, y, r, color="white"):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def update(self, cvs):
        cvs.create_oval(self.x - self.r, self.y - self.r,
                        self.x + self.r, self.y + self.r,
                        fill=self.color, width=0)
                               
        
