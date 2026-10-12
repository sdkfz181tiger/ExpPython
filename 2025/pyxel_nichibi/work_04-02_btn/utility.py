import pyxel
import math

try:
    from js import window
    from pyodide.ffi import JsNull
except Exception:
    window = None

#==========
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
        pyxel.blt(self.x, self.y, 
            0, self.u, self.v, self.w, self.h, 0)

    def move(self, spd, deg):
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad) # x方向の速度
        self.vy = spd * math.sin(rad) # y方向の速度

#==========
# LocalStorageクラス
class LocalStorage:

    @staticmethod
    def set_item(key:str, value:str):
        if window is None:
            return
        print(f"set_str() key:{key}, value:{value}")
        window.localStorage.setItem(key, value)

    @staticmethod
    def get_item(key:str, default=None)->str|None:
        if window is None:
            return None
        print(f"get_str() key:{key}")
        value = window.localStorage.getItem(key)
        if isinstance(value, JsNull):
            return default
        return str(value)
