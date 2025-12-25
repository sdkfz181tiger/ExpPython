# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import random
import sprite

# App
class App:
    def __init__(self):
        pyxel.init(240, 160, title="Hello, Pyxel!!")
        pyxel.images[0].load(0, 0, "images/ninja/front_01.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, 
            "Hello, Pyxel!!", 
            pyxel.frame_count % 16)
        pyxel.blt(61, 66, 0, 0, 0, 48, 48)

def main():
    """ メイン処理 """
    App()

if __name__ == "__main__":
    main()