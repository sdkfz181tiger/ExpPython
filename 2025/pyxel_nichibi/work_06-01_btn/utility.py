import pyxel
import math

#==========
# BaseSpriteクラス
class BaseSprite:

    def __init__(self, x, y, u=0, v=0, w=8, h=8):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.vx = 0
        self.vy = 0
        

    def update(self):
        self.x += self.vx
        self.y += self.vy


    def draw(self):
        pyxel.blt(self.x, self.y, 
            0, self.u, self.v, self.w, self.h, 0)


    def move(self, spd, deg):
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad) # x方向の速度
        self.vy = spd * math.sin(rad) # y方向の速度


    def get_min_x(self):
        return self.x


    def get_min_y(self):
        return self.y


    def get_max_x(self):
        return self.x + self.w


    def get_max_y(self):
        return self.y + self.h


    def collide(self, other):
        if other.get_max_x() < self.get_min_x():
            return False
        if other.get_max_y() < self.get_min_y():
            return False
        if self.get_max_x() < other.get_min_x():
            return False
        if self.get_max_y() < other.get_min_y():
            return False
        return True

#==========
# Buttonクラス
class Button:

    def __init__(self, x, y, title="BTN", on_click = None,
                 bkg_color=3, txt_color=7):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.title = title

        self.p = 3
        self.w = len(title) * 4 + self.p * 4
        self.h = 5 + self.p * 2
        
        self.on_click = on_click
        self.bkg_color = bkg_color
        self.txt_color = txt_color


    def update(self):

        if not pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            return
        
        mx = pyxel.mouse_x
        my = pyxel.mouse_y
        if mx < self.x: return
        if my < self.y: return
        if self.x + self.w < mx: return
        if self.y + self.h < my: return
        print(f"Click:{mx, my}")
        if self.on_click is None: return
        self.on_click(self.title)
        

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h,
                   self.bkg_color)
        pyxel.text(self.x + self.p * 2, self.y + self.p,
                   self.title, self.txt_color)

