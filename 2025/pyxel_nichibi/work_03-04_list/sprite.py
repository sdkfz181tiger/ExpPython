import pyxel
import math

# Spriteクラス
class Sprite:

    def __init__(self, x, y, w, h, color,
                 u=0, v=0):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

        self.u = u
        self.v = v
        self.vx = 0
        self.vy = 0

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)

    def move(self, spd, deg):
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad) # x方向の速度
        self.vy = spd * math.sin(rad) # y方向の速度