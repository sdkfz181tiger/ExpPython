# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import random
import sprite

W, H = 160, 120

# App
class App:
    def __init__(self):
        pyxel.init(W, H, title="Hello, Pyxel!!")

        pyxel.images[0].load(0, 0, "images/leaf_01.png")
        pyxel.images[1].load(0, 0, "images/frog/frog_01.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        
        pyxel.text(10, 10, 
            "Hello, Pyxel!!", 
            pyxel.frame_count % 16)

        pyxel.blt(W/2-32, H/2, 0, 0, 0, 20, 10)
        pyxel.blt(W/2+32, H/2, 1, 0, 0, 20, 24)

def main():
    """ メイン処理 """
    App()

if __name__ == "__main__":
    main()