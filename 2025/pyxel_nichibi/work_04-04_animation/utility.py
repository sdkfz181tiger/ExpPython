import pyxel
import math

#==========
# Spriteクラス
class Sprite:

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

        self.anim_flg = False
        self.anim_index = 0
        self.anim_key = ""
        self.anims = {}

    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.animate()


    def draw(self):
        pyxel.blt(self.x, self.y, 0,
            self.u, self.v, self.w, self.h, 0)


    def move(self, spd, deg):
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad) # x方向の速度
        self.vy = spd * math.sin(rad) # y方向の速度


    def stop(self):
        self.vx = 0
        self.vy = 0


    def animate(self):
        if not self.anim_flg:
            return
        anims = self.anims[self.anim_key]
        self.u = anims[self.anim_index][0]
        self.v = anims[self.anim_index][1]
        if pyxel.frame_count % 3 == 0:
            self.anim_index += 1
        if len(anims) <= self.anim_index:
            self.anim_index = 0


    def set_animation(self, key, animations):
        self.anims[key] = animations


    def start_animation(self, key):
        if not key in self.anims:
            return
        self.anim_flg = True
        self.anim_index = 0
        self.anim_key = key


    def stop_animation(self):
        self.anim_flg = False


    def toggle_animation(self):
        self.anim_flg = not self.anim_flg

