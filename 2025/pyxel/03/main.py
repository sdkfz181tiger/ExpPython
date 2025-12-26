# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel as px
import random
import sprite

W, H = 160, 120

# App
class App:
    def __init__(self):
        px.init(W, H, title="Hello, Pyxel!!")

        px.images[0].load(0, 0, "images/leaf_01.png")
        px.images[1].load(0, 0, "images/frog/frog_01.png")
        px.run(self.update, self.draw)

    def update(self):
        if px.btnp(px.KEY_Q):
            px.quit()

    def draw(self):
        px.cls(0)
        
        px.text(10, 10, 
            "Hello, Pyxel!!", 
            px.frame_count % 16)

        # Draw something
        px.pset(30, 20, 7)
        px.line(30, 30, 120, 30, 8)

        # Circle
        px.circ(30, 50, 10, 11)
        px.circb(60, 50, 10, 11)

        # Rect
        px.rect(30, 70, 20, 10, 12)
        px.rectb(60, 70, 10, 20, 12)

        # Smile
        self.draw_smile(90, 90, 10)

    def draw_smile(self, x, y, r):
        fill = px.rndi(0, 10)
        border = px.rndi(0, 10)
        hr = r / 2
        px.circ(x, y, r, fill)
        px.line(x-hr, y-hr, x-r/2, y, border)
        px.line(x+hr, y-hr, x+r/2, y, border)
        px.line(x-hr, y+hr, x+r/2, y+hr, border)

def main():
    """ メイン処理 """
    App()

if __name__ == "__main__":
    main()