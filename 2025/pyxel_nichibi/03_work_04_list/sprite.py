import pyxel
import math

# Spriteクラス
class Sprite:

    def __init__(self, x, y, size, color):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.size = size
        self.color = color

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pyxel.circ(self.x, self.y, self.size, self.color)

    def move(self, spd, deg):
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad) # x方向の速度
        self.vy = spd * math.sin(rad) # y方向の速度