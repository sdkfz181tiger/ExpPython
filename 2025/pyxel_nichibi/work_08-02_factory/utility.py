import pyxel
import pytweening as tween
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

        # Animation
        self.anim_flg = False
        self.anim_index = 0
        self.anim_key = ""
        self.anims = {}

        # Tween
        self.t_frame = -1
        self.t_points = []

    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.animate() # Animation
        self.tween() # Tween


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
        if -1 < self.t_frame:
            self.t_frame = -1


    #==========
    # Collision
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


    def is_inside(self, x, y):
            if x < self.get_min_x():
                return False
            if y < self.get_min_y():
                return False
            if self.get_max_x() < x:
                return False
            if self.get_max_y() < y:
                return False
            return True


    #==========
    # Animation
    def animate(self):
        if not self.anim_flg:
            return
        anims = self.anims[self.anim_key]
        frame = anims[self.anim_index]
        if frame is None:
            self.anim_flg = False
            self.anim_index = 0
            frame = anims[self.anim_index]
        self.u = frame[0]
        self.v = frame[1]
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


    #==========
    # Tween
    def tween(self):
        if self.t_frame < 0:
            return
        if len(self.t_points) -1 <= self.t_frame:
            self.t_frame = -1
            return
        self.t_frame += 1
        self.x, self.y = self.t_points[self.t_frame]


    def move_to(self, x, y, sec, func):
        t_interval_size = 1 / (30 * sec)
        self.t_frame = 0
        self.t_points = list(func(
                    self.x, self.y, x, y, 
                    t_interval_size))
                